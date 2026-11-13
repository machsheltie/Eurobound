# Blind critic loop (bead Eurobound-72sl)

A repeatable score loop for art. Fixed camera shots are captured from the running game, critics who never saw the build score each against its approved reference (1-10, 3 worst differences), fixers touch only shots under 7, then everything is re-captured and rescored. The author's approval and hand-painted distress are never replaced; the loop only reports. No paid APIs: critics are Claude Code Sonnet subagents launched by the orchestrating session.

## Files
- `shots/<scene>.json`: fixed shot list (id, time of day, bro positions and facing, optional crop, reference, neutral description). Pilot: `arcade_hall.json` (6 hall shots, 2 Lord Pilsner shots).
- `refs/*.jpg`: downscaled copies of the approved references. Hall plates are the night and day plates the hall paints from (`game/assets/worlds/debaucheryville/absinthe_arcade/interior/hall/aa_int_hall_*.png`, the v8 lineage). Pilsner is `Assets/Graphics/characters3d/lord_pilsner_v2/lord_pilsner_ref.png`, the painting look B was built from. Built by `prepare-refs` and committed because the originals are untracked.
- `capture.gd`, `run_round.py`: windowed capture runner, output `<scene>/round_<n>/<shot_id>.jpg`.
- `critic_prompt.md`: the exact blind-critic prompt.
- `results/summarize.py`: score deltas. Logs live in `results/<scene>/round_<n>.jsonl`, one line per shot: `{"shot_id","score","worst":[3],"verdict"}`.

## Run a round (orchestrating session)
1. Once per worktree: `Godot_console --headless --path game --import --quit` (never commit the .import churn). Once per reference change: `python -I tools/critic_loop/run_round.py prepare-refs` (set `CRITIC_REF_ROOT` to the main checkout if a source is untracked).
2. Capture: `python -I tools/critic_loop/run_round.py capture --round N` (optionally `--shots a,b`). It runs ONE windowed Godot and waits for it to exit; check no orphan Godot process remains. Never edit project.godot (resolution comes from `--resolution 1920x1080`).
3. Critics: for each shot fill `critic_prompt.md` (reference path, capture path, describe, shot_id) and spawn one Sonnet subagent per shot, or per 3 shots. Pass nothing else.
4. Append each returned JSON line to `results/arcade_hall/round_N.jsonl`. If a reply is not strict JSON, re-ask that critic once.
5. File a bead (bd) only for shots under 7: shot id, capture path, the 3 worst differences, acceptance "critic score >= 7 next round". Fixers work only on those shots and must not alter the reference or hand-painted distress.
6. Re-capture all shots (round N+1) so a fix cannot silently regress another, rescore, then run `python -I tools/critic_loop/results/summarize.py`.
7. Stop after 5 rounds or when every shot passes. The author still reviews and approves finals.

## Token budget
Images are max 1280 px wide JPEG q80, 8 shots. A critic reads 2 images and returns about 60 tokens, so a round is 8 small Sonnet runs; batch 3 shots per critic to cut overhead. The orchestrator never reads captures beyond one spot check and never re-reads an image. Fix only sub-7 shots.

## Notes
- Hall references show an empty room, so bro shots are judged for room fidelity and figure scale; the two Pilsner shots are cropped and judged against his portrait.
- Shots are deterministic: the hall runs with `spawn_player=false`, so no NPCs, clock or schedules.
- Another scene needs its own `shots/<scene>.json`; capture.gd currently stages the hall's `night`, `spawn_player`, `WORLD_SCALE` and `ACTOR_GROUP`.
