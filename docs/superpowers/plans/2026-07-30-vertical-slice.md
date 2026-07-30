# Eurobound Vertical Slice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A playable loop in Godot 4.4 — title screen → walk Clocktower Plaza → NPC dialogue → one battle → XP/item reward → save/reload — all content read from `Assets/Data/` JSON.

**Architecture:** Four autoloads (`DataRepo`, `GameState`, `SaveSystem`, `SceneRouter`) plus an input-map bootstrap. Scene files are deliberately thin (root node + script); each script builds its children in `_ready()` — far more reliable for AI-authored text edits than hand-writing `.tscn` node trees. Pure logic (damage, dialogue traversal, save round-trip) lives in plain classes with GUT unit tests; visual scenes are verified by headless smoke checks plus a manual playtest checklist.

**Tech Stack:** Godot 4.4 (GDScript, mobile renderer), GUT 9.x for unit tests, Python 3 for data validation tooling.

**Spec:** `docs/superpowers/specs/2026-07-30-vertical-slice-design.md`

## Global Constraints

- Godot `4.4` features (`config/features=PackedStringArray("4.4", "Mobile")`); do not change the renderer.
- GDScript only. No C#, no external plugins beyond GUT.
- Content is NEVER hardcoded in GDScript — stats, dialogue, items, enemies come from `Assets/Data/*.json` via `DataRepo`.
- Placeholder visuals only: `ColorRect` / `Label`. No image assets in this plan.
- Data errors fail loud at startup (`push_error` naming file and field); never fail silently mid-game.
- Save path: `user://saves/slot1.json`. Corrupt/missing save → Continue disabled, never a crash.
- All test commands assume the repo root as working directory. `godot` means the Godot 4.4 console binary (established in Task 0).
- Commit at the end of every task. Never commit `.godot/`.
- Existing placeholder `.gd`/`.tscn` files (0–21 bytes) are overwritten freely; anything with real content is only modified as specified.

## File Structure

```
Tools/validate_data.py                     # Python: validates all slice JSON parses + required fields
Assets/Data/party/party_members.json       # NEW: Lord Pilsner starting stats
Assets/Data/enemies/debaucheryville_enemies.json   # REPLACE placeholder: one real enemy
Assets/Data/items/consumables.json         # REPLACE placeholder: three consumables
Assets/Data/skills/party_abilities.json    # REPLACE placeholder: Roast Line
Assets/Data/npcs/dialogue_trees/debaucheryville_dialogue.json  # FIX: strip '#' header lines
Assets/Data/npcs/base_profiles/debaucheryville_core.json       # FIX: strip '#' header lines
Scripts/core/data_repo.gd                  # Autoload: JSON loading + typed getters
Scripts/systems/GameState.gd               # Autoload: party/inventory/flags/position (replaces 6-line stub)
Scripts/core/save_system.gd                # Autoload: save/load slot1
Scripts/core/scene_router.gd               # Autoload: scene transitions, battle handoff
Scripts/core/input_manager.gd              # Autoload: registers input actions in code
Scripts/characters/player_controller.gd    # Player movement + interaction
Scenes/characters/Player.tscn              # thin: CharacterBody2D + script
Scripts/characters/npc_controller.gd       # NPC: interact() → dialogue
Scenes/characters/NPCBase.tscn             # thin: Area2D + script
Scripts/characters/enemy.gd                # Overworld enemy: wander + touch → battle
Scenes/characters/Enemy.tscn               # thin: Area2D + script
Scripts/worlds/location_base.gd            # Shared location behavior (floor, walls, spawn, restore)
Scripts/worlds/clocktower_plaza.gd         # The slice's one location
Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn  # thin: Node2D + script
Scripts/systems/dialogue_runner.gd         # PURE: dialogue tree traversal (GUT-tested)
Scripts/ui/dialogue_box.gd                 # DialogueBox UI (typewriter, options)
Scenes/ui/dialogue/DialogueBox.tscn        # thin: CanvasLayer + script
Scripts/battle/damage_calculator.gd        # PURE: damage math (GUT-tested)
Scripts/battle/battle_manager.gd           # BattleScene controller
Scenes/battle/BattleScene.tscn             # thin: Control + script
Scripts/ui/title_screen.gd                 # New Game / Continue
Scenes/main/TitleScreen.tscn               # thin: Control + script
Scripts/ui/pause_menu.gd                   # Resume / Save / Quit
Scenes/ui/menus/PauseMenu.tscn             # thin: CanvasLayer + script
tests/unit/test_data_repo.gd
tests/unit/test_game_state.gd
tests/unit/test_save_system.gd
tests/unit/test_dialogue_runner.gd
tests/unit/test_damage_calculator.gd
docs/superpowers/playtest-checklist.md
```

---

### Task 0: Toolchain and project configuration

**Files:**
- Modify: `project.godot` (name, autoload section added later per-task)
- Create: `.gitignore`
- Create: `addons/gut/` (vendored GUT)

**Interfaces:**
- Produces: a working `godot` command; `addons/gut/gut_cmdln.gd` runnable headless; `.godot/` ignored by git.

- [ ] **Step 1: Locate or install Godot 4.4**

Check for an existing install (the project was created with 4.4, so it may exist):

```powershell
Get-ChildItem "$env:LOCALAPPDATA\Programs","$env:USERPROFILE\Downloads","C:\Program Files" -Recurse -Filter "Godot*.exe" -ErrorAction SilentlyContinue | Select-Object -First 5 FullName
```

If none found, download Godot 4.4.1 stable (standard, not .NET) from https://godotengine.org/download/windows/, unzip to `C:\Tools\Godot\`, and note the **console** exe path (`Godot_v4.4.1-stable_win64_console.exe`). The console variant prints errors to stdout — required for headless testing.

- [ ] **Step 2: Make `godot` invocable**

```powershell
Set-Alias godot "C:\Tools\Godot\Godot_v4.4.1-stable_win64_console.exe"   # session-local; also add the folder to user PATH for permanence
godot --version
```

Expected: prints `4.4.x.stable.official...`

- [ ] **Step 3: Create `.gitignore`**

```gitignore
.godot/
*.tmp
```

- [ ] **Step 4: Fix project name in `project.godot`**

Change `config/name="project"` to `config/name="Eurobound"`.

- [ ] **Step 5: Vendor GUT**

```powershell
git clone --depth 1 --branch v9.4.0 https://github.com/bitwes/Gut.git "$env:TEMP\gut-clone"
Copy-Item -Recurse "$env:TEMP\gut-clone\addons\gut" "addons\gut"
Remove-Item -Recurse -Force "$env:TEMP\gut-clone"
```

