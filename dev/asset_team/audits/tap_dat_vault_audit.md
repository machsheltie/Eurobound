# Audit: The Tap Dat Vault

**Files read:** design/worlds/debaucheryville/the_tap_dat_vault.md (whole); PNG_Assets/Tap_Dat_Vault_Complete_PNG_Asset_Requirements.md; design/items/brewery_tour/{beer,opener,stamp}_tap_dat_vault_item.md; worlds/debaucheryville/environment/tap_dat_vault_environment.json; npcs/The_Tap_Dat_Vault/npc_glitching_bouncer.md; Quests/Location Specific/Debaucheryville/brewerytourdebaucheryville.md (grep); debaucheryville_locations_index.md (grep); dev/asset_team/TEAM_BRIEF.md s2; dev/asset_team/reviews/tap_dat_vault_{ext,int}_review.jpg.

## Q1, how well does it represent the location? 4/5
- Exterior matches "large metal vault door, neon graffiti TAP DAT VAULT, countdown glyphs, steam seeping" (doc, Exterior Description): painted door, dripping cyan/pink tags, pink glyph strip, glitch-pixel blocks, vents. Strong.
- Interior has the subwoofer vats (copper tanks with speaker cones), DJ booth with camera rig, "YOU ARE BREWTIFUL" hologram, neon-lit floor. Missing "cyberpunk basement" and "GPU having a breakdown": it reads as a steampunk brewhouse with speakers.

## Q2, interior and exterior requirements? 3/5
- Palette (#00FFFF primary, #FF1493 accent, #4B0082 background): exterior is mostly grey stone and steel; cyan/pink live only on the door, no purple. Interior day plate is amber and brown. Night plate carries the palette on the floor reflections only, not as the dominant colour.
- Missing required items: vape rig dispenser at the bar (bar shows taps and jars), neon tubing floor-to-ceiling grid, circuit-board fermentation chambers, "heavy density" vapor clouds hanging mid-air, RGB flicker/crash, fridge livestreamer. Satire (beer is vape, ad-spam, tech-bro club) is not visible; only the door gag lands.
- Plaza surround (lamp posts, planters, stone balustrades) is respectable and tidy.

## Verdict: REDO, interior (exterior door is KEEP-quality; plaza dressing and palette could be pushed)
Over the top: exterior yes, interior no.

## Redo plan
- **Hook:** "We Don't Serve Beer, We Inhale It": a nightclub inside a GPU having a breakdown (doc Theme & Vibe).
- **Palette:** #4B0082 walls and ground, #00FFFF tubing and vat glow dominant, #FF1493 accents; no brown/copper.
- **Exterior:** keep door; drop cobble-quaint dressing, add more glitch and cyan/pink spill on the plaza.
- **Interior:** black-purple basement, neon tube grid floor to ceiling, circuit-board fermentation chambers, vats as subwoofers, vape rig bar, DJ booth, fridge livestream setup, hanging vapor, RGB flicker.
- **Satire beats:** bartender vape lanyard and vats-are-subwoofers (Obvious signs they ignore); "inhaled beverages" (Cultural Targets); CRT ad-bot spam (Glitched Brew Ad Bot).
- **Not in the file, needs approval:** how literal is the glitch-art (pixel-sorted tearing across the plate)? Should day/night differ only by RGB intensity, since it is a midnight venue?
