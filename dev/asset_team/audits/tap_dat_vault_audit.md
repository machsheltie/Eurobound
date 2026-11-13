# Audit: The Tap Dat Vault

**Files read (all 8 subfolder files plus main md), under design/worlds/debaucheryville/:**
- the_tap_dat_vault.md (whole)
- core/tap_dat_vault_core.json
- environment/tap_dat_vault_environment.json
- interactions/tap_dat_vault_interactions.json
- items/tap_dat_vault_items.json
- location_nodes/tap_dat_vault_location_nodes.json
- npcs/The_Tap_Dat_Vault/tap_dat_vault_npcs.json and npc_glitching_bouncer.md
- PNG_Assets/Tap_Dat_Vault_Complete_PNG_Asset_Requirements.md (incl. legacy sheets 1-5)
- sprite_mapping/tap_dat_vault_sprite_mapping.json
- events/: no match (MISSING)
- design/items/brewery_tour/{beer,opener,stamp}_tap_dat_vault_item.md
- dev/asset_team/reviews/tap_dat_vault_{ext,int}_review.jpg (re-viewed)

## Q1, how well does it represent the location? 4/5 (unchanged)
- Exterior is the strongest piece: stairs down to a graffitied vault door, countdown-glyph strip, cyan/pink tubes, steam vents (md Exterior Description; core.json "countdown glyphs"; env.json "Neon graffiti door").
- Interior has subwoofer vats, DJ booth, "YOU ARE BREWTIFUL" hologram, wet neon floor. It still reads as a steampunk copper brewhouse with speakers, not "a nightclub inside a GPU having a breakdown" (md Theme & Vibe).

## Q2, interior and exterior requirements? 3/5 (unchanged)
The new files raise the required list, not the score:
- Missing required items: circuit-board fermentation chambers and neon floor-to-ceiling grid (md Furniture & Props; PNG legacy sheet 1), vape rig dispenser (bar shows plain taps and jars), heavy suspended vapor, RGB-flicker/software-crash walls, fridge livestreamer, bartender with vape lanyard, DJ zombies, techno monks (PNG sheet 3), vapor pressure console with gauges (location_nodes tdv_rhythm), VIP vapor lounge door, Ad Bot spam banners.
- Palette: md and PNG say #00FFFF / #FF1493 / #4B0082 plus black and vapor white; core.json drops purple (cyan, pink, vault steel, vapor white). Plates are copper-amber and grey stone; cyan/pink is door and floor reflection only.
- Exterior has the prescribed plaza surround tidy and respectable; core.json calls it a "Tap Dat-owned plaza node".

## Verdict: REDO interior (unchanged); exterior door KEEP, plaza dressing and palette pushed
Over the top: door yes, interior no.

## Redo plan
- **Hook:** "We Don't Serve Beer, We Inhale It": a nightclub inside a GPU breakdown (md).
- **Palette:** #4B0082 walls, #00FFFF tubing and vat glow dominant, #FF1493 accents, #000000 structure, vapor white haze (PNG Color Palette); no copper or brown.
- **Exterior (tdv_plaza, tdv_vault):** keep door. Add countdown glyphs lit to 00:00, steam, cyan/pink spill, glitch-block tearing on plaza stone; reduce cobble-quaint dressing.
- **Interior nodes (location_nodes):** tdv_vats subwoofer vats with LED nonsense metrics; tdv_rhythm vapor pressure console with three-strike icons and gauges; tdv_adbot CRT spam banners; tdv_brewmistress strobe arena; tdv_service bar with vape rig dispenser; tdv_selfie hologram wall near bar. Add circuit-board fermentation chambers, floor-to-ceiling neon grid, DJ booth with livestream rig, VIP vapor lounge door, hanging vapor, RGB wall flicker.
- **NPC stations:** Glitching Bouncer at tdv_vault (chrome silhouette, cyan/pink scanner), bartender with vape lanyard at bar, DJ zombies at booth, techno monks half-visible in vapor, fridge livestreamer inside a chamber, vapor club patrons and livestream drones (npcs.json ambient).
- **Satire beats made visible:** vape lanyard and vats-are-subwoofers (md "Obvious signs"); ad spam; "inhaled beverages"; "Your lungs are just another glass" (beer item).
- **Lighting:** emission masks per sprite_mapping (r signs, g puzzle cues, b boss cues); puzzle/boss cues override ambience.

## Conflicts, approval questions
1. md says the bouncer checks two openers; core.json, npcs.json and the opener item say no opener gates entry (stale dialogue). Treat md as superseded?
2. md: door opens at exactly 00:00; core.json: window 00:00-00:59.
3. Tour slot: md "2 of 4", core.json "Stop 3".
4. Palette: purple missing from core.json.
5. DJ zombies, monks, bartender, livestreamer are in md and PNG but not npcs.json or sprite_mapping: build them?

## Not in the file, needs approval
How literal is the glitch-art (pixel-sorted tearing across the plate)? Should day and night differ only by RGB intensity, since it is a midnight venue?