(If tag `v9.4.0` doesn't exist, use the newest `v9.x` tag — GUT 9.x targets Godot 4.)

- [ ] **Step 6: Verify GUT runs headless**

Create `tests/unit/test_smoke.gd`:

```gdscript
extends GutTest

func test_truth() -> void:
	assert_true(true)
```

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: `1 passed` (first run may import assets; run twice if it exits during import).

- [ ] **Step 7: Commit**

```bash
git add .gitignore project.godot addons/gut tests/unit/test_smoke.gd
git commit -m "chore: toolchain — GUT vendored, project name, gitignore"
```

---

### Task 1: Data hygiene and slice data files

**Files:**
- Create: `Tools/validate_data.py`
- Create: `Assets/Data/party/party_members.json`
- Modify (replace placeholder content): `Assets/Data/enemies/debaucheryville_enemies.json`, `Assets/Data/items/consumables.json`, `Assets/Data/skills/party_abilities.json`
- Modify (strip `#` comment header lines): `Assets/Data/npcs/dialogue_trees/debaucheryville_dialogue.json`, `Assets/Data/npcs/base_profiles/debaucheryville_core.json`

**Interfaces:**
- Produces: valid-JSON data files with these exact top-level shapes, consumed by `DataRepo` in Task 2:
  - `party_members.json` → `{"party_members": {"lord_pilsner": {...}}}`
  - `debaucheryville_enemies.json` → `{"enemies": {"feral_segway_tourist": {...}}}`
  - `consumables.json` → `{"consumables": {"<item_id>": {...}}}`
  - `party_abilities.json` → `{"abilities": {"roast_line": {...}}}`
  - `debaucheryville_dialogue.json` → `{"dialogue_trees": {"vlad_validator": {"default_greeting": {...}}}}` (existing content, now parseable)

- [ ] **Step 1: Write the validator (the "failing test" for this task)**

`Tools/validate_data.py`:

```python
"""Validates that every JSON file the vertical slice needs parses and has required keys."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "Assets" / "Data"

REQUIRED = {
    "party/party_members.json": ["party_members", "party_members.lord_pilsner",
        "party_members.lord_pilsner.max_hp", "party_members.lord_pilsner.offense"],
    "enemies/debaucheryville_enemies.json": ["enemies", "enemies.feral_segway_tourist",
        "enemies.feral_segway_tourist.max_hp", "enemies.feral_segway_tourist.xp_reward"],
    "items/consumables.json": ["consumables", "consumables.lukewarm_kebab"],
    "skills/party_abilities.json": ["abilities", "abilities.roast_line",
        "abilities.roast_line.sp_cost"],
    "npcs/dialogue_trees/debaucheryville_dialogue.json": ["dialogue_trees",
        "dialogue_trees.vlad_validator", "dialogue_trees.vlad_validator.default_greeting"],
    "npcs/base_profiles/debaucheryville_core.json": ["npcs"],
    "locations/debaucheryville/debaucheryville_locations.json": [],
}

def dig(obj, dotted):
    for part in dotted.split("."):
        if not isinstance(obj, dict) or part not in obj:
            return None
        obj = obj[part]
    return obj

failures = 0
for rel, keys in REQUIRED.items():
    path = ROOT / rel
    if not path.exists():
        print(f"MISSING  {rel}"); failures += 1; continue
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        print(f"INVALID  {rel}: {e}"); failures += 1; continue
    missing = [key for key in keys if dig(data, key) is None]
    for key in missing:
        print(f"NOKEY    {rel}: missing '{key}'"); failures += 1
    if not missing:
        print(f"OK       {rel}")
sys.exit(1 if failures else 0)
```

- [ ] **Step 2: Run it to see current failures**

Run: `python Tools/validate_data.py`
Expected: FAIL — `INVALID` for the two NPC files (comment headers), `NOKEY`/`INVALID` for enemies, consumables, abilities, `MISSING` for party_members.

- [ ] **Step 3: Strip comment headers from the two NPC files**

Both files begin with one or two lines starting with `#` (e.g. `# File: assets/data/...`). JSON forbids comments. Remove ONLY those leading `#` lines (and the blank line after), leaving the `{` as the first character. Do not alter any other content — these files hold real, authored dialogue. One-liner:

```python
import re
from pathlib import Path
for p in [Path("Assets/Data/npcs/dialogue_trees/debaucheryville_dialogue.json"),
          Path("Assets/Data/npcs/base_profiles/debaucheryville_core.json")]:
    text = p.read_text(encoding="utf-8-sig")
    p.write_text(re.sub(r"^(\s*#[^\n]*\n)+\s*", "", text), encoding="utf-8")
```

- [ ] **Step 4: Write the slice data files**

`Assets/Data/party/party_members.json` (stats derived from `Design/Character Profiles/LordPilsner/`; tune later, structure is what matters):

```json
{
  "schema_version": "1.0",
  "party_members": {
    "lord_pilsner": {
      "display_name": "Lord Pilsner",
      "level": 1,
      "xp": 0,
      "max_hp": 45,
      "max_sp": 12,
      "offense": 8,
      "defense": 6,
      "speed": 5,
      "charm": 9,
      "luck": 4,
      "grit": 3,
      "skills": ["roast_line"]
    }
  }
}
```

`Assets/Data/enemies/debaucheryville_enemies.json` (replace entire placeholder content):

```json
{
  "schema_version": "1.0",
  "world_name": "debaucheryville",
  "enemies": {
    "feral_segway_tourist": {
      "display_name": "Feral Segway Tourist",
      "battle_intro": "A Feral Segway Tourist rolls up aggressively!",
      "max_hp": 28,
      "offense": 6,
      "defense": 3,
      "speed": 6,
      "luck": 2,
      "xp_reward": 12,
      "gold_reward": 8,
      "item_drop": "lukewarm_kebab",
      "drop_chance": 1.0
    }
  }
}
```

`Assets/Data/items/consumables.json` (replace entire placeholder content):

```json
{
  "schema_version": "1.0",
  "consumables": {
    "lukewarm_kebab": {
      "display_name": "Lukewarm Kebab",
      "heal_hp": 20,
      "heal_sp": 0,
      "description": "Street meat of dubious provenance. Restores 20 HP."
    },
    "absinthe_shot": {
      "display_name": "Absinthe Shot",
      "heal_hp": 0,
      "heal_sp": 8,
      "description": "Tastes like licorice and bad decisions. Restores 8 SP."
    },
    "questionable_goulash": {
      "display_name": "Questionable Goulash",
      "heal_hp": 40,
      "heal_sp": 0,
      "description": "Simmering since the Velvet Revolution. Restores 40 HP."
    }
  }
}
```

`Assets/Data/skills/party_abilities.json` (replace entire placeholder content):

```json
{
  "schema_version": "1.0",
  "abilities": {
    "roast_line": {
      "display_name": "Roast Line",
      "sp_cost": 4,
      "power_multiplier": 1.8,
      "battle_text": "{user} delivers a devastating roast!"
    }
  }
}
```

- [ ] **Step 5: Run validator to verify it passes**

Run: `python Tools/validate_data.py`
Expected: `OK` on all seven lines, exit code 0.

- [ ] **Step 6: Commit**

```bash
git add Tools/validate_data.py Assets/Data/party/party_members.json Assets/Data/enemies/debaucheryville_enemies.json Assets/Data/items/consumables.json Assets/Data/skills/party_abilities.json "Assets/Data/npcs/dialogue_trees/debaucheryville_dialogue.json" "Assets/Data/npcs/base_profiles/debaucheryville_core.json"
git commit -m "data: fix JSON headers, add slice data (party, enemy, items, abilities)"
```

---

### Task 2: DataRepo autoload

**Files:**
- Create: `Scripts/core/data_repo.gd`
- Test: `tests/unit/test_data_repo.gd`
- Modify: `project.godot` (add `[autoload]` section)

**Interfaces:**
- Consumes: the JSON shapes from Task 1.
- Produces (used by every later task):
  - `func load_all() -> bool`
  - `func get_party_member(id: String) -> Dictionary` — e.g. `get_party_member("lord_pilsner")` → dict with `display_name, level, xp, max_hp, max_sp, offense, defense, speed, charm, luck, grit, skills`
  - `func get_enemy(id: String) -> Dictionary`
  - `func get_item(id: String) -> Dictionary`
  - `func get_ability(id: String) -> Dictionary`
  - `func get_dialogue_tree(npc_id: String) -> Dictionary` — e.g. `get_dialogue_tree("vlad_validator")` → `{"default_greeting": {...}, ...}`
  - Unknown IDs: `push_error` naming the ID, return `{}`.

- [ ] **Step 1: Write the failing test**

`tests/unit/test_data_repo.gd`:

```gdscript
extends GutTest

var repo

func before_each() -> void:
	repo = load("res://Scripts/core/data_repo.gd").new()
	assert_true(repo.load_all(), "load_all should succeed with valid data files")

func test_party_member_lord_pilsner() -> void:
	var p: Dictionary = repo.get_party_member("lord_pilsner")
	assert_eq(p.get("display_name"), "Lord Pilsner")
	assert_eq(int(p.get("max_hp")), 45)

func test_enemy_lookup() -> void:
	var e: Dictionary = repo.get_enemy("feral_segway_tourist")
	assert_eq(int(e.get("max_hp")), 28)
	assert_eq(e.get("item_drop"), "lukewarm_kebab")

func test_item_lookup() -> void:
	var i: Dictionary = repo.get_item("lukewarm_kebab")
	assert_eq(int(i.get("heal_hp")), 20)

func test_ability_lookup() -> void:
	var a: Dictionary = repo.get_ability("roast_line")
	assert_eq(int(a.get("sp_cost")), 4)

func test_dialogue_tree_vlad() -> void:
	var t: Dictionary = repo.get_dialogue_tree("vlad_validator")
	assert_true(t.has("default_greeting"))
	var greeting: Dictionary = t["default_greeting"]
	assert_true(greeting.has("text"))
	assert_true(greeting.has("options"))

func test_unknown_id_returns_empty() -> void:
	assert_eq(repo.get_enemy("nonexistent_enemy"), {})
```

- [ ] **Step 2: Run test to verify it fails**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: FAIL — script `data_repo.gd` not found / parse error.

- [ ] **Step 3: Implement DataRepo**

`Scripts/core/data_repo.gd`:

```gdscript
extends Node
## Loads all game data JSON at startup. The ONLY module that touches Assets/Data.
## Content is never hardcoded elsewhere; unknown IDs fail loud.

const DATA_ROOT := "res://Assets/Data/"

var _party: Dictionary = {}
var _enemies: Dictionary = {}
var _items: Dictionary = {}
var _abilities: Dictionary = {}
var _dialogue_trees: Dictionary = {}

func _ready() -> void:
	var ok := load_all()
	assert(ok, "DataRepo: failed to load game data — see errors above")

func load_all() -> bool:
	var ok := true
	var party_doc := _load_json(DATA_ROOT + "party/party_members.json")
	_party = party_doc.get("party_members", {})
	ok = ok and not _party.is_empty()

	var enemy_doc := _load_json(DATA_ROOT + "enemies/debaucheryville_enemies.json")
	_enemies = enemy_doc.get("enemies", {})
	ok = ok and not _enemies.is_empty()

	var item_doc := _load_json(DATA_ROOT + "items/consumables.json")
	_items = item_doc.get("consumables", {})
	ok = ok and not _items.is_empty()

	var ability_doc := _load_json(DATA_ROOT + "skills/party_abilities.json")
	_abilities = ability_doc.get("abilities", {})
	ok = ok and not _abilities.is_empty()

	var dialogue_doc := _load_json(DATA_ROOT + "npcs/dialogue_trees/debaucheryville_dialogue.json")
	_dialogue_trees = dialogue_doc.get("dialogue_trees", {})
	ok = ok and not _dialogue_trees.is_empty()

	return ok

func get_party_member(id: String) -> Dictionary:
	return _lookup(_party, id, "party member")

func get_enemy(id: String) -> Dictionary:
	return _lookup(_enemies, id, "enemy")

func get_item(id: String) -> Dictionary:
	return _lookup(_items, id, "item")

func get_ability(id: String) -> Dictionary:
	return _lookup(_abilities, id, "ability")

func get_dialogue_tree(npc_id: String) -> Dictionary:
	return _lookup(_dialogue_trees, npc_id, "dialogue tree")

func _lookup(table: Dictionary, id: String, kind: String) -> Dictionary:
	if not table.has(id):
		push_error("DataRepo: unknown %s id '%s'" % [kind, id])
		return {}
	return table[id]

func _load_json(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		push_error("DataRepo: missing data file: " + path)
		return {}
	var text := FileAccess.get_file_as_string(path)
	var parsed: Variant = JSON.parse_string(text)
	if parsed == null or not (parsed is Dictionary):
		push_error("DataRepo: invalid JSON in " + path)
		return {}
	return parsed
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: PASS (7 tests incl. smoke). Note: `test_unknown_id_returns_empty` will print one expected `push_error` line.

- [ ] **Step 5: Register the autoload**

Add to `project.godot` (after the `[application]` section):

```ini
[autoload]

DataRepo="*res://Scripts/core/data_repo.gd"
```

Verify the project still boots: `godot --headless --path . --quit`
Expected: exits 0, no script errors printed.

- [ ] **Step 6: Commit**

```bash
git add Scripts/core/data_repo.gd tests/unit/test_data_repo.gd project.godot
git commit -m "feat: DataRepo autoload — JSON loading with loud failures"
```

---

### Task 3: GameState autoload

**Files:**
- Modify (replace 6-line stub): `Scripts/systems/GameState.gd`
- Test: `tests/unit/test_game_state.gd`
- Modify: `project.godot` (append to `[autoload]`)

**Interfaces:**
- Consumes: `DataRepo.get_party_member`, `DataRepo.get_item` (injected as a repo object for testability).
- Produces (used by Save/Battle/Dialogue/UI tasks):
  - `func new_game(repo) -> void` — builds party from data
  - `var party: Array` — `[{id, display_name, hp, sp, max_hp, max_sp, offense, defense, speed, charm, luck, grit, level, xp, skills}]`
  - `var inventory: Dictionary` (item_id → count), `var gold: int`
  - `var flags: Dictionary` (name → true)
  - `var current_scene_path: String`, `var player_position: Vector2`
  - `func add_item(id: String, count: int = 1) -> void`
  - `func use_item(id: String, repo) -> bool` — applies heal to party[0], decrements; false if absent/useless
  - `func set_flag(name: String) -> void`, `func has_flag(name: String) -> bool`
  - `func grant_rewards(xp: int, gold_amount: int, item_id: String) -> void`
  - `func to_dict() -> Dictionary`, `func from_dict(d: Dictionary) -> void` (exact round-trip)

- [ ] **Step 1: Write the failing test**

`tests/unit/test_game_state.gd`:

```gdscript
extends GutTest

var repo
var state

func before_each() -> void:
	repo = load("res://Scripts/core/data_repo.gd").new()
	repo.load_all()
	state = load("res://Scripts/systems/GameState.gd").new()
	state.new_game(repo)

func test_new_game_builds_party_from_data() -> void:
	assert_eq(state.party.size(), 1)
	assert_eq(state.party[0]["id"], "lord_pilsner")
	assert_eq(int(state.party[0]["hp"]), 45)
	assert_eq(int(state.party[0]["sp"]), 12)

func test_add_and_use_item() -> void:
	state.add_item("lukewarm_kebab")
	state.party[0]["hp"] = 10
	assert_true(state.use_item("lukewarm_kebab", repo))
	assert_eq(int(state.party[0]["hp"]), 30)
	assert_false(state.use_item("lukewarm_kebab", repo), "second use should fail — none left")

func test_use_item_caps_at_max_hp() -> void:
	state.add_item("lukewarm_kebab")
	state.party[0]["hp"] = 40
	state.use_item("lukewarm_kebab", repo)
	assert_eq(int(state.party[0]["hp"]), 45)

func test_flags() -> void:
	assert_false(state.has_flag("vlad_insulted"))
	state.set_flag("vlad_insulted")
	assert_true(state.has_flag("vlad_insulted"))

func test_grant_rewards() -> void:
	state.grant_rewards(12, 8, "lukewarm_kebab")
	assert_eq(int(state.party[0]["xp"]), 12)
	assert_eq(state.gold, 8)
	assert_eq(int(state.inventory.get("lukewarm_kebab", 0)), 1)

func test_round_trip() -> void:
	state.add_item("absinthe_shot", 2)
	state.set_flag("test_flag")
	state.gold = 99
	state.player_position = Vector2(120, 88)
	state.current_scene_path = "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn"
	var d := state.to_dict()
	var restored = load("res://Scripts/systems/GameState.gd").new()
	restored.from_dict(d)
	assert_eq(restored.to_dict(), d)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: FAIL — `new_game` not defined (stub has no methods).

- [ ] **Step 3: Implement GameState**

Replace `Scripts/systems/GameState.gd` entirely:

```gdscript
extends Node
## Single source of truth for run-time game state. What SaveSystem serializes.
## Holds no behavior about HOW scenes change (SceneRouter) or WHERE data
## comes from (DataRepo is passed in where needed, keeping this testable).

var party: Array = []
var inventory: Dictionary = {}
var gold: int = 0
var flags: Dictionary = {}
var current_scene_path: String = ""
var player_position: Vector2 = Vector2.ZERO

func new_game(repo) -> void:
	party = []
	inventory = {}
	gold = 20
	flags = {}
	current_scene_path = "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn"
	player_position = Vector2.ZERO
	_add_party_member("lord_pilsner", repo)

func _add_party_member(id: String, repo) -> void:
	var data: Dictionary = repo.get_party_member(id)
	if data.is_empty():
		return
	var member := {
		"id": id,
		"display_name": data.get("display_name", id),
		"level": int(data.get("level", 1)),
		"xp": int(data.get("xp", 0)),
		"hp": int(data.get("max_hp", 1)),
		"max_hp": int(data.get("max_hp", 1)),
		"sp": int(data.get("max_sp", 0)),
		"max_sp": int(data.get("max_sp", 0)),
		"offense": int(data.get("offense", 1)),
		"defense": int(data.get("defense", 0)),
		"speed": int(data.get("speed", 1)),
		"charm": int(data.get("charm", 0)),
		"luck": int(data.get("luck", 0)),
		"grit": int(data.get("grit", 0)),
		"skills": data.get("skills", []),
	}
	party.append(member)

func add_item(id: String, count: int = 1) -> void:
	inventory[id] = int(inventory.get(id, 0)) + count

func use_item(id: String, repo) -> bool:
	if int(inventory.get(id, 0)) <= 0:
		return false
	var item: Dictionary = repo.get_item(id)
	if item.is_empty() or party.is_empty():
		return false
	var member: Dictionary = party[0]
	member["hp"] = mini(int(member["max_hp"]), int(member["hp"]) + int(item.get("heal_hp", 0)))
	member["sp"] = mini(int(member["max_sp"]), int(member["sp"]) + int(item.get("heal_sp", 0)))
	inventory[id] = int(inventory[id]) - 1
	if inventory[id] <= 0:
		inventory.erase(id)
	return true

func set_flag(flag_name: String) -> void:
	flags[flag_name] = true

func has_flag(flag_name: String) -> bool:
	return flags.get(flag_name, false)

func grant_rewards(xp: int, gold_amount: int, item_id: String) -> void:
	if not party.is_empty():
		party[0]["xp"] = int(party[0]["xp"]) + xp
	gold += gold_amount
	if item_id != "":
		add_item(item_id)

func to_dict() -> Dictionary:
	return {
		"party": party.duplicate(true),
		"inventory": inventory.duplicate(true),
		"gold": gold,
		"flags": flags.duplicate(true),
		"current_scene_path": current_scene_path,
		"player_position": {"x": player_position.x, "y": player_position.y},
	}

func from_dict(d: Dictionary) -> void:
	party = d.get("party", [])
	inventory = d.get("inventory", {})
	gold = int(d.get("gold", 0))
	flags = d.get("flags", {})
	current_scene_path = d.get("current_scene_path", "")
	var pos: Dictionary = d.get("player_position", {"x": 0, "y": 0})
	player_position = Vector2(float(pos.get("x", 0)), float(pos.get("y", 0)))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: PASS.

- [ ] **Step 5: Register autoload (after DataRepo)**

In `project.godot` `[autoload]` section, append:

```ini
GameState="*res://Scripts/systems/GameState.gd"
```

Verify: `godot --headless --path . --quit` → exit 0, no errors.

- [ ] **Step 6: Commit**

```bash
git add Scripts/systems/GameState.gd tests/unit/test_game_state.gd project.godot
git commit -m "feat: GameState autoload — party, inventory, flags, round-trip serialization"
```

---

### Task 4: SaveSystem autoload

**Files:**
- Modify (replace empty stub): `Scripts/core/save_system.gd`
- Test: `tests/unit/test_save_system.gd`
- Modify: `project.godot` (append to `[autoload]`)

**Interfaces:**
- Consumes: a GameState-shaped object (`to_dict`/`from_dict`), injected for testability.
- Produces (used by TitleScreen and PauseMenu):
  - `const SAVE_PATH := "user://saves/slot1.json"`
  - `func save_game(state) -> bool`
  - `func load_game(state) -> bool` — false on missing/corrupt file, state untouched
  - `func has_save() -> bool` — true only if the file exists AND parses

- [ ] **Step 1: Write the failing test**

`tests/unit/test_save_system.gd`:

```gdscript
extends GutTest

var saver
var state

func before_each() -> void:
	saver = load("res://Scripts/core/save_system.gd").new()
	var repo = load("res://Scripts/core/data_repo.gd").new()
	repo.load_all()
	state = load("res://Scripts/systems/GameState.gd").new()
	state.new_game(repo)
	if FileAccess.file_exists(saver.SAVE_PATH):
		DirAccess.remove_absolute(saver.SAVE_PATH)

func test_no_save_initially() -> void:
	assert_false(saver.has_save())

func test_save_then_load_round_trip() -> void:
	state.gold = 77
	state.set_flag("saved_once")
	assert_true(saver.save_game(state))
	assert_true(saver.has_save())
	var fresh = load("res://Scripts/systems/GameState.gd").new()
	assert_true(saver.load_game(fresh))
	assert_eq(fresh.gold, 77)
	assert_true(fresh.has_flag("saved_once"))

func test_corrupt_save_is_not_loadable() -> void:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var f := FileAccess.open(saver.SAVE_PATH, FileAccess.WRITE)
	f.store_string("{ this is not json")
	f.close()
	assert_false(saver.has_save())
	assert_false(saver.load_game(state))
	assert_eq(state.gold, 20, "failed load must leave state untouched")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: FAIL — SAVE_PATH/methods not defined.

- [ ] **Step 3: Implement SaveSystem**

`Scripts/core/save_system.gd`:

```gdscript
extends Node
## Persists GameState to disk as JSON. Corrupt saves are treated as absent —
## the player sees a disabled Continue button, never a crash.

const SAVE_PATH := "user://saves/slot1.json"

func save_game(state) -> bool:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var f := FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if f == null:
		push_error("SaveSystem: cannot open %s for writing (%s)" % [SAVE_PATH, FileAccess.get_open_error()])
		return false
	f.store_string(JSON.stringify(state.to_dict(), "  "))
	f.close()
	return true

func load_game(state) -> bool:
	var data := _read_save()
	if data.is_empty():
		return false
	state.from_dict(data)
	return true

func has_save() -> bool:
	return not _read_save().is_empty()

func _read_save() -> Dictionary:
	if not FileAccess.file_exists(SAVE_PATH):
		return {}
	var text := FileAccess.get_file_as_string(SAVE_PATH)
	var parsed: Variant = JSON.parse_string(text)
	if parsed == null or not (parsed is Dictionary):
		push_error("SaveSystem: save file is corrupt: " + SAVE_PATH)
		return {}
	return parsed
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: PASS (corrupt-save test prints one expected `push_error`).

- [ ] **Step 5: Register autoload and commit**

Append to `[autoload]`: `SaveSystem="*res://Scripts/core/save_system.gd"`
Verify boot: `godot --headless --path . --quit` → exit 0.

```bash
git add Scripts/core/save_system.gd tests/unit/test_save_system.gd project.godot
git commit -m "feat: SaveSystem — slot1 JSON persistence with corrupt-save fallback"
```

---

### Task 5: Input actions and SceneRouter

**Files:**
- Modify (replace empty stub): `Scripts/core/input_manager.gd`
- Create: `Scripts/core/scene_router.gd`
- Modify: `project.godot` (append to `[autoload]`)

**Interfaces:**
- Produces input actions (used by Player, DialogueBox, menus): `move_left`, `move_right`, `move_up`, `move_down` (WASD + arrows), `interact` (E, Space, Enter), `pause` (Esc).
- Produces SceneRouter API (used by Enemy, BattleScene, TitleScreen, PauseMenu, locations):
  - `func goto_scene(path: String) -> void`
  - `func goto_battle(enemy_id: String) -> void` — stashes return scene + player position from GameState
  - `func end_battle() -> void` — returns to the stashed scene; sets `restore_pending = true`
  - `var pending_enemy_id: String`
  - `var restore_pending: bool` — location scripts check this to reposition the player at `GameState.player_position`

- [ ] **Step 1: Implement input registration**

`Scripts/core/input_manager.gd`:

```gdscript
extends Node
## Registers gameplay input actions in code — avoids hand-editing serialized
## InputEventKey blocks in project.godot.

const ACTIONS := {
	"move_left": [KEY_A, KEY_LEFT],
	"move_right": [KEY_D, KEY_RIGHT],
	"move_up": [KEY_W, KEY_UP],
	"move_down": [KEY_S, KEY_DOWN],
	"interact": [KEY_E, KEY_SPACE, KEY_ENTER],
	"pause": [KEY_ESCAPE],
}

func _ready() -> void:
	for action in ACTIONS:
		if not InputMap.has_action(action):
			InputMap.add_action(action)
		for keycode in ACTIONS[action]:
			var ev := InputEventKey.new()
			ev.physical_keycode = keycode
			InputMap.action_add_event(action, ev)
```

- [ ] **Step 2: Implement SceneRouter**

`Scripts/core/scene_router.gd`:

```gdscript
extends Node
## All scene transitions go through here. Owns the overworld↔battle handoff:
## remembers where the player was so locations can restore position.

var pending_enemy_id: String = ""
var restore_pending: bool = false

var _return_scene_path: String = ""

func goto_scene(path: String) -> void:
	GameState.current_scene_path = path
	get_tree().call_deferred("change_scene_to_file", path)

func goto_battle(enemy_id: String) -> void:
	pending_enemy_id = enemy_id
	_return_scene_path = GameState.current_scene_path
	get_tree().call_deferred("change_scene_to_file", "res://Scenes/battle/BattleScene.tscn")

func end_battle() -> void:
	pending_enemy_id = ""
	restore_pending = true
	get_tree().call_deferred("change_scene_to_file", _return_scene_path)
```

- [ ] **Step 3: Register autoloads**

Append to `[autoload]` (InputSetup before SceneRouter, both after the data/state autoloads):

```ini
InputSetup="*res://Scripts/core/input_manager.gd"
SceneRouter="*res://Scripts/core/scene_router.gd"
```

- [ ] **Step 4: Verify boot**

Run: `godot --headless --path . --quit`
Expected: exit 0, no errors. (SceneRouter references the GameState autoload; both must be registered.)

- [ ] **Step 5: Commit**

```bash
git add Scripts/core/input_manager.gd Scripts/core/scene_router.gd project.godot
git commit -m "feat: input actions in code + SceneRouter with battle handoff"
```

---

### Task 6: Player scene and movement

**Files:**
- Modify (replace empty stubs): `Scripts/characters/player_controller.gd`, `Scenes/characters/Player.tscn`

**Interfaces:**
- Consumes: input actions from Task 5.
- Produces (used by locations, NPC, Enemy):
  - `Player.tscn` — root `CharacterBody2D` named `Player`, collision layer 1; builds its own ColorRect visual, collision shape, `Camera2D`, and an `InteractZone` (`Area2D`, collision mask 2) in `_ready()`
  - `var can_move: bool` — dialogue/menus set false to freeze the player
  - On `interact` press: calls `interact()` on the nearest overlapping area that has that method

- [ ] **Step 1: Write the scene file**

`Scenes/characters/Player.tscn` (replace placeholder content entirely):

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/characters/player_controller.gd" id="1"]

[node name="Player" type="CharacterBody2D"]
script = ExtResource("1")
```

- [ ] **Step 2: Implement the controller**

`Scripts/characters/player_controller.gd`:

```gdscript
extends CharacterBody2D
## Overworld player: 8-direction movement, interaction with nearby areas.
## Children are built in _ready() so the .tscn stays a trivial text file.

const SPEED := 140.0

var can_move: bool = true

var _interact_zone: Area2D

func _ready() -> void:
	collision_layer = 1
	collision_mask = 1

	var visual := ColorRect.new()
	visual.color = Color(0.9, 0.75, 0.2)  # beer-gold placeholder for Lord Pilsner
	visual.size = Vector2(24, 32)
	visual.position = Vector2(-12, -28)
	add_child(visual)

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = Vector2(22, 14)
	shape.shape = rect
	shape.position = Vector2(0, -4)
	add_child(shape)

	var camera := Camera2D.new()
	camera.zoom = Vector2(2, 2)
	add_child(camera)

	_interact_zone = Area2D.new()
	_interact_zone.collision_layer = 0
	_interact_zone.collision_mask = 2
	var zone_shape := CollisionShape2D.new()
	var zone_rect := RectangleShape2D.new()
	zone_rect.size = Vector2(48, 48)
	zone_shape.shape = zone_rect
	_interact_zone.add_child(zone_shape)
	add_child(_interact_zone)

func _physics_process(_delta: float) -> void:
	if not can_move:
		velocity = Vector2.ZERO
		return
	var direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = direction * SPEED
	move_and_slide()
	GameState.player_position = global_position

func _unhandled_input(event: InputEvent) -> void:
	if not can_move:
		return
	if event.is_action_pressed("interact"):
		for area in _interact_zone.get_overlapping_areas():
			if area.has_method("interact"):
				area.interact()
				return
```

- [ ] **Step 3: Verify scripts parse**

Run: `godot --headless --path . --quit`
Expected: exit 0, no parse errors.

- [ ] **Step 4: Commit**

```bash
git add Scripts/characters/player_controller.gd Scenes/characters/Player.tscn
git commit -m "feat: player movement, camera, and interaction zone"
```

---

### Task 7: Location template and Clocktower Plaza

**Files:**
- Create: `Scripts/worlds/location_base.gd`, `Scripts/worlds/clocktower_plaza.gd`
- Modify (replace any placeholder): `Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn`

**Interfaces:**
- Consumes: `Player.tscn`, `SceneRouter.restore_pending`, `GameState.player_position`, `DataRepo` location metadata.
- Produces:
  - `location_base.gd` — `class_name LocationBase extends Node2D`; exports `location_id: String`, `bounds: Rect2` (default `Rect2(0, 0, 960, 640)`); in `_ready()` builds floor ColorRect, four boundary `StaticBody2D` walls, spawns the Player at `spawn_point` (or restores position if `SceneRouter.restore_pending`), and instances `PauseMenu.tscn`
  - `var spawn_point: Vector2` — subclasses set before calling `super._ready()`
  - `func spawn_npc(npc_id: String, pos: Vector2) -> void`, `func spawn_enemy(enemy_id: String, pos: Vector2) -> void` — every future location reuses these
  - `ClocktowerPlaza.tscn` — the slice location: one NPC (`vlad_validator`) and one enemy (`feral_segway_tourist`)

- [ ] **Step 1: Implement LocationBase**

`Scripts/worlds/location_base.gd`:

```gdscript
class_name LocationBase
extends Node2D
## Template every location extends: placeholder floor, boundary walls,
## player spawn/restore, pause menu. Subclasses set spawn_point and
## spawn their NPCs/enemies, then call super._ready().

const PLAYER_SCENE := preload("res://Scenes/characters/Player.tscn")
const NPC_SCENE := preload("res://Scenes/characters/NPCBase.tscn")
const ENEMY_SCENE := preload("res://Scenes/characters/Enemy.tscn")
const PAUSE_MENU_SCENE := preload("res://Scenes/ui/menus/PauseMenu.tscn")

@export var location_id: String = ""
@export var bounds: Rect2 = Rect2(0, 0, 960, 640)

var spawn_point: Vector2 = Vector2(480, 320)
var player: CharacterBody2D

func _ready() -> void:
	_build_floor()
	_build_walls()
	player = PLAYER_SCENE.instantiate()
	if SceneRouter.restore_pending:
		player.position = GameState.player_position
		SceneRouter.restore_pending = false
	else:
		player.position = spawn_point
		GameState.player_position = spawn_point
	add_child(player)
	add_child(PAUSE_MENU_SCENE.instantiate())

func spawn_npc(npc_id: String, pos: Vector2) -> void:
	var npc := NPC_SCENE.instantiate()
	npc.npc_id = npc_id
	npc.position = pos
	add_child(npc)

func spawn_enemy(enemy_id: String, pos: Vector2) -> void:
	var enemy := ENEMY_SCENE.instantiate()
	enemy.enemy_id = enemy_id
	enemy.position = pos
	add_child(enemy)

func _build_floor() -> void:
	var floor_rect := ColorRect.new()
	floor_rect.color = Color(0.25, 0.22, 0.28)  # grimy cobblestone placeholder
	floor_rect.position = bounds.position
	floor_rect.size = bounds.size
	floor_rect.z_index = -10
	add_child(floor_rect)

func _build_walls() -> void:
	var thickness := 16.0
	var edges := [
		Rect2(bounds.position - Vector2(0, thickness), Vector2(bounds.size.x, thickness)),
		Rect2(Vector2(bounds.position.x, bounds.end.y), Vector2(bounds.size.x, thickness)),
		Rect2(bounds.position - Vector2(thickness, 0), Vector2(thickness, bounds.size.y)),
		Rect2(Vector2(bounds.end.x, bounds.position.y), Vector2(thickness, bounds.size.y)),
	]
	for edge in edges:
		var wall := StaticBody2D.new()
		wall.collision_layer = 1
		var shape := CollisionShape2D.new()
		var rect := RectangleShape2D.new()
		rect.size = edge.size
		shape.shape = rect
		wall.position = edge.position + edge.size / 2.0
		wall.add_child(shape)
		add_child(wall)
```

- [ ] **Step 2: Implement Clocktower Plaza**

`Scripts/worlds/clocktower_plaza.gd`:

```gdscript
extends LocationBase
## The vertical slice's one location. Vlad guards the Absinthe Arcade
## entrance; one Feral Segway Tourist roams the plaza.

func _ready() -> void:
	location_id = "debaucheryville_clocktower_plaza"
	spawn_point = Vector2(480, 500)
	super._ready()
	spawn_npc("vlad_validator", Vector2(480, 140))
	spawn_enemy("feral_segway_tourist", Vector2(240, 320))
```

`Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn`:

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/worlds/clocktower_plaza.gd" id="1"]

[node name="ClocktowerPlaza" type="Node2D"]
script = ExtResource("1")
```

- [ ] **Step 3: Create placeholder NPC/Enemy/PauseMenu scene stubs so preloads resolve**

These get real implementations in Tasks 8, 9, 11 — for now, minimal valid scenes so the location parses.

`Scenes/characters/NPCBase.tscn`:

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/characters/npc_controller.gd" id="1"]

[node name="NPCBase" type="Area2D"]
script = ExtResource("1")
```

`Scripts/characters/npc_controller.gd` (minimal, expanded in Task 8):

```gdscript
extends Area2D

@export var npc_id: String = ""
```

`Scenes/characters/Enemy.tscn`:

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/characters/enemy.gd" id="1"]

[node name="Enemy" type="Area2D"]
script = ExtResource("1")
```

`Scripts/characters/enemy.gd` (minimal, expanded in Task 9):

```gdscript
extends Area2D

@export var enemy_id: String = ""
```

`Scenes/ui/menus/PauseMenu.tscn`:

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/ui/pause_menu.gd" id="1"]

[node name="PauseMenu" type="CanvasLayer"]
script = ExtResource("1")
```

`Scripts/ui/pause_menu.gd` (minimal, expanded in Task 11):

```gdscript
extends CanvasLayer
```

- [ ] **Step 4: Verify the scene loads headless**

Run: `godot --headless --path . "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn" --quit-after 3`
Expected: exit 0, no script errors.

- [ ] **Step 5: Manual check (first visible milestone!)**

Run: `godot --path . "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn"`
Expected: a dark plaza with a gold rectangle (you) that moves with WASD/arrows, blocked at all four edges. Close the window when satisfied.

- [ ] **Step 6: Commit**

```bash
git add Scripts/worlds/ Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn Scenes/characters/NPCBase.tscn Scripts/characters/npc_controller.gd Scenes/characters/Enemy.tscn Scripts/characters/enemy.gd Scenes/ui/menus/PauseMenu.tscn Scripts/ui/pause_menu.gd
git commit -m "feat: LocationBase template + walkable Clocktower Plaza"
```

---

### Task 8: Dialogue — runner, box UI, and NPC wiring

**Files:**
- Create: `Scripts/systems/dialogue_runner.gd`, `Scripts/ui/dialogue_box.gd`
- Modify: `Scenes/ui/dialogue/DialogueBox.tscn` (replace placeholder), `Scripts/characters/npc_controller.gd` (expand stub)
- Test: `tests/unit/test_dialogue_runner.gd`

**Interfaces:**
- Consumes: `DataRepo.get_dialogue_tree(npc_id)` — real Vlad data with node shape `{text, speaker, options: [{text, leads_to, requires: null|{item}, sets_flags?}]}`.
- Produces:
  - `DialogueRunner` (pure, `class_name DialogueRunner`):
    - `_init(tree: Dictionary)`
    - `func start(node_key: String = "default_greeting") -> Dictionary` — returns the node, records its `sets_flags`
    - `func available_options(inventory: Dictionary) -> Array` — filters options whose `requires.item` is absent from inventory
    - `func choose(option: Dictionary) -> Dictionary` — follows `leads_to`, records option `sets_flags`; returns `{}` when dialogue ends
    - `var collected_flags: Array` — caller applies to GameState when dialogue closes
  - `DialogueBox.tscn` — `CanvasLayer`; `func open(npc_id: String, player) -> void` freezes player, shows typewriter text + option buttons, applies flags on close, unfreezes player
  - `npc_controller.gd` — `func interact()` instances DialogueBox and opens its own `npc_id`

- [ ] **Step 1: Write the failing runner test**

`tests/unit/test_dialogue_runner.gd`:

```gdscript
extends GutTest

var repo
var tree: Dictionary

func before_each() -> void:
	repo = load("res://Scripts/core/data_repo.gd").new()
	repo.load_all()
	tree = repo.get_dialogue_tree("vlad_validator")

func test_start_returns_greeting() -> void:
	var runner := DialogueRunner.new(tree)
	var node := runner.start()
	assert_true(node.has("text"))
	assert_eq(node.get("speaker"), "Vlad the Validator")

func test_option_requiring_item_is_hidden_without_it() -> void:
	var runner := DialogueRunner.new(tree)
	runner.start()
	var all_options: Array = tree["default_greeting"]["options"]
	var visible := runner.available_options({})
	assert_lt(visible.size(), all_options.size(),
		"the [Show NFT Screenshot] option requires an item the player lacks")

func test_option_requiring_item_shown_with_it() -> void:
	var runner := DialogueRunner.new(tree)
	runner.start()
	var visible := runner.available_options({"Rare_NFT_Screenshot": 1})
	assert_eq(visible.size(), tree["default_greeting"]["options"].size())

func test_choose_follows_leads_to() -> void:
	var runner := DialogueRunner.new(tree)
	runner.start()
	var options := runner.available_options({})
	var next := runner.choose(options[0])
	assert_true(next.has("text"), "choosing an option should enter the next node")

func test_unknown_node_returns_empty() -> void:
	var runner := DialogueRunner.new(tree)
	assert_eq(runner.start("no_such_node"), {})
```

- [ ] **Step 2: Run test to verify it fails**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: FAIL — `DialogueRunner` not declared.

- [ ] **Step 3: Implement DialogueRunner**

`Scripts/systems/dialogue_runner.gd`:

```gdscript
class_name DialogueRunner
## Pure dialogue-tree traversal — no UI, no autoload access, fully testable.
## Understands the fields the slice needs (text/speaker/options/leads_to/
## requires.item/sets_flags) and ignores the rest of the authored schema.

var collected_flags: Array = []
var current_key: String = ""

var _tree: Dictionary

func _init(tree: Dictionary) -> void:
	_tree = tree

func start(node_key: String = "default_greeting") -> Dictionary:
	collected_flags = []
	return _enter(node_key)

func available_options(inventory: Dictionary) -> Array:
	var node: Dictionary = _tree.get(current_key, {})
	var visible: Array = []
	for option in node.get("options", []):
		var req: Variant = option.get("requires")
		if req is Dictionary and req.has("item"):
			if int(inventory.get(req["item"], 0)) > 0:
				visible.append(option)
		else:
			visible.append(option)
	return visible

func choose(option: Dictionary) -> Dictionary:
	for flag in option.get("sets_flags", []):
		collected_flags.append(flag)
	var next: Variant = option.get("leads_to", "")
	if next == null or String(next).is_empty():
		current_key = ""
		return {}
	return _enter(String(next))

func _enter(key: String) -> Dictionary:
	if not _tree.has(key):
		push_error("DialogueRunner: unknown dialogue node '%s'" % key)
		current_key = ""
		return {}
	current_key = key
	var node: Dictionary = _tree[key]
	for flag in node.get("sets_flags", []):
		collected_flags.append(flag)
	return node
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: PASS.

- [ ] **Step 5: Implement the DialogueBox UI**

`Scenes/ui/dialogue/DialogueBox.tscn` (replace placeholder):

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/ui/dialogue_box.gd" id="1"]

[node name="DialogueBox" type="CanvasLayer"]
script = ExtResource("1")
```

`Scripts/ui/dialogue_box.gd`:

```gdscript
extends CanvasLayer
## Bottom-anchored dialogue panel: speaker name, typewriter text, option
## buttons. Applies collected flags to GameState when the dialogue closes.

const CHARS_PER_SECOND := 40.0

var _runner: DialogueRunner
var _player
var _panel: PanelContainer
var _speaker_label: Label
var _text_label: Label
var _options_box: VBoxContainer
var _full_text: String = ""
var _typing: bool = false

func _ready() -> void:
	layer = 10
	_panel = PanelContainer.new()
	_panel.anchor_left = 0.05
	_panel.anchor_right = 0.95
	_panel.anchor_top = 0.7
	_panel.anchor_bottom = 0.97
	add_child(_panel)

	var vbox := VBoxContainer.new()
	_panel.add_child(vbox)

	_speaker_label = Label.new()
	_speaker_label.add_theme_color_override("font_color", Color(0.95, 0.8, 0.3))
	vbox.add_child(_speaker_label)

	_text_label = Label.new()
	_text_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_text_label.size_flags_vertical = Control.SIZE_EXPAND_FILL
	vbox.add_child(_text_label)

	_options_box = VBoxContainer.new()
	vbox.add_child(_options_box)

func open(npc_id: String, player) -> void:
	_player = player
	_player.can_move = false
	var tree: Dictionary = DataRepo.get_dialogue_tree(npc_id)
	if tree.is_empty():
		_close()
		return
	_runner = DialogueRunner.new(tree)
	_show_node(_runner.start())

func _show_node(node: Dictionary) -> void:
	if node.is_empty():
		_close()
		return
	_speaker_label.text = String(node.get("speaker", ""))
	_full_text = String(node.get("text", ""))
	_start_typing()

func _start_typing() -> void:
	_typing = true
	_clear_options()
	_text_label.text = ""
	var tween := create_tween()
	var duration := _full_text.length() / CHARS_PER_SECOND
	tween.tween_method(_set_visible_chars, 0, _full_text.length(), duration)
	tween.finished.connect(_on_typing_done)

func _set_visible_chars(count: int) -> void:
	_text_label.text = _full_text.substr(0, count)

func _on_typing_done() -> void:
	_typing = false
	_text_label.text = _full_text
	_build_options()

func _build_options() -> void:
	_clear_options()
	var options := _runner.available_options(GameState.inventory)
	if options.is_empty():
		var done := Button.new()
		done.text = "[End]"
		done.pressed.connect(_close)
		_options_box.add_child(done)
		done.grab_focus()
		return
	var first := true
	for option in options:
		var button := Button.new()
		button.text = String(option.get("text", "..."))
		button.pressed.connect(_on_option_pressed.bind(option))
		_options_box.add_child(button)
		if first:
			button.grab_focus()
			first = false

func _on_option_pressed(option: Dictionary) -> void:
	_show_node(_runner.choose(option))

func _clear_options() -> void:
	for child in _options_box.get_children():
		child.queue_free()

func _unhandled_input(event: InputEvent) -> void:
	if _typing and event.is_action_pressed("interact"):
		# Skip the typewriter animation.
		get_viewport().set_input_as_handled()
		for tween in get_tree().get_processed_tweens():
			tween.kill()
		_on_typing_done()

func _close() -> void:
	if _runner != null:
		for flag in _runner.collected_flags:
			GameState.set_flag(flag)
	if _player != null:
		_player.can_move = true
	queue_free()
```

- [ ] **Step 6: Wire the NPC**

Replace `Scripts/characters/npc_controller.gd`:

```gdscript
extends Area2D
## Static overworld NPC. Player's InteractZone (mask 2) finds us on layer 2;
## interact() opens our dialogue tree.

const DIALOGUE_BOX_SCENE := preload("res://Scenes/ui/dialogue/DialogueBox.tscn")

@export var npc_id: String = ""

func _ready() -> void:
	collision_layer = 2
	collision_mask = 0

	var visual := ColorRect.new()
	visual.color = Color(0.3, 0.6, 0.9)  # bouncer-blue placeholder
	visual.size = Vector2(24, 32)
	visual.position = Vector2(-12, -28)
	add_child(visual)

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = Vector2(32, 40)
	shape.shape = rect
	add_child(shape)

	var body := StaticBody2D.new()
	body.collision_layer = 1
	var body_shape := CollisionShape2D.new()
	var body_rect := RectangleShape2D.new()
	body_rect.size = Vector2(24, 16)
	body_shape.shape = body_rect
	body_shape.position = Vector2(0, -4)
	body.add_child(body_shape)
	add_child(body)

func interact() -> void:
	var location := get_parent()
	var box := DIALOGUE_BOX_SCENE.instantiate()
	location.add_child(box)
	box.open(npc_id, location.player)
```

- [ ] **Step 7: Verify headless + manual dialogue check**

Run: `godot --headless --path . "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn" --quit-after 3` → exit 0.
Then: `godot --path . "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn"` — walk to the blue rectangle, press E. Expected: Vlad's greeting types out, options appear, choosing walks the tree, `[End]`/terminal option closes it and you can move again.

- [ ] **Step 8: Commit**

```bash
git add Scripts/systems/dialogue_runner.gd Scripts/ui/dialogue_box.gd Scenes/ui/dialogue/DialogueBox.tscn Scripts/characters/npc_controller.gd tests/unit/test_dialogue_runner.gd
git commit -m "feat: dialogue system — pure runner, typewriter box, NPC wiring"
```

---

### Task 9: Overworld enemy and battle trigger

**Files:**
- Modify (expand stub): `Scripts/characters/enemy.gd`

**Interfaces:**
- Consumes: `SceneRouter.goto_battle(enemy_id)`, Player (collision layer 1).
- Produces: an enemy that wanders randomly and, on touching the player, freezes both and calls `SceneRouter.goto_battle(enemy_id)`.

- [ ] **Step 1: Implement the enemy**

Replace `Scripts/characters/enemy.gd`:

```gdscript
extends Area2D
## Visible overworld enemy: wanders near its spawn, touching the player
## starts a battle via SceneRouter.

const WANDER_SPEED := 50.0
const WANDER_RADIUS := 120.0

@export var enemy_id: String = ""

var _home: Vector2
var _direction: Vector2 = Vector2.ZERO
var _triggered: bool = false

func _ready() -> void:
	collision_layer = 0
	collision_mask = 1
	_home = position

	var visual := ColorRect.new()
	visual.color = Color(0.85, 0.25, 0.25)  # danger-red placeholder
	visual.size = Vector2(26, 26)
	visual.position = Vector2(-13, -13)
	add_child(visual)

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = Vector2(26, 26)
	shape.shape = rect
	add_child(shape)

	body_entered.connect(_on_body_entered)

	var timer := Timer.new()
	timer.wait_time = 1.2
	timer.timeout.connect(_pick_direction)
	add_child(timer)
	timer.start()
	_pick_direction()

func _pick_direction() -> void:
	if position.distance_to(_home) > WANDER_RADIUS:
		_direction = (_home - position).normalized()
	else:
		_direction = Vector2.from_angle(randf() * TAU) if randf() > 0.3 else Vector2.ZERO

func _process(delta: float) -> void:
	if not _triggered:
		position += _direction * WANDER_SPEED * delta

func _on_body_entered(body: Node) -> void:
	if _triggered or not (body is CharacterBody2D):
		return
	_triggered = true
	body.can_move = false
	SceneRouter.goto_battle(enemy_id)
```

- [ ] **Step 2: Verify headless**

Run: `godot --headless --path . "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn" --quit-after 3`
Expected: exit 0. (Touching the enemy would error until BattleScene exists in Task 10 — that's fine; don't touch it in manual runs yet.)

- [ ] **Step 3: Commit**

```bash
git add Scripts/characters/enemy.gd
git commit -m "feat: wandering overworld enemy that triggers battle on contact"
```

---

### Task 10: Battle — damage calculator and battle scene

**Files:**
- Modify (replace empty stubs): `Scripts/battle/damage_calculator.gd`, `Scripts/battle/battle_manager.gd`, `Scenes/battle/BattleScene.tscn`
- Test: `tests/unit/test_damage_calculator.gd`

**Interfaces:**
- Consumes: `SceneRouter.pending_enemy_id`, `SceneRouter.end_battle()`, `DataRepo.get_enemy/get_ability/get_item`, `GameState.party/inventory/use_item/grant_rewards`.
- Produces:
  - `DamageCalculator` (pure, `class_name DamageCalculator`):
    - `static func compute(attacker: Dictionary, defender: Dictionary, rng: RandomNumberGenerator, multiplier: float = 1.0) -> Dictionary` → `{"damage": int >= 1, "crit": bool}`; crit chance = `luck * 0.01`, crit doubles damage
  - `BattleScene.tscn` — reads `SceneRouter.pending_enemy_id`; menu Bash / Roast Line / Item / Run; win → `GameState.grant_rewards` + `SceneRouter.end_battle()`; lose → party[0] hp set to 1 + `end_battle()`; Run → 50% flee

- [ ] **Step 1: Write the failing damage test**

`tests/unit/test_damage_calculator.gd`:

```gdscript
extends GutTest

func _rng(seed_value: int) -> RandomNumberGenerator:
	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value
	return rng

func test_damage_is_at_least_one() -> void:
	var weak := {"offense": 1, "luck": 0}
	var tank := {"defense": 99}
	for i in range(20):
		var result := DamageCalculator.compute(weak, tank, _rng(i))
		assert_gt(int(result["damage"]), 0)

func test_damage_scales_with_offense() -> void:
	var rng_a := _rng(42)
	var rng_b := _rng(42)
	var low := DamageCalculator.compute({"offense": 4, "luck": 0}, {"defense": 2}, rng_a)
	var high := DamageCalculator.compute({"offense": 10, "luck": 0}, {"defense": 2}, rng_b)
	assert_gt(int(high["damage"]), int(low["damage"]))

func test_multiplier_increases_damage() -> void:
	var base := DamageCalculator.compute({"offense": 8, "luck": 0}, {"defense": 3}, _rng(7), 1.0)
	var boosted := DamageCalculator.compute({"offense": 8, "luck": 0}, {"defense": 3}, _rng(7), 1.8)
	assert_gt(int(boosted["damage"]), int(base["damage"]))

func test_zero_luck_never_crits() -> void:
	for i in range(50):
		var result := DamageCalculator.compute({"offense": 5, "luck": 0}, {"defense": 1}, _rng(i))
		assert_false(result["crit"])

func test_max_luck_always_crits() -> void:
	for i in range(50):
		var result := DamageCalculator.compute({"offense": 5, "luck": 100}, {"defense": 1}, _rng(i))
		assert_true(result["crit"])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: FAIL — `DamageCalculator` not declared.

- [ ] **Step 3: Implement DamageCalculator**

Replace `Scripts/battle/damage_calculator.gd`:

```gdscript
class_name DamageCalculator
## Pure damage math. RNG is injected so tests are deterministic.
## Formula (slice-simple, tune later): offense*2 − defense, ±2 spread,
## floor 1; crit chance = luck%, crit doubles.

static func compute(attacker: Dictionary, defender: Dictionary, rng: RandomNumberGenerator, multiplier: float = 1.0) -> Dictionary:
	var base := int(attacker.get("offense", 1)) * 2 - int(defender.get("defense", 0))
	base = maxi(1, base)
	var damage := maxi(1, int(round(base * multiplier)) + rng.randi_range(-2, 2))
	var crit := rng.randf() < float(attacker.get("luck", 0)) * 0.01
	if crit:
		damage *= 2
	return {"damage": damage, "crit": crit}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit`
Expected: PASS.

- [ ] **Step 5: Implement the battle scene**

`Scenes/battle/BattleScene.tscn` (replace placeholder):

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/battle/battle_manager.gd" id="1"]

[node name="BattleScene" type="Control"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
script = ExtResource("1")
```

Replace `Scripts/battle/battle_manager.gd`:

```gdscript
extends Control
## EarthBound-style front-view battle. One party member vs one enemy.
## All numbers come from DataRepo/GameState; win/lose returns via SceneRouter.

var _enemy: Dictionary
var _enemy_hp: int
var _member: Dictionary
var _rng := RandomNumberGenerator.new()

var _log_label: Label
var _stats_label: Label
var _menu: VBoxContainer
var _enemy_visual: ColorRect

func _ready() -> void:
	_rng.randomize()
	_enemy = DataRepo.get_enemy(SceneRouter.pending_enemy_id)
	if _enemy.is_empty():
		push_error("BattleScene: no enemy for id '%s'" % SceneRouter.pending_enemy_id)
		SceneRouter.end_battle()
		return
	_enemy_hp = int(_enemy["max_hp"])
	_member = GameState.party[0]
	_build_ui()
	_log(String(_enemy.get("battle_intro", "%s appears!" % _enemy["display_name"])))
	_set_menu_enabled(true)

func _build_ui() -> void:
	var bg := ColorRect.new()
	bg.color = Color(0.08, 0.05, 0.12)
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)

	_enemy_visual = ColorRect.new()
	_enemy_visual.color = Color(0.85, 0.25, 0.25)
	_enemy_visual.size = Vector2(120, 120)
	_enemy_visual.anchor_left = 0.5
	_enemy_visual.anchor_right = 0.5
	_enemy_visual.anchor_top = 0.25
	_enemy_visual.anchor_bottom = 0.25
	_enemy_visual.position = Vector2(-60, -60)
	add_child(_enemy_visual)

	var enemy_name := Label.new()
	enemy_name.text = String(_enemy["display_name"])
	enemy_name.anchor_left = 0.5
	enemy_name.anchor_right = 0.5
	enemy_name.anchor_top = 0.12
	enemy_name.position = Vector2(-100, 0)
	enemy_name.custom_minimum_size = Vector2(200, 0)
	enemy_name.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	add_child(enemy_name)

	_log_label = Label.new()
	_log_label.anchor_top = 0.55
	_log_label.anchor_left = 0.1
	_log_label.anchor_right = 0.9
	_log_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	add_child(_log_label)

	_stats_label = Label.new()
	_stats_label.anchor_top = 0.68
	_stats_label.anchor_left = 0.1
	add_child(_stats_label)

	_menu = VBoxContainer.new()
	_menu.anchor_top = 0.75
	_menu.anchor_left = 0.1
	_menu.anchor_right = 0.4
	add_child(_menu)
	_add_action("Bash", _on_bash)
	_add_action("Roast Line", _on_roast)
	_add_action("Item", _on_item)
	_add_action("Run", _on_run)
	_refresh_stats()

func _add_action(label: String, handler: Callable) -> void:
	var button := Button.new()
	button.text = label
	button.pressed.connect(handler)
	_menu.add_child(button)

func _refresh_stats() -> void:
	_stats_label.text = "%s  HP %d/%d  SP %d/%d" % [
		_member["display_name"], _member["hp"], _member["max_hp"],
		_member["sp"], _member["max_sp"]]

func _log(text: String) -> void:
	_log_label.text = text

func _set_menu_enabled(enabled: bool) -> void:
	for button in _menu.get_children():
		button.disabled = not enabled
	if enabled and _menu.get_child_count() > 0:
		_menu.get_child(0).grab_focus()

func _on_bash() -> void:
	_player_attack(1.0, "%s bashes!" % _member["display_name"])

func _on_roast() -> void:
	var ability: Dictionary = DataRepo.get_ability("roast_line")
	var cost := int(ability.get("sp_cost", 0))
	if int(_member["sp"]) < cost:
		_log("Not enough SP!")
		return
	_member["sp"] = int(_member["sp"]) - cost
	_player_attack(float(ability.get("power_multiplier", 1.0)),
		String(ability.get("battle_text", "")).format({"user": _member["display_name"]}))

func _on_item() -> void:
	if not GameState.use_item("lukewarm_kebab", DataRepo) \
			and not GameState.use_item("questionable_goulash", DataRepo) \
			and not GameState.use_item("absinthe_shot", DataRepo):
		_log("No usable items!")
		return
	_refresh_stats()
	_log("%s scarfs something questionable." % _member["display_name"])
	_enemy_turn()

func _on_run() -> void:
	if _rng.randf() < 0.5:
		_log("Got away safely!")
		_finish(false)
	else:
		_log("Couldn't escape!")
		_enemy_turn()

func _player_attack(multiplier: float, flavor: String) -> void:
	_set_menu_enabled(false)
	var result := DamageCalculator.compute(_member, _enemy, _rng, multiplier)
	_enemy_hp -= int(result["damage"])
	var text := "%s %d damage!" % ["SMAAAASH!!" if result["crit"] else flavor, result["damage"]]
	_log(text)
	_refresh_stats()
	if _enemy_hp <= 0:
		_win()
	else:
		_enemy_turn()

func _enemy_turn() -> void:
	_set_menu_enabled(false)
	await get_tree().create_timer(0.9).timeout
	var result := DamageCalculator.compute(_enemy, _member, _rng)
	_member["hp"] = int(_member["hp"]) - int(result["damage"])
	_log("%s attacks! %d damage!" % [_enemy["display_name"], result["damage"]])
	_refresh_stats()
	if int(_member["hp"]) <= 0:
		_lose()
	else:
		_set_menu_enabled(true)

func _win() -> void:
	await get_tree().create_timer(0.9).timeout
	var xp := int(_enemy.get("xp_reward", 0))
	var gold := int(_enemy.get("gold_reward", 0))
	var drop := ""
	if _rng.randf() < float(_enemy.get("drop_chance", 0.0)):
		drop = String(_enemy.get("item_drop", ""))
	GameState.grant_rewards(xp, gold, drop)
	var summary := "You won! +%d XP, +%d gold." % [xp, gold]
	if drop != "":
		summary += " Found: %s!" % String(DataRepo.get_item(drop).get("display_name", drop))
	_log(summary)
	_finish(true)

func _lose() -> void:
	await get_tree().create_timer(0.9).timeout
	_member["hp"] = 1
	_log("%s got wrecked... crawling back to the plaza." % _member["display_name"])
	_finish(false)

func _finish(_won: bool) -> void:
	await get_tree().create_timer(1.5).timeout
	SceneRouter.end_battle()
```

- [ ] **Step 6: Verify headless + full manual loop**

Run: `godot --headless --path . --quit` → exit 0.
Then: `godot --path . "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn"` — walk into the red square. Expected: battle screen, Bash/Roast/Item/Run all work, winning shows rewards and returns you to the plaza at the same spot, and the enemy is still gone-ish (it may re-trigger — acceptable for the slice; walk away after returning).

- [ ] **Step 7: Commit**

```bash
git add Scripts/battle/damage_calculator.gd Scripts/battle/battle_manager.gd Scenes/battle/BattleScene.tscn tests/unit/test_damage_calculator.gd
git commit -m "feat: battle — tested damage calc, full turn loop, rewards"
```

---

### Task 11: Title screen, pause menu, and main flow

**Files:**
- Modify (replace placeholders): `Scenes/main/TitleScreen.tscn`, `Scripts/ui/pause_menu.gd`
- Create: `Scripts/ui/title_screen.gd`
- Modify: `project.godot` (set main scene)

**Interfaces:**
- Consumes: `SaveSystem.has_save/load_game/save_game`, `GameState.new_game`, `SceneRouter.goto_scene`.
- Produces: boot flow — running the project lands on the title screen; New Game starts the plaza fresh; Continue restores a save; Esc in a location pauses with Resume / Save / Quit to Title.

- [ ] **Step 1: Implement TitleScreen**

`Scenes/main/TitleScreen.tscn` (replace placeholder):

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Scripts/ui/title_screen.gd" id="1"]

[node name="TitleScreen" type="Control"]
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
script = ExtResource("1")
```

`Scripts/ui/title_screen.gd`:

```gdscript
extends Control
## Title: New Game / Continue. Continue is disabled unless a valid save exists.

func _ready() -> void:
	var bg := ColorRect.new()
	bg.color = Color(0.06, 0.04, 0.1)
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)

	var vbox := VBoxContainer.new()
	vbox.anchor_left = 0.35
	vbox.anchor_right = 0.65
	vbox.anchor_top = 0.3
	vbox.anchor_bottom = 0.7
	vbox.add_theme_constant_override("separation", 16)
	add_child(vbox)

	var title := Label.new()
	title.text = "EUROBOUND"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 48)
	vbox.add_child(title)

	var subtitle := Label.new()
	subtitle.text = "One Last Round"
	subtitle.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	vbox.add_child(subtitle)

	var new_game := Button.new()
	new_game.text = "New Game"
	new_game.pressed.connect(_on_new_game)
	vbox.add_child(new_game)

	var continue_button := Button.new()
	continue_button.text = "Continue"
	continue_button.disabled = not SaveSystem.has_save()
	continue_button.pressed.connect(_on_continue)
	vbox.add_child(continue_button)

	new_game.grab_focus()

