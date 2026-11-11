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

The session that set this up also runs the sync on a timer while it is open, so beads changed by other sessions show up within about 15 minutes.
