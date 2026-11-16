# beads_board

Keeps the author's bead review page in step with the tracker:
https://claude.ai/artifact/NgqNUkLBWENWRQtESxYiCZ

The page reads every bead from its own store (collection `board`), so it shows new beads, status changes and closes as soon as the store is synced. The author's verdicts live in the same store (collection `verdicts`, one doc per bead id: `{verdict: approve|change|drop, priority, note}`).

The page is for checking where things stand. It asks no questions: author-ruling beads show a link to the Eurobound Desk instead (author, 2026-11-16).

## Sync (any Claude session, after it creates, updates or closes beads)

1. Run `python -I Tools/orchestrator/sync_check.py` from the repo root (not `sync_board.py` directly). It exports `bd list --all` to `Tools/beads_board/out/` (gitignored) and prints the changed doc ids and their file paths. `sync_board.py` forgets a change the moment it prints it (`sync_board.py:125`), so a run you do not finish would leave the page stale; `sync_check.py` keeps unwritten ids in `Tools/beads_board/out/pending.json` and repeats them until you run `python -I Tools/orchestrator/sync_check.py --ack` after step 4 succeeds. One export takes about 26 s (it calls `bd dep list` per open bead, `sync_board.py:60`).
2. If `changed` is empty, stop.
3. List the store once to get each doc's current `version`: `ArtifactData list`, url above, collection `board`.
4. Write the changed docs in ONE `ArtifactData batch`: an `op: "set"` per doc, `collection: "board"`, `doc_id` as printed, `file_path` from the script's output, and `if_version` from step 3 for every doc that already exists (omit it for a new doc). Delete any ids listed under `removed`.

A version conflict means another session synced first. Re-run the script and the batch.

## Author-ruling beads: questions go to the Eurobound Desk (author, 2026-11-16)

Author, 2026-11-16: "I think the beads issues that need my feedback should have their questions sent to the production desk for me to answer so I don't have to answer in two places. The beads artifact should just be for me to check up on where things stand."

Each `author-ruling` bead still carries `metadata.ask` = `{"question": "...", "options": [{"label": "...", "recommended": bool}]}` (set with `bd update <id> --set-metadata ask=<json>`, or `bead_new.py --ask-question/--ask-option`). It is the source for the Desk card: the question the author must answer and 2–4 options, which are decisions or routes, never invented content. The bead page no longer shows it.

**Posting** (whoever files or finds the bead):
1. Check the Desk `questions` collection for a doc whose `bead` matches. Check the bead page's `answers` collection too (see below). If either already holds the question or an answer, do not post it again.
2. Post it as described under "Ask" below: `doc_id` `<bead-id>-q<n>`, `title` = `metadata.ask.question`, `options` = `metadata.ask.options` unchanged, `context` written for a cold reader with the bead description's file:line references, `bead` = the bead id.
3. `bd update <bead> --status blocked` and `bd comments add <bead> "Waiting on Eurobound Desk <doc_id>: <title>"`.
4. Sync the bead page.

The answer comes back through the Desk relay below.

**Old answers on the bead page.** Before 2026-11-16 the page had its own answer form, which wrote `answers/<bead-id>` = `{bead, question, choice, note, at, relayed: false}`. The page now shows any unrelayed one read-only. To relay one:
1. Run `bd comments add <bead> "Author answer (bead page), verbatim: <choice> / <note>"`, quoting the words exactly.
2. Run `bd update <bead> --remove-label author-ruling --status open`.
3. Update the answer doc with `relayed: true` (pin `if_version`).
4. Re-sync the board.

Never reinterpret the author's words.

## Eurobound Desk: every question for the author, from every window

Desk: https://claude.ai/artifact/Pm3AgZ5qHqqmcoRcEv52JF (author, 2026-11-12: "These two need to be folded into one for all of our open agent windows to utilize. When I click submit, it should notify the corresponding window and give them the answers they were waiting on."). It replaced both the old decisions page (https://claude.ai/artifact/ABVcfvJZCSX9zmnvXmncuH, retired) and the Production Desk, and keeps the Production Desk's link and data. Every question for the author goes here, from any window, bead or not: never in chat, never a separate page, never a guess.

