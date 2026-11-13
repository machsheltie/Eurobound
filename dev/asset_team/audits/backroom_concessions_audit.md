# Audit: Backroom Concessions (backroom_concessions)

## Files read (full 8-file set, 2026-11-12)
All under design/worlds/debaucheryville/:
1. backroomconcessions.md (main md, whole)
2. core/backroom_concessions_core.json
3. environment/backroom_concessions_environment.json
4. interactions/backroom_concessions_interactions.json
5. items/backroom_concessions_items.json
6. location_nodes/backroom_concessions_location_nodes.json
7. npcs/Backroom_Concessions/backroom_concessions_npcs.json (the only file in that folder)
8. PNG_Assets/Backroom_Concessions_Complete_PNG_Asset_Requirements.md (its "Spatial Composition" and "Visual target" are literally PENDING)
9. sprite_mapping/backroom_concessions_sprite_mapping.json (read; sprite status "built" for both plates)
- events/: no match for the stem or the location_id. Nothing MISSING among the eight.
- Reviews re-viewed: backroom_concessions_ext_review.jpg, backroom_concessions_int_review.jpg.

## Q1, how well does it represent the location? 3 / 5
- Painted correctly: concealed door, "404: Calories Not Found" sign backlit by a hacked rack (md l.25, l.36), CRT row, "Hot Pockets + Protocols" menu (md l.46), mismatched chairs, steaming fryer, gutted-machine pair node (location_nodes bc_vending_pair).
- Missing: one machine "stuffed with thermal paste" (md l.47; environment.json says it too), pop-up-ad cascade on the CRTs (the plate shows plain desktops), hacked electronics as lamps, LAN-party badges, any visible grease or health-code rot, ozone and mining shimmer (md particle list). Reads as a tidy gamer den, not a hacker snack-trap. JSON adds "office-chair lurkers" and "hacker diners" as ambient crowd; neither is on the plates.

## Q2, how well does it lean into the design requirements? 3 / 5
- md palette is Neon Green #00FF41, Warning Orange #FF8C00, Server Black #1C1C1C. Painted green is limited to sign, rack LEDs and one machine; beige/olive plaster and a red-brown checkerboard (in no file) dominate. Exterior is mostly mustard wall.
- Satire "health-code violations as underground authenticity" is not visible: no thermal paste sundae, no CryptoDöner box, no sticky fryer filth.
- Standard: "I don't want respectable Prague." This is handsome and moody, so it fails the seedy, over-the-top bar.

## Verdict: REDO (both plates)
Kept: door, sign, rack, menu board, CRT row as layout. Re-do colour balance and the missing jokes.

## Redo plan (from all files)
**Hook:** Hacker mystique as a deep-fryer; a food court in a server closet.
**Palette:** md/PNG spec: #1C1C1C ground, #00FF41 dominant light, #FF8C00 fryer and LEDs, supporting #E8E8D0, #C0C0C0, #8B4513, error red #FF0000 for pop-ups.
**Exterior:** near-black wall, door ajar, sign huge and glitching, rack cables like intestines, grease-slick floor, no beige, no checkerboard.
**Interior:** booth between two gutted machines (left: thermal paste tubs; right: glowing "inner knowledge"); CRTs mid pop-up cascade; peeling laminated menu; counter wood with grease; ozone shimmer; floor stained concrete or sticky lino.
**Satire beats made visible:** thermal paste as "industrial art"; infected CRTs as dining atmosphere; fryer beside mining rigs; "Hot Pockets + Protocols"; Donny.exe's counter props (lanyard, broken vape mod) as set dressing only.
**Not in the file, needs approval (md vs JSON conflicts):**
- Palette: md says green/orange/black; core + environment JSON say sick fluorescent, server blue, thermal-paste silver, error red. Which governs?
- Menu: md has CryptoDöner, Thermal Paste Sundae, RAM Chips & Dip, Alt+Meat Slider (6 SOVS), 404 Juice (2 SOVS); items.json has the first three plus "Protocol Pocket" (6) and no Slider or Juice. Which five items get icons?
- Effects differ (sundae: md +5 Int/-3 HP, JSON heat resistance/accuracy penalty); not a visual issue but icons depend on it.
- Donny.exe look: md lanyard + vape mod; npcs.json apron + keyboard holster. Which?
- Entrance: md says via a restroom-stall graffiti clue; core.json says hidden door behind Cyberspace Kavarna. Which room is the door in?
- Which pop-up ad text may appear on CRTs?
