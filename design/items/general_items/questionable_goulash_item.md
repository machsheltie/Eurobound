# Item Definition: Questionable Goulash

*"Simmering since the Velvet Revolution. Restores 40 HP."* - engine description (`game/assets/data/items/consumables.json:21`)

> **Source and status.** Bead Eurobound-4jln (reverse documentation of an engine entry). Short item doc per the author's ruling on Desk Eurobound-rpac-q2 (2026-11-15): "A: a short .md per item from its template". Built from `design/templates/consumable_item_template.md`.
> - **Sourced:** the name, the numbers and the description are copied from `game/assets/data/items/consumables.json:17-22`. The 3D icon was accepted by the author ("I think the goulash is fine tbh", commit 64ba918e; `game/assets/items/icons/3d/questionable_goulash_128.png`, `questionable_goulash_512.png`).
> - **Where it came from:** the entry was first written as vertical-slice scaffolding (`docs/superpowers/plans/2026-07-30-vertical-slice.md:293-298`), not from an author brief. No shop, drop or quest gives it out in data today.
> - **Not sourced:** every field below marked **PENDING (author)**. Nothing in this doc is invented, and nothing here changes engine data.
> - **Routing:** `general_items/` for now, because nothing in data or design ties it to a city. The asset team filed its icon commits under Debaucheryville, which is not a ruling. Its source (and so its folder) goes on the Eurobound Desk (`Eurobound-4jln-q1`).

## 📋 Item Identity
- **Item ID**: `item_questionable_goulash` (doc ID; grep 2026-11-17: no other use)
- **Engine Key**: `questionable_goulash` (`game/assets/data/items/consumables.json:17`)
- **Display Name**: Questionable Goulash (`consumables.json:18`)
- **Subtitle / Product Line**: PENDING (author)
- **Internal Name**: A goulash (from the name). Anything beyond that is PENDING (author)
- **Item Type**: Consumable
- **Subtype**: food (from the name and the HP heal; the entry has no `subtype` field)
- **Rarity**: PENDING (author)
- **Vendor / Source**: PENDING (author). No shop, drop or quest gives it out in data
- **Location**: PENDING (author)

---

## 🎭 The Deception

### What It Actually Is
"Simmering since the Velvet Revolution." (engine description, `consumables.json:21`). Anything beyond that is PENDING (author).

### What The Bros Believe It Is
PENDING (author).

### The Comedy Gap
PENDING (author).

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | PENDING (author) (the entry has no `price`) |
| **Actual Value** | PENDING (author) |
| **Resale Value** | PENDING (author) |
| **Can Be Sold** | PENDING (author) |
| **Stack Size** | PENDING (author) (the entry has no `max_stack`) |
| **Bundle Deals** | PENDING (author) |

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."
>
> "It can go as dark comedy, dirty, and unfamily friendly as it likes as this is an MA game."

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | "Simmering since the Velvet Revolution. Restores 40 HP." | Engine description (`consumables.json:21`); whether it stays: Desk `Eurobound-4jln-q1` |
| 2 | PENDING (author) | PENDING (author) |

---

## 📣 Vendor Pitch Copy

### Pitch
```
PENDING (author): no vendor in data.
```

### Purchase Line
> PENDING (author)

---

## 📊 Effects on Use

| Effect | Value | Duration | Stack Rule | Notes |
|--------|-------|----------|------------|-------|
| HP restored | 40 | Instant | — | `heal_hp` (`consumables.json:19`) |
| Bravado restored | 0 | Instant | — | `heal_bravado` (`consumables.json:20`) |
| Status applied | None | — | — | The entry applies no status |

### Interaction With Other Statuses
| Existing Status | What Happens |
|-----------------|--------------|
| None in data | PENDING (author) |

### What It Does NOT Do
- ❌ Nothing beyond the 40 HP heal is in data. Anything else is PENDING (author).

---

## 🍺 Intoxication Review

Not intoxicating (the entry has no `alcohol` or `intoxicant` field).

---

## ⚙️ Engine Fields (`consumables.json`)

Copied from `game/assets/data/items/consumables.json:17-22`, verbatim:

```json
"questionable_goulash": {
  "display_name": "Questionable Goulash",
  "heal_hp": 40,
  "heal_bravado": 0,
  "description": "Simmering since the Velvet Revolution. Restores 40 HP."
}
```

