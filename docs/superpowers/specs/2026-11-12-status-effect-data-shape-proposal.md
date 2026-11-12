# Proposal: status-effect data shape for `status_effects.json`

**Bead:** Eurobound-1m4. **Status:** PROPOSED, waiting on the author (Production Desk `Eurobound-1m4-q1`). Nothing in engine data or code has changed.
**Author answer that ordered this (bead page, 2026-11-12), verbatim:** "Yes: have a systems designer propose the status-data shape for my review".
**Serves:** `design/mechanics/intoxication_law.md` (§2, §3, §7, §8) and `design/narrative/bros_choose_debauchery.md` ("Intoxicants do not provide uncomplicated, consequence-free advantages").
**Builds on:** the approved item-side shape, `docs/superpowers/specs/2026-11-12-consumable-intoxicant-fields-proposal.md` (ledger: Production Desk Eurobound-sue-q1, "Approve as proposed").

**No numbers are invented.** Every delta, rate, chance and length is `null`, with a `_pending` note that cites the doc line it comes from (the same convention `consumables.json` already uses). The only integers in the examples are the two alcohol-ladder offsets in §4, which are approved design rules ("displays one step lower", "skips a tier upward"), not balance values. If the author wants them null too, they become null.

---

## 1. What exists today

| Fact | Where |
|---|---|
| `status_effects.json` is `{"schema_version": "1.0", "status_effects": {}}` | `game/assets/data/skills/status_effects.json` |
| A battle status is `id -> turns left`, counted down at the end of the bearer's own turn; `-1` = until cured | `game/battle/battle_unit.gd:28-29`, `:172-177` |
| Engine stats: `offense`, `defense`, `speed`, `luck`, `grit`, `charm`, `max_hp`, `max_bravado` | `battle_unit.gd:15-27`; template rule in `design/templates/status_effect_template.md` |
| Accuracy is not a stat. It is **steps**: 95% base, −9% per step (Sloppy −3, Grease Fingers −2) | `game/battle/battle_rulings.gd` (`BASE_HIT_PCT`, `HIT_PCT_PER_STEP`); `battle_core.gd:393-398` |
| Status behaviour is hard-coded by id: turn skips and DoTs (`_turn_lost`), redirects (`_redirect`), accuracy (`_hit`), attack and speed (`BattleUnit.attack_stat`, `battle_speed`), skill locks (`can_use_skill`), the enemy `NEGATIVE` list, `LASTING_STATUSES` | `battle_core.gd:17`, `:169-171`, `:292-319`, `:365-408`; `battle_unit.gd:132-155`; `battle_rulings.gd:30` |
| Display names are built from ids (`gush_locked` → "Gush Locked", hyphen lost) | `battle_core.gd:477-478` |
| Enemies have no Bravado. Their move resource is `sp`; moves cost it | `battle_unit.gd:104`; `battle_core.gd:603`, `:805` |
| A **field-status system exists**: saved in `GameState.flags.field_status`, units `clock` (game minutes) and `real` (seconds), ticked by `PlayerController`, carried into battle through `BATTLE_MAP` as `-1` (until cured). It has **no step unit** | `game/core/field_status.gd:1-49`, `:126-134`; `game/characters/player/player_controller.gd:174` |
| Dialogue choices already pass through a status hook (Green Fairy Confusion randomises the pick) | `game/worlds/debaucheryville/absinthe_arcade/dialogue_box.gd:74`; `field_status.gd:173-181` |
| An item can cure one named status (`cures_status`) | `battle_core.gd:203-207` |
| `GameClock.is_drink` means **alcoholic** (`alcohol: true`) only | `game/core/game_clock.gd:22-23` |
| Rest is `GameClock.rest` (next morning, 10:00) | `game_clock.gd:60-65` |
| The intoxication tier shows on each bro's menu card (`intoxication_tier`); the alcohol ladder itself is not built (Eurobound-p0j, deferred) | `game/ui/field_menu.gd:394-395` |
| Crash, Sugar Rush Hour, Gush-Locked, Cottonmouth and Hungover are not in the engine | grep of `game/` |

## 2. The split, and how "then" chains

