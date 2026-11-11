# Enemy Profile: [DISPLAY NAME]

*"[battle_intro line, exactly as it plays]"*

> **Template Version 1.0 — created 2026-11-11 at the author's request; pending author review**

<!--
HOW TO USE THIS TEMPLATE
This template is for REGULAR ENEMIES: the random-encounter and trash-mob bestiary
(street pests, coffeeshop creatures, tourist hordes). Named villains, minibosses, city
bosses and the finale use villain_template.md instead — every villain gets one.
If an "enemy" has a name, a racket, a phase change or a story tie, it is a villain.

One enemy per doc, or one doc per encounter family when the members share a concept
(fill the Identity, Stats and Moves sections once per member).

Rules that apply while filling it in:
- Read .claude/CLAUDE.md and the eurobound-satire-voice skill first.
- Enemy identity, stats, moves, rewards and drops need an author ruling. Anything you
  draft that the author has not ruled on is marked PROPOSED, in the field itself.
- Statuses come from design/mechanics/Battle/status_effects.md. A new status needs
  status_effect_template.md and an author ruling first.
- Stat names match the engine JSON (game/assets/data/enemies/[city]_enemies.json).
- Rewards are SOVS. The JSON field is still named gold_reward; the value is SOVS.
  Renaming the field is proposed engineering work, not something to do from this doc.
- Replace every [bracketed placeholder]. Delete this comment block before publishing.
- Keep every H2 header (with its emoji) and every table's column shape exactly as here.
-->

## 📋 Enemy Identity
- **Enemy ID**: `[enemy_name_snake_case]` (the key in `[city]_enemies.json`; grep the repo to confirm it is unique)
- **Display Name**: [Funny, unique name — what the battle UI shows]
- **City**: [Debaucheryville / Sinfonia / Publandia / Shamsterdam]
- **Zone / Encounter Table**: [District, venue or dungeon where it spawns]
- **Encounter Family**: [e.g. Street & District / Coffeeshop Creatures — matches the city overview's Enemy Encounters heading]
- **Group Size**: [Solo / 2–3 / swarm of N]
- **Overview Source**: `design/worlds/[city]/[city].md` → Enemy Encounters (the one-line concept this doc expands)

---

## 🎭 Core Concept

### What It Actually Is
[One line. The reality: who or what this is and why it is hostile.]

### What The Bros Think It Is
[One line. The bros' read. They are never afraid — annoyed, overconfident, flattered, or trying to network with it.]

### The Comedy Gap
[Internal only. Never explain the joke in battle text.]

---

## ⚔️ Combat Specification

### Core Stats (engine fields)
| Stat | Value | Notes |
|------|-------|-------|
| `max_hp` | [X] | [Rolling HP meter applies] |
| `offense` | [X] | |
| `defense` | [X] | |
| `speed` | [X] | |
| `luck` | [X] | |
| `charm` | [X or —] | [Optional; resists/drives social attacks] |
| `grit` | [X or —] | [Optional; crit resist] |

### Moves (1–3; data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight | Battle Text |
|------|------|--------|------------------|--------|-------------|
| [Move 1] | [Physical / Social / Gimmick / AoE] | [Damage word or effect] | [Status or —] | [%] | "[Log line]" |
| [Move 2] | | | | [%] | "[Log line]" |
| [Move 3] | | | | [%] | "[Log line]" |

### Weaknesses & Resistances
| Category | Detail |
|----------|--------|
| **Weak against** | [What works — and why it's funny] |
| **Resistant to** | [Damage types / statuses, with %] |
| **Immune to** | [Statuses, or "none"] |

### Intoxication Hook (only if it inflicts or feeds on drinking or drugs)
[An enemy that inflicts an alcohol or drug status (Contact High Cloud, a shot-pushing promoter) follows `design/mechanics/intoxication_law.md`: alcohol escalates Buzzed → Beer Goggles → Shitfaced → Catastrophe; loss of control is bounded, readable and recoverable; run the law's 10-point design review (§8) for any new mechanic. Delete this subsection if it does not apply.]

---

## 💬 Battle Text

| Moment | Line |
|--------|------|
| `battle_intro` | "[Appears at fight start — matches the subtitle above]" |
| On defeat | "[Deadpan log line]" |
| On fleeing (if it can flee) | "[Line]" |
| Bro reaction (optional) | **[Bro]**: "[Line — never afraid, never self-aware]" |

---

## 💰 Rewards & Drops

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."

Junk drops are welcome and get real inspect microcopy (use `consumable_item_template.md`, `equipment_template.md` or `permanent_item_template.md` for the dropped item itself).

| Reward | Engine Field | Value | Notes |
|--------|--------------|-------|-------|
| XP | `xp_reward` | [X] | |
| SOVS | `gold_reward` | [X] | Value is SOVS; field rename pending |
| Item drop | `item_drop` | `[item_key]` or none | [Must exist in an item JSON or be specced] |
| Drop chance | `drop_chance` | [0.0–1.0] | |
| Other (tickets, collectibles) | [PROPOSED field] | [Value] | [Notes] |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Battle Sprite** | [Pose, facing (battle sprites face west), size, palette] |
| **Palette Swaps** | [Any recolors used as tougher variants, with names] |
| **Text/Markings** | [Exact text on clothing or props. Read and fix every word on generated art] |
| **Overworld Sprite** | [If it is visible before the fight, or "random encounter only"] |
| **Filename** | [`snake_case_filename.png` or "not yet specced"] |

---

## ⚙️ Engine Entry (`[city]_enemies.json`)

```json
"[enemy_name_snake_case]": {
  "display_name": "[Display Name]",
  "battle_intro": "[Line]",
  "max_hp": [0],
  "offense": [0],
  "defense": [0],
  "speed": [0],
  "luck": [0],
  "xp_reward": [0],
  "gold_reward": [0],
  "item_drop": "[item_key]",
  "drop_chance": [0.0]
}
```

| Field | Value |
|-------|-------|
| **Fields the schema does not have yet** | [Moves, statuses, weaknesses. List what this enemy needs; schema additions are proposed engineering work and need an author ruling] |
| **Registered** | [Yes/No] |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Enemy ID unique across the repo (grep) | ☐ |
| Display name funny and unique across the game | ☐ |
| Not a villain (no name-brand racket, phases or story tie) | ☐ |
| Concept: actual vs believed written | ☐ |
| Stats use engine field names | ☐ |
| Statuses from the master list (or new and PROPOSED via status_effect_template.md) | ☐ |
| Rewards in SOVS; drops exist or are specced | ☐ |
| Junk drops have funny inspect microcopy | ☐ |
| Intoxication hook and 10-point review done (if it applies) | ☐ |
| No real city or place names in battle text | ☐ |
| Every unruled number marked PROPOSED | ☐ |
| Bros never afraid, disgusted or self-aware | ☐ |

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

- [Encounter-table weighting, zone dependencies]
- [Open question for the author]

---

## 🔧 Development Status

- **Status**: [Concept / Drafted / Author-Approved / Sprites Commissioned / Implemented]
- **File Location**: `design/worlds/[city]/enemies/[enemy_name].md` (PROPOSED folder — confirm with the author before the first doc lands)
- **Registered In**: `game/assets/data/enemies/[city]_enemies.json` [Yes/No]
- **Sprite**: [filename.png or "not yet specced"]

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial enemy doc | [name] |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `game/assets/data/enemies/debaucheryville_enemies.json`, `design/worlds/shamsterdam/shamsterdam.md` (Enemy Encounters) and the combat subset of `villain_template.md`. Villains use `villain_template.md`.*