func _on_new_game() -> void:
	GameState.new_game(DataRepo)
	SceneRouter.goto_scene(GameState.current_scene_path)

func _on_continue() -> void:
	if SaveSystem.load_game(GameState):
		SceneRouter.restore_pending = true
		SceneRouter.goto_scene(GameState.current_scene_path)
```

- [ ] **Step 2: Implement PauseMenu**

Replace `Scripts/ui/pause_menu.gd`:

```gdscript
extends CanvasLayer
## Esc pauses. Resume / Save / Quit to Title. Instanced by LocationBase.

var _panel: PanelContainer
var _save_button: Button

func _ready() -> void:
	layer = 20
	process_mode = Node.PROCESS_MODE_ALWAYS
	_panel = PanelContainer.new()
	_panel.anchor_left = 0.35
	_panel.anchor_right = 0.65
	_panel.anchor_top = 0.3
	_panel.anchor_bottom = 0.7
	_panel.visible = false
	add_child(_panel)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 12)
	_panel.add_child(vbox)

	var title := Label.new()
	title.text = "PAUSED"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	vbox.add_child(title)

	var resume := Button.new()
	resume.text = "Resume"
	resume.pressed.connect(_toggle)
	vbox.add_child(resume)

	_save_button = Button.new()
	_save_button.text = "Save"
	_save_button.pressed.connect(_on_save)
	vbox.add_child(_save_button)

	var quit := Button.new()
	quit.text = "Quit to Title"
	quit.pressed.connect(_on_quit)
	vbox.add_child(quit)

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("pause"):
		_toggle()

