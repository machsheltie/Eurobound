Window: Asset Development Team (2026-11-17; one task from the Production Desk Orchestrator: Eurobound-zx7u, the seven missing Arcade masks and guides)

# Handoff: Asset Development Team, Arcade masks and guides (zx7u)

The author's ruling (rcj-q1..q7) was "Build the missing ones". **Five of the seven ids are built.** Four of them passed blind review; the fifth, the scale/camera guide, is on the Desk. **Two ids wait on the Desk.** zx7u is **blocked** on Desk cards q1, q2 and q3. Nothing is committed. Godot and GUT were not touched.

## Built

Everything is derived from the scene code through each room's paint camera, never painted. The round trip is 0.000 px for both cameras.

The script is `Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py`. It reads the constants from the `.gd` files by regex; the hall depth-layer outlines come from `interior_layer_polys.json`. Rebuild with:

```
python -I Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py
```

The spec names one file per id, but the inside spans two plates, so the interior masks come as `_hall` and `_north_wing`. Each has a JSON legend. All are 2752x1536.

- **Interior collision:** `game/assets/worlds/debaucheryville/absinthe_arcade/interior/masks/aa_mask_interior_collision_{hall,north_wing}.png`. White is blocked, black is walkable. It holds the walls, `FLOOR_BLOCKERS` and the occluder-prism colliders.
- **Interior interaction:** `.../masks/aa_mask_interior_interaction_{hall,north_wing}.png`. One flat colour per `INTERACT_POINTS` id plus the exit boxes, each a 1 m reach disc.
- **Interior occlusion:** `.../masks/aa_mask_interior_occlusion_{hall,north_wing}.png`, plus `_hall_ids.png` with sort depths in the legend. The north wing mask is empty because that room has no occluders in code.
- **Node overlay:** `Assets/Graphics/worlds/debaucheryville/absinthearcade/guides/aa_guide_node_overlay_{hall,north_wing}.png`. Every `aa_node_*` is labelled at its code position. `aa_node_mirror_corridor` on the north wing is off the plate, so its dot is clamped and flagged in the legend.
- **Scale and camera guide:** `.../guides/aa_guide_scale_camera.png` (hall). It shows bro scale at four depths, the 16:9, 16:10 and 4:3 crops, the walkable lanes and the sightlines.
- **Git:** the guide PNGs are gitignored (`Assets/Graphics/worlds/**/*.png`); they rebuild from the script. The `.import` files beside the masks were written by a Godot editor another session has open. They are not hand-written.
- **Review overlays:** `dev/asset_team/reviews/zx7u_*_overlay.jpg` and `zx7u_scale_camera_1280.jpg`.

## QC

There is no dedicated gate for masks. I used gate C item 5 and gate T item 7 from `dev/qc/QC_COVERAGE.md`, plus a code-fidelity check. Every line is in `dev/asset_team/reviews/qc_log.jsonl`.

- **Round 1:** the masks and node overlays PASS. The reviewer recomputed 10 blockers, 1 occluder and 6 interaction anchors independently, and all match. The scale guide failed on overlapping labels.
- **Round 2 (guide only):** the overlap was fixed, but 3 labels were not exact ids.
- **Round 3 (guide only):** one label should read `exit_north_arch`, and one cluster of labels is crowded. That makes two failed fixes, so it went to the Desk as **Eurobound-zx7u-q3**. My recommended option: rename that label, space out the cluster, and ship without another round.

## Waiting on the Desk (window "Asset Development Team")

- **Eurobound-zx7u-q1: what form the outside masks take.** The exterior is a 3D street with a follow camera (`absinthe_arcade_exterior_hd2d.gd`), so there is no single plate. Options: A, a top-down plan (recommended); B, the start-camera view; C, over the facade picture.
- **Eurobound-zx7u-q2: a mask for the mirror corridor.** The mirror switches live in the mirror-corridor room. Options: A, build its interaction mask too (recommended); B, no.
- **Eurobound-zx7u-q3: finishing the scale guide**, as above.

## Findings filed (code, not art; the art session changed no code)

- **Eurobound-0wn9:** the north wing has a gap in its DDR floor blocker. `absinthe_arcade_north_wing_hd2d.gd:58-59` leaves z 8.7-9.9 open in front of the painted cabinet.
- **Eurobound-tsd0:** `location_nodes/absinthe_arcade_location_nodes.json:42` puts the claw alcove west of the bar. The code (x 6.3) and the plate put it east.
- **Eurobound-ikba:** hall code that drifts from the plate:
  - the stool blockers;
  - the foosball and prize_counter anchors;
  - no sort depth for the mezzanine and north arch layers (the arch outline is a rectangle);
  - the `NORTH_EXIT_Z` threshold sits about 110 px below the painted arch.

## Re-run `build_masks_guides.py` when these land

- **59b9** (north wing plate): the three `*_north_wing` masks and the north wing node overlay.
- **ssv5** (DDR pads): the hall occlusion mask (the DDR cut-out alpha) and the scale guide.
- **d4i6** (doors and cat): the hall occlusion mask if the `entry_doors` layer changes, and the exterior masks once they are built.
- **0wn9 / ikba:** after any code fix.
- **j9ru** (Taproom chalice): no effect. The taproom is not one of these plates.

## Tracking

- zx7u is blocked, with comments.
- New beads: 0wn9, tsd0, ikba.
- The bead page is synced and acked.
- New Asset Board row `int-aa_masks_guides`, set to parked, with a note naming the three Desk cards.

## Changed files (uncommitted, this window's only)

- `Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py` (new)
- `game/assets/worlds/debaucheryville/absinthe_arcade/interior/masks/` (new: 7 PNGs + 6 JSON legends)
- `Assets/Graphics/worlds/debaucheryville/absinthearcade/guides/` (new: 3 PNGs, gitignored, + 3 JSON)
- `dev/asset_team/reviews/zx7u_*` (7 review images) and `qc_log.jsonl` (4 lines)
- this handoff

## Cleanup

A Sonnet build subagent and three blind reviewers ran, and all have finished. No Chrome, Blender or Godot was started.
