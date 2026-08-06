# Bravado Consolidation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Bravado the engine's real resource stat, add its state machine and Ultimate gating, strike the invented Composure stat, land the `key_items`/`equipment` loader, and add an ability template.

**Architecture:** Five independent tasks against a thin Godot 4.4 vertical slice. Tasks 1 and 2 touch engine code and data; Task 3 touches design docs only; Task 4 adds a loader; Task 5 adds a template. Task 2 depends on Task 1's rename landing first. Tasks 3, 4, and 5 are independent of each other.

**Tech Stack:** Godot 4.4 / GDScript, JSON data files, Python 3.13 for validation, GUT for unit tests.

**Spec:** `docs/superpowers/specs/2026-08-06-bravado-consolidation-design.md`

## Global Constraints

- **Godot is not installed in this environment.** `godot` is not on PATH and no binary exists on disk. **GUT tests cannot be executed.** Write them correctly, then state plainly in your report that they are UNRUN. Never claim a GUT test passed. Never write "tests pass" without command output. This is not a reason to skip writing tests.
- What you CAN and MUST run: `python Tools/validate_data.py` (capital T), `python -c "import json; json.load(...)"` for any JSON you touch, and grep sweeps for stale identifiers.
- All money is SOVS. Never the euro glyph, never "euros", never "koruna".
- Stat vocabulary in item JSON is exactly two keys: `bravado` and `charm`. No others.
- Zero Bravado does NOT cause collapse or forced retreat. That is HP's job. Author ruling.
- New files and folders: snake_case, no spaces.
- Commit directly on `main`. Do not create a branch. Do not commit anything under `.superpowers/` or `scratch/`.
- Do not touch `design/legacy/` or `design/characters/PermanantCosmeticChanges/permanent_cosmetic_changes.json`.

---

### Task 1: Rename SP to Bravado across engine and data

**Files:**
- Modify: `game/assets/data/party/party_members.json` (`max_sp` → `max_bravado`)
- Modify: `game/assets/data/skills/party_abilities.json` (`sp_cost` → `bravado_cost`)
- Modify: `game/assets/data/items/consumables.json` (`heal_sp` → `heal_bravado`)
- Modify: `game/core/game_state.gd:33-34,56`
- Modify: `game/battle/battle_manager.gd:84-86,102-106`
- Modify: `game/tests/unit/test_data_repo.gd:25`
- Modify: `game/tests/unit/test_game_state.gd:16`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: the identifiers `max_bravado`, `bravado`, `bravado_cost`, `heal_bravado`. Task 2 builds its state machine on the runtime `bravado` field set by `game_state.gd`.

- [ ] **Step 1: Capture the current state so you can prove the rename is complete**

```bash
grep -rn "max_sp\|sp_cost\|heal_sp\|\"sp\"\|\[\"sp\"\]" --include=*.gd --include=*.json game/ | grep -v "/addons/" > scratch/sp_before.txt
cat scratch/sp_before.txt
wc -l < scratch/sp_before.txt
```

Expected: 12 or so matches across the seven files listed above. Record the exact count — Step 6 checks it reaches zero.

- [ ] **Step 2: Rename in the three JSON data files**

`party_members.json`: every `"max_sp"` key becomes `"max_bravado"`. Values unchanged.
`party_abilities.json`: every `"sp_cost"` key becomes `"bravado_cost"`. Values unchanged.
`consumables.json`: every `"heal_sp"` key becomes `"heal_bravado"`. Values unchanged.

Then confirm all three still parse:

```bash
python -c "
import json
for p in ['game/assets/data/party/party_members.json','game/assets/data/skills/party_abilities.json','game/assets/data/items/consumables.json']:
    json.load(open(p, encoding='utf-8-sig'))
    print('parsed', p)
"
```

- [ ] **Step 3: Rename in `game/core/game_state.gd`**

Lines 33-34 currently read:

```gdscript
		"sp": int(data.get("max_sp", 0)),
		"max_sp": int(data.get("max_sp", 0)),
```

Become:

