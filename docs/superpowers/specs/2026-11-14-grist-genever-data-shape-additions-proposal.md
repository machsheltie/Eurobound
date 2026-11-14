# Proposal: five data-shape additions for the ruled Grist and Genever values

**Status: PROPOSED, waiting on the author (Eurobound Desk `Eurobound-cvkq-q1`).** Nothing here is canon until approved.
**Bead:** Eurobound-cvkq (found by Eurobound-xmyi).
**Author answer that ordered this (bead page, 2026-11-13), verbatim:** "Have a systems designer propose shape additions for my review".
**Builds on the two approved shapes:**
- item side: `docs/superpowers/specs/2026-11-12-consumable-intoxicant-fields-proposal.md` §2 (Production Desk Eurobound-sue-q1, "Approve as proposed");
- status side: `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md` §3 (Production Desk Eurobound-1m4-q1, "Approve as proposed"), with its `clock_minutes` note (`:82`).

**This proposal sets no balance number.** Every number in the examples is one the author already approved (Eurobound Desk eb8-q1, `docs/superpowers/specs/2026-11-12-grist-genever-review-numbers-proposal.md` §3-§5; Eurobound Desk vt7k-q2 for the Space Cake cap). What is PROPOSED is the field names, where each field lives, and the small reading rules marked PROPOSED in §3. All five fields are optional, and an absent field means today's behaviour, so no existing entry has to change.

**Serves:** `design/mechanics/intoxication_law.md` §7 (bounded durations) and `design/narrative/bros_choose_debauchery.md` l.16 (the drawback has to actually run in the engine).

---

## 1. The five ruled values with nowhere to go

| # | Ruled value | Where it is ruled | Where it sits today |
|---|---|---|---|
| 1 | The Shakes: −15 percentage points on the hit roll (95% to 80%), "not rounded to 9-point steps" | `design/items/brewery_tour/beer_bottoms_down_item.md:34` (point 8) | `the_shakes.accuracy_steps` is null with a `_pending` note (`game/assets/data/skills/status_effects.json`, `the_shakes`). The hit roll reads steps only (`game/battle/battle_core.gd:553-560`) |
| 2 | Grist's Speed buff: 15% of Speed, rounded, at least +1 | `design/items/brewery_tour/beer_wobbly_windmill_brewery_item.md:12`, `:32` | `stats` takes whole-number deltas only (shape doc `:56`). The value lives in a note |
| 3 | Grist applies two statuses: the Speed buff (3 turns / 120 steps, refresh) and the Navigation penalty (200 steps, extend, no battle counter) | `beer_wobbly_windmill_brewery_item.md:12-13`, `:29`, `:32` | `intoxicant` names one status (item shape §2). It points at the penalty; the Speed buff has no status entry and no slot |
| 4 | Caps on extend: The Shakes 12 turns / 480 steps; Grist's Navigation penalty 800 steps (4 servings, R6) | `beer_bottoms_down_item.md:29`; `beer_wobbly_windmill_brewery_item.md:13` | No cap field. `Intoxicant.apply_field` (`game/core/intoxicant.gd:104-107`) and `BattleCore._apply_intoxicant` (`battle_core.gd:259-260`) add without limit, so a fifth serving goes past the cap today |
| 5 | Food that shortens The Shakes: Frietomat −2 turns / −80 steps a meal; Stroopwafel Cart −2 / −80; De Zilte Waarheid herring −1 / −40 | `beer_bottoms_down_item.md:32` (point 6); `design/worlds/shamsterdam/frietomat.md:271`; `stroopwafel_cart.md:254`; `de_zilte_waarheid.md:298` | `cured_by` and `cures_status` only end a status. Nothing shortens one |

A sixth value already works around the same gap: Space Cake Gamble's approved cap of 180 minutes is a code constant because the shape has no cap (`game/core/field_status.gd:53`, `:307-308`). Addition 4 below covers it.

---

## 2. The additions at a glance

