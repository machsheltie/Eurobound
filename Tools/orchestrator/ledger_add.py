#!/usr/bin/env python3
"""Add one entry to the rulings ledger and stage only that entry.

    python -I Tools/orchestrator/ledger_add.py "- **(Author, chat, 2026-11-14; Eurobound-xxxx) ...**"

The entry goes into docs/superpowers/NEXT_WORK.md just before the line
"## Resolved (moved 2026-11-11 by Eurobound-j50)", after the last existing entry.

Other sessions keep uncommitted edits in that file, so `git add` would stage their
work too. This writes the entry twice instead:
  1. into the working tree file (their edits stay, unstaged);
  2. into a blob built from the INDEX version (`git show :path` -> `git hash-object -w`
     -> `git update-index --cacheinfo`), so the staged diff is the entry alone.
Building from the index, not HEAD, is what lets two calls before one commit keep
both entries.

Refuses (exit 2, nothing changed) if the anchor is missing from either version, the
file is not in the index, or the entry is empty. An entry already present in a
version is not added to it again. Standard library only.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

LEDGER = "docs/superpowers/NEXT_WORK.md"
ANCHOR = "## Resolved (moved 2026-11-11 by Eurobound-j50)"


class Refuse(Exception):
    """A reason not to write. Nothing has been changed when this is raised."""


def git(repo: Path, *args: str, stdin: bytes | None = None) -> bytes:
    p = subprocess.run(["git", "-C", str(repo), *args], input=stdin, capture_output=True)
    if p.returncode != 0:
        raise Refuse(f"git {' '.join(args)} failed:\n{p.stderr.decode('utf-8', 'replace').strip()}")
    return p.stdout


def insert(text: str, entry: str, anchor: str, where: str) -> str | None:
    """`text` with `entry` placed after the last entry above `anchor`; None if it is already there."""
    lines = text.splitlines(keepends=True)
    at = next((n for n, line in enumerate(lines) if line.rstrip("\r\n") == anchor), None)
    if at is None:
        raise Refuse(f"anchor line not found in the {where}: {anchor!r}")
    if any(line.rstrip("\r\n") == entry for line in lines):
        return None
    eol = "\r\n" if lines[at].endswith("\r\n") else "\n"
    spot = at
    while spot > 0 and not lines[spot - 1].strip():
        spot -= 1
    if spot > 0 and not lines[spot - 1].endswith(("\n", "\r")):
        lines[spot - 1] += eol
    new = [entry.replace("\r\n", "\n").replace("\n", eol) + eol]
    if spot == at:  # no blank line stood between the last entry and the anchor
        new.append(eol)
    return "".join(lines[:spot] + new + lines[spot:])


def ledger_add(repo: Path, entry: str, path: str = LEDGER, anchor: str = ANCHOR) -> str:
    entry = entry.replace("﻿", "").strip()
    if not entry:
        raise Refuse("the entry is empty")
    root = Path(git(repo, "rev-parse", "--show-toplevel").decode().strip())
    stages = git(root, "ls-files", "-s", "--", path).decode().splitlines()
    if not stages:
        raise Refuse(f"{path} is not in the index")
    if len(stages) > 1 or stages[0].split()[2] != "0":
        raise Refuse(f"{path} has merge conflicts in the index")
    mode = stages[0].split()[0]
    work = root / path
    if not work.is_file():
        raise Refuse(f"{path} is missing from the working tree")

    # Read and check both versions before writing either.
    new_work = insert(work.read_bytes().decode("utf-8"), entry, anchor, "working tree file")
    new_index = insert(git(root, "show", f":{path}").decode("utf-8"), entry, anchor, "index version")

    done = []
    if new_index is not None:
        sha = git(root, "hash-object", "-w", "--stdin", stdin=new_index.encode("utf-8")).decode().strip()
        git(root, "update-index", "--cacheinfo", f"{mode},{sha},{path}")
        done.append("index")
    if new_work is not None:
        work.write_bytes(new_work.encode("utf-8"))
        done.append("working tree")
    if not done:
        return f"already present in the index and the working tree: {path}"
    return f"ledger entry added to {' and '.join(done)}: {path}\nstaged: only the entry. Commit it with commit_paths.py."


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Add a rulings-ledger entry; stage only the entry.")
    ap.add_argument("entry", help="the full entry line, starting with '- **('")
    ap.add_argument("--repo", type=Path, default=Path.cwd(), help="any folder inside the repository (default: cwd)")
    ap.add_argument("--file", default=LEDGER, help=f"ledger path in the repo (default: {LEDGER})")
    ap.add_argument("--anchor", default=ANCHOR, help="the line the entry goes before")
    a = ap.parse_args(argv)
    try:
        print(ledger_add(a.repo, a.entry, a.file, a.anchor))
    except (Refuse, OSError, UnicodeDecodeError) as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    sys.exit(main())
