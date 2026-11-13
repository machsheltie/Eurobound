# Plan: Central Shamsterdam Bike Crossing (outdoor area plate, asset team)

**Files read** (design/worlds/shamsterdam/): central_shamsterdam_bike_crossing.md; core, environment, interactions, items, location_nodes, events, sprite_mapping `central_shamsterdam_bike_crossing_*.json`; npcs/central_shamsterdam_bike_crossing_npcs.json; PNG_Assets/central_shamsterdam_bike_crossing_png_assets.md. **MISSING:** `npcs/<Location>/` folder (no per-NPC .md).

**Hook**: "Frogger, But The Logs Hate You": six bike lanes, two tram tracks, a "false safety" island.

**Palette**: Bike Lane Red #CC0000 (lanes, dominant); Dutch Orange #FF6600 (warning signs, construction, rental bikes); Tram Yellow #FFD700 (trams, hazard stripes, eye-catcher); Asphalt Grey #4A4A4A (ground); Bicycle Black #1C1C1C (frames, tires, wire); Sidewalk Stone #B8B8B8 (curbs, island); Judgmental Blue #003DA5 (officer, call box); Safety Vest Orange #FF5500 (rental guy).

**Area layout**: Fixed high three-quarter camera looks north across the crossing from the south sidewalk. Foreground: south sidewalk, rental kiosk (TRAM TRACK MAGNETS), Tourism Board pamphleteer, signs "Cyclists Have Priority" and "Trams Cannot Stop", useless signal button, exit south to The Flesh Market. Midground: lanes 1-3 east, tram track 1, pedestrian island (Fallen Tourist), tram track 2, lanes 4-6 west, with tram poles and tangled wire overhead. Southwest corner: cafe terrace (Gerrit). Far side: north sidewalk, canal "full of sunken bikes", exits north (Canal Ring Promenade) and east (Museum Mile); west exit Coffeeshop Quarter. Bike racks everywhere, Emergency Call Box, "I Shamsterdam" ghost outline. Cargo Parade wall of bakfiets sprites. Flat-fronted, wire-and-sign-heavy; no stepped gables.

**Satire beats made visible**
1. "bike-friendly city" marketing vs reality: pamphlets plus "Cyclists Have Priority" (nodes; PNG doc).
2. Island as "False hope made concrete" (interactions).
3. "Some bikes have been there since the 1970s"; canal of sunken bikes.
4. Cargo Parade: "Wall of bakfiets", flowers, dogs, waving children (md).
5. Ghost sign: "Faded outline where the famous sign USED to be (removed 2018)".

**Not in the file, needs approval**
- Debauchery: the file is traffic satire only. Proposal: night party bikes, bar crawlers, The Flesh Market neon bleeding in from the south. Approve?
- Conflict: I SHAMSTERDAM is a ghost outline here (removed 2018) but an empty plinth on Museum Mile (shamsterdam.md line 53). Which is canon?
- Conflict: core/events JSON still say swipe/tap; md says W/S and D-pad (v35).
- Same kiosk as shamsterdam_bike_rental.md?
- "Dutch" is used throughout (palette name, NPC text): real national term; keep?
