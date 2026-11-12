# Enemy Profile: The Triple-Dredged Knight

*"A Triple-Dredged Knight clanks forward, shedding crumbs like a dandruff commercial."*

> **Source and status.** [CANON — author approved, 2026-11-12, Eurobound-p1y] Approved on Production
> Desk `Eurobound-p1y-q2`, verbatim: "Approve all as drafted". Name, concept, gimmick, move names,
> status, junk drop and flavor lines are verbatim from the approved draft,
> `design/worlds/sinfonia/villains/the_golden_cutlet/roster_proposal_for_author.md` §1. Every field
> the draft does not cover is marked **PENDING (author)**; every number is **PENDING (balancing
> pass)**. The gimmick is approved as a concept; engine support is proposed engineering work.

## 📋 Enemy Identity
- **Enemy ID**: `triple_dredged_knight` (the key in `sinfonia_enemies.json`; grep 2026-11-12: unique)
- **Display Name**: The Triple-Dredged Knight
- **City**: Sinfonia
- **Zone / Encounter Table**: The Golden Cutlet, Heritage Vaults (basement). Which vault: **PENDING (author)** (dungeon layout is the author's).
- **Encounter Family**: Heritage Vault Staff
- **Group Size**: **PENDING (author)**
- **Overview Source**: `design/worlds/sinfonia/sinfonia.md` has no Enemy Encounters section yet; the concept source is the approved roster draft §1.

---

## 🎭 Core Concept

### What It Actually Is
A server in vacuum-formed plastic armor that has been floured, egg-washed and breadcrumbed, because the menu says everything here is "hand-breaded to order", the staff included.

### What The Bros Think It Is
He's a real knight. Lord Pilsner wants to be knighted by him.

### The Comedy Gap
Dinner-theater fake chivalry, and the "hand-made" upcharge on deep-fried plastic.

---

## ⚔️ Combat Specification

### Core Stats (engine fields)
| Stat | Value | Notes |
|------|-------|-------|
| `max_hp` | PENDING (balancing pass) | Rolling HP meter applies |
| `offense` | PENDING (balancing pass) | |
| `defense` | PENDING (balancing pass) | Near zero once all three coats are off (see Gimmick); number pending |
| `speed` | PENDING (balancing pass) | |
| `luck` | PENDING (balancing pass) | |
| `charm` | PENDING (balancing pass) | |
| `grit` | PENDING (balancing pass) | |

### Gimmick (approved concept)
He fights in three coats that come off in order: flour, then egg, then crumb. Each coat shrugs off a different kind of attack, so the party has to switch it up as the layers come off. Whoever lands a hit on the egg coat gets **Grease Fingers**. Strip all three and he's a sweaty man in a plastic breastplate with almost no defense.

Which attack type each coat shrugs off, and how many hits strip a coat: **PENDING (author / balancing pass)**.

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| Crumb Shed | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Egg Wash | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Shield of Panko | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |

### Weaknesses & Resistances
| Category | Detail |
|----------|--------|
| **Weak against** | Shifts per coat; with all three coats stripped he has almost no defense |
| **Resistant to** | Shifts per coat (each coat shrugs off a different kind of attack); which types and percentages: PENDING (author / balancing pass) |
| **Immune to** | PENDING (author) |

---

## 💬 Battle Text

| Moment | Line |
|--------|------|
| `battle_intro` | "A Triple-Dredged Knight clanks forward, shedding crumbs like a dandruff commercial." |
| On defeat | "The Triple-Dredged Knight is down to the plastic. He still has four tables." |
| On fleeing (if it can flee) | PENDING (author) |
| Bro reaction (optional) | **Lord Pilsner**: "Kneel me. I mean knight me. Do the sword thing." |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Junk drops are welcome and get real inspect microcopy (use `consumable_item_template.md`, `equipment_template.md` or `permanent_item_template.md` for the dropped item itself).

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | PENDING (balancing pass) | |
| SOVS | `gold_reward` | PENDING (balancing pass) | Value is SOVS; field rename pending |
| Item drop | `item_drop` | [Loose Breastplate Crumbs](../../../items/sinfonia_items/loose_breastplate_crumbs_item.md) (`item_key` `loose_breastplate_crumbs`, proposed; not yet registered) | Junk drop; item doc with author-approved inspect microcopy (2026-11-12, Eurobound-2kty-q1). Engine registration: Eurobound-jlzw |
| Drop chance | `drop_chance` | PENDING (balancing pass) | |
| Other (tickets, collectibles) | — | — | |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | Three coat states (flour, egg, crumb). Facing west; size and palette PENDING (author) |
| **Palette Swaps** | One palette swap per coat. Tougher variants: PENDING (author) |
| **Text/Markings** | None in the draft |
| **Overworld Sprite** | PENDING (author) |
| **Filename** | not yet specced |

---

## ⚙️ Engine Entry (`sinfonia_enemies.json`)

`null` = PENDING (balancing pass). Not registered.

```json
"triple_dredged_knight": {
  "display_name": "The Triple-Dredged Knight",
  "battle_intro": "A Triple-Dredged Knight clanks forward, shedding crumbs like a dandruff commercial.",
  "max_hp": null,
  "offense": null,
  "defense": null,
  "speed": null,
  "luck": null,
  "xp_reward": null,
  "gold_reward": null,
  "item_drop": null,
  "drop_chance": null
}
```

| Field | Value |
|-------|-------|
| **Fields the schema does not have yet** | Moves; coat stages (three ordered defense states, each with its own resistance and sprite); on-hit status for attackers (Grease Fingers on hitting the egg coat). Schema additions are proposed engineering work and need an author ruling |
| **Registered** | No |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Enemy ID unique across the repo (grep) | ✅ 2026-11-12 |
| Display name funny and unique across the game | ✅ canon index + grep 2026-11-12 |
| Not a villain (no name-brand racket, phases or story tie) | ✅ coat stages are a gimmick, not boss phases |
| Concept: actual vs believed written | ✅ |
| Stats use engine field names | ✅ (values pending) |
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ✅ Grease Fingers |
| Rewards in SOVS; drops exist or are specced | ✅ junk drop specced in its item doc |
| Junk drops have funny inspect microcopy | ✅ author-approved, in the item doc |
| Intoxication hook and 10-point review done (if it applies) | n/a |
| No real city or place names in battle text | ✅ |
| Every unruled number marked PROPOSED | ✅ marked PENDING (balancing pass) |
| Bros never afraid, disgusted or self-aware | ✅ |

---

## 🚫 Warnings & Restrictions

### Content
- [x] No narrator, disclaimer, moral framing, or any device that explains the joke; battle text never winks at the player
- [x] Full-strength MA satire; no sanitized version, no safe-build swap. The only ceiling is no nudity
- [x] Satire is sharp and specific — the bros' delusion AND the city's culture are both fair game (author ruling 2026-08-03: no punch-direction rules; "it's offensive" is not a design consideration)
- [x] Enemies are never boring, corporate or professional, even the fine collector
- [x] No mascots: no enemy joins the party, becomes a pet, or follows the bros afterwards
- [x] Funny, unique name; no real place names in player-facing text; real brands, products and songs keep their real names

### Money & Crypto
- [x] All money is SOVS ("40 SOVS", "1 SOV"); never euros, the € glyph or koruna
- [x] Crypto content conforms to `design/economy/economy_system.md`; coins only from `design/economy/shitcoin_master_pool.md` (no crypto content)

---

## 📝 Development Notes

- Encounter-table weighting and vault placement: PENDING (author).
- Move effects, types and battle text: PENDING (author); the draft named the moves only.

---

## 🔧 Development Status

- **Status**: Author-Approved (concept, 2026-11-12); numbers pending the balancing pass
- **File Location**: `design/worlds/sinfonia/enemies/triple_dredged_knight.md` (author ruling 2026-11-12, Eurobound-0q4x)
- **Registered In**: `game/assets/data/enemies/sinfonia_enemies.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Initial enemy doc from the approved roster draft (Eurobound-p1y) | world-builder agent |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `game/assets/data/enemies/debaucheryville_enemies.json`, `design/worlds/shamsterdam/shamsterdam.md` (Enemy Encounters) and the combat subset of `villain_template.md`. Villains use `villain_template.md`.*
