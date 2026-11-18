# Enemy Profile: Feral Segway Tourist

*"A Feral Segway Tourist rolls up aggressively!"*

> **Source and status.** Bead Eurobound-4jln (reverse documentation of an engine entry). Built from `design/templates/enemy_template.md`.
> - **Sourced:** the name, `battle_intro`, stats and rewards are copied from `game/assets/data/enemies/debaucheryville_enemies.json:5-16`. Eight approved villain docs (2026-11-09) use these numbers as their benchmark, for example `design/worlds/debaucheryville/villains/absinthe_arcade/kebab_kombat/condiment_clan_ninja.md:109` ("calibrated against the only shipped Debaucheryville enemy (Feral Segway Tourist: HP 28 / Off 6 / Def 3 / Spd 6 / Luck 2 / XP 12 / 8 SOVS)"). The others: `croc_monsieur.md:145`, `hit_and_ponder_hatchback.md:126`, `sinking_fund.md:136`, `count_continue.md:106`, `shish_kahn.md:118`, `player_two_palette_swap.md:96`, `super_turbo_hyper_jarmila.md:97`, `two_seventy_vratislav.md:103`.
> - **Where it came from:** the entry was first written as vertical-slice scaffolding (`docs/superpowers/plans/2026-07-30-vertical-slice.md:258-270`; placement at `:1126-1134`, "one Feral Segway Tourist roams the plaza"), not from an author brief. It is not on the city overview's Enemy Encounters list (`design/worlds/debaucheryville/debaucheryville.md:166-178`). In the game today it is spawned only by test fixtures (`game/tests/fixtures/street/street_encounter_test_screen.tscn:10`, `game/tests/unit/test_street_encounters.gd:11`).
> - **Not sourced:** every field below marked **PENDING (author)**. Nothing in this doc is invented, and nothing here changes engine data. Whether it stays goes on the Eurobound Desk (`Eurobound-4jln-q1`).

## 📋 Enemy Identity
- **Enemy ID**: `feral_segway_tourist` (the key in `debaucheryville_enemies.json:5`; grep 2026-11-17: no other use outside its data, tests and the benchmark notes)
- **Display Name**: Feral Segway Tourist (`debaucheryville_enemies.json:6`)
- **City**: Debaucheryville (`debaucheryville_enemies.json:3`, `"world_name": "debaucheryville"`)
- **Zone / Encounter Table**: PENDING (author). The vertical-slice plan put one on the plaza outside the Absinthe Arcade (`2026-07-30-vertical-slice.md:1126-1134`); no live scene spawns it
- **Encounter Family**: PENDING (author) (not on `debaucheryville.md:166-178`)
- **Group Size**: PENDING (author) (the plan spawns one)
- **Overview Source**: none. `design/worlds/debaucheryville/debaucheryville.md` → Enemy Encounters does not list it

---

## 🎭 Core Concept

### What It Actually Is
A tourist on a Segway (from the name). Anything beyond that is PENDING (author).

### What The Bros Think It Is
PENDING (author).

### The Comedy Gap
PENDING (author).

---

## ⚔️ Combat Specification

### Core Stats (engine fields)
| Stat | Value | Notes |
|------|-------|-------|
| `max_hp` | 28 | `debaucheryville_enemies.json:8` |
| `offense` | 6 | `:9` |
| `defense` | 3 | `:10` |
| `speed` | 6 | `:11` |
| `luck` | 2 | `:12` |
| `charm` | — | Not in the entry |
| `grit` | — | Not in the entry |

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| PENDING (author) | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (author) | PENDING (author) |

