# Item Definition: Defaced Flyer

*"PENDING (author). The source gives: +1 Charm, +2 Bravado, but random NPCs heckle you" - `design/quests/debaucheryville/club_flyers.md:312`*

> **Reverse-documented draft, 2026-11-17 (Eurobound-gora).** Built from `design/templates/equipment_template.md` (the nearest fit for a trinket that carries stats: "other accessories"; no trinket slot or template exists). Filled ONLY from `design/quests/debaucheryville/club_flyers.md` and the rulings ledger, each quoted with file:line. Everything the source does not give is **PENDING** and is on the Eurobound Desk as `Eurobound-gora-q1`. Nothing here is registered in engine data.

**Source, verbatim** (`design/quests/debaucheryville/club_flyers.md:312`, Path B "Rewards"):

> - Slander: Trinket “Defaced Flyer” (+1 Charm, +2 Bravado, but random NPCs heckle you).

**Why it ships** (ledger, `docs/superpowers/NEXT_WORK.md:872`, author on the bead page, Eurobound-e4bh, 2026-11-13): "Both apply: the old lines are extra rewards/flavor on top of canon". The "Slander" Defaced Flyer trinket is one of those old lines (`club_flyers.md:562`).

## 📋 Item Identity
- **Item ID**: `item_defaced_flyer` (unique: no other hit in the repo)
- **Engine Key**: `defaced_flyer` (not registered; `equipment.json` untouched)
- **Display Name**: Defaced Flyer (unique; the quest's prose uses "defaced flyers" for the vandalised posters, `club_flyers.md:279, :283, :320`)
- **Internal Name**: PENDING. From the quest: one of rival DJ Hardstyle Hynek's flyers after the bros vandalise it (`club_flyers.md:216-242`).
- **Item Type**: Equipment (the source says "Trinket", `club_flyers.md:312`)
- **Slot**: PENDING (no trinket slot exists; the template's nearest is accessory)
- **Equippable By**: PENDING
- **Rarity**: PENDING
- **Source**: Quest reward, Club Flyers ("Peak Y2K Marketing Genius", `debaucheryville_sidequest_club_flyers_01`), Path B "Alpha Male Vandalism 2001" only (`club_flyers.md:216, :302-312`)
- **Location**: Debaucheryville (Hynek's flyers "around city", `club_flyers.md:232`)

---

## 🎭 The Deception

### What It Actually Is
PENDING (author). Path B, verbatim (`club_flyers.md:222-223`): "Vandalizing existing flyers with the artistic skill and maturity of middle schoolers from 1999."

### What The Bros Believe It Is
"PENDING (author)." Path B, verbatim (`club_flyers.md:219-220`): "\"Guerrilla marketing\" like they learned from watching Fight Club too many times."

### The Comedy Gap
PENDING (internal).

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | Not sold (quest reward, `club_flyers.md:312`) |
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
| `max_bravado` | +2 | Source: "+2 Bravado" (`club_flyers.md:312`). Which engine stat "Bravado" on gear maps to is PENDING. |
| `offense` | — | |
| `defense` | — | |
| `speed` | — | |
| `charm` | +1 | Source: "+1 Charm" (`club_flyers.md:312`) |
| `luck` | — | |
| `grit` | — | |

### Passive / Special Effect
| Effect | Trigger | Value | Notes |
|--------|---------|-------|-------|
| Heckling | "random NPCs heckle you" (`club_flyers.md:312`) | PENDING | Which NPCs, how often, and whether it does anything beyond lines: PENDING. |

### Era Cringe (the drawback)
Source: "but random NPCs heckle you" (`club_flyers.md:312`). What that costs in play is PENDING.

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

PENDING: written by the Writers' Room and approved on the Desk (rule: Desk `Eurobound-rpac-q1`). Canon the writer must use, verbatim from `club_flyers.md`:

- The vandalism (`:233-242`): "Deface them with era-appropriate vandalism"; "Add \"PWNED!\" to every flyer"; "Draw flame decals over his face"; "Write \"WASSSUUUUP!\" in speech bubbles"; "Add tribal tattoo designs over venue information"; "Bradley writes \"All Your Base Are Belong to Us\" thinking it's current"; "Chadwick adds \"BOOYAH!\" to everything"; "Lord Pilsner adds beer bottle stickers to Hynek's face"; "Bradley crosses out names and writes \"THIS SUCKS\" in block letters"; "Gel pens and correction fluid deployed like weapons of mass destruction".
- Tools (`:229`, `:251`): "I brought gel pens."; "adding flame decals with red gel pen".
- Later state (`:277`, `:320`): the graffiti artist adds "'CIRCA 2001' labels"; "Defaced flyers with \"CIRCA 2001\" labels added by graffiti artist".
- Development note (`:555`): "Defaced flyers should show progressive vandalism (more gel pen each time)".

Which of these the item copy shows is PENDING.

---

## 🎨 Sprite & Paper-Doll Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | PENDING |
| **On-Bro Appearance** | PENDING |
| **Per-Bro Variants** | PENDING |
| **Text/Markings** | PENDING (canon lettering candidates listed above; read and fix every word on generated art) |
| **Battle Sprite** | Not a weapon |
| **Filename** | not yet specced |

---

## ⚙️ Engine Fields (`equipment.json`)

Not registered: `equipment.json` has no ruled schema, and Eurobound-gora changes no engine data.

| Field | Value |
|-------|-------|
| `display_name` | Defaced Flyer |
| `slot` | PENDING |
| `equippable_by` | PENDING |
| Stat deltas | `charm` +1, Bravado +2 (stat key PENDING) |
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
| Era Cringe drawback pays for the bonus | ☐ heckling named in source; effect PENDING |
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

- Path B also gives the "Frosted Tips Vandal" trinket ("+2 Bravado, -2 Charm", `club_flyers.md:304`; `design/items/debaucheryville_items/frosted_tips_vandal_item.md`). Whether a bro can carry both at once depends on the slot question.
- Open for the author (Desk `Eurobound-gora-q1`): slot, what the heckling does, value, inspect text, look.

---

## 🔧 Development Status

- **Status**: Concept (reverse-documented; identity PENDING)
- **File Location**: `design/items/debaucheryville_items/defaced_flyer_item.md`
- **Registered In**: `equipment.json` No (schema pending)
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Reverse-documented from `club_flyers.md` (Eurobound-gora) | writer agent |
