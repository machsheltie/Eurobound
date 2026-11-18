# Item Definition: Lukewarm Kebab

*"Street meat of dubious provenance. Restores 20 HP."* - engine description (`game/assets/data/items/consumables.json:8`)

> **Source and status.** Bead Eurobound-4jln (reverse documentation of an engine entry). Short item doc per the author's ruling on Desk Eurobound-rpac-q2 (2026-11-15): "A: a short .md per item from its template". Built from `design/templates/consumable_item_template.md`.
> - **Sourced:** the name, the numbers and the description are copied from `game/assets/data/items/consumables.json:4-9`. The drops are copied from `game/assets/data/enemies/debaucheryville_enemies.json:15-16` (Feral Segway Tourist) and `:70-71` (Condiment Clan Ninja, approved 2026-11-09 in `design/worlds/debaucheryville/villains/absinthe_arcade/kebab_kombat/condiment_clan_ninja.md:182`). The 3D icon is author-approved (ledger `docs/superpowers/NEXT_WORK.md:889`, asset-team-qc-lukewarm_kebab: "Round 3 is fine: build it").
> - **Where it came from:** the entry was first written as vertical-slice scaffolding (`docs/superpowers/plans/2026-07-30-vertical-slice.md:281-286`), not from an author brief. Whether it stays as is goes on the Eurobound Desk (`Eurobound-4jln-q1`).
> - **Not sourced:** every field below marked **PENDING (author)**. Nothing in this doc is invented, and nothing here changes engine data.
> - **Routing:** `debaucheryville_items/`, because both sources that give it out are Debaucheryville enemies (eurobound-item-creation, Step 3, test 2).

## 📋 Item Identity
- **Item ID**: `item_lukewarm_kebab` (doc ID; grep 2026-11-17: no other use)
- **Engine Key**: `lukewarm_kebab` (`game/assets/data/items/consumables.json:4`)
- **Display Name**: Lukewarm Kebab (`consumables.json:5`)
- **Subtitle / Product Line**: PENDING (author)
- **Internal Name**: A kebab (from the name). Anything beyond that is PENDING (author)
- **Item Type**: Consumable
- **Subtype**: food (from the name and the HP heal; the entry has no `subtype` field)
- **Rarity**: PENDING (author)
- **Vendor / Source**: enemy drop. Feral Segway Tourist (`feral_segway_tourist`), `drop_chance` 1.0 (`debaucheryville_enemies.json:15-16`). Condiment Clan Ninja (`condiment_clan_ninja`), 25% common drop (`debaucheryville_enemies.json:70-71`; approved 2026-11-09, `condiment_clan_ninja.md:182`: "Reuses the existing Debaucheryville drop, no new item"). No shop sells it.
- **Location**: Debaucheryville (both droppers). Which streets: PENDING (author)

---

## 🎭 The Deception

### What It Actually Is
"Street meat of dubious provenance." (engine description, `consumables.json:8`). Anything beyond that is PENDING (author).

### What The Bros Believe It Is
PENDING (author).

### The Comedy Gap
PENDING (author).

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | None: not sold (no shop entry; drop only) |
| **Actual Value** | PENDING (author) |
| **Resale Value** | PENDING (author) (the entry has no `sell_value`) |
| **Can Be Sold** | PENDING (author) |
| **Stack Size** | PENDING (author) (the entry has no `max_stack`) |
| **Bundle Deals** | None |

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."
>
> "It can go as dark comedy, dirty, and unfamily friendly as it likes as this is an MA game."

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | "Street meat of dubious provenance. Restores 20 HP." | Engine description (`consumables.json:8`); whether it stays: Desk `Eurobound-4jln-q1` |
| 2 | PENDING (author) | PENDING (author) |

---

## 📣 Vendor Pitch Copy

### Pitch
```
None: the item is a drop, not sold.
```

### Purchase Line
> None: not sold.

---

## 📊 Effects on Use

| Effect | Value | Duration | Stack Rule | Notes |
|--------|-------|----------|------------|-------|
| HP restored | 20 | Instant | — | `heal_hp` (`consumables.json:6`) |
| Bravado restored | 0 | Instant | — | `heal_bravado` (`consumables.json:7`) |
| Status applied | None | — | — | The entry applies no status |

