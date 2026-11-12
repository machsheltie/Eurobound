# Absinthe Arcade Location Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a canon-reconciled eight-file Absinthe Arcade design package matching the established Debaucheryville location structure.

**Architecture:** Seven focused JSON files share one location ID and cross-reference stable object, node, NPC, item, and destination IDs. One Markdown art specification binds those data files to the approved Godot 4.4 painterly HD-2D exterior/interior pipeline while keeping linked sublocation interiors independently owned.

**Tech Stack:** JSON, Markdown, Godot 4.4 content conventions, painterly HD-2D painted-box diorama assets

**Spec:** `docs/superpowers/specs/2026-11-02-absinthe-arcade-location-package-design.md`

## Global Constraints

- Arcade location ID is exactly `debaucheryville_clocktower_arcade_01`.
- Taproom destination ID is exactly `debaucheryville_brewery_absinthium_taproom_01`.
- Restroom destination ID is exactly `debaucheryville_arcade_maintenance_closet_01`.
- The DDR restroom unlock costs exactly three Arcade tokens and is permanent.
- Sea-Monkeys (Mint #73) (`item_sea_monkeys`, `sea_monkeys_obtained`) is the claw reward; the Beer Pong Saint Relic is struck (2026-08-01 §7c). ~~`Beer Pong Saint Relic` is current canon; `Sea-Monkeys` is struck legacy content.~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd).
- The newer `design/Quests/debaucheryville/` files own current quest state and dialogue.
- Linked sublocation interiors remain in their dedicated Markdown files.
- Art direction is painterly Godot 4.4 HD-2D, not a pure pixel-art tileset.
- Preserve existing unrelated working-tree changes.

## Review Focus

- Cross-file IDs: every exit, node, interaction, NPC, and item reference must resolve to the same spelling.
- Boundary leakage: Arcade files may show entry cues but must not specify Taproom or restroom interior assets.
- Quest drift: use current Sea-Monkeys claw-NFT ~~Beer Pong Saint~~ (struck (author, NEXT_WORK.md:597; Eurobound-ukxd)) and Backpack Girl routing, not superseded quest text.
- Image-generation clarity: both hidden entrances must have unambiguous position, landmark, state, and visual cue descriptions.
- Pipeline drift: the PNG and mapping files must reflect painted faces/depth cards/billboards and avoid obsolete 32-bit-only assumptions.

---

### Task 1: Core Identity and Environmental State

**Files:**
- Create: `design/World Design/Debaucheryville/core/absinthe_arcade_core.json`
- Create: `design/World Design/Debaucheryville/environment/absinthe_arcade_environment.json`

**Interfaces:**
- Consumes: design spec, existing `*_core.json` and `*_environment.json` schemas, finalized exterior manifest.
- Produces: canonical location ID, exit IDs, global state flags, palette, time states, audio/lighting/FX IDs used by later files.

- [ ] **Step 1: Create the core JSON in the established schema**

Include identity, always-open access, token gating for games, two explicit sublocation exits, dignified-historic-versus-tacky-retrofit visual hierarchy, satire, state flags, and HD-2D performance intent.

- [ ] **Step 2: Parse the core JSON and assert required destinations**

Run a PowerShell `ConvertFrom-Json` check asserting the Arcade location ID and both destination IDs.

- [ ] **Step 3: Create the environment JSON in the established schema**

Define layered chiptune/venue ambience, time-of-day changes, green/purple/amber lighting, controlled fog/sparks/digital artifacts, mirror-lag accessibility fallback, weather read-through at the threshold, and permanent/dynamic storytelling details.

- [ ] **Step 4: Parse both JSON files and assert their shared location ID**

Expected: both parse without error and equal `debaucheryville_clocktower_arcade_01`.

- [ ] **Step 5: Commit**

Commit only the two Task 1 files with message `docs: define Absinthe Arcade core environment`.

### Task 2: Spatial Graph and Player Interactions

**Files:**
- Create: `design/World Design/Debaucheryville/location_nodes/absinthe_arcade_location_nodes.json`
- Create: `design/World Design/Debaucheryville/interactions/absinthe_arcade_interactions.json`

**Interfaces:**
- Consumes: Task 1 exit/state IDs and the spec's landmark layout.
- Produces: stable node and interaction IDs used by NPC, item, PNG, and sprite-mapping files.

- [ ] **Step 1: Create the location-node graph**

Model the exterior threshold, vestibule, token/Backpack Girl node, central bottle bar, cabinet loop, claw alcove, mirror corridor, northern wing, DDR maintenance recess, Taproom curtain, and both transitions. Include image-generation descriptions, sightlines, landmark orientation, and node connections.

- [ ] **Step 2: Parse the graph and assert both destination nodes exist**

Expected: transition nodes resolve to the two exact destination IDs, and the northern wing connects to both without making either destination part of the Arcade interior.

- [ ] **Step 3: Create the interactions JSON**

Define token exchange, three cabinet parodies, rigged claw flow, three-token DDR unlock, Taproom curtain discovery, flyer placement, Backpack Girl quest binding, mirror/shadow puzzle, and examinable exterior/interior props. Store dialogue ownership as references where quests/profiles are authoritative.

- [ ] **Step 4: Parse and assert unlock/current-canon values**

Expected: DDR cost is `3`, restroom unlock is permanent, claw reward ID is `item_sea_monkeys` (Sea-Monkeys (Mint #73)), and no Beer Pong Saint Relic item exists. ~~claw reward ID is the Beer Pong Saint Relic, and no `Sea-Monkeys` string exists.~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd).

- [ ] **Step 5: Commit**

Commit only the two Task 2 files with message `docs: map Absinthe Arcade nodes interactions`.

### Task 3: Items and NPC Population

**Files:**
- Create: `design/World Design/Debaucheryville/items/absinthe_arcade_items.json`
- Create: `design/World Design/Debaucheryville/npcs/Absinthe_Arcade/absinthe_arcade_npcs.json`

**Interfaces:**
- Consumes: Task 1 state IDs and Task 2 node/interaction IDs.
- Produces: item/NPC IDs referenced by art and sprite mapping.

- [ ] **Step 1: Create the item catalog**

Specify Arcade tokens, Sea-Monkeys (Mint #73) (`item_sea_monkeys`) ~~Beer Pong Saint Relic~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd), broken Game Boy, and Ballad of the Bros as a quest-owned referenced collectible. Record destination-owned Taproom/restroom rewards as external references rather than Arcade inventory.

- [ ] **Step 2: Parse and check item canon**

Expected: `item_sea_monkeys` (Sea-Monkeys (Mint #73)) exists, no Beer Pong Saint Relic item does, and token value/economy matches the interaction file. ~~Expected: Beer Pong Saint exists, `Sea-Monkeys` does not, and token value/economy matches the interaction file.~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd).

- [ ] **Step 3: Create the NPC file**

Bind Backpack Girl to her existing profile and quest routing; define Arcade Employee, token attendant/bartender, ambient hacker, EDM ghost, rogue backpacker, and speedrunner ambient groups with schedules, nodes, sprite needs, and quest callbacks.

- [ ] **Step 4: Parse and check Backpack Girl ownership**

Expected: NPC ID is `debaucheryville_npc_backpack_girl_01`, four-state dialogue is referenced rather than duplicated, and her schedule includes the established Arcade hours.

- [ ] **Step 5: Commit**

Commit only the two Task 3 files with message `docs: define Absinthe Arcade items npcs`.

### Task 4: Art Requirements and Sprite Mapping

**Files:**
- Modify: `design/worlds/debaucheryville/PNG_Assets/Absinthe_Arcade_Complete_PNG_Asset_Requirements.md`
- Create: `design/World Design/Debaucheryville/sprite_mapping/absinthe_arcade_sprite_mapping.json`

**Interfaces:**
- Consumes: Tasks 1–3 IDs, exterior asset manifest, master component breakdown, and the approved interior layout.
- Produces: authoritative asset list and engine-facing mapping for every Arcade-visible landmark, state, NPC, prop, and FX layer.

- [ ] **Step 1: Replace obsolete pure-pixel requirements with the HD-2D package**

Document exterior painted faces, day/night/emission states, depth layers, street cutouts, interior hall faces/cards, central bar, cabinet sets, both hidden-entry exteriors, characters, UI, masks, accessibility states, naming, and delivery checks. Clearly link to the two destination Markdown files and exclude their interiors.

- [ ] **Step 2: Create the sprite-mapping JSON**

Map exterior/interior faces, depth cards, props, cabinet states, characters, UI, animations, lighting, node placement roles, and atlas/LOD groupings. Use asset IDs that match the PNG document and interactions.

- [ ] **Step 3: Parse mapping and verify pipeline terms**

Expected: JSON parses; the PNG document and mapping contain `Godot 4.4`, `HD-2D`, both linked destination IDs, and no claim that the hero façade is a 32-bit tile sheet.

- [ ] **Step 4: Commit**

Commit only the Task 4 files with message `docs: specify Absinthe Arcade HD2D assets`.

### Task 5: Cross-Package Validation

**Files:**
- Verify: all eight Absinthe Arcade package files

**Interfaces:**
- Consumes: all prior task outputs.
- Produces: one internally consistent, reviewable location package.

- [ ] **Step 1: Parse all seven JSON files in one command**

Expected: seven successful parses and no errors.

- [ ] **Step 2: Run cross-file invariant checks**

Assert the shared Arcade ID, exact linked destination IDs, three-token unlock, current NFT name, Backpack Girl ID, referenced quest ownership, and absence of the struck Beer Pong Saint Relic ~~absence of `Sea-Monkeys`~~ struck (author, NEXT_WORK.md:597; Eurobound-ukxd).

- [ ] **Step 3: Search for boundary and pipeline violations**

Confirm linked interiors are not duplicated, both entrance visuals are explicit, and obsolete pure-pixel wording is absent from the authoritative PNG/mapping files.

- [ ] **Step 4: Inspect the final diff**

Confirm only the two planning documents and eight requested package files changed as part of this work; preserve all pre-existing unrelated changes.

- [ ] **Step 5: Commit validation corrections if needed**

Commit only corrections to the eight package files with message `docs: validate Absinthe Arcade package`.
