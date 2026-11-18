# Item Definition: Absinthe Shot

*"Tastes like licorice and bad decisions. Restores 8 Bravado."* - engine description (`game/assets/data/items/consumables.json:15`)

> **Source and status.** Bead Eurobound-4jln (reverse documentation of an engine entry). Short item doc per the author's ruling on Desk Eurobound-rpac-q2 (2026-11-15): "A: a short .md per item from its template". Built from `design/templates/consumable_item_template.md`.
> - **Sourced:** the name, the numbers, the `alcohol` flag and the description are copied from `game/assets/data/items/consumables.json:10-16`. A 3D icon is built (`game/assets/items/icons/3d/absinthe_shot_128.png`, `absinthe_shot_512.png`; icon batch 15, blind A4 pass, `Production/session-logs/session-log.md:2195`).
> - **Where it came from:** the entry was first written as vertical-slice scaffolding (`docs/superpowers/plans/2026-07-30-vertical-slice.md:287-292`), not from an author brief. No shop, drop or quest gives it out in data today.
> - **Conflicting design mention:** `design/items/docs/items.md:65-67` lists "Absinthe Shot (Debaucheryville Special)" under Regional Specialty Items: "Massive damage boost but inflicts "Hallucinating" (random targeting)", flavour "The green fairy has some strong opinions". The engine entry restores 8 Bravado and applies no status. Which one is the item goes on the Eurobound Desk (`Eurobound-4jln-q1`).
> - **Not sourced:** every field below marked **PENDING (author)**. Nothing in this doc is invented, and nothing here changes engine data.
> - **Routing:** `debaucheryville_items/`, on the strength of the `items.md:65` mention ("Debaucheryville Special"). If the author rules the engine entry is a different item, the folder is part of that answer.
> - **Name check:** not the same item as the Absinthe Shot Flight on The Bohemian Trap's menu (30 SOVS, `design/worlds/debaucheryville/the_bohemian_trap.md:145`; `npc_emil_green_fairy.md:221`). The names differ; whether the two should stay separate is part of `Eurobound-4jln-q1`.

## 📋 Item Identity
- **Item ID**: `item_absinthe_shot` (doc ID; grep 2026-11-17: no other use)
- **Engine Key**: `absinthe_shot` (`game/assets/data/items/consumables.json:10`)
- **Display Name**: Absinthe Shot (`consumables.json:12`)
- **Subtitle / Product Line**: PENDING (author)
- **Internal Name**: A shot of absinthe (from the name). Anything beyond that is PENDING (author)
- **Item Type**: Consumable
- **Subtype**: alcohol (`"alcohol": true`, `consumables.json:11`)
- **Rarity**: PENDING (author)
- **Vendor / Source**: PENDING (author). No shop, drop or quest gives it out in data
- **Location**: Debaucheryville per `design/items/docs/items.md:65`; where in the city: PENDING (author)

---

## 🎭 The Deception

### What It Actually Is
"Tastes like licorice and bad decisions." (engine description, `consumables.json:15`). Anything beyond that is PENDING (author).

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
| 1 | "Tastes like licorice and bad decisions. Restores 8 Bravado." | Engine description (`consumables.json:15`); whether it stays: Desk `Eurobound-4jln-q1` |
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
| HP restored | 0 | Instant | — | `heal_hp` (`consumables.json:13`) |
| Bravado restored | 8 | Instant | — | `heal_bravado` (`consumables.json:14`) |
| Counts as a drink | yes | — | — | `alcohol: true` (`consumables.json:11`); per the template's field table this ends Sober (`game_state.gd`, `game_clock.gd`, `navigation_roll.gd`) |
| Status applied | None | — | — | The entry has no `intoxicant` block. `items.md:65` says "Hallucinating"; see the conflict note above |

### Interaction With Other Statuses
| Existing Status | What Happens |
|-----------------|--------------|
| Sober | Ends it (`alcohol: true`) |
| Others | PENDING (author) |

### What It Does NOT Do
- ❌ In data it applies no intoxication status and no drawback. Whether that stands is PENDING (author) (see the review below).

---

## 🍺 Intoxication Review

Intoxicating (`alcohol: true`). The review below is PENDING (author): the engine entry gives +8 Bravado with no cost in data, and `design/narrative/bros_choose_debauchery.md` says "Intoxicants do not provide uncomplicated, consequence-free advantages." That gap is part of Desk `Eurobound-4jln-q1`; this doc does not fill it.

