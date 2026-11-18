Window: Asset Development Team (2026-11-17; one task from the Production Desk Orchestrator: Eurobound-pg9a, cut the whole bronze Green Fairy statue out of the Arcade restroom plate)

# Handoff: Asset Development Team, restroom Green Fairy statue (pg9a)

**State: the art, the QC and the location ids are done. The scene and the tests wait for the Godot slot.** The orchestrator said to stop and ask before touching the scene or running GUT; I asked by SendMessage. Nothing is committed.

**Orchestrator, 2026-11-17:** the Godot slot is still held by the street-encounters build (iqgo). This window's task is finished and pg9a stays in_progress. The orchestrator will send the scene step as a new task built from this handoff once Godot is free.

## Done

1. **Mask.**
   - SAM 2.1 zones `tools/paint_zones/zones/aa_restroom_statue_day.json` cover body, wings, plinth and both roll stacks. The run output is in `tools/paint_zones/work/aa_restroom_statue_day/`.
   - `Tools/content_generation/absinthe_arcade/hd2d/cut_restroom_statue.py mask` unions the zones, closes 9 px slivers and fills holes. The mask fits the night plate exactly, so the plates are registered.
2. **Clean niche.**
   - A Firefly Gemini 3.1 (Nano Banana 2) edit of the approved day plate, at 2K and 16:9. The prompt is `dev/asset_team/prompts/aa_int_restroom_statue_removal_1.txt`; the result is `Tools/content_generation/absinthe_arcade/hd2d/work_restroom_statue/gemini_clean_day_1.png`.
   - Phase correlation measured a 0 px shift against the plate.
   - `cut_restroom_statue.py composite <that png>` pastes it inside a 40 px margin only. The 40 px covers the statue's painted cast shadow and outline; 14 px left a ghost. Every pixel outside the margin is unchanged.
   - Night niche: an affine day-to-night colour fit on the niche wall. Emit niche: the hall emit rule (`cut_interior_layers.emit_map`).
   - The originals with the statue are kept once in `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Interior/plates_with_statue/`. The script always re-reads those, so it can be re-run.
3. **Outputs** in `game/assets/worlds/debaucheryville/absinthe_arcade/interior/restroom/`:
   - Clean plates: `aa_int_restroom_{day,night,emit}.png`.
   - Statue layers: `props/aa_int_restroom_statue_{day,night,emit}.png`. All three share one alpha and are 655 x 805.
   - Placement: `props/statue.json` (`plate_xy` 1046, 26; `object_id` green_fairy_statue; `node_id` aa_node_restroom_statue).
   - `props/statue_hands.json` and the hand PNGs are unchanged.
4. **Blind gate C, round 1: PASS.** The sheet is `dev/asset_team/reviews/pg9a_gate_c_sheet.jpg`, plus `pg9a_clean_niche_full_res.jpg` and `pg9a_game_size_{day,night}.jpg`. The line is in `dev/asset_team/reviews/qc_log.jsonl`. Notes:
   - the niche wall is a softer plaster wash than the stonework (acceptable; an optional texture pass would help);
   - the night niche has no lamp falloff.
   - The review sheet is built by `Tools/content_generation/absinthe_arcade/hd2d/restroom_statue_review.py`.
5. **Location files.**
   - `design/worlds/debaucheryville/sprite_mapping/absinthe_arcade_sprite_mapping.json` has a new `asset_groups.props` entry, `aa_prop_restroom_green_fairy_statue`. It has its file, node, interaction and `variants` day/night/emit.
   - In `design/worlds/debaucheryville/location_nodes/absinthe_arcade_restroom_location_nodes.json`, `feature_details.aa_node_restroom_statue` gains an `art` field and the layer order in `occlusion`.
   - The ids `green_fairy_statue` and `aa_node_restroom_statue` already existed from v2bb. `tools/validate_data.py` gives SUMMARY OK 21 with no errors.
6. **Tracking.**
   - Eurobound-pg9a is in_progress with a full comment.
   - New Asset Board row `int-aa_prop_restroom_green_fairy_statue` (in_progress, with a thumbnail), plus a feed entry.
   - The bead page is synced and acked.

## Still to do (needs the Godot slot; ask the Production Desk Orchestrator first)

- In `game/worlds/debaucheryville/absinthe_arcade_restroom_hd2d.gd`, add the statue as one node from `props/statue.json`: a plate-rect quad like the hand quads (around line 95), with day/night textures and emit at night.
  - It goes behind Jakub: his z is `JAKUB_AT.z` 0.8 and the hands sit at `HANDS_Z`, so the statue needs a z between the plate and Jakub.
  - The hands stay in front of him.
- In the scene, check that Jakub still reads as asleep in her arms. Then run the GUT suite with `python -I Tools/orchestrator/gut.py`, and the A5 critic shots if they are wanted.
- Then set the board row and the bead to done and send the orchestrator a summary.

## Changed files (uncommitted, this window's only)

- **New files:**
  - `Tools/content_generation/absinthe_arcade/hd2d/cut_restroom_statue.py` and `restroom_statue_review.py`
  - `Tools/content_generation/absinthe_arcade/hd2d/work_restroom_statue/`: the Gemini clean plate and the two masks (7 MB; needed to re-run, so committing them is the author's call)
  - `tools/paint_zones/zones/aa_restroom_statue_day.json`, and `tools/paint_zones/work/aa_restroom_statue_day/` (SAM output)
  - `game/.../restroom/props/aa_int_restroom_statue_{day,night,emit}.png` and `props/statue.json`
  - `Assets/.../references/Interior/plates_with_statue/` (three originals)
  - `dev/asset_team/prompts/aa_int_restroom_statue_removal_1.txt`
  - in `dev/asset_team/reviews/`: `pg9a_gate_c_sheet.jpg`, `pg9a_clean_niche_full_res.jpg`, `pg9a_game_size_day.jpg`, `pg9a_game_size_night.jpg`
  - this handoff
- **Modified files:**
  - `game/.../restroom/aa_int_restroom_{day,night,emit}.png` (clean plates). Godot needs a reimport.
  - The two location JSONs above.
  - `dev/asset_team/reviews/qc_log.jsonl` (1 line).

## Cleanup

My Firefly tab and the local CORS server are closed. No Blender or Godot was started. The two PNGs left in Downloads are another agent's.
