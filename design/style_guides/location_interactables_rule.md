# Location Interactables Rule

**Status: binding (author, 2026-11-14).** "And rules for interactable items within locations." It applies to every location built for the game, painted plates and 3D kits alike, and sits beside `reference_locked_texturing_protocol.md` and `3d_asset_rules.md`.

**Approved locations are reworked too (author, 2026-11-14, Desk `Eurobound-31uj-q1`):** "Looks like we will need to do the rework." The Absinthe Arcade plates are reworked to this rule, starting from the audit in `docs/superpowers/reports/2026-11-14-arcade-interactables-audit.md` (25 items painted in, 8 missing).

Work tracking: `Eurobound-31uj`.

## The core rule (author's text)

If agents are building usable game locations, anything the player can interact with must not exist only as painted or background geometry unless it is purely decorative. Location art is not "make one finished image and infer the rest". It is:

> environment shell + placed prop set + interactive asset list + stateful logic hooks

Every visible thing in a location belongs to one of four buckets.

### 1. Background / baked environment

Safe to be part of the building mesh or the wall and floor textures: plaster walls, ceiling beams, fixed trim, floor tiles, distant mural details, permanently built counters, non-interactive wall grime and stains.

### 2. Placed prop

A separate scene asset even when it is not interactive: stools, tables, arcade cabinets, lamps, trash cans, freestanding signs, bottles on shelves, hanging speakers, bathroom fixtures. They usually should not be baked into the background, because they may need collision, reuse in other rooms, independent lighting and shadow, later animation or interaction, or to move, swap, break or disappear in quest states.

### 3. Interactive object

Must be a separate asset **and** must be identified in the location data: a door the player enters, a lever/button/switch, a save point terminal, a lootable cabinet, a beer stamp station, a prize counter, a vending machine, a sink or toilet if used in gameplay, a special jukebox, a couchsurf bed trigger, a hidden switch, a quest pickup object.

Each needs: its own mesh or prefab, a location-file entry, an interaction ID, a collision or trigger, state logic, and often several visual states.

### 4. Pickup / inventory item

Usually exists as both a world prop version and an inventory/icon version: a wristband, key, bottle opener, quest clue, collectible NFT trigger object, special beer, dropped pager, a weird artifact on a shelf. If it can be picked up, examined, equipped or referenced by quests, it is not just painted into the room.

## Mandatory interaction rule (author's text)

Any object that meets **any** of these conditions must be generated and tracked as a separate asset/prefab, not baked into the background:

- the player can interact with it
- the player can collide with it meaningfully
- the object changes state
- the object can be collected, examined, opened, activated, moved, destroyed or hidden
- the object is quest-relevant
- the object may recur in multiple locations
- the object may need animation, VFX or sound hooks
- the object may need UI prompt or tooltip support

If none apply, it may remain background dressing.

**The shorthand test:** "Could game logic ever need to refer to this thing?" If yes, it is a separate asset.

Things often baked in by accident: doors, stools in front of counters, arcade cabinets, prize machines, wall phones, sinks, mirrors, graffiti hotspots, QR posters, bottle opener displays, special framed pictures, suspicious milk crates, hidden vents, save devices and Wi-Fi spots.

## Interactables are declared in the location files

Not just generated visually. They appear in the location's data: location core data, interactive elements, environmental interactions, sprite/asset mapping, and quest hooks or state logic where they apply. (In this repo: the per-location companion files under `design/worlds/<city>/` — core, interactions, environmental, items, npcs, events, sprite_mapping — and their engine copies under `game/assets/data/locations/`.)

## Two outputs for every location

**A. Scene decomposition list.** Every visible item, classified as one of: architectural shell, non-interactive prop, interactive prop, pickup/collectible, NPC anchor, FX/VFX anchor, UI/trigger point.

**B. Asset requirement list.** For each non-background item: asset name; asset type; reuse or unique; collision needed; interaction needed; state variations; animation needed; sound cue; quest dependency; inventory icon needed; material set needed.

## Example: Absinthe Arcade (author's text)

- **Fine to bake into architecture:** limestone wall texture, checkerboard floor, ceiling plaster, general bar front wood paneling, fixed wall molding.
- **Separate props:** arcade machines, bar stools, prize counter display, claw machine, skee-ball lane units, neon sign assemblies, DDR machine, bidet seat toilet, sink bank, mirror, bottle display.
- **Separate interactive assets:** redemption counter terminal, prize counter interaction point, specific arcade cabinets used in quests/minigames, bathroom stall doors if usable, hidden maintenance panel, save/Wi-Fi hotspot object, specific loot container, graffiti interaction point, bottle-opener collectible display, any NPC-owned workstation.

## In short

- Backgrounds can be flattened or baked.
- Props should usually be separate assets.
- Anything interactable is explicitly identified in the location files and generated as a usable asset, not painted into the building.
