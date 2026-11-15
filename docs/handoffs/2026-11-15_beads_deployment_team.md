# Handoff: BEADS DEPLOYMENT TEAM (2026-11-15)

**Window name: Beads Deployment Team** (the author's main orchestrator). Per the author's note on bead Eurobound-jpkw ("One task. Then handoff and clear context."), **this window can be cleared now.** Nothing of its own is running or uncommitted.

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

## In flight

Nothing. All three agents landed and are committed and pushed: the quest step-markers proposal (Eurobound-wn1f, Desk `Eurobound-wn1f-q2`), the old NPC conversations audit (Eurobound-rras, Desk `Eurobound-rras-q2`), and Roast Line tagged as spoken (Eurobound-uwrw, closed, d6c53e88). No agent of this window is running and the working tree holds no uncommitted work of its own.

## Answers that arrived after the handoff (recorded on the beads and in the ledger; the work is NOT done)

- **Eurobound-r61w**: "270 SOVS: the prices are right, fix the total". Fix `total_money_spent` in `game/assets/data/quests/astronomical_cockup.json`; Path B's name ("Second" vs "Secret" Show Seekers) is still unanswered.
- **Eurobound-rras**: "Go with the audit: keep, fix and cut as listed". Apply the cuts from `docs/superpowers/reports/2026-11-15-old-npc-conversations-audit.md`; the "keep with a fix" lines need the Writers' Room or the author for the fixed wording.
- **Eurobound-wn1f**: "Approve as proposed". Build the eleven approved step markers; the four two-reading steps are asked again as `Eurobound-wn1f-q3`.
- **Eurobound-2tb9** (now P1): "Yes: find it and show it to me before anything is saved". Find the author's story text and show it on the Desk; save nothing first.
- **Names picked on the Writers' Room's cards**: the kapsalon buff is "Tray Rage" (Eurobound-n355) and the Meme Black Market quest is "Don't Look at the Baby" (Eurobound-p64h). The Writers' Room applies them; check they landed.
- **Main-quest session**: the author said "Ask me monday" (card `Eurobound-c8xn-wr1`).
- Next queued cards posted: story question 3 of 46 (`Eurobound-c8xn-q4`) and NPC group 3 of 18 (`Eurobound-4ynh-q4`).

Third round, same day (recorded; work NOT done):

- **Eurobound-b10l**: "Strike both lines". Remove the "Meta References" bullet from `vlad_the_validator.md` and `crypto_clown.md`.
- **Eurobound-b8yo**: "Nobody: remove him; the Shadow Exchange is staffed by the NPCs already in its files". Remove Dmitri the Exchanger from the engine data and the old conversation files.
- **Eurobound-wn1f**: "A for all four". Every quest step is decided; build the whole proposal.
- Story question 3 joins the author's Monday Writers' Room session; question 4 of 46 is posted (`Eurobound-c8xn-q5`); NPC group 4 of 18 is posted (`Eurobound-4ynh-q5`).

## Queued, not started

- **Eurobound-7nbx**: author ruled the Great Doner Debate's Shamsterdam half "starts once the base quest has a winner and the bros reach Shamsterdam". Apply it to `design/quests/general_quests/greatdonerdebate.md` (the expansion-pack trigger and headings); the ledger entry is in.

- **Eurobound-x2ws**: author ruled "No autosave for now: hotspots and beds only" and 3 save slots. Engine work: slots, save at beds. One Godot agent.
- **Eurobound-04t2**: author kept the Arcade's talk box for the whole game. Move `dialogue_box.gd` to shared code and switch the Dialogue Manager add-on off, in a worktree. Conditions from the Arcade owner: class name and API unchanged; add-on off through its toggle, never by hand-editing `project.godot`, folder left in place; full GUT; put the SHA on the bead for the Arcade window to review and merge. Tell the Arcade window before starting. Then send the Writers' Room (eurobound-2b) the NPC conversation data format.
- **Eurobound-7rdd** (Legendary Hangover extras), **Eurobound-fjdk** (Munchies vendor rules), **Eurobound-81oy**, **Eurobound-ny6e** (a test pinning dropped Crash turns), **Eurobound-8b28** (NPC count off by 2-3).
- **Monday 2026-11-16**: Eurobound-it49, -j45c, -zf6e (first SOVS shop stock) come off deferral once the author has generated the items.

## Waiting on the author (Eurobound Desk, window "Beads Deployment Team")

- `Eurobound-c8xn-q3`: story question 2 of 46 (question 1 went to a Writers' Room session with the author). The queue is `docs/story/story_holes_queue.md`; post the next one after each answer (the bead has the QUEUED DESK QUESTIONS comment).
- `Eurobound-4ynh-q3`: NPCs without a profile, group 2 of 18 (The Absinthium Taproom); the rest are queued on the bead.
- `Eurobound-wn1f-q2` (quest step markers), `Eurobound-rras-q2` (audit verdict), `Eurobound-9tz9-q1` (Velvet Curtain Club door), `Eurobound-r61w-q1` (Scam Gauntlet 170 or 270 SOVS), `Eurobound-b10l-q1` (two lines that nod at the player), `Eurobound-b8yo-q1` (who Dmitri the Exchanger is), `Eurobound-jykm`-related work is closed.
- `Eurobound-rpac-q1`, `-q2` (Writers' Room): item description format, and where descriptions go for the 173 items with no `.md`.
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
