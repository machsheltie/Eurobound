# Proposal: intoxicant fields for `consumables.json`

**Bead:** Eurobound-sue. **Status:** APPROVED as proposed (author, Production Desk `Eurobound-sue-q1`, 2026-11-12: "Approve as proposed"). Implemented in `consumables.json` and `Tools/validate_data.py` (Eurobound-sue); unruled values carry `null` plus a `_pending` note citing the doc line.
**Author answer that ordered this (2026-11-12):** "Yes: have a systems designer propose a field shape for my review".
**Serves:** `design/mechanics/intoxication_law.md` (§2 escalation, §3 bounded loss of control, §7 bounded durations and predictable recovery, §8 review point 9) and `design/narrative/bros_choose_debauchery.md` ("Intoxicants do not provide uncomplicated, consequence-free advantages"). Nothing here sets a number.

## 1. The split

The **item** says what happens when it is used: which status, how long, what happens on a re-hit, what comes after, what it costs. The **status** says what it does while active (stat deltas, cleaning or pacification hits, Bravado steal or drain, the overworld stop, the hostel hook, the alcohol-tier distortion). Status behaviour belongs in a status table, not in every item that applies it, so this ruling covers the item side only. The status table is a follow-up (§5).

## 2. New fields (all optional)

| Field | Type | Allowed values | Default when absent | Serves |
|---|---|---|---|---|
| `subtype` | string | `food`, `drink`, `vape`, `drug`, `coupon`, `junk` (author may add) | none | Item template "Subtype"; lets UI and the validator tell a vape from a kebab |
| `usable_in` | array of string | `battle`, `field` | `["battle","field"]` | Where the item menu offers it |
| `max_stack` | int ≥ 1 | any | no cap | Template "Stack Size". **Reuses the key the kebab coupon already has**, no new name |
| `price` | object `{coin, amount}` | `coin`: `sovs` or a master-pool ticker in lower case (`huff`); `amount`: int ≥ 0, or `null` = not ruled | not sold | Economy spec; crypto-only vendors (Tony420) |
| `bundles` | array of `{qty, amount}` | `qty` int ≥ 2; `amount` int, or `null` = "quoted at the point of sale"; same coin as `price` | none | Tony420 tiered deals |
| `intoxicant` | object, below | | not an intoxicant | Both laws |
| `intoxicant.status` | string | a status id, snake_case | required inside `intoxicant` | Law §8.2 immediate effect |
| `intoxicant.duration` | object `{battle_turns, field_steps, ends_on_rest}` | ints ≥ 1 or `null` = not ruled; bool | required | Law §3 and §7: every loss of control is bounded |
| `intoxicant.stack_rule` | string | `extend` (re-hit adds the duration again), `refresh` (re-hit resets it), `none` (re-hit does nothing) | `refresh` | Law §8.3 escalation conditions |
| `intoxicant.then` | object `{status, stacks}` | `status`: a status id that fires when the main status ends; `stacks`: bool, each re-hit while active adds one more | none | "No free advantage": the bill (Crash, Cottonmouth) |

`alcohol: true` is untouched and stays separate: it is the drink flag GameClock reads (10 clock minutes, round v37) and the alcohol ladder's input. A drink that also applies a status uses both.

## 3. Existing entries stay valid

Every new field is optional, and an absent field means today's behaviour. The validator's required list (`display_name`, `heal_hp`, `heal_bravado`, `description`) does not change. `alcohol`, `revive_pct`, `cures_status`, `source`, `max_stack` and the coupon's ad-hoc `effect` block keep their meaning. No entry has to be edited for the new shape to land.

## 4. Example only: the two items in the new shape

`"AUTHOR"` marks every value no ruling has set; the implementation would carry `null` there. Numbers come from the item docs and nowhere else.

```json
"strawberry_shortcake_speedcakes": {
  "display_name": "STRAWBERRY SHORTCAKE SPEEDCAKES™", "heal_hp": 0, "heal_bravado": 0,
  "description": "Tastes like strawberry frosting licked off a car battery.",
  "subtype": "vape", "usable_in": "AUTHOR", "max_stack": "AUTHOR",
  "price": {"coin": "huff", "amount": 420},
  "intoxicant": {
    "status": "sugar_rush_hour",
    "duration": {"battle_turns": "AUTHOR", "field_steps": "AUTHOR", "ends_on_rest": true},
    "stack_rule": "extend",
    "then": {"status": "crash", "stacks": true}
  }
},
"mango_og_gushers": {
  "display_name": "MANGO OG GUSHERS™", "heal_hp": 0, "heal_bravado": 0,
  "description": "You remember the commercials being more innocent.",
  "subtype": "vape", "usable_in": "AUTHOR", "max_stack": "AUTHOR",
  "price": {"coin": "huff", "amount": "AUTHOR"},
  "bundles": [{"qty": 2, "amount": 690}, {"qty": 3, "amount": 1000}, {"qty": 4, "amount": null}],
  "intoxicant": {
    "status": "gush_locked",
    "duration": {"battle_turns": "AUTHOR", "field_steps": "AUTHOR", "ends_on_rest": "AUTHOR"},
    "stack_rule": "extend",
    "then": {"status": "cottonmouth", "stacks": true}
  }
}
```

Sources: 420 $HUFF, "ends on its timer or at the next hostel rest", "extends the compulsion and stacks the Crash" (Speedcakes doc, Economic Details and review points 3 and 6). 2 for 690, 3 for 1000, 4 quoted later, "extends the duration and stacks the coming Cottonmouth" (Mango doc, Bundle Deals and Effects table). Mango's doc says Gush-Locked runs on turns and steps; it does not say whether a rest ends it, so `ends_on_rest` is AUTHOR. Neither doc rules whether the vape can be used mid-battle.

## 5. What BattleCore would need (described, not coded)

- `has_battle_effect()` also counts an `intoxicant.status`; today both items return false (0 HP, 0 Bravado) and never appear in the battle item menu. `usable_items()` filters on `usable_in`.
- `use_item()` applies `intoxicant.status` through `_apply_status()` with `duration.battle_turns`, honouring `stack_rule`. Today `_apply_status()` overwrites the turn count, so `extend` needs a new branch. It also bumps a pending count for `then` when `stacks` is true.
- When the status runs out, the turn tick fires `then.status` (Crash already has design numbers in `design/mechanics/Battle/status_effects.md`: −3 all stats, 75% skip, 3 turns). Crash, Sugar Rush Hour, Gush-Locked and Cottonmouth do not exist in the engine yet.
- Statuses live on `BattleUnit` and end with the fight. `field_steps` and `ends_on_rest` need party statuses to persist in `GameState` (and its save) across battles and the overworld.
- `_status_name()` builds names from ids ("gush_locked" becomes "Gush Locked", losing the hyphen), so these statuses need a display-name entry.
- The behaviour itself (cleaning hits, pacification hits, Bravado steal or drain, the Stare, the Munchies Tax, tier distortion, the cross-status rules) lives in the status table and in battle, overworld and rest hooks: separate engineering beads, each still owing numbers to the balancing pass.
- `Tools/validate_data.py` gains optional-field type checks: the enums above, `price.coin` against the master pool, `intoxicant.status` and `then.status` against the status table.
