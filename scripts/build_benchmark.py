"""Convert the Day 6 benchmark to the Day 7 schema and add unanswerable cases.

    python scripts/build_benchmark.py

Inputs : $DAY6_STARTER_DIR/data/benchmark.json, data/day6/chunks.json, data/day6/unanswerable.json
Outputs: data/day6/questions.json  answerable questions with gold (for evaluation only)
         data/day6/cases.json      every case WITHOUT gold/answer (what the agent may see)

Conversion: gold_page [p] -> gold[].page = p; evidence = the exact span of the Day 6
evidence_quote inside the matching chunk (same words, chunk's own line breaks);
the original quote is kept in evidence_quote_day6. Every gold item must match
at least one chunk under src/evidence.py rules or the script fails.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.day6_index import load_config  # noqa: E402  (also loads .env)
from src.evidence import evidence_in_chunk, exact_span, normalize, strict_starter_hit  # noqa: E402

DATA = ROOT / "data" / "day6"


def convert(q: dict, chunks: list[dict]) -> dict:
    if len(q["gold_page"]) != 1:
        raise ValueError(f"{q['id']}: expected one gold page, got {q['gold_page']}")
    page = q["gold_page"][0]
    base = {"source_id": q["gold_source_id"], "page": page, "evidence": q["evidence_quote"]}
    matches = [c for c in chunks if evidence_in_chunk(c, base)]
    if not matches:
        raise ValueError(f"{q['id']}: evidence not found in any chunk on page {page}")
    spans = {exact_span(c["text"], q["evidence_quote"]) for c in matches}
    if None in spans or len(spans) != 1:
        raise ValueError(f"{q['id']}: cannot recover one exact evidence span: {spans}")
    out = {"id": q["id"], "split": q["split"], "type": q.get("type"), "question": q["question"],
           "answerable": True, "expected_behavior": "search_and_answer",
           "expected_answer": q["expected_answer"],
           "gold": [{**base, "evidence": spans.pop()}],
           "evidence_quote_day6": q["evidence_quote"]}
    if q.get("filter"):
        out["filter"] = q["filter"]
        if q.get("filter_note"):
            out["filter_note"] = q["filter_note"]
    return out


def main() -> None:
    load_config()
    day6 = os.getenv("DAY6_STARTER_DIR")
    if not day6:
        sys.exit("FAIL: DAY6_STARTER_DIR missing in .env")
    raw = json.loads((Path(day6) / "data" / "benchmark.json").read_text(encoding="utf-8"))["questions"]
    chunks = json.loads((DATA / "chunks.json").read_text(encoding="utf-8"))
    unanswerable = json.loads((DATA / "unanswerable.json").read_text(encoding="utf-8"))

    questions = [convert(q, chunks) for q in raw]
    ids = [q["id"] for q in questions] + [u["id"] for u in unanswerable]
    if len(set(ids)) != len(ids):
        sys.exit("FAIL: duplicate question IDs")
    for u in unanswerable:
        if u.get("answerable") is not False or u.get("split") not in ("dev", "test") or not u.get("absence_reason"):
            sys.exit(f"FAIL: {u.get('id')}: invalid unanswerable case")

    # The agent input: question + user-provided filter only; never gold or expected answers.
    cases = [{k: q[k] for k in ("id", "split", "question", "answerable", "expected_behavior", "filter") if k in q}
             for q in questions + unanswerable]

    (DATA / "questions.json").write_text(json.dumps(questions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "cases.json").write_text(json.dumps(cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts = Counter((c["split"], c["answerable"]) for c in cases)
    print("dev : answerable %d, unanswerable %d" % (counts["dev", True], counts["dev", False]))
    print("test: answerable %d, unanswerable %d" % (counts["test", True], counts["test", False]))
    strict = [q["id"] for q in questions if any(strict_starter_hit(c, q["gold"]) for c in chunks)]
    cross = [q["id"] for q in questions if q["id"] not in strict]
    print(f"gold matches a chunk (src/evidence.py): {len(questions)}/{len(questions)}")
    print(f"starter baseline hit() would accept: {len(strict)}/{len(questions)}; "
          f"evidence on chunk page_end (cross-page chunk): {cross}")
    leaked = [c["id"] for c in cases if any(normalize(q["expected_answer"]) in json.dumps(c, ensure_ascii=False)
                                            for q in questions)]
    if leaked:
        sys.exit(f"FAIL: expected answers leaked into cases: {leaked}")


if __name__ == "__main__":
    main()
