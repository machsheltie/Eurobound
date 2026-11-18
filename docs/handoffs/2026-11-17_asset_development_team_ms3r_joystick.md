Window: Asset Development Team (2026-11-17; one task from the Production Desk Orchestrator: Eurobound-ms3r, the closet joystick resize)

# Handoff: Asset Development Team, closet joystick resize (ms3r)

The author's answer (Desk ms3r-q2), verbatim: "Shrink the joystick to the brief (mock-up size); keep the switch as built so it reads".

**The joystick is resized, and blind gate C round 4 PASSED. GUT has not been run** because the Godot slot is taken. Nothing is committed.

## What changed

- **Script:** in `Tools/content_generation/absinthe_arcade/hd2d/closet_wall_props.py`, `joy_corners = quad_world("left", 9.4, 8.6, 1.42, 2.28)`. It was 9.7, 8.3, 1.1, 2.6. The comment explains the sizing.
  - The closet plate is not drawn to tile scale (bd memory `arcade-closet-plate`), so the span is sized to the approved mock-up (`dev/asset_team/arcade_refs/closet/c9_joystick_mockup_*.jpg`, about 60x115 px beside the door) rather than to the brief's tile count.
- **Scene data:** in `game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.gd`, the `PROPS["joystick"]` span is now `["left", 8.6, 9.4, 1.42, 2.28]`, in step with the script. The depth is 9.5, following the far end of the span plus 0.1 as the other wall props do.
- **Re-run:** `python -I Tools/content_generation/absinthe_arcade/hd2d/closet_wall_props.py` wrote 21 sprites. Only the six joystick PNGs and `aa_closet_props.json` changed. The joystick is now 57x117 px at (760,825); it was 96x201.
- **Sheet:** `--sheet dev/asset_team/reviews/ms3r_joystick_r4_sheet.jpg`.
- **The switch is untouched:** 31x79 at (826,475).
- **Blind gate C, round 4: PASS.** The line is in `dev/asset_team/reviews/qc_log.jsonl`. Notes:
  - all six states share one footprint;
  - the alpha is clean with no seam;
  - the faint state is barely visible by design;
  - the joystick is about 1/4 of the door's height (the mock-up is about 1/3).

## For the orchestrator: the test run when Godot is free

```
python -I Tools/orchestrator/gut.py --select maintenance_closet
```

`test_maintenance_closet.gd` checks the wall quads generically from `PROPS`, so no test pins the old span. It was 7/7 before this change.

Godot needs a reimport for the six changed joystick PNGs.

## Tracking

- ms3r has a comment. It stays open for its other items: C5-C7 graffiti split, C10 chandelier, tag pickup, C12 door, A5.
- The bead page is synced and acked.
- Asset Board row `int-aa_closet_build` is set to review, with a new thumbnail.

## Changed files (uncommitted, this window's only)

- `Tools/content_generation/absinthe_arcade/hd2d/closet_wall_props.py`
- `game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.gd` (the `PROPS` joystick line only)
- `game/assets/worlds/debaucheryville/absinthe_arcade/interior/closet/props/aa_closet_joystick_{faint,faint_uv,glowing,glowing_uv,glowing_emit,glowing_uv_emit}.png` and `aa_closet_props.json`
- `dev/asset_team/reviews/ms3r_joystick_r4_sheet.jpg` (new) and `qc_log.jsonl` (1 line)
- this handoff

The untracked `.import` files in `closet/props/` were there before this task and are not mine.

## Cleanup

No processes were started apart from the Python runs, which have exited. No Chrome, Blender or Godot.
