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

`hooks.py` holds the Claude Code hooks. `pre-bash` (commit guard, raw-GUT stop) and `post-bash` (bead-page reminder) have been installed in `.claude/settings.json` since 2026-11-14. The `SessionStart` check is not installed. See `HOOKS_PROPOSAL.md`.

Every window does one task, writes a handoff and is then cleared (author, 2026-11-15, Eurobound-jpkw). The format is in "Handoffs and window names" below.

## commit_paths.py

```bash
python -I Tools/orchestrator/commit_paths.py <paths-file> <message-file> [--dry-run] [--staged-only]
```

Commits exactly the paths listed in `<paths-file>` (one per line) with the message in `<message-file>`, then prints the commit's stat. It never pushes. Commit only when the author asks (root `CLAUDE.md`, Git).

- It refuses if anything outside the list is already staged, and prints what is. Unstage those files or ask the session that staged them.
- A line may be absolute, use backslashes, or be quoted. The file may start with a BOM or be UTF-16, which is what `>` writes in Windows PowerShell 5.1.
- Git tracks `Tools/`, but the folder on disk is `tools/`. Each path is matched against `git ls-files` first and the filesystem second, so either spelling works and a new file is added under git's spelling.
- If the on-disk folder case differs from git's, an untracked file is staged under git's spelling (hash-object + update-index; the executable bit and symlinks are kept). A file it cannot stage that way is refused.
- List files, not folders. A deleted file is listed by its old path; a path tracked but gone from disk, or removed with `git rm`, is committed as a deletion.
- `--staged-only` commits exactly what is ALREADY staged for the listed paths (index content, not the working tree) and stages nothing. Use it for ledger entries added by `ledger_add.py` and for hand-staged hunks, where the working-tree file also holds another session's edits. It refuses if anything outside the list is staged, or if nothing is staged.
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
- The whole suite takes about two minutes. Godot is taken from the environment variable `GODOT_BIN` (full path to the console binary), else `godot` on PATH. Set it once per machine, e.g. PowerShell `setx GODOT_BIN "<full path to Godot_v4.7.2-stable_win64_console.exe>"` (new terminals pick it up), or `export GODOT_BIN=...` in Git Bash. Do not write that path into a tracked file: the repository is public. If the variable is not set, `gut.py` reads the path from `Tools/orchestrator/godot_bin.local` (one line, untracked), so every session on this machine works without setting anything.

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

**An `author-ruling` bead must also go on the Eurobound Desk** (author, 2026-11-16). `bead_new.py` only stores the question in `metadata.ask`; the bead page no longer takes answers. Post `questions/<bead-id>-q<n>` on the Desk from that `metadata.ask`, mark the bead `blocked` and add the "Waiting on Eurobound Desk" comment. The steps are in `Tools/beads_board/README.md`, "Author-ruling beads".

## Handoffs and window names

Author, 2026-11-15 (Desk playtest note, Eurobound-jpkw), verbatim: "One task. Then handoff and clear context. There's zero reason to run on like this." Every window and every agent does ONE task, writes a handoff, tells the Production Desk Orchestrator, and stops. The author then clears the window. Window names survive `/clear`, so the next task reaches the same name as a fresh start.

**Where:** `docs/handoffs/<date>_<window_slug>_<task>.md`, e.g. `docs/handoffs/2026-11-17_beads_deployment_team_f3tq.md`. The slug is the window name in snake_case. The task part is the bead id or a short slug. Leave it off only when the handoff closes the window for good.

**Shape** (taken from the 2026-11-17 handoffs):

