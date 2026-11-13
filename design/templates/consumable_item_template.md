# Item Definition: [Display Name]

*"[Satirical tagline: the vendor's pitch line or the bros' belief, played straight]" - [Who says it]*

> **Template Version 1.1 — created 2026-11-11 at the author's request; approved by the author 2026-11-11**

<!--
HOW TO USE THIS TEMPLATE
This template is for CONSUMABLES: items that deplete when used. Food, drinks, drugs,
vapes, pills, energy shots, medicine and single-use merch. One use (or one stack unit)
and it's gone. Anything reusable, infinite-use, or permanently attached to a bro stays on
permanent_item_template.md (see candy_smokes_item.md and summer_vacay_stein_item.md for
the edge cases). Brewery beers, openers and stamps keep their own brewery templates.

Headline consumables get their own doc built from this template. Ordinary menu rows inside
a location doc do not need one.

Rules that apply while filling it in:
- Read .claude/CLAUDE.md, the eurobound-satire-voice skill,
  design/narrative/bros_choose_debauchery.md and design/mechanics/intoxication_law.md first.
- Every price is SOVS ("40 SOVS", singular "1 SOV"), or an amount of one named coin from
  design/economy/shitcoin_master_pool.md. Crypto-only vendors (Tony420) never price in SOVS.
- Item identity, price, stats and effects need an author ruling. Anything you draft that
  the author has not ruled on is marked PROPOSED, in the field itself.
- Replace every [bracketed placeholder]. Delete this comment block before publishing.
- Keep every H2 header (with its emoji) and every table's column shape exactly as here.
- Optional subsections say so in their heading. Omit them when they do not apply.
-->

