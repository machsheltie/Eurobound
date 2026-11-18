# Sprite Development Team: handoff, 2026-11-17 (Eurobound-d4i6, window cat and front doors cut out of the Arcade front face)

The Production Desk Orchestrator assigned one task: cut the window cat and the front door leaves, plus the entrance glimpse, out of `aa_face_front` (day, night and emit), rebuild the plate behind them, and run blind gate C. The cat is canon and is never removed from the game.

## State: the art pass is done; the cat is blocked on the author; nothing is wired

- **Nothing in the game changed.** The live face, `game/assets/worlds/debaucheryville/absinthe_arcade/exterior/faces/aa_face_front_*`, is untouched and still has the cat painted in. All new files are staged.
- **Doors pass gate C** (8/10, round 1).
- **The cat fails gate C three times** (5, 5 and 5). The card is fine; every fail is on the wall rebuilt behind her: a smeared curtain, seams along her outline, and a relief ghost in the height map. Under the asset QC rule, three fails send it to the author. It is on the Desk as `Eurobound-d4i6-q1`, with the three tries side by side. The recommended option is a Firefly fill, as was done for the restroom statue (pg9a). The bead is `blocked` with `author-ruling`.

## Files (none committed)

**Tool** (committable, deterministic): `Tools/content_generation/absinthe_arcade/exterior_cutouts/front_face_cutouts.py`.
- Reads the live plates and writes everything below.
- It checks that every pixel outside the cut regions is unchanged on all 5 maps.
- `--review DIR` writes the gate C images.

**Staged clean plates:** `Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_exterior/02_facade/_staged_d4i6/aa_face_front_{day,night,emit,height,normal}.png`.

**New layers** (`.../absinthearcade_exterior/07_props/`):
- **Doors:** `aa_prop_front_door_leaf_{left_outer,left_inner,right_inner}_{day,night,emit}.png` and `aa_layer_entrance_interior_{day,night,emit}.png`.
  - Placement is in `aa_prop_front_doors.json`: the opening is face px 289-766 × 1224-1700, with a median height per piece for its depth.
  - Behind them, the plate is the dark doorway void (height 1, flat normal).
  - The threshold step and the leaves' kick plates below row 1700 stay painted.
- **Cat:** `aa_prop_window_cat_{day,night,emit}.png` and `aa_prop_window_cat.json`.
  - The JSON gives top-left px, size, real size (about 0.28 × 0.49 m), sill height 6.36 m, and centre x −1.896 m.
  - The source is the approved plate cat. `TR/aa_prop_window_cat.glb` is unused, and the idle loop was not made (it is optional).

**QC:** `dev/asset_team/reviews/qc_log.jsonl` has 4 lines (doors r1; cat r1, r2, r3). The sheets are `dev/asset_team/reviews/d4i6_gate_c_r{1,2,3}_*.jpg` and `d4i6_game_size_{day,night}.jpg`. The Desk image is `.desk_upload/sprite_dev/d4i6_cat_three_tries.jpg`.

## For the wiring step (orchestrator-gated: Godot, scene, GUT)

1. **Copy the files.** Copy the staged plates over the live faces only in the same change that adds the cat card and the door layers, so the cat is never missing. The new 07_props PNGs need copying into `game/.../exterior/props/` too.
2. **Load the layers.** Load the door pieces and the glimpse the way `_build_flyer_panel` loads its cards. The glimpse belongs at recess depth.
3. **Keep `exit_front_door` as it is.**
4. **Move the cat's examine point.** `EXAMINE_POINTS["window_cat"]` (gd:886) is at x −3.3, about 1.4 m left of the cat and just past the building's left corner (−3.21). It belongs near x −1.9, which is close to the facade Wi-Fi hotspot at (−2.06, 1.35), so check the nearest-interact pick.
5. **Confirm the examine text still plays:** `absinthe_arcade_hall_lines.json:29`.

## Process

No Godot, Blender or Chrome was started, and no Tripo or Firefly credits were used. Each QC round used a fresh blind Sonnet reviewer. The bead page is synced and acked. This window can be cleared.
