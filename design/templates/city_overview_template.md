# [CITY NAME]

## Theme: [Two- or three-word theme] — "[The city's tagline, played straight]"

> **Template Version 1.0 — created 2026-11-11 at the author's request; pending author review**

<!--
HOW TO USE THIS TEMPLATE
This is the CITY OVERVIEW: the one hub doc per city that indexes everything in it.
It lives at design/worlds/[city]/[city].md. Worked examples:
design/worlds/shamsterdam/shamsterdam.md (most complete) and
design/worlds/sinfonia/sinfonia.md.

The overview is an index, not the content. Every building, NPC, enemy, quest, item and
host gets its own doc from its own template; the overview names it in a line or two and
links to it.

Rules that apply while filling it in:
- Read .claude/CLAUDE.md, design/narrative/Synopsis.md and the eurobound-satire-voice
  skill first.
- THE STORY BELONGS TO THE AUTHOR. A new city, its theme, boss, districts and any story
  tie need author rulings before they are written. This template holds structure only;
  never fill a section by invention. Anything drafted without a ruling is PROPOSED.
- Parody names only in player-facing text. The real-world inspiration may appear ONLY in
  the internal field marked below and never anywhere a player can read it. Minted world
  names and exemptions live in the rulings ledger (docs/superpowers/NEXT_WORK.md).
- Replace every [bracketed placeholder]. Delete this comment block before publishing.
- Keep every H2 header (with its emoji) and every table's column shape exactly as here.
  Add city-specific H3s freely under any H2.
-->

## 📋 City Identity
- **City ID**: `[city_snake_case]`
- **Display Name**: [Parody name — unique across the game]
- **Real-World Inspiration (internal only, never player-facing)**: [City]
- **Satirical Core**: [One paragraph: the gap between what tourists THINK this city is and what it ACTUALLY is.]
- **What The Bros Expect**: "[In their words. They came for exactly this; never afraid, never disgusted.]"
- **What The City Delivers**: [In spades, with consequences.]
- **Entry / Unlock**: [How and when the party arrives — author ruling]

---

## 🗺️ Streets & Districts

| District | One-Line Identity | Key Locations | Location Doc |
|----------|-------------------|---------------|--------------|
| [District name] | [What it is] | [Buildings in it] | `design/worlds/[city]/[district].md` or "none" |

### [District name]
- [Bullet: atmosphere, encounters, inspectable signage, mini-games]

---

## 🏛️ Buildings & Establishments

| Establishment | Type | Role (hub / shop / quest / vice venue / dungeon) | Location Doc |
|---------------|------|--------------------------------------------------|--------------|
| [Name] | [Bar / club / café / hostel / museum / etc.] | [Role] | `design/worlds/[city]/[location].md` |

Every establishment gets a doc from `location_validation_template.md`.

---

## 🧩 Scene Decomposition List

**Rule (author, 2026-11-14, binding):** `design/style_guides/location_interactables_rule.md`. Read it before filling this section.

**Mandatory interaction rule:** any object must be generated and tracked as a separate asset/prefab, not baked into the background, if any of these is true: the player can interact with it; the player can collide with it meaningfully; it changes state; it can be collected, examined, opened, activated, moved, destroyed or hidden; it is quest-relevant; it may recur in multiple locations; it may need animation, VFX or sound hooks; it may need UI prompt or tooltip support. If none apply, it may remain background dressing. The shorthand test: "Could game logic ever need to refer to this thing?" If yes, it is a separate asset.

List every visible item in the city's own scenes (streets, districts), one row each. Each establishment's list lives in its own location doc. Class is exactly one of: architectural shell / non-interactive prop / interactive prop / pickup-collectible / NPC anchor / FX-VFX anchor / UI-trigger point.

| Item | Class | Baked or separate | Location-file entry / interaction ID |
|------|-------|-------------------|--------------------------------------|
| [Visible item] | [One of the seven classes] | [Baked / Separate] | [Location data file entry and interaction ID, or "none" for baked shell] |

---

## 🛍️ Shops & Vendors

| Shop / Vendor | Stock Type | Price Range | Vendor NPC | Doc |
|---------------|------------|-------------|------------|-----|
| [Name] | [Equipment / consumables / services / darknet] | [X–Y SOVS] | [NPC name] | `[path]` |

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Stock rows follow the row specs in `consumable_item_template.md` and `equipment_template.md`.

---

## 🍺 Breweries (4 per city)

| # | Brewery | Signature Beer | Opener | Stamp | Status |
|---|---------|----------------|--------|-------|--------|
| 1 | [Name] | `[beer doc]` | `[opener doc]` | `[stamp doc]` | [Done / Owed] |
| 2 | [Name] | | | | |
| 3 | [Name] | | | | |
| 4 | [Name] | | | | |

Beers, openers and stamps use `signature_beer_item_template.md`, `opener_item_template.md` and `stamp_item_template.md`.

---

## ⚙️ Deeper Mechanics & Systems

| System | What It Does | Spec Doc | Status |
|--------|--------------|----------|--------|
| [City-specific system] | [One line] | `[path]` | [Author-ruled / PROPOSED] |

### City-Specific Status Effects
| Status | Effect Summary | Master List Entry |
|--------|----------------|-------------------|
| "[Name]" | [One line] | [Yes / PROPOSED via `status_effect_template.md`] |

