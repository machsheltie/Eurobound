#!/usr/bin/env python3
"""Create a bead with the house rules enforced (root CLAUDE.md, "File what you find").

    python -I Tools/orchestrator/bead_new.py "Title" --acceptance "What done looks like" \
        --agent tools-programmer --effort low --found-by Eurobound-nwqs \
        [--skills "tdd, code-review"] [--labels tooling,bug] [--discovered-from Eurobound-nwqs] \
        [-p 2] [-t task] [--dry-run] < description.txt

The description comes from stdin and is written for a cold reader. Run from the
repository root. The wrapper:
  - requires --acceptance, --agent, --effort and --found-by;
  - writes metadata {agent, effort, found_by} and adds the agent:/effort: labels;
  - adds a discovered-from dependency when --discovered-from is given;
  - never passes an assignee (bd derives machsheltie from git);
  - refuses an `author-ruling` bead without an ask: --ask-question plus 2-4
    --ask-option values (mark at most one with --ask-recommended N, counted from 1).

Search first (`bd search`) to avoid a duplicate. An author-ruling bead also needs its
question on the Eurobound Desk (Tools/beads_board/README.md); this does not post it.
Prints the new bead id. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EFFORTS = ("low", "medium", "high", "xhigh", "max")
RULING = "author-ruling"


class Refuse(Exception):
    """A house rule the request breaks. Nothing has been created when this is raised."""


def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Create a bead with the Eurobound house rules enforced.")
    ap.add_argument("title")
    ap.add_argument("--acceptance", required=True, help="what complete looks like")
    ap.add_argument("--agent", required=True, help="agent type that should do the work, e.g. tools-programmer")
    ap.add_argument("--effort", required=True, choices=EFFORTS)
    ap.add_argument("--found-by", required=True, help="bead id or session that found the work")
    ap.add_argument("--skills", default="", help="real skill names, comma-separated")
    ap.add_argument("--labels", default="", help="extra labels, comma-separated")
    ap.add_argument("--discovered-from", default="", help="bead id this work came out of")
    ap.add_argument("-p", "--priority", default="2")
    ap.add_argument("-t", "--type", default="task")
    ap.add_argument("--ask-question", default="", help="author-ruling: the question for the author")
    ap.add_argument("--ask-option", action="append", default=[], help="author-ruling: one option (2-4 of these)")
    ap.add_argument("--ask-recommended", type=int, default=0, help="which option is recommended (1-based)")
    ap.add_argument("--dry-run", action="store_true", help="print the bd command and metadata; create nothing")
    return ap


def build(a: argparse.Namespace, description: str) -> tuple[list[str], dict]:
    """The `bd create` arguments (without --metadata) and the metadata object."""
    for name in ("title", "acceptance", "agent", "found_by"):
        if not str(getattr(a, name)).strip():
            raise Refuse(f"--{name.replace('_', '-')} is empty" if name != "title" else "the title is empty")
    if not description.strip():
        raise Refuse("the description is empty; pipe it in on stdin, written for a cold reader")

    labels = []
    for label in [f"agent:{a.agent.strip()}", f"effort:{a.effort}", *a.labels.split(",")]:
        label = label.strip()
        if label and label not in labels:
            labels.append(label)

    meta: dict = {"agent": a.agent.strip(), "effort": a.effort, "found_by": a.found_by.strip()}
    question = a.ask_question.strip()
    options = [o.strip() for o in a.ask_option if o.strip()]
    if RULING in labels or question or options:
        if not question:
            raise Refuse(f"an {RULING} bead needs --ask-question (the question the author must answer)")
        if not 2 <= len(options) <= 4:
            raise Refuse(f"an {RULING} bead needs 2 to 4 --ask-option values; got {len(options)}")
        if len(set(options)) != len(options):
            raise Refuse("the --ask-option values must differ from each other")
        if not 0 <= a.ask_recommended <= len(options):
            raise Refuse(f"--ask-recommended must be between 1 and {len(options)}")
        if RULING not in labels:
            labels.append(RULING)
        meta["ask"] = {"question": question,
                       "options": [{"label": o, "recommended": n == a.ask_recommended}
                                   for n, o in enumerate(options, 1)]}

    argv = ["create", a.title.strip(), "--stdin", "--acceptance", a.acceptance.strip(),
            "--labels", ",".join(labels), "--priority", str(a.priority), "--type", a.type, "--silent"]
    if a.skills.strip():
        argv += ["--skills", a.skills.strip()]
    if a.discovered_from.strip():
        argv += ["--deps", f"discovered-from:{a.discovered_from.strip()}"]
    return argv, meta


def run_bd(argv: list[str], description: str) -> subprocess.CompletedProcess:
    bd = shutil.which("bd") or shutil.which("bd.cmd") or "bd"
    return subprocess.run([bd, *argv], input=description, capture_output=True, text=True, encoding="utf-8")


def create(a: argparse.Namespace, description: str) -> str:
    argv, meta = build(a, description)
    if a.dry_run:
        return "bd " + " ".join(argv) + "\nmetadata: " + json.dumps(meta, ensure_ascii=False)
    # Metadata goes through a file: nested JSON does not survive Windows command-line quoting.
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "metadata.json"
        f.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
        p = run_bd([*argv, "--metadata", f"@{f}"], description)
    if p.returncode != 0:
        raise Refuse(f"bd create failed:\n{(p.stderr or p.stdout).strip()}")
    return p.stdout.strip()


def main(argv: list[str] | None = None, stdin: str | None = None) -> int:
    a = parser().parse_args(argv)
    if stdin is None:
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8-sig")
        stdin = "" if sys.stdin.isatty() else sys.stdin.read()
    try:
        print(create(a, stdin.replace("﻿", "")))
    except Refuse as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    sys.exit(main())
