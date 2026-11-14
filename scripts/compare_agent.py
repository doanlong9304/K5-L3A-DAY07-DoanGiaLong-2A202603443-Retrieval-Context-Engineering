"""Compare agent runs of one split: human-label metrics + automatic metrics + cost/time.

    python scripts/compare_agent.py --split dev --runs baseline-dense ctx-recent-dense
    -> results/agent/<split>/comparison.md

Each run folder needs summary.json, auto_metrics.json (scripts/score_agent.py) and
agent_metrics.json (starter/agent_metrics.py over the reviewed labels).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=["dev", "test"])
    ap.add_argument("--runs", nargs="+", required=True)
    args = ap.parse_args()
    base = ROOT / "results" / "agent" / args.split
    head = ("| Run | Retriever | Context | Grounded (TB /2) | 2 / 1 / 0 | Citation hợp lệ | Từ chối đúng "
            "| Từ chối nhầm | Context Evidence | Search/câu | LLM calls | Token vào / ra | Chi phí | Trung vị s/câu | Nhãn |")
    lines = [f"# So sánh cấu hình agent — {args.split}", "", head, "|" + "---|" * 15]
    for run in args.runs:
        d = base / run
        s, a, m = load(d / "summary.json"), load(d / "auto_metrics.json"), load(d / "agent_metrics.json")
        g = m["grounded_answer"]
        reviewers = {r.get("reviewer", "") for r in load(d / "reviews.json")}
        status = "nháp" if any("DRAFT" in r for r in reviewers) else "đã duyệt"
        searches = ", ".join(f"{k}:{v}" for k, v in s["tool_use"]["searches_per_case"].items())
        lines.append(
            f"| {run} | {s['config']['retriever']} | {s['config'].get('context_policy', 'first')} "
            f"| {g['mean']:.3f} | {g['2']} / {g['1']} / {g['0']} "
            f"| {m['citation_validity']['n']}/{m['citation_validity']['N']} | {m['abstention']['n']}/{m['abstention']['N']} "
            f"| {m['false_abstention']['n']}/{m['false_abstention']['N']} | {a['context_evidence_rate']} | {searches} "
            f"| {s['llm_calls']} | {s['tokens']['input_tokens']:,} / {s['tokens']['output_tokens']:,} "
            f"| ${s['llm_cost_usd']:.2f} | {s['seconds']['median_per_case']} | {status} |")
    lines += ["", "Search/câu: số lượt search → số câu. Chi phí theo giá niêm yết claude-opus-5-5 ($4 / $20 mỗi 1M token)."]
    out = base / "comparison.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("->", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
