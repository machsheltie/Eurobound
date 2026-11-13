extends Node
## Single source of truth for run-time game state. What SaveSystem serializes.
## Holds no behavior about HOW scenes change (SceneRouter) or WHERE data
## comes from (DataRepo is passed in where needed, keeping this testable).

var party: Array = []
var inventory: Dictionary = {}
var sovs: int = 0
var flags: Dictionary = {}
var current_scene_path: String = ""
var player_position: Vector2 = Vector2.ZERO

## Bumped whenever the save schema changes shape in a way older saves can't satisfy.
## Author ruling, 2026-08-06: an incompatible save is rejected cleanly, never migrated
## and never crashed on. Bumped here because the SP -> Bravado rename means a
## pre-rename save holds "sp"/"max_sp" party member keys; loading it would make
## battle_manager.gd crash indexing a "bravado" key that save never wrote.
const SAVE_VERSION := 2

## Returns the Bravado band for a value against a given max: "zero", "low", "mid", or "high".
## Bands are percent-of-max (author ruling, 2026-08-06), at the round v26 thirds: Low under 1/3,
## High at 2/3 and above (ef3_bravado_tiers), applied game-wide (ef4_bravado_bands_game_wide,
## 2026-11-11). BattleRules.tier is the single source.
## Zero Bravado means Bravado cannot be spent. It does NOT cause collapse or
## forced retreat — that belongs to HP reaching zero.
func bravado_state(value: int, max_value: int) -> String:
	if max_value <= 0 or value <= 0:
		return "zero"
	return BattleRules.tier(value, max_value)

## Ultimates are locked out in the zero and low bands.
func can_use_ultimate(value: int, max_value: int) -> bool:
	var state := bravado_state(value, max_value)
	return state == "mid" or state == "high"

func new_game(repo) -> void:
	party = []
	inventory = {}
	sovs = 20
	flags = {}
	_ensure_economy_seed()
	current_scene_path = "res://worlds/debaucheryville/clocktower_plaza.tscn"
	player_position = Vector2.ZERO
	# The three bros travel together from the start (Synopsis); Chadwick's and Bradley's
	# numbers were approved in round v26 (ef3_party_stats).
	for id in ["lord_pilsner", "chadwick", "bradley"]:
		_add_party_member(id, repo)

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

## `max_stack` (consumables.json, Eurobound-umy): the cap on copies carried. null = no cap.
func add_item(id: String, count: int = 1, max_stack: Variant = null) -> void:
	var total := int(inventory.get(id, 0)) + count
	if max_stack is int or max_stack is float:
		total = mini(total, int(max_stack))
	inventory[id] = total

func use_item(id: String, repo) -> bool:
	if int(inventory.get(id, 0)) <= 0:
		return false
	var item: Dictionary = repo.get_item(id)
	if item.is_empty() or party.is_empty():
		return false
	if not Intoxicant.usable_in(item, Intoxicant.CTX_FIELD):
		return false
	var member: Dictionary = party[0]
	FieldStatus.cure_by_item(self, String(member.get("id", "")), id, item)
	Intoxicant.apply_field(self, String(member.get("id", "")), item)
	NavigationRoll.note_item_used(self, item)  # an alcohol: true drink ends Sober
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

func grant_rewards(xp: int, sovs_amount: int, item_id: String) -> void:
	if not party.is_empty():
		party[0]["xp"] = int(party[0]["xp"]) + xp
	grant_sovs(sovs_amount)
	if item_id != "":
		add_item(item_id)

# --- SOVS wallet (economy Phase 0, Eurobound-jvwg) ---
# SOVS stays boring: no fees, no pending state, no failed transactions
# (design/economy/economy_system.md §1.4). All volatility lives in the back alley.
# The non-SOVS coin store waits on the author's ruling on its shape (Eurobound-cyb6).

## Registry key in quest_flags.json (§8.2). 0 is the registry default: not generated yet.
const ECONOMY_SEED_FLAG := "economy_seed"

func can_afford(amount: int) -> bool:
	return amount >= 0 and sovs >= amount

## Takes `amount` SOVS. Refuses (returns false, takes nothing) when funds are short.
func spend_sovs(amount: int) -> bool:
	if not can_afford(amount):
		return false
	sovs -= amount
	return true

func grant_sovs(amount: int) -> void:
	if amount > 0:
		sovs += amount

## The one SOVS purchase path (§8.4): select, pay, done. No fee, no pending state,
## no failure return. The caller checks can_afford first and shows its own
## cannot-afford notice; called without the funds, this changes nothing.
func purchase_sovs(item_id: String, price: int, count: int = 1, max_stack: Variant = null) -> void:
	if not spend_sovs(price):
		push_warning("purchase_sovs(%s): caller skipped can_afford" % item_id)
		return
	add_item(item_id, count, max_stack)

## Layer A root (§8.1): generated once, saved in flags, never regenerated or shown to players.
func economy_seed() -> int:
	return int(flags.get(ECONOMY_SEED_FLAG, 0))

## Rolls the seed only when absent: at new game, or on loading a save made before it existed.
func _ensure_economy_seed() -> void:
	if economy_seed() != 0:
		return
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	var value := 0
	while value == 0:
		value = int(rng.randi())
	flags[ECONOMY_SEED_FLAG] = value

func to_dict() -> Dictionary:
	return {
		"save_version": SAVE_VERSION,
		"party": party.duplicate(true),
		"inventory": inventory.duplicate(true),
		"sovs": sovs,
		"flags": flags.duplicate(true),
		"current_scene_path": current_scene_path,
		"player_position": {"x": player_position.x, "y": player_position.y},
	}

func from_dict(d: Dictionary) -> void:
	party = d.get("party", [])
	inventory = d.get("inventory", {})
	# Saves written before the SOVS rename stored the wallet under the legacy key "gold".
	# Same schema otherwise, so they load (SAVE_VERSION unchanged).
	sovs = int(d.get("sovs", d.get("gold", 0)))
	flags = d.get("flags", {})
	_ensure_economy_seed()
	current_scene_path = d.get("current_scene_path", "")
	var pos: Dictionary = d.get("player_position", {"x": 0, "y": 0})
	player_position = Vector2(float(pos.get("x", 0)), float(pos.get("y", 0)))
