"""Automatic checks for an agent run + a review sheet and label template for manual grading.

    python scripts/score_agent.py --split dev --run baseline-dense

Reads results/agent/<split>/<run>/traces.json and the gold files (used here only, after the run).
Writes into the same folder:
  auto_metrics.json  computed by code, no judgement:
                     - Context Evidence Rate: gold evidence inside the FINAL context sent to the model
                     - cited-evidence rate: some cited chunk contains the gold evidence (a hint only;
                       a citation can support a claim without containing the gold sentence)
                     - tool use, status counts, false abstentions, searches, tokens, cost, time
  review_sheet.md    per case: question, expected answer, gold evidence, agent answer, full text
                     of every cited chunk -> read this to grade
  reviews.json       labels in starter/agent_metrics.py format. Created with null labels if
                     missing; existing labels are never overwritten (new cases are appended).
Then aggregate the human labels with starter/agent_metrics.py (see --help of that script).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.evidence import evidence_hit  # noqa: E402

DATA = ROOT / "data" / "day6"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--split", required=True, choices=["dev", "test"])
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    run_dir = ROOT / "results" / "agent" / args.split / args.run
    traces = load(run_dir / "traces.json")
    gold = {q["id"]: q for q in load(DATA / "questions.json")}
    unans = {u["id"]: u for u in load(DATA / "unanswerable.json")}
    chunks = {c["id"]: c for c in load(DATA / "chunks.json")}
    summary = load(run_dir / "summary.json")

    rows = []
    for t in traces:
        qid = t["query_id"]
        answerable = qid in gold
        row = {"query_id": qid, "answerable": answerable, "status": t["status"], "n_searches": t["n_searches"],
               "citations": t["citations"], "stop_reason": t["stop_reason"]}
        if answerable and t["status"] != "error":
            g = gold[qid]["gold"]
            ctx = [chunks[i] for i in t["final_context_ids"]]
            row["context_evidence"] = any(evidence_hit(c, g) for c in ctx)
            row["evidence_found_by_any_search"] = any(
                evidence_hit(chunks[r["id"]], g) for e in t["events"] if e["event"] == "search" for r in e["results"])
            row["cited_has_evidence"] = any(evidence_hit(chunks[i], g) for i in t["citations"])
        rows.append(row)

    ok = [r for r in rows if r["status"] != "error"]
    ans = [r for r in ok if r["answerable"]]
    una = [r for r in ok if not r["answerable"]]

    def frac(n: int, d: int) -> str:
        return f"{n}/{d}" + (f" ({n / d:.0%})" if d else " (không áp dụng)")

    metrics = {
        "run": args.run, "split": args.split, "config": summary["config"],
        "errors": frac(len(rows) - len(ok), len(rows)),
        "tool_use": frac(sum(r["n_searches"] > 0 for r in ok), len(ok)),
        "searches_per_case": summary["tool_use"]["searches_per_case"],
        "context_evidence_rate": frac(sum(r["context_evidence"] for r in ans), len(ans)),
        "evidence_retrieved_in_any_search": frac(sum(r["evidence_found_by_any_search"] for r in ans), len(ans)),
        "answered_with_citation": frac(sum(r["status"] == "answered" and bool(r["citations"]) for r in ok),
                                       sum(r["status"] == "answered" for r in ok)),
        "cited_chunk_has_gold_evidence (hint)": frac(sum(r["cited_has_evidence"] for r in ans if r["status"] == "answered"),
                                                     sum(r["status"] == "answered" for r in ans)),
        "abstained_on_unanswerable": frac(sum(r["status"] == "abstain" for r in una), len(una)),
        "false_abstention_on_answerable": frac(sum(r["status"] == "abstain" for r in ans), len(ans)),
        "lost_in_context (retrieved but not in final context)": [
            r["query_id"] for r in ans if r["evidence_found_by_any_search"] and not r["context_evidence"]],
        "llm_calls": summary["llm_calls"], "tokens": summary["tokens"], "llm_cost_usd": summary.get("llm_cost_usd"),
        "seconds": summary["seconds"], "per_case": rows,
    }
    (run_dir / "auto_metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Review sheet: everything a human grader needs, one section per case.
    lines = [f"# Review sheet — {args.split} / {args.run}", "",
             "Chấm theo BENCHMARK.md: `answer_grade` 0 = sai/thiếu evidence, 1 = đúng một phần, 2 = đúng và đủ "
             "(từ chối câu có đáp án = 0); `citation_support`: mỗi citation có thực sự hỗ trợ ý được trích không; "
             "`abstention_correct`: câu thiếu evidence có được từ chối mà không thêm khẳng định vô căn cứ không.", ""]
    for t, r in zip(traces, rows):
        qid = t["query_id"]
        lines += [f"## {qid} — {t['status']} ({r['n_searches']} search, filter={t['filter']})", "",
                  f"**Câu hỏi:** {t['question']}", ""]
        if r["answerable"]:
            g = gold[qid]
            lines += [f"**Đáp án chuẩn:** {g['expected_answer']}", "",
                      f"**Evidence gold (trang {g['gold'][0]['page']}):** {g['evidence_quote_day6']}", "",
                      f"*Tự động:* context có evidence = {r.get('context_evidence')}, "
                      f"chunk được trích có evidence = {r.get('cited_has_evidence')}", ""]
        else:
            lines += [f"**Câu thiếu evidence.** Lý do: {unans[qid]['absence_reason']}", ""]
        lines += ["**Truy vấn của agent:** " + " | ".join(t["queries"]), "",
                  "**Câu trả lời của agent:**", "", "> " + (t["answer"] or "").replace("\n", "\n> "), ""]
        reason = next((e.get("reason") for e in t["events"] if e["event"] == "abstain"), None)
        if reason:
            lines += [f"**Lý do từ chối (model):** {reason}", ""]
        for cid in t["citations"]:
            c = chunks[cid]
            m = c["metadata"]
            lines += [f"<details><summary>[{cid}] trang {c['page']}-{m['page_end']}, Điều {m['article']}</summary>",
                      "", "```text", c["text"], "```", "</details>", ""]
    (run_dir / "review_sheet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Label template; keep any labels already written by the grader.
    rev_path = run_dir / "reviews.json"
    existing = {r["query_id"]: r for r in load(rev_path)} if rev_path.exists() else {}
    reviews = []
    for t, r in zip(traces, rows):
        if t["status"] == "error":
            continue  # provider errors need no label (reported separately)
        if t["query_id"] in existing:
            reviews.append(existing[t["query_id"]])
            continue
        item = {"query_id": t["query_id"], "citation_support": [None] * len(t["citations"]), "reason": ""}
        item["answer_grade" if r["answerable"] else "abstention_correct"] = None
        reviews.append(item)
    rev_path.write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for k in ("tool_use", "context_evidence_rate", "evidence_retrieved_in_any_search", "answered_with_citation",
              "cited_chunk_has_gold_evidence (hint)", "abstained_on_unanswerable", "false_abstention_on_answerable",
              "lost_in_context (retrieved but not in final context)", "llm_cost_usd"):
        print(f"{k:55} {metrics[k]}")
    print(f"-> {run_dir.relative_to(ROOT)}/auto_metrics.json, review_sheet.md, reviews.json "
          f"({len(existing)} existing labels kept)")


if __name__ == "__main__":
    main()
