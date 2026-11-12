# Enemy Profile: On-The-House Wenches

*"The On-The-House Wenches are on the house. The mead is not."*

> **Source and status.** [CANON — author approved, 2026-11-12, Eurobound-p1y] Approved on Production
> Desk `Eurobound-p1y-q2`, verbatim: "Approve all as drafted". Name, concept, gimmick, intoxication
> hook (including its 10-point review), move names, status, junk drop and flavor lines are verbatim
> from the approved draft,
> `design/worlds/sinfonia/villains/the_golden_cutlet/roster_proposal_for_author.md` §6. Every field
> the draft does not cover is marked **PENDING (author)**; every number is **PENDING (balancing
> pass)**. The gimmick is approved as a concept; engine support is proposed engineering work.
> They are also an add in Phase 2 of The Schnitzel King's fight
> (`design/worlds/sinfonia/villains/the_golden_cutlet/the_schnitzel_king.md`).

## 📋 Enemy Identity
- **Enemy ID**: `on_the_house_wenches` (the key in `sinfonia_enemies.json`; grep 2026-11-12: unique)
- **Display Name**: On-The-House Wenches
- **City**: Sinfonia
- **Zone / Encounter Table**: The Golden Cutlet, Heritage Vaults (basement). Which vault: **PENDING (author)** (dungeon layout is the author's).
- **Encounter Family**: Heritage Vault Staff
- **Group Size**: A small pack; size **PENDING (balancing pass)**
- **Overview Source**: `design/worlds/sinfonia/sinfonia.md` has no Enemy Encounters section yet; the concept source is the approved roster draft §6.

---

## 🎭 Core Concept

### What It Actually Is
A pack of servers in polyester bodices pushing plastic goblets of "complimentary" honey mead that tastes like Robitussin strained through a Renaissance Faire. It's on the house until the bill comes.

### What The Bros Think It Is
Free drinks. That's what the Pass promised. It's working.

### The Comedy Gap
The "complimentary" drink that turns up on the tab, and bottomless drinks as a business model.

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

### Gimmick (approved concept, intoxication)
They don't fight the bros, they pour for them. The bros never refuse a goblet, so every pour pushes a bro up the alcohol escalation: **Buzzed** (Liquid Confidence: braver, sloppier) and then **Beer Goggles** (the bro tries to buy the Wenches a drink instead of hitting them, and hits his own friends). Nothing is charged after this fight: every goblet is chalked on a slate behind the bar, and the slate comes back at the King's defeat, so the post-battle bill stays Flash Pillory's gimmick alone. They chant Chumbawamba's "Tubthumping" with every drink in the chorus swapped for mead.

> **Depends on Production Desk `Eurobound-p1y-q3`.** The approved draft ties the slate to The
> Schnitzel King's defeat payoff option (b). The author approved the draft but has not picked a
> payoff yet; how the slate comes due is settled by that answer.

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| Top You Up | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| It's Complimentary | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Last Orders | PENDING (author) | PENDING (author) | Sloppy | PENDING (balancing pass) | PENDING (author) |

### Weaknesses & Resistances
| Category | Detail |
|----------|--------|
| **Weak against** | PENDING (author) |
| **Resistant to** | PENDING (author) |
| **Immune to** | PENDING (author) |

### Intoxication Hook (only if it inflicts or feeds on drinking or drugs)
Follows `design/mechanics/intoxication_law.md`. Approved §8 review (concept only; thresholds to the balancing pass):

1. Source: the Wenches' "complimentary" mead (an enemy action, not an item).
2. Immediate effect: one step up the alcohol escalation per goblet.
3. Escalation: Buzzed, then Beer Goggles; capped at Beer Goggles inside this fight (Shitfaced and Catastrophe stay with the player's own drinking).
4. Cues: goblet animation, the bro's sprite flushes, the tier label on his status bar.
5. Control: at Beer Goggles, a chance his action targets an ally or turns into flirting (the canon Beer Goggles −Accuracy / +Friendly Fire).
6. Duration and recovery: wears off after battle in the normal way; no lasting control loss.
7. Comedy: the bros think they're finally getting the Pass's free beer; every goblet is chalked on the slate that comes due when the King falls.
8. Interactions: stacks with Liquid Confidence and Sloppy; does not trigger Blackout Drunk inside this fight.
9. Tech: needs a per-character intoxication tier and an enemy-driven "pour" action (proposed engineering work).
10. Author approval: given 2026-11-12 ("Approve all as drafted") for the cap, the slate (tab) and the mechanic. The slate's payoff waits on `Eurobound-p1y-q3`; thresholds and the friendly-fire chance wait on the balancing pass.

---

## 💬 Battle Text

| Moment | Line |
|--------|------|
| `battle_intro` | "The On-The-House Wenches are on the house. The mead is not." |
| Battle log | "Bradley accepts the goblet. Bradley accepts the next goblet. Nobody is offering anymore; Bradley is just taking." |
| On defeat | PENDING (author) |
| On fleeing (if it can flee) | PENDING (author) |
| Bro reaction (Beer Goggles) | **Chadwick**: "Ladies. Ladies. You wanna see the VIP part of my Pass?" |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Junk drops are welcome and get real inspect microcopy (use `consumable_item_template.md`, `equipment_template.md` or `permanent_item_template.md` for the dropped item itself).

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | PENDING (balancing pass) | |
| SOVS | `gold_reward` | PENDING (balancing pass) | Value is SOVS; field rename pending |
| Item drop | `item_drop` | Plastic Goblet, Sticky (`item_key` PENDING) | Junk drop; needs its own item doc, inspect microcopy and an author ruling |
| Drop chance | `drop_chance` | PENDING (balancing pass) | |
| Other (tickets, collectibles) | PROPOSED field: the slate | — | No charge after this fight; goblets are chalked on the slate (payoff per `Eurobound-p1y-q3`) |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | Goblet-raise pose. Facing west; size and palette PENDING (author) |
| **Palette Swaps** | PENDING (author) |
| **Text/Markings** | None in the draft |
| **Overworld Sprite** | PENDING (author) |
| **Filename** | not yet specced |

---

## ⚙️ Engine Entry (`sinfonia_enemies.json`)

`null` = PENDING (balancing pass). Not registered.

```json
"on_the_house_wenches": {
  "display_name": "On-The-House Wenches",
  "battle_intro": "The On-The-House Wenches are on the house. The mead is not.",
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
| **Fields the schema does not have yet** | Moves; group size; a per-character intoxication tier and an enemy-driven "pour" action; an in-fight cap at Beer Goggles; a dungeon-wide slate counter. Schema additions are proposed engineering work and need an author ruling |
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
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ✅ Liquid Confidence, Sloppy; Buzzed and Beer Goggles are the canon alcohol escalation |
| Rewards in SOVS; drops exist or are specced | ☐ junk drop needs an item doc |
| Junk drops have funny inspect microcopy | ☐ pending item doc |
| Intoxication hook and 10-point review done (if it applies) | ✅ approved 2026-11-12; thresholds pending |
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
- Move effects, types and battle text: PENDING (author); the draft named the moves and tied Sloppy to *Last Orders* only.
- Boss add: pours for whoever is still standing in Phase 2 of The Schnitzel King's fight.
- The chorus parody of "Tubthumping" is described, not written; the actual sung lines are PENDING (author).

---

## 🔧 Development Status

- **Status**: Author-Approved (concept, 2026-11-12); numbers pending the balancing pass; slate payoff pending `Eurobound-p1y-q3`
- **File Location**: `design/worlds/sinfonia/enemies/on_the_house_wenches.md` (author ruling 2026-11-12, Eurobound-0q4x)
- **Registered In**: `game/assets/data/enemies/sinfonia_enemies.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Initial enemy doc from the approved roster draft (Eurobound-p1y) | world-builder agent |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `game/assets/data/enemies/debaucheryville_enemies.json`, `design/worlds/shamsterdam/shamsterdam.md` (Enemy Encounters) and the combat subset of `villain_template.md`. Villains use `villain_template.md`.*