**Ask** (any session or subagent with the ArtifactData tool):
1. `ArtifactData set` on the desk url, `collection: "questions"`, a new `doc_id` (`<bead-id>-q<n>` for a bead question, otherwise `<window-slug>-<topic>`), with data:
   `{title, context, options, status: "open", relayed: false, order, window, asked_by, asked_at, bead, blocking, images, note_label}`
   - `window`: the asking session's exact name as `ListAgents` prints it (e.g. "Sprite Development Team", "Absinthe Orchestrator"). The answer is sent back to this window, so get it right. The desk groups questions by it.
   - `title`: the question in one line. `context`: what you found, with file:line references, and why it matters.
   - `options`: a list of `{label, recommended}` (decisions or routes, never invented content). `note_label`: optional label for the write-in box.
   - `bead`: the bead id, or "" if none. `blocking`: what work waits on the answer.
   - `images`: optional `[{url, caption, pixel}]`. Upload each image to the desk first (Artifact publish with `url` = the desk, `asset: true`, `file_paths` for up to 25 files staged inside the repo) and use the returned `/_blob/<id>` url. `pixel: true` renders it unsmoothed.
   - `order`: epoch seconds. `asked_by`: agent role or session name. `asked_at`: an ISO time.
2. For a bead: `bd update <bead> --status blocked` and `bd comments add <bead> "Waiting on Eurobound Desk <doc_id>: <title>"`.
3. Mark the item "waiting on the author" on its board (Asset Board, Arcade Build Board or bead page) with the desk doc id, then finish anything that doesn't depend on the answer.
4. Optional progress log: `collection: "updates"`, `doc_id: "<timestamp>-<slug>"`, data `{at, title, body, kind, bead}`.

**One at a time** (when the author asks for it): post only the first question; keep the rest and post the next after each answer.

**Relay.** The author's Send saves each answer into its doc (`status: "answered"`, `answer: {choice, note, at}`) and sends one "sent to Claude" comment on the desk. That comment wakes the session watching the desk with auto-replies armed: the Absinthe Orchestrator. A fallback timer (about every 20 minutes) catches anything missed. Whoever relays:
1. Queries `questions` where `status == "answered"` and `relayed == false` (every question is posted with `relayed: false`; the Desk rejects queries on nested fields such as `answer.at`).
2. Claims each one FIRST: `update` it with `relayed: true` pinned with `if_version`. If the pin fails, someone else has it; skip it.
3. Sends the answer verbatim to `window` with SendMessage ("Author answer (Eurobound Desk <doc_id>), verbatim: <choice> / <note>"). For a bead, also `bd comments add <bead> "Author answer (Eurobound Desk <doc_id>), verbatim: <choice> / <note>"` and `bd update <bead> --status open`.
4. Replies in the desk's comment thread with who got what, and resolves it.
Never answer on the author's behalf.

**Receiving an answer** (the asking window): act on it, then update the item on its board straight away (Asset Board, Arcade Build Board, bead page) so nothing still says it waits on the author once the author has answered. Then sync the bead page as above if beads changed.

The session that set up the bead page also runs its sync on a timer while it is open, so beads changed by other sessions show up within about 15 minutes.

## Playtest notes on the Desk (author, 2026-11-13, Eurobound-7qf3)

The Desk has a **Playtest notes** box. While playing, the author types or dictates what feels off. Dictation works in Chromium browsers and the desktop app.

**Where notes are stored.** Each note is saved as `playtest_notes/<id>` = `{text, at, status: "new", bead: "", reply: ""}`. The Desk also sends a "sent to Claude" comment. The Absinthe Orchestrator's fallback timer picks up any note the comment missed.

**Filing a note.** Any session can do this:
1. Claim the note: update `status: "filing"`, pinned with `if_version`.
2. Search for a duplicate with `bd search`.
3. File a bead for a cold reader. Follow the root CLAUDE.md "File what you find" rule, with `found_by: "author playtest note <id>"`. Quote the note verbatim, and add file:line once the cause is found.
4. Update the note to `{status: "filed", bead: "<id>", reply: "<one plain sentence on what happens next>"}`. The author sees "Filed · <bead>" under the note.
5. Send the bead to the window that owns that area.

Treat a note as a bug report or a wish. If it needs a content or mechanics decision, the bead gets the `author-ruling` label and its question goes on the Desk like any other.
