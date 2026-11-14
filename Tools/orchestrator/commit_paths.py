#!/usr/bin/env python3
"""Commit exactly the listed paths, and nothing else.

    python -I Tools/orchestrator/commit_paths.py <paths-file> <message-file> [--repo DIR] [--dry-run] [--staged-only]

<paths-file> holds one path per line. Each line may be absolute or relative, use
backslashes, be quoted, or spell a folder in the wrong case (tools/ for Tools/);
the file may start with a BOM or be UTF-16 (Windows PowerShell 5.1 `>`).
<message-file> is the commit message, used as written (a BOM is stripped, nothing
is appended).

Refuses (exit 2, nothing changed) when:
  - anything outside the list is already staged (it prints what is);
  - a listed path is neither tracked (index or HEAD) nor on disk, is a directory, or is ambiguous;
  - the list or the message is empty, or there is nothing to commit.

A tracked path that is gone from disk (or removed with `git rm`) is committed as a deletion.
An untracked file whose on-disk folder case differs from git's (tools/ vs Tools/) is staged
under git's spelling with hash-object + update-index.

--staged-only commits exactly what is ALREADY staged for the listed paths (index content, not
the working tree) and stages nothing; it refuses if anything outside the list is staged or
nothing is staged. For ledger_add.py entries and hand-staged hunks.

Prints the new commit's stat. Never pushes. Standard library only.
"""
from __future__ import annotations

import argparse
import os
import re
import stat
import subprocess
import sys
import tempfile
from pathlib import Path


class Refuse(Exception):
    """A reason not to commit. Nothing has been changed when this is raised."""


def git(repo: Path, *args: str, stdin: bytes | None = None, check: bool = True) -> str:
    p = subprocess.run(["git", "-C", str(repo), *args], input=stdin, capture_output=True)
    if check and p.returncode != 0:
        raise Refuse(f"git {' '.join(args)} failed:\n{p.stderr.decode('utf-8', 'replace').strip()}")
    return p.stdout.decode("utf-8", "replace")


def read_text(path: Path) -> str:
    """Decode a text file, dropping a UTF-8 or UTF-16 BOM."""
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig")


def _slashes(p: str) -> str:
    p = p.replace("\\", "/")
    m = re.match(r"^/([a-zA-Z])/(.*)$", p)  # Git Bash form: /c/Users/... -> C:/Users/...
    if m:
        p = f"{m.group(1).upper()}:/{m.group(2)}"
    return p


def normalize(line: str, root: str) -> str:
    """One line of the paths file -> a repo-relative, forward-slash path ('' for a blank line)."""
    p = line.replace("\ufeff", "").strip().strip('"').strip("'").strip()
    if not p:
        return ""
    p = _slashes(p)
    r = _slashes(root).rstrip("/")
    if p.casefold() == r.casefold():
        raise Refuse(f"'{line.strip()}' is the repository root, not a file")
    if p.casefold().startswith(r.casefold() + "/"):
        p = p[len(r) + 1:]
    elif re.match(r"^([a-zA-Z]:)?/", p):
        raise Refuse(f"'{line.strip()}' is outside the repository ({root})")
    while p.startswith("./"):
        p = p[2:]
    p = re.sub(r"/+", "/", p)
    if ".." in p.split("/"):
        raise Refuse(f"'{line.strip()}' contains '..'")
    return p


def _on_disk(root: Path, rel: str) -> tuple[str, bool] | None:
    """The path as the filesystem spells it, matched case-insensitively, and whether it is a directory."""
    cur, parts = root, []
    for part in rel.split("/"):
        try:
            names = os.listdir(cur)
        except OSError:
            return None
        hit = part if part in names else next((n for n in names if n.casefold() == part.casefold()), None)
        if hit is None:
            return None
        parts.append(hit)
        cur = cur / hit
    return "/".join(parts), cur.is_dir()


def resolve(rel: str, tracked: list[str], root: Path, staged_only: bool = False) -> str:
    """Spell `rel` the way git should see it: the index's case first, the filesystem's second."""
    if rel in tracked:
        return rel
    same = sorted({t for t in tracked if t.casefold() == rel.casefold()})
    if len(same) == 1:
        return same[0]
    if len(same) > 1:
        raise Refuse(f"'{rel}' matches more than one tracked path: {', '.join(same)}")
    if staged_only:
        raise Refuse(f"'{rel}' is not tracked or staged, so --staged-only has nothing to commit for it")
    disk = _on_disk(root, rel)
    if disk is None:
        raise Refuse(f"'{rel}' is not tracked and not on disk")
    spelled, is_dir = disk
    if is_dir:
        raise Refuse(f"'{rel}' is a directory; list its files one per line")
    # Untracked file: keep git's spelling for every parent folder git already knows (Tools/, not tools/).
    dirs: dict[str, str] = {}
    for t in tracked:
        bits = t.split("/")[:-1]
        for n in range(1, len(bits) + 1):
            d = "/".join(bits[:n])
            dirs.setdefault(d.casefold(), d)
    bits = spelled.split("/")
    for n in range(len(bits) - 1, 0, -1):
        known = dirs.get("/".join(bits[:n]).casefold())
        if known:
            return "/".join([known, *bits[n:]])
    return spelled


