# Beads (bd) for Eurobound

The main project instructions are in `.claude/CLAUDE.md`. This file holds the beads block that `bd setup` manages, plus the Eurobound rules that qualify it.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:1105d646 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/core-concepts/sync-concepts.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

## Beads: rules specific to Eurobound

These qualify the generated block above. Where the two disagree, these win. They sit outside the markers so re-running `bd setup` cannot overwrite them.

- **One identity: `machsheltie`.** It is `git user.name` and what `bd` derives its actor from. `heirr` is the Windows account, not an identity. Never pass an assignee inferred from the environment: omit `-a`, or pass `-a machsheltie`.
- **Run `bd` from the repository root.**
- **What goes where:**
  - **Work state** (open tasks, what is blocked, which round is open, what waits on the author) → beads issues. Use `bd dep add` for blockers; an item waiting on an author answer gets the label `author-ruling`.
  - **Canon and author rulings** → the rulings ledger (`docs/superpowers/NEXT_WORK.md`, economy spec §0a). A bead may point at a ruling; it never replaces the ledger entry. Search canon with `tools/canon_index` (see its README).
  - **How the author wants agents to work** → the existing Claude auto-memory. `bd remember` is for durable technical findings (tool gotchas, pipeline facts). Do not migrate or delete the auto-memory without an author ruling.
- **Content work still needs author rulings.** A bead for new content, story, mechanics or numbers records the question; it is not permission to invent the answer (`.claude/CLAUDE.md`, "Ask the author first").
- **Write beads for a cold reader:** name the file and line, what is wrong, and what "done" looks like.
- **File what you find (author, 2026-11-11).** Every session and every agent that comes across work needing doing, outside the task in hand, files a bead for it instead of dropping it or doing it unasked. Each bead carries: a description for a cold reader (`--stdin`), `--acceptance` (what complete looks like), `--metadata '{"agent":"<agent type>","effort":"<low|medium|high|xhigh|max>","found_by":"<bead id or session>"}'`, matching `agent:`/`effort:` labels, `--skills` (real skill names), and `--deps discovered-from:<id>` when it came out of another bead. Search first (`bd search`) to avoid duplicates. Anything needing an author decision gets the `author-ruling` label and states the question without inventing an answer. When you brief a subagent, pass this rule on.
- **Keep the author's bead page current.** After you create, update or close beads, sync the review page (https://claude.ai/artifact/NgqNUkLBWENWRQtESxYiCZ) as described in `Tools/beads_board/README.md`.
- **Git:** commit or push only when the author asks (conservative profile). `bd` sync rides on the git remote; do not run Dolt remote sync unasked.
