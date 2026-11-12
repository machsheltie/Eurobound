# One canonical shape for flag writes in data: PROPOSED

**Status:** PROPOSED, awaiting the author (Production Desk Eurobound-r8l8-q1). Nothing is migrated until it is approved.
**Bead:** Eurobound-r8l8. **Author's ruling (bead page, 2026-11-12, verbatim):** "Pick one canonical shape for new data and migrate the old (an agent proposes which)".
**Related:** `docs/superpowers/specs/2026-11-12-quest-flag-schema-proposal.md` §4.5 and §7 items 8-9 (APPROVED); Eurobound-pjas (validator tier 3).

---

## 1. What the data does today

No game code reads any of these keys. A grep of `game/**/*.gd` finds none of them, so every shape below is design intent waiting for an importer. Changing the shape breaks no running code.

| # | Shape | Where (file:line) | Count |
|---|---|---|---|
| 1 | `{"effect": "set_flag", "flag": "x", "value": true}` in an effect list | `design/worlds/publandia/events/cloverleaf_events.json:60, 125, 152, 224` | 4 |
| 2 | `"set_flag": {"x": true}` on a result object | `design/worlds/sinfonia/events/cafe_sachertorte_events.json:409, 422` | 2 |
| 3 | `"sets_flag": "x"` on a rule object | `design/worlds/sinfonia/core/stadtpark_gustavs_refuge_core.json:182`, `design/worlds/sinfonia/items/stadtpark_gustavs_refuge_items.json:262`, `design/worlds/sinfonia/items/cafe_sachertorte_items.json:216` | 3 |
| 4 | `"quest_flags_on_acquire": ["x"]` on an item | `design/worlds/debaucheryville/items/clock_wine_item.md:211` (JSON block inside the doc) | 1 |
| 5 | `"sets_state": "x"` on a reward or interaction | `design/worlds/debaucheryville/items/absinthe_arcade_items.json:105, 128`; `design/worlds/debaucheryville/interactions/absinthe_arcade_interactions.json:489, 545, 568`; `design/worlds/debaucheryville/location_nodes/astronomical_cockup_square_location_nodes.json:146`; `design/worlds/sinfonia/interactions/the_black_tie_backroom_interactions.json:330` | 7 |
| 6 | `{"action": "flag_set", "flag": "x"}` in a timeline | `design/worlds/sinfonia/events/stadtpark_gustavs_refuge_events.json:62, 83` | 2 |
| 7 | `"flag_set": "x"` on a reward or scene | `game/assets/data/npcs/easter_eggs.json:24, 48, 72, 97, 121, 144, 165`; `game/assets/data/locations/debaucheryville/debaucheryville_interactions.json:1791`; `game/assets/data/locations/debaucheryville/debaucheryville_environmental.json:3267, 3273` | 10 |
| 8 | `"sets_flags": ["x", "y"]` on a dialogue option or node | `game/assets/data/npcs/dialogue_trees/debaucheryville_dialogue.json:44, 83, 206, 227, 251` | 5 |

So there are eight shapes, not four, carrying 34 writes in 15 files. The legacy `Assets/Data/` tree repeats shapes 7 and 8 (`Assets/Data/npcs/easter_eggs.json`, `Assets/Data/npcs/dialogue_trees/debaucheryville_dialogue.json`, `Assets/Data/locations/debaucheryville/*.json`).

Not in scope: the quest JSON `quest_flags` blocks (`on_start`, `on_complete_a`, ...), which `check_quest` already owns, and read shapes (`flags_present`, `requires_flag_false`, `state_not_set`), which are conditions, not writes.

## 2. Recommendation: `"set_flags": {"<flag id>": <value>}`

One key, `set_flags`, whose value is an object mapping each flag id to the value it gets.

```json
"result": { "debt_cleared": true, "set_flags": { "debt_relief_claimed": true } }
```

In an effect list or a timeline, the entry keeps its list's own discriminator and carries the same object:

```json
{ "effect": "set_flags", "set_flags": { "entered_cloverleaf": true } }
{ "time": 24, "action": "set_flags", "set_flags": { "gustav_trust_earned": true } }
```

Why this shape:
1. **It fits anywhere.** Most writes sit on reward, result, rule or item objects, not in effect lists. A field drops onto any of them, so the migration changes keys, not structure. Shape 1 would force every reward object into an effect list.
2. **It carries values.** The registry has `int`, `array` and `dict` flags, and some bools are cleared (`debaucheryville.absinthe_arcade.cara_tab_open`, "cleared on payment"). A list of ids (shapes 3-8) can only ever write `true`.
3. **Several flags in one place.** Shape 8 already sets two flags at once. A map does that without repeating the key.
4. **One key for tools.** The validator and any importer walk the JSON and stop at every `set_flags` key, whatever the context. Today they would have to know eight key names and three nesting rules.
5. **The name matches the engine.** `GameState.set_flag()` (`game/core/game_state.gd:88`) is the call it lands on, and shape 2 already uses this form with a singular key.

