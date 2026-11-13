# Quest flag schema and validation depth: APPROVED

**Status:** APPROVED (author, 2026-11-12; Production Desk Eurobound-vyn-q1, verbatim: "Approve as proposed"). Implemented under Eurobound-vyn: `quest_flags.json` populated (§5), tier 2 in `Tools/validate_data.py` (§6), `sidequest_template.md` updated (§2, §7.1). Tier 3 and the §7 author questions are tracked as beads.
**Bead:** Eurobound-vyn. **Author's ask (bead page, 2026-11-12):** "Have an agent propose a schema from the design docs' flag tables for my approval".
**Related:** Eurobound-70z (schemas for the empty engine data files; deferred). NEXT_WORK.md "DEFERRED 2026-08-06" items 5 and 6.

---

## 1. What exists today

### 1.1 The engine stub
`game/assets/data/world_data/quest_flags.json` is `{"schema_version": "1.0", "quest_flags": {}}`.
`Tools/validate_data.py` lists it in `PENDING_SCHEMA` (line 28), so it reports `PENDING world_data/quest_flags.json: pending schema (Eurobound-70z)`. Add one entry and it reports `PARSED ... has entries but no ruled schema`. Nothing checks its contents.

### 1.2 How the game stores flags
- All flags sit in one dictionary, `GameState.flags` (`game/core/game_state.gd:9`), and are saved whole (`to_dict`, line 107). `set_flag()` and `has_flag()` (lines 88-92) handle booleans only. Most code reads `state.flags.get(id, default)` directly.
- **The dictionary holds more than quest booleans.** Here is what it carries now:

