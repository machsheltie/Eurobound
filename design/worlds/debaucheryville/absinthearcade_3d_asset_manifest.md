# Absinthe Arcade — 3D Exterior Asset Manifest

Production manifest for the first hero building's modular exterior kit. The numbers here mirror `tools/content_generation/absinthe_arcade/manifest.json`, which is the source of truth the Blender scripts validate against. **If you change a number, change it in the JSON first.**

- **Location doc:** `design/worlds/debaucheryville/absinthearcade.md`
- **References:** `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/` (8 boards)
- **Blockout:** `Assets/Graphics/worlds/debaucheryville/absinthearcade/blockout/arcade_building_base.gltf`
- **Authoring scene:** `Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/aa_exterior.blend`

## Decisions this kit is built on (author, 2026-10-26)

| Decision | Ruling |
|---|---|
| Engine target | **Unity, Universal Render Pipeline (URP).** FBX is the import format; GLB is still exported for previews. Textures follow URP Lit's slots (see below). |
| Dimensions | **The existing blockout wins:** 14 m wide, 16.8 m to the eave, 20 m to the ridge, 12 m deep. Ground floor 6 m, three upper floors at 3.6 m. Entrance opening 4.4 × 4.8 m. Upper window opening 1.4 × 2.2 m. This supersedes the brief's 12 × 15 m / 4 × 4.5 m arch / 1.5 × 2.5 m windows. |
| Polygon budget | **None.** No triangle limits on any asset or on the building (author, 2026-10-26: the storefront must not look basic). The earlier 80k → 100k ceilings are retired. |
| Surrounding buildings | **Not part of this kit.** The neighbouring buildings in the reference renders were only scaffolding to get the arcade right. None will be used, and none of their signage or names come into the game. |
| "Pillars" | = the street bollards (`aa_prop_bollard`). |

## Conventions

- **Units and axes (engine space):** meters, Y-up, facade front plane at z = 0 facing +Z (the street), building centered on x = 0, sidewalk top at y = 0. In Blender the same building faces −Y. The scripts convert between the two spaces.
- **Scale check:** character reference height is 1.8 m. The arch opening is about 2.4 character heights tall.
- **Snap grid:** 0.1 m. Window bays are centered at x = ±4.6.
- **Naming:** `aa_<category>_<name>` in snake_case. Each asset is one Blender collection with the same name, authored at the world origin. Placed copies are collection-instance empties named `<asset_id>__NN`.
- **Pivots:**
  - `facade` — the building origin
  - `ground` — bottom center of the footprint
  - `wall` — center of the back face, which sits flush on the wall
  - `sill` — bottom center of the window opening, on the facade plane

## Structural layout (front elevation, engine space)

```
 y (m)
 20.0 ┤                 /‾‾‾‾‾‾‾ roof ridge ‾‾‾‾‾‾‾\
 16.8 ┤ ══════════════════ cornice / eave ══════════════════
      │ [win_upper]       ░░░░ aa_decal_mural ░░░░     [win_upper]
 14.1 ┤ [bal_upper]       ░░ (7 × 10.8 m, centered ░░   [bal_upper]
      │                   ░░  x=0, y=11.4)        ░░
 10.5 ┤ [win_upper]       ░░░░░░░░░░░░░░░░░░░░░░░░░    [win_upper]
  9.6 ┤ ─────────────────── floor band ────────────────────────
  6.9 ┤ [win_upper]       ░░ ( Headphone Gentleman ) ░░ [win_upper]
  6.0 ┤ ═══════════ ground-floor cornice ══╡ head ╞════════════
      │ lantern  [win_gnd_arched]  ┌─ stepped pixel marquee ─┐   lantern
  3.0 ┤ hanging  [bal_ground   ]   │   ABSINTHE / ARCADE     │ 13
      │ sign     [awning]          │    tagline bar          │ door
      │ drain    [cabinet] [chalk] │   4.4 m arch opening    │ sign  drain
  0.0 ┼──bollard─────────planter───┴─────────────────────────┴─planter──bollard
     -7.0        -4.6                     0                     +4.6        +7.0   x (m)
```

Exact instance positions are in `manifest.json → assets[].instances`. `setup_scene.py` turns them into the `aa_layout` collection, and `export_assets.py` writes them back out as `export/aa_layout.json` for engine assembly. Three anchors are new and not in the blockout: both wall lanterns and both planters. Adjust them in the JSON if they read wrong.

