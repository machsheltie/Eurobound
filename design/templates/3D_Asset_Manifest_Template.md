# [Building Name] — 3D Asset Manifest

**Purpose:** production manifest for one building's 3D kit (exterior or interior) headed for Godot 4.7 (Forward+ renderer; the Godot project is `game/`). Rules that apply to every kit live in `design/style_guides/3d_asset_rules.md`; this file records what is specific to this building. Every section below is required. Worked example: `design/worlds/debaucheryville/absinthearcade_3d_asset_manifest.md` (its engine sections are from the superseded Unity plan; the current Godot manifest for that building is `Assets/Graphics/worlds/debaucheryville/absinthearcade/absinthearcade_exterior/hd2d_asset_manifest.md`).

**File naming:** `[location]_3d_asset_manifest.md`, snake_case, saved beside the location doc in `design/worlds/[world]/`.

The numbers here mirror `tools/content_generation/[building]/manifest.json`, the source of truth the Blender scripts validate against. **If you change a number, change it in the JSON first.**

- **Location doc:** `design/worlds/[world]/[location].md`
- **References:** `Assets/Graphics/worlds/[world]/[building]/references/` ([N] boards)
- **Blockout:** [path, or "none"]
- **Authoring scene:** `Assets/Graphics/worlds/[world]/[building]/blender/[prefix]_[exterior|interior].blend`

## Decisions this kit is built on (author, [date])

| Decision | Ruling |
|---|---|
| Dimensions | [width × eave × ridge × depth; floor heights; key openings] |
| Scope | [what is built; which reference elements are scaffolding and never built] |
| Building-specific rulings | [e.g. canon props, window types, open/closed states] |

## Conventions

- **Units and axes (engine space):** meters, Y-up, [front plane / origin rule]. Blender equivalent: [axis note].
- **Scale check:** character reference height 1.8 m; [key opening] is about [N] character heights.
- **Snap grid:** [value]. Bay centres: [values].
- **Naming:** `[prefix]_<category>_<name>` in snake_case; one Blender collection per asset at the world origin; placed copies are collection-instance empties named `<asset_id>__NN`.
- **Pivots:** [list the pivot types this kit uses and what each means].

## Structural layout

[Front elevation (or plan) diagram with heights and x positions, plus a note pointing to `manifest.json → assets[].instances` for exact anchors.]

## Asset list

| Asset ID | What it is | Source (Tripo / Blender scripted / hand) | Copies |
|---|---|---|---:|
| `[prefix]_shell_[...]` | [...] | [...] | [n] |

### Built so far

[One entry per asset as it lands: what was made, from which reference, final dimensions, and anything a later pass must know.]

### What does not get geometry

[Elements handled by decals, textures, or left out, and why.]

## Graybox review

[Date and result of each clay review (renders, what failed, what was fixed). Ornament work starts only after a pass is recorded here.]

## Source method

[Per asset class: which reference crop, Tripo template and steps, or which script builds it.]

## UV and texture rules

[Texture sets per material (StandardMaterial3D slots: `_basecolor` Albedo, `_normal` Normal Map, `_orm` ORM, `_emissive` Emission), texel density, scene texture caps, which surfaces the author hand-paints.]

## Emissive / neon

[If the kit has lit elements: mask channel layout and the `ShaderMaterial` / `.gdshader` contract (or the StandardMaterial3D Emission setup). Otherwise "None".]

## Godot import settings

[GLB (glTF 2.0) import options and destination folder under `game/`, StandardMaterial3D / ShaderMaterial mapping, layout JSON assembly into a Godot scene.]

## Pipeline

[The script run order for this kit, from reference to export.]

## Open items for the author

[Decisions awaiting an author ruling.]
