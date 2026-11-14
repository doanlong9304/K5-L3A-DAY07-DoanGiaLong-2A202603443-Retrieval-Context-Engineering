# Retrieval comparison — test (5 answerable questions)

Same corpus (Day 6 strategy B, 118 chunks), questions, gold and hit rule (src/evidence.py). Context = top-3 packed into the char budget. Unanswerable questions are not in the denominator.

| Run | Method | User filter | Hit@1 | Evidence Hit@3 | Context Evidence | Hit@10 | MRR@10 | Avg context chars | Embedding API calls | Misses@3 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bm25 | bm25 | yes | 5/5 | 5/5 | 5/5 | 5/5 | 1.000 | 2403 | 0 (local) | — |
| bm25-bigram | bm25-bigram | yes | 5/5 | 5/5 | 5/5 | 5/5 | 1.000 | 2464 | 0 (local) | — |
| dense | dense | yes | 5/5 | 5/5 | 5/5 | 5/5 | 1.000 | 2308 | 1 / query (cached on rerun) | — |
| hybrid | hybrid | yes | 5/5 | 5/5 | 5/5 | 5/5 | 1.000 | 2449 | 1 / query (cached on rerun) | — |

Budget: 3000 chars; embedding gemini-embedding-001 768d. Latency is not compared here: dense/hybrid reruns read query embeddings from cache (a fresh Gemini query embedding took ~360 ms/query in the first run).
