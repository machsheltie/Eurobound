# Absinthe Arcade Location Package Design

## Intent

Create the eight missing Absinthe Arcade production-design files in the established Debaucheryville location schema. The package must reconcile the older location brief with the finalized exterior art, current HD-2D/Godot direction, and the richer quest files without absorbing the separately designed Absinthium Taproom or Claw Machine Maintenance Closet Restroom.

## Goals

- Give Claude and other implementation agents one consistent description of the exterior, interior, contents, navigation, state, and asset mapping.
- Match the existing `core`, `environment`, `interactions`, `items`, `location_nodes`, `npcs`, `PNG_Assets`, and `sprite_mapping` patterns.
- Preserve established gameplay: tokens, twisted cabinets, rigged claw machine, Backpack Girl, the hidden restroom entrance, the hidden Taproom entrance, couchsurfing, the NFT hunt, and club-flyer placement.
- Make the two linked sublocation entrances unmistakable in interior-image generation while leaving their interiors to their own Markdown files.

## Non-goals

- Do not redesign or duplicate the Absinthium Taproom interior.
- Do not redesign or duplicate the Claw Machine Maintenance Closet Restroom interior.
- Do not implement Godot scenes, generate art, alter Blender files, or revise quest dialogue.
- Do not fold unrelated Backroom Concessions or Cyberspace Kavarna content into the Arcade.

## Canon and Precedence

When sources disagree, use this order:

1. Finalized exterior assets, `hd2d_asset_manifest.md`, and `references/mastercomponentbreakdown.md` for exterior appearance and production method.
2. The newer `design/Quests/debaucheryville/` versions for quest state, dialogue ownership, and current reward names.
3. Dedicated location files `the_absinthium_taproom.md` and `clawmachinemaintenanceclosetrestroom.md` for their IDs, gates, and entrance requirements.
4. `absinthearcade.md` for the Arcade's gameplay, satire, and remaining interior concepts.
5. Older `design/Quests/Location Specific/Debaucheryville/` versions only where the newer files are silent.

Quest dialogue remains in its authoritative quest/profile documents. The location package may bind triggers and summarize outcomes but must not create competing scene text.

## Selected Approach

Use canonical reconciliation rather than literal transcription or a multi-location redesign. The Arcade remains one location package with explicit outbound transitions to two separately authored sublocations.

Alternatives considered:

- Literal conversion was rejected because it would preserve obsolete pixel-art and narrow-alley assumptions that contradict the finalized exterior.
- Expanded complex redesign was rejected because it would duplicate the Taproom and restroom specifications and blur location ownership.

## Visual Direction

### Exterior

The Arcade occupies a tall, dignified Prague-inspired historic building adapted with a catastrophically tacky neon retrofit. Its readable hierarchy is:

1. Sincere cream limestone/plaster architecture, mansard roof, dormers, chimneys, carved surrounds, balconies, plants, and the canonical window cat.
2. A monumental Green Fairy mural transitioning from Art Nouveau flowers into pixel blocks and circuit traces.
3. The carved Headphone Gentleman over the entrance, with industrial ear cups, green tubes, purple conduit, junction boxes, and vandal moustache.
4. A black stepped marquee with green `ABSINTHE`, purple `ARCADE`, token and invader marks, plus `LOSE YOUR MIND ONE TOKEN AT A TIME`.
5. Stained-glass doors, checkerboard threshold, exterior cabinet, awning, chalkboard, wall signage, lanterns, bollards, planters, bucket, and wet-cobble reflections.

The production method is Godot 4.4 HD-2D painted-box diorama: painted building faces on simple 3D massing, selected depth layers, and billboard/cutout props. It is painterly, not 32-bit pixel art.

### Interior

The interior is a grand historic amusement hall vandalized by the same green-and-purple retrofit. Warm amber lamps and respectable stone, ironwork, arched ceilings, mezzanine rails, and checkerboard flooring act as the visual straight man. Toxic neon, sticker-bombed cabinets, bad signs, spectral mist, and lagging mirror effects provide the corruption.

The main hall is organized around a monumental cracked absinthe-bottle bar/reservoir. Cabinet aisles form a readable loop around the bar rather than a random maze. A northern L-shaped wing compresses into denser, darker cabinet rows and houses both hidden sublocation entrances. Mismatched seating remains as edge dressing, including one discoverable bidet stool, but does not obstruct circulation.

Core interior landmarks:

