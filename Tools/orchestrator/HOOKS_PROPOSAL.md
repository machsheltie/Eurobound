# Hooks proposal (Eurobound-nwqs)

**Status: proposed, not installed.** Nothing in `.claude/settings.json` has changed. Hooks run in every session, so they wait for the author's answer on the Eurobound Desk (question `Eurobound-nwqs-q1`).

The scripts in this folder already work when a session chooses to run them. A hook covers the case where a session forgets. Three hooks are proposed. All three call `Tools/orchestrator/hooks.py`, which is written and tested but not wired to anything.

## 1. Commit guard

**What it does.** Before a session runs a shell command, it stops four commands that have picked up another session's work, and tells the session what to run instead:

| Stopped | Why | Told to use |
|---|---|---|
| `git commit` with no file list, while files are staged | It commits everything staged, and all sessions share one index | `commit_paths.py`, or `git commit ... -- <paths>` |
| `git commit -a` | It commits every modified file | `commit_paths.py` |
| `git add -A`, `git add .`, `git add -u` | They stage every session's files | `git add <named files>` |
| `git add docs/superpowers/NEXT_WORK.md` | It stages other sessions' ledger edits | `ledger_add.py` |

A commit that names its files still goes through, and so does every other git command.

**Cost.** A few milliseconds on each shell command; one `git diff --cached` when the command is a commit.

**Limit.** It reads the command text, so an unusual spelling can slip past it. When it cannot tell, it allows the command.

Add to the `hooks` array of the existing `PreToolUse` entry whose `matcher` is `"Bash"`:

```json
{
  "type": "command",
  "command": "python -I \"$CLAUDE_PROJECT_DIR/Tools/orchestrator/hooks.py\" pre-bash",
  "timeout": 15
}
```

## 2. GUT guard

**What it does.** Two things:

- It stops a raw `gut_cmdln.gd` run and points the session at `gut.py`. A raw run puts about 1,400 lines in the session's context and can leave Godot running.
- After `git pull`, `merge`, `rebase`, `checkout` or `switch`, it tells the session that the class cache may be stale and the next GUT run needs `gut.py --import`. That is the step that was missed on 2026-11-14, when 5 tests broke.

**Cost.** A few milliseconds on each shell command.

The first half is part of the `pre-bash` command in hook 1, so it needs no extra entry. For the second half, add a new entry to `PostToolUse`:

```json
{
  "matcher": "Bash",
  "hooks": [
    {
      "type": "command",
      "command": "python -I \"$CLAUDE_PROJECT_DIR/Tools/orchestrator/hooks.py\" post-bash",
      "timeout": 10
    }
  ]
}
```

## 3. Bead page reminder

**What it does.** Two things:

- After a session creates, updates or closes a bead, it reminds that session to run `sync_check.py` and write the bead page before it finishes. It reminds at most once every 10 minutes per session. It is the same `post-bash` entry as hook 2.
- When a session starts, it runs `sync_check.py` once and tells the session if the bead page is behind.

**Cost.** The reminder is free. The start-up check adds about 26 seconds to each session start, run with a 90-second limit; a session can work while it runs only if the entry is marked `async`, and then the result is not shown to it, so it is not marked `async` here.

Add a new entry to `SessionStart`:

```json
{
  "hooks": [
    {
      "type": "command",
      "command": "python -I \"$CLAUDE_PROJECT_DIR/Tools/orchestrator/hooks.py\" session-start",
      "timeout": 90,
      "statusMessage": "Checking the bead page"
    }
  ]
}
```

## Not proposed

- **A check at Stop.** `sync_check.py` takes about 26 seconds, and a Stop hook runs each time any of the five sessions finishes a turn. The reminder in hook 3 reaches only the session that changed beads, and costs nothing.
- **Canon index rebuild.** `canon_index.py build` loads an embedding model. Running it from a hook would start that load in several sessions at once on a laptop that runs short of memory. It stays a manual step after editing design docs.
- **Ledger entry and bead creation as hooks.** They need words only the session has (the author's quote, the description), so they are scripts: `ledger_add.py` and `bead_new.py`.

## Everything at once

If the author picks "Add all of them", these are the three additions to `.claude/settings.json`. Existing entries stay as they are.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python -I \"$CLAUDE_PROJECT_DIR/Tools/orchestrator/hooks.py\" pre-bash",
            "timeout": 15
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python -I \"$CLAUDE_PROJECT_DIR/Tools/orchestrator/hooks.py\" post-bash",
            "timeout": 10
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python -I \"$CLAUDE_PROJECT_DIR/Tools/orchestrator/hooks.py\" session-start",
            "timeout": 90,
            "statusMessage": "Checking the bead page"
          }
        ]
      }
    ]
  }
}
```

For "Add only the commit guard", add the `PreToolUse` hook alone. It carries the raw-GUT stop from hook 2 with it, because both live in the `pre-bash` command.

## Installing (after the author says yes)

1. Read `.claude/settings.json` and merge the entries in; do not replace the file. The existing `PreToolUse` `Bash` entry already runs `validate-commit.sh` and `validate-push.sh`, and the new hook goes beside them.
2. Check the file still parses: `python -m json.tool .claude/settings.json`.
3. Pipe-test each mode. The first line should print a `deny` decision and the second should print nothing:
   ```bash
   echo '{"tool_name":"Bash","tool_input":{"command":"git add -A"}}' | python -I Tools/orchestrator/hooks.py pre-bash
   echo '{"tool_name":"Bash","tool_input":{"command":"git status"}}' | python -I Tools/orchestrator/hooks.py pre-bash
   ```
4. Running sessions pick the hooks up after `/hooks` is opened once or the session restarts.

**Turning one off:** delete its entry. If `hooks.py` itself fails, it exits quietly and the command goes ahead, so a broken hook cannot block a session.

Hooks 1 and 2 were pipe-tested on 2026-11-14 with the commands in step 3. The rules are covered by `HookRulesTest` in `Tools/tests/test_orchestrator.py`.
