# 3D Asset Rules

Binding rules for every 3D asset (buildings, props, decals) headed for the Godot build (project in `game/`). Author rulings, 2026-10-26 to 2026-10-27, unless marked otherwise. Building-specific rulings (e.g. the Absinthe Arcade window cat, its slide-only sash windows) live in that building's manifest and the rulings ledger, not here.

## Target and pipeline

- **Engine: Godot 4.7, Forward+ renderer.** GLB (glTF 2.0) is the import format, placed under `game/` and imported by Godot's scene importer. Materials are `StandardMaterial3D` (a `ShaderMaterial` where a custom `.gdshader` is needed). Textures follow the StandardMaterial3D slots: `_basecolor` (Albedo), `_normal` (Normal Map), `_orm` (ORM texture: R ambient occlusion, G roughness, B metallic), `_emissive` (Emission).
- **Pipeline:** author reference images → Tripo Studio → Blender → GLB plus a layout JSON for Godot scene assembly.
  - Tripo: run the reference crop through Image → **Asset Extraction** first (Tripo fuses anything touching the object into the mesh), then Generate 3D, then Export → GLB into the building's `tripo_raw/`.
  - Blender: every step is a re-runnable script in `tools/content_generation/<building>/`, driven by that folder's `manifest.json` (the source of truth for ids, dimensions, pivots and instances). Change numbers in the JSON first.
- **Every building gets a manifest doc** copied from `design/templates/3D_Asset_Manifest_Template.md`.

## Fidelity

- **The reference images are canon.** Match them: proportions, details, which window is which. When unsure what a reference shows, crop it at full resolution and look before building.
- **Surrounding buildings in a reference are scaffolding.** Build only the subject; none of the neighbours, their signage or their names enter the game.
- **Size props against the reference** (the doorway is the yardstick, stylized), not real-world measurements.
- **No polygon limits** on any asset or building (`tri_budget` stays `null`). Detail goes wherever it improves the look.
- **Textures inside the Blender scene are capped** at 4K for hero pieces and 2K for props; Tripo's 8K originals stay in the `tripo_raw/` GLBs. (Uncapped 8K maps exhausted GPU memory and crashed every render.)

## Architecture before detail

The untextured gray model must already read as a convincing, specific building.

1. Build large and medium forms first: real depth planes, recessed openings with reveals, projecting cornices and string courses with real profiles, plinth, physical thickness on everything that has it, small bevels on every edge that catches light.
2. **Graybox review:** render in neutral clay (mural, neon and textures off) under low raking daylight, plus an entrance close-up (see `tools/content_generation/absinthe_arcade/graybox_review.py`). Proceed to ornament only once the gray model passes.
3. Ornament and small detail last, and only where it answers a question: structural, decorative architecture, an old repair, retrofit, attachment logic, silhouette, or environmental history.

Later additions (signage, conduit, junction boxes, awnings, lighting) look chronologically newer than the architecture and visibly fastened to it: brackets, clamps, anchors, standoffs, cable entries.

## Surfaces belong to the author

- **The author hand-paints all distress and weathering** (Ucupaint): cracks, stains, grime, runoff, patches, edge wear. Agents build clean base surfaces.
- **Base material textures come from the author** as seamless, flat-lit, straight-on paintings. An agent's job is to make them tile cleanly and project correctly (by face direction, so reveals and returns don't smear), and to keep them a restrained underpainting.

## Working practice

- **Agents drive the tools themselves** (Tripo in the browser, Blender over MCP and scripts). Hand back only what needs a human: purchases, browser permission prompts, secrets.
- **Save before rendering, and render out of process** (`tools/content_generation/absinthe_arcade/render_shot.py` in a background Blender), so a crash never costs the live session.
- **Large binaries go through Git LFS** (`*.blend`, `*.glb`, `*.fbx`, world images). Commit `.blend` files at milestones only; each version adds its full size to LFS.
