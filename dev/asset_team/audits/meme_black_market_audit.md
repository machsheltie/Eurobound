# Audit: Meme Black Market (meme_black_market), full 8-file review

## Files read
- design/worlds/debaucheryville/memeblackmarket.md (whole)
- core/meme_black_market_core.json
- environment/meme_black_market_environment.json
- interactions/meme_black_market_interactions.json
- items/meme_black_market_items.json
- location_nodes/meme_black_market_location_nodes.json
- npcs/Meme_Black_Market/meme_black_market_npcs.json (folder holds only this file)
- PNG_Assets/Meme_Black_Market_Complete_PNG_Asset_Requirements.md (spatial composition sections "PENDING", palette and sheets present)
- sprite_mapping/meme_black_market_sprite_mapping.json (listing checked; node ids match location_nodes)
- events/: no match (MISSING). All 8 subfolder files exist.
- Also: design/Quests/general_quests/memeblackmarket.md, npc_tony420.md (mention)
- Plates: dev/asset_team/reviews/meme_black_market_ext_review.jpg, meme_black_market_int_review.jpg

## Q1, how well does it represent the location? 4/5 (held)
Threshold: the doc says a hidden VHS shelf, no external signage (md l.29-31, core zone "Hidden room behind Internet History Museum"). The plate has the shelf, kiosk and CRT with an open state glowing green, so the mechanism reads. Interior is the strongest of the three: candle-ringed AIM away-message altar, Guy Fieri visor wig, ASCII cats in the ducts, Funcoland bags, lava lamps, green vape mist, BSOD desk. New files: seven named nodes. The plate shows the threshold, counter altar, mastery desk and altar but not a distinct Meme Summon Circle ("Projected GIF ring for risky summons") or a Trinket Wall; it also lacks the "gutted Blockbuster" and "DO NOT LOOK AT THE BABY" beats.

## Q2, how well does it lean into the design requirements? 3/5 (held)
Palette conflict decides it (see below). Against the md palette the interior is brown and amber with little #4169E1 blue. Against core/environment JSON ("RGB magenta, CRT cyan, Windows grey, corrupted green") the threshold's synthwave pink and purple actually fits, but it dresses the room as a boutique museum corner: velvet ropes, brass posts, vines, cosy rug. The JSON says "RGB-lit contraband den where corrupted GIFs and obsolete jokes are treated as sacred inventory" and environmental_storytelling wants "corrupted artifacts" and a "crashing desktop"; none exist at the threshold.

## Verdict: REDO threshold; KEEP interior with a regrade and two added props (unchanged)
The threshold is the failure. The interior needs a summon circle and a visible trinket wall.

## Redo plan
- **Hook:** "Weaponized Nostalgia, Fair Market Value" (core.json subtitle); md l.200 "I run on LimeWire and vengeance".
- **Palette:** needs a ruling. md/PNG md: #4169E1 CRT blue, #00FF00 green, #8B4513 brown, #00FF7F Baja Blast mist. JSON: RGB magenta, CRT cyan, Windows grey, corrupted green. Safe merge: blue/cyan screen spill, magenta RGB cycling strips (md l.35 "RGB-lit"), green accent, brown carpet.
- **Exterior (threshold):** the museum back corner as a gutted Blockbuster (md l.29): dead rental shelving, GeoCities kiosk with swirling gif, broken MSN Messenger terminal with error dialogs (md l.19), dial-up modem shrine, one VHS shelf scraped off-kilter. No velvet ropes or vines. Keep the open state: green light from the shelf gap (PNG md Closed/Opening/Open frames).
- **Interior:** keep the room. Add a projected GIF summon ring on the floor (mbm_summon_point), a wall of Funcoland bags, icons and corrupted artifacts (mbm_trinket_wall), flickering corrupted-gif posters instead of tidy prints, a legible BSOD on the MemeMastery desk, ASCII cats kept.
- **Satire beats made visible:** away messages as devotional icons; Funcoland bags as sacred relics (md l.43); ASCII cats as guardians; Windows crash loop; MemeLord.exe layered merch, CRT visor, floppy wallet (npcs.json visual).
- **Conflicts, approval needed:** (1) trinket stock: md l.91-98 lists Shiba Hype 10, Dat Boi 5, Dancing Baby.exe 7, Trollface Bomb 13 SOVS; items.json lists Dancing Baby Charm 12, Infinite Badger Loop 10, Corrupted Reaction GIF 8. Which set is canon? (2) md access is graffiti, kiosk, password "AllYourBase69", 03:33 lockout; core.json uses only the entrance_unlocked flag. (3) Palette as above. (4) Exit destination id `debaucheryville_blockbuster_internet_museum_01` vs the museum's md name.
- **Not in the file, needs approval:** faded Blockbuster logo on the threshold wall; whether "DO NOT LOOK AT THE BABY" shows here or only in the Velvet Curtain bathroom.
