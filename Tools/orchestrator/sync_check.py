#!/usr/bin/env python3
"""Run the bead-page export and print only what a session has to write.

    python -I Tools/orchestrator/sync_check.py          # export, print what is pending
    python -I Tools/orchestrator/sync_check.py --ack    # after the ArtifactData batch succeeded

It runs Tools/beads_board/sync_board.py and prints one short block: each doc id to
`set` with its file path, and each doc id to delete. The ArtifactData write is the
session's job (Tools/beads_board/README.md, "Sync"); this script never touches the page.

sync_board.py forgets a change once it has reported it, so a report nobody acted on
would be lost. This keeps the unwritten doc ids in Tools/beads_board/out/pending.json
(gitignored) and repeats them on every run until `--ack` clears them.
Exit code: 0 nothing pending, 1 something pending, 2 the export failed.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

BOARD = Path(__file__).resolve().parents[1] / "beads_board"
PAGE = "https://claude.ai/artifact/NgqNUkLBWENWRQtESxYiCZ"


def merge(pending: dict, report: dict) -> dict:
    """Fold one sync_board.py report into the pending set."""
    files = dict(pending.get("files", {}))
    removed = [r for r in pending.get("removed", [])]
    for doc in report.get("changed", []):
        files[doc] = report.get("files", {}).get(doc, files.get(doc, ""))
        if doc in removed:
            removed.remove(doc)
    for doc in report.get("removed", []):
        files.pop(doc, None)
        if doc not in removed:
            removed.append(doc)
    return {"files": files, "removed": removed}


def render(pending: dict, counts: dict | None = None) -> str:
    files, removed = pending.get("files", {}), pending.get("removed", [])
    total = ""
    if counts:
        total = " (" + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + ")"
    if not files and not removed:
        return f"bead page: nothing to write{total}"
    lines = [f"bead page: {len(files)} to set, {len(removed)} to delete{total}"]
    lines += [f"  set    {doc}  {path}" for doc, path in files.items()]
    lines += [f"  delete {doc}" for doc in removed]
    lines.append(f"  write: ArtifactData list + ONE batch, collection board, {PAGE}; then sync_check.py --ack")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Export beads for the review page; print what must be written.")
    ap.add_argument("--ack", action="store_true", help="the ArtifactData write succeeded: clear the pending list")
    a = ap.parse_args(argv)
    store = BOARD / "out" / "pending.json"
    if a.ack:
        store.unlink(missing_ok=True)
        print("bead page: pending list cleared")
        return 0
    p = subprocess.run([sys.executable, "-I", str(BOARD / "sync_board.py")],
                       capture_output=True, text=True, encoding="utf-8", cwd=BOARD.parents[1])
    try:
        report = json.loads(p.stdout)
    except ValueError:
        print("bead page: sync_board.py failed\n" + (p.stderr or p.stdout).strip()[-600:], file=sys.stderr)
        return 2
    old = json.loads(store.read_text(encoding="utf-8")) if store.exists() else {}
    pending = merge(old, report)
    if pending["files"] or pending["removed"]:
        store.parent.mkdir(exist_ok=True)
        store.write_text(json.dumps(pending), encoding="utf-8")
    print(render(pending, report.get("counts")))
    return 1 if pending["files"] or pending["removed"] else 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    sys.exit(main())
