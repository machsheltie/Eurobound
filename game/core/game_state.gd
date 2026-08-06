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

## Bumped whenever the save schema changes shape in a way older saves can't satisfy.
## Author ruling, 2026-08-06: an incompatible save is rejected cleanly, never migrated
## and never crashed on. Bumped here because the SP -> Bravado rename means a
## pre-rename save holds "sp"/"max_sp" party member keys; loading it would make
## battle_manager.gd crash indexing a "bravado" key that save never wrote.
const SAVE_VERSION := 2

const BRAVADO_LOW_PCT := 0.25
const BRAVADO_MID_PCT := 0.70

## Returns the Bravado band for a value against a given max: "zero", "low", "mid",
## or "high". Bands are percent-of-max, not absolute (author ruling, 2026-08-06) —
## max_bravado varies per party member (Lord Pilsner's is 12, not the 100 an
## absolute band would assume), so the band has to scale with the character's own
## max, not a fixed number.
## Zero Bravado means Bravado cannot be spent. It does NOT cause collapse or
## forced retreat — that belongs to HP reaching zero.
func bravado_state(value: int, max_value: int) -> String:
	if max_value <= 0:
		return "zero"
	if value <= 0:
		return "zero"
	var pct := float(value) / float(max_value)
	if pct <= BRAVADO_LOW_PCT:
		return "low"
	if pct <= BRAVADO_MID_PCT:
		return "mid"
	return "high"

## Ultimates are locked out in the zero and low bands.
func can_use_ultimate(value: int, max_value: int) -> bool:
	var state := bravado_state(value, max_value)
	return state == "mid" or state == "high"

func new_game(repo) -> void:
	party = []
	inventory = {}
	gold = 20
	flags = {}
	current_scene_path = "res://worlds/debaucheryville/clocktower_plaza.tscn"
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
		"bravado": int(data.get("max_bravado", 0)),
		"max_bravado": int(data.get("max_bravado", 0)),
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
	member["bravado"] = mini(int(member["max_bravado"]), int(member["bravado"]) + int(item.get("heal_bravado", 0)))
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
		"save_version": SAVE_VERSION,
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