### Interaction With Other Statuses
| Existing Status | What Happens |
|-----------------|--------------|
| None in data | PENDING (author) |

### What It Does NOT Do
- ❌ Nothing beyond the 20 HP heal is in data. Anything else is PENDING (author).

---

## 🍺 Intoxication Review

Not intoxicating (the entry has no `alcohol` or `intoxicant` field).

---

## ⚙️ Engine Fields (`consumables.json`)

Copied from `game/assets/data/items/consumables.json:4-9`, verbatim:

```json
"lukewarm_kebab": {
  "display_name": "Lukewarm Kebab",
  "heal_hp": 20,
  "heal_bravado": 0,
  "description": "Street meat of dubious provenance. Restores 20 HP."
}
```

| Field | Required | Read by | Value |
|-------|----------|---------|-------|
| `display_name` | yes | data_repo / UI | Lukewarm Kebab |
| `heal_hp` | yes | `battle_core.gd` | 20 |
| `heal_bravado` | yes | `battle_core.gd` | 0 |
| `description` | yes | UI | Street meat of dubious provenance. Restores 20 HP. |
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
| `source` | optional | data only | omitted (the drops are set on the enemies) |
| `_pending` | optional | ignored at run time | omitted |
| **Fields the schema does not have yet** | | | None needed for what is in data |
| **Registered** | | | Yes |

---

## 🖼️ Physical description (icon art brief)

PENDING (author). The 12-field description is the Writers' Room's to write and the Desk's to approve (`design/items/docs/physical_descriptions_tracker.md`, rpac). The shipped icon is author-approved (round 3 reference, ledger `NEXT_WORK.md:889`), so a description should match it.

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
| **Inventory Icon** | 3D icon, built (`game/assets/items/icons/3d/lukewarm_kebab_128.png`, `lukewarm_kebab_512.png`) |
| **Design** | See the icon. Written description PENDING (author) |
| **Text/Markings** | PENDING (author) |
| **Color/Finish** | PENDING (author) |
| **States** | PENDING (author) |
| **Filename** | `lukewarm_kebab_128.png`, `lukewarm_kebab_512.png` |

---

## 🔗 Quest Hooks

| Hook | Quest / File | Reader (who or what reads it) | Flag | Status |
|------|--------------|-------------------------------|------|--------|
| Dropped after a Feral Segway Tourist fight | `game/assets/data/enemies/debaucheryville_enemies.json:15-16` | Battle rewards | none | Engine data |
| Common drop from the Condiment Clan Ninja (Kebab Kombat) | `design/worlds/debaucheryville/villains/absinthe_arcade/kebab_kombat/condiment_clan_ninja.md:182` | Battle rewards | none | Approved 2026-11-09 |

---

## 🗣️ Bro Lines on Use (optional — include only once written or approved)

None written or approved.

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item ID and engine key unique across the repo (grep) | ☑ (grep 2026-11-17) |
| Display name unique across the game (real brands keep real names) | ☑ (grep 2026-11-17) |
| No real city or place names in player-facing text | ☑ |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna, no bare numbers | ☑ (not sold) |
| Deception written: actual vs believed vs gap | ☐ PENDING (author) |
| Inspect microcopy written, short, funny, and junk items included | ☐ PENDING (author) |
| Effects, durations and stack rules specified (or marked PROPOSED) | ☑ (from data; stack PENDING) |
| Intoxication review complete (if intoxicating) | ☑ (not intoxicating) |
| A real cost pays for every benefit | ☐ PENDING (author) |
| Engine fields match the live `consumables.json` schema | ☑ |
| Quest hooks name their readers | ☑ |
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

- Several approved villain docs use its dropper, the Feral Segway Tourist, as their stat benchmark (see `design/worlds/debaucheryville/enemies/feral_segway_tourist.md`).
- Open for the author (Desk `Eurobound-4jln-q1`): does the entry stay as written, and who writes the PENDING text?

---

## 🔧 Development Status

- **Status**: Drafted (reverse-documented from engine data; identity text PENDING (author))
- **File Location**: `design/items/debaucheryville_items/lukewarm_kebab_item.md`
- **Registered In**: `consumables.json` Yes
- **Sprite**: `lukewarm_kebab_128.png`, `lukewarm_kebab_512.png`

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Short item doc reverse-documented from engine data (Eurobound-4jln, per rpac-q2) | Claude (agent) |
