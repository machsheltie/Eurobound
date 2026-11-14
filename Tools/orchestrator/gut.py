#!/usr/bin/env python3
"""Run the headless GUT suite and print only the totals and the failing tests.

    python -I Tools/orchestrator/gut.py                 # whole suite (res://tests/unit)
    python -I Tools/orchestrator/gut.py --import        # rebuild the class cache first
    python -I Tools/orchestrator/gut.py --select arcade # only test scripts whose name contains "arcade"

Use --import after a pull, a merge, a fresh worktree, or any change that adds or
renames a GDScript `class_name`: a stale game/.godot class cache broke 5 tests on
2026-11-14. The full output goes to a log file (path printed); read it with a filter
(`grep -n FAILED`), never whole.

Godot is started by this script and is always gone when it returns: on a timeout or
Ctrl+C its whole process tree is killed. It never touches a Godot it did not start.
Exit code: 0 all passed, 1 failures or script errors, 2 could not run.
Set GODOT_BIN to use another binary. Standard library only.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GODOT = "C:/Users/heirr/Downloads/Godot_v4.7.2-stable_win64.exe/Godot_v4.7.2-stable_win64_console.exe"
ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
TOTAL = re.compile(r"^(Scripts|Tests|Passing|Failing|Pending|Risky|Passing Tests|Failing Tests|Risky Tests|"
                   r"Pending Tests|Risky/Pending|Asserts|Orphans|Time)\s+\S+$")
ERROR = re.compile(r"SCRIPT ERROR|Parse Error|Could not find type|Failed to load script|Could not preload")


def parse(output: str) -> dict:
    """Totals, failing tests and script errors from GUT's command-line output."""
    lines = [ANSI.sub("", raw).rstrip() for raw in output.splitlines()]
    start = max((n for n, line in enumerate(lines) if "Run Summary" in line), default=None)
    totals, failing, script, test = [], [], "", ""
    for line in ([] if start is None else lines[start:]):
        s = line.strip()
        if s.startswith("res://") and s.endswith(".gd"):
            script, test = s, ""
        elif s.startswith("- "):
            test = s[2:].strip()
        elif s.startswith("[Failed]"):
            name = f"{script} :: {test}" if test else script
            if name and name not in failing:
                failing.append(name)
        elif TOTAL.match(s):
            totals.append(re.sub(r"\s+", " ", s))
    errors = []
    for n, line in enumerate(lines):
        if not ERROR.search(line):
            continue
        at = lines[n + 1].strip() if n + 1 < len(lines) and lines[n + 1].strip().startswith("at:") else ""
        if "res://addons/gut/" in at:  # GUT's own loader logs one on every run
            continue
        entry = f"{line.strip()} {at}".strip()
        if entry not in errors:
            errors.append(entry)
    return {"summary": start is not None, "totals": totals, "failing": failing, "errors": errors}


def render(r: dict, log: Path) -> str:
    out = []
    if not r["summary"]:
        out.append("GUT: no run summary found; the suite did not finish")
    out.append("GUT: " + ("; ".join(r["totals"]) if r["totals"] else "no totals"))
    if r["failing"]:
        out.append(f"failing ({len(r['failing'])}):")
        out += [f"  {name}" for name in r["failing"][:40]]
        if len(r["failing"]) > 40:
            out.append(f"  ... and {len(r['failing']) - 40} more")
    if r["errors"]:
        out.append(f"script errors ({len(r['errors'])}); a test that errors can still count as passing. "
                   "If they name a missing class, re-run with --import:")
        out += [f"  {e[:260]}" for e in r["errors"][:8]]
    out.append(f"log: {log}")
    return "\n".join(out)


def run(cmd: list[str], log: Path, timeout: int, mode: str = "w") -> tuple[int | None, str]:
    """Run Godot to completion, or kill its whole tree. Returns (exit code or None on timeout, output)."""
    with open(log, mode, encoding="utf-8", errors="replace") as f:
        p = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        try:
            code = p.wait(timeout=timeout)
        except (subprocess.TimeoutExpired, KeyboardInterrupt):
            code = None
        finally:
            if p.poll() is None:
                if os.name == "nt":
                    subprocess.run(["taskkill", "/PID", str(p.pid), "/T", "/F"], capture_output=True)
                else:
                    p.kill()
                p.wait(timeout=30)
    return code, log.read_text(encoding="utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Headless GUT run: totals and failing tests only.")
    ap.add_argument("--import", dest="do_import", action="store_true", help="rebuild the .godot class cache first")
    ap.add_argument("--dir", default="res://tests/unit", help="test folder (default: res://tests/unit)")
    ap.add_argument("--select", default="", help="only run test scripts whose file name contains this")
    ap.add_argument("--timeout", type=int, default=900, help="seconds before Godot is killed (default: 900)")
    a = ap.parse_args(argv)

    godot = os.environ.get("GODOT_BIN", GODOT)
    if not Path(godot).is_file():
        print(f"GUT: Godot binary not found: {godot}", file=sys.stderr)
        return 2
    game = REPO / "game"
    log = Path(tempfile.gettempdir()) / "eurobound_gut_last.log"
    base = [godot, "--headless", "--path", str(game)]

    if a.do_import:
        code, _ = run([*base, "--import", "--quit"], log, a.timeout)
        if code is None:
            print(f"GUT: class-cache import timed out after {a.timeout}s; Godot was killed\nlog: {log}", file=sys.stderr)
            return 2
        print(f"class-cache import: exit {code}")

    cmd = [*base, "-s", "addons/gut/gut_cmdln.gd", f"-gdir={a.dir}", "-ginclude_subdirs", "-gexit"]
    if a.select:
        cmd.append(f"-gselect={a.select}")
    code, output = run(cmd, log, a.timeout, "a" if a.do_import else "w")
    r = parse(output)
    print(render(r, log))
    if code is None:
        print(f"GUT: timed out after {a.timeout}s; Godot was killed", file=sys.stderr)
        return 2
    if not r["summary"]:
        return 2
    return 1 if r["failing"] or r["errors"] or code != 0 else 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    sys.exit(main())
