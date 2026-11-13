# Audit: Astronomical Cock-Up Square (debaucheryville)

## Files read
1. Main: design/worlds/debaucheryville/astronomical_cockup_square.md (whole)
2. core/: design/worlds/debaucheryville/core/astronomical_cockup_square_core.json (palette, key visuals "tourist_crowd", "graffiti_on_unesco_sign")
3. environment/: design/worlds/debaucheryville/environment/astronomical_cockup_square_environment.json
4. interactions/: design/worlds/debaucheryville/interactions/astronomical_cockup_square_interactions.json
5. items/: design/worlds/debaucheryville/items/astronomical_cockup_square_items.json
6. location_nodes/: design/worlds/debaucheryville/location_nodes/astronomical_cockup_square_location_nodes.json
7. npcs/: design/worlds/debaucheryville/npcs/Astronomical_Cockup_Square/ (ambient, clock wine, merchandise, mysterious local, party monk, tattoo barker, viewing spot, wristband guy, clock_scam_vendors.md, npcs.json; appearance sections only)
8. PNG_Assets/: design/worlds/debaucheryville/PNG_Assets/Astronomical_Cockup_Square_Complete_PNG_Asset_Requirements.md
9. sprite_mapping/: design/worlds/debaucheryville/sprite_mapping/astronomical_cockup_square_sprite_mapping.json (listed)
- events/: MISSING (no match). Also read: design/worlds/debaucheryville/maps/debaucheryville_district_diagram_proposal.md, design/Quests/debaucheryville/astronomical_cockup.md (first 60 lines).
- Image: dev/asset_team/reviews/astronomical_cockup_square_ext_review.jpg. The plates folder named in the task (gilded_square_astronomical_cockup_square/) does not exist; the square's plates are in game/assets/worlds/debaucheryville/astronomical_cockup_square/. Outdoor square: no interior.

## Q1. How well does it represent the location? 3/5
Present: the Gothic tower and blue-gold astronomical dial, skeleton, rooster, the "BEST VIEW 10 SOVS" pillar, the crossed-out heritage sign with "Astronomical Cock-Up" tag (l.72), the monk's velvet rope and rug with "BLESSINGS 20 SOVS" card, the green-backlit "AUTHENTIC CLOCK WINE" cart, souvenir stall, pink "EURO INK 4 LESS" neon. Missing: the doc's whole premise is a square of "50-200 tourists, all necks craned, phones, flash photography" (l.69) and a "coordinated scam ecosystem". The plate is an empty, serene, sunlit square. Wristband guy, merch plates and snow globes, folding tables, the "Holiday Inn" bathrobe, confetti, pigeons, the DMV-queue apostles are not readable. It looks like a heritage-site postcard where the scammers have wandered in.

## Q2. How well does it lean into the design requirements? 3/5
Palette: Stone Gray #708090 and Gothic Gold #CFB53B dominate correctly; Sky Blue and Cobblestone Brown are present. Scam Green #7FFF00 is only a small cart glow and Monk Purple #4B0082 is absent. Satire: the signs carry the joke, the architecture does not. Nothing says "tourist trap", it says "sincere Gothic square" (PNG spec l.27 says the square is sincere, but "overwhelmed by tourist density, scam stalls and phone flashes"). A tidy, respectable streetscape with tiny scam props. Boring by the author's standard.

The location_nodes file states the brief outright: "packed square... hundreds of tourists... phones raised... suspicious figures in long coats... smell of incense, cheap wine, and tourist desperation", plus hidden birthday-party easter egg. Core.json asks for "gothic_baroque_tourist_trap"; the plate is Gothic and nothing else. Environment JSON adds confetti in gold, gray and #7FFF00, violet incense smoke and flash bursts, none painted.

## Verdict: REDO (exterior; no interior exists)
Scores are 3 and 3, and it is not over the top.

## Redo plan
- **Hook**: A sincere 600-year-old clock drowned by a coordinated scam ring (l.128, l.525).
- **Palette**: Keep #708090 and #CFB53B on the tower; make #7FFF00 (wine cart, bottles) and #4B0082 (monk robes, banners) loud accents; #8B7355 ground; night #FFBF00 and #FF1493.
- **Exterior**: Same tower and exit layout (the exits sketch holds). Add a vendor ring: handwritten cardboard "BLESSINGS 20 SOVS", "AUTHENTIC CLOCK WINE" banners, folding tables stacked with plates, shirts and snow globes, a pillar with a ridiculous queue rope, camera-flash clutter at the crowd edge, crowd sprites kept as a separate layer.
- **Interior**: None.
- **Satire beats made visible**: crossed-out UNESCO sign (l.72); 10 SOVS viewing pillar (l.73, l.283); bathrobe monk with rope belt and sandals-with-socks (l.289); identical "vintage" bottle labels (l.164); "TATTOOS - CHEAP - FAST - REGRET FREE" sign (l.91).
- **Not in the file, needs approval**: Can crowd sprites be painted into the plate, or must they stay separate (no-people rule)? Does the birthday-party poster easter egg (l.516) appear?
