"""Evaluate retrieval methods on one split (answerable questions only).

    python scripts/eval_retrieval.py --method dense --split dev
    python scripts/eval_retrieval.py --method dense --split dev --no-filter

Metrics (same hit rule for every method, src/evidence.py):
  Hit@1, Evidence Hit@3      gold evidence in the top-1 / top-3 results
  Hit@10, MRR@10             extra: where the evidence sits when top-3 misses
  Context Evidence Rate      gold evidence inside the packed context (top-3, char budget)
Unanswerable cases are not in the denominator (BENCHMARK.md).
Gold is used only to score results AFTER retrieval; the retriever sees question + user filter.
Output: results/retrieval/<split>/<run-name>/{summary.json, traces.json}
"""
from __future__ import annotations

import argparse
import hashlib
import json
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.context import pack_context  # noqa: E402  dedupe, keep chunks that fit the budget
from src.day6_index import Day6Store, DenseRetriever, GeminiQueryEmbedder, load_config  # noqa: E402
from src.evidence import evidence_hit  # noqa: E402
from src.hybrid import RRFRetriever  # noqa: E402
from src.lexical import BM25Retriever  # noqa: E402

DATA = ROOT / "data" / "day6"
CACHE = ROOT / "results" / "cache" / "query_embeddings.json"


class CachedEmbedder:
    """Query embeddings cached on disk by (model, dims, task, text): one API call per new query."""

    def __init__(self, embedder: GeminiQueryEmbedder) -> None:
        self.inner = embedder
        self.key_prefix = f"{embedder.model}|{embedder.dimensions}|{embedder.task}|"
        self.cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
        self.hits = self.misses = 0

    def _key(self, text: str) -> str:
        return hashlib.sha256((self.key_prefix + text).encode()).hexdigest()

    def embed_query(self, text: str) -> list[float]:
        key = self._key(text)
        if key in self.cache:
            self.hits += 1
        else:
            self.misses += 1
            self.cache[key] = self.inner.embed_query(text)
            CACHE.parent.mkdir(parents=True, exist_ok=True)
            CACHE.write_text(json.dumps(self.cache), encoding="utf-8")
        return self.cache[key]


def build_retriever(method: str, cfg: dict, store: Day6Store):
    """Returns (retriever, embedder or None). Lexical methods make no API call."""
    if method == "dense":
        embedder = CachedEmbedder(GeminiQueryEmbedder(cfg))
        return DenseRetriever(embedder, store), embedder
    if method in ("bm25", "bm25-bigram"):
        chunks = json.loads((DATA / "chunks.json").read_text(encoding="utf-8"))
        return BM25Retriever(chunks, tokenizer="syllable" if method == "bm25" else "bigram"), None
    if method == "hybrid":
        dense, embedder = build_retriever("dense", cfg, store)
        bm25, _ = build_retriever("bm25-bigram", cfg, store)
        return RRFRetriever({"dense": dense, "bm25-bigram": bm25}, k=60, candidates=20), embedder
    raise ValueError(f"unknown method {method}")


def evaluate(retriever, questions: list[dict], *, use_filter: bool, top_k: int, budget: int) -> list[dict]:
    traces = []
    for q in questions:
        filters = q.get("filter") if use_filter else None
        t0 = time.perf_counter()
        results = retriever.search(q["question"], filters=filters, top_k=top_k)
        latency_ms = (time.perf_counter() - t0) * 1000
        context, context_ids = pack_context(results[:3], budget=budget)
        flags = [evidence_hit(r, q["gold"]) for r in results]
        first = next((i + 1 for i, f in enumerate(flags) if f), None)
        traces.append({
            "query_id": q["id"], "split": q["split"], "type": q.get("type"), "question": q["question"],
            "filter": filters,
            "results": [{"rank": i + 1, "id": r["id"], "score": round(r["score"], 4), "page": r["page"],
                         "page_end": r["metadata"]["page_end"], "chapter": r["metadata"]["chapter"],
                         "article": r["metadata"]["article"], "hit": f,
                         **({"component_ranks": r["component_ranks"]} if "component_ranks" in r else {})}
                        for i, (r, f) in enumerate(zip(results, flags))],
            "first_hit_rank": first,
            "hit1": first == 1, "hit3": first is not None and first <= 3, "hit10": first is not None,
            "context_ids": context_ids, "context_chars": len(context),
            "context_hit": any(f and r["id"] in context_ids for r, f in zip(results, flags)),
            "latency_ms": round(latency_ms, 1),
            "gold_pages": [g["page"] for g in q["gold"]],  # added after retrieval, for reading traces
        })
    return traces


