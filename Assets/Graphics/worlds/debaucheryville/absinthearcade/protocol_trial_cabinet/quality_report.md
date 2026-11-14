# Quality report: Protocol Trial 2, Absinthe Arcade street cabinet

Bead Eurobound-nhxz.9 (trial asset confirmed by the author, Desk Eurobound-nhxz-9-q1: "Yes, use the street cabinet"). Protocol: `design/style_guides/reference_locked_texturing_protocol.md`. Date 2026-11-14. Producer: technical artist (asset team). This is the final version after the blind nhxz.8 review (REVISION REQUIRED) and the last step-11 pass.

## Outcome: REVISION REQUIRED

Every defect the blind review named that was a projection or fill fault is fixed and measured (halos, black void, black back face, unpainted corners, yellow slivers, doubled rail, ORM seam texels). What is still wrong, and why this is not APPROVED:

- **The textures are soft.** On nine of the fifteen zones the render has only about 0.26 to 0.5 of the reference's edge detail (table below). The pixels are the reference's own, but the 400 px/m painting went through bilinear sampling into a 2048 atlas, a JPEG q92 intermediate in the projection tool, and a render filter; no sharpening was applied. Close up, lettering and sticker edges are visibly softer than the approved art.
- **Large parts of the mesh carry no art at all.** The back, the underside, the CRT and coin-door recess walls, the bevel strips and the sliver of mesh outside the reference silhouette are one flat colour, #231C24 (see "What each region is").
- **PBR values are assumed** and the Ucupaint step failed headless (see below).
- The blind review gate has not been re-run on this version.

Nothing here replaces the in-game cabinet; no `.gd`, `.tscn` or game data was touched.

## Correction to earlier versions of this report

The first report called the back and other unseen surfaces "inferred plain body paint". That was wrong. A build bug (the fill colour was written as a linear value, `c**2.2`, which stored as 3/255) made all of them near-black: the back face rendered mean RGB 3. A black fill under feathered zone edges was also the cause of the dark halo rings the blind review found around buttons, the joystick, the deck edge and the coin door. Both are fixed in this version; the numbers below are from the fixed version. A stale `*_orig.glb` copy kept by the projection tool hid the fix for one run (it always restarts from that copy), which is why the first re-run showed identical numbers.

## What each region is

| Region | What is on it | Source |
|---|---|---|
| Front face: marquee, CRT bezel and screen, deck, buttons, joystick, fascia, coin door, kick panel with stickers, both rails | Reference pixels, camera-matched orthographic projection (SAM zones plus a full-silhouette base pass) | directly observed |
| Top slope above the marquee | The front reference projected onto the slope (the marquee art and the grey-black housing above it), at a low normal threshold; stretched along the slope, exact seen from the front | observed (front reference), stretched |
| +X flank: body, stickers, yellow trim | Reference pixels from the side reference, flat side wall only | directly observed |
| -X flank | The +X reference mirrored horizontally, so the sticker layout is a copy of the other side | **inferred** |
| Back face | **Flat colour #231C24 (the +X side body median). No grain, wear, markings or paint detail** | **inferred** |
| Underside, recess walls (CRT, coin door), bevel strips, mesh edge beyond the reference silhouette (the old black wedge beside the right rail, the lower-right pockets) | **Flat #231C24, no detail** | **inferred** |
| Normal map | Flat, except sticker-vinyl edge relief derived from the SAM sticker mask (2.3% of texels) | inferred |
| Roughness, metallic | Assumed per finish: matte paint 0.75-0.85, plastic 0.3-0.55, CRT glass 0.08, coin door metallic 0.6 | **assumed, not measured, not physically validated** |
| AO | A real Cycles bake of the rebuilt mesh (so it also bakes the inferred back and underside) | computed |
| Emissive | The emit reference (marquee, screen, button glow); untouched texels forced to 0 | observed |

## Step by step

