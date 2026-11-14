"""Evidence matching for the Day 6 corpus.

Why not starter/baseline.py `hit()`: it needs the evidence to be an exact
substring and `chunk.page == gold.page`. Day 6 chunk text keeps the PDF line
breaks (evidence quotes are single-line), and a structure chunk can start on one
page and continue onto the next, so the evidence may sit on `page_end`.
Rule used here (same as Day 6 evaluation):
  same source_id, AND gold page in [chunk.page, chunk.metadata.page_end],
  AND whitespace-normalized evidence is inside the whitespace-normalized chunk text.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text)).strip()


def page_range(chunk: dict[str, Any]) -> tuple[int, int]:
    start = chunk["page"]
    end = (chunk.get("metadata") or {}).get("page_end") or start
    return start, end


def evidence_in_chunk(chunk: dict[str, Any], gold: dict[str, Any]) -> bool:
    start, end = page_range(chunk)
    return (chunk["source_id"] == gold["source_id"] and start <= gold["page"] <= end
            and normalize(gold["evidence"]) in normalize(chunk["text"]))


def evidence_hit(chunk: dict[str, Any], gold: list[dict[str, Any]]) -> bool:
    """True if the chunk contains any of the alternative gold evidence items."""
    return any(evidence_in_chunk(chunk, g) for g in gold)


def strict_starter_hit(chunk: dict[str, Any], gold: list[dict[str, Any]]) -> bool:
    """starter/baseline.py rule, kept only to report how it differs."""
    return any(chunk["source_id"] == g["source_id"] and chunk["page"] == g["page"]
               and g["evidence"] in chunk["text"] for g in gold)


def exact_span(text: str, quote: str) -> str | None:
    """The substring of `text` equal to `quote` up to whitespace (keeps the chunk's line breaks)."""
    words = normalize(quote).split(" ")
    m = re.search(r"\s+".join(map(re.escape, words)), unicodedata.normalize("NFC", text))
    return m.group(0) if m else None
