# Audit: euro_ink_4_less (debaucheryville)

**Verdict: REDO** (exterior mainly; interior repaint for palette and gags). Unchanged after the full 8-file review.

## Files read (all under design/worlds/debaucheryville/)
- Main: `euro_ink_4_less.md`
- core: `core/euro_ink_4_less_core.json`
- environment: `environment/euro_ink_4_less_environment.json`
- interactions: `interactions/euro_ink_4_less_interactions.json`
- items: `items/euro_ink_4_less_items.json`
- location_nodes: `location_nodes/euro_ink_4_less_location_nodes.json`
- npcs: `npcs/Euro_Ink_4_Less/euro_ink_4_less_npcs.json` (only file in folder)
- PNG_Assets: `PNG_Assets/Euro_Ink_4_Less_Complete_PNG_Asset_Requirements.md`
- sprite_mapping: `sprite_mapping/euro_ink_4_less_sprite_mapping.json`
- events/: no match. MISSING files: none. (Viktor the Barker's own file `npc_tattoo_barker.md` is cited by the md but is not one of the 8; not read.)
- Reviews seen: `reviews/euro_ink_4_less_ext_review.jpg`, `_int_review.jpg`.

## Q1, represents the location? 3/5
- Exterior has the small checks (pink neon with dead "4", WALK-INS WELCOME, HYGENIC / LICENSED / CHEAP FAST GOOD all YES, NO REGRETS Mostly, duck on the door). But it is a mossy ivy-covered box, not the "sketchy_professionalism" tourist-trap den in core JSON. Missing: Viktor at the alley mouth, the kebab shop north and currency exchange neighbour (core exits, md line 90), cobble-to-concrete alley.
- Interior covers more of the node list than first scored: reception counter with jewellery case, duct-taped chair, sheet-divided second station, beaded curtain with mattress, 4:20 clock, PAIN IS TEMPORARY poster, mirror, beanbag, magazines table. Not visible: Online Tattoo Academy certificate, home-printed licence, Wall of Fame, empty guest book, lollipop jar, autoclave.

## Q2, leans into requirements? 3/5
- Palette (PNG doc, md): Pink #FF1493, Clinical White #F5F5F5, Green #7FFF00, Blood Red #8B0000, Dingy Gray #696969, Nicotine Yellow #F5DEB3, Fluorescent #F0F8FF. Painted: pink and green neon on point, but gray, brown and moss dominate; white and nicotine yellow absent.
- Lighting spec (environment JSON): fluorescent main room with random flicker, neon accent, harsh work lamp at the chair. Interior has tubes and lamp but reads dim and moody. Night mode should be neon-dominant, "seedy_authentic".
- Satire is in text, not in the building; flash-art gags (geese-dragons, beaked skull, Looney Tunes) do not read.

## Redo plan
**Hook**: Confident incompetence: "No Regrets. Mostly No Regrets." Skeleton becomes duck (core key_comedy_beat).

**Palette**: Pink #FF1493 floods sign, window and alley; Clinical White #F5F5F5 walls and surfaces; Green #7FFF00 beer sign; Blood Red #8B0000 flash accents; Gray #696969 floor only; Nicotine Yellow #F5DEB3 ceiling stains.

**Exterior**: Narrow alley off Astronomical Cock-Up Square, kebab shop one side, suspicious currency exchange the other, dumpster, cracked concrete under pink spill (location_nodes). Glass door with peeling tint; window crammed with flash art; Viktor's position at the alley mouth (md layout). Remove ivy.

**Interior**: Single 15x20 ft room (md). Stations as in location_nodes: reception_counter (Marta, 50% present), tattoo_station (Donát, leather vest, gold tooth), flash_art_wall, waiting area with Wall of Fame and stuck 4:20 clock, back room visible through curtain. Stained beanbag, autoclave steam "for show", cigarette smoke from the back (environment JSON).

**Satire beats made visible**:
1. Dragons that look like geese; skulls with beaks (flash_art_wall, 3-look easter egg).
2. Online Tattoo Academy 2019 certificate and printed licence (examinable: fake_license).
3. CHEAP FAST GOOD, YES beside all three (md Window stickers).
4. Wall of Fame, uncertain faces; empty guest book; lollipop jar (items: Bravery Lollipop).

**Not in the file, needs approval**:
- Storey count: md says only "alley" and single-room interior.
- How loud may the pink glow be?
