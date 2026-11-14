# Retrieval comparison — dev (16 answerable questions)

Same corpus (Day 6 strategy B, 118 chunks), questions, gold and hit rule (src/evidence.py). Context = top-3 packed into the char budget. Unanswerable questions are not in the denominator.

| Run | Method | User filter | Hit@1 | Evidence Hit@3 | Context Evidence | Hit@10 | MRR@10 | Avg context chars | Embedding API calls | Misses@3 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bm25 | bm25 | yes | 13/16 | 15/16 | 15/16 | 16/16 | 0.872 | 2420 | 0 (local) | q04 |
| bm25-bigram | bm25-bigram | yes | 16/16 | 16/16 | 16/16 | 16/16 | 1.000 | 2262 | 0 (local) | — |
| dense | dense | yes | 12/16 | 16/16 | 16/16 | 16/16 | 0.875 | 2179 | 1 / query (cached on rerun) | — |
| hybrid | hybrid | yes | 16/16 | 16/16 | 16/16 | 16/16 | 1.000 | 2312 | 1 / query (cached on rerun) | — |
| bm25-bigram-nofilter | bm25-bigram | no | 15/16 | 16/16 | 16/16 | 16/16 | 0.958 | 2330 | 0 (local) | — |
| bm25-nofilter | bm25 | no | 10/16 | 14/16 | 14/16 | 16/16 | 0.753 | 2416 | 0 (local) | q04, q09 |
| dense-nofilter | dense | no | 11/16 | 15/16 | 15/16 | 15/16 | 0.812 | 2248 | 1 / query (cached on rerun) | q16 |
| hybrid-nofilter | hybrid | no | 14/16 | 15/16 | 15/16 | 16/16 | 0.919 | 2419 | 1 / query (cached on rerun) | q16 |

Budget: 3000 chars; embedding gemini-embedding-001 768d. Latency is not compared here: dense/hybrid reruns read query embeddings from cache (a fresh Gemini query embedding took ~360 ms/query in the first run).
