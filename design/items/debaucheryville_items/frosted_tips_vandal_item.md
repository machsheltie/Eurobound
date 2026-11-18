# Item Definition: Frosted Tips Vandal

*"PENDING (author). The source gives: +2 Bravado, -2 Charm, NPCs call you \"nu-metal tourist\"" - `design/quests/debaucheryville/club_flyers.md:304`*

> **Reverse-documented draft, 2026-11-17 (Eurobound-gora).** Built from `design/templates/equipment_template.md` (the nearest fit for a trinket that carries stats: "other accessories"; no trinket slot or template exists). Filled ONLY from `design/quests/debaucheryville/club_flyers.md` and the rulings ledger, each quoted with file:line. Everything the source does not give is **PENDING** and is on the Eurobound Desk as `Eurobound-gora-q1`. Nothing here is registered in engine data.

**Source, verbatim** (`design/quests/debaucheryville/club_flyers.md:304`, Path B "Rewards"):

> - **"Frosted Tips Vandal"** trinket (+2 Bravado, -2 Charm, NPCs call you "nu-metal tourist")

## 📋 Item Identity
- **Item ID**: `item_frosted_tips_vandal` (unique: no other hit in the repo)
- **Engine Key**: `frosted_tips_vandal` (not registered; `equipment.json` untouched)
- **Display Name**: Frosted Tips Vandal (unique; "Frosted tips" also appears as a bro fashion crime, `club_flyers.md:385`)
- **Internal Name**: PENDING. The name is all the source gives; what the object is (a hair product, a badge, something else) is PENDING.
- **Item Type**: Equipment (the source says "trinket", `club_flyers.md:304`)
- **Slot**: PENDING (no trinket slot exists; the template's nearest is accessory)
- **Equippable By**: PENDING
- **Rarity**: PENDING
- **Source**: Quest reward, Club Flyers ("Peak Y2K Marketing Genius", `debaucheryville_sidequest_club_flyers_01`), Path B "Alpha Male Vandalism 2001" only (`club_flyers.md:216, :302-304`)
- **Location**: Debaucheryville

---

## 🎭 The Deception

### What It Actually Is
PENDING (author).

### What The Bros Believe It Is
"PENDING (author)." Path B, verbatim (`club_flyers.md:219-220`): "\"Guerrilla marketing\" like they learned from watching Fight Club too many times."

### The Comedy Gap
PENDING (internal).

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | Not sold (quest reward, `club_flyers.md:304`) |
| **Actual Value** | PENDING |
| **Resale Value** | PENDING |
| **Can Be Sold** | PENDING |
| **Can Be Dropped** | PENDING |

---

## 📊 Stats & Effects

### Stat Block
| Stat | Change | Notes |
|------|--------|-------|
| `max_hp` | — | |
| `max_bravado` | +2 | Source: "+2 Bravado" (`club_flyers.md:304`). Which engine stat "Bravado" on gear maps to is PENDING. |
| `offense` | — | |
| `defense` | — | |
| `speed` | — | |
| `charm` | -2 | Source: "-2 Charm" (`club_flyers.md:304`) |
| `luck` | — | |
| `grit` | — | |

### Passive / Special Effect
| Effect | Trigger | Value | Notes |
|--------|---------|-------|-------|
| Name-calling | NPCs call you "nu-metal tourist" (`club_flyers.md:304`) | PENDING | Which NPCs and when: PENDING. |

### Era Cringe (the drawback)
Source: "-2 Charm" and NPCs calling the bros "nu-metal tourist" (`club_flyers.md:304`).

### What It Does NOT Do
- ❌ PENDING

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | PENDING | PENDING (Desk `Eurobound-gora-q1`) |

---

## 🖼️ Physical description (icon art brief)

PENDING: written by the Writers' Room and approved on the Desk (rule: Desk `Eurobound-rpac-q1`). The source gives no look. Nearby canon: "**Frosted tips** that somehow survived 20 years of bad decisions" (`club_flyers.md:385`); "Add tribal tattoo designs copied from nu-metal album covers" (`club_flyers.md:245`).

---

## 🎨 Sprite & Paper-Doll Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | PENDING |
| **On-Bro Appearance** | PENDING |
| **Per-Bro Variants** | PENDING |
| **Text/Markings** | PENDING |
| **Battle Sprite** | Not a weapon |
| **Filename** | not yet specced |

---

## ⚙️ Engine Fields (`equipment.json`)

Not registered: `equipment.json` has no ruled schema, and Eurobound-gora changes no engine data.

| Field | Value |
|-------|-------|
| `display_name` | Frosted Tips Vandal |
| `slot` | PENDING |
| `equippable_by` | PENDING |
| Stat deltas | `charm` -2, Bravado +2 (stat key PENDING) |
| `description` | PENDING |
| **Registered** | No |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item ID and engine key unique across the repo (grep) | ☑ |
| Display name unique across the game (real brands keep real names) | ☑ |
| Slot and equippable bros stated | ☐ PENDING |
| No real city or place names in player-facing text | ☑ (none written) |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna | ☑ (not sold) |
| Deception written: actual vs believed vs gap | ☐ PENDING |
| Stats use engine stat names (or marked PROPOSED) | ☐ Bravado key PENDING |
| Era Cringe drawback pays for the bonus | ☑ (-2 Charm and the name-calling, from the source) |
| Inspect microcopy written, short and funny | ☐ PENDING |
| Intoxication hook and 10-point review done (if it touches drinking or drugs) | ☑ (does not apply) |
| Every unruled field marked PROPOSED | ☑ (marked PENDING; nothing proposed) |
| Comedy value preserved at full strength | ☐ PENDING (no text written) |
| Bros never achieve self-awareness, fear or disgust | ☑ (no text written) |

---

## 🚫 Warnings & Restrictions

### Content
- [x] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke; nothing winks at the player
- [x] Full-strength MA satire; no sanitized version, no safe-build swap, no softened synonym. The only ceiling is no nudity
- [x] Satire is sharp and specific
- [x] No mascots
- [x] Funny, unique name; no real place names in player-facing text

### Crypto
- [x] Not a crypto item

---

## 📝 Development Notes

- An older audit lists this item with the same numbers ("+2 Bravado, -2 Charm", `docs/superpowers/sidequest_audit_new_elements_needed.md:111`); the quest doc is the source.
- Path B also gives the "Defaced Flyer" trinket (`design/items/debaucheryville_items/defaced_flyer_item.md`). Whether a bro can carry both depends on the slot question.
- Open for the author (Desk `Eurobound-gora-q1`): what the object is, slot, the name-calling's reach, value, inspect text, look.

---

## 🔧 Development Status

- **Status**: Concept (reverse-documented; identity PENDING)
- **File Location**: `design/items/debaucheryville_items/frosted_tips_vandal_item.md`
- **Registered In**: `equipment.json` No (schema pending)
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Reverse-documented from `club_flyers.md` (Eurobound-gora) | writer agent |