| # | New field | Side | Type | Meaning | Absent means |
|---|---|---|---|---|---|
| 1 | `accuracy_points` | status | int or null | Percentage points added to the bearer's hit chance (negative = worse), on top of any `accuracy_steps` | no change to the hit roll |
| 2 | `stats_pct` | status | object: engine stat name → `{pct, min_points}` | A delta worked out as a percentage of the bearer's own stat | no percentage deltas |
| 3 | `intoxicant.also` | item | array of `{status, duration, stack_rule}` | Extra statuses the item applies with the main one | one status, as today |
| 4 | `stack_cap` | status | `{battle_turns, field_steps, clock_minutes}`, ints ≥ 1 or null | The most that can be **left** on each counter after an `extend` | no cap, as today |
| 5 | `shortens_status` | item | array of `{status, battle_turns, field_steps, clock_minutes}` | Using the item takes this much off a live status | the item shortens nothing |

---

## 3. Each addition

### 3.1 `accuracy_points` (status)

- **Rule (PROPOSED):** the hit chance is `95 + 9 × steps + points`, where `points` is the sum of `accuracy_points` over the bearer's live, unsuppressed statuses. Steps and points add; neither replaces the other.
- **Why a second field and not a change to `accuracy_steps`:** Sloppy (−3 steps) and Grease Fingers (−2 steps) are approved in steps (`docs/superpowers/NEXT_WORK.md:567`), and The Shakes is ruled in points on purpose. Two honest fields beat one field with a unit flag.
- **Value:** `the_shakes.accuracy_points: -15`. `the_shakes.accuracy_steps` is removed from the entry.
- **Hook:** one line in `BattleCore._hit` (`battle_core.gd:560`) and a `StatusTable.accuracy_points` reader beside `accuracy_steps`.
- **Not added:** a hit floor. The approved ruling adds none (`grist-genever-review-numbers-proposal.md` §4, "Hit floor").

### 3.2 `stats_pct` (status)

- **Shape:** `"stats_pct": {"speed": {"pct": 15, "min_points": 1}}`. `pct` is a whole number, positive for a buff and negative for a penalty. `min_points` is a whole number ≥ 0; absent means 0.
- **Rule (PROPOSED):** delta = `pct`% of the stat, rounded to the nearest whole point (halves round up), and never smaller in size than `min_points`. It then adds to the stat like a `stats` delta.
- **Which Speed (PROPOSED reading, please confirm):** the bro's own Speed from his sheet, before Bravado and before other statuses. That gives +1 for all three bros (Speed 5 / 7 / 8), which is the worked figure the author approved (`beer_wobbly_windmill_brewery_item.md:12`: "+1 for all three bros"). The approved text also says "High Bravado gives +2" (`grist-genever-review-numbers-proposal.md` §5). This proposal reads that as the size comparison it sits beside (High Bravado's own Speed shift is +2, `design/mechanics/Battle/battle_numbers_proposal.md:32`), not as "Grist gives +2 at High Bravado". If the author meant the second, the rule becomes "after Bravado", and only Bradley at High Bravado changes (15% of 10 = 1.5, rounds to +2).
- **Allowed stats:** the six the status table reads: offense, defense, speed, luck, grit, charm (`game/battle/status_table.gd:11`).
- **Hook:** `StatusTable.stat_delta` takes the bearer's base stat as an extra argument; `BattleUnit.battle_speed` and its three siblings pass it (`game/battle/battle_unit.gd:137-175`).

### 3.3 `intoxicant.also` (item)

- **Shape:** a list inside `intoxicant`. Each row is `{status, duration: {battle_turns, field_steps, ends_on_rest}, stack_rule}`, the same three keys the main block has. A row has no `then`; a follow-up stays on the main status.
- **Rule (PROPOSED):** every row is applied at the same moment as the main status, each with its own duration and its own stack rule. Rows are independent: one ending never ends another.
- **Why not turn `intoxicant` into a list:** every approved entry and every reader (`intoxicant.gd`, `Tools/validate_data.py`) treats `intoxicant` as one object. `also` leaves all of them valid.
- **Grist:** `intoxicant.status` stays `wobbly_windmill_navigation` (200 steps, extend). `also` adds the Speed buff: 3 turns / 120 steps, `refresh`.
- **New status entry it needs:** the Speed buff gets its own id, `wobbly_windmill_speed`, with `section: "positive"`, `scope: ["battle", "field"]`, and the `stats_pct` from 3.2.
- **Open for the author (content, not shape):** the buff's display name. Canon gives one name, "a Grist status row on the bro's Status card" (`beer_wobbly_windmill_brewery_item.md:30`). Two rows cannot both be called "Windmill Grist". This proposal invents no name: the entry carries a placeholder with a `_pending` note, and the name is settled with the drink's rename (Eurobound-jsc). The other route is one Status-card row that shows both readouts; say so on the Desk if you prefer it.
- **Hooks:** `Intoxicant.apply_field` and `BattleCore._apply_intoxicant` loop over `also` (`intoxicant.gd:88-114`, `battle_core.gd:243-268`).

