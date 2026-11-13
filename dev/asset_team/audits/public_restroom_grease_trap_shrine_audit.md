# Audit: Public Restroom - Grease Trap Shrine (full 8-file review)

**Files read** (all under `design/worlds/debaucheryville/`):
1. Main md: `publicrestroomkebaballey.md` (restroom portion; core.json says "restroom portion only"; the tail is Mystery Meat Cart material appended by accident)
2. `core/public_restroom_grease_trap_shrine_core.json`
3. `environment/public_restroom_grease_trap_shrine_environment.json`
4. `interactions/public_restroom_grease_trap_shrine_interactions.json`
5. `items/public_restroom_grease_trap_shrine_items.json`
6. `location_nodes/public_restroom_grease_trap_shrine_location_nodes.json`
7. `npcs/Public_Restroom_Grease_Trap_Shrine/public_restroom_grease_trap_shrine_npcs.json` (no named NPCs; ambient flies, fryer steam, kebab jingle)
8. `PNG_Assets/Public_Restroom_Grease_Trap_Shrine_Complete_PNG_Asset_Requirements.md`
9. `sprite_mapping/public_restroom_grease_trap_shrine_sprite_mapping.json`
`events/`: MISSING (no match). Nothing else is missing. Also read earlier: `Quests/general_quests/publicrestroomgraffiti.md`.
Review images: `dev/asset_team/reviews/public_restroom_grease_trap_shrine_ext_review.jpg` and `_int_review.jpg` (the exterior reference sits on the int sheet).

## Q1, how well does it represent the location? Score: exterior 4/5, interior 3/5 (interior lowered from 4)
Exterior (tent flap, NOT A TOILET sign, glowing "Open Late" panel, neon kebab signs, Fistø "Puked here in '99" tag, skewer boxes, pickle barrels, flies) is faithful. Missing: the glowing chili-sauce trail (PNG L87, L100).
Interior has the receipt roll, swan, coin and antacid in the sink, QR mirror with Sheltie glyph, haiku door, and a neon-curtain doorway. The new nodes show what is absent: `gts_fisto_tag` and `gts_kebab_icon` (googly-eyed kebab glowing #00FF00 only while Hungover) are interior nodes in core and location_nodes but are nowhere on the interior plate; `gts_fixture` is a "tiny toilet" yet the room is a multi-fixture bathroom with a urinal; the skewer-hung bulb is a plain tube; no flies or cumin fog (environment ambient); no completion tracker on the haiku (`gts_haiku`).

## Q2, how well does it lean into the design requirements? Exterior 4/5, interior 3/5 (unchanged)
PNG palette: #FF8C00 dominant (reads), #8B4513 grease, #FFD700 oil highlights, #FF1493 tag, #00FF00 icon glow, #FF4500 trail, #2F4F4F shadow. Colour is right; the room is not a shrine: checkerboard tile, wood stalls and a marble vanity make a vintage restroom with orange light. Core.json's "lit like a sacred fryer exhaust" and PNG L127 "cramped mop closet size" are not delivered. No devotional arrangement.

## Verdict: REDO (interior); KEEP exterior (add the chili trail as an overlay).

## Redo plan (interior)
- **Hook:** "Half-shrine, half-biohazard, all ambiance" (md L37); "Not a Toilet, Unless Desperate" (core.json).
- **Palette:** #FF8C00 glow; #8B4513 grease film; #FFD700 highlights; #FF1493 Fistø tag; #00FF00 icon; #FF4500 trail; #2F4F4F shadow; fog #F0E68C / #98FB98 (PNG L188).
- **Exterior:** keep; add the chili trail (#FF4500 pulse) under the flap; crawl-entry states per PNG L226-240.
- **Interior (by node, in layout order):** `gts_crawlspace` tunnel from the tent flap; `gts_fixture` one tiny grease-glazed toilet, receipt roll "still warm"; `gts_sink` coin, antacid, napkin swan as offerings; `gts_mirror` cracked, QR codes, meat glyphs, Sheltie crown; `gts_fisto_tag` pink pilgrimage tag; `gts_kebab_icon` googly-eyed kebab icon; `gts_haiku` haiku with tracker; `gts_exit`. Closet scale; skewer bulb through the ceiling tile (md L23); flies and steam; no NPCs (npcs.json).
- **Satire beats:** (1) pilgrimage to a puke site; (2) warm 2004 receipt; (3) swan among biohazard; (4) skewer bulb; (5) "I pray. Then I leak."
- **Conflicts, need approval:**
  - Md says urinal (L25) and a stall; core says one tiny toilet. Which fixtures?
  - Fistø tag: md puts it on the exterior wall; nodes put it inside. Both?
  - Palette words in core ("fluorescent green", "kebab red") differ from PNG hex.
  - Items.json says "Kebab Coins"; items are priced 0, so likely moot.
  - Candles or extra offerings beyond the sink items?