```gdscript
		"bravado": int(data.get("max_bravado", 0)),
		"max_bravado": int(data.get("max_bravado", 0)),
```

Line 56 currently reads:

```gdscript
	member["sp"] = mini(int(member["max_sp"]), int(member["sp"]) + int(item.get("heal_sp", 0)))
```

Becomes:

```gdscript
	member["bravado"] = mini(int(member["max_bravado"]), int(member["bravado"]) + int(item.get("heal_bravado", 0)))
```

- [ ] **Step 4: Rename in `game/battle/battle_manager.gd`**

The stats label at lines 84-86 becomes:

```gdscript
	_stats_label.text = "%s  HP %d/%d  Bravado %d/%d" % [
		_member["display_name"], _member["hp"], _member["max_hp"],
		_member["bravado"], _member["max_bravado"]]
```

The ability cost check at lines 102-106 becomes:

```gdscript
	var cost := int(ability.get("bravado_cost", 0))
	if int(_member["bravado"]) < cost:
		_log("Not enough Bravado!")
		return
	_member["bravado"] = int(_member["bravado"]) - cost
```

- [ ] **Step 5: Update the two tests**

`game/tests/unit/test_data_repo.gd:25` becomes:

```gdscript
	assert_eq(int(a.get("bravado_cost")), 4)
```

`game/tests/unit/test_game_state.gd:16` becomes:

```gdscript
	assert_eq(int(state.party[0]["bravado"]), 12)
```

- [ ] **Step 6: Prove the rename is complete**

```bash
grep -rn "max_sp\|sp_cost\|heal_sp\|\"sp\"\|\[\"sp\"\]" --include=*.gd --include=*.json game/ | grep -v "/addons/"
```

Expected: **no output, exit 1.** Any remaining match is an incomplete rename — fix it.

Then confirm the data still validates:

```bash
python Tools/validate_data.py
```

Expected: 7 `OK` lines, exit 0.

- [ ] **Step 7: Clean up and commit**

```bash
rm -f scratch/sp_before.txt
rmdir scratch 2>/dev/null
git add game/assets/data/party/party_members.json game/assets/data/skills/party_abilities.json game/assets/data/items/consumables.json game/core/game_state.gd game/battle/battle_manager.gd game/tests/unit/test_data_repo.gd game/tests/unit/test_game_state.gd
git commit -m "refactor: rename SP to Bravado across engine data, code, and tests"
```

State in your report that the GUT tests were NOT run because Godot is unavailable.

---

### Task 2: Bravado state machine and Ultimate gating

**Files:**
- Modify: `game/core/game_state.gd` (add the state helper)
- Modify: `game/battle/battle_manager.gd` (enforce the Ultimate gate)
- Create: `game/tests/unit/test_bravado_state.gd`

**Interfaces:**
- Consumes: Task 1's `bravado` / `max_bravado` runtime fields on each party member dictionary.
- Produces: `GameState.bravado_state(value: int) -> String` returning one of `"zero"`, `"low"`, `"mid"`, `"high"`; and `GameState.can_use_ultimate(value: int) -> bool`.

- [ ] **Step 1: Write the failing test**

Create `game/tests/unit/test_bravado_state.gd`. Match the style of the existing tests in `game/tests/unit/` — read `test_game_state.gd` first and follow its `extends`, naming, and setup conventions exactly.

```gdscript
extends GutTest

func test_zero_band():
	assert_eq(GameState.bravado_state(0), "zero")

func test_low_band():
	assert_eq(GameState.bravado_state(1), "low")
	assert_eq(GameState.bravado_state(25), "low")

func test_mid_band():
	assert_eq(GameState.bravado_state(26), "mid")
	assert_eq(GameState.bravado_state(70), "mid")

func test_high_band():
	assert_eq(GameState.bravado_state(71), "high")
	assert_eq(GameState.bravado_state(100), "high")

func test_ultimate_locked_at_zero_and_low():
	assert_false(GameState.can_use_ultimate(0))
	assert_false(GameState.can_use_ultimate(25))

func test_ultimate_unlocked_at_mid_and_high():
	assert_true(GameState.can_use_ultimate(26))
	assert_true(GameState.can_use_ultimate(100))
```