### 3.4 `stack_cap` (status)

- **Shape:** `"stack_cap": {"battle_turns": 12, "field_steps": 480}`. Any of the three keys may be left out.
- **Rule (PROPOSED):** after an `extend`, each counter is cut back to its cap. The cap limits what is **left**, not the total ever served: a bro who has walked off half his Shakes can drink back up to 12 turns. This matches the approved Space Cake wording, "never more than 180 left" (`status_effects.json`, `space_cake_gamble._pending.stack_rule`).
- **Why on the status and not the item:** The Shakes comes from Oude Genever, Zeer Oude Jenever, a failed gauntlet round and the Couchsurf morning (`beer_bottoms_down_item.md:27`, `:29`). One cap on the status covers every source. A cap per item would have to be repeated on each and could disagree.
- **Values (all already approved):** `the_shakes` 12 turns / 480 steps; `wobbly_windmill_navigation` 800 steps; `space_cake_gamble` 180 clock minutes, which moves out of the code constant `FieldStatus.CLOCK_CAP_MINUTES` (`field_status.gd:53`).
- **Nobody is refused a drink.** The fifth serving is still bought and drunk, still heals, still counts on the alcohol ladder. Only the penalty's length stops growing, as approved (`grist-genever-review-numbers-proposal.md` §8, "Willing and delusional").
- **Hooks:** the two extend branches named in §1 row 4, and the clock extend (`field_status.gd:307-308`).

### 3.5 `shortens_status` (item)

- **Shape:** `"shortens_status": [{"status": "the_shakes", "battle_turns": 2, "field_steps": 80}]`. Whole numbers ≥ 1. It sits beside the existing `cures_status`.
- **Rule (PROPOSED):** when the bro uses or eats the item, each listed status he carries loses that much from each counter. If a counter reaches 0 the status ends the normal way, and any follow-up (`then`) still fires: food shortens the wait, it does not cancel the bill.
- **Why on the item:** the three rulings name the food, not the status's cure list (`frietomat.md:271`, "per meal"). `cured_by` on the status stays for full cures by kind (rest, any drink).
- **Values (all already approved):** every Frietomat meal and the Stroopwafel Cart's stroopwafel: 2 turns / 80 steps. De Zilte Waarheid's herring: 1 turn / 40 steps.
- **Dependency:** none of those foods is in `game/assets/data/items/consumables.json` yet. The field is ready for them; the values move in when the foods are engine-synced.
- **Hooks:** `FieldStatus.cure_by_item` (`field_status.gd:330`), which `GameState.use_item` already calls for every item (`game/core/game_state.gd:81-91`), and `BattleCore.use_item`.

---

## 4. The entries in the proposed shape

Only the new and changed fields are shown. Every number is an approved one.

```json
"the_shakes": {
  "accuracy_points": -15,
  "stack_cap": {"battle_turns": 12, "field_steps": 480}
},
"wobbly_windmill_navigation": {
  "stack_cap": {"field_steps": 800}
},
"wobbly_windmill_speed": {
  "display_name": "PLACEHOLDER (pending author, Eurobound-jsc)",
  "section": "positive", "scope": ["battle", "field"], "bearer": "bro",
  "default_duration": {"battle_turns": 3, "field_steps": 120, "ends_on_rest": true, "until_cured": false},
  "stack_rule": "refresh",
  "stats_pct": {"speed": {"pct": 15, "min_points": 1}}
},
"space_cake_gamble": {
  "stack_cap": {"clock_minutes": 180}
}
```