Considered and not recommended:
- **Shape 1 (effect entry):** good inside effect lists, but most writes are not in one.
- **Shape 8 (`sets_flags` list):** compact, but cannot carry a value or clear a flag.
- **Read every shape forever:** the author ruled against this.

## 3. Migration list (after approval)

Each write moves to `set_flags` with value `true`, since every legacy write is a plain "set". Ids keep their spelling; renaming ids is separate (Eurobound-tzbu ruled the quest JSON ids only).

| File | Lines | Change |
|---|---|---|
| `design/worlds/publandia/events/cloverleaf_events.json` | 60, 125, 152, 224 | `{"effect": "set_flag", "flag": X, "value": V}` → `{"effect": "set_flags", "set_flags": {X: V}}` |
| `design/worlds/sinfonia/events/cafe_sachertorte_events.json` | 409, 422 | `"set_flag"` → `"set_flags"` |
| `design/worlds/sinfonia/core/stadtpark_gustavs_refuge_core.json` | 182 | `"sets_flag": X` → `"set_flags": {X: true}` |
| `design/worlds/sinfonia/items/stadtpark_gustavs_refuge_items.json` | 262 | same |
| `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | 216 | same |
| `design/worlds/debaucheryville/items/clock_wine_item.md` | 211 | `"quest_flags_on_acquire": [X]` → `"set_flags_on_acquire": {X: true}` (an item's write fires on acquire, so the key names the trigger) |
| `design/worlds/debaucheryville/items/absinthe_arcade_items.json` | 105, 128 | `"sets_state": X` → `"set_flags": {X: true}` |
| `design/worlds/debaucheryville/interactions/absinthe_arcade_interactions.json` | 489, 545, 568 | same |
| `design/worlds/debaucheryville/location_nodes/astronomical_cockup_square_location_nodes.json` | 146 | same |
| `design/worlds/sinfonia/interactions/the_black_tie_backroom_interactions.json` | 330 | same |
| `design/worlds/sinfonia/events/stadtpark_gustavs_refuge_events.json` | 62, 83 | `{"action": "flag_set", "flag": X}` → `{"action": "set_flags", "set_flags": {X: true}}` |
| `game/assets/data/npcs/easter_eggs.json` | 24, 48, 72, 97, 121, 144, 165 | `"flag_set": X` → `"set_flags": {X: true}` |
| `game/assets/data/locations/debaucheryville/debaucheryville_interactions.json` | 1791 | same |
| `game/assets/data/locations/debaucheryville/debaucheryville_environmental.json` | 3267, 3273 | same |
| `game/assets/data/npcs/dialogue_trees/debaucheryville_dialogue.json` | 44, 83, 206, 227, 251 | `"sets_flags": [X, Y]` → `"set_flags": {X: true, Y: true}` |
| `Assets/Data/` mirrors of the four `game/` files above | as found | same, or skip if the author retires that tree |

Docs: `design/templates/sidequest_template.md` (Quest Flags section), `design/templates/consumable_item_template.md`, `permanent_item_template.md` and `equipment_template.md` gain one line naming `set_flags` (and `set_flags_on_acquire` for items). The schema proposal's §4.5 note ("Import has to read all three") gets a pointer here.

Two side effects to know about:
- `sets_state` on the Arcade interactions is the same idea as the Arcade's `state_tracking` keys. Moving it to `set_flags` makes those keys flags, which they already are in `quest_flags.json` (`sea_monkeys_obtained`, `broken_game_boy_found`, `absinthium_taproom_entrance_discovered`).
- `the_black_tie_backroom_interactions.json:330` sets `post_kings_were_humming`, and `astronomical_cockup_square_location_nodes.json:146` sets `post_clock_vulnerability`. Neither id is declared in `quest_flags.json`. The migration declares them, or files a bead if their meaning is unclear.

## 4. Validator change

In `Tools/validate_data.py` (engine data under `game/assets/data/`):
1. A recursive walk over every parsed JSON file, after the per-file checks. Any of the legacy keys (`set_flag`, `sets_flag`, `sets_flags`, `flag_set`, `sets_state`, `quest_flags_on_acquire`, an `"effect": "set_flag"` or `"action": "flag_set"` entry) is a FAIL naming the file, the JSON path and "use set_flags".
2. Every `set_flags` (and `set_flags_on_acquire`) value must be a non-empty object whose keys are strings and whose values are JSON scalars, arrays or objects.
3. Tier 3 (Eurobound-pjas) adds the cross-reference: every `set_flags` key must be declared in `quest_flags.json` (or match a `flag_patterns` family), and its value must match the declared `type`.

For design JSON under `design/worlds/`, which the validator does not load today: a `--design` switch that runs checks 1 and 2 over `design/**/*.json`, so new design data cannot copy a legacy shape. Unit tests for both go in `Tools/tests/test_validate_data.py`.

## 5. What approval unlocks

A follow-up bead: run the §3 migration and the §4 validator change in one change, so the validator goes green and stays green. Templates name the shape in the same change.