func _toggle() -> void:
	_panel.visible = not _panel.visible
	get_tree().paused = _panel.visible
	_save_button.text = "Save"

func _on_save() -> void:
	_save_button.text = "Saved!" if SaveSystem.save_game(GameState) else "Save failed!"

func _on_quit() -> void:
	get_tree().paused = false
	SceneRouter.goto_scene("res://Scenes/main/TitleScreen.tscn")
```

- [ ] **Step 3: Set the main scene**

In `project.godot` under `[application]`, add:

```ini
run/main_scene="res://Scenes/main/TitleScreen.tscn"
```

- [ ] **Step 4: Verify headless + manual**

Run: `godot --headless --path . --quit` → exit 0.
Then run the project plain: `godot --path .` — Expected: title screen; New Game → plaza; Esc → pause; Save → "Saved!"; Quit to Title → Continue now enabled; Continue → back in the plaza at your saved position.

- [ ] **Step 5: Commit**

```bash
git add Scenes/main/TitleScreen.tscn Scripts/ui/title_screen.gd Scripts/ui/pause_menu.gd project.godot
git commit -m "feat: title screen, pause menu, save/continue flow"
```

---

### Task 12: End-to-end verification

**Files:**
- Create: `docs/superpowers/playtest-checklist.md`

**Interfaces:**
- Consumes: everything.
- Produces: a repo-tracked manual checklist and a verified, committed slice.

- [ ] **Step 1: Run the full automated suite one final time**

```bash
python Tools/validate_data.py
godot --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests -ginclude_subdirs -gexit
godot --headless --path . --quit
```

Expected: validator OK ×7, all GUT tests pass, clean boot.

- [ ] **Step 2: Write the playtest checklist**

`docs/superpowers/playtest-checklist.md`:

```markdown
# Vertical Slice Playtest Checklist