## 📋 Item Identity
- **Item ID**: `item_[item_name_snake_case]` (doc ID; grep the repo to confirm it is unique)
- **Engine Key**: `[item_name_snake_case]` (the key in `game/assets/data/items/consumables.json`, which carries no `item_` prefix)
- **Display Name**: [Item Name — real brand names keep their real names; invented products get a funny one]
- **Subtitle / Product Line**: [Optional tagline printed under the name, e.g. the vendor's product category]
- **Internal Name**: [What it actually is, in plain terms]
- **Item Type**: Consumable
- **Subtype**: [alcohol / drug / stimulant / vape / food / medicine / consumable merch — pick one or two]
- **Rarity**: [Actual rarity] (bros think it's [Rarity bros believe])
- **Vendor / Source**: [NPC name] (`[npc_id]`), [shop, quest, drop or airdrop]
- **Location**: [Location, City — parody names only] [or "ICQ, any FREE Wi-Fi hotspot" for ICQ vendors]

---

## 🎭 The Deception

### What It Actually Is
[The mundane, cheap, gross or dangerous reality. Specific and concrete: what is in it, where it came from, what it costs to make.]

### What The Bros Believe It Is
"[The bros' delusion, in their own voice. What they think they are buying. They are never afraid, never disgusted, never scam-aware.]"

### The Comedy Gap
[One or two sentences: the distance between the two above, and where the player sees it before the bros do. Do not explain the joke in any player-facing text; this section is internal.]

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | [X SOVS] or [X CoinName ($TICKER)] |
| **Actual Value** | [X SOVS] |
| **Resale Value** | [X SOVS or "0 SOVS (worthless)"] |
| **Can Be Sold** | [Yes/No + why] |
| **Stack Size** | [Max per inventory slot] |
| **Bundle Deals** | [Optional "discount" tiers, or "None"] |

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."
>
> "It can go as dark comedy, dirty, and unfamily friendly as it likes as this is an MA game."

Every consumable gets inspect text, junk most of all. Keep each line short: one or two sentences that fit one text box. No moral, no warning label, no wink at the player.

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | "[Line]" | [Canon / PROPOSED] |
| 2 | "[Line]" | [Canon / PROPOSED] |

---

## 📣 Vendor Pitch Copy

### Pitch
```
[The vendor's sales copy, verbatim where the author wrote it. ICQ vendors use ICQ formatting:
caps, emoji, broken punctuation.]
```

### Purchase Line
> "[What the vendor says or sends when the bros buy it]"

### Delivery (Tony420 items — optional for other vendors)
[How the item reaches the bros. For Tony420 stock, follow the standing rule below.]

Author ruling (2026-11-11), verbatim: "All tony delivered things are drop delivered, unless a goon is already in a scene, or it's somewhere sheisty (say he's dealing with another darkweb adjacent character or they're at the kavarna or the shadow exchange)"

- **Default**: dead drop. Tony420 is never seen.
- **Goon exception**: a goon hands it over only when a goon is already in the scene, or the scene is sheisty (a darkweb-adjacent character, the Cyberspace Kavarna, the Shadow Exchange).
- Record the drop spot and pickup interaction here, marked PROPOSED until ruled.

---

## 📊 Effects on Use

| Effect | Value | Duration | Stack Rule | Notes |
|--------|-------|----------|------------|-------|
| HP restored | [X or 0] | Instant | — | `heal_hp` |
| Bravado restored | [X or 0] | Instant | — | `heal_bravado` |
| Status applied | "[Status Name]" | [Turns / minutes / until event] | [Refresh / Extend / Escalate / Blocked while active] | [Existing status from `design/mechanics/Battle/status_effects.md`, or new and PROPOSED] |
| [Stat change] | [+/-X] | [Duration] | [Rule] | [Notes] |
| Delayed effect | [What hits later] | [Timer] | [Rule] | [Space Cake pattern: the bros think it isn't working] |

### Interaction With Other Statuses
| Existing Status | What Happens |
|-----------------|--------------|
| [Status] | [Interaction] |

### What It Does NOT Do
- ❌ [Thing the bros believe it does but doesn't]
- ❌ [Thing the bros believe it does but doesn't]

---

## 🍺 Intoxication Review

*Required for anything intoxicating: alcohol, drugs, stimulants, intoxicating vapes. Write "Not intoxicating" and delete the tables for plain food or medicine.*

### The Three Questions (`design/narrative/bros_choose_debauchery.md`)
| Question | Answer |
|----------|--------|
| **What does the bro THINK he's getting?** | [Answer] |
| **What does he ACTUALLY get?** | [Answer] |
| **The gap: how does it become a gameplay consequence?** | [Answer] |

### No Free Advantage
"Intoxicants do not provide uncomplicated, consequence-free advantages." State the cost: [the drawback, crash, delayed consequence or loss of control that pays for any benefit].

### Alcohol Ladder Step (alcohol only)
- **Step**: [Buzzed / Beer Goggles / Shitfaced / Catastrophe — how far one serving pushes the drinker]

### 10-Point Design Review (`design/mechanics/intoxication_law.md` §8)
| # | Point | Answer |
|---|-------|--------|
| 1 | Source item or drink | [This item] |
| 2 | Immediate effect | [Answer] |
| 3 | Escalation conditions | [Answer] |
| 4 | Visible player-facing cues | [Answer] |
| 5 | Effect on player control | [Answer — bounded, readable, recoverable] |
| 6 | Duration and recovery | [Answer] |
| 7 | Comedic consequence | [Answer] |
| 8 | Interaction with other established statuses | [Answer] |
| 9 | Technical implementation dependencies | [Answer — flag anything the Godot build cannot do yet as proposed engineering work] |
| 10 | Requires further author approval? | [Yes/No + what] |

---

## ⚙️ Engine Fields (`consumables.json`)

The live schema (`game/assets/data/items/consumables.json`, read by `game/core/data_repo.gd`, `game/battle/battle_core.gd` and `game/core/game_state.gd`) has four fields per entry:

```json
"[item_name_snake_case]": {
  "display_name": "[Display Name]",
  "heal_hp": [0],
  "heal_bravado": [0],
  "description": "[Short in-voice description. Keep the joke; do not flatten it into a stat readout.]"
}
```

| Field | Value |
|-------|-------|
| `display_name` | [Value] |
| `heal_hp` | [Integer] |
| `heal_bravado` | [Integer] |
| `description` | [Value] |
| **Fields the schema does not have yet** | [Price, coin, stack size, subtype, status, duration, delayed effects. List what this item needs; adding schema fields is proposed engineering work and needs an author ruling] |
| **Registered** | [Yes/No — registration goes through the `eurobound-item-engine-sync` skill] |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | [Size and shape] |
| **Design** | [What it looks like] |
| **Text/Markings** | [Exact label text. Read and fix every word on generated art; AI misspellings are errors] |
| **Color/Finish** | [Palette] |
| **States** | [Full / partly used / empty, if any] |
| **Filename** | [`snake_case_filename.png` or "not yet specced"] |

---

## 🔗 Quest Hooks

| Hook | Quest / File | Reader (who or what reads it) | Flag | Status |
|------|--------------|-------------------------------|------|--------|
| [How the item shows up] | `[file path or quest ID]` | [Player via inspect / NPC name / quest script / ICQ broadcast / rest scene] | `[flag_name]` or "none" | [Canon / PROPOSED] |

Flag writes in data use the one canonical shape (author, 2026-11-12, Eurobound-r8l8): `"set_flags": {"<flag id>": <value>}`, and on the item entry itself, for a write that fires when the bros get it, `"set_flags_on_acquire": {"<flag id>": <value>}`. Never `quest_flags_on_acquire`, `set_flag`, `sets_flag`, `sets_flags`, `flag_set` or `sets_state`. Spec: `docs/superpowers/specs/2026-11-12-flag-write-shape-proposal.md`.

---

## 🗣️ Bro Lines on Use (optional — include only once written or approved)

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
| No real city or place names in player-facing text | ☐ |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna, no bare numbers | ☐ |
| Deception written: actual vs believed vs gap | ☐ |
| Inspect microcopy written, short, funny, and junk items included | ☐ |
| Effects, durations and stack rules specified (or marked PROPOSED) | ☐ |
| Intoxication review complete (if intoxicating) | ☐ |
| A real cost pays for every benefit | ☐ |
| Engine fields match the live `consumables.json` schema | ☐ |
| Quest hooks name their readers | ☐ |
| Every unruled field marked PROPOSED | ☐ |
| Comedy value preserved at full strength | ☐ |
| Bros never achieve self-awareness, fear or disgust | ☐ |

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

- [Implementation or asset dependency]
- [Open question for the author]

---

## 🔧 Development Status

- **Status**: [Concept / Drafted / Reviewed / Sprites Commissioned / Implemented]
- **File Location**: `[routed path per the eurobound-item-creation skill]`
- **Registered In**: `consumables.json` [Yes/No]
- **Sprite**: [filename.png or "not yet specced"]

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial item doc | [name] |

---

*Template Version 1.1 — created 2026-11-11 at the author's request; approved by the author 2026-11-11. Field set drawn from the 2026-11-11 template audit (section B) and the house style of `permanent_item_template.md`. Reusable and permanent items stay on `permanent_item_template.md`.*

<!--
TEMPLATE REVISION HISTORY (about this template itself; do not copy into item docs)
| Date | Change | Author |
|------|--------|--------|
| 2026-11-11 | v1.0 created from the template audit | Claude (agent) |
| 2026-11-11 | v1.1: author approval recorded; added Delivery subsection with the author's Tony420 drop-delivery rule (dead drop by default, goon exception) | Claude (agent) |
-->