def staged(repo: Path) -> list[str]:
    return [p for p in git(repo, "diff", "--cached", "--name-only", "-z").split("\0") if p]


def _stage_under_git_spelling(root: Path, rel: str) -> None:
    """Stage an untracked file under `rel` (git's folder spelling) when the disk spells it differently."""
    disk = _on_disk(root, rel)
    if disk is None or disk[0] == rel:
        return  # same spelling: a plain `git add` handles it
    f = root / disk[0]
    st = os.lstat(f)
    if stat.S_ISLNK(st.st_mode):
        mode = "120000"
        sha = git(root, "hash-object", "-w", "--stdin", stdin=os.readlink(f).encode("utf-8")).strip()
    elif stat.S_ISREG(st.st_mode):
        mode = "100755" if st.st_mode & 0o111 else "100644"
        sha = git(root, "hash-object", "-w", f"--path={rel}", str(f)).strip()
    else:
        raise Refuse(f"'{rel}' is not a regular file or symlink; cannot stage it under git's spelling")
    git(root, "update-index", "--add", "--cacheinfo", f"{mode},{sha},{rel}")


def commit_paths(repo: Path, paths_file: Path, message_file: Path, dry_run: bool = False,
                 staged_only: bool = False) -> str:
    root = Path(git(repo, "rev-parse", "--show-toplevel").strip())
    message = read_text(message_file).replace("\r\n", "\n").strip("\n")
    if not message.strip():
        raise Refuse(f"the message file is empty: {message_file}")

    tracked = [p for p in git(root, "ls-files", "-z").split("\0") if p]
    in_index = set(tracked)
    head = git(root, "ls-tree", "-r", "--name-only", "-z", "HEAD", check=False)
    tracked = sorted(in_index | {p for p in head.split("\0") if p})  # HEAD too: `git rm`'d paths
    wanted: list[str] = []
    for line in read_text(paths_file).splitlines():
        rel = normalize(line, str(root))
        if rel:
            got = resolve(rel, tracked, root, staged_only)
            if got not in wanted:
                wanted.append(got)
    if not wanted:
        raise Refuse(f"the paths file lists nothing: {paths_file}")

    listed = {w.casefold() for w in wanted}
    extra = [s for s in staged(root) if s.casefold() not in listed]
    if extra:
        raise Refuse("other files are already staged; unstage them or add them to the list:\n  "
                     + "\n  ".join(extra))
    if dry_run:
        return "would commit:\n  " + "\n  ".join(wanted)

    NUL = chr(0)
    spec = NUL.join(wanted).encode("utf-8")
    lit = ("--literal-pathspecs",)
    if staged_only:
        if not staged(root):
            raise Refuse("nothing is staged for the listed paths; stage the hunk first (nothing was committed)")
        with tempfile.TemporaryDirectory() as tmp:
            msg = Path(tmp) / "message.txt"
            msg.write_bytes((message + "\n").encode("utf-8"))
            git(root, "commit", "--cleanup=whitespace", "-F", str(msg))
        return git(root, "show", "--stat", "--format=%h %s", "HEAD").strip()
    for w in wanted:
        if w not in in_index:
            _stage_under_git_spelling(root, w)
    # A path that is only in HEAD (already `git rm`'d) is staged as a deletion already; `add` would not match it.
    addable = [w for w in wanted if w in in_index or _on_disk(root, w) is not None]
    if addable:
        git(root, *lit, "add", "-A", "--pathspec-from-file=-", "--pathspec-file-nul",
            stdin=NUL.join(addable).encode("utf-8"))
    now = staged(root)
    extra = [s for s in now if s.casefold() not in listed]
    if extra:  # another session staged something between the check and the add
        raise Refuse("other files were staged while this ran; nothing committed:\n  " + "\n  ".join(extra))
    if not now:
        raise Refuse("nothing to commit: the listed paths have no changes")

    with tempfile.TemporaryDirectory() as tmp:
        msg = Path(tmp) / "message.txt"
        msg.write_bytes((message + "\n").encode("utf-8"))
        git(root, *lit, "commit", "--only", "--cleanup=whitespace", "-F", str(msg),
            "--pathspec-from-file=-", "--pathspec-file-nul", stdin=spec)
    return git(root, "show", "--stat", "--format=%h %s", "HEAD").strip()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Commit exactly the listed paths. Never pushes.")
    ap.add_argument("paths_file", type=Path)
    ap.add_argument("message_file", type=Path)
    ap.add_argument("--repo", type=Path, default=Path.cwd(), help="any folder inside the repository (default: cwd)")
    ap.add_argument("--dry-run", action="store_true", help="resolve and check, but stage and commit nothing")
    ap.add_argument("--staged-only", action="store_true",
                    help="commit exactly what is already staged for the listed paths (index content); stage nothing")
    a = ap.parse_args(argv)
    try:
        print(commit_paths(a.repo, a.paths_file, a.message_file, a.dry_run, a.staged_only))
    except Refuse as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        return 2
    except OSError as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    sys.exit(main())