Run `godot --path .` and verify each item. Re-run after any change to core systems.

## Boot & Title
- [ ] Project opens to the title screen, no errors in console
- [ ] Continue is greyed out when no save exists (delete `%APPDATA%\Godot\app_userdata\Eurobound\saves\slot1.json` to test)
- [ ] New Game starts in Clocktower Plaza

## Overworld
- [ ] WASD and arrow keys both move Lord Pilsner
- [ ] All four plaza edges block movement
- [ ] The camera follows the player

## Dialogue (blue rectangle = Vlad)
- [ ] E near Vlad opens dialogue; player cannot move while it is open
- [ ] Text types out; pressing E mid-type completes it instantly
- [ ] "[Show NFT Screenshot]" option is HIDDEN (you lack the item)
- [ ] Choosing options walks to follow-up nodes; the tree ends cleanly
- [ ] After closing, movement works again

## Battle (red square = Feral Segway Tourist)
- [ ] Touching it opens the battle screen
- [ ] Bash deals damage and the enemy hits back
- [ ] Roast Line costs 4 SP; refuses when SP is too low
- [ ] Item heals (after winning once, you carry a Lukewarm Kebab)
- [ ] Run sometimes flees, sometimes fails
- [ ] Winning shows XP/gold/drop and returns you to your plaza position
- [ ] Losing returns you with 1 HP (no crash)

