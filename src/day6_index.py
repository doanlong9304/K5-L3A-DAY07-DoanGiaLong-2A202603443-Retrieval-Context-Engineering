"""Read-only access to the Day 6 index: Gemini query embeddings + pgvector dense search.

Reuses the Day 6 PostgreSQL container/volume and embedding model unchanged. The
connection is opened with default_transaction_read_only=on, so Day 7 code cannot
modify the Day 6 index. Results use the Day 7 chunk format
(id, text, source_id, source, page, metadata, score). Never returns mock vectors.
"""
from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from typing import Any

import psycopg
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "configs" / "day6_index.json"
META_COLS = ["page_end", "chapter", "chapter_title", "section", "article"]
RETRYABLE = {429, 500, 503}
log = logging.getLogger(__name__)


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    load_dotenv(ROOT / ".env")  # does not override variables already set
    return json.loads(path.read_text(encoding="utf-8"))


def _vec(v: list[float]) -> str:
    return "[" + ",".join(repr(float(x)) for x in v) + "]"


class GeminiQueryEmbedder:
    """Query-side embedder matching the Day 6 document index (same model, dims, task type)."""

    def __init__(self, cfg: dict[str, Any], max_retries: int = 6) -> None:
        from google import genai  # imported lazily so DB-only checks need no SDK call

        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY is not set (.env or environment).")
        e = cfg["embedding"]
        self.client = genai.Client(api_key=key)
        self.model = e["model"]
        self.dimensions = e["dimensions"]
        self.task = e["query_task_type"]
        self.max_retries = max_retries
        self.api_calls = 0

    def embed_queries(self, queries: list[str]) -> list[list[float]]:
        from google.genai import errors, types

        if not queries:
            return []
        config = types.EmbedContentConfig(task_type=self.task, output_dimensionality=self.dimensions)
        for attempt in range(self.max_retries + 1):
            try:
                resp = self.client.models.embed_content(model=self.model, contents=queries, config=config)
                self.api_calls += 1
                break
            except errors.APIError as exc:
                if exc.code not in RETRYABLE or attempt == self.max_retries:
                    raise
                wait = min(60, 5 * 2 ** attempt)
                log.warning("Embedding HTTP %s, retry %d in %ss", exc.code, attempt + 1, wait)
                time.sleep(wait)
        vectors = [e.values for e in resp.embeddings]
        if len(vectors) != len(queries) or any(len(v) != self.dimensions for v in vectors):
            raise RuntimeError("Embedding API returned wrong count or dimensions.")
        return vectors

    def embed_query(self, query: str) -> list[float]:
        return self.embed_queries([query])[0]


class Day6Store:
    """Read-only pgvector search over one Day 6 strategy (default B)."""

    def __init__(self, cfg: dict[str, Any], database_url: str | None = None) -> None:
        url = database_url or os.getenv("DATABASE_URL")
        if not url:
            raise RuntimeError("DATABASE_URL missing (.env or environment).")
        s = cfg["store"]
        self.table = s["table"]
        self.strategy = s["strategy"]
        self.filterable = set(s["filterable"])
        self.model = cfg["embedding"]["model"]
        self.dimensions = cfg["embedding"]["dimensions"]
        try:
            self.conn = psycopg.connect(url, connect_timeout=5, autocommit=True,
                                        options="-c default_transaction_read_only=on")
        except psycopg.OperationalError as exc:
            port = cfg["docker"]["host_port"]
            raise RuntimeError(
                f"Cannot connect to the Day 6 PostgreSQL ({exc}). Is Docker Desktop running and the "
                f"container up on 127.0.0.1:{port}? Run: python scripts/check_day6.py --start") from exc

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "Day6Store":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    @staticmethod
    def _row_to_chunk(r: dict[str, Any]) -> dict[str, Any]:
        out = {"id": r["id"], "text": r["text"], "source_id": r["document_id"], "source": r["source"],
               "page": r["page"], "metadata": {k: r[k] for k in META_COLS}}
        if "score" in r:
            out["score"] = float(r["score"])
        return out

    def search(self, query_vector: list[float], top_k: int = 3,
               filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """Dense cosine search; filters only on whitelisted metadata columns."""
        if len(query_vector) != self.dimensions:
            raise ValueError("query vector dimension mismatch")
        if top_k < 1:
            raise ValueError("top_k must be >= 1")
        where, params = ["strategy = %s", "embedding_model = %s"], [self.strategy, self.model]
        for key, value in (filters or {}).items():
            if key not in self.filterable:
                raise ValueError(f"filter on '{key}' not allowed")
            where.append(f"{key} = %s")
            params.append(value)
        qv = _vec(query_vector)
        with self.conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            cur.execute(f"""
                SELECT id, document_id, source, page, {", ".join(META_COLS)}, text,
                       1 - (embedding <=> %s::vector) AS score
                FROM {self.table} WHERE {" AND ".join(where)}
                ORDER BY embedding <=> %s::vector, id
                LIMIT %s""", [qv, *params, qv, top_k])
            return [self._row_to_chunk(r) for r in cur.fetchall()]

    def all_chunks(self) -> list[dict[str, Any]]:
        """Every chunk of the strategy in document order (for lexical indexes / export)."""
        with self.conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            cur.execute(f"""SELECT id, document_id, source, page, {", ".join(META_COLS)}, text
                            FROM {self.table} WHERE strategy = %s ORDER BY char_start, id""",
                        (self.strategy,))
            return [self._row_to_chunk(r) for r in cur.fetchall()]


class DenseRetriever:
    """Day 7 Retriever protocol: search(query, *, filters, top_k) -> chunks."""

    def __init__(self, embedder: GeminiQueryEmbedder, store: Day6Store) -> None:
        self.embedder = embedder
        self.store = store

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        hits = self.store.search(self.embedder.embed_query(query), top_k, filters)
        return [{**h, "strategy": "dense"} for h in hits]