```markdown
# Handoff: <Window Name>, <task in a few words> (<date>)

**Window name: <Window Name>.** <Who assigned the task, and what it was.> **Done. This window can be cleared.** <Anything still running, or "Nothing is running.">

## What was done
<One line or row per change: file:line, bead id, Desk card id, and the author's answer verbatim where one was used.>

## Checks
<What was run and its result: validate_data, the GUT count, canon_index build, the bead-page sync. Say plainly when something was not run, and why.>

## Committed / Uncommitted (this task)
<Commit SHAs, or "Not committed", with the list of files this window changed. Name any file that also holds another window's edits.>

## Open, and next for whoever takes the name
<What is still open, the first step for the next session, and the beads and Desk cards involved.>
```

**Rules**
- The window name comes first, both in the heading and in the bold first line. The mobile app may not show which window is which (see "Window names on mobile" below).
- List every bead created, updated or closed, and every Desk card posted.
- Quote author answers verbatim, never paraphrased. Never write user-profile or scratchpad paths: the repo is public.
- Then SendMessage the Production Desk Orchestrator. The message gives the per-bead results, the handoff path and "This window can be cleared".

**Window names on mobile**

A Claude Code session can carry a title that the Claude mobile app shows. According to the Claude Code docs (checked 2026-11-17: code.claude.com/docs/en/sessions.md, remote-control.md, cli-reference.md):

- **Set it at launch:** `claude --name "<Window Name>"` (or `-n`).
- **Set it inside a running session:** type `/rename <Window Name>`, or press Ctrl+R on the session in the session picker. The name shows on the prompt bar.
- **It survives `/clear`** when `/clear` is run with no argument. (`/clear <name>` labels the old conversation instead, and the new session starts unnamed, so never pass a name to `/clear`.) An auto-generated title does not survive `/clear`.
- **On mobile:** Remote Control sessions list under their name in claude.ai/code and in the Claude app's Code tab. The name comes from `--name`, then `/rename`, then an auto-generated one. Renaming a session from claude.ai or the app also renames it in the CLI (Claude Code v2.1.221 or later). The docs don't say whether a plain claude.ai/code web session shows a CLI `/rename` name.
- **No environment variable** sets the name. `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX` only changes auto-generated Remote Control names.

So every window should be started with `--name`, or renamed once with `/rename`, to its exact window name (the name `ListAgents` shows and the Desk `window` field uses). Only the author can type `/rename`; an agent cannot run slash commands. As a backstop, the window name still comes first in every handoff and every cross-window message.

**Where the Desk relay lives (and what a restart must re-arm)**

The Eurobound Desk relay (Tools/beads_board/README.md, "Relay") runs in the **Production Desk Orchestrator** window. That is the head orchestrator the author named on 2026-11-15; the window was called "Absinthe Orchestrator" then. It has two parts, both session-only:

1. **A Desk watch with auto-replies armed** on https://claude.ai/artifact/Pm3AgZ5qHqqmcoRcEv52JF. The author's Send posts a "sent to Claude" comment, which wakes the window.
2. **A fallback cron at :17 and :47** (CronCreate). It catches any answer or playtest note the watch missed.

Both live only in that session. Session crons expire after **7 days**, and both stop when the window is cleared, restarted or closed. A new Production Desk Orchestrator session must re-arm both before doing anything else:

- (a) Watch the Desk artifact for comments, with auto-replies armed (ArtifactComments).
- (b) Create the :17/:47 fallback cron again. Its prompt is the relay steps in Tools/beads_board/README.md plus the playtest-note filing steps.
- (c) Run one relay pass at once. Query `questions` where `status == "answered"` and `relayed == false`, and `playtest_notes` where `status == "new"`, to catch anything that landed while nothing was watching.

If the window will run for more than 7 days, re-create the cron before it expires. No other window runs a relay or upkeep cron. The 2026-11-15 handoffs record the old per-team crons (bead upkeep, eurobound-c8, eurobound-ad) being stopped.

## Tests

```bash
python -I -m unittest discover Tools/tests
```

`Tools/tests/test_orchestrator.py` covers `commit_paths`, `ledger_add`, `bead_new`, the GUT output parser, the pending list and the hook rules. Every git test builds its own temporary repository; none reads or writes this repository's index.
