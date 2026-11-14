"""Export the Day 6 strategy-B chunks from pgvector to the Day 7 chunk JSON format.

    python scripts/export_day6.py            # -> data/day6/chunks.json

Read-only: text and metadata come straight from the Day 6 table (vectors stay in
the database). Output: JSON array of {id, text, source_id, source, page, metadata}.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.day6_index import Day6Store, load_config  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--output", type=Path, default=ROOT / "data" / "day6" / "chunks.json")
    args = ap.parse_args()
    cfg = load_config()
    with Day6Store(cfg) as store:
        chunks = store.all_chunks()
    expected = cfg["store"]["expected_rows"][cfg["store"]["strategy"]]
    if len(chunks) != expected:
        sys.exit(f"FAIL: exported {len(chunks)} chunks, expected {expected}")
    ids = [c["id"] for c in chunks]
    if len(set(ids)) != len(ids) or any(not c["text"].strip() for c in chunks):
        sys.exit("FAIL: duplicate IDs or empty chunk text")
    for c in chunks:
        c["metadata"] |= {"strategy": cfg["store"]["strategy"], "doc_version": cfg["corpus"]["doc_version"],
                          "embedding_model": cfg["embedding"]["model"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(chunks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pages = sorted({c["page"] for c in chunks})
    print(f"Exported {len(chunks)} chunks (pages {pages[0]}-{pages[-1]}) -> {args.output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
