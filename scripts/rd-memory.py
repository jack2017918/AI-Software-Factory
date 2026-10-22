#!/usr/bin/env python3
"""Read/write Factory rd/* namespaces in Ruflo hybrid SQLite (.swarm/memory.db)."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
import uuid
from pathlib import Path

FACTORY = Path(__file__).resolve().parents[1]
DB = FACTORY / ".swarm" / "memory.db"
ALLOWED = {
    "rd/decisions",
    "rd/handoffs",
    "rd/failures",
    "rd/conventions",
}


def connect() -> sqlite3.Connection:
    if not DB.exists():
        raise SystemExit(f"missing {DB}")
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA foreign_keys=ON")
    return con


def require_ns(ns: str) -> None:
    if ns not in ALLOWED:
        raise SystemExit(f"namespace must be one of {sorted(ALLOWED)}, got {ns}")


def upsert(ns: str, key: str, content: str, tags: list[str] | None = None) -> str:
    require_ns(ns)
    if "product/buyers" in ns or "product/buyers" in key:
        raise SystemExit("refuse product/buyers in rd/*")
    now = int(time.time() * 1000)
    con = connect()
    row = con.execute(
        "SELECT id FROM memory_entries WHERE namespace=? AND key=?",
        (ns, key),
    ).fetchone()
    if row:
        con.execute(
            """UPDATE memory_entries
               SET content=?, updated_at=?, last_accessed_at=?,
                   access_count=access_count+1, status='active',
                   provenance_type='agent_output', type='semantic'
               WHERE id=?""",
            (content, now, now, row["id"]),
        )
        eid = row["id"]
    else:
        eid = str(uuid.uuid4())
        con.execute(
            """INSERT INTO memory_entries (
                 id, key, namespace, content, type, tags, metadata,
                 provenance_type, created_at, updated_at, last_accessed_at,
                 access_count, status
               ) VALUES (?,?,?,?,?,?,?,?,?,?,?,1,'active')""",
            (
                eid,
                key,
                ns,
                content,
                "semantic",
                json.dumps(tags or []),
                json.dumps({"source": "rd-memory.py"}),
                "agent_output",
                now,
                now,
                now,
            ),
        )
    con.commit()
    con.close()
    return eid


def get_one(ns: str, key: str) -> sqlite3.Row | None:
    require_ns(ns)
    con = connect()
    row = con.execute(
        """SELECT id, namespace, key, content, updated_at
           FROM memory_entries
           WHERE namespace=? AND key=? AND status='active'""",
        (ns, key),
    ).fetchone()
    if row:
        con.execute(
            """UPDATE memory_entries
               SET last_accessed_at=?, access_count=access_count+1
               WHERE id=?""",
            (int(time.time() * 1000), row["id"]),
        )
        con.commit()
    con.close()
    return row


def list_entries(ns: str | None) -> list[sqlite3.Row]:
    con = connect()
    if ns:
        require_ns(ns)
        rows = con.execute(
            """SELECT namespace, key, length(content) AS bytes, updated_at
               FROM memory_entries
               WHERE namespace=? AND status='active'
               ORDER BY namespace, key""",
            (ns,),
        ).fetchall()
    else:
        rows = con.execute(
            """SELECT namespace, key, length(content) AS bytes, updated_at
               FROM memory_entries
               WHERE status='active' AND namespace LIKE 'rd/%'
               ORDER BY namespace, key"""
        ).fetchall()
    con.close()
    return rows


def seed() -> list[tuple[str, str]]:
    missions = FACTORY / ".ai-team" / "missions"
    write_map = FACTORY / ".ai-team" / "write-map.md"
    items = [
        ("rd/handoffs", "phase0-smoke", missions / "phase0-smoke-handoffs.md"),
        ("rd/handoffs", "v1.0.0", missions / "v1.0.0-handoffs.md"),
        ("rd/handoffs", "v1.0.0-build:coordinator-architect", missions / "v1.0.0-build-handoffs.md"),
        ("rd/conventions", "write-map", write_map),
        (
            "rd/decisions",
            "cross-directory-write",
            None,
        ),
    ]
    decision = (
        "Parent workspace AI-Software stays the execution root. "
        "AI-Software-Factory and AI-Foreign are asset folders, not sandbox walls. "
        "Product missions MUST write AI-Foreign/. Factory runtime stays in Factory. "
        "Use factory-* agents. Persist handoffs in rd/handoffs via scripts/rd-memory.py."
    )
    written: list[tuple[str, str]] = []
    for ns, key, path in items:
        if path is None:
            content = decision
        else:
            if not path.exists():
                print(f"skip missing {path}", file=sys.stderr)
                continue
            content = path.read_text(encoding="utf-8")
        upsert(ns, key, content, tags=["seed", "2026-10-20"])
        written.append((ns, key))
    return written


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    up = sub.add_parser("upsert")
    up.add_argument("--namespace", required=True)
    up.add_argument("--key", required=True)
    g = up.add_mutually_exclusive_group(required=True)
    g.add_argument("--file")
    g.add_argument("--content")

    gt = sub.add_parser("get")
    gt.add_argument("--namespace", required=True)
    gt.add_argument("--key", required=True)

    ls = sub.add_parser("list")
    ls.add_argument("--namespace")

    sub.add_parser("seed")

    args = p.parse_args()
    if args.cmd == "upsert":
        text = Path(args.file).read_text(encoding="utf-8") if args.file else args.content
        eid = upsert(args.namespace, args.key, text)
        print(json.dumps({"ok": True, "id": eid, "namespace": args.namespace, "key": args.key}))
        return 0
    if args.cmd == "get":
        row = get_one(args.namespace, args.key)
        if not row:
            print(json.dumps({"ok": False, "hit": False, "namespace": args.namespace, "key": args.key}))
            return 2
        print(json.dumps({"ok": True, "hit": True, "namespace": row["namespace"], "key": row["key"], "content": row["content"]}, ensure_ascii=False))
        return 0
    if args.cmd == "list":
        rows = list_entries(args.namespace)
        print(json.dumps([{"namespace": r["namespace"], "key": r["key"], "bytes": r["bytes"]} for r in rows], ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "seed":
        written = seed()
        print(json.dumps({"ok": True, "written": [{"namespace": n, "key": k} for n, k in written]}, ensure_ascii=False, indent=2))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
