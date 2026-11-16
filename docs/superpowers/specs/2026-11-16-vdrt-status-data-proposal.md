# Proposal: the master status list, converted to the approved status-data shape

**Status: PROPOSED, waiting on the author.** Nothing here is in the live data. The live file `game/assets/data/skills/status_effects.json` is untouched.
**Bead:** Eurobound-vdrt. **Desk card:** `Eurobound-vdrt-q2`.
**Author answer that ordered this (bead page, 2026-11-16), verbatim:** "An agent converts the list to the approved data shape and flags every number that no longer fits, for my approval".
**Proposal data:** `docs/superpowers/specs/2026-11-16-vdrt-status-data-proposal.json` (same shape as the live file, plus three proposal-only top-level keys: `_descriptions`, `_flags`, and the two notes that explain them). The 21 entries pass `_check_status_entry` in `tools/validate_data.py`.
**Shape it follows:** `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md` (approved 2026-11-12, Eurobound Desk 1m4-q1; additions cvkq-q1, zcdf-q1).
**Source list:** `design/mechanics/Battle/status_effects.md` (118 lines).

## How the conversion worked

- **Names and descriptions are the list's own, word for word.** Display names are in each entry; the 21 descriptions are in `_descriptions` (the approved shape has no description field, see O4).
- **A number is entered only if the list gives it, it fits a shape field, and no later ruling or live data contradicts it.** There are 20 such numbers. They are still unruled: entering them is the proposal, approving the file is the ruling.
- **A number that conflicts, is a range, or has no field is not entered.** The field stays null (or is left out) and the reason is in `_pending` on the entry, or in `_flags` for things that have no field to hang a note on. Nothing is filled in to make a gap look closed.
- **Accuracy:** "-N Accuracy" is read as N steps, the way the engine already counts Sloppy and Grease Fingers (`game/battle/battle_core.gd:688-691`; shape doc section 1).
- **"All stats"** is the six combat stats, ruled 2026-11-13 (Eurobound Desk 64vo-q1, `docs/superpowers/NEXT_WORK.md:875`).
- **scope and bearer** are my reading of each line (see O5).

## Counts

| | |
|---|---|
| Statuses in the master list | 21 (6 positive, 8 negative, 4 neutral, 3 combo) |
| Entries in the proposal | 21: 20 new, plus Crash (already live, numbers filled from the list) |
| Numbers entered from the list, needing approval | 20 |
| Flags below | 40 (35 numbers or number-like items, 5 others) |
| Named by the GDD, defined nowhere, so not entered | Thirsty, Inspired |
| In code only, not in the list, not entered | Stun, Confused |

## Flags

`file:line` is given for both sides. "List" is `design/mechanics/Battle/status_effects.md`; "Ledger" is `docs/superpowers/NEXT_WORK.md`.

### A. The list number conflicts with a later ruling or live data (left null unless noted)

| # | Status | List says | The other side says | Proposal |
|---|---|---|---|---|
| A1 | Gains Bro | +2 Attack (List:9) | +20% ATK, ruled round v27 (Ledger:569; `game/battle/battle_rulings.gd:15` GAINS_BRO_ATK 1.2) | `stats.offense` null |
| A2 | Embarrassed | -2 Charm, -1 Confidence (List:47) | -20% ATK and -2 Bravado a turn (Ledger:569; `battle_rulings.gd:13-17`). Bead Eurobound-jsd0 is already open on this | `stats` null |
| A3 | Embarrassed | 2-3 turns (List:48) | 2 turns (Ledger:583; `battle_rulings.gd:39-41`), and a field version of 60 game-minutes that enters battle as 2 turns, 10% shorter per resistance point (Ledger:782-785; `game/core/field_status.gd:105-123`, `:768`) | duration null |
| A4 | Hydrated for Once | until next alcohol (List:15) | 5 turns (`design/items/docs/items.md:13`) | duration null |
| A5 | Hydrated for Once | +1 HP regen per turn (List:14) | +15% stamina (`design/mechanics/Battle/party.md:11`) | not entered |
| A6 | Hardcore Gamer | +1 Crit chance (List:29) | +1% crit (Ledger:569). Crit chance is not a shape field either | not entered |
| A7 | Caffeine Crash | 10 minutes real time (List:97) | the game has no real-time clock (`docs/superpowers/specs/2026-11-14-legendary-hangover-unit-and-rescale-proposal.md:42`); `clock_minutes` is game-clock | duration null |
| A8 | Crash | -3 all stats, 75% skip, 3 turns (List:108-109) | live values are all null (`game/assets/data/skills/status_effects.json:122`, `:124`, `:125`) | list numbers entered |
| A9 | Hungover | -2 all stats, 25% skip (List:36) | GDD says "-Offense, -Speed" (`design/game_design_document.md:14`) | list numbers entered, GDD is older |
| A10 | Grease Fingers | until washed or 4 turns (List:53) | 4 turns ruled (Ledger:583; `battle_rulings.gd:42`) | 4 entered, "washed" has no field |

### B. The number fits, but the engine already applies it by hand

Writing these live without removing the hard-coded line would count them twice.

