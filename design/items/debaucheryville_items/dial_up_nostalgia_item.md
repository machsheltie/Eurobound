# Item Definition: Dial-Up Nostalgia

*"PENDING (author). The source gives: NPCs ask if you need help using modern technology" - `design/quests/debaucheryville/club_flyers.md:204`*

> **Reverse-documented draft, 2026-11-17 (Eurobound-gora).** Built from `design/templates/equipment_template.md` (the nearest fit for a trinket: "other accessories"; no trinket slot or template exists). Filled ONLY from `design/quests/debaucheryville/club_flyers.md` and the rulings ledger, each quoted with file:line. Everything the source does not give is **PENDING** and is on the Eurobound Desk as `Eurobound-gora-q1`. Nothing here is registered in engine data.

**Source, verbatim** (`design/quests/debaucheryville/club_flyers.md:204`, "Rewards - Path A"):

> - **"Dial-Up Nostalgia" trinket** - NPCs ask if you need help using modern technology

## 📋 Item Identity
- **Item ID**: `item_dial_up_nostalgia` (unique: no other hit in the repo)
- **Engine Key**: `dial_up_nostalgia` (not registered; `equipment.json` untouched)
- **Display Name**: Dial-Up Nostalgia (unique as an item name; the phrase "dial-up nostalgia" also appears in prose in `design/worlds/debaucheryville/PNG_Assets/Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md:537`)
- **Internal Name**: PENDING. The name is all the source gives; what the object is is PENDING.
- **Item Type**: Equipment (the source says "trinket", `club_flyers.md:204`)
- **Slot**: PENDING (no trinket slot exists; the template's nearest is accessory)
- **Equippable By**: PENDING
- **Rarity**: PENDING
- **Source**: Quest reward, Club Flyers ("Peak Y2K Marketing Genius", `debaucheryville_sidequest_club_flyers_01`), Path A "Web 1.0 Marketing Mastery" only (`club_flyers.md:201-204`)
- **Location**: Debaucheryville

---

## 🎭 The Deception

### What It Actually Is
PENDING (author).

### What The Bros Believe It Is
"PENDING (author)." The quest's belief, verbatim (`club_flyers.md:17-18`): "Finally, someone recognizes their dormant marketing brilliance from their college days."

### The Comedy Gap
PENDING (internal).

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | Not sold (quest reward, `club_flyers.md:204`) |
| **Actual Value** | PENDING |
| **Resale Value** | PENDING |
| **Can Be Sold** | PENDING |
| **Can Be Dropped** | PENDING |

---

## 📊 Stats & Effects

### Stat Block
| Stat | Change | Notes |
|------|--------|-------|
| `max_hp` | PENDING | The source gives no stats. |
| `max_bravado` | PENDING | Not the Path A "+2 Bravado", which is its own reward line (`club_flyers.md:205`). |
| `offense` | PENDING | |
| `defense` | PENDING | |
| `speed` | PENDING | |
| `charm` | PENDING | |
| `luck` | PENDING | |
| `grit` | PENDING | |

### Passive / Special Effect
| Effect | Trigger | Value | Notes |
|--------|---------|-------|-------|
| Tech-help offers | "NPCs ask if you need help using modern technology" (`club_flyers.md:204`) | PENDING | Which NPCs and when: PENDING. |

### Era Cringe (the drawback)
Source: NPCs asking if the bros "need help using modern technology" (`club_flyers.md:204`). Whether it has any cost beyond those lines is PENDING.

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

PENDING: written by the Writers' Room and approved on the Desk (rule: Desk `Eurobound-rpac-q1`). The source gives no look, and the name names a feeling, not an object.

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
| `display_name` | Dial-Up Nostalgia |
| `slot` | PENDING |
| `equippable_by` | PENDING |
| Stat deltas | PENDING (none in the source) |
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
| Stats use engine stat names (or marked PROPOSED) | ☐ PENDING (none in the source) |
| Era Cringe drawback pays for the bonus | ☐ PENDING |
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

- Open for the author (Desk `Eurobound-gora-q1`): what the object is, any stats, slot, the tech-help lines' reach, value, inspect text, look.

---

## 🔧 Development Status

- **Status**: Concept (reverse-documented; identity PENDING)
- **File Location**: `design/items/debaucheryville_items/dial_up_nostalgia_item.md`
- **Registered In**: `equipment.json` No (schema pending)
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Reverse-documented from `club_flyers.md` (Eurobound-gora) | writer agent |
