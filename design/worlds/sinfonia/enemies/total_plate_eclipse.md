# Enemy Profile: Total Plate Eclipse

*"Turn around. It's still there."*

> **Source and status.** [CANON — author approved, 2026-11-12, Eurobound-p1y] Approved on Production
> Desk `Eurobound-p1y-q2`, verbatim: "Approve all as drafted". Name, concept, gimmick, move names,
> status, junk drop and flavor lines are verbatim from the approved draft,
> `design/worlds/sinfonia/villains/the_golden_cutlet/roster_proposal_for_author.md` §8. Every field
> the draft does not cover is marked **PENDING (author)**; every number is **PENDING (balancing
> pass)**. The gimmick is approved as a concept; engine support is proposed engineering work.

## 📋 Enemy Identity
- **Enemy ID**: `total_plate_eclipse` (the key in `sinfonia_enemies.json`; grep 2026-11-12: unique)
- **Display Name**: Total Plate Eclipse
- **City**: Sinfonia
- **Zone / Encounter Table**: The Golden Cutlet, Heritage Vaults (basement). Which vault: **PENDING (author)** (dungeon layout is the author's).
- **Encounter Family**: Heritage Vault Staff
- **Group Size**: **PENDING (author)**. Its gimmick assumes it fights alongside other enemies ("its allies").
- **Overview Source**: `design/worlds/sinfonia/sinfonia.md` has no Enemy Encounters section yet; the concept source is the approved roster draft §8.

---

## 🎭 Core Concept

### What It Actually Is
A schnitzel pounded so wide it eclipses its plate, its table and most of the room's light. It is the house special. It is hostile.

### What The Bros Think It Is
Lunch. Lord Pilsner has called dibs.

### The Comedy Gap
Size as authenticity, the hubcap-sized "traditional" portion made for photos, food as a tourist dare. The `battle_intro` is a nod to Bonnie Tyler's "Total Eclipse of the Heart" (two words, not a lyric quote).

---

## ⚔️ Combat Specification

### Core Stats (engine fields)
| Stat | Value | Notes |
|------|-------|-------|
| `max_hp` | PENDING (balancing pass) | Rolling HP meter applies |
| `offense` | PENDING (balancing pass) | |
| `defense` | PENDING (balancing pass) | |
| `speed` | PENDING (balancing pass) | |
| `luck` | PENDING (balancing pass) | |
| `charm` | PENDING (balancing pass) | |
| `grit` | PENDING (balancing pass) | |

### Gimmick (approved concept)
While it's up, it hangs over its allies, so hits aimed at the other enemies hit the schnitzel instead. It also blocks the light, which lowers the party's accuracy. Each hit trims it from the edge, and once it's trimmed enough the allies underneath can be targeted again. A bro can spend a turn eating some of it: he heals a little and gets **Grease Fingers**, and it shrinks.

How much trimming uncovers the allies, the accuracy loss and the heal: **PENDING (balancing pass)**.

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| Eclipse | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Lemon Wedge to the Eye | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Grease Rain | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |

### Weaknesses & Resistances
| Category | Detail |
|----------|--------|
| **Weak against** | It shrinks as it's trimmed or eaten |
| **Resistant to** | PENDING (author) |
| **Immune to** | PENDING (author) |

---

## 💬 Battle Text

| Moment | Line |
|--------|------|
| `battle_intro` | "Turn around. It's still there." |
| On defeat | PENDING (author) |
| On fleeing (if it can flee) | PENDING (author) |
| Bro reaction (optional) | **Lord Pilsner**: "Dibs. I said dibs in the car." |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Junk drops are welcome and get real inspect microcopy (use `consumable_item_template.md`, `equipment_template.md` or `permanent_item_template.md` for the dropped item itself).

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | PENDING (balancing pass) | |
| SOVS | `gold_reward` | PENDING (balancing pass) | Value is SOVS; field rename pending |
| Item drop | `item_drop` | Lemon Wedge, Used (`item_key` PENDING) | Junk drop; needs its own item doc, inspect microcopy and an author ruling |
| Drop chance | `drop_chance` | PENDING (balancing pass) | |
| Other (tickets, collectibles) | — | — | |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | One size per trim stage. Facing west; number of stages, size and palette PENDING (author) |
| **Palette Swaps** | PENDING (author) |
| **Text/Markings** | None in the draft |
| **Overworld Sprite** | PENDING (author) |
| **Filename** | not yet specced |

---

## ⚙️ Engine Entry (`sinfonia_enemies.json`)

`null` = PENDING (balancing pass). Not registered.

```json
"total_plate_eclipse": {
  "display_name": "Total Plate Eclipse",
  "battle_intro": "Turn around. It's still there.",
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
| **Fields the schema does not have yet** | Moves; a cover rule that redirects hits on allies to itself until trimmed; party-wide accuracy loss while it's up; size stages; an "eat" action available to the party (heal + Grease Fingers + shrink). Schema additions are proposed engineering work and need an author ruling |
| **Registered** | No |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Enemy ID unique across the repo (grep) | ✅ 2026-11-12 |
| Display name funny and unique across the game | ✅ canon index + grep 2026-11-12 |
| Not a villain (no name-brand racket, phases or story tie) | ✅ trim stages are a gimmick, not boss phases |
| Concept: actual vs believed written | ✅ |
| Stats use engine field names | ✅ (values pending) |
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ✅ Grease Fingers |
| Rewards in SOVS; drops exist or are specced | ☐ junk drop needs an item doc |
| Junk drops have funny inspect microcopy | ☐ pending item doc |
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

- Encounter-table weighting and vault placement: PENDING (author). Its cover gimmick only does anything when other enemies are present; which groups it spawns in: PENDING (author).
- Move effects, types and battle text: PENDING (author); the draft named the moves only.

---

## 🔧 Development Status

- **Status**: Author-Approved (concept, 2026-11-12); numbers pending the balancing pass
- **File Location**: `design/worlds/sinfonia/enemies/total_plate_eclipse.md` (author ruling 2026-11-12, Eurobound-0q4x)
- **Registered In**: `game/assets/data/enemies/sinfonia_enemies.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Initial enemy doc from the approved roster draft (Eurobound-p1y) | world-builder agent |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `game/assets/data/enemies/debaucheryville_enemies.json`, `design/worlds/shamsterdam/shamsterdam.md` (Enemy Encounters) and the combat subset of `villain_template.md`. Villains use `villain_template.md`.*
