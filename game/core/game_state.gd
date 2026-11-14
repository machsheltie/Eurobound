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
## Where the leader stood when the game was saved: {"x", "y", "z", "facing"} in the screen's own
## space (SaveSystem.capture_location). Empty = the screen's default spawn point.
var player_spot: Dictionary = {}

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
	player_spot = {}
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

## `rng` is optional (tests pass a seeded one). Item hook "self_status_risk" ({status, chance}):
## the drinker may take Green Fairy Confusion (Absinthe Lager, 30%), and drank_<id> is set.
func use_item(id: String, repo, rng: RandomNumberGenerator = null) -> bool:
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
	var risk: Variant = item.get("self_status_risk", null)
	if risk is Dictionary:
		flags["drank_" + id] = true
		if rng == null:
			rng = RandomNumberGenerator.new()
			rng.randomize()
		if String(risk.get("status", "")) == FieldStatus.GREEN_FAIRY_CONFUSION \
				and rng.randf() < float(risk.get("chance", 0.0)):
			FieldStatus.apply_confusion(self, String(member.get("id", "")), rng)
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
# The non-SOVS coin store is below (Phase 0b).

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

# --- Non-SOVS coin store (economy Phase 0b, Eurobound-1g9t) ---
# Author ruling on Eurobound-cyb6 (2026-11-13): "Dictionary: coin_id -> quantity held".
# Held in flags under the registry key, like economy_seed, so it saves with them
# (quest_flags.json; design/economy/economy_system.md §8.2). Quantities only: these
# coins are not SOVS and this store sets no price on them.

## Registry key in quest_flags.json (§8.2). Absent means the registry default, {}.
const BAGHOLDER_ASSETS_FLAG := "bagholder_assets"

## Every non-SOVS coin held, coin_id -> quantity. A copy: change holdings with deposit_coin.
func bagholder_assets() -> Dictionary:
	var held: Variant = flags.get(BAGHOLDER_ASSETS_FLAG, null)
	if held is Dictionary:
		return held.duplicate()
	return {}

func coin_quantity(coin_id: String) -> int:
	var held: Variant = flags.get(BAGHOLDER_ASSETS_FLAG, null)
	if held is Dictionary:
		return int(held.get(coin_id, 0))
	return 0

## Adds `amount` of `coin_id` to the holdings. An empty id or an amount of 0 or less
## changes nothing (same guard as grant_sovs).
func deposit_coin(coin_id: String, amount: int) -> void:
	if coin_id == "" or amount <= 0:
		return
	var held: Dictionary = bagholder_assets()
	held[coin_id] = int(held.get(coin_id, 0)) + amount
	flags[BAGHOLDER_ASSETS_FLAG] = held

## On load: JSON hands quantities back as floats, so they are made ints again. A store
## that is not a Dictionary is dropped (back to the default {}); so is any entry
## with an empty id or a quantity of 0 or less.
func _normalize_bagholder_assets() -> void:
	if not flags.has(BAGHOLDER_ASSETS_FLAG):
		return
	var raw: Variant = flags[BAGHOLDER_ASSETS_FLAG]
	if not (raw is Dictionary):
		flags.erase(BAGHOLDER_ASSETS_FLAG)
		return
	var held := {}
	for coin_id in raw:
		var quantity: Variant = raw[coin_id]
		if String(coin_id) != "" and (quantity is int or quantity is float) and int(quantity) > 0:
			held[String(coin_id)] = int(quantity)
	flags[BAGHOLDER_ASSETS_FLAG] = held

func to_dict() -> Dictionary:
	return {
		"save_version": SAVE_VERSION,
		"party": party.duplicate(true),
		"inventory": inventory.duplicate(true),
		"sovs": sovs,
		"flags": flags.duplicate(true),
		"current_scene_path": current_scene_path,
		"player_position": {"x": player_position.x, "y": player_position.y},
		"player_spot": player_spot.duplicate(true),
	}

## Party member numbers that are whole by definition. JSON has one number type, so a save
## hands them back as floats; from_dict makes them ints again.
const PARTY_INT_KEYS := ["level", "xp", "hp", "max_hp", "bravado", "max_bravado", "offense",
		"defense", "speed", "charm", "luck", "grit"]
## Flags that hold a whole number, made ints again on load for the same reason. "clock.minutes"
## is GameClock.KEY (written out here so this file does not depend on GameClock loading first).
const INT_FLAGS := ["clock.minutes", ECONOMY_SEED_FLAG]

## Takes a deep copy: the state never shares containers with the dictionary it was loaded from.
func from_dict(d: Dictionary) -> void:
	party = []
	var raw_party: Variant = d.get("party", [])
	if raw_party is Array:
		for raw in raw_party:
			if not (raw is Dictionary):
				continue
			var member: Dictionary = raw.duplicate(true)
			for key in PARTY_INT_KEYS:
				if member.get(key) is float:
					member[key] = int(member[key])
			party.append(member)
	inventory = {}
	var raw_inventory: Variant = d.get("inventory", {})
	if raw_inventory is Dictionary:
		for id in raw_inventory:
			inventory[String(id)] = int(raw_inventory[id])
	# Saves written before the SOVS rename stored the wallet under the legacy key "gold".
	# Same schema otherwise, so they load (SAVE_VERSION unchanged).
	sovs = int(d.get("sovs", d.get("gold", 0)))
	var raw_flags: Variant = d.get("flags", {})
	flags = raw_flags.duplicate(true) if raw_flags is Dictionary else {}
	_ensure_economy_seed()
	_normalize_bagholder_assets()
	for key in INT_FLAGS:
		if flags.get(key) is float:
			flags[key] = int(flags[key])
	current_scene_path = String(d.get("current_scene_path", ""))
	var pos: Dictionary = d.get("player_position", {"x": 0, "y": 0})
	player_position = Vector2(float(pos.get("x", 0)), float(pos.get("y", 0)))
	# A save from before the spot existed has none: the screen's default spawn is used.
	player_spot = {}
	var spot: Variant = d.get("player_spot", {})
	if spot is Dictionary and not spot.is_empty():
		player_spot = {
			"x": float(spot.get("x", 0.0)),
			"y": float(spot.get("y", 0.0)),
			"z": float(spot.get("z", 0.0)),
			"facing": String(spot.get("facing", "south")),
		}