| Kind | Examples (file) |
|---|---|
| Quest/world booleans, dotted ids | `debaucheryville.absinthe_arcade.cara_tab_paid` and six more (`grandpa_provides.gd:12-24`); `great_doner_debate.shamsterdam.complete` (`kavarna_chair.gd:8`, read only, the setter isn't built) |
| Quest/world booleans, flat ids | `brewery_tour_started` (`brewery_passport.gd:15`), `tony420_unlocked` (`tony420_hijack.gd:10`), `sea_monkeys_obtained` (`arcade_claw.gd:28`), `jakub_restroom_discovered`, `absinthium_taproom_entrance_discovered`, `mirror_shadow_secret_solved`, `broken_game_boy_found`, `arcade_maintenance_restroom_unlocked`, `club_flyer_placed` (read only), `has_inspected_first_crypto_trash` (`field_menu.gd:544`, read only) |
| Integer counters | `aa_broken_ddr_tokens_fed`, `rigged_claw_plays_since_payout`, `cabinet_kebab_kombat_rung`, `<enemy_id>_defeats`, `...cara_tab_stolen_sovs`, `...cara_tab_credit` |
| Id families built at runtime | `brewery_opener_<id>`, `brewery_stamp_<id>`, `nft_vault_<id>`, `icq_seen_<id>`, `<machine_id>_won` |
| System state | `clock.minutes` (int, `game_clock.gd:15`), `field_status` (dict, `field_status.gd:17`), `reality_anchor` (dict, line 30) |
| Settings | `settings.reduced_motion` (bool, `arcade_ambient_fx.gd:17`) |

- `game/assets/data/quest_log/quest_log.json` also reads flags. Its `started_when`, `completed_when`, `done_when` and `all` lists name flag ids, and `QuestLog` (`game/core/quest_log.gd`) works out quest state from them.

### 1.3 The validator today
`check_quest` (`Tools/validate_data.py:374`) already validates quest JSON under `game/assets/data/quests/` against the canonical quest schema (af3e4da, Eurobound-e8c). The bead description says "no quest handling", which is out of date; the ledger note on item 6 is current. `check_quest` requires a `quest_flags` key but never looks inside it.

### 1.4 Where the template's flag rule comes from
`design/templates/sidequest_template.md:253` says: "Namespaced `city.venue.event` strings (PRD §11). Flags are write-once booleans unless prefixed `counter.`. Every flag listed here must be registered in `data/quests/flags.json`." The citation is wrong: the rule is §15.4 of `docs/EUROBOUND_PRD.md` (line 618), and that PRD is the dead `claude/eurobound-jrpg-prd-uv5iog` document (`line_safe`, `SATIRE_MODE`, mobile-first). `.claude/CLAUDE.md` says never to treat it as canon. So the template's path, its `counter.` prefix and its write-once rule have no live ruling behind them. This proposal treats them as options, not canon.

---

## 2. Path

**Proposed: keep `game/assets/data/world_data/quest_flags.json`.**

Reasons:
1. The file exists, and the validator and ledger already point to it (Eurobound-j50).
2. The template's `data/quests/flags.json` comes from the dead PRD (§1.4).
3. Moving it to `game/assets/data/quests/flags.json` would break the validator. `_check_for` (`validate_data.py:420-425`) sends every file under `quests/` to `check_quest`, so a registry there would fail as a malformed quest.

If approved: `sidequest_template.md:253` and `:282` get the new path, and the "PRD §11" citation is removed.

---

## 3. Scope: which keys the registry declares

**Proposed: every key in `GameState.flags`, each tagged with a `category`.** Tier 3 (§6) checks that every flag the code reads is declared. If the registry held quest flags only, that check would report the clock, settings and field-status keys every run. A `category` field keeps quest flags easy to filter.

| `category` | Meaning | Today's examples |
|---|---|---|
| `quest` | Set or read by one quest's beats | `debaucheryville.absinthe_arcade.cara_tab_open`, `debt_relief_claimed` |
| `world` | Persistent world or venue state not owned by one quest | `jakub_restroom_discovered`, `tony420_unlocked`, `debaucheryville.mystery_cart.doner_tony_lore_seen` |
| `economy` | Wallet and crypto state (canonical list in `design/economy/economy_system.md` §8.2) | `legacy_vault_secured_count`, `has_inspected_first_crypto_trash` |
| `system` | Engine bookkeeping | `clock.minutes`, `field_status`, `reality_anchor` |
| `setting` | Player options | `settings.reduced_motion` |

Alternative, if the author wants the file kept to quests only: declare `quest` and `world` flags, and give the validator a fixed allow-list for the system, setting and economy keys.

---

## 4. The schema

### 4.1 File shape
```json
{
  "schema_version": "1.1",
  "quest_flags": {
    "<flag id>": { ...entry... }
  },
  "flag_patterns": {
    "<pattern with one {placeholder}>": { ...entry, without default-only fields... }
  }
}
```
`flag_patterns` declares id families built at runtime (`brewery_stamp_{brewery_id}`). Without it, every brewery or NFT would need its own entry, and tier 3 could not match `STAMP_PREFIX + brewery_id`.

### 4.2 Entry fields

| Field | Type | Required | Meaning | Maps from the design table column |
|---|---|---|---|---|
| (key) | string | yes | The flag id, exactly as code reads it | `Flag` |
| `type` | `"bool"` \| `"int"` \| `"float"` \| `"string"` \| `"array"` \| `"dict"` | yes | Value type. Replaces the dead `counter.` prefix. `"float"` was added under Eurobound-0jfv for `field_step_carry` (the fraction of a metre carried between field steps), which none of the approved types could hold. | `Type` |
| `default` | matches `type` | yes | The value when the key is absent (what `flags.get(id, default)` uses) | `Default` (economy §8.2 only; others imply `false`) |
| `category` | enum, §3 | yes | | (inferred from the doc's folder) |
| `write_once` | bool | yes | True if the flag is never cleared or lowered after it is set | "never cleared" / "cleared on ..." wording |
| `set_by` | array of strings | yes | When it is set, in the doc's words. Use `"NOT BUILT: <what>"` while no code writes it. | `Set when` / `Set When` |
| `read_by` | array of strings | yes, may be empty | What checks it, in the doc's words | `Read by` / `Purpose` / `Use` / `Wallet use` |
| `quest_id` | string \| null | no | The owning quest's `quest_id` when `category` is `quest` | (the doc's quest id) |
| `doc` | string | yes | `path:line` of the design-doc row (or prose line) that defines it | (the table's location) |
| `status` | `"ruled"` \| `"proposed"` | yes | The doc's own status. Grandpa Provides' table is headed PROPOSED; Mango's flag name is PROPOSED. | the doc's status marker |

`set_by` and `read_by` hold the design meaning in the doc's words. Code locations are not stored, because tier 3 finds them from the source and stored paths would go stale.

### 4.3 Id convention

Two dotted conventions are in use, and most ids are flat:
- **City first:** `debaucheryville.absinthe_arcade.ring_tip_given` (`<city>.<venue>.<event>`), also `debaucheryville.mystery_cart.doner_tony_lore_seen`.
- **Quest first:** `great_doner_debate.shamsterdam.complete` (`<quest>.<city>.<event>`). The Döner Debate is a general quest instanced per city, so the quest comes first.
- **Flat snake_case:** everything else in code and in most docs.

**Proposed rule for new flags.** Use lowercase dotted segments of `[a-z0-9_]`:
- `<city>.<venue>.<event>` for content tied to a venue.
- `<quest>.<city>.<event>` for instanced general quests.

**Existing flat ids stay as they are.** They are declared as they stand, because renaming them means changing code constants and any saves for no gain. The validator enforces the dotted rule only on entries without `"legacy_id": true`.

**Uniqueness:** ids are unique across the file. Tier 2 also flags generic flat ids that two quests could both claim (`path_a_chosen`, see §7).

### 4.4 Sample (real flags only)
Every value below is copied or condensed from the cited lines. Nothing is new.

```json
{
  "schema_version": "1.1",
  "quest_flags": {
    "debaucheryville.absinthe_arcade.cara_tab_open": {
      "type": "bool", "default": false, "category": "quest", "write_once": false,
      "set_by": ["Fight won (tab + service charge still owed)"],
      "read_by": ["\"Tab's open\" greeting"],
      "quest_id": "debaucheryville_sidequest_grandpa_provides_01",
      "doc": "design/quests/debaucheryville/grandpa_provides.md:366",
      "status": "proposed"
    },
    "debaucheryville.mystery_cart.doner_tony_lore_seen": {
      "type": "bool", "default": false, "category": "world", "write_once": true,
      "set_by": ["The Tony420 Döner exchange completes"],
      "read_by": [],
      "quest_id": null,
      "doc": "design/worlds/debaucheryville/mysterymeatcart.md:107",
      "status": "ruled"
    },
    "debt_relief_claimed": {
      "type": "bool", "default": false, "category": "quest", "write_once": true, "legacy_id": true,
      "set_by": ["Café option (a) \"That horse doesn't belong to us!\" applies -170 SOVS",
                 "Hans-Jürgen's Fiaker insurance payout applies -170 SOVS (Path A)",
                 "Café paid in full at Stage 1 (consumed-and-moot)"],
      "read_by": ["The other relief trigger: disabled once set"],
      "quest_id": null,
      "doc": "design/quests/sinfonia/fiaker_fiasco.md:369",
      "status": "ruled"
    },
    "perpetual_bride_refused_while_infected": {
      "type": "bool", "default": false, "category": "quest", "write_once": true, "legacy_id": true,
      "set_by": ["State 2 plays"],
      "read_by": ["Four-state routing: State 3 on a host never refused, State 4 on a host who did"],
      "quest_id": null,
      "doc": "design/quests/publandia/couchsurfingchroniclespublandia.md:583",
      "status": "ruled"
    },
    "legacy_vault_secured_count": {
      "type": "int", "default": 0, "category": "economy", "write_once": false, "legacy_id": true,
      "set_by": [],
      "read_by": ["Feeds the [N of ∞] progress counter (wallet_ui.md)"],
      "quest_id": null,
      "doc": "design/economy/economy_system.md:272",
      "status": "ruled"
    }
  },
  "flag_patterns": {}
}
```
Notes on the sample:
- `quest_id` is null wherever the doc gives none. Fiaker Fiasco's and the Publandia Chronicles' quest ids are not cited on those lines, so the sample does not guess them.
- `write_once: true` for `debt_relief_claimed` and the refused flag is my reading of "Once the flag is set..." and of the four-state routing. The author should confirm it.
- `cara_tab_open` is `write_once: false` because its doc row says "cleared on payment". This is the first live counter-example to the template's "write-once booleans" rule.
- `legacy_vault_secured_count`'s `set_by` is empty because §8.2 gives only its purpose. The economy isn't built yet.

### 4.5 How the design flag tables map in

| Doc table shape | Example | Columns → fields |
|---|---|---|
| Sidequest template: `Flag \| Type \| Set when \| Read by` | `grandpa_provides.md:360-366` | Flag→key, Type→`type`, Set when→`set_by`, Read by→`read_by`; `default` is `false` for bool, `0` for int |
| Economy state: `Flag \| Type \| Default \| Purpose` | `economy_system.md:266-274` | direct; Purpose→`read_by`. `Array[String]`→`array` |
| Economy consumers: `Flag \| Use` / `Flag \| Owner \| Wallet use` | `icq_airdrops.md:310-312`, `wallet_ui.md:240-245` | adds `read_by` lines to the §8.2 entry; these docs say §8.2 is canonical |
| Couchsurf host: `Flag \| Set When` | `couchsurf_host_template.md:97-102` | Flag→key, Set When→`set_by`; `read_by` from the four-state routing |
| Chronicles roster: `Entry \| NPC ID \| Flag \| Profile` | `couchsurfingchroniclespublandia.md:581-587`, `...shamsterdam.md:637-641` | Flag→key; `set_by` "State 2 plays" from the template |
| Consumable hooks: `Hook \| Quest/File \| Reader \| Flag \| Status` | `mango_og_gushers_item.md:223`, `strawberry_shortcake_speedcakes_item.md:192` | Flag→key, Reader→`read_by`, Status→`status` |
| Prose "Flag: `x`" / "State flag: `x` (bool, default false)" | `mysterymeatcart.md:107`, `fiaker_fiasco.md:369,378` | key, `type`, `default` from the prose; `doc` points at the line |

Design-side JSON writes flags in three different shapes. Import has to read all three: `{"effect": "set_flag", "flag": "x", "value": true}` (`design/worlds/publandia/events/cloverleaf_events.json:60`), `"set_flag": {"x": true}` (`design/worlds/sinfonia/events/cafe_sachertorte_events.json:409`), and `"sets_flag": "x"` (`design/worlds/sinfonia/core/stadtpark_gustavs_refuge_core.json:182`). This proposal does not touch them. **Superseded 2026-11-12:** the author approved one canonical write shape, `"set_flags": {"<flag id>": <value>}`, with the old shapes to be migrated (Eurobound-r8l8; `docs/superpowers/specs/2026-11-12-flag-write-shape-proposal.md`).

---

## 5. Population (after approval, not now)

The implementation bead fills the file from the doc tables in §4.5, plus every flag the code reads or writes (§1.2), with `doc` set to `"NONE: code only"` where no design doc defines it. Those entries make the doc gaps visible. The bead does not add flags to design docs.

---

## 6. Validation depth: three tiers

| Tier | What `validate_data.py` does | What it catches | Cost |
|---|---|---|---|
| **1. Parse only** | Today's behaviour, minus PENDING: the file parses and `quest_flags` is an object | Broken JSON, a missing collection | None (already there) |
| **2. Schema check** | Every entry has the §4.2 fields with the right types. `default` matches `type`. `category` and `status` are in their enums. Ids match the dotted rule unless `legacy_id`. Patterns hold exactly one `{placeholder}`. Ids are unique. `doc` names a file that exists. | Typos in `type`/`category`, a bool flag with default `0`, a malformed id, a dead `doc` path after a folder move, two entries for one id | Small: a `check_quest_flags` function plus unit tests in `Tools/tests/test_validate_data.py` |
| **3. Cross-reference** | Collect every flag id the game reads or writes: string constants and literals passed to `flags.get`, `flags[...]`, `has_flag` and `set_flag` in `game/**/*.gd` (tests excluded), the prefix constants matched against `flag_patterns`, every id in `quest_log/quest_log.json`, and every id in quest JSON `quest_flags` blocks. Fail on any id that is not declared. Warn on declared ids nothing reads, and on ids that are read but have no writer and no `NOT BUILT` note in `set_by`. | A typo in a flag constant, which would silently never fire. A quest log naming a flag no scene sets. Code ahead of its doc (§7, Grandpa Provides). Docs drifting away from code. | Medium: a regex scan of GDScript. Ids built at runtime need the `flag_patterns` block, or they show up as false failures. |

**Recommended: tier 2 now, tier 3 once the file is populated.** Tier 3 fails on every undeclared flag, so it has to land in the same change as the population, or the validator goes red. Each tier keeps PENDING behaviour for the other files in `PENDING_SCHEMA`, and `quest_flags.json` leaves that list.

Not proposed: checking that design docs and the registry agree row by row. That means parsing Markdown tables, whose shapes vary (§4.5), so it belongs in a separate audit tool if the author wants it.

---

## 7. Docs that conflict or name flags differently

1. **`sidequest_template.md:253, 282`.** It cites the dead PRD (§1.4), gives the path `data/quests/flags.json`, requires the `counter.` prefix (no code or doc uses it), and requires write-once (`grandpa_provides.md:366` clears `cara_tab_open` on payment).
2. **`grandpa_provides.md:359-366` against `game/worlds/debaucheryville/absinthe_arcade/grandpa_provides.gd:12-24`.** The doc table lists 5 flags. The code also uses `accounts_receivable_lost`, `cara_tab_stolen_sovs` (int), `cara_tab_credit` (int) and `grandpa_banter_played` (rounds v31 and v43), and none of them is in the doc table. The table is also headed "PROPOSED".
3. **City-first against quest-first dotted ids:** `debaucheryville.absinthe_arcade.*` against `great_doner_debate.shamsterdam.complete` (§4.3).
4. **Quest JSON `quest_flags` blocks** (`game/assets/data/quests/astronomical_cockup.json`, `vip_wristbands.json`) group flat ids by event (`on_start`, `on_complete_a`, `permanent`). Generic ids such as `path_a_chosen`, `path_b_chosen` and `wristbands_purchased` will collide once a second quest uses them.
   **Ruled 2026-11-12 (Eurobound-tzbu, verbatim: "Rename them to the approved dotted rule (<city>.<venue>.<event>) in the quest JSON and docs"):** both quest JSONs (engine and design copies) and the docs that name these flags now use dotted ids, e.g. `debaucheryville.astronomical_cockup_square.cockup_path_a_chosen`, `debaucheryville.velvet_curtain_club.vip_wristband_quest_complete`; all are declared in `quest_flags.json`.
5. **Chronicles payload flags use bracket ids:** `chronicles_entry_completed[<npc_id>]` and `encounter_scene_completed[<npc_id>]` (`design/quests/sinfonia/thekingswerehumming.md:513`). The engine flag dict has no indexed keys, so these become either a `flag_patterns` family or a `dict`-typed flag. That choice is the author's.
   **Ruled 2026-11-12 (Eurobound-9jza, verbatim: "One bool per NPC (a flag_patterns family); routing lists use the Chronicles flag"):** declared as the `flag_patterns` families `chronicles_entry_completed_{npc_id}` and `encounter_scene_completed_{npc_id}` (status ruled); the docs now write `chronicles_entry_completed_<npc_id>`.
6. **Economy §8.2 `sovs_balance`** (`economy_system.md:274`, `wallet_ui.md:245`) is listed as a flag, but the engine keeps the wallet in `GameState.sovs` (`game_state.gd:8`), not in `flags`. Either the row leaves the registry or the engine changes. That choice is the author's.
7. **The Absinthe Arcade NPC routing list** (`design/worlds/debaucheryville/npcs/Absinthe_Arcade/absinthe_arcade_npcs.json:24-29`) names `backpack_girl_couchsurf_completed` and `backpack_girl_met`. The Chronicles docs use `chronicles_entry_completed[<npc_id>]` for the same idea (item 5).
   **Ruled 2026-11-12 (Eurobound-9jza):** routing lists use the Chronicles flag, so `backpack_girl_couchsurf_completed` became `chronicles_entry_completed_debaucheryville_npc_backpack_girl_01` in the Arcade NPC, core and interactions JSON. `backpack_girl_met` is unchanged.
8. **Three shapes for flag writes in design JSON** (§4.5).
9. **Items record flags under `quest_flags_on_acquire`** (`design/worlds/debaucheryville/items/clock_wine_item.md:211`, `clock_wine_purchased`). This is a fourth, item-side shape.

---

## 8. What approval unlocks

- An implementation bead: populate `quest_flags.json` (§5), add `check_quest_flags` at the approved tier with tests, take the file out of `PENDING_SCHEMA`, and update `sidequest_template.md` (§2, §7.1).
- Each "That choice is the author's" in §7 (items 5 and 6) stays open until the author rules. The implementation declares those flags as the docs have them and marks them in `status`.