### Intoxication Hooks
[The city's drinking and drug landscape and where it hooks the law: which venues push which ladder steps (Buzzed → Beer Goggles → Shitfaced → Catastrophe) or drug statuses. Every new intoxication mechanic passes the 10-point review in `design/mechanics/intoxication_law.md` §8 in its own doc. Bros choose debauchery (`design/narrative/bros_choose_debauchery.md`); no intoxicant gives a free advantage.]

---

## 🎯 Key Encounters & Events

### Boss & Villains
| Villain | Tier | Venue | Villain Doc |
|---------|------|-------|-------------|
| [Name] | [Minor / Miniboss / City Boss] | [Venue] | `design/worlds/[city]/villains/[...].md` |

### Side Quests (all optional)
| Quest | Giver | Quest Doc |
|-------|-------|-----------|
| [Name] | [NPC] | `design/quests/[city]/[quest].md` |

### Special Encounters & Timed Events
- [Event, trigger, doc]

---

## 👾 Enemy Encounters

| Family | Enemy | One-Line Concept | Enemy Doc |
|--------|-------|------------------|-----------|
| [Street & District] | [Name] | [What it is vs what the bros think] | `design/worlds/[city]/enemies/[enemy].md` or "concept only" |

Each enemy gets a doc from `enemy_template.md` before it is statted.

---

## 👥 Key NPCs

| NPC | Role | Location | Profile |
|-----|------|----------|---------|
| [Name] | [Quest giver / vendor / ICQ contact / ambient] | [Venue] | `design/worlds/[city]/npcs/[Location_Name]/[npc].md` |

---

## 🛏️ Couchsurf Hosts

| Host | Venue | Four-State Routing Written | Entry |
|------|-------|----------------------------|-------|
| [Name] | [Venue] | [Yes / Owed] | `design/quests/[city]/couchsurfingchronicles[city].md` → [entry] |

Each host uses `couchsurf_host_template.md`.

---

## 🖼️ NFT Slots

| Slot | Route (where it is found) | Artwork Subject | NFT Doc | Counted in Collection? |
|------|---------------------------|-----------------|---------|------------------------|
| [#] | [Venue + method: QR mural / terminal / rigged mini-game / theft] | [90s/00s pop culture — never location-derived] | `[path]` or "copy owed (author)" | [Yes / bonus] |

NFT artwork is 90s/00s pop culture, never derived from the city. The route can be city-flavored; the artwork cannot. Card copy is the author's to write. Use `NFT_Template.md`.

---

## 📶 Wi-Fi Hotspots & Connectivity

| Hotspot | Location | What Happens There (save / ICQ / hints) |
|---------|----------|------------------------------------------|
| [Name] | [Venue] | [One line] |

---

## 🔗 Connections to Other Cities

| City | Connection | Callback / Recurring NPC |
|------|------------|--------------------------|
| [Parody city name] | [Route, rivalry, shared racket] | [NPC or gag] |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| City name, theme and story ties ruled by the author | ☐ |
| Real-world inspiration appears only in the internal field | ☐ |
| No real city or place names anywhere player-facing | ☐ |
| Every establishment, NPC, villain, quest and host links to its own doc (or is listed as owed) | ☐ |
| Scene decomposition list filled per `design/style_guides/location_interactables_rule.md` | ☐ |
| Four breweries listed | ☐ |
| Every couchsurf host has four-state routing (or is listed as owed) | ☐ |
| NFT artwork subjects are 90s/00s and not location-derived | ☐ |
| All prices in SOVS | ☐ |
| All side quests optional | ☐ |
| All names funny and unique across the game | ☐ |
| Every unruled item marked PROPOSED | ☐ |

---

## 🚫 Warnings & Restrictions

### Content
- [ ] No narrator, disclaimer, moral framing, or any device that explains the joke; the city never winks at the player
- [ ] Full-strength MA satire; no sanitized version, no safe-build swap. The only ceiling is no nudity. Sex happens and is never shown
- [ ] Satire is sharp and specific — the bros' delusion AND the city's culture are both fair game (author ruling 2026-08-03: no punch-direction rules)
- [ ] NPCs, venues and enemies are never boring, corporate or professional
- [ ] The bros are never afraid, disgusted, self-aware or scam-aware. They came for all of this
- [ ] No mascots: no pets, puppets, named companion objects or fourth party members (ambient animals only where the author rules them in, logged in the ledger)
- [ ] Parody names for every place; real brands, products, games and songs keep their real names

### Money & Crypto
- [ ] All money is SOVS ("40 SOVS", "1 SOV"); never euros, the € glyph or koruna
- [ ] Crypto content conforms to `design/economy/economy_system.md`; coins only from `design/economy/shitcoin_master_pool.md`

---

## 📝 Development Notes

- [Open rulings for the author]
- [Docs owed]

---

## 🔧 Development Status

- **Status**: [Concept / Drafted / Author-Approved / In Production]
- **File Location**: `design/worlds/[city]/[city].md`
- **Location Index**: `design/worlds/[city]/[city]_locations_index.md` [if one exists]
- **Engine Data**: `game/assets/data/locations/[city]/` [Yes/No]

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial overview | [name] |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Spine drawn from the 2026-11-11 template audit (section B2) and the four existing overviews, chiefly `design/worlds/shamsterdam/shamsterdam.md` and `design/worlds/sinfonia/sinfonia.md`.*
