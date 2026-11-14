# QA review: chadwick, round 1

**OUTCOME: APPROVED-PENDING-MANUAL**

The colour pass alone cannot approve. Tick every manual check below before marking APPROVED.

## Notes
- Colour delta is only meaningful where the render lighting matches the reference (protocol step 10). Reference lighting: painted reference (lighting baked into the art). Render lighting compared: game (G3 idle_S).
- No neutral-lighting render was supplied; neutral vs reference was not compared.
- Thresholds are PROVISIONAL pending real trials: pass <= 10.0, warn <= 20.0, fail above (CIEDE2000 on the median).

Reference contact sheet: `C:\Users\heirr\Desktop\Hope2_Studio\Eurobound\Tools\paint_zones\work\chadwick\segment_sheet.jpg`

## Render `Assets/Graphics/characters3d/chadwick/g3/idle_S.png` (lighting: game (G3 idle_S))

Contact sheet: `C:\Users\heirr\Desktop\Hope2_Studio\Eurobound\Tools\paint_zones\work\chadwick_qa_g3_idle_S\segment_sheet.jpg`

| zone | ref median | render median | dE00 | verdict | issue |
|---|---|---|---|---|---|
| cap_crown | #5A4D58 | #7F4C5E | 12.45 | warn | median colour off by dE00 12.45 (thresholds provisional) |
| face_skin | #B9704F | #B57051 | 0.98 | pass |  |
| polo | #DA5D50 | #D8584C | 1.27 | pass |  |
| jeans | #617284 | #617384 | 0.83 | pass |  |
| shoes | #C6B9B1 | #C2B8B1 | 1.36 | pass |  |

## Manual checks (reviewer ticks)
- [ ] UV and texture validation (seams, stretching, texel density, no baked lighting in base colour)
- [ ] PBR behaviour (base colour, roughness, metallic, normal, AO checked independently)
- [ ] Acceptable look at intended in-game scale (view the game-size render)
- [ ] Surface character, markings and lettering, finish, texture scale, boundaries (not covered by colour delta)
- [ ] Silhouette and painterly style preserved (no generic photoreal substitute; no unjustified upscaling)
- [ ] Observed vs invented details labelled in the material manifest

## Unavailable / fallback
- Step 9 (render): not run by this script; renders were supplied by the caller. Fixed camera/exposure/colour management is the caller's responsibility.
- Step 10 (surface character, markings, texture scale, finish, boundaries, seams): not automated; fallback is the manual checklist below. Only the colour comparison ran.
- Step 11 (correction loop): not run; this report only supplies the failing zones.
- Step 12 (final asset package / quality report): not assembled by this script.
