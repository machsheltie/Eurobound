# beads_board

Keeps the author's bead review page in step with the tracker:
https://claude.ai/artifact/NgqNUkLBWENWRQtESxYiCZ

The page reads every bead from its own store (collection `board`), so it shows new beads, status changes and closes as soon as the store is synced. The author's verdicts live in the same store (collection `verdicts`, one doc per bead id: `{verdict: approve|change|drop, priority, note}`).

## Sync (any Claude session, after it creates, updates or closes beads)

1. Run `python -I Tools/beads_board/sync_board.py` from the repo root. It exports `bd list --all` to `Tools/beads_board/out/` (gitignored) and prints the changed doc ids and their file paths.
2. If `changed` is empty, stop.
3. List the store once to get each doc's current `version`: `ArtifactData list`, url above, collection `board`.
4. Write the changed docs in ONE `ArtifactData batch`: an `op: "set"` per doc, `collection: "board"`, `doc_id` as printed, `file_path` from the script's output, and `if_version` from step 3 for every doc that already exists (omit it for a new doc). Delete any ids listed under `removed`.

A version conflict means another session synced first. Re-run the script and the batch.

## Author answers to "Your ruling" beads (author, 2026-11-12)

Each `author-ruling` bead carries `metadata.ask` = `{"question": "...", "options": [{"label": "...", "recommended": bool}]}` (set with `bd update <id> --set-metadata ask=<json>`). File every new author-ruling bead with one: the question the author must answer and 2–4 tappable options, which are decisions or routes, never invented content. The page shows the question, the options and a write-in box. The author's Submit writes `answers/<bead-id>` = `{bead, question, choice, note, at, relayed: false}`.

**Relay** (the timer, or any session):
1. Query `answers` where `relayed == false`.
2. For each answer:
   - Run `bd comments add <bead> "Author answer (bead page), verbatim: <choice> / <note>"`, quoting the words exactly.
   - Run `bd update <bead> --remove-label author-ruling --status open`.
   - Update the answer doc with `relayed: true` (pin `if_version`).
3. Re-sync the board. The bead now shows under "Ready for agents".
4. Pick it up per the CLAUDE.md bead rules: brief an agent with the answer. Never reinterpret the author's words.

## Production Desk: questions for the author while working a bead

Desk: https://claude.ai/artifact/Pm3AgZ5qHqqmcoRcEv52JF (author rule, 2026-11-11). Whenever an agent working a bead needs the author's input, it asks here, not in chat and not by guessing.

**Ask** (any session or subagent with the ArtifactData tool):
1. `ArtifactData set` on the desk url, `collection: "questions"`, `doc_id: "<bead-id>-q<n>"` (new doc, so no `if_version`), with data:
   `{bead, title, context, blocking, options, status: "open", order, asked_by, asked_at}`
   - `title`: the question in one line.
   - `context`: what you found, with file:line references, and why it matters.
   - `blocking`: what work waits on the answer.
   - `options`: an optional list of `{label, recommended}`.
   - `order`: epoch seconds.
   - `asked_by`: agent role or session name.
   - `asked_at`: an ISO time.
   Never put a guessed answer into the question.
2. Run `bd update <bead> --status blocked` and `bd comments add <bead> "Waiting on Production Desk <doc_id>: <title>"`.
3. Finish any part of the bead that doesn't depend on the answer, then stop and report the question id.
4. Optional: log progress as `ArtifactData set`, `collection: "updates"`, `doc_id: "<timestamp>-<bead>"`, data `{at, title, body, kind, bead}`.

**One at a time** (when the author asks for it): post only the first question, and save the rest as JSON in a bead comment headed `QUEUED DESK QUESTIONS (post one at a time after each answer):`. Whoever relays an answer posts the next queued question.

**Relay** (the session running the timer does this; any session may):
1. List `questions`. For each doc with `status: "answered"` and no `relayed`:
   - Run `bd comments add <bead> "Author answer (Production Desk <doc_id>), verbatim: <choice> / <note>"`, quoting the words exactly.
   - Run `bd update <bead> --status open`.
   - Update the doc with `relayed: true` (pin `if_version`).
2. Resume the bead with an agent that is given the answer.
Never answer on the author's behalf.

The session that set this up also runs the sync on a timer while it is open, so beads changed by other sessions show up within about 15 minutes.
