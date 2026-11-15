# Quality report: Protocol Trial 2, Absinthe Arcade street cabinet

Bead Eurobound-nhxz.9 (trial asset confirmed by the author, Desk Eurobound-nhxz-9-q1: "Yes, use the street cabinet"). Protocol: `design/style_guides/reference_locked_texturing_protocol.md`. Date 2026-11-14. Producer: technical artist (asset team). This is the final version after the blind nhxz.8 review (REVISION REQUIRED) and the last step-11 pass.

## Phase B revision (2026-11-14, after the author's Desk rulings)

Author rulings (Desk): "Fix the softness and the hidden sides, then show me again" (ArmorPaint not approved); the new other-side art "Approve it: go to Phase B". This section replaces the statements below that it contradicts; the first-pass text is kept for the record. **Status: ready for the nhxz.8 reference-locked review. Not self-approved.**

### B2: mechanical fixes after the blind nhxz.8 review (REVISION REQUIRED), 2026-11-14

Everything below supersedes the matching Phase B numbers and settings further down. The judgement calls (the -X layout, the 3072 atlas, the steel trim colour) are left to the author.

**Deviations from the approved references or rules, stated explicitly**

| # | Deviation | Why | Where it shows |
|---|---|---|---|
| D1 | **The -X flank is MIRRORED, not as drawn.** The approved other-side art was drawn in the +X view's orientation. Viewed from -X the cabinet's front is on the other side, so Phase B re-made the art with the silhouette AND the whole sticker cluster mirrored (`make_other_side_r3.py`, `CABINET_MIRROR=1`). The cluster's layout on the model is therefore the mirror image of the layout in the approved drawing. The lettering sticker is NOT mirrored (it reads correctly), so it is re-stamped at the mirrored position, tilted the other way. | A flat drawing cannot be seen from both sides without flipping. | `renders/cabinet_*_left.png`. **Option B** (new in B2): the cluster placed AS DRAWN inside the mirrored silhouette, lettering readable (`source_references/aa_prop_cabinet_side_other_alt_*`, `renders/cabinet_altB_*_left.png`, `cabinet_hi_altB_game_left.png`). Option A is what the package textures use; B exists for the author to choose. Both are side by side in the before/after sheet. B's atlas was built the same way but only its left render is kept. |
| D2 | Atlas 3072 x 3072, above the 2K props cap in `3d_asset_rules.md`. | Sharpness was asked for. | Needs an author ruling to stay. |
| D3 | The coin-door **metal trim albedo is lifted to dark steel** (slot-bezel rings, locks, hinges, coin-return frame; derived from the reference's own shading: 25 % reference, 75 % steel 190/192/198 scaled by the reference luminance). The door body stays black, as in the reference. | A metal reflects only what is around it; with the reference's near-black trim colour the metal read as nothing. | `renders/cabinet_hi_game_front.png`. In the neutral render (diffuse only) the trim is darker than the reference; `qa_color_compare.json` coin door 0.99 -> 0.92 of pixels under dE 15 reflects that. |
| D4 | The **game-light stand-in rig gained dielectric specular 0.2, sun specular 0.15 and a specular-only softbox** in front of the cabinet (area light, diffuse factor 0, 25 W, 1.6 x 1.0 m, 2.2 m in front, 0.45 m above the centre). Earlier game renders had none. | Polished metal needs something bright to reflect. It is not the in-game rig. | `render_lit.py` (`CAB_SOFTBOX` env overrides the power). The game renders are not part of the colour QA. |
| D5 | The references are enlarged 3x with Lanczos before sampling and sharpened in-mask (not AI upscaling, no invented detail). | Sharpness. | `prep_projection_b.py`. |
| D6 | The back, underside, recess walls and bevel strips are invented grime (inferred). | No reference shows them. | `renders/cabinet_*_back.png`, `cabinet_*_bottom.png`. |

**What B2 changed**

| Item | Fix | Result |
|---|---|---|
| Halos / crunch | Unsharp radius 2.4 -> **1.6 px** (enlarged space), percent now **30-70** (coin door 70, kick-panel and +X stickers 70, -X flank 60, control panel 55, marquee 60, rest 30-50, was up to 140), a **detail threshold** (luma 0.03 ramping to 0.09: flat areas are untouched) and a **local min/max clamp** (radius 2: the result can never overshoot the neighbouring pixels, so no dark or bright fringes). New `project_ref.py` keys `sharpen_thr` and `sharpen_clamp`. | `renders/cabinet_hi_game_left.png` lettering sticker and rim are clean at 100 %. Detail ratio is now 0.65-1.2 against the reference (was 1.2-1.8); halo-free was chosen over a high ratio. |
| Underside / back grime | Generated per texel at the full 3072 atlas resolution: fine grain at about 150 and 330 cells/m, hairline scratches of constant width (noise iso-lines divided by the local gradient), dark pits, much less rust and oil than Phase B (the first underside was a soft rusty blotch pattern), so it reads like the +X body (dark charcoal, grain, scratches). Back base value lifted about 28 % so the wear reads in game light; still dark. | `renders/cabinet_neutral_bottom.png`, `cabinet_game_back.png`. All inferred. |
| Back wedge (around y = 385) | **NOT FIXED, only investigated.** A texel dump of the triangles around it (z 0.85-0.95 m, x below -0.28 m, back-facing) shows dark grime texels (base colour 0.07-0.19, roughness 0.85, metallic 0, flat normal), so it is not a texture fault in the inferred fill. It is a lit face of the back shoulder shelf seen edge-on, with a shadow terminator from the tall front body giving the wedge shape. It stays in `cabinet_neutral_back.png` as a small bright notch at the right edge. Tried without effect on the wedge: up-facing texels made 80 % darker, game-rig dielectric specular 0.2, sun specular 0.15. Remaining suspect, untested: the faces at the -X end of the shelf pick up the yellow rim of the -X art through the `left_all` pass (their texels sit at x between -0.3615 and -0.3625 m). Filed for follow-up rather than guessed at. | `cabinet_game_back.png` (still visible, smaller and dimmer than in Phase B). |
| Metal | Door body stays black matte. The **trim** is its own zone (hand-placed from the reference: four slot bezel rings, two locks, two hinge strips, the coin-return frame ring) with **metallic 1.0, roughness 0.28** (assumed, not measured) and a height value so the edges get a relief normal. Value range stays sane: roughness 0.08-0.85, metallic 1.0 on 0.23 % of texels. | In `cabinet_hi_game_front.png` the trim reads brighter than the door body and the bezel edges and hinges catch light (measured at 740 px, trim luminance p90 143 / p99 205 against the door body p90 86 / p99 119). |

**Colour QA after B2** (neutral render vs reference; "detail" is render over reference Laplacian variance, 1.0 = as sharp as the approved art):

| Zone | dE | pixels dE<15 | detail |
|---|---|---|---|
| marquee | 1.1 | 0.98 | 0.84 |
| marquee ink | 0.3 | 1.00 | 1.95 |
| CRT bezel | 1.6 | 1.00 | 0.66 |
| CRT screen | 1.4 | 1.00 | 0.68 |
| screen invader | 1.9 | 1.00 | 0.65 |
| control panel | 5.3 | 1.00 | 0.77 |
| joystick | 3.2 | 1.00 | 0.69 |
| lower fascia | 0.1 | 1.00 | 0.85 |
| coin door | 0.4 | 0.92 (metal trim is dark in the diffuse-only render) | 0.74 |
| kick panel stickers | 1.2 | 0.81 | 0.65 |
| rail left | 0.5 | 0.99 | 1.16 |
| rail right | 1.3 | 0.89 | 1.18 |
| side body | 0.1 | 0.99 | 0.90 |
| side stickers | 0.3 | 0.97 | 0.85 |
| side trim | 1.1 | 0.98 | 11.69 (the trim line) |

**SAM compare (`qa_sam_compare.json`): STALE.** It was not re-run (SAM needs the model and a long GPU/CPU job; the zones and cameras did not change, but the textures did). Treat the file as the first pass's. The -X flank has no zone comparison.

**Process note.** `build_cabinet.py` is not bit-deterministic (18315 / 18319 / 18333 vertices on different runs), so all three projection GLBs and both -X options come from ONE build. `assemble_pbr.py` needs absolute output paths (relative ones silently wrote nothing). The blind-review gate has not seen B2.

### Phase B first numbers (superseded where B2 above differs)

#### What changed

| Fix | What was done | Result |
|---|---|---|
| Softness | Three causes found in the first pass and removed: (1) the projection tool wrote the atlas as **JPEG q92**; it now takes `"lossless": true` and writes PNG (small edit to `tools/char3d/project_ref.py`, plus a clamp for masks touching the image edge); (2) the 400 px/m references were sampled 1:1 into 2048 texels; they are now enlarged **3x with Lanczos (no AI)** before sampling, masks 3x with bilinear + threshold, bilinear sampling; (3) no sharpening; an **unsharp mask inside each zone mask only** (`sharpen` [radius px, percent]): coin door 140 %, kick-panel and +X stickers 130 %, -X flank 110 %, control panel 80 %, marquee 90 %, other zones 45-70 %. Atlas **3072 x 3072** (was 2048). | Edge-detail ratio render/reference went from 0.26-0.50 to 1.23-1.76 on every zone below (table). **Caution:** a ratio above 1.0 is the unsharp mask at work, not extra information; the zone with the strongest setting (coin door 1.76, stickers 1.69) is the one to eyeball for ringing. |
| -X flank | The new author-approved art (`source_references/aa_prop_cabinet_side_other_*`, round 3: Firefly painterly cluster, ONE Pillow lettering sticker "XXX PAC-MAN: The Director's Cut", doc cite `design/worlds/debaucheryville/clawmachinemaintenanceclosetrestroom.md` line 30) is projected onto -X, replacing the mirror of the +X side. The art was re-made **as seen from -X** (`make_other_side_r3.py` with `CABINET_MIRROR=1`: silhouette and cluster mirrored, lettering NOT mirrored) so the lettering reads correctly on the model. | Seen in `renders/cabinet_*_left.png`; every letter read. Status: **directly observed (the approved art)**, projected on a reliable camera (IoU 0.987). The sticker mask used for the -X relief map is derived from the art (assumed). |
| Back, underside, recess walls, bevel strips | **Flat grime painted in the style of the +X body**, in 3D position space (`scripts/grime_fill.py`): mottled #231C24 paint, soft vertical drips, rust creeping up from the foot (worst underneath), dark oily pools, light scuffs, edge chips (distance to a box edge), six peeled-sticker residue ghosts on the back. Colour only, no relief. | **INFERRED: no reference shows these faces.** The projection passes overwrite it wherever a reference exists. Seen in `renders/cabinet_neutral_back.png` and the new `cabinet_neutral_bottom.png` / `cabinet_game_bottom.png`. The back in game light is almost black (it faces away from the key light). |
| Metal | Coin door value map: **metallic 0.85, roughness 0.38** (was 0.6 / 0.45). All other values unchanged (matte paint 0.75-0.85, plastic 0.3-0.55, CRT glass 0.08). | **ASSUMED, not measured, not physically validated**, kept in a sane range (roughness 0.08-0.85, metallic max 0.85 on 1.5 % of texels, coin door only). The neutral render is diffuse-only by design, so metal can only be judged in the game-light render. |

### Colour QA after Phase B (neutral render vs reference; same method as below)

| Zone | dE | pixels dE<15 | detail (was) |
|---|---|---|---|
| marquee | 1.7 | 0.96 | 1.32 (0.44) |
| marquee ink | 0.5 | 1.00 | 5.88 (1.15) |
| CRT bezel | 1.5 | 1.00 | 1.28 (0.35) |
| CRT screen | 1.4 | 1.00 | 1.30 (0.36) |
| screen invader | 1.6 | 1.00 | 1.26 (0.32) |
| control panel | 5.1 | 1.00 | 1.59 (0.40) |
| joystick | 3.8 | 1.00 | 1.23 (0.36) |
| lower fascia | 0.1 | 1.00 | 1.36 (0.70) |
| coin door | 0.4 | 0.99 | 1.76 (0.26) |
| kick panel stickers | 1.7 | 0.70 | 1.27 (0.26) |
| rail left | 0.2 | 0.99 | 1.57 (1.01) |
| rail right | 0.4 | 0.90 | 1.40 (0.80) |
| side body | 0.0 | 0.98 | 1.27 (0.50) |
| side stickers | 1.9 | 0.87 | 1.69 (0.31) |
| side trim | 0.8 | 0.98 | 13.73 (5.01; the trim line, not extra detail) |

Colour is as good as or better than the first pass everywhere (kick panel 0.55 -> 0.70, +X stickers 0.75 -> 0.87, right rail 0.79 -> 0.90 of pixels under dE 15). The **-X flank has no reference comparison** (the new art has no SAM zones); it was checked by eye against the approved art (`dev/asset_team/reviews/cabinet_other_side_art.jpg`, side-by-side in the before/after sheet). **The SAM-assisted IoU check (`qa_sam_compare.json`) was NOT re-run** for this pass (it needs the SAM model); that file is the first pass's and is stale. SAM masks are still not blind-reviewed.

### Validation after Phase B (`validation_report.json`)

3072 atlas, 26,824 triangles, UVs inside 0-1, no degenerate UV triangles, UV area / covered area 0.996, 69 % coverage, texel density median **1076 px/m** (887-1109) against the reference's 400 px/m (2.7x oversampled; **3072 is above the 2K props cap in `3d_asset_rules.md`**, used because the author asked for a sharper texture; it needs a ruling if it is to stay), near-black texels 1.1 % of the atlas (dark art and dark grime, not an unfilled void), AO mean 0.96 over covered texels, roughness 0.08-0.85, metallic max 0.85, emissive 3.4 % of texels above 0.15. GLB about 12 MB.

### Still open after Phase B

1. Back, underside and walls are **invented grime** (flat colour, no relief): the author's hand pass or a reference is still the proper fix.
2. PBR values are assumed; the Ucupaint step still has no layer file (the step 8 fallback stands).
3. The unsharp mask can ring on very dark/bright edges (check the coin door and sticker rims at 100 %); drop the percent if the review calls it crunchy.
4. The emit and value (ORM) projection passes report "unreliable" silhouette IoU (0.66) on the side views because their black reference background counts as figure; they use the same camera as the day pass (IoU 0.98+), so this is a metric artefact, as in the first pass.
5. The blind nhxz.8 review has not seen this version; SAM masks not blind-reviewed.

### Phase B scripts

`scripts/make_other_side_r3.py` (art; `CABINET_MIRROR=1`), `scripts/prep_projection_b.py` (3x references and masks, sharpen settings, value maps incl. the metal door and the -X sticker mask), `scripts/grime_fill.py` (wear), `scripts/render_lit.py` (new `bottom` view), `scripts/validate_package.py` (atlas size read from the map; fast raster). Order: `build_cabinet.py` (3072, #231c24) -> `grime_fill.py` -> `prep_projection_b.py` -> `project_ref.py` x3 (day, emit, orm; `"lossless": true`) -> `assemble_pbr.py` (absolute output paths: relative ones silently wrote nothing) -> `render_lit.py` -> `qa_compare.py` -> `validate_package.py` -> `before_after_sheet.py`. Note: `build_cabinet.py` is not bit-deterministic (a rebuild gave 18315 instead of 18319 vertices), so all three projection GLBs must come from ONE build.

## First-pass outcome (kept for the record; where Phase B above differs, Phase B wins)

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
| -X flank | First pass: the +X reference mirrored. **Phase B: the new author-approved art, projected** (see above) | observed (the approved art) |
| Back face | First pass: flat #231C24. **Phase B: flat grime painted in the +X body style (inferred, see above)** | **inferred** |
| Underside, recess walls (CRT, coin door), bevel strips, mesh edge beyond the reference silhouette | First pass flat #231C24; **Phase B: inferred grime fill** | **inferred** |
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
