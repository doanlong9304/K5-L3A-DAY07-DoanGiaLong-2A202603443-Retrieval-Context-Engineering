"""Check (and optionally start) the Day 6 index that Day 7 reuses.

    python scripts/check_day6.py            # DB checks only, no API call
    python scripts/check_day6.py --start    # start the Day 6 container first (same project/volume)
    python scripts/check_day6.py --query "Thời hạn hoạt động của dự án trong khu kinh tế?"   # + 1 real embedding call

--start runs Docker Compose with the Day 6 compose files and project name, so it
reuses the existing container and volume (the ingested vectors). It never runs
`down` or touches volumes. DAY6_STARTER_DIR in .env points to Day 6's starter/.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.day6_index import Day6Store, DenseRetriever, GeminiQueryEmbedder, load_config  # noqa: E402


def fail(msg: str) -> None:
    sys.exit(f"FAIL: {msg}")


def docker_state(container: str) -> str | None:
    try:
        r = subprocess.run(["docker", "inspect", "-f", "{{.State.Status}}", container],
                           capture_output=True, text=True, timeout=30)
    except FileNotFoundError:
        fail("docker CLI not found. Install/start Docker Desktop.")
    except subprocess.TimeoutExpired:
        fail("docker did not respond. Is Docker Desktop running?")
    if r.returncode != 0:
        if "daemon" in r.stderr.lower() or "pipe" in r.stderr.lower():
            fail("Docker engine not reachable. Open Docker Desktop and wait until it says 'Engine running'.")
        return None
    return r.stdout.strip()


def start(cfg: dict) -> None:
    day6 = os.getenv("DAY6_STARTER_DIR")
    if not day6 or not (Path(day6) / "docker-compose.yml").exists():
        fail("DAY6_STARTER_DIR in .env must point to the Day 6 starter/ folder (with docker-compose.yml).")
    day6 = Path(day6).resolve()
    files = ["-f", str(day6 / "docker-compose.yml")]
    if (day6 / "docker-compose.override.yml").exists():
        files += ["-f", str(day6 / "docker-compose.override.yml")]
    cmd = ["docker", "compose", "-p", cfg["docker"]["compose_project"], "--project-directory", str(day6),
           *files, "up", "-d", "--wait"]
    print("Running:", " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        err = r.stderr.strip()
        if "ports are not available" in err or "forbidden by its access permissions" in err:
            fail(f"Port {cfg['docker']['host_port']} is blocked (Windows reserved range?). Check: "
                 "netsh interface ipv4 show excludedportrange protocol=tcp\n" + err)
        fail("docker compose up failed:\n" + err)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", action="store_true", help="start the Day 6 container before checking")
    ap.add_argument("--query", help="also embed this query with Gemini and run a dense search")
    ap.add_argument("-k", "--top-k", type=int, default=3)
    args = ap.parse_args()
    cfg = load_config()

    if args.start:
        start(cfg)
    state = docker_state(cfg["docker"]["container"])
    if state != "running":
        fail(f"container {cfg['docker']['container']} is {state or 'missing'}. "
             "Run: python scripts/check_day6.py --start")
    print(f"Docker: {cfg['docker']['container']} running")

    s, e, corpus = cfg["store"], cfg["embedding"], cfg["corpus"]
    with Day6Store(cfg) as store:
        cur = store.conn.cursor()
        ver = cur.execute("SELECT extversion FROM pg_extension WHERE extname = 'vector'").fetchone()
        if not ver:
            fail("pgvector extension missing")
        rows = cur.execute(f"""
            SELECT strategy, count(*), count(DISTINCT id), array_agg(DISTINCT embedding_model),
                   array_agg(DISTINCT doc_version), min(vector_dims(embedding)), max(vector_dims(embedding))
            FROM {s['table']} GROUP BY strategy ORDER BY strategy""").fetchall()
        found = {r[0]: r for r in rows}
        for name, expected in s["expected_rows"].items():
            r = found.get(name)
            if not r:
                fail(f"strategy {name}: no rows. Was the volume recreated? Re-run Day 6 ingest.")
            _, n, distinct, models, versions, dmin, dmax = r
            if n != expected or distinct != n:
                fail(f"strategy {name}: {n} rows / {distinct} distinct ids, expected {expected}")
            if models != [e["model"]] or versions != [corpus["doc_version"]] or not dmin == dmax == e["dimensions"]:
                fail(f"strategy {name}: model {models}, doc_version {versions}, dims {dmin}-{dmax} do not match config")
        print(f"pgvector {ver[0]} | table {s['table']} | " +
              ", ".join(f"{k}={found[k][1]} rows" for k in s["expected_rows"]) +
              f" | {e['model']} {e['dimensions']}d | doc_version {corpus['doc_version'][:12]}…")
        print(f"Day 7 uses strategy {s['strategy']}: {len(store.all_chunks())} chunks readable")

        if args.query:
            retriever = DenseRetriever(GeminiQueryEmbedder(cfg), store)
            hits = retriever.search(args.query, top_k=args.top_k)
            print(json.dumps([{k: h[k] for k in ("id", "page", "score")} | {"article": h["metadata"]["article"],
                              "text": h["text"][:90]} for h in hits], ensure_ascii=False, indent=2))
    print("Day 6 index OK (read-only).")


if __name__ == "__main__":
    main()
