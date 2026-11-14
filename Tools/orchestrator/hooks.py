#!/usr/bin/env python3
"""Claude Code hook entry points for the repeatable-action rules. NOT INSTALLED.

Nothing runs this until the author approves the entries in HOOKS_PROPOSAL.md and they
are added to .claude/settings.json. Each mode reads the hook's JSON from stdin and
prints a JSON decision (or nothing, which means "carry on").

    python -I Tools/orchestrator/hooks.py pre-bash        # PreToolUse, matcher Bash
    python -I Tools/orchestrator/hooks.py post-bash       # PostToolUse, matcher Bash
    python -I Tools/orchestrator/hooks.py session-start   # SessionStart

pre-bash denies, with the fix in the reason:
  - `git commit` with no pathspec while files are staged, and `git commit -a`;
  - `git add -A`, `git add .`, `git add -u` (they stage other sessions' work);
  - `git add docs/superpowers/NEXT_WORK.md` (stages other sessions' ledger edits);
  - a raw gut_cmdln.gd run (floods the context; use gut.py).
post-bash adds a reminder for Claude:
  - after a bead write (bd create/update/close/...): sync the bead page, at most once
    every 10 minutes per session;
  - after git pull/merge/rebase/checkout/switch: the class cache may be stale.
session-start runs sync_check.py once and passes its block to the session.

A hook that breaks must never block work: any error here exits 0 with no output.
Scripts started with subprocess (commit_paths.py, ledger_add.py) are not Bash tool
calls, so these rules do not apply to them. Standard library only.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
LEDGER = "docs/superpowers/next_work.md"
TOOLS = "Tools/orchestrator"
GIT = r"(?:^|[;&|(\n]\s*)git(?:\s+-[cC]\s+\S+)*\s+"
BEAD_WRITE = re.compile(r"(?:^|[;&|(\n]\s*)bd\s+(create|new|update|close|reopen|delete|dep|label|comments\s+add)\b"
                        r"|bead_new\.py")
CACHE_RISK = re.compile(GIT + r"(pull|merge|rebase|checkout|switch|stash\s+pop)\b")


def _head(command: str, sub: str) -> str | None:
    """The text after `git <sub>` up to the first quote or line end (flags and paths, not the message)."""
    m = re.search(GIT + sub + r"\b([^\n\"']*)", command)
    return None if m is None else m.group(1)


def _rest(command: str, sub: str) -> str:
    m = re.search(GIT + sub + r"\b", command)
    return "" if m is None else command[m.end():]


def pre_bash(command: str, staged: list[str]) -> str | None:
    """A reason to deny this Bash command, or None to allow it."""
    if "gut_cmdln" in command and "gut.py" not in command:
        return (f"Run GUT with `python -I {TOOLS}/gut.py` (add --import after a pull or a new class_name). "
                "It prints only the totals and failing tests, logs the rest to a file, and never leaves Godot running.")

    head = _head(command, "add")
    if head is not None:
        tokens = head.replace("\\", "/").split()
        if any(t in ("-A", "--all", ".", "-u", "--update", "*", ":/") for t in tokens):
            return ("`git add` of everything stages other sessions' work. Stage named files only, or use "
                    f"`python -I {TOOLS}/commit_paths.py <paths-file> <message-file>`.")
        if any(t.strip("\"'").casefold().endswith(LEDGER) for t in tokens):
            return ("Other sessions keep uncommitted edits in the rulings ledger; `git add` would stage them. "
                    f"Use `python -I {TOOLS}/ledger_add.py \"<entry>\"`, which stages only your entry.")

    head = _head(command, "commit")
    if head is not None:
        rest = _rest(command, "commit")
        if any("a" in cluster for cluster in re.findall(r"(?<=\s)-([a-zA-Z]+)\b", " " + head)) or "--all" in head:
            return ("`git commit -a` commits every modified file, including other sessions' work. Use "
                    f"`python -I {TOOLS}/commit_paths.py <paths-file> <message-file>`.")
        has_paths = bool(re.search(r"\s--\s+\S", rest) or re.search(r"\s(--only|-o|--pathspec-from-file\S*)\b", rest))
        if not has_paths and staged:
            shown = "\n  ".join(staged[:15]) + (f"\n  ... and {len(staged) - 15} more" if len(staged) > 15 else "")
            return ("`git commit` with no pathspec commits everything staged, and several sessions share this "
                    f"index. Staged now:\n  {shown}\nCommit your own files with "
                    f"`python -I {TOOLS}/commit_paths.py <paths-file> <message-file>`, or pass `-- <paths>`.")
    return None


def post_bash(command: str) -> list[str]:
    """Reminders for Claude after this Bash command ran."""
    notes = []
    if BEAD_WRITE.search(command):
        notes.append(f"BEAD_SYNC: beads changed. Before you finish, run `python -I {TOOLS}/sync_check.py`, write the "
                     "docs it lists to the bead page (Tools/beads_board/README.md, Sync), then `sync_check.py --ack`.")
    if CACHE_RISK.search(command):
        notes.append("CLASS_CACHE: the checkout changed, so game/.godot may be stale. Run the next GUT suite with "
                     f"`python -I {TOOLS}/gut.py --import`.")
    return notes


def _throttled(session: str, key: str, seconds: int = 600) -> bool:
    """True if this session was already reminded about `key` within `seconds`."""
    mark = Path(tempfile.gettempdir()) / f"eurobound_hook_{re.sub(r'[^A-Za-z0-9_-]', '_', session)[:60]}_{key}"
    try:
        if mark.exists() and time.time() - mark.stat().st_mtime < seconds:
            return True
        mark.write_text("", encoding="utf-8")
    except OSError:
        pass
    return False


def _emit(event: str, **fields) -> None:
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event, **fields}}))


def main(argv: list[str]) -> int:
    mode = argv[0] if argv else ""
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        data = {}
    command = str((data.get("tool_input") or {}).get("command") or "")
    session = str(data.get("session_id") or "none")

    if mode == "pre-bash":
        staged: list[str] = []
        if re.search(GIT + r"commit\b", command):
            p = subprocess.run(["git", "-C", str(REPO), "diff", "--cached", "--name-only"],
                               capture_output=True, text=True, encoding="utf-8", timeout=10)
            staged = [s for s in p.stdout.splitlines() if s]
        reason = pre_bash(command, staged)
        if reason:
            _emit("PreToolUse", permissionDecision="deny", permissionDecisionReason=reason)
    elif mode == "post-bash":
        notes = [n for n in post_bash(command) if not _throttled(session, n.split(":")[0])]
        if notes:
            _emit("PostToolUse", additionalContext="\n".join(notes))
    elif mode == "session-start":
        p = subprocess.run([sys.executable, "-I", str(HERE / "sync_check.py")],
                           capture_output=True, text=True, encoding="utf-8", timeout=90)
        if p.returncode == 1 and p.stdout.strip():
            _emit("SessionStart", additionalContext=p.stdout.strip())
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception:  # a broken hook must not block the session
        sys.exit(0)
