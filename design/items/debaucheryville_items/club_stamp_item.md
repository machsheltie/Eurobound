# Item Definition: Club Stamp

*"PENDING (author). The source glosses it only as: temporary VIP access" - `design/quests/debaucheryville/club_flyers.md:210`*

> **Reverse-documented draft, 2026-11-17 (Eurobound-gora).** Built from `design/templates/consumable_item_template.md`. Filled ONLY from `design/quests/debaucheryville/club_flyers.md` and the rulings ledger, each quoted with file:line. Everything the source does not give is **PENDING** and is on the Eurobound Desk as `Eurobound-gora-q1`. Nothing here is registered in engine data.

**Source, verbatim** (`design/quests/debaucheryville/club_flyers.md:209-210`, "Rewards - Path A"):

> - Honest Promo → Bravado +1, SOVS reward, minor VIP access.
> - Honest: “Club Stamp” consumable (temporary VIP access).

**Why it ships** (ledger, `docs/superpowers/NEXT_WORK.md:872`, author on the bead page, Eurobound-e4bh, 2026-11-13): "Both apply: the old lines are extra rewards/flavor on top of canon". The two "Honest" lines are among those old lines (`club_flyers.md:562`).

## 📋 Item Identity
- **Item ID**: `item_club_stamp` (unique: no other hit in the repo)
- **Engine Key**: `club_stamp` (not registered; `consumables.json` untouched)
- **Display Name**: Club Stamp (unique as a full name; see "Near names" below)
- **Subtitle / Product Line**: PENDING
- **Internal Name**: PENDING (the source says only "consumable", `club_flyers.md:210`)
- **Item Type**: Consumable (source: "“Club Stamp” consumable", `club_flyers.md:210`)
- **Subtype**: PENDING
- **Rarity**: PENDING
- **Vendor / Source**: Quest reward, Club Flyers ("Peak Y2K Marketing Genius", `debaucheryville_sidequest_club_flyers_01`), Path A "Web 1.0 Marketing Mastery" only (`club_flyers.md:201-210`). Quest giver Vape Witch Vanessa (`debaucheryville_npc_vape_witch_vanessa_01`, per `docs/superpowers/specs/2026-11-17-club-flyers-quest-draft.json`).
- **Location**: Velvet Curtain Club, Debaucheryville (quest location, `club_flyers.md:7-8`); where the stamp is handed over is PENDING.

**Near names (distinct items, not this one):** "Lucky Club Stamp (Fake)", 8 SOVS, "+5 Confidence, no actual effect", "Placebo power" (`design/worlds/debaucheryville/midnight_munchies_general_store.md:169`); "Club Stamp Collection Book", 20 SOVS (`design/worlds/debaucheryville/neon_and_chrome_boutique.md:170`); "Club Stamp Collection (Access to VIP areas)" (`design/worlds/debaucheryville/debaucheryville.md:109`); the status "Club Stamped: Proof of venue visits, unlocks insider knowledge" (`debaucheryville.md:136`).

---

## 🎭 The Deception

### What It Actually Is
PENDING (author). The source gives no description beyond "temporary VIP access" (`club_flyers.md:210`).

### What The Bros Believe It Is
"PENDING (author): the source gives no bro line about the stamp."

### The Comedy Gap
PENDING. The quest's own gap (`club_flyers.md:16-24`): the bros think their "dot-com era business knowledge" is cutting-edge; Vanessa just needs cheap labor to poster the city.

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | Not sold (quest reward, `club_flyers.md:210`) |
| **Actual Value** | PENDING |
| **Resale Value** | PENDING |
| **Can Be Sold** | PENDING |
| **Stack Size** | PENDING |
| **Bundle Deals** | None (quest reward) |

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."
>
> "It can go as dark comedy, dirty, and unfamily friendly as it likes as this is an MA game."

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | PENDING | PENDING (Desk `Eurobound-gora-q1`) |

---

## 📣 Vendor Pitch Copy

### Pitch
```
None: quest reward, not sold.
```

