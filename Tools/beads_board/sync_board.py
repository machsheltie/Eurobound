#!/usr/bin/env python3
"""Export every bead (open, in progress and closed) for the bead review page.

    python -I Tools/beads_board/sync_board.py

Writes Tools/beads_board/out/board_<n>.json chunks (each under ~180 KB, the page's
store caps a document at 256 KB) plus meta.json, then prints which docs changed since
the last run. A Claude session then writes the changed docs to the page's `board`
collection with ArtifactData (see README.md). Standard library only.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
STATE = OUT / "last_hashes.json"
CHUNK_LIMIT = 180_000
BD = shutil.which("bd") or shutil.which("bd.cmd") or "bd"


def bd(*args: str) -> str:
    return subprocess.run([BD, *args], capture_output=True, text=True, encoding="utf-8").stdout


def split_skills(desc: str, notes: str) -> tuple[str, list[str]]:
    skills = ""
    m = re.search(r"\n*##\s*Required Skills\s*\n+(.+?)(\n\n|\Z)", desc, re.S)
    if m:
        skills = m.group(1).strip()
        desc = (desc[: m.start()] + desc[m.end():]).strip()
    if not skills:
        m2 = re.search(r"Required skills:\s*([^\n]+?)\.(\s|$)", notes or "")
        if m2:
            skills = m2.group(1)
    return desc, [s.strip() for s in re.split(r"[,\n]", skills) if s.strip()]


def main() -> None:
    raw = json.loads(bd("list", "--all", "--json", "-n", "0") or "[]")
    issues = raw if isinstance(raw, list) else raw.get("issues", [])
    beads = []
    for i in issues:
        md = i.get("metadata") or {}
        if isinstance(md, str):
            try:
                md = json.loads(md)
            except ValueError:
                md = {}
        desc, skills = split_skills(i.get("description") or "", i.get("notes") or "")
        deps = []
        if i.get("dependency_count") and i.get("status") != "closed":
            try:
                deps = [d["id"] for d in json.loads(bd("dep", "list", i["id"], "--json") or "[]")]
            except (ValueError, KeyError, TypeError):
                deps = []
        labels = i.get("labels") or []
        ask = md.get("ask")
        if isinstance(ask, str):
            try:
                ask = json.loads(ask)
            except ValueError:
                ask = None
        beads.append({
            "ask": ask if isinstance(ask, dict) and i.get("status") != "closed" else None,
            "id": i["id"], "title": i["title"], "p": i.get("priority", 2), "type": i.get("issue_type", ""),
            "status": i.get("status", "open"),
            "labels": [l for l in labels if not l.startswith(("agent:", "effort:"))],
            "agent": md.get("agent", ""), "effort": md.get("effort", ""), "by": md.get("found_by", ""),
            "skills": skills, "desc": desc, "acc": i.get("acceptance_criteria") or "", "deps": deps,
            "updated": i.get("updated_at", ""), "closed": i.get("closed_at") or "",
            "reason": (i.get("close_reason") or "")[:600], "comments": i.get("comment_count", 0),
        })
    # Open work first (by priority), then closed (newest first); closed beads drop their long text.
    beads.sort(key=lambda b: (b["status"] == "closed", b["p"] if b["status"] != "closed" else 0,
                              "" if b["status"] != "closed" else "~" + b["closed"][::-1], b["id"]))
    for b in beads:
        if b["status"] == "closed":
            b["desc"] = b["desc"][:400]
            b["acc"] = ""

    chunks, cur, size = [], [], 0
    for b in beads:
        n = len(json.dumps(b, ensure_ascii=False))
        if cur and size + n > CHUNK_LIMIT:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(b)
        size += n
    if cur:
        chunks.append(cur)

    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("board_*.json"):
        old.unlink()
    docs = {}
    for n, chunk in enumerate(chunks, 1):
        docs[f"board_{n}"] = {"beads": chunk}
    counts = {}
    for b in beads:
        counts[b["status"]] = counts.get(b["status"], 0) + 1
    meta = {"chunks": list(docs), "counts": counts, "total": len(beads)}
    docs["meta"] = meta

    prev = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    hashes, changed = {}, []
    for doc_id, body in docs.items():
        h = hashlib.sha1(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        hashes[doc_id] = h
        if prev.get(doc_id) != h:
            changed.append(doc_id)
    if changed and "meta" not in changed:
        changed.append("meta")
    meta["synced"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for doc_id, body in docs.items():
        (OUT / f"{doc_id}.json").write_text(json.dumps(body, ensure_ascii=False), encoding="utf-8")
    removed = [d for d in prev if d not in docs]
    STATE.write_text(json.dumps(hashes), encoding="utf-8")
    print(json.dumps({"changed": changed, "removed": removed, "counts": counts,
                      "files": {d: str((OUT / f"{d}.json")) for d in changed}}, indent=1))


if __name__ == "__main__":
    if sys.stdout.encoding.lower() != "utf-8" and hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
