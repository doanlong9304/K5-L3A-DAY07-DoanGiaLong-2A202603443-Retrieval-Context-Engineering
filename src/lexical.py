"""BM25 lexical retrieval over the exported Day 6 chunks (data/day6/chunks.json).

score(q, d) = sum over query terms t of
    idf(t) * tf(t,d) * (k1 + 1) / (tf(t,d) + k1 * (1 - b + b * len(d) / avg_len))
    idf(t)  = ln(1 + (N - df(t) + 0.5) / (df(t) + 0.5))

Tokenizers (Vietnamese words are often 2+ syllables, e.g. "đầu tư"):
  syllable : lowercase NFC syllables ("dự án đầu tư" -> dự, án, đầu, tư)
  bigram   : syllables + adjacent syllable pairs (adds dự_án, án_đầu, đầu_tư)
No external word segmenter; bigrams approximate compound words.
"""
from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter
from typing import Any


def syllables(text: str) -> list[str]:
    return re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold())


def syllables_bigrams(text: str) -> list[str]:
    s = syllables(text)
    return s + [f"{a}_{b}" for a, b in zip(s, s[1:])]


TOKENIZERS = {"syllable": syllables, "bigram": syllables_bigrams}


class BM25Retriever:
    """Day 7 Retriever protocol: search(query, *, filters, top_k) -> chunks with score."""

    def __init__(self, chunks: list[dict[str, Any]], tokenizer: str = "syllable",
                 k1: float = 1.5, b: float = 0.75) -> None:
        self.chunks = chunks
        self.tokenize = TOKENIZERS[tokenizer]
        self.name = "bm25" if tokenizer == "syllable" else f"bm25-{tokenizer}"
        self.k1, self.b = k1, b
        self.tf = [Counter(self.tokenize(c["text"])) for c in chunks]
        self.lengths = [sum(tf.values()) for tf in self.tf]
        self.avg_len = sum(self.lengths) / len(self.lengths)
        df = Counter(term for tf in self.tf for term in tf)
        n = len(chunks)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def _score(self, terms: list[str], i: int) -> float:
        tf, norm = self.tf[i], self.k1 * (1 - self.b + self.b * self.lengths[i] / self.avg_len)
        return sum(self.idf[t] * tf[t] * (self.k1 + 1) / (tf[t] + norm) for t in terms if t in tf)

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        terms = list(dict.fromkeys(self.tokenize(query)))  # unique query terms, order kept
        scored = []
        for i, c in enumerate(self.chunks):
            if filters and any(c["metadata"].get(k) != v for k, v in filters.items()):
                continue
            s = self._score(terms, i)
            if s > 0:
                scored.append((s, c["id"], i))
        scored.sort(key=lambda x: (-x[0], x[1]))  # tie-break by id: deterministic
        return [{**self.chunks[i], "score": s, "strategy": self.name} for s, _, i in scored[:top_k]]