## Save / Load
- [ ] Esc pauses; Resume unpauses
- [ ] Save shows "Saved!"; Quit to Title enables Continue
- [ ] Continue restores position, HP/SP/XP, gold, inventory, and flags
- [ ] Quit the app entirely, relaunch, Continue still works

## Data integrity
- [ ] `python Tools/validate_data.py` exits clean
- [ ] Breaking a JSON file on purpose makes the game fail LOUDLY at boot (then revert)
```

- [ ] **Step 3: Execute the checklist manually**

Run through every item. Fix anything that fails before proceeding (use superpowers:systematic-debugging for any failure). This step is done only when every box checks.

- [ ] **Step 4: Final commit**

```bash
git add docs/superpowers/playtest-checklist.md
git commit -m "feat: vertical slice complete — playtest checklist verified"
```

---

## Self-Review Notes

- **Spec coverage:** title screen (T11), one location (T7), walk (T6), NPC dialogue with flags + item-gated options (T8), visible enemy → battle (T9), battle with Bash/skill/item/run + rewards (T10), save/reload (T4, T11), data-driven content with loud failures (T1, T2), placeholder art only (global), GUT tests for damage/data/save round-trip (T2–T4, T8, T10), manual checklist (T12). Loss handling: respawn at 1 HP (T10) per spec.
- **Known simplification:** defeated overworld enemies respawn on scene re-entry and can re-trigger immediately after a battle; acceptable per spec scope (persistent enemy defeat state is a post-slice feature). Walk away after returning.
- **Type consistency check:** `DataRepo` getters return `Dictionary`; `GameState.use_item(id, repo)` signature matches battle usage; `SceneRouter.restore_pending` consumed by `LocationBase._ready()` and set by `end_battle()`/`_on_continue()`; `DialogueRunner.choose(option: Dictionary)` (not an index) matches DialogueBox usage.
