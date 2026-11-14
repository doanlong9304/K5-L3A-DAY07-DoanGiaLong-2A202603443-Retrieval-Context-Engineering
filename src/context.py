"""Context packing shared by retrieval evaluation and the agent.

Same policy as starter/baseline.py pack_context: walk candidates in order, drop
duplicate IDs, keep each block only if the whole context still fits the character
budget (blocks that do not fit are skipped, not truncated). The header adds the
page range and article so the model can cite and the grader can verify.
"""
from __future__ import annotations

from typing import Any


def block(c: dict[str, Any]) -> str:
    m = c.get("metadata") or {}
    pages = f"{c['page']}" if m.get("page_end") in (None, c["page"]) else f"{c['page']}-{m['page_end']}"
    art = f" | Điều {m['article']}" if m.get("article") else ""
    return f"[{c['id']}] (nguồn: {c['source']} | trang {pages}{art})\n{c['text']}"


def pack_context(candidates: list[dict[str, Any]], budget: int) -> tuple[str, list[str]]:
    blocks: list[str] = []
    ids: list[str] = []
    seen: set[str] = set()
    for c in candidates:
        if c["id"] in seen:
            continue
        seen.add(c["id"])
        b = block(c)
        if len("\n\n".join(blocks + [b])) <= budget:
            blocks.append(b)
            ids.append(c["id"])
    return "\n\n".join(blocks), ids
