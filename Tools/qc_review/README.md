# Tools/qc_review: SAM-assisted QA review for 3D assets

Implements steps 9-11 (the comparison part) of `design/style_guides/reference_locked_texturing_protocol.md`, for the QC section "Reference-locked review for every 3D asset" in `dev/asset_team/QC.md`. Bead Eurobound-nhxz.8.

## What it does

1. Runs SAM (`tools/paint_zones/segment_ref.py`) on the approved reference, then on each review render, strictly one at a time (about 2 GB VRAM, about 30 s each).
2. Compares the zones named in each render zone file with the same-named reference zone: median, shadow and light colour, CIEDE2000 in Lab (numpy only).
3. Writes `reports/<id>_qa_round<n>.json` and `.md` (override with `--out`).

Verdict per zone, on the median colour (PROVISIONAL thresholds, constants `PASS_MAX` / `WARN_MAX` in `review_3d.py`, pending real trials):

| dE00 | verdict |
|---|---|
| <= 10 | pass |
| 10 to 20 | warn |
| > 20, or missing/empty mask | fail (with reason) |

Shadow and light dE are reported, and noted in the issue only when above 20 (info; they depend on lighting). They do not change the verdict.

**Outcome:** `BLOCKED` (input missing or SAM failed; exit code 2), `REVISION REQUIRED` (any zone fails), otherwise `APPROVED-PENDING-MANUAL`. The script never says APPROVED: the protocol also needs UV/texture validation, PBR behaviour and a game-scale look, so the report lists them as manual checks for the reviewer to tick. It also lists the protocol steps it did not run as "unavailable/fallback".

**Lighting caveat (protocol step 10):** colour delta only means something where render lighting matches the reference. Label each render with `--lighting` (`neutral`, `game`, ...); the report records which lighting was compared against the reference and warns if no neutral render was given.

## Usage

Run from the repo root (the zone files' image paths are relative to it; `tools/paint_zones` and its venv must exist there):

```
tools/paint_zones/.venv/Scripts/python Tools/qc_review/review_3d.py chadwick \
  --ref-zones tools/paint_zones/zones/chadwick_ref.json \
  --render Tools/qc_review/zones/chadwick_g3_idle_S_render.json --lighting "game (G3 idle_S)" \
  --round 1 --sheet
```

- `--render` and `--lighting` repeat, matched by order. `--reference-lighting` labels the reference's lighting.
- Each render needs its own zone file: same zone names as the reference file, boxes in render coordinates, and a **distinct `asset_id`** (SAM writes to `work/<asset_id>/`, so reusing the reference id would overwrite it). Always give a box. Only the zones named in the render file are compared; the zones of the reference not listed are not reviewed.
- A zone is compared as it was prompted: the reference zones use `minus` and `neg` to exclude neighbours, so mirror those in the render file or the medians will differ for that reason (e.g. the worked example's `cap_crown` includes the patch and cap front in the render and so warns).
- Never reinstall the paint_zones venv; torch and sam2 are already in it.

## Tests

`tools/paint_zones/.venv/Scripts/python Tools/qc_review/test_review_3d.py` (plain asserts, no pytest in that venv): CIEDE2000 against the published Sharma test pairs, verdict thresholds, empty/missing masks, outcome logic.

## Worked example

`reports/chadwick_qa_round1.md`: reference `chadwick_ref.json` against the G3 render `g3/idle_S.png`. This render is game lighting, not neutral, and the painted reference has baked lighting, so the numbers are indicative only.