| Field | Required | Read by | Value |
|-------|----------|---------|-------|
| `display_name` | yes | data_repo / UI | Questionable Goulash |
| `heal_hp` | yes | `battle_core.gd` | 40 |
| `heal_bravado` | yes | `battle_core.gd` | 0 |
| `description` | yes | UI | Simmering since the Velvet Revolution. Restores 40 HP. |
| `alcohol` | optional | `game_clock.gd`, `navigation_roll.gd`, `game_state.gd` | omitted |
| `subtype` | optional | `status_table.gd` | omitted |
| `usable_in` | optional | `game_state.gd`, `intoxicant.gd` | omitted |
| `max_stack` | optional | `game_state.gd`, `intoxicant.gd` | omitted |
| `price` | optional | data only | omitted |
| `bundles` | optional | data only | omitted |
| `intoxicant` | optional | `intoxicant.gd`, `battle_core.gd` | omitted |
| `self_status_risk` | optional | `game_state.gd` | omitted |
| `revive_pct` | optional | `battle_core.gd` | omitted |
| `cures_status` | optional | `battle_core.gd` | omitted |
| `effect` | optional | data only | omitted |
| `source` | optional | data only | omitted |
| `_pending` | optional | ignored at run time | omitted |
| **Fields the schema does not have yet** | | | None needed for what is in data |
| **Registered** | | | Yes |

---

## 🖼️ Physical description (icon art brief)

PENDING (author). The 12-field description is the Writers' Room's to write and the Desk's to approve: `design/items/docs/physical_descriptions_tracker.md:17` has it in batch 2 ("no pot, stew or colour; 3 refs failed"). The icon was later accepted by the author (commit 64ba918e), so a description should match it.

| Field | Description |
|-------|-------------|
| **silhouette** | PENDING (author) |
| **scale_cue** | PENDING (author) |
| **materials_and_cheap_cues** | PENDING (author) |
| **colours** | PENDING (author) |
| **contents** | PENDING (author) |
| **decoration** | PENDING (author) |
| **condition** | PENDING (author) |
| **garnish_and_addons** | PENDING (author) |
| **palette_anchors** | PENDING (author) |
| **reads_at_icon_size** | PENDING (author) |
| **must_not_look_like** | PENDING (author) |
| **lettering** | PENDING (author) |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | 3D icon, built and accepted (`game/assets/items/icons/3d/questionable_goulash_128.png`, `questionable_goulash_512.png`) |
| **Design** | See the icon. Written description PENDING (author) |
| **Text/Markings** | PENDING (author) |
| **Color/Finish** | PENDING (author) |
| **States** | PENDING (author) |
| **Filename** | `questionable_goulash_128.png`, `questionable_goulash_512.png` |

---

## 🔗 Quest Hooks

| Hook | Quest / File | Reader (who or what reads it) | Flag | Status |
|------|--------------|-------------------------------|------|--------|
| None in data or design | — | — | none | PENDING (author) |

---

## 🗣️ Bro Lines on Use (optional — include only once written or approved)

None written or approved.

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item ID and engine key unique across the repo (grep) | ☑ (grep 2026-11-17) |
| Display name unique across the game (real brands keep real names) | ☑ (grep 2026-11-17) |
| No real city or place names in player-facing text | ☑ ("Velvet Revolution" is a historical event, not a place) |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna, no bare numbers | ☐ PENDING (author) (no price) |
| Deception written: actual vs believed vs gap | ☐ PENDING (author) |
| Inspect microcopy written, short, funny, and junk items included | ☐ PENDING (author) |
| Effects, durations and stack rules specified (or marked PROPOSED) | ☑ (from data; stack PENDING) |
| Intoxication review complete (if intoxicating) | ☑ (not intoxicating) |
| A real cost pays for every benefit | ☐ PENDING (author) |
| Engine fields match the live `consumables.json` schema | ☑ |
| Quest hooks name their readers | ☑ (none) |
| Every unruled field marked PROPOSED | ☑ (marked PENDING (author); nothing proposed) |
| Comedy value preserved at full strength | ☐ PENDING (author) |
| Bros never achieve self-awareness, fear or disgust | ☑ (no bro text) |

---

## 🚫 Warnings & Restrictions

### Content
- [ ] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke
- [ ] No sanitized version, no safe-build swap, no softened synonym
- [ ] The only ceiling is no nudity
- [ ] The bros stay willing and delusional; the consequences stay funny

### Crypto
- [ ] Coins come from `design/economy/shitcoin_master_pool.md`; no one-off coins invented in an item file
- [ ] Coin exchange rates come from the author's economy pass, not from this file
- [ ] The vendor always knows exactly what the coin is worth; the bros never do

---

## 📝 Development Notes

- At 40 HP it ties the Wobbly Windmill beer for the biggest HP heal in `consumables.json` (twice the Lukewarm Kebab). Nothing gives it to the player yet.
- Open for the author (Desk `Eurobound-4jln-q1`): does it stay, where it is sold or found (and so which city folder), and who writes the PENDING text.

---

## 🔧 Development Status

- **Status**: Drafted (reverse-documented from engine data; identity text PENDING (author))
- **File Location**: `design/items/general_items/questionable_goulash_item.md` (folder provisional until the source is ruled)
- **Registered In**: `consumables.json` Yes
- **Sprite**: `questionable_goulash_128.png`, `questionable_goulash_512.png`

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Short item doc reverse-documented from engine data (Eurobound-4jln, per rpac-q2) | Claude (agent) |
