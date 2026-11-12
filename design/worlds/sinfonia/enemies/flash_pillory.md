# Enemy Profile: Flash Pillory

*"Flash Pillory says the photo is free and the frame is not optional."*

> **Source and status.** [CANON — author approved, 2026-11-12, Eurobound-p1y] Approved on Production
> Desk `Eurobound-p1y-q2`, verbatim: "Approve all as drafted". Name, concept, gimmick, move names,
> status, junk drop and flavor lines are verbatim from the approved draft,
> `design/worlds/sinfonia/villains/the_golden_cutlet/roster_proposal_for_author.md` §5. Every field
> the draft does not cover is marked **PENDING (author)**; every number is **PENDING (balancing
> pass)**. The gimmick is approved as a concept; engine support is proposed engineering work.

## 📋 Enemy Identity
- **Enemy ID**: `flash_pillory` (the key in `sinfonia_enemies.json`; grep 2026-11-12: unique)
- **Display Name**: Flash Pillory
- **City**: Sinfonia
- **Zone / Encounter Table**: The Golden Cutlet, Heritage Vaults (basement). Which vault: **PENDING (author)** (dungeon layout is the author's).
- **Encounter Family**: Heritage Vault Staff
- **Group Size**: **PENDING (author)**
- **Overview Source**: `design/worlds/sinfonia/sinfonia.md` has no Enemy Encounters section yet; the concept source is the approved roster draft §5.

---

## 🎭 Core Concept

### What It Actually Is
A "court photographer" in a ruff who claps tourists into a portable wooden pillory, takes their picture, and sells it back to them in a cardboard frame. The photo is free. The frame is mandatory.

### What The Bros Think It Is
It's a photo op. They pose.

### The Comedy Gap
The souvenir photo upsell at every tourist attraction on earth.

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
He locks one bro in the stocks (that bro can use only Social moves), and every flash lowers the party's accuracy. Every photo he takes goes on a bill the bros pay after the battle unless they buy the prints back; the longer the fight, the bigger the bill. His *Proof Sheet* inflicts **Tourist Trap Victim**.

He is the only Golden Cutlet enemy that charges a post-battle bill (the On-The-House Wenches' tab pays off at The Schnitzel King's defeat instead). Accuracy loss per flash, SOVS per photo and the buy-back price: **PENDING (balancing pass)**.

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| Say Schnitzel | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Lock and Pose | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (balancing pass) | PENDING (author) |
| Proof Sheet | PENDING (author) | PENDING (author) | Tourist Trap Victim | PENDING (balancing pass) | PENDING (author) |

### Weaknesses & Resistances
| Category | Detail |
|----------|--------|
| **Weak against** | PENDING (author) |
| **Resistant to** | PENDING (author) |
| **Immune to** | PENDING (author) |

---

## 💬 Battle Text

| Moment | Line |
|--------|------|
| `battle_intro` | "Flash Pillory says the photo is free and the frame is not optional." |
| On defeat | "Flash Pillory goes down. The camera keeps shooting. Every shot is of the ceiling. You are invoiced for them." |
| On fleeing (if it can flee) | PENDING (author) |
| Bro reaction (in the stocks) | **Lord Pilsner**: "Is this the VIP section?" |
| Bro reaction | **Bradley**: "Dear's gonna love this one." |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Junk drops are welcome and get real inspect microcopy (use `consumable_item_template.md`, `equipment_template.md` or `permanent_item_template.md` for the dropped item itself).

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | PENDING (balancing pass) | |
| SOVS | `gold_reward` | PENDING (balancing pass) | Value is SOVS; field rename pending |
| Item drop | `item_drop` | [Souvenir Frame (Empty)](../../../items/sinfonia_items/souvenir_frame_empty_item.md) (`item_key` `souvenir_frame_empty`, proposed; not yet registered) | Junk drop; item doc with author-approved inspect microcopy (2026-11-12, Eurobound-2kty-q1). Engine registration: Eurobound-jlzw |
| Drop chance | `drop_chance` | PENDING (balancing pass) | |
| Other (tickets, collectibles) | PROPOSED field: post-battle print bill | PENDING (balancing pass) | A SOVS charge after the battle that grows with every photo taken, waived if the bros buy the prints back |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | Facing west; pose, size and palette PENDING (author) |
| **Palette Swaps** | PENDING (author) |
| **Text/Markings** | The frame reads "MY HERITAGE TRIAL" in gold foil. Read and fix every word on generated art |
| **Overworld Sprite** | PENDING (author) |
| **Filename** | not yet specced |

---

## ⚙️ Engine Entry (`sinfonia_enemies.json`)

`null` = PENDING (balancing pass). Not registered.

```json
"flash_pillory": {
  "display_name": "Flash Pillory",
  "battle_intro": "Flash Pillory says the photo is free and the frame is not optional.",
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
| **Fields the schema does not have yet** | Moves; locking one party member to Social moves only; party-wide accuracy loss per flash; a post-battle SOVS bill that grows with fight length, with a buy-back option. Schema additions are proposed engineering work and need an author ruling |
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
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ✅ Tourist Trap Victim |
| Rewards in SOVS; drops exist or are specced | ✅ junk drop specced in its item doc; bill in SOVS, amount pending |
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
- Move effects, types and battle text: PENDING (author); the draft named the moves and tied Tourist Trap Victim to *Proof Sheet* only.

---

## 🔧 Development Status

- **Status**: Author-Approved (concept, 2026-11-12); numbers pending the balancing pass
- **File Location**: `design/worlds/sinfonia/enemies/flash_pillory.md` (author ruling 2026-11-12, Eurobound-0q4x)
- **Registered In**: `game/assets/data/enemies/sinfonia_enemies.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Initial enemy doc from the approved roster draft (Eurobound-p1y) | world-builder agent |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `game/assets/data/enemies/debaucheryville_enemies.json`, `design/worlds/shamsterdam/shamsterdam.md` (Enemy Encounters) and the combat subset of `villain_template.md`. Villains use `villain_template.md`.*