- Entrance vestibule and checkerboard threshold.
- Token exchange and Backpack Girl's cabinet-side sitting spot on the primary route.
- Central bottle bar and seating ring.
- Twisted cabinet gallery.
- Rigged claw/prize alcove for the Sea-Monkeys (Mint #73) NFT, `item_sea_monkeys`. ~~for the Beer Pong Saint Relic~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd).
- Broken DDR maintenance bay and its concealed restroom door.
- Northern Time Crisis row and the green-curtain Taproom transition.
- Mirror corridor/shadow-puzzle segment.

## Linked Sublocation Boundaries

### The Absinthium Taproom

- Destination ID: `debaucheryville_brewery_absinthium_taproom_01`.
- Arcade-side entrance: north end, behind/adjacent to a cracked Time Crisis cabinet, marked by a breathing green velvet curtain, vapor leaking below it, and the brass warning plaque.
- It is visually discoverable from the Arcade after dark; Taproom-specific tour/opening requirements are evaluated by the destination.
- The Arcade package owns the curtain, approach path, discovery interaction, and transition node only.
- The Taproom file owns the Distortion Den, mirror maze, Dr. Vanek, Green Fairy Wisp, brewery stamp, signature brew, and all interior art.

### Claw Machine Maintenance Closet Restroom

- Destination ID: `debaucheryville_arcade_maintenance_closet_01`.
- Arcade-side entrance: maintenance door beside the broken DDR machine in the northern service recess.
- Unlock: insert three Arcade tokens into the broken DDR machine; access remains permanent afterward.
- The Arcade package owns the DDR token interaction, door exterior, unlock flag, and transition node only.
- The restroom file owns the cramped interior, graffiti, fixture gags, ICQ consequence, and bathroom-network progression.

## Quest and State Integration

- `Couchsurfing Chronicles`: Backpack Girl appears in the Arcade from 14:00–22:00 and drifts between the back area and hostel from 22:00–04:00. The Arcade binds her interaction; her profile and quest file own dialogue and four-state Herp routing.
- `Nothing Is Getting Through`: use `debaucheryville_npc_backpack_girl_01` and `backpack_girl_refused_while_infected`; do not duplicate rejection dialogue.
- `NFT Hunt`: the claw reward is Sea-Monkeys (Mint #73), `item_sea_monkeys`; acquisition state `sea_monkeys_obtained`. ~~the current reward is `Beer Pong Saint Relic`; `Sea-Monkeys` is struck legacy text and must not become an item~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd): the Beer Pong Saint Relic is the struck piece (2026-08-01 §7c) and must not become an item.
- `Brewery Tour`: the Arcade exposes the Taproom entrance; the Taproom evaluates tour credentials and grants its own items.
- `Club Flyers`: the entrance has a flyer-placement interaction and Arcade Employee reaction binding.
- `VIP Wristbands`: a fake Arcade VIP claim may be referenced, but the location must not create a real VIP section.

## File Responsibilities

- `core`: identity, access, exits, mood, visual theme, satire, state flags, and performance intent.
- `environment`: audio, lighting, time/weather states, particles, environmental storytelling, and accessibility fallbacks.
- `interactions`: cabinet games, token exchange, claw machine, hidden-entry discovery/unlocks, flyer placement, examinations~~, and narrator bindings~~ struck (no-narrator ruling, Eurobound-2pie).
- `items`: Arcade tokens, Sea-Monkeys (Mint #73) (`item_sea_monkeys`) ~~Beer Pong Saint Relic~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd), broken Game Boy, Ballad of the Bros reference, and non-item unlock rewards. Destination-owned brewery/restroom rewards remain references only.
- `location_nodes`: image-generation-ready spatial plan, node connections, landmarks, occlusion/read-through notes, and both outbound transition nodes.
- `npcs`: Backpack Girl, Arcade Employee, token attendant/bartender role, ambient hackers, EDM ghosts, rogue backpackers, and speedrunner callbacks.
- `PNG_Assets`: HD-2D exterior/interior face art, depth layers, props, characters, UI, states, masks, and linked-entrance visibility requirements.
- `sprite_mapping`: filenames/IDs, frames, world/depth placement roles, lighting overlays, UI mappings, and optimization groupings.

## Validation

- All seven JSON files parse.
- Every file uses `debaucheryville_clocktower_arcade_01` as the Arcade location ID.
- Both destination IDs appear in core exits and location nodes.
- The DDR unlock cost is exactly three tokens.
- Sea-Monkeys (Mint #73) (`item_sea_monkeys`, `sea_monkeys_obtained`) is present and the Beer Pong Saint Relic is absent. ~~`Beer Pong Saint Relic` is present and `Sea-Monkeys` is absent.~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd).
- No file describes either linked sublocation's interior as part of the Arcade.
- PNG and sprite-mapping documents describe the approved painterly HD-2D pipeline, not a pure pixel-art tileset.