| # | Step | Result |
|---|---|---|
| 1 | Register references | DONE. Six canonical PNGs (front/side x day/night/emit) copied byte-identical to `source_references/`, sha256 in `source_references.json`; originals in `07_props/` untouched. Not added to `tools/paint_zones/refs/registry.json` (shared, untracked file in another checkout). |
| 2 | SAM masks | DONE. SAM 2.1 hiera_base_plus, box + point prompts, front 12 zones, side 3, scores all >= 0.8; overlays in `sam_overlays/`, masks in `masks/`, crops in `crops/`. Producer-checked only; **the blind mask review has not been done**. SAM's side body mask has holes (dark sticker interiors), so the side also has a silhouette base pass. |
| 3 | Material manifest | DONE. `material_manifest.json`: 19 entries, colours sampled from the crops, observed vs inferred labelled (inferred: -X flank, back, underside/walls/edges). |
| 4 | GPT Image studies | NOT RUN. No supplemental view was needed. |
| 5 | Mesh (Tripo + Blender) | **Tripo raw mesh rejected, rebuilt by script (nhxz.3 method).** Raw mesh: 0.58 x 0.57 x 0.98 m, aspect 0.59 against 0.39, a different design, side IoU 0.753. Rebuilt `street_cabinet_trial.glb`: side profile traced from the reference alpha and, in this pass, **restored to the traced silhouette** (the first rebuild raised the front-top corner to match the marquee and added a black wedge at the top), extruded to 0.725 m, CRT recess and coin-door plate from the front layout, bevels, 2.5 cm grid tessellation, 26,824 triangles, 0.725 x 1.847 x 0.955 m, one 2048 UV atlas. Tripo website texturing not used: **0 credits spent**. |
| 6 | SAM-guided projection | DONE with `tools/char3d/project_ref.py` (unforked). Reliability IoU (tool): **front 0.974, right 0.983, left 0.984**. Own full-resolution silhouette check: front 0.961, side 0.980 (was 0.954 before the top was restored). This pass added: a base-colour pass first (whole silhouette, alpha 1) so no texel inside the silhouette is empty or black; feather 2 px instead of 1; side views limited by a `clip` to the flat side wall (|x| > 0.3615 m), which removed the yellow slivers beside the CRT bezel and the doubled left rail (the recess walls and bevel strips had been taking the side reference's yellow trim). `auto_align` was tried and dropped (it needs a mesh texture to correlate against). |
| 7 | Local repair (Modddif) | **FALLBACK (Desk nhxz-q3).** The named fallback, ChatGPT repaint + Blender, was not used and "TRIAL NEEDS CHATGPT" was never sent: no visible surface needed generating. Only scripted Blender/projection fixes ran. Nothing here was made by an image generator. |
| 8 | PBR finish (ArmorPaint) | **FALLBACK (Desk nhxz-q3), partly failed.** **Ucupaint 3.0.0 could not be driven headless.** Two scripted attempts failed (`scripts/ucupaint_layers.py`: first `space.id` was None, then `poll() failed, context is incorrect`; its layer operators need a Shader Editor with an edit tree). So **there is no Ucupaint layer file and no `distress_AUTHOR` layer.** A **scripted Blender stand-in** made the maps instead: a Cycles AO bake, roughness and metallic projected through the same SAM cameras from per-zone value images, the sticker-relief normal, the emit reference. The ORM, base colour, emissive and normal islands are now dilated 8 texels outward, and roughness is clamped at 0.04 (seam texels had read 0.01 from the black fill; the range is now 0.08-0.85). |
| 9 | Review renders | DONE, `renders/`: Cycles CPU, fixed orthographic cameras fitted to the reference frame (front and right are reference-view matched at 290x740 and 383x740), fixed exposure, Standard view transform. Neutral (diffuse only: white world, no specular, no emission, so colour is comparable) and a game-light stand-in (warm key from the viewer's front-left, 40 degrees, cool dim sky, emission on). Views: front, right, back, left. The in-game rig is not part of this package; under this key the +X side and the back are in shadow. |
| 10 | SAM-assisted QA | DONE, two ways, tables below. |
| 11 | Correct and repeat | Five rounds in total, the last two after review: right rail and side-sticker halos (round 5), then this final pass. |
| 12 | Package | This folder. |

## Colour QA (neutral render vs reference, final)

dE = CIE76 between the median colours of the zone in the reference and in the render; "pixels dE<15" is the share of the zone's pixels under 15; detail ratio is render Laplacian variance over reference Laplacian variance (1.0 = as sharp as the approved art).

| Zone | dE | pixels dE<15 | detail | Verdict |
|---|---|---|---|---|
| marquee | 3.8 | 0.91 | 0.44 | colour pass, soft |
| marquee ink | 0.1 | 1.00 | 1.15 | pass |
| CRT bezel | 1.6 | 0.99 | 0.35 | colour pass, soft |
| CRT screen | 1.4 | 1.00 | 0.36 | colour pass, soft |
| screen invader | 1.9 | 0.98 | 0.32 | colour pass, soft |
| control panel | 5.1 | 0.99 | 0.40 | colour pass, soft |
| joystick | 3.4 | 0.96 | 0.36 | colour pass, soft |
| lower fascia | 0.1 | 1.00 | 0.70 | pass |
| coin door | 0.5 | 0.96 | 0.26 | colour pass, **soft** |
| kick panel stickers | 1.6 | 0.55 | 0.26 | **marginal, soft** (sticker edges shifted or blurred) |
| rail left | 0.9 | 0.99 | 1.01 | pass |
| rail right | 4.4 | 0.79 | 0.80 | pass |
| side body | 0.1 | 0.95 | 0.50 | pass |
| side stickers | 1.0 | 0.75 | 0.31 | colour pass, **soft** |
| side trim | 2.2 | 0.84 | 5.01 | pass (the high ratio is the trim line, not extra detail) |

Compared with the version the blind review saw, the colour numbers are the same or better (control panel 6.1 -> 5.1, marquee 5.2 -> 3.8, left rail 2.9 -> 0.9), but several detail ratios fell (control panel 2.39 -> 0.40, fascia 1.74 -> 0.70): the earlier higher values were partly the dark halo outlines, which added edge contrast that is not in the painting. The fix made the render cleaner and also exposed how soft the base texture is.

SAM-assisted comparison (the same prompts run on the neutral renders; mask IoU against the reference masks): marquee 0.98, bezel 0.99, screen 0.99, invader 0.95, deck 0.93 (2.5 px x shift), joystick 0.95, fascia 0.96, coin door 0.98, kick panel 0.97, rail left 0.93, rail right 0.80, side stickers 0.95, side body 0.94, marquee ink 0.84, **side trim 0.41** (SAM on the render finds a different part of the thin trim; a weak metric, the colour check on the trim passes). The earlier side-sticker IoU was 0.91, the left rail 0.82.

## UV and texture validation (`validation_report.json`, no Blender)

- 26,824 triangles, 2048 x 2048 atlas, UVs inside 0-1, no degenerate UV triangles, UV triangle area / covered area 0.995 (no real overlap), 69% coverage, **black texels in the base colour atlas: 0.006%** (it was 52% before the fill fix).
- Texel density median 718 px/m (592-739) against the reference's 400 px/m, about 1.8x oversampled: smart-project packing at 69% coverage would leave under 400 px/m at 1024 and 1024 would downsample the sticker detail; 2048 is the props cap in `3d_asset_rules.md`. No AI upscaling; pixels are the reference's, bilinearly sampled. This oversampling does not make the textures sharper than the source.
- ORM: AO mean 0.96 over covered texels (min 0.25 in the recess corners), roughness 0.08-0.85, metallic max 0.6 (coin door only, 1.5% of texels). Normal: flat except 2.3% sticker relief. Emissive: 3.1% of texels above 0.15 (marquee, screen, buttons).
- A unique-UV atlas, not a tiling material; not seamless-tileable by design.

## Open defects

1. **Softness** (above): the largest remaining gap to the approved art.
2. **Flat inferred surfaces** (back, underside, recess walls): no art and no wear; the author's hand pass or a new back reference is needed.
3. **Right rail** is the weakest zone left (0.79 of pixels under dE 15, SAM mask IoU 0.80): a thin curved rail on a straight box edge.
4. **-X flank** is a mirrored copy.
5. **Blind review not re-run**, SAM masks not blind-reviewed, PBR values assumed.

## Distress (hand-painted by the author)

Per `3d_asset_rules.md` the author paints all distress. Kept as the approved art's own pixels, nothing added: grime streaks on the front fascia, scuffs and cracks on the +X body (heaviest at the bottom), coin-door edge wear, rail chipping. No `distress_AUTHOR` Ucupaint layer exists (step 8 failure). The back, underside and mirrored -X flank have no distress reference at all.

## Tools and fallbacks, named

- Modddif: not used (Desk nhxz-q3). Fallback named: ChatGPT repaint + Blender; ChatGPT not used.
- ArmorPaint: not used (Desk nhxz-q3). Fallback named: Ucupaint in Blender, which failed headless; a scripted Blender stand-in produced the maps.
- Tripo: website texturing not used, API never touched, 0 credits. SAM 2.1 base-plus (SAM 3/3.1 is gated, see `tools/paint_zones/README.md`). Blender 5.2.3. No purchase, no sign-up, no payment dialog.

## Notes for the pipeline

- `project_ref.py` needs a mesh above 500 vertices; a dense even tessellation for its silhouette report; a lowered `ndot` per zone for slanted surfaces (deck 0.25, base pass 0.2); `clip` to keep the side views off recess walls and bevels; a base pass before the zone views; and it restarts from `<glb>_orig.glb`, so a changed input mesh needs a fresh work folder or the stale copy wins.
- A generated Blender image must be filled with display values (`generated_color = hex/255`), not `c**2.2`; `Image.pixels` of 8-bit images are display-encoded, not linear.
- The raw Tripo geometry was not usable for this hard-surface prop; the measuring-stick rebuild is. The mesh is a silhouette extrusion with two relief features (gray-clay stage), not a full architectural rebuild.

## Paths

Every path in the committed reports and scripts is relative to the package folder or the repo root. Machine-specific locations (the shared SAM work folder, the shared tool venv, Blender) are read from the `PAINT_ZONES_WORK` environment variable or the command line; `scripts/scrub_paths.py` rewrites absolute paths in the projection reports. Squash-merge note: the earlier commits of this branch held absolute paths; only the final tree is meant to land.

## Package contents (`Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet/`)

Committed (text): `quality_report.md`, `material_manifest.json`, `source_references.json`, `validation_report.json`, `qa_color_compare.json`, `qa_sam_compare.json`, `projection_report_*.json`, `masks/*_segment.json`, `sam_overlays/*_legend.txt`, `scripts/` (re-runnable scripts and zone JSON). Before/after sheet `dev/asset_team/reviews/protocol_trial_cabinet_before_after.jpg` (committed).

**On disk, gitignored** (`.gitignore`: `*.glb`, `Assets/Graphics/worlds/**/*.png|jpg`; no Git LFS; author ruling 2026-10-27): `mesh/street_cabinet_trial.glb` (final), `mesh/street_cabinet_rebuilt.glb` (geometry, fill only), `mesh/arcade_cabinet_tripo_raw.glb` (copy of the raw mesh, 77 MB), `pbr/cabinet_{basecolor,orm,normal,emissive}.png`, `source_references/*.png`, `masks/*.png`, `crops/*.png`, `sam_overlays/*.jpg`, `renders/*.png`. Copied to the main checkout at the same path so they survive the worktree's removal.