## Asset list

| Asset ID | What it is | Source | Copies |
|---|---|---|---:|
| `aa_shell_facade` | Hull, openings, recesses, roof, bands, cornice, quoins | Blender (scripted from blockout) | 1 |
| `aa_arch_hero` | Archivolt, Headphone Gentleman sculpt, stepped marquee, tagline bar, neon loop, stained-glass doors | Blender hand + Tripo sculpt | 1 |
| `aa_window_upper` | RETIRED Tripo prefab; upper windows are now built into `aa_shell_facade` (openings, storey-specific surrounds, slide-only sash windows) | Blender scripted (`build_shell.py`) | 0 |
| `aa_window_ground_arched` | Round-headed surround and sash | Blender hand | 1 |
| `aa_balcony_iron_upper` | Juliet rail and pots, top floor | Blender hand | 2 |
| `aa_prop_arcade_cabinet` | Sticker-bombed street cabinet | Tripo + cleanup | 1 |
| `aa_prop_chalkboard` | A-frame pavement sign | Tripo + cleanup | 1 |
| `aa_prop_bollard` | Cast-iron street post (the brief's "pillars") | Tripo + cleanup | 2 |
| `aa_prop_wall_lantern` | Bracket lantern | Tripo + cleanup | 2 |
| `aa_prop_awning` | Corrugated acrylic rain awning | Blender hand | 1 |
| `aa_prop_hanging_sign` | TOKENS / DRINKS / GAMES / REGRETS | Blender hand | 1 |
| `aa_prop_doorframe_sign` | Offer board right of the door | Blender hand | 1 |
| `aa_prop_drainpipe` | Downpipe, brackets, hopper | Blender scripted | 2 |
| `aa_prop_conduit_set` | Purple/green conduit, clips, junction boxes | Blender scripted (curves) | 1 |
| `aa_prop_planter` | Terracotta pot and shrub | Tripo + cleanup | 2 |
| `aa_prop_house_number` | Enamel "13" plaque | Blender hand | 1 |
| `aa_decal_mural` | Green Fairy mural, conforming decal | Blender scripted | 1 |

No polygon limits apply. Model and keep detail wherever it improves the look; the validator only enforces a cap on an asset whose `tri_budget` is set to a number in the JSON (all are `null`).

### Built so far

- **Headphone Gentleman** (part of `aa_arch_hero`), 2026-10-26. Tripo image-to-3D from `references/tripo_inputs/headphone_gentleman_front_day.png`, raw GLB kept in `tripo_raw/`. Kept at full Tripo detail: ~1.51M tris of carved stone (`aa_arch_hero_gentleman`) with Tripo's 4K basecolor / roughness-metal / normal maps. Tripo's own tubes and junction boxes were stripped and rebuilt as clean hard-surface parts (`aa_arch_hero_gentleman_hardware`, ~14k tris): two bolted earcup junction boxes with conduit glands, the green conduit loop over the crown, green side runs and a purple feed that bend back into the wall for the conduit set to pick up. Scale: earcups ~1.05 m apart, bust seated on the arch crown from 5.0 m to 6.5 m.
- **Street props**, 2026-10-26, all Tripo at full detail (~1.45–1.98M tris each, 4K PBR maps), raw GLBs in `tripo_raw/`:
  - `aa_prop_arcade_cabinet`: v2. The first pass (from the photo, kept as `tripo_raw/arcade_cabinet_tripo_raw_v1_photo.glb`) had a potted plant and a bin fused to its sides, so it was regenerated: Tripo Asset Extraction turned the reference views into a clean isolated image (`references/tripo_inputs/arcade_cabinet_clean_extracted.png`), then multi-view 3D from that plus generated side and back views. Slimmed to reference proportions, 0.78 × 1.64 × 0.86 m.
  - `aa_prop_chalkboard`: image-to-3D from the sheet's front view; the "REAL ARCADE / REAL ABSINTHE / REAL BAD DECISIONS" board copy came through in the texture. A stray panel Tripo added on one side was cut off. 0.6 × 1.0 m, A-frame open 0.83 m.
  - `aa_prop_bollard`: image-to-3D from the sheet's bollard front view. 0.32 × 0.9 m.
  - `aa_prop_wall_lantern`: text-to-3D (no clean reference panel): wrought-iron scroll bracket, hexagonal glass box, flat wall plate. Projects 0.79 m from the wall.
  - `aa_prop_planter`: text-to-3D: weathered terracotta pot with a boxwood shrub and trailing ivy. 0.6 × 0.9 m.

- **Hero entrance arch** (`aa_arch_hero`, complete), 2026-10-26. 5.44 m wide × 7.14 m tall, projects 1.45 m. Parts:
  - `aa_arch_hero_archivolt` + `_plinths`: molded stone band swept around the 4.4 m basket arch and down both jambs to stepped plinths (Blender, `m_aa_trim_stone`). Replaces the blockout archivolt.
  - `aa_arch_hero_marquee`: Tripo multi-view from a clean Asset-Extraction image of the Brand Board / entrance references. 4.6 m wide, sits from 3.3 m (top of the door opening) to 5.34 m; the bust's corbel overlaps its stepped crown as in the reference.
  - `aa_arch_hero_tagline_panel`: Tripo garbled the tagline ("USE YOUR MINID"), so a crisp text panel is mounted over the bar face. Textures in `textures/aa_arch_hero_tagline_{basecolor,emissive,neonmask}.png`, neon mask on the purple channel with per-letter flicker phase.
  - `aa_arch_hero_door_leaf_l` / `_r`: Tripo multi-view stained-glass door leaf (clean extraction from the doorway reference), mirrored, 0.84 × 3.25 m each, set into the reveal; walkway between them 2.72 m.
  - `aa_arch_hero_neon_loop`: green neon tube arcing over the head from the marquee's top corners (half-width 2.28 m, apex 7.1 m) on 12 steel standoff clips.
  - Night preview: the marquee, door glass and cabinet get a temporary auto-glow from their saturated green/purple texels (material node `AA_NeonStrength`); the Unity neon mask replaces this in the texture pass.

- **Facade dressing**, 2026-10-26, all Tripo multi-view from clean Asset-Extraction images (sources in `references/tripo_inputs/*_clean_extracted.png`, raw GLBs in `tripo_raw/`):
  - `aa_window_upper` (×6): full baroque window unit (surround, cartouche, sill, casement, curtains, geranium box), 2.0 × 2.99 m, depth flattened to 0.41 m against the wall. The reference's cat on the sill was removed at extraction (no pets/mascots).
  - `aa_window_ground_arched`: arched window plus its iron balcony and plants as one piece, 2.2 × 3.27 m, 0.55 m deep. **`aa_balcony_iron_ground` is retired** (absorbed into this asset).
  - `aa_prop_hanging_sign`: TOKENS / DRINKS / GAMES / REGRETS blade sign on a scroll bracket, projecting from the wall, 1.6 m tall.
  - `aa_prop_awning`: corrugated acrylic canopy on scroll brackets, 1.25 m wide, 0.85 m projection; canopy faces reassigned to a clear `m_aa_glass_acrylic` (Tripo can't make transparency).
  - `aa_prop_doorframe_sign`: offer board, 0.81 × 2.4 m, neon martini at the foot. Tripo garbled the copy (ABSINTRE / PINDALL / CHUICES); a crisp lettering panel (`textures/aa_prop_doorframe_sign_text_basecolor.png`) covers it: ARCADE / ABSINTHE / PINBALL / POKER / & / POOR / LIFE / CHOICES.

- **Fittings**, 2026-10-26:
  - `aa_balcony_iron_upper` (×2): Tripo text-to-3D Juliet balcony (scroll railing, side returns, three geranium pots), 2.1 m wide, sitting on the top-floor sills in front of the window flower boxes.
  - `aa_prop_drainpipe` (×2): Blender cast-iron downpipe, full eave height, hopper head, kicked shoe, wall brackets every 1.8 m.
  - `aa_prop_conduit_set`: Blender. Green conduit from the gentleman's right tube along under the first-floor band to a junction box, then down to a box at street level; purple feed from his purple tube along a higher run into the same box; purple run on the left from the facade edge past a junction box into the marquee's top corner. Clips every 0.6 m. Conduit uses the neon materials so it glows at night as in the reference.
  - `aa_prop_house_number`: enamel "13" plaque, generated texture `textures/aa_prop_house_number_basecolor.png`.
  - Lanterns raised to 4.7 m and the hanging sign lowered to centre at 3.0 m so they no longer collide.

- **Reference-scale pass on the street frontage** (author, 2026-10-26: "the cabinet looks in miniature compared to the reference"). The reference is stylized; props read big against the 3.3 m doorway. Now: cabinet 2.3 m tall (marquee just under the awning), chalkboard 1.5 m, awning 1.63 m wide centred over the cabinet at 2.34–3.32 m, arched window + balcony shrunk to 1.51 × 2.25 m and raised to 3.38–5.63 m so it sits above the awning and under the cornice. Cabinet, awning and window share x = −4.4. **Rule going forward:** size street props against the reference doorway, not real-world catalogue sizes.
- **Shell** (`aa_shell_facade`, `tools/content_generation/absinthe_arcade/build_shell.py`, re-runnable): limestone walls with only the entrance arch cut (window units carry their own glass), recess with a dark interior backing, side/back walls, gables, slate roof, swept plinth, ground-floor cornice, two floor bands, dentilled eave cornice, rusticated quoins. Limestone is a Tripo-generated swatch made seamless (offset-blend) at 2048 px with derived normal / roughness / URP mask (`textures/m_aa_limestone_tile_*`), one repeat per 2.8 m. The blockout is now hidden entirely.
- **Green Fairy mural** (`aa_decal_mural`): recreated flat on white by Tripo's image tool from the Mural Board's clean-artwork panel, upscaled to 4K, keyed to alpha, 6.66 × 11 m from 5.05 m up, shrink-wrapped onto the walls and mouldings so the paint runs over the cornice and bands as in the reference. Its bottom notch frames the gentleman. Night glow: the token (steady) and the green/purple pixel field (flicker) via `textures/m_aa_mural_decal_{emissive,neonmask}.png`.

### What does not get geometry

These are texture or decal work, not polygons:
- marquee lettering and tagline text
- chalkboard and sign copy
- mural (including the painted carved flowers)
- stickers on the cabinet
- the pixel/circuit transition

## Graybox review

- **2026-10-27, baseline:** failed (flat wall plane, windows stuck on, thin bands, floating gentleman). Triggered the architectural quality pass.
- **2026-10-27, after the massing pass:** real openings with recessed sash windows, banded rustication, projecting central bay with lesenes, stepped voussoir arch, keystone-seated gentleman. Still open: arched ground-floor window opening, balconies, gentleman's cartouche surround, retrofit attachment, reseating the mural and props on the new wall faces.

## Source method

**Tripo is used for organic and sculpted forms only.** Its output is one triangulated mesh with an auto-atlas. That is fine for props and the head, and wrong for modular architecture that has to snap on a grid.

| Tripo input | Best reference panel |
|---|---|
| Headphone Gentleman head | Entrance Reference Board, panel 3 (straight on, daylight) + panel 4 (three-quarter) |
| Arcade cabinet | Exterior Reference Sheet, section 1 (front / three-quarter / side / rear) |
| Chalkboard | Exterior Reference Sheet, section 3 (front + side) |
| Bollard | Exterior Reference Sheet, section 5 (front / side / top) |
| Wall lantern | No dedicated panel. Crop from the Clocktower Plaza night shots (left lanterns). |
| Planter | No dedicated panel. Crop from the entrance boards (pots beside the door). |

Generate from a cropped daylight, power-off view so lighting doesn't get baked into the albedo. Then run `ingest_tripo.py`.

**Built in Blender:** the shell (extend the blockout generator), window and balcony trims, the arch frame and marquee, the awning, conduit and drainpipes (curve-based), and the signs.

## UV and texture rules (PBR, Unity URP)

- **Two UV layers on every mesh:**
  - `uv_material` (UV0) — may tile or use trim sheets
  - `uv_bake` (UV1) — unique, non-overlapping, inside 0..1, for AO and lightmaps
- **Per-asset texture set names (Unity URP Lit):**
  - `<asset>_basecolor` → Base Map
  - `<asset>_normal` → Normal Map (OpenGL +Y, Unity's convention, so no flip)
  - `<asset>_mask` → R = metallic, G = ambient occlusion, B = unused, A = smoothness. Assign this one texture to **both** the Metallic Map and Occlusion Map slots; URP reads metallic from R, smoothness from A and occlusion from G.
  - `<asset>_emissive` → Emission Map
  - `<asset>_neonmask` → custom Shader Graph input (below)
- **Material sets:**

| Material | Kind | Res | Used by |
|---|---|---|---|
| `m_aa_limestone_tile`, `m_aa_plaster_tile` | tiling, 2 m repeat | 2048 | shell |
| `m_aa_trim_stone` | trim sheet | 2048 | shell bands, window and balcony stone |
| `m_aa_roof_tile` | tiling | 1024 | roof |
| `m_aa_arch_hero` | unique | 4096 | arch (head gets ~30% of the sheet) |
| `m_aa_iron` | shared atlas | 1024 | balconies, bollards, lanterns, brackets, drainpipes |
| `m_aa_glass_acrylic` | shared, transparent | 512 | window glass, awning, door glass |
| `m_aa_cabinet` | unique | 2048 | arcade cabinet |
| `m_aa_props_atlas` | shared atlas | 2048 | chalkboard, signs, planters, plaque, conduit and boxes |
| `m_aa_mural_decal` | unique, transparent | 4096 | Green Fairy mural |

## Neon / emissive mask

Every neon-bearing asset gets a `_neonmask` RGBA texture on `uv_material`, at the same resolution as its `_emissive` map:

| Channel | Meaning |
|---|---|
| R | Green neon group (#3FF014) |
| G | Purple neon group (#BF00FF) |
| B | Flicker phase 0..1. Paint a different gray per letter or tube segment so the "stuttering 8-bit neon" never blinks in unison. |
| A | Flicker enable. White = stutters, black = steady when lit. |

Shader contract for any engine:
`emission = emissive_map × night + (R × green + G × purple) × anim(B, A) × night`

Warm sources (lanterns, the CRT screen glow, interior spill) live only in `_emissive`, with no mask, so they stay steady and keep their colour.

Neon assets: `aa_arch_hero`, `aa_prop_arcade_cabinet`, `aa_prop_hanging_sign`, `aa_prop_doorframe_sign`, `aa_prop_conduit_set`, `aa_decal_mural` (the fairy's token).

The **Headphone Gentleman gag** depends on this mask. By day, the earcup junction boxes and the tube over his head are plain grey electrical work. At night the R channel lights the tube green and the headset appears. Keep that tube on its own mask island with A = 0 so it doesn't flicker; the joke reads better steady.

`pack_neon_mask.py` combines four grayscale masks into the RGBA file.

## Unity import settings

| Setting | Value | Why |
|---|---|---|
| Format | FBX from `export/fbx/` | Exported -Z forward / Y up with the axis conversion baked in |
| Scale Factor / Convert Units | 1 / on | Blender meters = Unity units |
| Bake Axis Conversion | on | Matches the exporter's baked space transform, so no stray 90° rotation |
| Generate Lightmap UVs | **off** | `uv_bake` already arrives as UV1, which is Unity's lightmap channel |
| Normals / Tangents | Import / Import | Keeps the baked normals valid |
| Read/Write | off | Saves memory; turn on only for meshes used by runtime scripts |
| Prefabs | One prefab per asset ID; `aa_layout.json` drives an editor script that assembles the storefront | Keeps kit pieces reusable |

### Neon Shader Graph contract

Lit Shader Graph (URP) with:
- inputs: `_NeonMask`, `_GreenColor` (HDR, default #3FF014 × intensity), `_PurpleColor` (HDR, #BF00FF), `_FlickerRate`
- a global float `_AA_Night` (0 = day, 1 = night), set from the time-of-day system with `Shader.SetGlobalFloat`
- flicker = `lerp(1, stepped_noise(floor(_Time.y × _FlickerRate) + B × 37), A)`
- Emission = `_EmissionMap × _AA_Night + (R × _GreenColor + G × _PurpleColor) × flicker × _AA_Night`

URP Bloom on the global post-processing Volume gives the glow. The editor script and the Shader Graph get built once the Unity project exists.

## Pipeline

```
setup_scene.py      build collections, import blockout, placeholders, layout
ingest_tripo.py     Tripo GLB -> scaled, pivoted, decimated, UV'd kit asset
validate_assets.py  budgets, UVs, transforms, pivots, dims, materials -> report
pack_neon_mask.py   4 grayscale masks -> <asset>_neonmask.png   (plain Python)
export_assets.py    per-asset GLB + FBX, aa_layout.json        (runs validate first)
```

Commands and flags are in `tools/content_generation/absinthe_arcade/README.md`.

## Open items for the author

None. All four items from the first pass were settled on 2026-10-26 (Unity URP, surrounding buildings out of scope, pillars = bollards, lantern and planter placement approved).
