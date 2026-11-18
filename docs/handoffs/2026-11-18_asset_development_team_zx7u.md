Window: Asset Development Team (2026-11-18; one task from the Production Desk Orchestrator: finish Eurobound-zx7u on the author's Desk answers q1-q3)

# Handoff: Asset Development Team, Arcade masks and guides finished (zx7u)

All seven Arcade masks and guides are built, and **Eurobound-zx7u is closed**. Nothing is committed. Godot and GUT were not touched. No Chrome, Blender or Godot was started, and the one blind-review subagent has finished.

## Author answers acted on (Eurobound Desk, verbatim)
- **q1:** "A: A top-down map of the street (plan view): blocked areas and the things that hide the bros, seen from above /"
- **q2:** "A: Yes, make a mirror-corridor interaction mask too, the same way /"
- **q3:** "A: Rename that label to exit_north_arch, space out the crowded labels, and ship it without another review round /"

## What was built
One script still rebuilds everything, in about 70 s:

```
python -I Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py
```

It was re-run on the current code, which includes the ikba hall re-measure and the 0wn9/a4zx north wing blockers. Every camera round trip is 0.000 px.

- **Exterior (q1):** `game/assets/worlds/debaucheryville/absinthe_arcade/exterior/masks/`
  - All files are a top-down plan in real metres at 100 px/m, 2500x2500. The pixel transform is in each JSON legend: +X right, -Z (behind the building) up, so the camera side is at the bottom.
  - `aa_mask_exterior_collision.png`: white is blocked. It holds the street box and its edge walls, the building box and `SOLID_PROPS`. The legend also lists the door trigger and the spawns.
  - `aa_mask_exterior_occlusion.png`: grey shows how much of a bro standing there the follow camera cannot see (0 = visible, 255 = hidden). Each floor point is ray-cast at 5 body heights to the fixed-offset Phantom camera. The occluders are the building, cabinet, awning (box plus bracket cards), the A-frame chalkboard, billboards turned to the camera yaw, the wall sign and the lanterns.
  - `aa_mask_exterior_occlusion_ids.png`: each occluder's footprint in its own colour, with its hide zone in the same colour at 55%.
  - The legend lists what is not modelled. The door leaves have no geometry yet (d4i6). The flyer panel sits flat on the wall.
- **Mirror corridor (q2):** `interior/masks/aa_mask_interior_interaction_mirror_corridor.png` + `.json`.
  - It shows `shadow_switch_1..3`, each with a 1 m reach (1.818 tiles) and its stand point and facing (west/east/west), plus `exit_north_arch`.
  - `exit_south_to_hall` is off the plate, and the legend says so. The north wing legend now flags its own off-plate south exit the same way.
- **Scale guide (q3):** `Assets/Graphics/.../guides/aa_guide_scale_camera.png`. The label now reads `exit_north_arch`, and every label keeps 34 px clear. It shipped with no QC round, logged as shipped on the author's ruling.
- **Review images:** `dev/asset_team/reviews/zx7u_aa_mask_exterior_plan_labels.jpg` (labelled exterior plan) and `zx7u_aa_mask_interior_interaction_mirror_corridor_overlay.jpg`.

## QC
Blind gate C5 + T7 + code fidelity, round 4, covered the two new masks only. They **passed first time**.
- The reviewer recomputed everything independently. The worst errors were 0.018 m (the awning tube radius) and 0.05 px.
- I then applied the reviewer's two optional exactness fixes:
  - the tube radius in the awning geometry;
  - `stand_facing` in the corridor legend, which matches the reviewer's values.
- Both log lines are in `dev/asset_team/reviews/qc_log.jsonl`.

## Findings filed (code, not art; this art session changed no code)
- **Eurobound-5mab:** the bros can walk behind the Arcade building, where the camera loses them completely (about 36 m² fully hidden). The street box is ±12 m and the building only reaches z -7.5. The likely fix is to block that strip. Cutting the building away instead would be a Desk question.
- **Eurobound-a0it:** the exterior chalkboard collider sits 0.24 m in front of the art (`SOLID_PROPS`, exterior .gd:804), and the cabinet collider is 4.6 cm off.
- Not filed, noted only: the exterior's interact points (Wi-Fi hotspot, examine points) have no mask. The spec doesn't list one, so it's an author call if ever wanted.

## Re-run build_masks_guides.py when these land
- 5mab, a0it, d4i6 (doors): exterior masks.
- 59b9: north wing masks and overlay.
- ssv5: hall occlusion and scale guide.
- Any later fix to hall, north wing or corridor colliders, interact points or switches.

## Tracking
- zx7u is closed with a comment.
- New beads: 5mab and a0it.
- The bead page is synced and acked.
- The Asset Board row `int-aa_masks_guides` is set to done, with a note in plain words and three thumbnails (street map, corridor mask, final scale guide).

## Changed files (uncommitted, this window's only)
- `Tools/content_generation/absinthe_arcade/hd2d/build_masks_guides.py` (untracked; extended with the corridor, the exterior plan and the label spacing)
- `game/assets/worlds/debaucheryville/absinthe_arcade/exterior/masks/` (new: 3 PNG + 3 JSON)
- `game/assets/worlds/debaucheryville/absinthe_arcade/interior/masks/` (regenerated, plus the new mirror_corridor PNG + JSON)
- `Assets/Graphics/worlds/debaucheryville/absinthearcade/guides/` (regenerated; the PNGs are gitignored)
- `dev/asset_team/reviews/zx7u_*` (review images) and `qc_log.jsonl` (2 lines)
- this handoff

## Next for this window
u5xn-q1 (rebuild the rhinestone shirt in Tripo, about 130 credits). The orchestrator will send it as its own task. It was not started.
