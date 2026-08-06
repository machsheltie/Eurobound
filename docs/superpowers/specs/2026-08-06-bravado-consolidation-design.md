# Bravado Consolidation — Design

**Date:** 2026-08-06
**Status:** Approved (author, 2026-08-06)
**Scope:** Make Bravado the engine's real resource stat, strike the invented Composure stat, add the
Bravado state machine and Ultimate gating, land the `key_items`/`equipment` schema and loader, and
add an ability template.

---

## 1. Problem

Five separate defects, all rooted in the same gap between design canon and engine data.

1. **The engine has no Bravado.** `design/mechanics/Battle/bravado.md` opens with "Bravado is the
   magic system of EuroBound." The engine instead has `max_sp` / `sp_cost` / `heal_sp`. No design
   doc anywhere defines SP. The engine name is vertical-slice placeholder naming for the thing
   canon calls Bravado.
2. **Composure was invented by an agent.** It appears in exactly two item docs, both from commit
   `97f63ed`, and in zero mechanics docs. Elsewhere in the repo it is ordinary prose, plus one PNG
   asset at Venustempel explicitly scoped to ambient visitor NPCs and flagged "never applied to the
   bros, who are not embarrassed by anything in this building."
3. **No Bravado state machine, no Ultimate gating.** `bravado.md` specifies four states and an
   Ultimate lockout. The engine implements none of it — `grep -i ultimate` over every `.gd` file
   outside `addons/` returns nothing.
4. **`key_items.json` and `equipment.json` are unreadable.** Both are empty, and `data_repo.gd:27`
   loads only `consumables.json`. The `eurobound-item-engine-sync` skill routes most items to
   `key_items.json`, so it writes data nothing consumes.
5. **Abilities have no template.** Items, quests, NPCs, villains, locations, NFTs, and PNG specs all
   have one in `design/templates/`. Abilities do not.

---

## 2. Ruling: Bravado replaces SP

SP and Bravado are the same resource. The engine is renamed to canon.

| Old | New |
|---|---|
| `max_sp` | `max_bravado` |
| `sp` (runtime) | `bravado` |
| `sp_cost` | `bravado_cost` |
| `heal_sp` | `heal_bravado` |

This touches, and only touches:

- `game/assets/data/party/party_members.json` — `max_sp`
- `game/assets/data/skills/party_abilities.json` — `sp_cost`
- `game/assets/data/items/consumables.json` — `heal_sp`
- `game/core/game_state.gd:33-34,56`
- `game/battle/battle_manager.gd:84-86,102-106`
- `game/tests/unit/test_data_repo.gd:25`
- `game/tests/unit/test_game_state.gd:16`
- `Tools/validate_data.py` — the `REQUIRED` key list

The user-facing battle label changes from `SP %d/%d` to `Bravado %d/%d`.

---

## 3. Ruling: the Bravado state machine

Four states over a 0–100 bar.

| State | Value | Effect |
|---|---|---|
| Zero | 0 | Bravado moves unavailable. Basic attacks still work. |
| Low | 1–25 | Ultimates locked out. Ordinary specials usable if affordable. |
| Mid | 26–70 | Normal operation. |
| High | 71–100 | Flavor state only — no mechanical effect. |

**Zero Bravado does NOT cause collapse or forced retreat.** Author ruling, 2026-08-06. Running out
of Bravado means only that Bravado cannot be spent. Collapse belongs to HP reaching zero.

`design/mechanics/Battle/bravado.md` currently states the opposite — "Zero Bravado: 'Dad on a
Bender' collapse — dropped animations, forced retreat if not restored." That line is struck and the
doc corrected. The legacy copy under `design/legacy/` is left alone; it is legacy.

The four states are exposed as a function of the current value, not stored state. There is one
source of truth — the number — and the band is derived from it.

---

## 4. Ruling: Ultimate gating

Ultimates are gated but not authored. Author ruling: build the flag and threshold now, defer
creating actual Ultimate abilities.

- An ability may carry `"is_ultimate": true`. Absent, it is an ordinary ability.
- An Ultimate cannot be used while Bravado is in the Zero or Low band.
- The refusal is surfaced to the player, not silent.
- No Ultimate ability is added to `party_abilities.json` in this work. The four named in the
  character docs — Fratocalypse Now, Final Round's On Me, Global Trend, Mid-Life Crisis — need
  damage numbers, targeting, and failure states that are not yet specified, and each needs its own
  author ruling.