### The Three Questions (`design/narrative/bros_choose_debauchery.md`)
| Question | Answer |
|----------|--------|
| **What does the bro THINK he's getting?** | PENDING (author) |
| **What does he ACTUALLY get?** | In data: +8 Bravado, and Sober ends. Anything else PENDING (author) |
| **The gap: how does it become a gameplay consequence?** | PENDING (author) |

### No Free Advantage
"Intoxicants do not provide uncomplicated, consequence-free advantages." State the cost: PENDING (author). In data there is none.

### Alcohol Ladder Step (alcohol only)
- **Step**: PENDING (author)

### 10-Point Design Review (`design/mechanics/intoxication_law.md` §8)
| # | Point | Answer |
|---|-------|--------|
| 1 | Source item or drink | Absinthe Shot (`absinthe_shot`) |
| 2 | Immediate effect | +8 Bravado (`consumables.json:14`); ends Sober |
| 3 | Escalation conditions | PENDING (author) |
| 4 | Visible player-facing cues | PENDING (author) |
| 5 | Effect on player control | PENDING (author) |
| 6 | Duration and recovery | PENDING (author) |
| 7 | Comedic consequence | PENDING (author) |
| 8 | Interaction with other established statuses | PENDING (author) |
| 9 | Technical implementation dependencies | PENDING (author) |
| 10 | Requires further author approval? | Yes: everything in this review |

---

## ⚙️ Engine Fields (`consumables.json`)

Copied from `game/assets/data/items/consumables.json:10-16`, verbatim:

```json
"absinthe_shot": {
  "alcohol": true,
  "display_name": "Absinthe Shot",
  "heal_hp": 0,
  "heal_bravado": 8,
  "description": "Tastes like licorice and bad decisions. Restores 8 Bravado."
}
```

| Field | Required | Read by | Value |
|-------|----------|---------|-------|
| `display_name` | yes | data_repo / UI | Absinthe Shot |
| `heal_hp` | yes | `battle_core.gd` | 0 |
| `heal_bravado` | yes | `battle_core.gd` | 8 |
| `description` | yes | UI | Tastes like licorice and bad decisions. Restores 8 Bravado. |
| `alcohol` | optional | `game_clock.gd`, `navigation_roll.gd`, `game_state.gd` (true = a drink; ends Sober) | true |
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
| **Fields the schema does not have yet** | | | PENDING (author): depends on the intoxication ruling |
| **Registered** | | | Yes |

---

## 🖼️ Physical description (icon art brief)

PENDING (author). The 12-field description is the Writers' Room's to write and the Desk's to approve (`design/items/docs/physical_descriptions_tracker.md`, rpac). The icon already exists; `design/items/debaucheryville_items/tan_line_neon_shooter_item.md:65` uses it as a must-not-look-like reference ("same lathe — colour is the only tell"), so a description should match the shipped icon.

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
| **Inventory Icon** | 3D icon, built (`game/assets/items/icons/3d/absinthe_shot_128.png`, `absinthe_shot_512.png`) |
| **Design** | See the icon. Written description PENDING (author) |
| **Text/Markings** | PENDING (author) |
| **Color/Finish** | PENDING (author) |
| **States** | PENDING (author) |
| **Filename** | `absinthe_shot_128.png`, `absinthe_shot_512.png` |

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
| Display name unique across the game (real brands keep real names) | ☑ (Absinthe Shot Flight is a different name; see the name check) |
| No real city or place names in player-facing text | ☑ |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna, no bare numbers | ☐ PENDING (author) (no price) |
| Deception written: actual vs believed vs gap | ☐ PENDING (author) |
| Inspect microcopy written, short, funny, and junk items included | ☐ PENDING (author) |
| Effects, durations and stack rules specified (or marked PROPOSED) | ☐ PENDING (author) |
| Intoxication review complete (if intoxicating) | ☐ PENDING (author) |
| A real cost pays for every benefit | ☐ PENDING (author) (none in data) |
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

- `docs/research/2026-11-14-jrpg-item-categories.md:111` counts it as one of four built Bravado restores, all alcohol.
- Open for the author (Desk `Eurobound-4jln-q1`): engine entry or the `items.md:65` version; where it is sold or found; the cost the intoxication law asks for; who writes the PENDING text.

---

## 🔧 Development Status

- **Status**: Drafted (reverse-documented from engine data; identity text PENDING (author))
- **File Location**: `design/items/debaucheryville_items/absinthe_shot_item.md`
- **Registered In**: `consumables.json` Yes
- **Sprite**: `absinthe_shot_128.png`, `absinthe_shot_512.png`

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Short item doc reverse-documented from engine data (Eurobound-4jln, per rpac-q2) | Claude (agent) |
