"""Collect results/retrieval/<split>/*/summary.json into one Markdown comparison table.

    python scripts/compare_retrieval.py --split dev     # -> results/retrieval/dev/comparison.md
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=["dev", "test"])
    args = ap.parse_args()
    base = ROOT / "results" / "retrieval" / args.split
    rows = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(base.glob("*/summary.json"))]
    rows.sort(key=lambda s: (not s["config"]["use_user_filter"], s["run"]))
    n = rows[0]["metrics"]["hit1"]["N"]
    lines = [f"# Retrieval comparison — {args.split} ({n} answerable questions)", "",
             "Same corpus (Day 6 strategy B, 118 chunks), questions, gold and hit rule (src/evidence.py). "
             "Context = top-3 packed into the char budget. Unanswerable questions are not in the denominator.", "",
             "| Run | Method | User filter | Hit@1 | Evidence Hit@3 | Context Evidence | Hit@10 | MRR@10 "
             "| Avg context chars | Embedding API calls | Misses@3 |",
             "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for s in rows:
        m, c = s["metrics"], s["config"]
        api = "0 (local)" if s["method"].startswith("bm25") else "1 / query (cached on rerun)"
        lines.append(f"| {s['run']} | {s['method']} | {'yes' if c['use_user_filter'] else 'no'} "
                     f"| {m['hit1']['str']} | {m['hit3']['str']} | {m['context_evidence']['str']} "
                     f"| {m['hit10']['str']} | {m['mrr10']:.3f} | {m['avg_context_chars']} | {api} "
                     f"| {', '.join(m['misses_at_3']) or '—'} |")
    lines += ["", f"Budget: {rows[0]['config']['budget_chars']} chars; embedding "
              f"{rows[0]['config']['embedding']}. Latency is not compared here: dense/hybrid reruns read "
              "query embeddings from cache (a fresh Gemini query embedding took ~360 ms/query in the first run)."]
    out = base / "comparison.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[4:4 + len(rows) + 2]))
    print(f"-> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