The gating path is covered by tests using a fixture ability, so the mechanism is proven without
inventing content.

---

## 5. Ruling: item stat vocabulary

Item stat blocks use two stat keys and no others:

- `bravado`
- `charm`

**Charm** is an existing engine stat and a world stat — it flavors NPC interaction, including the
Couchsurfing Chronicles hosts. The eight audience-split variants found across item docs
(`Charm (Tourists)`, `Charm (Locals)`, `Charm (Backroom staff)`, and five more) collapse into the
single `charm` key. Author ruling: charm can be combined.

**Composure is struck.** Removed from `design/items/gold_circle_coin_item.md` and
`design/items/leopard_print_thong_item.md`, folded into Bravado. Bravado already models
embarrassment — `bravado.md` specifies "Embarrassed: drains Bravado per turn; disables Ultimate
gain" — so nothing is lost.

**One-off flavor stats stay in the design docs and never reach JSON.** Club Entry, Airport Security,
Gold Value, Herp Suppression, Bro Credibility, Party Prep, Perceived Confidence, Resolve, and Sun
Protection each appear exactly once. They are jokes, and they are funnier in the doc than they would
be as engine fields.

---

## 6. Ruling: `key_items` and `equipment` schema

```json
"item_vip_wristband_im_seven": {
  "display_name": "VIP All-Access Wristband",
  "description": "Level Seven access. Doesn't even exist in America.",
  "type": "permanent_cosmetic",
  "stats": { "bravado": 2, "charm": -1 }
}
```

- Keyed by Item ID, matching the `consumables.json` convention.
- `type` is one of `permanent_cosmetic`, `curse`, `quest` for `key_items.json`; for
  `equipment.json` it is the slot name.
- `stats` is optional. When present, its keys are limited to `bravado` and `charm`, and its values
  are signed integers — **not** the quoted strings (`"+2"`) used by
  `design/characters/PermanantCosmeticChanges/permanent_cosmetic_changes.json`. That file is a
  design artifact, not engine data, and is left untouched.
- `description` carries the item's voice from its design doc. A description that reads like a
  database field is a defect.

`data_repo.gd` gains loaders for both files, following the existing `_load_json` pattern. Unlike the
five current loads, an empty `key_items` or `equipment` object is **not** a failure — both files are
legitimately empty until items are authored, and failing startup on that would block the game.

`Tools/validate_data.py` gains both files in `REQUIRED`, with no required keys, so their presence
and parseability are checked without demanding content.

---

## 7. Ruling: ability template

`design/templates/ability_template.md`, following the conventions of `permanent_item_template.md`
and `sidequest_template.md`: an instructional comment block that is deleted on use, bracketed
placeholders, and a validation checklist.

It must capture what the engine actually reads — ability id, display name, `bravado_cost`,
`power_multiplier`, `battle_text`, `is_ultimate` — alongside the design-side material: which bro
owns it, the Bravado state it requires, its satirical framing, and its failure behavior.

Per `CLAUDE.md`, templates are floors, not ceilings.

---

## 8. Non-goals

- Authoring any actual Ultimate ability.
- Building the Bravado regen sources from `bravado.md` (NPC compliments, flex moments, drinking-game
  wins, party synergy). Those are battle-system work.
- The Ego Meter, a separate mechanic in `battle_system.md`.
- Touching `design/characters/PermanantCosmeticChanges/permanent_cosmetic_changes.json` or anything
  under `design/legacy/`.
- Migrating the 12 loose item docs in `design/items/`.
- An ability-creation skill to pair with the template. The template comes first; the skill is a
  separate decision.

---

## 9. Author rulings captured

Recorded 2026-08-06:

1. SP and Bravado are the same resource; rename the engine to Bravado.
2. Zero Bravado does not cause collapse or forced retreat — that is HP's job. It only means Bravado
   cannot be spent.
3. Build the Ultimate flag and threshold; defer authoring Ultimates.
4. Charm can be combined — the audience-split variants collapse to one stat.
5. Composure is struck and folded into Bravado.
6. Write the `key_items`/`equipment` loader now rather than later.
7. Add an ability template alongside the existing item and quest templates.
