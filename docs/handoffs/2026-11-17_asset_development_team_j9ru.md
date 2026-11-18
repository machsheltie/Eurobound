Window: Asset Development Team (2026-11-17; one task from the Production Desk Orchestrator: Eurobound-j9ru, the Absinthium Taproom floating chalice selfie spot, art only)

# Handoff: Asset Development Team, Taproom floating chalice (j9ru)

**State: partly done. I stopped at the Gemini wall edit** because the agents' Chrome window is minimized (screenX -21333). The orchestrator has asked the author to restore it. Everything that doesn't need Firefly is done. Nothing is committed. j9ru is in_progress.

## Done

1. **Segmentation.** SAM 2.1 zones `tools/paint_zones/zones/aa_taproom_chalice_day.json`, one zone `chalice` with box 1305,190-1445,380. The output is in `tools/paint_zones/work/aa_taproom_chalice_day/`, with mask bbox 1322,201-1430,370 (10,067 px). Its edge was checked on the day plate and is tight to the bowl, stem and foot.
2. **Generic cut script.** `Tools/content_generation/absinthe_arcade/hd2d/cut_plate_prop.py` generalizes the pg9a cut, driven by a config file. The config for this prop is `Tools/content_generation/absinthe_arcade/hd2d/prop_cuts/taproom_chalice.json`:
   - `close_px` 3, `margin_px` 16, `pad_px` 8;
   - the prop spec, with ids and the float block;
   - originals to be kept in `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Interior/plates_with_chalice/`.

   `mask` has run, writing `work_taproom_chalice/prop_mask.png` and `inpaint_mask.png`.
3. **Float animation**, as a bob spec, which is how the tweened Arcade animations are declared. The entry is `animation_sequences.taproom_chalice_float` in `design/worlds/debaucheryville/sprite_mapping/absinthium_taproom_sprite_mapping.json`:
   - `tween_bob`, a vertical sine bob of the chalice layer only;
   - amplitude 6 plate px, period 3.2 s, looping;
   - low motion: still at the rest position.

   The same block goes into `props/chalice.json` when the composite runs.
4. **Location files** (ids already existed from v2bb: interaction and node `at_selfie`):
   - In the sprite mapping, asset `absinthium_taproom_node_at_selfie` now points at `interior/taproom/props/aa_int_taproom_chalice_day.png`. It also gains `prop_asset_id aa_prop_taproom_floating_chalice`, the interaction id, its variants, the placement file and a note.
   - The `interaction_bindings` entry for `at_selfie` gains `prop_asset` and `hotspot` (the chalice layer's rect; it triggers the `at_selfie` event).
   - In `design/worlds/debaucheryville/location_nodes/absinthium_taproom_location_nodes.json`, `feature_details.at_selfie` gains an `art` field and an occlusion note.
   - `tools/validate_data.py` reports no errors.
5. **Gate C sheet builder:** `Tools/content_generation/absinthe_arcade/hd2d/prop_review.py`. Its panels are A through G as in pg9a, plus H, a float strip at -6, 0 and +6 px.
6. **Prompt:** `dev/asset_team/prompts/aa_int_taproom_chalice_removal_1.txt`.
7. **Tracking:**
   - The bead has a comment and is in_progress.
   - The bead page is synced and acked.
   - New Asset Board row `int-aa_prop_taproom_floating_chalice`, in_progress.

## Remaining: the art, once Chrome is back

1. **The Gemini wall edit.**
   - **Where:** the Firefly home screen, model **Gemini 3.1 (Nano Banana 2)**, aspect **Auto** (the input is 16:9), resolution **2K**.
   - **Input:** attach the live day plate `game/assets/worlds/debaucheryville/absinthe_arcade/interior/taproom/aa_int_taproom_day.png` (2752x1536) as the only reference, through the local CORS server (bd memory `firefly-reference-upload-via-local-server`).
   - **Prompt:** the text in `dev/asset_team/prompts/aa_int_taproom_chalice_removal_1.txt`. It removes only the goblet and continues the curtain, mist and glow.
   - **Saving:** use Firefly's Download button, then move the file to `Tools/content_generation/absinthe_arcade/hd2d/work_taproom_chalice/gemini_clean_day_1.png`.
   - **Check:** measure the shift against the plate by phase correlation, as in pg9a; it must be 0.
2. **Composite.** Run `python -I Tools/content_generation/absinthe_arcade/hd2d/cut_plate_prop.py Tools/content_generation/absinthe_arcade/hd2d/prop_cuts/taproom_chalice.json composite Tools/content_generation/absinthe_arcade/hd2d/work_taproom_chalice/gemini_clean_day_1.png`.
   - The mask is `work_taproom_chalice/inpaint_mask.png`: the prop mask dilated 16 px and feathered.
   - It rewrites `aa_int_taproom_{day,night,emit}.png` and writes `props/aa_int_taproom_chalice_{day,night,emit}.png` and `props/chalice.json`.
   - **Watch for a ghost.** The chalice's bright glow halo is painted on the curtain. If a dark or bright outline shows after the composite, raise `margin_px` (pg9a needed 40).
3. **Review sheet.** Run `python -I Tools/content_generation/absinthe_arcade/hd2d/prop_review.py Tools/content_generation/absinthe_arcade/hd2d/prop_cuts/taproom_chalice.json j9ru`. Then send a fresh blind Sonnet to gate C (`dev/qc/QC_COVERAGE.md`, checklist C) with the sheet, the files, the spec lines (`the_absinthium_taproom.md:242-245` and `:407`) and the location entries. Log the result in `dev/asset_team/reviews/qc_log.jsonl`.
4. **Close out the art.** Set the board row to in_progress with a thumbnail and the gate C result, comment on j9ru, and sync the bead page.

## Scene steps (a separate task, once the Godot slot is free)

- Add the chalice as one node in the Taproom scene from `props/chalice.json`:
  - a plate-rect quad like the restroom hand quads in `absinthe_arcade_restroom_hd2d.gd`;
  - day and night textures, with emit at night;
  - placed just in front of the alcove curtain.
- Tween its y with a sine of amplitude 6 plate px (convert to world units at the plate scale) and a period of 3.2 s, looping. When low motion is on, hold it still.
- Add a hotspot on the chalice rect bound to the interaction `at_selfie`, so the existing selfie flow runs (`absinthium_taproom_interactions.json` event `at_selfie`). Reimport the plates, then run GUT through `Tools/orchestrator/gut.py`.

## Changed files (uncommitted, this window's only)

- **New files:**
  - `Tools/content_generation/absinthe_arcade/hd2d/cut_plate_prop.py`, `prop_review.py` and `prop_cuts/taproom_chalice.json`
  - `Tools/content_generation/absinthe_arcade/hd2d/work_taproom_chalice/` (two masks)
  - `tools/paint_zones/zones/aa_taproom_chalice_day.json` and `tools/paint_zones/work/aa_taproom_chalice_day/`
  - `dev/asset_team/prompts/aa_int_taproom_chalice_removal_1.txt`
  - this handoff
- **Modified files:**
  - `design/worlds/debaucheryville/sprite_mapping/absinthium_taproom_sprite_mapping.json`
  - `design/worlds/debaucheryville/location_nodes/absinthium_taproom_location_nodes.json`
- **No plates were changed yet.**

## Cleanup

My Firefly tab is closed, and so is the CORS server on port 8773. No Blender or Godot was started.
