"""Hybrid retrieval by Reciprocal Rank Fusion (Cormack et al., 2009).

rrf(d) = sum over retrievers r of 1 / (k + rank_r(d)),  rank starting at 1;
a chunk missing from a retriever's candidate list gets nothing from it.
Uses ranks only, so dense cosine (~0.6-0.8) and BM25 (~5-30) scores need no
normalization. k = 60 is the paper's default (not tuned on dev).
"""
from __future__ import annotations

from typing import Any


class RRFRetriever:
    """Day 7 Retriever protocol; fuses several retrievers that share the same chunk IDs."""

    def __init__(self, retrievers: dict[str, Any], k: int = 60, candidates: int = 20) -> None:
        self.retrievers = retrievers
        self.k = k
        self.candidates = candidates
        self.name = "hybrid-rrf(" + "+".join(retrievers) + ")"

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        fused: dict[str, dict[str, Any]] = {}
        for name, retriever in self.retrievers.items():
            for rank, hit in enumerate(retriever.search(query, filters=filters, top_k=self.candidates), start=1):
                entry = fused.setdefault(hit["id"], {"chunk": hit, "score": 0.0, "ranks": {}})
                entry["score"] += 1 / (self.k + rank)
                entry["ranks"][name] = rank
        ordered = sorted(fused.values(), key=lambda e: (-e["score"], e["chunk"]["id"]))[:top_k]
        out = []
        for e in ordered:
            chunk = {k: v for k, v in e["chunk"].items() if k not in ("score", "strategy")}
            out.append({**chunk, "score": e["score"], "strategy": self.name, "component_ranks": e["ranks"]})
        return out