```json
"beer_wobbly_windmill_brewery": {
  "intoxicant": {
    "status": "wobbly_windmill_navigation",
    "duration": {"battle_turns": null, "field_steps": 200, "ends_on_rest": true},
    "stack_rule": "extend",
    "also": [
      {"status": "wobbly_windmill_speed",
       "duration": {"battle_turns": 3, "field_steps": 120, "ends_on_rest": true},
       "stack_rule": "refresh"}
    ]
  }
},
"<each Frietomat meal, and the stroopwafel, when synced>": {
  "shortens_status": [{"status": "the_shakes", "battle_turns": 2, "field_steps": 80}]
},
"<the herring, when synced>": {
  "shortens_status": [{"status": "the_shakes", "battle_turns": 1, "field_steps": 40}]
}
```

**Validator (`Tools/validate_data.py`, after approval):** `accuracy_points` int or null; `stats_pct` keys from the six stats, `pct` a non-zero int, `min_points` an int ≥ 0; `stack_cap` keys from the three counters, ints ≥ 1 or null, and an error if a status has a cap without `stack_rule: "extend"`; `intoxicant.also` rows checked like the main block, each `status` resolving in the status table; `shortens_status` rows with a resolving `status` and at least one counter. Each gets a test in `Tools/tests/test_validate_data.py`.

---

## 5. What this does not cover

- **Navigation −20 has no field** because Navigation is not an engine stat. It is read from `navigation/voetgangerstunnel.json` by status id (Eurobound-76gz, Eurobound-1esc). Unchanged.
- **The Space Cake landing's +40 Bravado and 15-second wobble** are code constants (`field_status.gd:50-51`), and their `_pending` note points at this bead. They are one-off landing events, not something a second status would reuse, so no field is proposed. If the author wants them in data, that is a sixth addition for another pass.
- **Percentage modifiers already hard-coded** (Embarrassed −20% attack, `game/battle/battle_rulings.gd:13`) stay where they are. Moving old statuses into the table belongs to Eurobound-70z (deferred by the author).
- **The Status-card name** of Grist's rows follows the Eurobound-jsc rename.

## 6. How this fits Eurobound-70z

Eurobound-70z owns the full schema for `status_effects.json` and is deferred. These five fields follow the same rule as the approved shape (shape doc §7): optional, absent means "does nothing", `schema_version` stays "1.0". 70z can rename or absorb them later without breaking the entries.

## 7. Intoxication law §8: 10-point review

The additions carry rulings into data. They add no mechanic and change no number, so each point records what stays true.

| # | Point | Answer |
|---|---|---|
| 1 | Source | Oude Genever (The Shakes) and Windmill Grist, both `alcohol: true`; the Space Cake for the moved cap. No source is added |
| 2 | Immediate effect | Unchanged. `accuracy_points` and `stats_pct` let the engine apply the ruled −15 points and +15% Speed instead of holding them in notes |
| 3 | Escalation | Unchanged: more servings last longer, never hit harder. `stack_cap` makes the approved 4-serving cap real; today the engine ignores it |
| 4 | Player-facing cues | Unchanged. The Speed buff needs a Status-card name (3.3, open) |
| 5 | Player control | Unchanged. No field here takes or returns control |
| 6 | Duration and recovery | Tighter than today: the caps bound every extend, and food shortens The Shakes as approved. Counters stay in the saved `FieldStatus` rows |
| 7 | Comedic consequence | Unchanged, and now enforced: with `also`, Grist's Speed buff finally exists in the engine and still runs out before the Navigation penalty |
| 8 | Interactions | Points and steps add in the hit roll, as approved for The Shakes with Sloppy and Grease Fingers. `shortens_status` never skips a follow-up |
| 9 | Technical dependencies (proposed engineering) | The hooks named in §3 (hit roll, percentage deltas, the `also` loop, the three extend caps, the shorten call), the validator checks and tests in §4. One gameplay-programmer bead after approval |
| 10 | Further author approval | The five field names and placements; the PROPOSED reading rules in 3.1-3.5; the "which Speed" reading in 3.2; the Speed buff's name in 3.3 |

Nothing here warns, explains or softens. The bros still drink the fifth one.

## 8. If approved

1. Add the five fields to the two shape proposals and the ledger (`docs/superpowers/NEXT_WORK.md`).
2. Validator checks and tests (§4).
3. Move the five values out of the `_pending` notes into real fields, add `wobbly_windmill_speed`, and move the 180-minute cap out of code. No number changes.
4. File the engine bead for §7 point 9.
