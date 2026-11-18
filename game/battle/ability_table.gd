class_name AbilityTable
extends RefCounted
## Read side of the bros' moves: assets/data/skills/party_abilities.json ("abilities") and
## assets/data/skills/combos.json ("combos"). BattleCore reads counter-brags and combos from here;
## the battle screen still gets the abilities dictionary from its caller.
## A missing or broken file is an empty table. Tests swap in fixtures with set_tables().

const ABILITIES_PATH := "res://assets/data/skills/party_abilities.json"
const COMBOS_PATH := "res://assets/data/skills/combos.json"

static var _abilities: Dictionary = {}
static var _combos: Dictionary = {}
static var _loaded := false


static func _load() -> void:
	if _loaded:
		return
	_loaded = true
	_abilities = _read(ABILITIES_PATH, "abilities")
	_combos = _read(COMBOS_PATH, "combos")


static func _read(path: String, key: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return {}
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
	if not (parsed is Dictionary):
		return {}
	var table: Variant = Dictionary(parsed).get(key, {})
	return Dictionary(table) if table is Dictionary else {}


static func abilities() -> Dictionary:
	_load()
	return _abilities


static func combos() -> Dictionary:
	_load()
	return _combos


static func ability(id: String) -> Dictionary:
	var a: Variant = abilities().get(id, {})
	return Dictionary(a) if a is Dictionary else {}


static func combo(id: String) -> Dictionary:
	var c: Variant = combos().get(id, {})
	return Dictionary(c) if c is Dictionary else {}


## Tests: swap in fixture tables (id -> entry). Call reset() afterwards.
static func set_tables(abilities_: Dictionary, combos_: Dictionary) -> void:
	_abilities = abilities_
	_combos = combos_
	_loaded = true


static func reset() -> void:
	_abilities = {}
	_combos = {}
	_loaded = false