- [ ] **Step 2: Implement the state helper in `game/core/game_state.gd`**

Add these near the other public functions. Read the file first and match its existing style — indentation, typing, and naming.

```gdscript
const BRAVADO_LOW_MAX := 25
const BRAVADO_MID_MAX := 70

## Returns the Bravado band for a value: "zero", "low", "mid", or "high".
## Zero Bravado means Bravado cannot be spent. It does NOT cause collapse or
## forced retreat — that belongs to HP reaching zero.
func bravado_state(value: int) -> String:
	if value <= 0:
		return "zero"
	if value <= BRAVADO_LOW_MAX:
		return "low"
	if value <= BRAVADO_MID_MAX:
		return "mid"
	return "high"

## Ultimates are locked out in the zero and low bands.
func can_use_ultimate(value: int) -> bool:
	var state := bravado_state(value)
	return state == "mid" or state == "high"
```

- [ ] **Step 3: Enforce the gate in `game/battle/battle_manager.gd`**

In the ability-use path, before the cost check added in Task 1, refuse Ultimates when the band is too low. The refusal must be visible to the player, not silent:

```gdscript
	if bool(ability.get("is_ultimate", false)) \
			and not GameState.can_use_ultimate(int(_member["bravado"])):
		_log("Not enough Bravado for an Ultimate!")
		return
```

Place this immediately before the `var cost := int(ability.get("bravado_cost", 0))` line so an Ultimate is refused on band before it is refused on cost.

- [ ] **Step 4: Verify what can be verified**

```bash
python Tools/validate_data.py
grep -n "bravado_state\|can_use_ultimate\|is_ultimate" game/core/game_state.gd game/battle/battle_manager.gd game/tests/unit/test_bravado_state.gd
```

Expected: validator prints 7 `OK`, exit 0. The grep shows the helper defined in `game_state.gd`, called in `battle_manager.gd`, and exercised in the test.

Confirm the boundary values match the spec exactly: 0 is zero, 1 and 25 are low, 26 and 70 are mid, 71 and 100 are high. An off-by-one here is a real defect.

- [ ] **Step 5: Commit**

```bash
git add game/core/game_state.gd game/battle/battle_manager.gd game/tests/unit/test_bravado_state.gd
git commit -m "feat: Bravado state machine and Ultimate gating"
```

State in your report that the GUT tests were NOT run because Godot is unavailable.

---

### Task 3: Strike Composure, correct the Bravado doc

**Files:**
- Modify: `design/items/gold_circle_coin_item.md`
- Modify: `design/items/leopard_print_thong_item.md`
- Modify: `design/mechanics/Battle/bravado.md`

**Interfaces:**
- Consumes: nothing. Independent of Tasks 1, 2, 4, 5.
- Produces: design docs whose stat vocabulary matches the engine's.

- [ ] **Step 1: Read all three files before editing**

You are editing satirical content for an MA-rated game. Match the surrounding voice exactly. Do not soften, moralize, explain a joke, or make a line "safer" — this project treats that as a top-severity defect.

- [ ] **Step 2: Strike Composure from `gold_circle_coin_item.md`**

Line 80 currently reads:

```
Composure:         +2 (no Groin Blurts can interrupt dialogue while suppression is active)
```

Delete the line. The item already grants `+4 Bravado` on line 79, which now carries this effect; fold the parenthetical's meaning into that line's existing parenthetical if it reads naturally, otherwise just delete. Do not invent a replacement stat.

Line 119 currently reads, inside a comparison table:

```
| **Stats** | +4 Bravado, +2 Composure, party-wide `the_herp` suppression | +1 to +2 single-stat, wearer only |
```

Becomes:

```
| **Stats** | +4 Bravado, party-wide `the_herp` suppression | +1 to +2 single-stat, wearer only |
```

- [ ] **Step 3: Strike Composure from `leopard_print_thong_item.md`**

Line 68 currently reads:

```
Composure:            -1 (he brings it up)
```