The approved item shape already decides **what an item does when used**: which status, how long (`intoxicant.duration`), what a re-hit does (`intoxicant.stack_rule`), what follows (`intoxicant.then`). This proposal decides **what a status does while it is active**, in one place, so every item, enemy move or scene that applies it gets the same behaviour.

Rules that keep the two from overlapping:

1. **Duration:** the applier's duration wins. A status carries `default_duration` only for when nobody supplies one, which is exactly the case for a `then` follow-up (Crash after Sugar Rush Hour, Cottonmouth after Gush-Locked) and for enemy moves.
2. **Re-application:** the item's `stack_rule` governs an item re-hit. The status's own `stack_rule` covers only what the item shape leaves open: **how stacked follow-ups combine** when `then.stacks` is true and two or more are pending (the docs say Crash "Stacks per hit taken" and Cottonmouth is "Stacked by repeat hits of the vape", but not what a stack does).
3. **Chaining:** `then` stays on the item. A status may carry its own `then` (same `{status, stacks}` shape) only for chains that hold whatever applied it, such as the master list's "Manic" → "Crash" (`design/mechanics/Battle/status_effects.md:18-22`). None of the four uses it. If both exist, the item's wins.
4. **Cures:** the item's `cures_status` stays as it is. The status's `cured_by` covers cures by **kind** (any drink, any rest), which an item field can't express.

## 3. The shape

One entry per status id under `status_effects`. Only `display_name` is required. **Every other field is optional, and an absent field means "this status does not do that"**, so the statuses hard-coded today keep working untouched and nothing has to be migrated.

