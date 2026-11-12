# Enemy Profile: Voluntold Wrangler

*"Voluntold Wrangler scans the room for the man most likely to say yes."*

> **Source and status.** [CANON — author approved, 2026-11-12, Eurobound-p1y] Approved on Production
> Desk `Eurobound-p1y-q2`, verbatim: "Approve all as drafted". Name, concept, gimmick, move names,
> status and flavor lines are verbatim from the approved draft,
> `design/worlds/sinfonia/villains/the_golden_cutlet/roster_proposal_for_author.md` §4. Every field
> the draft does not cover is marked **PENDING (author)**; every number is **PENDING (balancing
> pass)**. The gimmick is approved as a concept; engine support is proposed engineering work.
> He is also an add in Phase 1 of The Schnitzel King's fight
> (`design/worlds/sinfonia/villains/the_golden_cutlet/the_schnitzel_king.md`).

## 📋 Enemy Identity
- **Enemy ID**: `voluntold_wrangler` (the key in `sinfonia_enemies.json`; grep 2026-11-12: unique)
- **Display Name**: Voluntold Wrangler
- **City**: Sinfonia
- **Zone / Encounter Table**: The Golden Cutlet, Heritage Vaults (basement). Which vault: **PENDING (author)** (dungeon layout is the author's).
- **Encounter Family**: Heritage Vault Staff
- **Group Size**: **PENDING (author)**
- **Overview Source**: `design/worlds/sinfonia/sinfonia.md` has no Enemy Encounters section yet; the concept source is the approved roster draft §4.

---

## 🎭 Core Concept

### What It Actually Is
A Master of Revels in velvet with a long shepherd's hook, whose whole job is dragging "volunteers" out of the audience and onstage for the bit.

### What The Bros Think It Is
They've been discovered. Finally.

### The Comedy Gap
Forced audience participation (canon), the dinner show that makes the customer the entertainment.

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
He hooks one bro out of the party and onto a little stage, where the bro does something "traditional" in a cardboard crown (leads a sing-along, gets pelted with bread rolls). The hooked bro loves it and won't come down, so he can't act until the Wrangler is beaten or another bro spends a turn booing him off. When he comes down he has **Embarrassed**, which he takes as a standing ovation.

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| The Hook | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Give It Up For | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Back by Popular Demand | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |

> **Renamed (author, Eurobound Desk 6qvk-q1, 2026-11-12: "Back by Popular Demand").** The approved draft
> called this move "Encore", which is already Phase 3 of the Bassline Opera House boss fight.

### Weaknesses & Resistances
| Category | Detail |
|----------|--------|
| **Weak against** | Beat him and the hooked bro returns at once |
| **Resistant to** | PENDING (author) |
| **Immune to** | PENDING (author) |

---

## 💬 Battle Text

| Moment | Line |
|--------|------|
| `battle_intro` | "Voluntold Wrangler scans the room for the man most likely to say yes." |
| On defeat | PENDING (author) |
| On fleeing (if it can flee) | PENDING (author) |
| Bro reaction (hooked) | **Lord Pilsner**: "They picked me. Out of everybody. Get the crown on straight, this is going on the Christmas card." |
| Bro reaction | **Bradley**: "Can I get picked? Pick me. I'm married, I never get picked." |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Junk drops are welcome and get real inspect microcopy (use `consumable_item_template.md`, `equipment_template.md` or `permanent_item_template.md` for the dropped item itself).

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | PENDING (balancing pass) | |
| SOVS | `gold_reward` | PENDING (balancing pass) | Value is SOVS; field rename pending |
| Item drop | `item_drop` | PENDING (author) | The draft names no junk drop for him |
| Drop chance | `drop_chance` | PENDING (balancing pass) | |
| Other (tickets, collectibles) | — | — | |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | Hook pose, plus a stage-and-crown overlay for whichever bro is hooked. Facing west; size and palette PENDING (author) |
| **Palette Swaps** | PENDING (author) |
| **Text/Markings** | None in the draft |
| **Overworld Sprite** | PENDING (author) |
| **Filename** | not yet specced |

---

## ⚙️ Engine Entry (`sinfonia_enemies.json`)

`null` = PENDING (balancing pass or author). Not registered.

```json
"voluntold_wrangler": {
  "display_name": "Voluntold Wrangler",
  "battle_intro": "Voluntold Wrangler scans the room for the man most likely to say yes.",
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
| **Fields the schema does not have yet** | Moves; removing one party member from play until the enemy dies or an ally spends a turn; status applied on return (Embarrassed); a party-member overlay (stage and crown). Schema additions are proposed engineering work and need an author ruling |
| **Registered** | No |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Enemy ID unique across the repo (grep) | ✅ 2026-11-12 |
| Display name funny and unique across the game | ✅ canon index + grep 2026-11-12 |
| Not a villain (no name-brand racket, phases or story tie) | ✅ (appears as a boss add; still a regular enemy) |
| Concept: actual vs believed written | ✅ |
| Stats use engine field names | ✅ (values pending) |
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ✅ Embarrassed |
| Rewards in SOVS; drops exist or are specced | ☐ pending |
| Junk drops have funny inspect microcopy | ☐ no drop yet |
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
- Boss add: joins The Schnitzel King in Phase 1 and hooks a bro onstage "for the toast".
- Third move renamed from "Encore" to "Back by Popular Demand" (author, 6qvk-q1); names stay unique.

---

## 🔧 Development Status

- **Status**: Author-Approved (concept, 2026-11-12); numbers pending the balancing pass
- **File Location**: `design/worlds/sinfonia/enemies/voluntold_wrangler.md` (author ruling 2026-11-12, Eurobound-0q4x)
- **Registered In**: `game/assets/data/enemies/sinfonia_enemies.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Initial enemy doc from the approved roster draft (Eurobound-p1y) | world-builder agent |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `game/assets/data/enemies/debaucheryville_enemies.json`, `design/worlds/shamsterdam/shamsterdam.md` (Enemy Encounters) and the combat subset of `villain_template.md`. Villains use `villain_template.md`.*
