# Enemy Profile: Tableside Thumper

*"Tableside Thumper raises the mallet and asks if anybody's celebrating a birthday."*

> **Source and status.** [CANON — author approved, 2026-11-12, Eurobound-p1y] Approved on Production
> Desk `Eurobound-p1y-q2`, verbatim: "Approve all as drafted". Name, concept, gimmick, move names,
> status, junk drop and flavor lines are verbatim from the approved draft,
> `design/worlds/sinfonia/villains/the_golden_cutlet/roster_proposal_for_author.md` §2. Every field
> the draft does not cover is marked **PENDING (author)**; every number is **PENDING (balancing
> pass)**. The gimmick is approved as a concept; engine support is proposed engineering work.

## 📋 Enemy Identity
- **Enemy ID**: `tableside_thumper` (the key in `sinfonia_enemies.json`; grep 2026-11-12: unique)
- **Display Name**: Tableside Thumper
- **City**: Sinfonia
- **Zone / Encounter Table**: The Golden Cutlet, Heritage Vaults (basement). Which vault: **PENDING (author)** (dungeon layout is the author's).
- **Encounter Family**: Heritage Vault Staff
- **Group Size**: **PENDING (author)**
- **Overview Source**: `design/worlds/sinfonia/sinfonia.md` has no Enemy Encounters section yet; the concept source is the approved roster draft §2.

---

## 🎭 Core Concept

### What It Actually Is
The man who pounds the schnitzel flat at your table with a mallet, for the "experience". The experience is on the bill. Now he's pounding the bros.

### What The Bros Think It Is
It's a show, and they're the VIP table.

### The Comedy Gap
Performative craftsmanship, the "tableside" surcharge, food as theater.

---

## ⚔️ Combat Specification

### Core Stats (engine fields)
| Stat | Value | Notes |
|------|-------|-------|
| `max_hp` | PENDING (balancing pass) | Rolling HP meter applies |
| `offense` | PENDING (balancing pass) | Rises with each pound he lands (see Gimmick); step size pending |
| `defense` | PENDING (balancing pass) | |
| `speed` | PENDING (balancing pass) | |
| `luck` | PENDING (balancing pass) | |
| `charm` | PENDING (balancing pass) | |
| `grit` | PENDING (balancing pass) | |

### Gimmick (approved concept)
A wind-up hitter. He raises the mallet and shouts the count, and the audience claps along. Each pound he lands makes the next one louder and harder. If the party hits him while the mallet is up, the count resets and he loses the turn. A pound that lands while the crowd is cheering inflicts **Embarrassed**.

Count length and escalation per pound: **PENDING (balancing pass)**.

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| Hand-Pounded | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Crowd Count-In | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Surcharge | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |

### Weaknesses & Resistances
| Category | Detail |
|----------|--------|
| **Weak against** | Interrupt on wind-up: a hit while the mallet is up resets the count and costs him the turn |
| **Resistant to** | PENDING (author) |
| **Immune to** | PENDING (author) |

---

## 💬 Battle Text

| Moment | Line |
|--------|------|
| `battle_intro` | "Tableside Thumper raises the mallet and asks if anybody's celebrating a birthday." |
| Bark | "HAND-POUNDED! THAT'S A SURCHARGE! HAND-POUNDED!" |
| On defeat | PENDING (author) |
| On fleeing (if it can flee) | PENDING (author) |
| Bro reaction (optional) | **Chadwick**: "Get my food in the shot. Get me in the shot. Hit me again, I wasn't filming." |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Junk drops are welcome and get real inspect microcopy (use `consumable_item_template.md`, `equipment_template.md` or `permanent_item_template.md` for the dropped item itself).

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | PENDING (balancing pass) | |
| SOVS | `gold_reward` | PENDING (balancing pass) | Value is SOVS; field rename pending |
| Item drop | `item_drop` | Splintered Mallet Head (`item_key` PENDING) | Junk drop; needs its own item doc, inspect microcopy and an author ruling |
| Drop chance | `drop_chance` | PENDING (balancing pass) | |
| Other (tickets, collectibles) | — | — | |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | Mallet-up telegraph pose. Facing west; size and palette PENDING (author) |
| **Palette Swaps** | PENDING (author) |
| **Text/Markings** | None in the draft |
| **Overworld Sprite** | The mallet-up pose is the overworld tell |
| **Filename** | not yet specced |

---

## ⚙️ Engine Entry (`sinfonia_enemies.json`)

`null` = PENDING (balancing pass). Not registered.

```json
"tableside_thumper": {
  "display_name": "Tableside Thumper",
  "battle_intro": "Tableside Thumper raises the mallet and asks if anybody's celebrating a birthday.",
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
| **Fields the schema does not have yet** | Moves; a wind-up/count state that escalates per landed pound and resets on interrupt; conditional status (Embarrassed while the crowd is cheering). Schema additions are proposed engineering work and need an author ruling |
| **Registered** | No |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Enemy ID unique across the repo (grep) | ✅ 2026-11-12 |
| Display name funny and unique across the game | ✅ canon index + grep 2026-11-12 |
| Not a villain (no name-brand racket, phases or story tie) | ✅ |
| Concept: actual vs believed written | ✅ |
| Stats use engine field names | ✅ (values pending) |
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ✅ Embarrassed |
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

- Encounter-table weighting and vault placement: PENDING (author).
- Move effects, types and battle text: PENDING (author); the draft named the moves only.

---

## 🔧 Development Status

- **Status**: Author-Approved (concept, 2026-11-12); numbers pending the balancing pass
- **File Location**: `design/worlds/sinfonia/enemies/tableside_thumper.md` (author ruling 2026-11-12, Eurobound-0q4x)
- **Registered In**: `game/assets/data/enemies/sinfonia_enemies.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Initial enemy doc from the approved roster draft (Eurobound-p1y) | world-builder agent |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `game/assets/data/enemies/debaucheryville_enemies.json`, `design/worlds/shamsterdam/shamsterdam.md` (Enemy Encounters) and the combat subset of `villain_template.md`. Villains use `villain_template.md`.*