| Field | Type | Meaning | Serves |
|---|---|---|---|
| `display_name` | string | The name as the player sees it ("Gush-Locked") | Fixes the hyphen loss in `_status_name` |
| `section` | `positive` \| `negative` \| `neutral` \| `combo` \| null | Master-list section (`status_effects.md`) | Grouping; later replaces the hard-coded `NEGATIVE` list |
| `scope` | array of `battle`, `field` | Where it acts | Template "Scope" |
| `bearer` | `bro` \| `enemy` \| `any` | Who can carry it | Template "Applies To" |
| `default_duration` | `{battle_turns, field_steps, ends_on_rest, until_cured}` | Used only when the applier gives none (§2.1). Ints ≥ 1 or null; bools. `until_cured: true` means the counters are ignored and only `cured_by` (or rest, if `ends_on_rest`) ends it | Law §3, §7 (bounded) |
| `stack_rule` | `extend` \| `refresh` \| `intensify` \| `none` \| null | How stacked follow-ups combine (§2.2). `intensify` multiplies stat deltas by the stack count | Law §8.3 |
| `stats` | object: engine stat name → int delta; key `all` = every stat in the ruled set (§8 Q1) | Flat deltas while active | Speed/Defense/"all stats" |
| `accuracy_steps` | int | Added to the hit roll's steps (negative = worse) | "−Accuracy" |
| `skip_turn_chance` | float 0–1 | Rolled at the start of the bearer's turn | Crash's 75% skip |
| `damage_out_mult` | float | Multiplier on damage the bearer deals | Only needed if "Pacified/Mellowed" is ruled as "deals reduced damage" (Eurobound-4ug) |
| `bravado_tick` | `{battle_per_turn, field_amount, field_every_steps}` | Bravado gained (+) or drained (−) over time | Gush-Locked drain |
| `attack_conversion` | object, below | Turns the **Attack command** into something else | Cleaning hits, pacification hits |
| `attack_conversion.kind` | `cleaning` \| `pacification` | Which resolver runs after a landed hit | |
| `attack_conversion.applies_to` | `attack` | The Attack command only; skills and items unchanged (both docs say so) | Speedcakes doc :104, Mango doc :126 |
| `attack_conversion.damage_mult` | float | Damage multiplier on the converted hit | "reduced damage" |
| `attack_conversion.bravado_steal` | `{per_hit, cap}` | Moves `min(per_hit, target.sp)` from the enemy's `sp` to the bro's Bravado | Cleaning |
| `attack_conversion.inflict` | `{status, chance, turns}` | Status rolled onto the target after a landed hit | Pacification |
| `attack_conversion.battle_text` | array of string, tokens `{user}` `{target}` `{amount}` | Replaces "X attacks!" (same tokens as skills' `battle_text`) | Approved battle lines |
| `attack_conversion.animation` | string | Battle-sprite animation id | Gush-Locked swing |
| `locks` | array of `bravado_cost_skills` \| `spoken_bravado_skills` | What the bearer can't use. `bravado_cost_skills` is what Embarrassed does today | Cottonmouth |
| `field.compulsion` | `{kind, every: {amount, unit}, lasts_seconds, input_lock}`; `kind`: `clean_nearest_interactable` \| `stare`; `unit`: `steps` \| `real_seconds` | Bounded overworld loss of control | Law §3, §7 |
| `field.text_speed_mult` | float | Dialogue scroll speed while active | Sped-up / crawling text |
| `field.text_filter` | `trailing_ellipsis` | Text decoration on the bro's lines | Mango cue ("bro...") |
| `field.choices` | `{mode, pool}`; `mode`: `shuffle` \| `replace` | `shuffle` = the existing Green Fairy behaviour; `replace` = swap options for lines from `pool` | Cottonmouth scramble; law §3 |
| `on_rest` | array of `{event, flag, ...params}` | Events the rest scene runs while the status is active, **before** `ends_on_rest` removes it | Deep clean, Munchies Tax |
| `ladder` | `{display_offset, gain_bonus}` | `display_offset`: shown tier = real tier + offset (display only). `gain_bonus`: a tier gain while active lands this many extra steps up, capped at Catastrophe | Tier display shift, cross-fade |
| `interactions` | array of `{with, rule, ...}` | `suppress`: `with` has no effect while this is active. `cancel_into`: both are removed and `into` is applied (symmetric; written on one side only). `modify_then`: changes the named follow-up. `unaffected`: a guard that records an approved non-interaction | Law §8.8 |
| `cured_by` | array of `{kind, value}`; `kind`: `rest` \| `item_subtype` \| `item_id` | Class-based cures | Cottonmouth |
| `then` | `{status, stacks}` | Status-native chain only (§2.3) | Manic → Crash, later |
| `cues` | `{icon, idle_anim, particle}` | Asset ids for the visible cues | Law §8.4 |
| `_pending` | object: dotted path → note | Why a value is null and where it comes from | Same as `consumables.json` |

## 4. The four statuses in this shape

Text in `battle_text` is copied only where the author approved it. Flag names marked PROPOSED in the item docs stay PROPOSED here.

```json
{
  "schema_version": "1.0",
  "status_effects": {
    "sugar_rush_hour": {
      "display_name": "Sugar Rush Hour",
      "section": null,
      "scope": ["battle", "field"],
      "bearer": "bro",
      "default_duration": {"battle_turns": null, "field_steps": null, "ends_on_rest": true, "until_cured": false},
      "stats": {"speed": null},
      "accuracy_steps": null,
      "attack_conversion": {
        "kind": "cleaning",
        "applies_to": "attack",
        "damage_mult": null,
        "bravado_steal": {"per_hit": null, "cap": null},
        "battle_text": null,
        "animation": null
      },
      "field": {
        "compulsion": {"kind": "clean_nearest_interactable", "every": {"amount": null, "unit": null}, "lasts_seconds": null, "input_lock": true},
        "text_speed_mult": null
      },
      "on_rest": [{"event": "deep_clean", "flag": "speedcakes_deep_clean_pending", "sorts_inventory": true, "discards": null, "never_discards": "key_items"}],
      "ladder": {"display_offset": -1},
      "interactions": [
        {"with": "hungover", "rule": "suppress"},
        {"with": "port_o_cologne", "rule": "unaffected"}
      ],
      "cues": {"icon": null, "idle_anim": null, "particle": null},
      "_pending": {
        "section": "pending author: mixed buff and debuff; Manic, its nearest kin, sits under POSITIVE (design/mechanics/Battle/status_effects.md:18)",
        "default_duration.battle_turns": "balancing pass: strawberry_shortcake_speedcakes_item.md:93 ('Short, TBD'); the item's intoxicant.duration overrides this",
        "default_duration.field_steps": "balancing pass: strawberry_shortcake_speedcakes_item.md:94 ('Bounded, TBD')",
        "stats.speed": "balancing pass: strawberry_shortcake_speedcakes_item.md:93 ('+Speed (TBD)')",
        "accuracy_steps": "balancing pass: strawberry_shortcake_speedcakes_item.md:93 ('−Accuracy (TBD)')",
        "attack_conversion.damage_mult": "balancing pass: strawberry_shortcake_speedcakes_item.md:102 ('Reduction: TBD')",
        "attack_conversion.bravado_steal.per_hit": "balancing pass: strawberry_shortcake_speedcakes_item.md:103 ('Amount stolen per hit ... TBD')",
        "attack_conversion.bravado_steal.cap": "balancing pass: strawberry_shortcake_speedcakes_item.md:103 ('cap ... TBD'); an enemy with 0 sp yields nothing, behaviour also TBD there",
        "attack_conversion.battle_text": "pending author: the two cleaning-hit lines are PROPOSED, not approved (strawberry_shortcake_speedcakes_item.md:106-111, :153)",
        "attack_conversion.animation": "pending sprite work: no cleaning-hit animation is specified",
        "field.compulsion.every": "balancing pass: strawberry_shortcake_speedcakes_item.md:94 ('breaks off at intervals'), :243 ('compulsion interval'); steps or seconds not ruled",
        "field.compulsion.lasts_seconds": "balancing pass: strawberry_shortcake_speedcakes_item.md:148 ('walks off to clean the nearest interactable, then returns')",
        "field.text_speed_mult": "balancing pass: strawberry_shortcake_speedcakes_item.md:93 ('faster dialogue text'), :147",
        "on_rest.0.flag": "PROPOSED flag name: strawberry_shortcake_speedcakes_item.md:192 (the deep clean itself is approved, :94)",
        "on_rest.0.discards": "pending author: one thrown-away item per strawberry_shortcake_speedcakes_item.md:150; which item is open (:153), never a key item",
        "ladder.display_offset": "approved rule, not a balance value: strawberry_shortcake_speedcakes_item.md:116 ('displays one step lower')",
        "interactions.0": "approved: strawberry_shortcake_speedcakes_item.md:117 ('suppressed while active, returns when the Crash fires')",
        "interactions.1": "approved: strawberry_shortcake_speedcakes_item.md:118 ('He cleans everything except himself')",
        "cues": "pending art: pink sparkle-and-sponge icon, jaw-clench idle (strawberry_shortcake_speedcakes_item.md:147)"
      }
    },

    "gush_locked": {
      "display_name": "Gush-Locked",
      "section": null,
      "scope": ["battle", "field"],
      "bearer": "bro",
      "default_duration": {"battle_turns": null, "field_steps": null, "ends_on_rest": null, "until_cured": false},
      "stats": {"defense": null, "speed": null},
      "accuracy_steps": null,
      "bravado_tick": {"battle_per_turn": null, "field_amount": null, "field_every_steps": null},
      "attack_conversion": {
        "kind": "pacification",
        "applies_to": "attack",
        "damage_mult": null,
        "inflict": {"status": null, "chance": null, "turns": null},
        "battle_text": [
          "{user} slowly touches {target}'s shoulder and whispers, \"We don't need to fight, man. Look at your elbows.\" {target} is completely baffled.",
          "{user} takes a massive swing at {target}, forgets why his arm is up, and just leaves it there. {target} lowers their weapon out of second-hand awkwardness."
        ],
        "animation": null
      },
      "field": {
        "compulsion": {"kind": "stare", "every": {"amount": null, "unit": null}, "lasts_seconds": null, "input_lock": true},
        "text_speed_mult": null,
        "text_filter": "trailing_ellipsis"
      },
      "on_rest": [{"event": "munchies_tax", "flag": "mango_munchies_tax_pending", "food_items": null, "sovs": null}],
      "ladder": {"gain_bonus": 1},
      "interactions": [
        {"with": "hungover", "rule": "suppress"},
        {"with": "hungover", "rule": "modify_then", "then": "cottonmouth", "effect": null},
        {"with": "sugar_rush_hour", "rule": "cancel_into", "into": null}
      ],
      "cues": {"icon": null, "idle_anim": null, "particle": null},
      "_pending": {
        "section": "pending author: mixed buff and debuff (mango_og_gushers_item.md:114)",
        "default_duration.battle_turns": "balancing pass: mango_og_gushers_item.md:114 ('turns in combat ... TBD')",
        "default_duration.field_steps": "balancing pass: mango_og_gushers_item.md:114 ('step count in the overworld, TBD')",
        "default_duration.ends_on_rest": "pending author: mango_og_gushers_item.md:179 names turns and steps only (same open point as consumables.json)",
        "stats.defense": "balancing pass: mango_og_gushers_item.md:114 ('+Defense ... All amounts TBD')",
        "stats.speed": "balancing pass: mango_og_gushers_item.md:114 ('−Speed')",
        "accuracy_steps": "balancing pass: mango_og_gushers_item.md:114 ('−Accuracy')",
        "bravado_tick.battle_per_turn": "balancing pass: mango_og_gushers_item.md:115 ('Rate TBD'); negative = drain",
        "bravado_tick.field_amount": "pending author: mango_og_gushers_item.md:115 says 'over time'; whether the drain also runs on the overworld is not ruled",
        "bravado_tick.field_every_steps": "pending author: as above",
        "attack_conversion.damage_mult": "balancing pass: mango_og_gushers_item.md:123 ('Reduction: TBD')",
        "attack_conversion.inflict.status": "pending author (Eurobound-4ug): 'Pacified' or 'Mellowed', mango_og_gushers_item.md:124; it gets its own entry here once named",
        "attack_conversion.inflict.chance": "balancing pass: mango_og_gushers_item.md:124",
        "attack_conversion.inflict.turns": "balancing pass: mango_og_gushers_item.md:124 ('skips its next turn or deals reduced damage': which one is Eurobound-4ug)",
        "attack_conversion.battle_text": "approved lines: mango_og_gushers_item.md:137-138 ([BRO] -> {user}, [ENEMY] -> {target}); the PROPOSED pairing with the animation (:140) is not encoded",
        "attack_conversion.animation": "pending sprite work: one Gush-Locked swing per bro, mango_og_gushers_item.md:131",
        "field.compulsion.every": "balancing pass: mango_og_gushers_item.md:117 ('interval ... TBD')",
        "field.compulsion.lasts_seconds": "balancing pass: mango_og_gushers_item.md:117 ('2–3 seconds per stop in the draft')",
        "field.text_speed_mult": "balancing pass: mango_og_gushers_item.md:175 ('text scroll slows to a crawl')",
        "on_rest.0.flag": "PROPOSED flag name: mango_og_gushers_item.md:223 (the Munchies Tax itself is approved, :118)",
        "on_rest.0.food_items": "balancing pass: mango_og_gushers_item.md:118 ('a random edible/consumable food item gone ... or ... SOVS gone'); whether it picks one or the other is not ruled",
        "on_rest.0.sovs": "balancing pass: mango_og_gushers_item.md:118 ('Amount TBD')",
        "ladder.gain_bonus": "approved rule, not a balance value: mango_og_gushers_item.md:145 ('skips a tier upward')",
        "interactions.0": "approved: mango_og_gushers_item.md:146 ('temporarily masks the Hungover penalty')",
        "interactions.1.effect": "pending author: mango_og_gushers_item.md:146 ('doubles the thirst of the Cottonmouth that follows'); 'thirst' has no mechanic yet (see §8 Q4)",
        "interactions.2.into": "pending author (Eurobound-4ug): existing 'confused' or a new status, mango_og_gushers_item.md:147",
        "cues": "pending art: half-lidded eyes, tropical smoke-cloud particle (mango_og_gushers_item.md:175)"
      }
    },

    "crash": {
      "display_name": "Crash",
      "section": "combo",
      "scope": null,
      "bearer": "bro",
      "default_duration": {"battle_turns": null, "field_steps": null, "ends_on_rest": null, "until_cured": false},
      "stack_rule": null,
      "stats": {"all": null},
      "skip_turn_chance": null,
      "_pending": {
        "scope": "pending author: master list defines Crash in battle turns only (design/mechanics/Battle/status_effects.md:106-109), but Sugar Rush Hour can end on the overworld or at a rest; does Crash wait for the next fight, or run on steps too? (§8 Q2)",
        "default_duration.battle_turns": "balancing pass: master-list figure is 3 turns (status_effects.md:108)",
        "default_duration.field_steps": "pending author: see scope",
        "default_duration.ends_on_rest": "pending author: not stated anywhere",
        "stack_rule": "pending author: 'Stacks per hit taken' (strawberry_shortcake_speedcakes_item.md:96) without saying whether a stack lengthens it (extend) or deepens it (intensify)",
        "stats.all": "balancing pass: master-list figure is −3 to all stats (status_effects.md:107); which stats 'all' covers is §8 Q1",
        "skip_turn_chance": "balancing pass: master-list figure is 75% (status_effects.md:107)"
      }
    },

    "cottonmouth": {
      "display_name": "Cottonmouth",
      "section": "negative",
      "scope": ["battle", "field"],
      "bearer": "bro",
      "default_duration": {"ends_on_rest": true, "until_cured": true},
      "stack_rule": null,
      "stats": {"all": null},
      "locks": ["spoken_bravado_skills"],
      "field": {"choices": {"mode": null, "pool": null}},
      "cured_by": [{"kind": "rest"}, {"kind": "item_subtype", "value": "drink"}],
      "cues": {"icon": null, "idle_anim": null, "particle": null},
      "_pending": {
        "stack_rule": "pending author: 'Stacked by repeat hits of the vape' (mango_og_gushers_item.md:119); with no timer, a stack could deepen the penalty or need one drink per stack (§8 Q3)",
        "stats.all": "balancing pass: mango_og_gushers_item.md:119 ('−1 all stats (draft figure, TBD)')",
        "locks": "approved: mango_og_gushers_item.md:119 ('no spoken Bravado abilities until he drinks something'); needs skills tagged as spoken (§8 Q5)",
        "field.choices.mode": "pending author: mango_og_gushers_item.md:119 ('dialogue choices scrambled with thirsty demands for liquid'): shuffle, replace, or both",
        "field.choices.pool": "pending author: the thirsty lines are new content and are not written",
        "cured_by.1": "PROPOSED reading of 'a beverage consumable' (mango_og_gushers_item.md:119, :179): an item with subtype 'drink' or alcohol true. Note GameClock.is_drink is alcohol-only (game_clock.gd:22)",
        "cues": "pending art: no Cottonmouth cue is specified"
      }
    }
  }
}
```

## 5. Runtime model (PROPOSED)

- **In battle,** `BattleUnit.statuses` keeps its meaning (`id -> turns left`, `-1` until cured). Per-status extras (pending `then` stacks, stack count) go in a parallel dictionary on the unit, so nothing that reads `statuses` today breaks.
- **On the overworld,** the live status is a `FieldStatus` row in the saved `GameState.flags.field_status`. That needs a third unit, `steps`, next to `clock` and `real` (`field_status.gd:4-9`), because the approved item field is `field_steps`.
- **Counting rule (PROPOSED for the author's review):** a status carries two independent counters. Battle turns tick only in battle, steps tick only on the overworld, and the status ends when either reaches 0 (or at rest, if `ends_on_rest`). On ending, `then` fires. The alternative is one shared budget split across both; the counters-first rule is simpler to read and to test.
- **Carry into and out of battle:** today `FieldStatus.battle_statuses()` maps a field status into battle as `-1` (`field_status.gd:126-134`), which would make Gush-Locked last the whole fight. These statuses need their real `battle_turns` carried in and the remainder written back to the field row after the fight. That is engineering work, filed as its own bead (§9).

## 6. What can be data and what needs a hook

| Behaviour | Field | Data-driven? | Hook it needs |
|---|---|---|---|
| Stat deltas | `stats` | Yes | `BattleUnit.attack_stat`, `defense_stat`, `battle_speed`, `grit_stat` (`battle_unit.gd:132-170`) sum deltas from the table instead of per-id `if`s |
| Accuracy | `accuracy_steps` | Yes | `BattleCore._hit` (`battle_core.gd:393-398`) adds the table's steps |
| Skip chance | `skip_turn_chance` | Yes | `BattleCore._turn_lost` (`:292-319`) one generic roll |
| Bravado drain (battle) | `bravado_tick.battle_per_turn` | Yes | `_turn_lost`, beside the Embarrassed drain (`:309-310`) |
| Durations, battle | `default_duration.battle_turns` | Yes | Already ticked by `end_own_turn` (`battle_unit.gd:172-177`) |
| Durations, field | `default_duration.field_steps` | Needs a hook | `FieldStatus` `steps` unit; `PlayerController` reports steps |
| `then` on expiry | item `intoxicant.then` / status `then` | Needs a hook | `end_own_turn` erases silently today; an expiry callback (Eurobound-umy covers the item side) and the same in `FieldStatus.tick` |
| Cleaning / pacification hits | `attack_conversion` | Numbers and text yes; resolver no | `BattleCore.attack()` (`:211-216`) looks up the attacker's conversion, applies `damage_mult`, then runs one of **two coded resolvers** by `kind`: cleaning (move `sp` to Bravado) or pacification (`_apply_status` with `inflict`). Skills keep calling `_party_hit` unchanged |
| Ability locks | `locks` | Yes, once skills are tagged | `BattleCore.can_use_skill` (`:169-171`) checks the bearer's locks against skill tags; `party_abilities.json` needs a `spoken` tag |
| Tier display shift, cross-fade | `ladder` | Yes, once the ladder exists | The alcohol ladder (Eurobound-p0j, deferred) consults the table when it computes the shown tier (`field_menu.gd:394`) and when it applies a tier gain |
| Suppress / cancel | `interactions` | Yes | An `is_active(id)` check that respects suppressors, used where `has_status` is read today; `cancel_into` resolved in `_apply_status` (`:441-463`) and the field `apply` |
| Cures by kind | `cured_by` | Yes | `BattleCore.use_item` (`:183-207`) and the field item menu remove statuses whose `cured_by` matches the item; the rest scene clears `rest` cures |
| Overworld compulsion | `field.compulsion` | Interval and length yes; behaviour no | One **coded runner per `kind`** in `PlayerController`: walk to the nearest interactable and back (clean), or stop and show an epiphany box (stare). Input locks for `lasts_seconds` and always releases (law §3, §7: no softlock) |
| Dialogue scroll, ellipsis | `field.text_speed_mult`, `text_filter` | Yes | The dialogue box typewriter |
| Dialogue scramble | `field.choices` | Yes for `shuffle` (exists); `replace` needs a hook | `dialogue_box.gd:74` already routes choices through `FieldStatus.choice_index`; `replace` adds option-text substitution |
| Rest events | `on_rest` | Params yes; events no | The rest scene runs each event by id (`deep_clean`, `munchies_tax`) and sets its flag before `ends_on_rest` removes the status |
| Display name | `display_name` | Yes | `_status_name` (`:477`) reads the table first |

## 7. How this fits Eurobound-70z

Eurobound-70z (deferred by the author: "Defer until the systems that use them are designed") owns the full schemas for the empty data files, `status_effects.json` among them. This proposal does not pre-empt it:

- It writes **four entries**, the ones the approved intoxicant items already point at. It does not migrate Embarrassed, Sloppy, Confused, Stun, Food Poisoning or any other hard-coded status, and it does not touch the other empty files.
- Every field but `display_name` is optional and absent means "does nothing", so 70z can add fields (master-list description, sources, percentage modifiers like Embarrassed's −20% ATK, lasting-status persistence) without breaking these entries.
- Its vocabulary follows `design/templates/status_effect_template.md` (engine stat names, duration, stacking, cures, scope), so 70z can adopt it as the starting point, rename fields, or replace it.
- `schema_version` stays `"1.0"`. 70z decides the version once the full schema is ruled.
- The validator already checks `intoxicant.status` and `then.status` against this table once it has entries (`Tools/validate_data.py:236`, `:258`). With these four entries, all four ids the two items name resolve.

## 8. Open semantic questions (rulings, not numbers)

The shape holds each of these as `null` until the author rules. None blocks approving the shape.

1. **"All stats"** (Crash −3, Cottonmouth −1, and Hungover's −2): which engine stats does it cover? Offense, defense, speed, charm, luck and grit, or also accuracy, max HP and max Bravado?
2. **Crash outside battle:** Sugar Rush Hour can end on the overworld or at a rest. Does Crash wait for the next fight (battle turns only), or does it also run on steps?
3. **Stacked follow-ups:** does a stacked Crash last longer or hit harder? Does a stacked Cottonmouth hit harder, or need one drink per stack?
4. **"Doubles the thirst"** (Hungover into Cottonmouth): double stacks, double penalty, or two drinks to clear?
5. **Spoken Bravado abilities:** which abilities count? Today only Roast Line exists (`party_abilities.json`).
6. **Suppressed Hungover:** does its timer pause while suppressed, or keep running?
7. **The Sugar Rush Hour × Gush-Locked cancel:** do Crash and Cottonmouth still fire afterwards? (The "into" status itself is Eurobound-4ug.)
8. **Cottonmouth's cure:** does any beverage count (water, soda, beer), or only certain drinks?

## 9. Intoxication law §8: 10-point review of this proposal

| # | Point | Answer |
|---|---|---|
| 1 | Source item or drink | STRAWBERRY SHORTCAKE SPEEDCAKES™ (Sugar Rush Hour, then Crash) and MANGO OG GUSHERS™ (Gush-Locked, then Cottonmouth), both from Tony420. Crash is also the master list's post-Manic status. The shape adds no source |
| 2 | Immediate effect | Each approved effect has a field: `stats`, `accuracy_steps`, `attack_conversion`, `bravado_tick`, `field.compulsion`. No effect is added or softened |
| 3 | Escalation conditions | Re-hits stay on the item (`stack_rule: extend`, `then.stacks`). The status adds only how stacked follow-ups combine (`stack_rule`, pending) and the ladder offsets (`display_offset`, `gain_bonus`) |
| 4 | Visible player-facing cues | `cues`, `field.text_speed_mult`, `text_filter`, `attack_conversion.battle_text` and `animation`, the shifted tier on the menu card. Asset ids are pending art |
| 5 | Effect on player control | Bounded by construction: `field.compulsion` needs an interval and a length; the runner always releases input; battle choices stay the player's (converted hits replace only the Attack result). Cottonmouth narrows dialogue options and spoken abilities; it never removes the menu |
| 6 | Duration and recovery | Every status has a turn count, a step count, a rest end, or a cure (`cured_by`). Nothing can last forever: Cottonmouth, the one `until_cured` status, also ends on rest. Status state lives in the saved field-status rows, so save/load keeps it consistent |
| 7 | Comedic consequence | Kept intact in data: cleaning hits that steal the enemy's `sp`, pacification swings with the approved lines, the deep clean and the Munchies Tax as rest events, the sober-looking tier that lands with the Crash |
| 8 | Interaction with other established statuses | `interactions`: Hungover suppressed by both, Port-O-Cologne explicitly unaffected, the Sugar Rush Hour × Gush-Locked cancel, the doubled thirst. Hungover itself is not in the engine yet (Eurobound-p0j) |
| 9 | Technical implementation dependencies | Proposed engineering work, listed in §6: generic stat/accuracy/skip/drain reads in BattleCore and BattleUnit; two attack-conversion resolvers; skill tags for locks; a `steps` unit and two-way battle carry in FieldStatus (new bead); expiry callbacks for `then` (Eurobound-umy); compulsion runners in PlayerController; choice replacement in the dialogue box; rest-scene events; the alcohol ladder (Eurobound-p0j) |
| 10 | Requires further author approval? | Yes: this shape (Production Desk Eurobound-1m4-q1); the §5 counting rule; the eight §8 questions; Pacified/Mellowed and the cancel state (Eurobound-4ug); every number (balancing pass); the PROPOSED Speedcakes battle lines and both rest-flag names |

## 10. Follow-ups if approved

- Write the four entries into `game/assets/data/skills/status_effects.json` exactly as approved, with `_pending` notes; extend `Tools/validate_data.py` to type-check them.
- BattleCore and BattleUnit hooks from §6 (beside Eurobound-umy, which applies the item side).
- FieldStatus `steps` unit and two-way battle carry (bead filed with this proposal).
- The "Pacified"/"Mellowed" entry once Eurobound-4ug names it.
