# orchestrator

Small scripts for steps the Eurobound sessions repeat by hand and sometimes get wrong (author, 2026-11-14: "should develop hooks for repeatable actions"; bead Eurobound-nwqs). Several sessions share one working tree and one git index, so most of these exist to keep one session from committing or overwriting another's work.

Run everything from the repository root with `python -I`. All scripts use the standard library only. A script that refuses prints `REFUSED: <reason>` and exits 2 without changing anything.

| Step | Script |
|---|---|
| Commit my files and nothing else | `commit_paths.py` |
| Add a rulings-ledger entry | `ledger_add.py` |
| See what the bead page needs | `sync_check.py` |
| Run the GUT suite | `gut.py` |
| File a bead | `bead_new.py` |

`hooks.py` holds the proposed Claude Code hooks. It is **not installed**; see `HOOKS_PROPOSAL.md`.

## commit_paths.py

```bash
python -I Tools/orchestrator/commit_paths.py <paths-file> <message-file> [--dry-run]
```

Commits exactly the paths listed in `<paths-file>` (one per line) with the message in `<message-file>`, then prints the commit's stat. It never pushes. Commit only when the author asks (root `CLAUDE.md`, Git).

- It refuses if anything outside the list is already staged, and prints what is. Unstage those files or ask the session that staged them.
- A line may be absolute, use backslashes, or be quoted. The file may start with a BOM or be UTF-16, which is what `>` writes in Windows PowerShell 5.1.
- Git tracks `Tools/`, but the folder on disk is `tools/`. Each path is matched against `git ls-files` first and the filesystem second, so either spelling works and a new file is added under git's spelling.
- List files, not folders. A deleted file is listed by its old path.
- The message is used as written. Nothing is appended, so put any trailer lines in the message file yourself.
- `--dry-run` resolves the paths and runs the staged check without staging anything.

## ledger_add.py

```bash
python -I Tools/orchestrator/ledger_add.py "- **(Author, chat, 2026-11-14; Eurobound-xxxx) Subject: \"verbatim words\".** What it means."
```

Puts the entry in `docs/superpowers/NEXT_WORK.md` after the last entry above `## Resolved (moved 2026-11-11 by Eurobound-j50)`.

Other sessions keep uncommitted edits in that file, so `git add` would stage their work with yours. The script writes the entry to the working tree file, and separately to a blob built from the index version, so the staged change is your entry alone. Two calls before one commit keep both entries. Then commit with `commit_paths.py`, listing `docs/superpowers/NEXT_WORK.md`.

It refuses if the anchor line is missing from either version. An entry that is already there is not added twice. In PowerShell, put an entry that contains double quotes in a variable or use Git Bash, so the quotes survive.

## sync_check.py

```bash
python -I Tools/orchestrator/sync_check.py          # export, print what is pending
python -I Tools/orchestrator/sync_check.py --ack    # after the ArtifactData batch succeeded
```

Runs `Tools/beads_board/sync_board.py` and prints one short block: the doc ids to `set` with their file paths, and the doc ids to delete. The write itself is yours: `ArtifactData list` for the versions, then one `batch`, as in `Tools/beads_board/README.md`.

`sync_board.py` forgets a change once it has reported it. This script remembers unwritten doc ids in `Tools/beads_board/out/pending.json` and repeats them until you run `--ack`. One run takes about 26 seconds. Exit code 0 means nothing is pending, 1 means something is.

## gut.py

```bash
python -I Tools/orchestrator/gut.py                  # whole suite
python -I Tools/orchestrator/gut.py --import         # rebuild the class cache first
python -I Tools/orchestrator/gut.py --select wallet  # test scripts whose name contains "wallet"
```

Prints the totals, the failing tests, and any script errors. The full output goes to `%TEMP%/eurobound_gut_last.log`; search it, don't read it whole.

- Use `--import` after a pull, a merge, a new worktree, or a new or renamed `class_name`. A stale `game/.godot` class cache broke 5 tests on 2026-11-14.
- A test that throws a script error stops at that line but still counts as passing, so the script lists script errors and exits 1 when there are any. GUT's own loader error on every run (`gut_loader.gd:35`) is left out.
- Godot is always gone when the script returns. On a timeout (`--timeout`, default 900 s) or Ctrl+C it kills the process tree it started. It never touches a Godot it did not start, such as the author's editor.
- The whole suite takes about two minutes. Set `GODOT_BIN` to use another binary.

## bead_new.py

```bash
python -I Tools/orchestrator/bead_new.py "Title" \
  --acceptance "What done looks like" --agent tools-programmer --effort low \
  --found-by Eurobound-xxxx --discovered-from Eurobound-xxxx \
  --labels "bug,tooling" --skills "tdd" < description.txt
```

A wrapper round `bd create` for the "File what you find" rule. The description comes from stdin. It requires `--acceptance`, `--agent`, `--effort` and `--found-by`, writes them to the metadata, adds the `agent:` and `effort:` labels, and never passes an assignee. It prints the new bead id.

An `author-ruling` bead needs its question and 2 to 4 options, or it is refused:

```bash
... --labels author-ruling --ask-question "Which shape?" \
    --ask-option "Dictionary" --ask-option "Array" --ask-recommended 1
```

Options are decisions or routes, never invented content. Three things stay with you: search first (`bd search`), post the question on the Eurobound Desk, and sync the bead page afterwards (`sync_check.py`).

## Tests

```bash
python -I -m unittest discover Tools/tests
```

`Tools/tests/test_orchestrator.py` covers `commit_paths`, `ledger_add`, `bead_new`, the GUT output parser, the pending list and the hook rules. Every git test builds its own temporary repository; none reads or writes this repository's index.
