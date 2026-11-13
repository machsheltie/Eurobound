# Audit: Public Restroom - Grease Trap Shrine

**Files read:** `design/worlds/debaucheryville/publicrestroomkebaballey.md` (whole; it has no hex palette, and its tail is the Mystery Meat Cart material appended by accident); `PNG_Assets/Public_Restroom_Grease_Trap_Shrine_Complete_PNG_Asset_Requirements.md` (palette lives here); `Quests/general_quests/publicrestroomgraffiti.md`; `dev/asset_team/reviews/public_restroom_grease_trap_shrine_ext_review.jpg` and `_int_review.jpg`. Other grep hits (`core/`, `interactions/`, `location_nodes/`, npcs) add no visual requirements.

## Q1, how well does it represent the location? Score 4/5
Exterior is very faithful: grease-stained vinyl tent flap, hand-scrawled "NOT A TOILET (unless desperate)" (L13), repurposed glowing "Open Late" sign (L7), skewer boxes and pickle barrels (L16), Fistø's pink tag with the Mecca line (L17-18), fryer steam (L8), neon kebab signage, and the dark gap under the flap for the crawlspace.
Interior hits: glistening grease walls (L21), receipt roll (L22), swan napkin, coin and antacid in the sink (L24), mirror with QR and meat glyphs and a Sheltie (L25-26), haiku on the stall door (L29-31). Misses: the bulb dangling from a skewer stabbed in the ceiling tile (L23) is a plain wall tube; no flies or fog; no googly-eyed kebab icon visible. The PNG spec says toilet "cramped mop closet size"; the painted room is a spacious three-fixture bathroom.

## Q2, how well does it lean into the design requirements? Score 4/5 exterior, 3/5 interior
Palette (PNG spec): Sickly Orange #FF8C00 dominant (sign, tent glow, glazed walls), Hot Pink #FF1493 tag, Chili Red #FF4500 neon bleed, Dark Slate #2F4F4F shadows. The orange dominates correctly, so the colour reads. The exterior is seedy and a bit absurd. The interior is the problem: checkerboard tile, wooden stalls, an urn-like sink counter and a gilt mirror make a tidy vintage restroom with orange light. Nothing reads as a shrine ("sacred biohazard", L33-37): no offerings, no devotional arrangement, no pilgrim wear on the floor. It is atmospheric, not over the top.

## Verdict: REDO (interior). KEEP exterior (4 and 4, clearly characterful).

## Redo plan (interior)
- **Hook:** "Half-shrine, half-biohazard, all ambiance" (L37).
- **Palette:** #FF8C00 sign-light glow filling the room; #8B4513 grease film on every surface; #FFD700 oil-slick highlights; #FF1493 Fistø tag; #FF4500 chili trail through the flap; #2F4F4F shadows.
- **Exterior:** Keep as painted.
- **Interior:** Shrink to a cramped closet (PNG spec); a single grease-glazed toilet like an altar; the dangling bulb on a skewer through the ceiling tile (L23); sink with coin, antacid and swan arranged as offerings (L24); cracked mirror with QR and meat glyphs (L25-26); haiku stall wall (L29-31); glowing googly-eyed kebab icon on the wall (L44).
- **Satire beats:** (1) pilgrimage to a puke site (L18); (2) receipt "still warm" (L22); (3) swan napkin amid biohazard (L24); (4) skewer bulb (L23); (5) "I pray. Then I leak." (L31).
- **Not in the file, needs approval:** Are candles or offerings allowed beyond the sink items? How many fixtures does the closet hold (the file also names a urinal, L25)? Should flies appear inside?
