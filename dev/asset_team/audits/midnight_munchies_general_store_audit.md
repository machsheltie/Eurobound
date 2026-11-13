# Audit: Midnight Munchies General Store (debaucheryville)

**Verdict: REDO** (unchanged after the full 8-file review)

## Files read (all under design/worlds/debaucheryville/)
- Main: `midnight_munchies_general_store.md`
- core: `core/midnight_munchies_general_store_core.json`
- environment: `environment/midnight_munchies_general_store_environment.json`
- interactions: `interactions/midnight_munchies_general_store_interactions.json`
- items: `items/midnight_munchies_general_store_items.json`
- location_nodes: `location_nodes/midnight_munchies_general_store_location_nodes.json`
- npcs: `npcs/Midnight_Munchies_General_Store/midnight_munchies_general_store_npcs.json` (only file in folder)
- PNG_Assets: `PNG_Assets/Midnight_Munchies_General_Store_Complete_PNG_Asset_Requirements.md`
- sprite_mapping: `sprite_mapping/midnight_munchies_general_store_sprite_mapping.json`
- events/: no match. MISSING files: none. (PNG doc "Spatial Composition" and "State and Character Coverage" are PENDING.)
- Reviews seen: `reviews/midnight_munchies_general_store_ext_review.jpg`, `_int_review.jpg`.

## Q1, represents the location? 2/5
- core/nodes call for "a fluorescent survival beacon" blazing "into dark Hostel Row" (location_nodes mm_storefront). Painted: a quaint brick corner house with flower boxes, ivy, lamppost, rooftop AC. Green neon at night is right, but the day face is village charm.
- Signs painted: MIDNIGHT MUNCHIES, "Open When You Need Us", hours plate. Missing: "Prices reflect the hour. Plan ahead next time." and "You could have bought this cheaper earlier. But here we are." (md Signage). Core subtitle "We Know Why" not shown. The window is neat, not "cluttered" (md).
- Interior: five identical straight aisles, a fridge wall, counter at left, and a heat-lamp case at far right. The nodes JSON wants Recovery Aisle, Hygiene and Supplies, Heat Lamp Lottery, Věra's Counter as distinct landmarks; the plate does not tell aisles apart. No Věra, no foragers, no post-club customers (npcs JSON).

## Q2, leans into requirements? 2/5
- Palette conflict between files: md and PNG doc give White #F5F5F5, Energy Drink Green #00FF00, Late Night Blue #191970, Warning Red #FF6347, Heat Lamp Orange #FFA500; core and environment JSON give fluorescent white, convenience red, energy-drink blue, heat-lamp orange (no green). Painted: tan brick, grime, green fridge glow, orange only in the heat lamp, no red anywhere.
- Lighting spec: harsh fluorescent, heat-lamp glow, neon flicker (md). Interior is dim and moody, not blown out.
- Satire is not in the building. Respectable, not seedy.

## Redo plan
**Hook**: A fluorescent lifeline whose markup "measures how badly the player failed to plan" (core atmosphere): 20% markup after 02:00 (interactions mm_checkout).

**Palette**: #F5F5F5 blown-out interior and fridge glare; #00FF00 neon and energy-drink glow; #191970 street and sky; #FF6347 price and warning signs; #FFA500 heat lamp. Ask which palette set is canon (see below).

**Exterior**: Squat corner box over-lit against a dark street (nodes mm_storefront); window crammed with energy drinks and emergency items (md); six sign lines including the two red price jokes; flickering neon; hours "10 PM - 8 AM, We Don't Judge Your Timing". No flower boxes, no ivy.

**Interior**: Cramped, maximum density (md). Landmarks per node: mm_recovery_aisle (energy drinks, hangover kits), mm_hygiene_aisle (supplies; "Just In Case" and Practical sections), mm_heat_lamp (big orange case, kebabs, mystery items), mm_counter (Věra, practical cardigan, scanner; lottery tickets, cigarettes), mm_exit. Ambient: hostel kitchen foragers, post-club customers, delivery worker (npcs JSON).

**Satire beats made visible**:
1. Price board with a 2 AM +20% line (interactions, items prices 3 to 12 SOVS).
2. "Cheaper earlier" honest sign (md).
3. Heat Lamp Lottery: heat-lamp kebab, 6 SOVS, result unknown (items, interactions).
4. Brass-knuckle keychains, party-popper "flash grenades", fake VIP wristbands (md sections 3 and 4).

**Not in the file, needs approval**:
- Which palette set is canon, md/PNG (green, blue) or core/environment (convenience red, energy-drink blue)?
- A visible clock at 2 AM or later?
- How crowded may the heat-lamp case look?
