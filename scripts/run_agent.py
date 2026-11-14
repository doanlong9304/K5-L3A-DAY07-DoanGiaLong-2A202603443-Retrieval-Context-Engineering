"""Run the Gemini agent on benchmark cases and save full traces.

    python scripts/run_agent.py --split dev --retriever dense --run baseline-dense
    python scripts/run_agent.py --split dev --retriever dense --run smoke --ids q01,u01

Input : data/day6/cases.json (question + user filter only; no gold, no expected answer)
Output: results/agent/<split>/<run>/traces.json  one record per case (starter/agent_metrics.py format
        + full events, context, usage), and summary.json (config, status counts, tool use, tokens, time).
Answer quality, citation support and abstention correctness are labelled by hand afterwards.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from collections import Counter
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.agent import AgentConfig, make_controller, run_agent  # noqa: E402
from src.day6_index import Day6Store, load_config  # noqa: E402
from scripts.eval_retrieval import build_retriever  # noqa: E402

DATA = ROOT / "data" / "day6"
# USD per 1M tokens (input, output). Claude: Anthropic list prices; output includes thinking.
PRICES = {"claude-opus-5-5": (4.0, 20.0), "claude-sonnet-5-5": (2.0, 10.0), "claude-haiku-5-5": (0.10, 0.50)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--split", required=True, choices=["dev", "test"])
    ap.add_argument("--retriever", required=True, choices=["dense", "bm25-bigram", "hybrid"])
    ap.add_argument("--run", required=True, help="run name, e.g. baseline-dense")
    ap.add_argument("--model", default="claude-opus-5-5", help="claude-* uses the Anthropic API, else Gemini")
    ap.add_argument("--max-searches", type=int, default=3)
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--budget", type=int, default=3000, help="context budget in characters")
    ap.add_argument("--context-policy", default="first", choices=["first", "recent"],
                    help="context packing order across searches (first = starter/baseline)")
    ap.add_argument("--ids",help="comma-separated case IDs (smoke runs)")
    ap.add_argument("--resume", action="store_true", help="keep finished cases in the run folder, rerun the rest")
    ap.add_argument("--pause",type=float, default=0.0, help="seconds between cases (free-tier rate limits)")
    args = ap.parse_args()

    cfg_index = load_config()
    cases = [c for c in json.loads((DATA / "cases.json").read_text(encoding="utf-8")) if c["split"] == args.split]
    if args.ids:
        wanted = args.ids.split(",")
        cases = [c for c in cases if c["id"] in wanted]
    agent_cfg = AgentConfig(model=args.model, max_searches=args.max_searches, top_k=args.top_k, budget=args.budget,
                            context_policy=args.context_policy)
    controller = make_controller(args.model, agent_cfg.temperature)

    out = ROOT / "results" / "agent" / args.split / args.run
    out.mkdir(parents=True, exist_ok=True)
    trace_file = out / "traces.json"
    done: dict[str, dict] = {}
    if args.resume and trace_file.exists():  # keep finished cases; rerun missing and errored ones
        done = {t["query_id"]: t for t in json.loads(trace_file.read_text(encoding="utf-8"))
                if t["status"] != "error"}
        print(f"resume: {len(done)} finished cases kept")

    def save() -> list[dict]:
        ordered = [done[c["id"]] for c in cases if c["id"] in done] + \
                  [t for t in errored.values() if t["query_id"] not in done]
        trace_file.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return ordered

    errored: dict[str, dict] = {}
    with Day6Store(cfg_index) as store:
        retriever, embedder = build_retriever(args.retriever, cfg_index, store)
        todo = [c for c in cases if c["id"] not in done]
        for i, case in enumerate(todo, 1):
            # Only the question and the user-provided filter reach the agent.
            result = run_agent(case["question"], controller, retriever, agent_cfg, filters=case.get("filter"))
            trace = {"query_id": case["id"], "split": case["split"], "question": case["question"],
                     "filter": case.get("filter"), "model": args.model, "retriever": args.retriever, **result}
            (errored if result["status"] == "error" else done)[case["id"]] = trace
            save()  # written after every case: an interruption loses nothing
            print(f"[{i}/{len(todo)}] {case['id']}: {result['status']:8} searches={result['n_searches']} "
                  f"cites={result['citations']} {result['seconds']}s retries={result['usage']['llm_retries']}"
                  + (f" ERROR {result.get('error', '')[:120]}" if result["status"] == "error" else ""))
            if result["status"] == "error" and "PerDay" in result.get("error", ""):
                print("Daily quota exhausted: stopping. Rerun later with --resume.")
                break
            if args.pause and i < len(todo):
                time.sleep(args.pause)
    traces = save()

    ok = [t for t in traces if t["status"] != "error"]
    tok = {k: sum(t["usage"][k] for t in traces) for k in ("input_tokens", "output_tokens", "thinking_tokens")}
    summary = {
        "run": args.run, "split": args.split,
        "run_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "config": {**asdict(agent_cfg), "retriever": args.retriever, "context_budget_unit": "characters",
                   "filter": "user-provided chapter filter from cases.json when present"},
        "cases": len(traces),
        "status": dict(Counter(t["status"] for t in traces)),
        "stop_reasons": dict(Counter(t["stop_reason"] for t in traces)),
        "tool_use": {"cases_with_search": sum(t["n_searches"] > 0 for t in ok), "N": len(ok),
                     "searches_per_case": dict(sorted(Counter(t["n_searches"] for t in ok).items()))},
        "tokens": tok, "llm_calls": sum(t["usage"]["llm_calls"] for t in traces),
        "llm_cost_usd": round(tok["input_tokens"] / 1e6 * PRICES[args.model][0]
                              + (tok["output_tokens"] + tok["thinking_tokens"]) / 1e6 * PRICES[args.model][1], 4)
        if args.model in PRICES else None,
        "price_note": "list price USD per 1M tokens (input, output) as of 2026-11; free tier would be 0",
        "served_models": sorted({m for t in traces for m in t["usage"].get("served_models", [])}),
        "embedding_api_calls": getattr(embedder, "misses", 0) if embedder else 0,
        "seconds": {"median_per_case": round(statistics.median(t["seconds"] for t in traces), 2) if traces else None,
                    "total": round(sum(t["seconds"] for t in traces), 1)},
        "errors": [{"query_id": t["query_id"], "error": t.get("error")} for t in traces if t["status"] == "error"],
    }
    summary["complete"] = len([t for t in traces if t["status"] != "error"]) == len(cases)
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("status", "stop_reasons", "tool_use", "tokens", "seconds")},
                     ensure_ascii=False))
    print("->", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
