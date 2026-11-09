# Absinthe Arcade Exterior — HD-2D Asset Manifest

Engine: **Godot 4.4**. Build: **painted-box diorama**. The building is simple 3D boxes
(main block + angled left corner bay + mansard roof wedge) that wear painted textures. Props
and characters are flat `Sprite3D` billboards. Finish: **painterly HD**, matched to the reference
renders. Massing: **asset-sheet building** (4 storeys, slate mansard, dormers, chimneys).
Author rulings, 2026-11-02.

Bible: `references/Exterior/` (every image). Canon details: `references/mastercomponentbreakdown.md`.
Window cat stays (see memory ruling). Neighbouring cafe and plaza buildings are scaffolding; they are never built.

## Technical frame

| Item | Value |
|---|---|
| Camera | Fixed HD-2D tilt (~30-40 deg down), perspective with a narrow FOV, depth-of-field tilt-shift |
| Elevation art | Strict orthographic, no perspective, so it maps onto box faces without distortion |
| Texture size | Shared scale 66.5 px/m (front wall 15.4 m = 1024 px). Front 1065x1712, sides 18 m deep (left 1405x1712 incl. hanging sign, right 1294x1712), back 1066x1722, roof top 1024x1197. Sizes in `02_facade/faces.json` |
| World scale | Footprint 15.4 m wide x 18 m deep (author 2026-11-02: deep enough to hold the hall loop, mezzanine and north L-wing); ~25.8 m to chimney tops; roof deck at 23.6 m |
| Filtering | Linear + mipmaps (painterly, not pixel art); sRGB albedo |
| Day/night | Separate baked-light textures per face: `_day` and `_night`. Night also gets an `_emit` mask (neon, windows, lanterns) for the Godot glow pass |
| Alignment | Day and night are pixel-registered (cross-fade safe): night is a Nano Banana Pro relight of the day master, SIFT/affine-registered (median residual ~0.5 px), then given the day silhouette. Glow pass baked by `night_glow.py` |
| Props | Alpha PNG cutouts, pivot at bottom centre, `_day` / `_night` / `_emit`, 400 px/m at real-world size (`07_props/props.json`, built by `finalize_props.py`). Placed in Godot at PAINT_SCALE 2.4 (see Scale) |
| Scale | The painted facade reads at ~2.4x real size (its double doorway is 7.25 m; real ~3 m). **Ruling 2026-11-02: the world is in real metres.** The diorama node (building + props, laid out in painting units) is scaled by 1/2.4 in Godot, so characters, physics and the camera use true metres; a 1.8 m person stands cabinet-high beside a ~3 m doorway |
| Relief | Every face also ships `_height` (128 = wall plane, ±1 m range) and `_normal`. Godot displaces a subdivided quad (`game/worlds/debaucheryville/hd2d_relief_face.gdshader`, relief_scale 0.35): sills, cornices, mouldings, carving, neon/conduit and the marquee project; windows and the doorway recess; steep returns are shaded as stone. One height map serves day and night. Height source: Firefly NB Pro (aspect **Auto**) converts the day master into a grey height render, then `register_to.py` (picks affine or plain resize by edge overlap) -> `_gen/<face>_height_reg.png` -> `finalize_faces.py` |

## Deliverables

Status key: ☐ todo · ◐ generated, needs QA · ☑ approved

### A. Building faces (box textures)
| id | day | night | emit |
|---|---|---|---|
| aa_face_front (hero) | ◐ | ◐ | ◐ |
| aa_face_left (incl. corner bay) | ◐ | ◐ | ◐ |
| aa_face_right | ◐ | ◐ | ◐ |
| aa_face_back | ◐ | ◐ | ◐ |
| aa_roof_mansard (slopes, dormers, chimneys) | ◐ | ◐ | ◐ |

### B. Depth layers (alpha cutouts that stand proud of the front face)
| id | day | night |
|---|---|---|
| aa_layer_marquee (sign + tagline bar) | ☐ | ☐ |
| aa_layer_keystone_head (headphone gentleman + tubes) | ☐ | ☐ |
| aa_layer_entrance_interior (depth card seen through the doors) | ☐ | ☐ |
| aa_layer_awning (corrugated rain awning) | ☐ | ☐ |

### C. Street props (billboards)
| id | day | night |
|---|---|---|
| aa_prop_street_cabinet | ☐ | ☐ |
| aa_prop_chalkboard ("REAL ARCADE / REAL ABSINTHE / REAL BAD DECISIONS") | ☐ | ☐ |
| aa_prop_wall_sign_tokens ("TOKENS / DRINKS / GAMES / REGRETS") | ☐ | ☐ |
| aa_prop_hanging_sign_clocktower_plaza | ☐ | ☐ |
| aa_prop_wall_lantern | ☐ | ☐ |
| aa_prop_bollard | ☐ | ☐ |
| aa_prop_potted_shrub | ☐ | ☐ |
| aa_prop_metal_bucket | ☐ | ☐ |
| aa_prop_window_cat | ☐ | ☐ |

### D. Tileable surfaces
| id | variants |
|---|---|
| aa_tile_limestone_wall | day (one albedo; lighting comes from the engine) |
| aa_tile_slate_roof | day |
| aa_tile_cobblestone | dry_day, wet_night |
| aa_tile_checker_floor | day |

### E. Validation
- ◐ Godot diorama `game/worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn` (N toggles day/night); captures in `11_technical/godot_captures/`
- Contact sheet of every asset at game scale over the cobble ground
- Godot preview scene `game/worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn` with a day/night toggle

## Provenance
Generated with GPT Image (ChatGPT, the author's account) from the author's reference images,
which were made with Nano Banana 2 and GPT Image 2.5. Post-processing (crop, register, alpha,
resize) is done by deterministic scripts in this folder. Each delivered file is logged in `provenance.json`.

## Build pipeline (re-runnable)
1. Generate/relight in Firefly (Nano Banana Pro); raw outputs in `02_facade/_gen/`.
2. `tools/content_generation/absinthe_arcade/hd2d/register_to.py DAY NIGHT OUT` aligns night to day.
3. `night_glow.py` bakes neon bloom (`--disc` for the fairy token).
4. `finalize_faces.py 02_facade/_gen 02_facade` writes `_day/_night/_emit` + `faces.json`.
5. Copy `02_facade/aa_*.png` + `faces.json` to `game/assets/worlds/debaucheryville/absinthe_arcade/exterior/faces/`.
