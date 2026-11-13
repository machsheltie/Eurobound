# Audit: Ye Olde B.R.E.W. Lab

**Files read (all 8 subfolder files plus main md), under design/worlds/debaucheryville/:**
- ye_olde_brew_lab.md (whole)
- core/ye_olde_brew_lab_core.json
- environment/ye_olde_brew_lab_environment.json
- interactions/ye_olde_brew_lab_interactions.json
- items/ye_olde_brew_lab_items.json
- location_nodes/ye_olde_brew_lab_location_nodes.json
- npcs/Ye_Olde_BREW_Lab/ye_olde_brew_lab_npcs.json (the only file in that folder)
- PNG_Assets/Ye_Olde_BREW_Lab_Complete_PNG_Asset_Requirements.md (incl. legacy sheets 1-7)
- sprite_mapping/ye_olde_brew_lab_sprite_mapping.json
- events/: no match (MISSING)
- design/items/brewery_tour/{beer,opener,stamp}_ye_olde_brew_lab_item.md
- dev/asset_team/reviews/ye_olde_brew_lab_{ext,int}_review.jpg (re-viewed)

## Q1, how well does it represent the location? 4/5 (unchanged)
- Exterior hits the md: Staff Only rope, QR pad in the frame, neon-blue hologram sign, beer-tap surveillance camera, door humming in a red velvet club.
- Interior: green vats, console row, flavor holograms, posters, LED floor paths, bottle-warmer rigs, foam sculptures (hop, cube, thumbs-up). Faithful to the md, but the md calls for "venture capital and desperation" and the room is a clean showroom.

## Q2, interior and exterior requirements? 3/5 (unchanged)
Legacy sheet 1 gives a squalor list the plate skips:
- Missing: robotic bartender tap-dancing on ceiling rails with charging station and ERROR 404 glitch (headline prop, ybl_service); USB/ethernet duct-taped to vats and tanks; "DEFINITELY LEGITIMATE BREWING" router; temperature sensors showing errors; "DOGE TO THE MOON" sticker on mining rigs; four posters (only two painted; missing "Move Fast and Brew Things - Management (2019-2019)" and "The Only Failure Is Not Pivoting" with PIVOT over ICO); hex-code vat labels legible; stock-ticker buzzword cube (Fermenting Algorithm); L-shaped layout (plate is an open rectangle).
- Palette: md/PNG #F0F0F0, #00D4FF, #0A0A0A, #39FF14, plus #FF0000 critical red for gauges. core.json uses harsh blue, bioluminescent green, lab white, screen cyan. Plate follows these but has no red and little server black.
- Exterior: club red velvet is the parent's; the lab door itself is a plain grey steel door. Respectable, not grifter-built.

## Verdict: REDO interior (unchanged); exterior KEEP, with door dressing pushed
Faithful, not over the top.

## Redo plan
- **Hook:** failed ICO pivots to "AI-optimized craft brewing" (md Theme & Vibe); card text "Algorithm Verified".
- **Palette:** keep #F0F0F0, #00D4FF, #39FF14, #0A0A0A; add #FF0000 alert glows; clinical look visibly failing.
- **Exterior (ybl_stair door):** keep; add handwritten "B.R.E.W." tape sign, stuck QR pad, scorch or foam residue under the door.
- **Interior (L-shape, location_nodes):** ybl_vats left leg (duct-taped cables, hex-code labels, error sensors, DOGE-sticker rigs); ybl_consoles right leg (NFT flavor screens); ybl_taste station with pressure gauge; ybl_algorithm stock-ticker cube on LED paths; ybl_brewbot arena (white-chrome brewer with beer-printer arms); ybl_service rail bartender; ybl_selfie Algorithm Archive terminal with blockchain-hash screen; charging station.
- **NPC stations:** Robotic Bartender at ybl_service; lab technicians and screen avatars near brewbot, service, selfie (npcs.json, max 4 each).
- **Satire beats made visible:** duct-taped USB; four failed-startup posters; router label; "Management (2019-2019)"; holographic labels tracking crypto price; glitching bartender (md "Obvious signs").
- **Lighting:** cyan overhead LEDs, green vat glow, blue screens, white hologram flicker (md Lighting Setup); emission mask per sprite_mapping.

## Conflicts, approval questions
1. md: finish by taste-profile OR defeat BrewBot, with a self-destruct bypass and bartender stamp speech; interactions.json makes taste, then algorithm, then boss strictly sequential. Which governs?
2. md: Fermenting Algorithm only spawns if pressure gauge exceeds 60%; JSON requires clearing it.
3. md: Algorithm Archive is bonus loot behind BrewBot; JSON makes it the selfie terminal.
4. Palette: md/PNG include #0A0A0A and #FF0000; core.json omits them.
5. md Blockchain Bock "+10 SOVS buff, 18 SOVS"; JSON "18 ±5, 13-23": confirm.

## Not in the file, needs approval
How much squalor beyond the doc (pizza boxes, sleeping bags)? Is a sleeping founder allowed in the plate?