| # | Status | Value | Hard-coded at |
|---|---|---|---|
| B1 | Sloppy | -3 steps | `game/battle/battle_core.gd:688-689` |
| B2 | Grease Fingers | -2 steps | `battle_core.gd:690-691` |
| B3 | Food Poisoning | 50% skip (List:81) | `battle_core.gd:524-526`. Its -2 HP a turn is at `:523` |

### C. Ranges (the shape holds one whole number per counter, left null)

| # | Status | List |
|---|---|---|
| C1 | Liquid Confidence | 3-5 turns (List:5) |
| C2 | Hungover | 3-5 turns (List:37) |
| C3 | Sloppy | 1-2 turns (List:43) |

### D. Numbers with no field in the shape (not entered)

| # | Status | List |
|---|---|---|
| D1 | Liquid Confidence | +2 Bravado (List:4). Not a stat; no one-off Bravado gain |
| D2 | Gains Bro | +1 Intimidation (List:9). Not an engine stat (`game/battle/status_table.gd:12`) |
| D3 | Manic | double actions per turn (List:19) |
| D4 | Heart Palpitations | +1 Priority next turn (List:24) |
| D5 | Heart Palpitations | -1 HP per turn (List:24). `bravado_tick` is Bravado only |
| D6 | Hardcore Gamer | -1 HP per turn (List:29), hard-coded at `battle_core.gd:527-528` |
| D7 | Hungover | -1 HP per turn (List:36) |
| D8 | Sloppy | 15% chance to hit allies (List:42), hard-coded at `battle_core.gd:670` |
| D9 | Grease Fingers | can't use tech items (List:52). `locks` covers Bravado skills only |
| D10 | Broke AF | -1 Confidence (List:57). Not an engine stat |
| D11 | Tourist Trap Victim | 2x shop prices (List:62) |
| D12 | Port-O-Cologne | -3 Charm with NPCs, +25% vendor prices (List:67) |
| D13 | The Herp | -2 Charm with NPCs (List:73) |
| D14 | Food Poisoning | -2 HP per turn (List:81), and the 5-8 battles length (List:82): the shape counts turns, steps and minutes, not battles (`battle_rulings.gd:31`) |
| D15 | Caffeine Crash | overworld move speed reduced (List:96) |
| D16 | Hydrated for Once | immunity to Hangover (List:14). `suppress` hides an active status; it does not block a new one |
| D17 | Existential Crisis | all abilities become "Question Life Choices" (List:115) |

### E. Scale

| # | Status | Note |
|---|---|---|
| E1 | Hungover -2, Crash -3 | The bros' stats run 2 to 12 (`docs/superpowers/specs/2026-11-14-legendary-hangover-unit-and-rescale-proposal.md:27-35`). Chadwick Grit 2 and Bradley Defense 2 hit the floor of 1 (the floor is ruled for Legendary Hangovers, Ledger:887). Probably fine; the author should know |
| E2 | Caffeine Crash -1 vs Crash -3 | Two statuses for one idea (energy-drink comedown), at two sizes (List:96, :108). Keep both, merge, or drop one? |

### O. Other flags (not numbers)

| # | Flag |
|---|---|
| O1 | **Thirsty and Inspired.** The GDD calls them core statuses (`design/game_design_document.md:14`, `:289`: "Thirsty (regen halved)", "Inspired (+Charm/+Crit)"). The master list does not define them, so there is nothing to convert. Not entered, not invented. |
| O2 | **Existential Crisis** was taken out of the Arcade villains (Ledger:423). Whether the status itself stays in the game is not ruled. Entered as listed. |
| O3 | **Blackout Drunk** (List:102-106) combines three things and wipes items. It is a consequence mechanic: `design/mechanics/intoxication_law.md` requires its 10-point design review before it is built, and nothing relates it to the law's Catastrophe tier (law lines 157-163). Entered with no effect fields. |
| O4 | **Descriptions have no home in the shape** (`STATUS_FIELDS`, `tools/validate_data.py:100-103`). They sit in `_descriptions` in the proposal. If the status card is to read them from data, a `description` field needs a ruling. |
| O5 | **scope and bearer are my reading.** The list never says them. Scope follows the line (a battle stat means battle; a shop or NPC effect means field). Bearer is "bro" throughout. Each one is a one-word edit if wrong. |

## Rules read

Intoxication law (`design/mechanics/intoxication_law.md`) and Bros Choose Debauchery (`design/narrative/bros_choose_debauchery.md`): the alcohol and caffeine buffs in the list (Liquid Confidence, Manic, Heart Palpitations, Hardcore Gamer) each carry a cost in the list's own text, so the "no free advantage" rule holds as written. Hydrated for Once is a buff with no cost, but it comes from water, not an intoxicant. No text was rewritten, so there is no satire change here. The law's 10-point review was not run, because this proposal adds no new intoxication mechanic; O3 is the one place it will be needed.

## If approved

1. Write the 20 new entries into `game/assets/data/skills/status_effects.json` and the Crash numbers over its nulls. Run `tools/validate_data.py`.
2. For B1 to B3, remove the hard-coded line in the same change, or leave that entry's number null.
3. Each unfilled field (A, C, D) stays a separate question or a balancing-pass task; nothing here closes them.