The `-1` penalty is real and should survive as a Bravado penalty, since Bravado is what embarrassment drains. Replace with a Bravado line, keeping the joke intact. The file already has a `Bravado: +2` line at line 66 — do not create a second Bravado entry; fold the penalty into the existing line's value and parenthetical so the net effect and the gag both survive. Read both lines first and make the arithmetic explicit in your report.

- [ ] **Step 4: Correct the collapse ruling in `design/mechanics/Battle/bravado.md`**

The "Visual States" section currently contains:

```
    • Zero Bravado: “Dad on a Bender” collapse — dropped animations, forced retreat if not restored.
```

Author ruling 2026-08-06 strikes this. Zero Bravado means only that Bravado cannot be spent; collapse and forced retreat belong to HP reaching zero. Rewrite that bullet to say so, in the doc's existing voice. Keep the other three state bullets untouched.

Do NOT edit `design/legacy/Game Files/Markdown Files/bravado.md`. It is legacy.

- [ ] **Step 5: Verify**

```bash
grep -rn -i "composure" design/items/ && echo "FAIL: Composure survives in an item doc" || echo "PASS: no Composure in item docs"
grep -n -i "collapse\|forced retreat" design/mechanics/Battle/bravado.md
grep -rn "€" design/items/gold_circle_coin_item.md design/items/leopard_print_thong_item.md design/mechanics/Battle/bravado.md && echo "FAIL: euro glyph" || echo "PASS: no euro glyph"
```

Expected: no Composure in `design/items/`; the collapse grep shows only the corrected wording, with no surviving claim that zero Bravado forces retreat; no euro glyph.

- [ ] **Step 6: Commit**

```bash
git add design/items/gold_circle_coin_item.md design/items/leopard_print_thong_item.md design/mechanics/Battle/bravado.md
git commit -m "content: strike agent-invented Composure stat; correct zero-Bravado ruling"
```

---

### Task 4: `key_items` / `equipment` schema and loader

**Files:**
- Modify: `game/core/data_repo.gd`
- Modify: `Tools/validate_data.py`
- Create: `game/tests/unit/test_key_items_loader.gd`

**Interfaces:**
- Consumes: nothing from Tasks 1-3. Independent.
- Produces: `DataRepo.get_key_item(id: String) -> Dictionary` and `DataRepo.get_equipment(id: String) -> Dictionary`, which the `eurobound-item-engine-sync` skill's output will eventually feed.

- [ ] **Step 1: Read `game/core/data_repo.gd` in full**

Note the existing pattern: each load does `_load_json(DATA_ROOT + "<path>")`, extracts the inner object with `.get("<key>", {})`, and ANDs `not ...is_empty()` into `ok`. Note also the `_lookup` helper used by the existing getters.

- [ ] **Step 2: Add both loads — but do NOT require them to be non-empty**

`key_items.json` and `equipment.json` are legitimately empty until items are authored. Failing startup on an empty object would block the game. Add the loads WITHOUT the `ok = ok and not ...is_empty()` line the other five use:

```gdscript
	var key_item_doc := _load_json(DATA_ROOT + "items/key_items.json")
	_key_items = key_item_doc.get("key_items", {})

	var equipment_doc := _load_json(DATA_ROOT + "items/equipment.json")
	_equipment = equipment_doc.get("equipment", {})
```

Declare `_key_items` and `_equipment` alongside the existing backing dictionaries, matching their declaration style.

- [ ] **Step 3: Add the two getters**

Match the existing getter style exactly:

```gdscript
func get_key_item(id: String) -> Dictionary:
	return _lookup(_key_items, id, "key item")

func get_equipment(id: String) -> Dictionary:
	return _lookup(_equipment, id, "equipment")
```

- [ ] **Step 4: Write the test**

Create `game/tests/unit/test_key_items_loader.gd`. Read `game/tests/unit/test_data_repo.gd` first and match its conventions. The test must assert that loading succeeds with both files empty — that is the specific regression this guards:

