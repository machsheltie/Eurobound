# Sprite Development Team: handoff, 2026-11-17 (Eurobound-59b9, Arcade north wing: split N1-N5 out of the plate)

The Production Desk Orchestrator assigned one task, art and data only. A fresh subagent did the production; each gate C round used a fresh blind Sonnet reviewer.

## State: everything that doesn't need the browser is done; the door is on the Desk; four items wait for Gemini fills

No Godot, GUT, Blender or Chrome was run, and no credits were used. The live plates are unchanged and nothing is committed. The bead is `blocked` with `author-ruling`.

**N2, the maintenance door**
- Made: the leaf, plus top and side lamp pieces in `locked_red` and `unlocked_green` (day, night and emit). The clean plate has the baked lamp light relit out, because the unlock light stays in code.
- Gate C scored 5, 6, then 7 out of 10 (a marginal fail), so it went to the Desk:
  - `Eurobound-59b9-q1`: accept try 3 (recommended), one more fix, or a repaint.
  - `-q2`: what the amber lamp does (it is unlit for now).
  - `-q3`: `opening_exterior_only` as a scene fade (recommended) or new art.
- The earlier tries' images were overwritten in place, so the Desk shows try 3 only.

**N1, N3, N4 and N5 are cut, but their gate C is pending.** The holes behind the DDR and in the left corner (curtain, Time Crisis cabinet, vapour) need a Gemini fill, and the agents' Chrome window was down.
- **N1 DDR:** `error` and `unlock_pulse`. The token states reuse `error`, and the pips stay a stand-in (w2ig).
- **N3 curtain:** `day_inert`, `evening_faint`, `night_breathing`, `discovered`, plus the glow layer and the plaque. The glow levels are for the author's room review, per the plan.
- **N4 Time Crisis:** `displaced_revealed`, `night_glow` and `curtain_hidden`, moved 94 px. `curtain_hidden` needs the left fill first.
- **N5 vapour:** one FX layer. The 20:00-04:00 showing rule is scene work.
- **Fill prep** is in `props_staged/gemini/{ddr,left}_{day,night}` (crop, mask, preview and prompt for each). Finish with `north_wing_cutouts.py --fill <name>=<png>`, then run blind gate C on N1, N3, N4 and N5. After 3 fails, an item goes to the Desk.

## Files (none committed)

- **Staged:** `game/assets/worlds/debaucheryville/absinthe_arcade/interior/north_wing/props_staged/`.
  - A `.gdignore` keeps Godot out of it for now.
  - One JSON per item gives ids, the state-to-file map, per-plate boxes, anchors, the interaction point and draw order.
  - `clean_plates/` holds the staged plates, and `status.json` lists the open holes.
- **Script:** `tools/content_generation/absinthe_arcade/hd2d/north_wing_cutouts.py`. It is deterministic and checks itself: nothing outside the holes changes, and drawing the layers back reproduces the plate.
- **SAM:** prompts in `tools/paint_zones/zones/aa_north_wing_{day,night}.json`, masks in `tools/paint_zones/work/aa_north_wing_*/masks/`. The whole `tools/paint_zones/` folder is untracked.
- **Data:**
  - `design/worlds/debaucheryville/sprite_mapping/absinthe_arcade_sprite_mapping.json` (lines about 311-341 and 478): the Time Crisis id is `cracked_time_crisis_cabinet`, the name `location_nodes` already uses, with `state_source: taproom_curtain`. The curtain and the door get an `interaction_id`, and there are staged-file notes.
  - `design/worlds/debaucheryville/absinthe_arcade_id_map.md:32`.
  - `validate_data.py` passes. Another session's uncommitted edits in the mapping file were left alone.
- **QC:** `dev/asset_team/reviews/qc_log.jsonl` has the door's rounds 1-3. The sheet is `dev/asset_team/reviews/59b9_gate_c_r3_door_sheet.jpg`, and the review PNGs are in the session scratchpad.

## Found and filed

- `Eurobound-10g6`: the day and night plates are misregistered on the left wall by 90-130 px, so `plate_prop_layer.gd` needs a per-plate box. Recommended: a loader change rather than new art.
- `Eurobound-k2bn`: update the interior manifest rows (96-97, 206-207, 242-246) once the pieces are wired.
- Not filed, noted on the bead:
  - The day DDR pads show hands where the night ones show arrows.
  - Bead zx7u's north-wing mask reviews may overlap with this work.
  - The door's derived height (2.86 m) rests on an approximate camera fit.

## For the scene step (orchestrator-gated)

Swap the staged clean plates in only together with the nodes that draw the pieces, so nothing vanishes. Then:
- the door's lamp state follows `arcade_maintenance_restroom_unlocked`;
- the curtain follows the time of day (active 20:00-04:00);
- the Time Crisis cabinet follows the curtain;
- the vapour shows 20:00-04:00 only.

This window can be cleared.
