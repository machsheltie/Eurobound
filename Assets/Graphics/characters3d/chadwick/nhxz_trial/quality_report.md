# Chadwick: Reference-Locked Texturing trial, quality report

**Status: REVISION REQUIRED.** It is not approved: the blind reviewer preferred the original texture twice, and protocol step 11 says to stop after repeated failures. Date: 2026-11-14. Beads: Eurobound-nhxz.1, .2 and .6. Protocol: `design/style_guides/reference_locked_texturing_protocol.md`.

## Steps actually run

| Step | Done? | What and where |
|---|---|---|
| 1 Register reference | Yes | `tools/paint_zones/refs/registry.json`: chadwick_portrait_v3 (canonical, sha256), chadwick_tripo_src (derived, Tripo input only) |
| 2 SAM segmentation | Yes | SAM 2.1 hiera_base_plus, run locally. 20 zones on the portrait and 19 on the Tripo source (`work/chadwick*/`). The portrait masks passed a blind check (qc_log `chadwick_sam_masks_v1`). |
| 3 Material manifest | Yes | `tools/paint_zones/manifests/chadwick.json`: 20 materials with sampled colours and observed/inferred flags; the back is listed as unseen |
| 4 GPT Image studies | **Not run** | No zone needed a flat study for this test |
| 5 Mesh | Yes, existing | `chadwick_shared.glb` (Tripo website build plus shared skeleton); no new Tripo credits spent |
| 6 Projection | Yes | `tools/char3d/project_ref.py`, with each zone clipped to its SAM mask, auto-aligned per zone by phase correlation, and colour gains of at most 12% toward the canonical medians. **The canonical portrait could not be used as the camera:** its pose differs, so the silhouette IoU is 0.66, below the 0.85 floor. The derived Tripo source was used for geometry (IoU 0.893), with colour truth from the canonical manifest. The face, hair, goatee and cap patch were skipped because they are previously approved work (Desk `sprite-dev-chadwick-3d-face`). |
| 7 Local repair (Modddif) | **Fallback** | Modddif waits on Desk nhxz-q3. The fallback was `delight_px` 35 (divide out each zone's large-scale luminance) on the polo, collar and arms. |
| 8 PBR finish (ArmorPaint) | **Not run** | It waits on nhxz-q3. The game uses the toon look (`look.py`), base colour only, so no PBR maps were made or validated. |
| 9 Review renders | Yes | `render_chadwick_trial_base/` (before), `render_chadwick_zoned/` (v1), `render_zoned_v2/`, `render_zoned_v3/`: idle S/E/N with the same camera and light |
| 10 SAM-assisted QA | Yes | `tools/paint_zones/qa_compare.py` segments each render with SAM and gives ΔE per zone against the canonical manifest (`qa_colour.json`); a blind A/B review was also run |
| 11 Fix and repeat | Twice | v1 (no alignment) → v2 (auto-align) → v3 (plus delight). Both blind reviews failed (qc_log `chadwick_texture_ab`, `chadwick_texture_ab_v3`). |
| 12 Package | Partly | `chadwick_zoned.glb` (v3), `chadwick_zoned_v1.glb`, `chadwick_zoned_v2.glb`, the reports, colour_gains.json, this report. Not shipped: the game still uses `chadwick_shared.glb`. |

## What worked

- SAM zones are accurate once each prompt has a box. Straps over cloth need `keep_hsv`/`open_px`.
- Auto-alignment found the same offset a human had tuned (patch 15, -7) and removed the ghosting: the doubled sunglasses and doubled strap edge in v1.
- Small hard parts improved in the numbers. In v1, ΔE fell for the pager (61 → 12), sunglasses (17 → 1.3) and watch (11 → 5). In v3 it fell for the wristband (40 → 18) and wallet strap (3.1 → 1.1).

## What failed, precisely

1. **Painted lighting comes across with the pixels.** The source is a painting with a strong key light. Projecting it puts the folds, muscle shading and knee grime into the base colour. The fallback delight removes the broad shading but not the folds, and the blind reviewer still calls the result "baked in" and "grimy". Tripo's own texture had already been delit by Tripo, so it reads cleaner, even though it is blurrier.
2. **The canonical art can't be the camera for a character.** The approved portrait poses Chadwick (pointing, hand in pocket). Only the arms-down derived copy lines up with the mesh, so every projected pixel comes from an AI interpretation, not from the canon.
3. **The numbers are noisy on thin parts.** SAM on a render sometimes takes the neighbouring zone (sunglasses v3 at 47, belt 58-67 in every version), so ΔE on thin parts can't be relied on yet.

## What would fix it (the author's call)

- A real albedo step: either Tripo Studio's multiview texturing with "Remove Lighting" on the website (30 credits per 8K run, per the tool check), or the ruled fallback (author, nhxz-q3, 2026-11-14: "Neither for now: use the fallbacks"): step 7 = ChatGPT repaint of a flat-lit render, projected back, plus Blender fixes; step 8 = Ucupaint. Modddif and ArmorPaint are off for now; the author wants "a few" trial assets before deciding on ArmorPaint.
- Or keep the current hand-texturing rule and use SAM zones only for targeted fixes on small hard parts (pager, sunglasses, strap, watch, wristband, lettering), where projection measurably helped.
