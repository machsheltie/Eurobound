# Sprite Development Team: handoff, 2026-11-17 (Eurobound-2bb9, Base Color image lookup in char3d)

The Production Desk Orchestrator assigned one task: switch the char3d scripts that took the first image node (and could pick a normal map) to the shared `Tools/item3d/material_lookup.base_image()`.

## Done (bead closed)

| Script | Change |
|---|---|
| `Tools/char3d/find_uv_region.py` | `base_image(me.materials[0])` |
| `Tools/char3d/fix_dark_faces.py` | `base_image(me.materials[0])` |
| `Tools/char3d/whitney_v3_repair.py` (untracked one-off) | first non-None `base_image` over the materials |
| `Tools/char3d/render_dirs.py` | `export_posed` (was line 369) |
| `Tools/char3d/pose_render.py` | its two-step lookup is replaced; it exits with a message if there is no image |

**Import route.** Every char3d script is launched by its path with `blender --python`. `CHAR3D_DIR` only serves item3d finding char3d, not the other way round. So each script adds `<its folder>/../item3d` to `sys.path`, and no new module was needed. `render_dirs.py` lines 121 and 335 already followed Base Color and were left alone, as was `item3d/handheld_screen.py` (per the bead).

## Checks

- **Unit test.** `blender --background --python Tools/item3d/test_material_lookup.py` passed all 5 cases.
- **Regression, old vs new code** (scratch only, 0 Tripo credits):
  - `render_dirs` idle S frame of `cara_shared.glb`: byte-identical.
  - `render_dirs` posed-GLB export of the same frame: byte-identical.
  - `find_uv_region` on Cara: identical output.
  - `fix_dark_faces` on a copy of Cara: identical GLB.
  - `whitney_v3_repair` on `whitney_v3_raw`: identical GLB, and the renders are pixel-identical (the PNG bytes differ only in metadata).
  - `pose_render` on Jakub (`jakub_cradled_v2`): pixel-identical.
- **Known, harmless.** `export_posed` runs on `look.toon_material` materials, where the image feeds a mix node and there is no Principled BSDF. So `base_image` prints its fallback WARNING there, once per material. It picks the only image, which is correct.

## State

- **Changed:** the four tracked char3d scripts above, plus the untracked `whitney_v3_repair.py`.
- **Not touched:** the bros' files.
- Nothing is committed. Every Blender I started has exited.
- The bead page is synced and acked.

This window can be cleared.
