# Absinthe Arcade Blender pipeline

Scripts for the Absinthe Arcade exterior kit. Specs and budgets are in `manifest.json`. The full production manifest is `design/worlds/debaucheryville/absinthearcade_3d_asset_manifest.md`.

Tested on Blender 5.2.3 LTS. Target engine: Unity URP (import the FBX files). Everything except `pack_neon_mask.py` runs inside Blender.

```sh
BLEND=Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/aa_exterior.blend
DIR=tools/content_generation/absinthe_arcade

# 1. Build or refresh the scene. Safe to re-run; real meshes are never touched.
blender "$BLEND" --python $DIR/setup_scene.py

# 2. Bring in a Tripo model (scaled to manifest height, pivoted, decimated, UV'd).
#    Save the .blend afterwards; background runs don't save on their own.
blender "$BLEND" --python $DIR/ingest_tripo.py -- --asset aa_prop_arcade_cabinet --file cabinet.glb [--yaw 180]

# 3. Check budgets, UVs, transforms, pivots, dims and materials.
blender "$BLEND" --background --python $DIR/validate_assets.py -- --strict

# 4. Pack a neon mask (plain Python + Pillow).
python $DIR/pack_neon_mask.py --green g.png --purple p.png --phase phase.png --flicker flick.png \
    --out aa_arch_hero_neonmask.png

# 5. Export each asset as GLB + FBX, plus export/aa_layout.json.
blender "$BLEND" --background --python $DIR/export_assets.py -- [--only aa_arch_hero] [--allow-placeholders]
```

Outputs go to `Assets/Graphics/worlds/debaucheryville/absinthearcade/export/`.

## Authoring rules the validator enforces

- Model each asset inside its own `aa_kit/<asset_id>` collection, at the world origin, with transforms applied.
- Position it to its pivot rule: `ground`, `wall`, `sill` or `facade` (see `manifest.json → pivots`). In Blender the street side is **−Y**.
- Give every mesh two UV layers, `uv_material` and `uv_bake`. `uv_bake` must stay inside 0..1.
- No polygon limits: `tri_budget` is `null` on every asset. A cap is only checked if an asset is given a number.
- Only the layout collection places things. To move a copy, edit `instances` in the manifest and re-run `setup_scene.py`.

Delete an asset's placeholder before modeling it, or let `ingest_tripo.py` remove it for you.
