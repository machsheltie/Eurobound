# Audit: Hostel Midnight Checkout (debaucheryville)

**Verdict: REDO** (confirmed after the full 8-file review)

## Files read (all under design/worlds/debaucheryville/)
- Main: `hostel_midnight_checkout.md`
- core: `core/hostel_midnight_checkout_core.json`
- environment: `environment/hostel_midnight_checkout_environment.json`
- interactions: `interactions/hostel_midnight_checkout_interactions.json`
- items: `items/hostel_midnight_checkout_items.json`
- location_nodes: `location_nodes/hostel_midnight_checkout_location_nodes.json`
- npcs: `npcs/Hostel_Midnight_Checkout/hostel_midnight_checkout_npcs.json` (the only file in that folder)
- PNG_Assets: `PNG_Assets/Hostel_Midnight_Checkout_Complete_PNG_Asset_Requirements.md`
- sprite_mapping: `sprite_mapping/hostel_midnight_checkout_sprite_mapping.json`
- events/: no match. MISSING files: none. (PNG doc says "Spatial Composition" and "State and Character Coverage" are still PENDING.)
- Reviews seen: `reviews/hostel_midnight_checkout_ext_review.jpg`, `_int_review.jpg`.

## Q1, represents the location? 2/5
- Exterior is better than first scored: four storeys, patched brick with blue patches, neon with dead S and O, AC units, laundry, 4.2 Stars / 24 HOUR / Quiet Hours plates. But the neighbours are equally tidy, so the "competing for the same desperate clientele" joke (md) is invisible, and it still reads as a handsome old townhouse.
- The location_nodes/core JSONs define seven nodes: hmc_exterior, hmc_reception, hmc_dorm, hmc_bunk_confession, hmc_kitchen, hmc_lounge_wifi, hmc_exit. The interior plate shows only reception, kitchen nook and lounge. The Representative Dorm and Confession Bunk (the quest node, lower bunk plus curtain) are absent, as is the ICQ terminal.
- The two JSONs do not require a basement or per-floor cutaways. Those come from the md only.

## Q2, leans into requirements? 2/5
- Palette (md, core, PNG doc): Beige #D4C4A8, Hostel Blue #4169E1, Institutional Green #8FBC8F, Warning Red #FF6347, Faded Wood #8B4513. Painted: orange-brown brick, pink neon, blue only as patches, green only as wainscot.
- Lighting spec (md): harsh fluorescent commons. Interior has fluorescent tubes but is grimy-moody, not hostel-blue/beige.
- Props in md/PNG doc not visible: Wi-Fi corner with Occupied sign, SINGLE working outlet (a cable on the floor hints at it), 2007 microwave, one burner, key hooks half-empty (reception shows full pigeonholes), note wall as a "gallery". Seedy and over the top: no.

## Redo plan
**Hook**: "12 SOVS/Night. Your Dignity Costs Extra." (md subtitle). Passive-aggressive notes are the architecture.

**Palette**: Beige #D4C4A8 dominant on facade and walls; Blue #4169E1 bunk frames, sign trim; Green #8FBC8F corridors; Red #FF6347 neon and warning notes; Faded Wood #8B4513 doorframe (PNG doc palette table).

**Exterior**: Keep the four-storey patched face; add identical rival hostels either side with their own tired signs (md "Environmental Context"); more ACs at random intervals; hand-painted "4.2 Stars" plate; staff or backpackers always entering and leaving (md Atmosphere).

**Interior**: One playable plate per node: reception counter with half-empty key hooks and bell (md); Representative Dorm with narrow bunk aisles and 60% ladders (location_nodes); Confession Bunk, lower bunk with curtain (location_nodes); kitchen with note gallery, one burner, 2007 microwave, mystery fridge (items: hmc_mystery_fridge_food); lounge with single outlet, Wi-Fi corner, ICQ terminal (interactions: hmc_wifi). Staff stations: Radek (night, shirt, stubble, "thousand-yard calm"), Day Receptionist (layers, key ring), Long-Term Guest at the bunk with too many tote bags (npcs JSON). Fluorescent common areas, dim corridors, individual bunk lights (md).

**Satire beats made visible**:
1. Neon with two dead letters, "4.2 Stars, It was an experience" (md Signage).
2. Note wall: LABEL YOUR FOOD, WHO TOOK MY CHEESE (md Kitchen; PNG doc CRITICAL).
3. Booking tiers as visible price boards: 12, 35, 45 SOVS (items JSON).
4. Ambient backpackers, snorers, kitchen foragers (npcs JSON, max 4 each).

**Not in the file, needs approval**:
- Extra storeys and basement appear in the md only, not in the nodes. One cutaway, or a plate per floor?
- PNG doc "Visual target" is PENDING. How far past "questionable structural choices" may the building lean?
