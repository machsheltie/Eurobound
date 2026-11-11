# Item Definition: [Display Name]

*"[Satirical tagline: the shop's pitch or the bros' belief, played straight]" - [Who says it]*

> **Template Version 1.0 — created 2026-11-11 at the author's request; pending author review**

<!--
HOW TO USE THIS TEMPLATE
This template is for EQUIPMENT: anything a bro can equip and unequip through a slot.
Weapons, headgear, torso, legs, footwear, necklaces, rings, watches/bracelets, phones,
other accessories, and combo sets. If it can come off, it lives here.

- Permanently affixed items (wristbands, curses, tattoos) stay on permanent_item_template.md.
- Items that deplete when used stay on consumable_item_template.md.
- Brewery beers, openers and stamps keep their own brewery templates.

Headline gear (each bro's signature weapon, quest rewards, boss drops) gets its own doc.
Ordinary shop stock can live as rows in a location doc's equipment table, using the
"Shop Table Row Spec" columns at the bottom of this template.

Rules that apply while filling it in:
- Read .claude/CLAUDE.md and the eurobound-satire-voice skill first. Use the
  eurobound-item-creation skill to route and file the doc.
- Every price is SOVS ("40 SOVS", singular "1 SOV"), or an amount of one named coin
  from design/economy/shitcoin_master_pool.md. Never euros, never the € glyph.
- Item identity, slot, price and every stat number need an author ruling. Anything you
  draft that the author has not ruled on is marked PROPOSED, in the field itself.
- Stat names match the engine: max_hp, max_bravado, offense, defense, speed, charm,
  luck, grit (game/assets/data/party/party_members.json). Old docs use joke stats
  ("+5 Cool Factor", "+2 Office Drone Energy"); keep the joke in the flavor text and
  map the real effect onto an engine stat, or mark it PROPOSED.
- Replace every [bracketed placeholder]. Delete this comment block before publishing.
- Keep every H2 header (with its emoji) and every table's column shape exactly as here.
- Optional subsections say so in their heading. Omit them when they do not apply.
-->

## 📋 Item Identity
- **Item ID**: `item_[item_name_snake_case]` (doc ID; grep the repo to confirm it is unique)
- **Engine Key**: `[item_name_snake_case]` (the key in `game/assets/data/items/equipment.json`, no `item_` prefix)
- **Display Name**: [Item Name — real brand names keep their real names; invented gear gets a funny one]
- **Internal Name**: [What it actually is, in plain terms]
- **Item Type**: Equipment
- **Slot**: [weapon / head / torso / legs / feet / necklace / ring / watch-bracelet / phone / accessory / combo set]
- **Equippable By**: [Lord Pilsner / Chadwick / Bradley / any bro]
- **Rarity**: [Actual rarity] (bros think it's [Rarity bros believe])
- **Source**: [Shop + vendor NPC (`[npc_id]`) / quest reward / enemy drop / villain drop / found]
- **Location**: [Location, City — parody names only]

---

## 🎭 The Deception

### What It Actually Is
[The mundane, cheap, dated or broken reality. Specific: what it is made of, where it came from, which decade it belongs to.]

### What The Bros Believe It Is
"[The bros' delusion, in their own voice. What they think it says about them. They are never afraid, never disgusted, never scam-aware.]"

### The Comedy Gap
[One or two sentences, internal only. Never explain the joke in player-facing text.]

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | [X SOVS] or [X CoinName ($TICKER)] or "Not sold" |
| **Actual Value** | [X SOVS] |
| **Resale Value** | [X SOVS or "0 SOVS (worthless)"] |
| **Can Be Sold** | [Yes/No + why] |
| **Can Be Dropped** | [Yes/No + why] |

---

## 📊 Stats & Effects

### Stat Block
| Stat | Change | Notes |
|------|--------|-------|
| `max_hp` | [+/-X or —] | |
| `max_bravado` | [+/-X or —] | |
| `offense` | [+/-X or —] | |
| `defense` | [+/-X or —] | |
| `speed` | [+/-X or —] | |
| `charm` | [+/-X or —] | |
| `luck` | [+/-X or —] | |
| `grit` | [+/-X or —] | |

### Passive / Special Effect
| Effect | Trigger | Value | Notes |
|--------|---------|-------|-------|
| [Effect] | [Always / in battle / at hotspots / once per dungeon] | [Value] | [Status from `design/mechanics/Battle/status_effects.md`, or new and PROPOSED] |

### Era Cringe (the drawback)
[Every piece of gear pays for its bonus. The dated, embarrassing or physically inconvenient cost, and what it does in play: a stat penalty, an NPC reaction, a noise, a status. No piece of gear is a free advantage.]

### What It Does NOT Do
- ❌ [Thing the bros believe it does but doesn't]
- ❌ [Thing the bros believe it does but doesn't]

### Intoxication Hook (only if the gear touches drinking or drugs)
[Gear that dispenses, boosts or interacts with alcohol or drugs (a keg-tap club, a flask holster) follows `design/narrative/bros_choose_debauchery.md` and `design/mechanics/intoxication_law.md`: no free advantage, bounded loss of control, and the law's 10-point design review (§8) answered here before integration. Delete this subsection if it does not apply.]

---

## ⚔️ Weapon Details (weapons only — omit for armour and accessories)

| Attribute | Value |
|-----------|-------|
| **Weapon Class** | [Staff / club / paddle / thrown / etc.] |
| **Bro** | [Which bro's signature line this belongs to] |
| **Attack Style** | [Single target / line / AoE] |

### Battle Flavor Text
- "[Normal hit line]"
- "[Critical SMAAAASH line]"
- "[Miss line]"

### Signature Moves (if the weapon grants any; abilities use `ability_template.md`)
| Move | Effect | Ability Doc |
|------|--------|-------------|
| [Move name] | [What it does] | `[path or "PROPOSED"]` |

---

## ⬆️ Upgrade Path (optional)

| Stage | Display Name | How Obtained | Stat Change |
|-------|--------------|--------------|-------------|
| 1 | [Name] | [Starting / bought] | [Values] |
| 2 | [Name] | [Quest / vendor / materials] | [Values] |
| 3 | [Name] | [Source] | [Values] |

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Every piece of gear gets inspect text, junk most of all. One or two sentences that fit one text box. No moral, no warning label, no wink at the player.

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | "[Line]" | [Canon / PROPOSED] |
| 2 | "[Line]" | [Canon / PROPOSED] |

---

## 🎨 Sprite & Paper-Doll Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | [Size and shape] |
| **On-Bro Appearance** | [How it shows on the 128x128 bro sprite, per `design/style_guides/character_sprite_pipeline.md`; or "icon only"] |
| **Per-Bro Variants** | [Differences per bro, if any] |
| **Text/Markings** | [Exact text. Read and fix every word on generated art; AI misspellings are errors] |
| **Battle Sprite** | [Weapons: how it reads in battle] |
| **Filename** | [`snake_case_filename.png` or "not yet specced"] |

---

## ⚙️ Engine Fields (`equipment.json`)

`game/assets/data/items/equipment.json` is read by `game/core/data_repo.gd` (`get_equipment`) but has **no ruled schema yet** (the file is `{"equipment": {}}`). Fill in what this item needs; do not register it until the author rules the schema. The `eurobound-item-engine-sync` skill refuses to invent it.

| Field | Value |
|-------|-------|
| `display_name` | [Value] |
| `slot` | [Value — PROPOSED field] |
| `equippable_by` | [Value — PROPOSED field] |
| Stat deltas | [Values — PROPOSED field names match party stats] |
| `description` | [Short in-voice description. Keep the joke.] |
| **Registered** | [Yes/No — pending schema ruling] |

---

## 🗣️ Bro Lines on Equip (optional — include only once written or approved)

**Lord Pilsner**:
> "[Line]"

**Chadwick**:
> "[Line]"

**Bradley**:
> "[Line]"

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item ID and engine key unique across the repo (grep) | ☐ |
| Display name unique across the game (real brands keep real names) | ☐ |
| Slot and equippable bros stated | ☐ |
| No real city or place names in player-facing text | ☐ |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna | ☐ |
| Deception written: actual vs believed vs gap | ☐ |
| Stats use engine stat names (or marked PROPOSED) | ☐ |
| Era Cringe drawback pays for the bonus | ☐ |
| Inspect microcopy written, short and funny | ☐ |
| Intoxication hook and 10-point review done (if it touches drinking or drugs) | ☐ |
| Every unruled field marked PROPOSED | ☐ |
| Comedy value preserved at full strength | ☐ |
| Bros never achieve self-awareness, fear or disgust | ☐ |

---

## 🚫 Warnings & Restrictions

### Content
- [ ] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke; nothing winks at the player
- [ ] Full-strength MA satire; no sanitized version, no safe-build swap, no softened synonym. The only ceiling is no nudity
- [ ] Satire is sharp and specific — the bros' delusion AND the city's culture are both fair game (author ruling 2026-08-03: no punch-direction rules)
- [ ] No mascots: gear is never a pet, puppet, named companion object or emotional-support entity
- [ ] Funny, unique name; no real place names in player-facing text; real brands, products, games and songs keep their real names

### Crypto
- [ ] Crypto content conforms to `design/economy/economy_system.md`; coins come from `design/economy/shitcoin_master_pool.md`, never invented in an item file
- [ ] The vendor always knows exactly what the gear is worth; the bros never do

---

## 📝 Development Notes

- [Implementation or asset dependency]
- [Open question for the author]

---

## 🔧 Development Status

- **Status**: [Concept / Drafted / Reviewed / Sprites Commissioned / Implemented]
- **File Location**: `[routed path per the eurobound-item-creation skill: design/items/[city]_items/ or design/items/general_items/]`
- **Registered In**: `equipment.json` [Yes/No — schema pending author ruling]
- **Sprite**: [filename.png or "not yet specced"]

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial item doc | [name] |

---

## 🧾 Shop Table Row Spec (for equipment rows inside location docs)

Every equipment table in a location doc uses these columns, in this order:

| Item | Slot | Equippable By | Price | Stats | Era Cringe | Shopkeeper Comment |
|------|------|---------------|-------|-------|------------|--------------------|
| [Name] | [Slot] | [Bro(s)] | [X SOVS] | [+X defense, ...] | [Drawback] | "[Flavor line]" |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2) and `design/items/docs/equipment.md`, `design/characters/Bradley/bradleysweapons.md` and `design/worlds/debaucheryville/threads_and_treads.md`. Permanent items stay on `permanent_item_template.md`; consumables on `consumable_item_template.md`.*