### Purchase Line
> PENDING: the source writes no hand-over line (Vanessa's payment scene is not written either; see Desk `Eurobound-3ddh-q1`, step 5a).

---

## 📊 Effects on Use

| Effect | Value | Duration | Stack Rule | Notes |
|--------|-------|----------|------------|-------|
| HP restored | PENDING | — | — | `heal_hp` |
| Bravado restored | PENDING | — | — | `heal_bravado`. Not the Path A "+1 Bravado" (`club_flyers.md:209`), which is a quest reward already ruled to stack with the +2 (`club_flyers.md:212`, Desk `Eurobound-e4bh-q1`). |
| VIP access | "temporary VIP access" (`club_flyers.md:210`) | PENDING ("temporary") | PENDING | What it opens is PENDING. Same Path A list: "minor VIP access" (`club_flyers.md:209`); whether that is this stamp or a separate reward is PENDING. |

### Interaction With Other Statuses
| Existing Status | What Happens |
|-----------------|--------------|
| "VIP Status" ("+Access to exclusive areas, +Respect from bouncers", `debaucheryville.md:132`) | PENDING: whether the stamp grants this status. |
| Velvet Curtain Club VIP Stall Bravado gate ("Bravado check required to bypass buffed-out bouncers", `design/worlds/debaucheryville/velvetcurtainclubvipstall.md:16`) | PENDING: whether the stamp gets the bros past it. |

### What It Does NOT Do
- ❌ PENDING

---

## 🍺 Intoxication Review

Not intoxicating (source: a club stamp giving "temporary VIP access", `club_flyers.md:210`; no drink or drug named).

---

## ⚙️ Engine Fields (`consumables.json`)

Not registered (Eurobound-gora: no engine data changes). Fields known from the source:

```json
"club_stamp": {
  "display_name": "Club Stamp",
  "heal_hp": null,
  "heal_bravado": null,
  "description": "PENDING",
  "_pending": "effect, duration, value and description: Eurobound Desk Eurobound-gora-q1"
}
```

| Field | Required | Read by | Value |
|-------|----------|---------|-------|
| `display_name` | yes | data_repo / UI | Club Stamp |
| `heal_hp` | yes | `battle_core.gd` | PENDING |
| `heal_bravado` | yes | `battle_core.gd` | PENDING |
| `description` | yes | UI | PENDING |
| `usable_in` | optional | `game_state.gd`, `intoxicant.gd` | PENDING |
| `max_stack` | optional | `game_state.gd`, `intoxicant.gd` | PENDING |
| `source` | optional | data only | `debaucheryville_sidequest_club_flyers_01` (Path A) |
| **Fields the schema does not have yet** | | | A timed VIP-access effect: no field for it exists. Proposed engineering work once the effect is ruled. |
| **Registered** | | | No |

---

## 🖼️ Physical description (icon art brief)

PENDING: written by the Writers' Room and approved on the Desk (rule: Desk `Eurobound-rpac-q1`). The source gives no look.

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | PENDING |
| **Design** | PENDING |
| **Text/Markings** | PENDING |
| **Color/Finish** | PENDING |
| **States** | PENDING |
| **Filename** | not yet specced |

---

## 🔗 Quest Hooks

| Hook | Quest / File | Reader (who or what reads it) | Flag | Status |
|------|--------------|-------------------------------|------|--------|
| Given on Path A completion | `design/quests/debaucheryville/club_flyers.md:201-210` | quest script | PENDING (markers on Desk `Eurobound-3ddh-q1`) | Canon (the reward); flag PENDING |
| Opens "temporary VIP access" | PENDING | PENDING | PENDING | PENDING |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item ID and engine key unique across the repo (grep) | ☑ |
| Display name unique across the game (real brands keep real names) | ☑ (near names listed above) |
| No real city or place names in player-facing text | ☑ (none written) |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna, no bare numbers | ☑ (not sold) |
| Deception written: actual vs believed vs gap | ☐ PENDING |
| Inspect microcopy written, short, funny, and junk items included | ☐ PENDING |
| Effects, durations and stack rules specified (or marked PROPOSED) | ☐ PENDING |
| Intoxication review complete (if intoxicating) | ☑ (not intoxicating) |
| A real cost pays for every benefit | ☐ PENDING |
| Engine fields match the live `consumables.json` schema | ☐ not registered |
| Quest hooks name their readers | ☐ PENDING |
| Every unruled field marked PROPOSED | ☑ (marked PENDING; nothing proposed) |
| Comedy value preserved at full strength | ☐ PENDING (no text written) |
| Bros never achieve self-awareness, fear or disgust | ☑ (no text written) |

---

## 🚫 Warnings & Restrictions

### Content
- [x] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke
- [x] No sanitized version, no safe-build swap, no softened synonym
- [x] The only ceiling is no nudity
- [x] The bros stay willing and delusional; the consequences stay funny

### Crypto
- [x] Not a crypto item

---

## 📝 Development Notes

- Open for the author (Desk `Eurobound-gora-q1`): what "temporary VIP access" opens and for how long; whether "minor VIP access" (`club_flyers.md:209`) is this stamp; value, inspect text, look.
- Not asked here: Path A's SOVS amount (Desk `Eurobound-z39e-q1`); quest step markers (Desk `Eurobound-3ddh-q1`).

---

## 🔧 Development Status

- **Status**: Concept (reverse-documented; identity PENDING)
- **File Location**: `design/items/debaucheryville_items/club_stamp_item.md`
- **Registered In**: `consumables.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Reverse-documented from `club_flyers.md` (Eurobound-gora) | writer agent |
