# Audit: The Stoutworks Brewery (publandia)

## Files read
1. Main: design/worlds/publandia/the_stoutworks_brewery.md (whole)
2. core/: MISSING (no stoutworks file; only cloverleaf, paddys_premium_motors exist)
3. environment/: MISSING
4. interactions/: MISSING
5. items/: MISSING. Brewery-tour items read: design/items/brewery_tour/opener_stoutworks_brewery_item.md (beer_ and stamp_ items are covered by the main file's sections)
6. location_nodes/: MISSING
7. npcs/: design/worlds/publandia/npcs/The_Stoutworks_Brewery/npc_turlough_osullivan.md (the folder's only file)
8. PNG_Assets/: design/worlds/publandia/PNG_Assets/The_Stoutworks_Brewery_PNG_Assets.md (read through sheet 4)
9. sprite_mapping/: MISSING. events/: MISSING.
- Images: dev/asset_team/reviews/the_stoutworks_brewery_ext_review.jpg, opener_stoutworks_brewery_review.png. No interior plates exist.
- Not read in full: Quests/Publandia/brewerytourpublandia.md and passport docs (name hits only).

## Q1. How well does it represent the location? 3/5
Matches the literal text: Victorian red brick, copper dome, tall chimney, steam, "THE STOUTWORKS" copper lettering and the Est. 1869 plaque, "BREWERY EXPERIENCE" office, "Staff Only" door, conveyor walkway to smaller facilities, barrels on the cobbles (l.31-41). Missing the premise: this is a "cathedral of beer production" gone wrong, with a sentient yeast "situation". There is no "Temporary Closure Due to 'Maintenance Issues'" notice, no foam, no leaking yeast, no hazard lights, no sign anything is off. No interior is built at all (six floors, gift shop, tasting room).

## Q2. How well does it lean into the design requirements? 2/5
Palette: copper #B87333 and brick #8B4513 dominate, so the base colours are right. Yeast Cream #F0E68C and Hazard Amber #FF8C00 (warning lights, meltdown) are not visible; Steam White is only a few chimney puffs. Satire: reads as a handsome, tasteful heritage brewery postcard. "Cathedral of beer... religious experience" (l.115) is not pushed (no pews, stained glass vats, pilgrim queue, gift-shop shrine). A respectable building: boring.

The PNG spec supplies visual gags the plate ignores: a handwritten "IN CASE OF YEAST: RUN" sign, a derailment marker of a dropped lanyard and a single shoe, tour rope barriers, a fermentation window with a shape pressing the glass, a vat porthole where "something looks back", and a pipe-organ array making the cathedral literal. Only the main file and spec define it, as the six JSON sub-folders have no Stoutworks entry.

## Verdict: REDO (exterior and interior)
Both scores are below 4. The interior does not exist yet and must be built to this standard.

## Redo plan
- **Hook**: Beer tour as religious experience, where the yeast took "living culture" literally (l.115).
- **Palette**: #B87333 copper domes and pipes; #8B4513 brick; #1A1A1A vats; #F5F5F5 steam; #F0E68C foam spilling from windows; #FF8C00 hazard beacons.
- **Exterior**: Brewery built as a cathedral (vat-shaped rose window, copper spire still), pilgrim queue barrier, foam oozing from the Staff Only door, a hand-lettered "Temporary Closure Due to 'Maintenance Issues'" sign (l.39) over a still-lit gift shop; yeast-cream drips down the brick.
- **Interior**: Floors 1-6 per l.45-81: Welcome Center with gift shop, malt house, mash tuns, fermentation halls (foam, CO2), barrel rooms, copper cathedral. Open floor, warm copper light, amber alarms.
- **Satire beats made visible**: gift shop open through the apocalypse (l.276); tour office "Book Your Journey" (l.37); "Est. 1869... grandfather's grandfather" (l.36); "Staff Only (ignored)" (l.38); tasting-room view into ominous fermentation halls (l.464); "IN CASE OF YEAST: RUN" handwritten sign, lone shoe and lanyard (PNG spec sheet 3); vat porthole where something looks back (sheet 4).
- **Not in the file, needs approval**: Does the exterior show the yeast situation already, or only the closure sign? Real-brand parody is only a planning note (l.130); no real name may appear in the art.
