# Audit: Neon & Chrome Boutique

**Files read (8-file set, city debaucheryville, all under design/worlds/debaucheryville/):**
- Main md: neon_and_chrome_boutique.md (whole)
- core/neon_and_chrome_boutique_core.json
- environment/neon_and_chrome_boutique_environment.json
- interactions/neon_and_chrome_boutique_interactions.json
- items/neon_and_chrome_boutique_items.json
- location_nodes/neon_and_chrome_boutique_location_nodes.json
- npcs/Neon_And_Chrome_Boutique/neon_and_chrome_boutique_npcs.json (only file in folder)
- PNG_Assets/Neon_And_Chrome_Boutique_Complete_PNG_Asset_Requirements.md (HD-2D sheet plus folded-in legacy sheets, read in full)
- sprite_mapping/neon_and_chrome_boutique_sprite_mapping.json
- events/: no folder exists in this city, nothing matches. MISSING files: none.
- Also: debaucheryville.md (line 94); dev/asset_team/reviews/neon_and_chrome_boutique_ext_review.jpg and _int_review.jpg (looked at again).

## Q1, how well does it represent the location? Score 3/5
Doc: "a club entrance that sells things", "sells the idea of entry before the club does" (core atmosphere), bass audible from inside. Painted exterior: chrome-pillared glass front, pink and cyan neon tubes, mannequins on lit plinths, LED sign (blue-shifts at night), "Look Like You Belong / Actual belonging sold separately". All text present and the night plate glows. But it reads as an upscale deco shop. No rope, queue, light leak onto the street, speaker, fog or strobe. The interior plate (re-viewed) is stronger than the old audit said: purple counters, platform pyramid, velvet rope at the door, speaker stack, mirror. Still tidy and palm-fronded, not seedy.

## Q2, interior and exterior requirements? Score 3/5 (was 2)
Palette (md and PNG sheet): #FF1493, #C0C0C0, #4B0082, #00BFFF, plus #1A1A1A. Purple and chrome dominate; pink is only sign and tubes. Exterior misses: Neon Underglow Strip and wet pavement reflection (PNG sheet 1), open-door light spill. Interior has: Footwear pyramid, Eyewear wall, rope, mirror. Missing: Club Simulation booth with strobe, UV, fog and bass pulse (nodes ncb_fitting, ncb_simulation), Premium Stock locked gate ("PROVEN CUSTOMERS ONLY", rope plus chrome shutter), Katarina Counter, Glow section in UV. Floor is warm brown marble, not club-purple. Over the top: partial.

## Verdict: REDO exterior; REVISE interior (keep layout, repaint mood and add missing nodes)

## Redo plan
**Hook:** Glass door that sells the fantasy of the door: the shop is a fake VIP entrance (md subtitle "Dress for the Club You Want to Be In.").
**Palette:** #FF1493 sign and window glow, #4B0082 walls and floor, #C0C0C0 chrome, #00BFFF LED strips, #1A1A1A shadow zones (PNG sheet palette table). Core adds "showroom black".
**Exterior:** Node ncb_storefront. Add pink/purple Neon Underglow Strip and wet-look sidewalk reflection, light spilling from the chrome-framed auto door, speaker bass-glow, rope and stanchions, LED script sign (PNG sheet 1). Keep the four-category strip and small honest line.
**Interior:** Walk order from location_nodes: eyewear, footwear, premium, fitting, simulation, counter, exit. Add: Premium Stock gate (rope plus chrome shutter), Club Simulation booth with "CLUB SIMULATION" sign and chrome-ringed curtain, fog vent and bass stack (PNG sheets 2 and 3), Katarina Counter with register and "confidence talk" zone, UV Glow section, glass case for the Velvet Rope Clip. Repaint floor purple/black. NPC stations: Katarina at ncb_counter (chrome tailoring, neon headset), Showroom Host at ncb_fitting (club black, light piping), up to 4 customers and 4 mannequins (npcs json).
**Satire beats made visible:** empty wristband holder; platform pyramid ("higher the platform, the higher the shelf"); locked gate; "Look Like You Belong" vs honest line; Pre-Game Group and VIP Aspirant stations (md Customer NPCs).
**Conflicts, approval needed:**
1. Premium unlock: md says defeat Count Velvet Absinthe; items/interactions/nodes json say Velvet stage-7 plus vip_wristband_quest_complete and velvet_curtain_club_access_was_always_free. Which gate shows on the plate?
2. Subtitle: md "Dress for the Club You Want to Be In." vs core json "Equip Your Night" (that is the md tagline).
3. Staff: md names Assistant Dominik; npcs json names only "Showroom Host". Same person?
4. Items: json has 5 items (e.g. Premium Wrist Cuff 120, Glow Harness 95); md has about 25 with different prices. Which is stock?
5. Md sections 3 and 4 (Access, Glow) have no node in json.
**Not in the file, needs approval:** doorman or queue prop (no-people rule); how tall the platform pyramid may be.