def summarize(traces: list[dict]) -> dict:
    n = len(traces)

    def rate(key: str) -> dict:
        k = sum(t[key] for t in traces)
        return {"n": k, "N": n, "rate": round(k / n, 3), "str": f"{k}/{n}"}

    return {"hit1": rate("hit1"), "hit3": rate("hit3"), "context_evidence": rate("context_hit"),
            "hit10": rate("hit10"),
            "mrr10": round(sum(1 / t["first_hit_rank"] for t in traces if t["first_hit_rank"]) / n, 3),
            "misses_at_3": [t["query_id"] for t in traces if not t["hit3"]],
            "not_rank1": [t["query_id"] for t in traces if not t["hit1"]],
            "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces)),
            "median_latency_ms": round(statistics.median(t["latency_ms"] for t in traces), 1)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--method", required=True, choices=["dense", "bm25", "bm25-bigram", "hybrid"])
    ap.add_argument("--split", required=True, choices=["dev", "test"])
    ap.add_argument("--no-filter", action="store_true", help="ignore the user-provided chapter filter")
    ap.add_argument("--top-k", type=int, default=10, help="results fetched (metrics use top-1/3/10)")
    ap.add_argument("--budget", type=int, default=3000, help="context budget in characters (incl. source header)")
    ap.add_argument("--name", help="run name (default: method[-nofilter])")
    args = ap.parse_args()

    cfg = load_config()
    questions = [q for q in json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
                 if q["split"] == args.split]
    name = args.name or args.method + ("-nofilter" if args.no_filter else "")
    with Day6Store(cfg) as store:
        retriever, embedder = build_retriever(args.method, cfg, store)
        t0 = time.perf_counter()
        traces = evaluate(retriever, questions, use_filter=not args.no_filter, top_k=args.top_k, budget=args.budget)
        total_s = time.perf_counter() - t0

    summary = {
        "run": name, "method": args.method, "split": args.split,
        "run_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "config": {"top_k_fetched": args.top_k, "context_from": "top-3", "budget_chars": args.budget,
                   "use_user_filter": not args.no_filter, "chunks": "Day 6 strategy B (118)",
                   "embedding": f"{cfg['embedding']['model']} {cfg['embedding']['dimensions']}d"},
        "metrics": summarize(traces),
        "cost": {"embedding_api_calls": getattr(embedder, "misses", 0),
                 "embedding_cache_hits": getattr(embedder, "hits", 0), "total_seconds": round(total_s, 2)},
    }
    out = ROOT / "results" / "retrieval" / args.split / name
    out.mkdir(parents=True, exist_ok=True)
    (out / "traces.json").write_text(json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    m = summary["metrics"]
    print(f"[{args.split}] {name}: Hit@1 {m['hit1']['str']} | Hit@3 {m['hit3']['str']} | "
          f"Context {m['context_evidence']['str']} | Hit@10 {m['hit10']['str']} | MRR@10 {m['mrr10']} | "
          f"ctx {m['avg_context_chars']} chars | {m['median_latency_ms']} ms/query")
    print(f"  misses@3: {m['misses_at_3']} | not rank-1: {m['not_rank1']}")
    print(f"  API calls {summary['cost']['embedding_api_calls']}, cache hits {summary['cost']['embedding_cache_hits']}"
          f" -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