The entry has no moves; it uses the default attack.

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
| `battle_intro` | "A Feral Segway Tourist rolls up aggressively!" (`debaucheryville_enemies.json:7`) |
| On defeat | PENDING (author) |
| On fleeing (if it can flee) | PENDING (author) |
| Bro reaction (optional) | PENDING (author) |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | 12 | `debaucheryville_enemies.json:13` |
| SOVS | `sovs_reward` | 8 | `:14`. The engine field is `sovs_reward` (the template's `gold_reward` has been renamed in data) |
| Item drop | `item_drop` | `lukewarm_kebab` | `:15`; item doc `design/items/debaucheryville_items/lukewarm_kebab_item.md` |
| Drop chance | `drop_chance` | 1.0 | `:16` |
| Other (tickets, collectibles) | — | None | Not in the entry |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | PENDING (author). No art exists (no matching file under `game/assets/`) |
| **Palette Swaps** | PENDING (author) |
| **Text/Markings** | PENDING (author) |
| **Overworld Sprite** | PENDING (author) |
| **Filename** | not yet specced |

---

## ⚙️ Engine Entry (`debaucheryville_enemies.json`)

Copied from `game/assets/data/enemies/debaucheryville_enemies.json:5-16`, verbatim:

```json
"feral_segway_tourist": {
  "display_name": "Feral Segway Tourist",
  "battle_intro": "A Feral Segway Tourist rolls up aggressively!",
  "max_hp": 28,
  "offense": 6,
  "defense": 3,
  "speed": 6,
  "luck": 2,
  "xp_reward": 12,
  "sovs_reward": 8,
  "item_drop": "lukewarm_kebab",
  "drop_chance": 1.0
}
```

| Field | Value |
|-------|-------|
| **Fields the schema does not have yet** | PENDING (author): moves, statuses and weaknesses wait on a design |
| **Registered** | Yes |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Enemy ID unique across the repo (grep) | ☑ (grep 2026-11-17) |
| Display name funny and unique across the game | ☑ unique (grep 2026-11-17); funny: PENDING (author) |
| Not a villain (no name-brand racket, phases or story tie) | ☑ (none in data) |
| Concept: actual vs believed written | ☐ PENDING (author) |
| Stats use engine field names | ☑ |
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ☑ (none in data) |
| Rewards in SOVS; drops exist or are specced | ☑ (8 SOVS; `lukewarm_kebab` exists) |
| Junk drops have funny inspect microcopy | ☐ PENDING (author) (see the kebab doc) |
| Intoxication hook and 10-point review done (if it applies) | ☑ (does not apply in data) |
| No real city or place names in battle text | ☑ |
| Every unruled number marked PROPOSED | ☑ (every number is engine data; nothing proposed) |
| Bros never afraid, disgusted or self-aware | ☑ (no bro text) |

---

## 🚫 Warnings & Restrictions

### Content
- [ ] No narrator, disclaimer, moral framing, or any device that explains the joke; battle text never winks at the player
- [ ] Full-strength MA satire; no sanitized version, no safe-build swap. The only ceiling is no nudity
- [ ] Satire is sharp and specific — the bros' delusion AND the city's culture are both fair game (author ruling 2026-08-03: no punch-direction rules; "it's offensive" is not a design consideration)
- [ ] Enemies are never boring, corporate or professional, even the fine collector
- [ ] No mascots: no enemy joins the party, becomes a pet, or follows the bros afterwards
- [ ] Funny, unique name; no real place names in player-facing text; real brands, products and songs keep their real names

### Money & Crypto
- [ ] All money is SOVS ("40 SOVS", "1 SOV"); never euros, the € glyph or koruna
- [ ] Crypto content conforms to `design/economy/economy_system.md`; coins only from `design/economy/shitcoin_master_pool.md`

---

## 📝 Development Notes

- Its stats are the benchmark line for the Absinthe Arcade villains (see the source block). Changing them would not change those docs, but their notes compare against these numbers.
- It is the fixture enemy for the data validator tests (`Tools/tests/test_validate_data.py:631-646`) and the GUT street-encounter tests.
- Open for the author (Desk `Eurobound-4jln-q1`): does it stay as a street enemy, where it spawns, and who writes the PENDING text.

---

## 🔧 Development Status

- **Status**: Drafted (reverse-documented from engine data; identity text PENDING (author))
- **File Location**: `design/worlds/debaucheryville/enemies/feral_segway_tourist.md` (author ruling 2026-11-12, Eurobound-0q4x)
- **Registered In**: `game/assets/data/enemies/debaucheryville_enemies.json` Yes
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Enemy doc reverse-documented from engine data (Eurobound-4jln) | Claude (agent) |
