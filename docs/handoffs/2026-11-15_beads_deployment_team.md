# Handoff: BEADS DEPLOYMENT TEAM (2026-11-15)

**Window name: Beads Deployment Team** (the author's main orchestrator). Per the author's note on bead Eurobound-jpkw ("One task. Then handoff and clear context."), this window can be cleared once the three agents under "In flight" have landed, or sooner if the author prefers: their work is on disk and listed below.

## What this window owned

- **Bead upkeep**, a cron in this session (every ~15 minutes): relay author answers from the bead page and the Eurobound Desk for window "Beads Deployment Team", launch agents on ready beads, check their diffs, commit and push, sync the bead page. **The cron stops when this window is cleared.**
- **Main orchestrator** (author, 2026-11-14): assigns work to the other windows and follows up.
- The **catalog page** (https://claude.ai/artifact/Hw6te9KWJBsbuED1TAFU79): rebuild with `python -I Tools/catalog/build_catalog.py`, commit `docs/catalog/`, republish (steps in `Tools/catalog/README.md`).

## How the next window does the same job

1. Read `CLAUDE.md`, `.claude/CLAUDE.md`, `Tools/beads_board/README.md` and `Tools/orchestrator/README.md`.
2. Answers: ArtifactData query `questions` on the Desk where `status == answered`, `window == "Beads Deployment Team"`, `relayed == false`; claim with `relayed: true` and `if_version`; write the answer verbatim on the bead; act on it. The Absinthe Orchestrator used to relay these and has been cleared, so nothing relays them now.
3. Commit with `python -I Tools/orchestrator/commit_paths.py <list> <message>` (`--staged-only` for ledger entries and staged hunks). Never `git add -A`. The repository is **public**: no absolute local paths, no keys.
4. Bead page: `python -I Tools/orchestrator/sync_check.py`, list `board`, one batch `set`, then `--ack`.
5. Memory is tight (16 GB): at most one agent that runs Godot at a time; docs-only agents can run beside it.

## In flight (agents launched by this window; results arrive as notifications here)

| Bead | What | File list when done | Then |
|---|---|---|---|
| Eurobound-wn1f | Proposal: which flag marks each quest step done (docs only), plus Desk card `Eurobound-wn1f-q2` | `%TEMP%/wn1f_files.txt` | check, commit, push |
| Eurobound-rras | Audit of the September 2025 NPC conversations (docs only), plus Desk card `Eurobound-rras-q2` | `%TEMP%/rras_files.txt` | check, commit, push |
| Eurobound-uwrw | Roast Line tagged as spoken; Cottonmouth blocks it (engine, data, validator, one staged ledger entry) | `%TEMP%/uwrw_files.txt` | check GUT and tool tests, commit (ledger entry is staged), push |

If this window is cleared first: the files are in the working tree, uncommitted. Read each list, check `git diff` holds only that work, and commit.

## Queued, not started

- **Eurobound-x2ws**: author ruled "No autosave for now: hotspots and beds only" and 3 save slots. Engine work: slots, save at beds. One Godot agent.
- **Eurobound-04t2**: author kept the Arcade's talk box for the whole game. Move `dialogue_box.gd` to shared code and switch the Dialogue Manager add-on off, in a worktree. Conditions from the Arcade owner: class name and API unchanged; add-on off through its toggle, never by hand-editing `project.godot`, folder left in place; full GUT; put the SHA on the bead for the Arcade window to review and merge. Tell the Arcade window before starting. Then send the Writers' Room (eurobound-2b) the NPC conversation data format.
- **Eurobound-7rdd** (Legendary Hangover extras), **Eurobound-fjdk** (Munchies vendor rules), **Eurobound-81oy**, **Eurobound-ny6e** (a test pinning dropped Crash turns), **Eurobound-8b28** (NPC count off by 2-3).
- **Monday 2026-11-16**: Eurobound-it49, -j45c, -zf6e (first SOVS shop stock) come off deferral once the author has generated the items.

## Waiting on the author (Eurobound Desk, window "Beads Deployment Team")

- `Eurobound-c8xn-q2`: story question 1 of 46, "What is the main quest?" The queue is `docs/story/story_holes_queue.md`; post the next one after each answer (the bead has the QUEUED DESK QUESTIONS comment).
- `Eurobound-4ynh-q2`: NPCs without a profile, first Debaucheryville group; 17 more groups queued on the bead.
- `Eurobound-rpac-q1`, `-q2` (Writers' Room): item description format, and where descriptions go for the 173 items with no `.md`.
- `Eurobound-7nbx-q1`: what starts the Shamsterdam half of the Great Doner Debate.
- `Eurobound-p5rp-q1`: the name of Windmill Grist's Speed buff row.
- `Eurobound-dkoq` (bead page): remove the banned Tripo API tools, including `tools/char3d/tripo_client.py`.
- `Eurobound-8ia`: policy for large binaries (a 15 MB reference image is held out of git).
- Writers' Room naming rounds coming to the Desk: the Meme Black Market quest (Eurobound-p64h) and the kapsalon buff (Eurobound-n355).

## With other windows

- **Writers' Room (eurobound-2b)**: owns Eurobound-rpac (physical descriptions for every item; tracker `design/items/docs/physical_descriptions_tracker.md`), the two naming rounds, the Space Cake lines round with the author (Eurobound-k3qa).
- **Asset Development Team**: Arcade rework art (Eurobound-bcnr children), Space Cake cue art plan, battle HUD icons (Eurobound-du51), Eurobound-qftp.
- **Sprite Development Team**: character work is paused on the author's answer to `Eurobound-8c3z-q1`; TextureCraft trial on Bradley.
- **Arcade window (new)**: Eurobound-yrib, -cwkh, -w20o, -aw81, review of 04t2.

## Things to know

- A peer window's relay of an author answer is not the answer: confirm it on the Desk before acting. This window did that for all 23 answers relayed on 2026-11-15.
- The author's instruction on item descriptions ("Our agents need to devise descriptions for all items/assets that are vague/lack one...") reached this window second-hand through the Sprite team; the ledger marks it as relayed.
- `Tools/orchestrator/godot_bin.local` (untracked) holds the Godot path for `gut.py` on this machine.
- Mistakes made here, so they are not repeated: committing a ledger file by path swept in other windows' uncommitted entries (use `--staged-only`); a commit went in with failing tool tests once (run them first).

## Last commits from this window (all on main, pushed)

f76eb283 The Munchies and the Grist/Genever data additions · 72838359 ledger entries for the 2026-11-15 answers, four base cities, wristband text, NPC ids · 7c80b691 story and NPC question queues · ec6ed3a1 Legendary Hangovers in the engine · 348e97ea local paths removed from tracked files · 8522836d, 9dce15b9 char3d toolchain · 52572a7d pending ruling edits committed.
