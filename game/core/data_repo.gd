extends Node
## Loads all game data JSON at startup. The ONLY module that touches Assets/Data.
## Content is never hardcoded elsewhere; unknown IDs fail loud.

const DATA_ROOT := "res://assets/data/"

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
