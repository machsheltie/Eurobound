# Audit: Cyberspace Kavarna (cyberspace_kavarna), full 8-file review

## Files read
- design/worlds/debaucheryville/cyberspacekavarna.md (whole)
- core/cyberspace_kavarna_core.json
- environment/cyberspace_kavarna_environment.json
- interactions/cyberspace_kavarna_interactions.json
- items/cyberspace_kavarna_items.json
- location_nodes/cyberspace_kavarna_location_nodes.json
- npcs/Cyberspace_Kavarna/cyberspace_kavarna_npcs.json (plus npc_dmitri_the_router.md, npc_tony420.md openings)
- PNG_Assets/Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md
- sprite_mapping/cyberspace_kavarna_sprite_mapping.json
- events/: no match (MISSING). All 8 subfolder files exist.
- Also: docs/superpowers/specs/2026-11-02-cyberspace-kavarna-location-package-design.md; quests/icqscammersting (sting struck 2026-11-12)
- Plates: dev/asset_team/reviews/cyberspace_kavarna_ext_review.jpg, cyberspace_kavarna_int_review.jpg

## Q1, how well does it represent the location? 3/5
Unchanged. Doc and core.json say a basement den beneath Hostel Row (core zone; location_nodes ck_stair: "Narrow stair with flickering INTERNET/KAVARNA sign and warning placards"). The exterior plate is a tidy three-storey brick townhouse with shutters and flower boxes, not a stairwell between hostels. The interior is close in spirit, but the new files require seven named landmarks and the plate shows only the CRT maze and stairs.

## Q2, how well does it lean into the design requirements? 2/5 (was 3)
The JSONs widen the gap. Required but absent in the plates: Rental Desk with Dmitri (ck_rental_desk), Katka's Station, Restroom Graffiti Clue, and a hidden door under a flickering "404 Calories Not Found" sign (location_nodes ck_backroom_door); the interior door is plain and dark with no sign. The exterior has flower boxes where the doc wants smoke and desperation. The neon reads "KABAPHA" (mangled Cyrillic/Latin mix), a generated-text error. #DC143C and #696969 barely register. Terminals 7 and 13, Ethernet ivy, the CryptoDoner machine and the stretched Johnny Mnemonic poster (PNG md) are absent.

## Verdict: REDO (unchanged; exterior fully, interior second pass)
Both scores are under 4 and the new files add named nodes the plates lack.

## Redo plan
- **Hook:** "Your Data Is Not Safe. Cash Only." (core.json satirical_subtitle): a smoke-stained Y2K bunker of CRTs, Soviet furniture and duct-taped Ethernet.
- **Palette:** md l.52: #00FF41 dominant, #DC143C accent, #696969 ground; PNG md adds #E8E8D0 and #0000FF. core and environment JSON list only monitor green, nicotine beige, fluorescent white, error blue (see conflicts).
- **Exterior:** sunken stair pinched between plain hostel flanks, nothing like a townhouse. Huge flickering INTERNET neon (PNG effects: 160x48, off/on/flicker), spelled correctly, KAVARNA in Cyrillic beneath, the three warning signs, a smoke-belching vent, green glow on cobbles, wet-street response (environment.json weather_effects).
- **Interior:** keep the room, rebuild around the seven nodes in connection order: stair, rental desk (ancient register, "CASH ONLY" in several languages, multiple calculators), CRT maze, Katka's Station (black vinyl, headset, luminous makeup, npcs.json), restroom graffiti, hidden door under "404 Calories Not Found", exit. Stained concrete floor, Ethernet ivy, duct tape, ashtray piles, bootleg poster wall, red crypto rigs, Terminals 7 and 13 marked, more BSOD screens, fluorescent strips plus green glow.
- **Satire beats made visible:** warning signs (md l.31); posters (The Matrix photocopied to a green smudge, Johnny Mnemonic stretched sideways); crypto rig "Making Money" handwritten sign; doubled "Peak Tourist Hours" pricing; the silent patron at Tony420's rented chair (md l.145).
- **Conflicts, approval needed:** (1) md l.49 and l.160 hide a metro back exit; core.json exit ck_exit_backroom leads to Backroom Concessions behind the 404 door. Where does the door lead? (2) JSON palette drops the #DC143C and #696969 that md and PNG md require. (3) Dmitri is a "cable-wrapped cardigan" in npcs.json, a "faded Adidas tracksuit" in the PNG md. (4) PNG md calls him "the Operator", others "The Router".
- **Not in the file, needs approval:** hostel names on the flanking walls; how much stairwell shows below street level.
