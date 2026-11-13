# Audit: Bottoms Down (shamsterdam)

**Files read** (under design/worlds/shamsterdam/; searched by stem `bottoms_down` and id `shamsterdam_oldtown_bottoms_down_01`):
1. Main md: bottoms_down.md (whole)
2. core/: MISSING
3. environment/: MISSING
4. interactions/: MISSING
5. items/: MISSING (item docs live in design/items/brewery_tour/: stamp_bottoms_down_item.md read)
6. location_nodes/: MISSING
7. npcs/bottoms_down/npc_kees.md (appearance, sprite notes)
8. PNG_Assets/bottoms_down_png_assets.md (palette, sheets 1-3); sprite_mapping/: MISSING; events/: no match
Also: dev/asset_team/reviews/bottoms_down_ext_review.jpg and _int_review.jpg. Kees's apron (amber #FFBF00 ground into #806517) matches the palette, so the palette is binding at prop level too. The only extra grep hits (bike crossing JSON) mention other venues. The new files change neither verdict nor plan.

## Q1, how well does it represent the location? Score 2/5
The file's exterior is "narrow alley, low door everyone hits their head, no signage, faded gold lettering, brass plaque 'Proudly Confusing Tourists Since Then'". The plate is a tidy, sunlit, well-kept brick gabled house between two handsome neighbours, with a polished wooden sign reading "Bottoms Down" and a neat plaque. It is the same stepped gable, brick facade, flanking trees and cobbles as the other Shamsterdam plates. Nothing says jenever, bowing, or "dignity destruction zone". The interior is much closer: long low room, oak bar, bottle wall, barrel tables, candles, sawdust.

## Q2, does it lean into the design requirements? Score 3/5
Palette: Jenever Amber #FFBF00 and Sawdust Tan #D2B48C show in the interior (amber light, tan floor). The exterior is red brick and green; amber and Oak Brown barely appear. Missing or weak: overfilled glasses with visible meniscus on the bar (the doc's central gag), brass foot rail, the "Traditional Drinking Method" illustration, newspaper clippings of horizontal patrons, spills, the sense of a hazardous low ceiling. It reads as a handsome historic pub, the "respectable" outcome the author rejected. The satire (the room is prepared for your failure) is not visible.

## Verdict: REDO (exterior; interior needs a pass for the glass gag)
The exterior is a respectable stepped-gable canal-town plate. The interior is good but over-polished and lacks the doc's jokes.

## Redo plan
- **Hook:** A 400-year-old dive that has never needed a sign; the room was built to catch you when you fall (Theme & Vibe).
- **Palette:** Jenever Amber #FFBF00 (lit glass, window glow, lettering), Oak Brown #806517 (door, beams, bar), Candlelit Cream #FFF8DC (light pools), Sawdust Tan #D2B48C (spill on the cobbles, step), Brass Warm #B5892E (plaque), Old Room Shadow #2B2116 (walls, low ceiling).
- **Exterior:** Squat, sagging, crooked 1624 house wedged in a dark alley, door absurdly low and head-scarred, lintel dented, sawdust drifting onto the cobbles, spilled amber on the step, brass plaque only. Not a stepped gable.
- **Interior:** Keep the layout. Add overfilled tulip glasses bulging past the brim, spills, sawdust drifts, the brass foot rail, the diagram on the wall, one lone chair, beams hanging low.
- **Satire beats made visible:** (1) sawdust on the floor "for a REASON" (The Sawdust); (2) glasses too full to lift (The Bar, The Catch); (3) low door and beams, "everyone hits their head" (Exterior); (4) newspaper clippings "all look the same: horizontal" (Decorative Elements).
- **Not in the file, needs approval:** May a horizontal patron lie outside the door as set dressing? Does the exterior get any sign beyond the faded lettering?