```gdscript
extends GutTest

func test_load_succeeds_with_empty_key_items():
	assert_true(DataRepo.load_all())

func test_key_items_dictionary_exists_when_empty():
	assert_eq(DataRepo.get_key_item("nonexistent_item"), {})

func test_equipment_dictionary_exists_when_empty():
	assert_eq(DataRepo.get_equipment("nonexistent_item"), {})
```

If `load_all()` is not the actual entry point name, use the real one from `data_repo.gd` — read it, do not guess.

- [ ] **Step 5: Add both files to the validator**

In `Tools/validate_data.py`, add two entries to `REQUIRED` with empty key lists, so presence and parseability are checked without demanding content:

```python
    "items/key_items.json": [],
    "items/equipment.json": [],
```

- [ ] **Step 6: Verify**

```bash
python Tools/validate_data.py
```

Expected: **9** `OK` lines now (the original 7 plus the 2 new), exit 0.

```bash
grep -n "key_items\|equipment" game/core/data_repo.gd
```

Expected: the load, the backing dictionary, and the getter for each.

- [ ] **Step 7: Commit**

```bash
git add game/core/data_repo.gd Tools/validate_data.py game/tests/unit/test_key_items_loader.gd
git commit -m "feat: load key_items and equipment JSON; extend data validator"
```

State in your report that the GUT tests were NOT run because Godot is unavailable.

---

### Task 5: Ability template

**Files:**
- Create: `design/templates/ability_template.md`

**Interfaces:**
- Consumes: the engine field names established in Tasks 1 and 2 — `bravado_cost`, `power_multiplier`, `battle_text`, `is_ultimate` — and the four Bravado bands.
- Produces: a template for authoring abilities, sitting alongside the existing item and quest templates.

- [ ] **Step 1: Read the two reference templates in full**

`design/templates/permanent_item_template.md` and `design/templates/sidequest_template.md`. Match their conventions: an instructional HTML comment block that the author deletes on use, `[bracketed placeholders]` throughout, H2 section headers, and a validation checklist table at the end.

Also read `game/assets/data/skills/party_abilities.json` for the real engine shape, and `design/mechanics/Battle/bravado.md` for the state vocabulary.

- [ ] **Step 2: Write the template**

It must cover both halves of an ability:

**Engine fields** — the ability id, display name, `bravado_cost`, `power_multiplier`, `battle_text`, and `is_ultimate`. These map 1:1 onto `party_abilities.json`, so an author filling the template has everything the engine needs.

**Design material** — which bro owns it and their Bravado Style (Lord Pilsner's Keg-Fu, Chadwick's Bro-Mancy, Bradley's Frat-Sorcery), the minimum Bravado band required, what the move is satirizing, what it looks like on screen, and what happens when it fails.

Include a note that Ultimates require the Mid band or higher, and that zero Bravado means Bravado cannot be spent — it does not cause collapse.

The template is a floor, not a ceiling, per `CLAUDE.md`.

Write the placeholder examples in the game's voice. A template full of limp examples produces limp abilities.

- [ ] **Step 3: Verify**

```bash
test -f design/templates/ability_template.md && echo "PASS: exists"
grep -c "\[" design/templates/ability_template.md
grep -n "bravado_cost\|is_ultimate\|power_multiplier\|battle_text" design/templates/ability_template.md
grep -n "€" design/templates/ability_template.md && echo "FAIL: euro glyph" || echo "PASS: no euro glyph"
```

Expected: the file exists, contains bracketed placeholders, names all four engine fields, and has no euro glyph.

- [ ] **Step 4: Commit**

```bash
git add design/templates/ability_template.md
git commit -m "templates: ability template covering engine fields and design material"
```

---

## Open items for the author

- **The GUT tests in Tasks 1, 2, and 4 are written but never executed** — Godot is not installed in this environment. Run them in the editor before trusting the engine changes.
- No Ultimate ability exists yet. The gate is built and tested; the four named Ultimates in the character docs still need damage numbers, targeting, and failure states, each requiring its own ruling.
- An ability-creation skill to pair with Task 5's template is a separate decision, not covered here.
