class_name StatusTable
extends RefCounted
## Read side of assets/data/skills/status_effects.json (Eurobound-984j; shape approved on Production
## Desk Eurobound-1m4-q1, docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md).
## Every live number is null until the balancing pass. Null means "not tuned yet": it adds nothing,
## rolls nothing and cures nothing. No default is ever invented here.
## Stat key "all" is ruled-open (spec section 8 Q1), so it is deliberately a no-op.

const PATH := "res://assets/data/skills/status_effects.json"
## Only these stat keys are read. "all" is ignored on purpose.
const STAT_KEYS := ["offense", "defense", "speed", "luck", "grit", "charm"]

static var _cache: Dictionary = {}
static var _loaded := false


## All entries, id -> entry. Loads the file once; a missing or broken file is an empty table.
static func entries() -> Dictionary:
	if not _loaded:
		_loaded = true
		_cache = {}
		if FileAccess.file_exists(PATH):
			var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(PATH))
			if parsed is Dictionary:
				_cache = Dictionary(parsed).get("status_effects", {})
	return _cache


## Tests: swap in fixture entries (id -> entry). Call reset() afterwards.
static func set_entries(table: Dictionary) -> void:
	_cache = table
	_loaded = true


static func reset() -> void:
	_cache = {}
	_loaded = false


static func entry(id: String) -> Dictionary:
	return Dictionary(entries().get(id, {}))


static func has_entry(id: String) -> bool:
	return entries().has(id)


## The table's display name, or "" when the entry has none (callers fall back to the id).
static func display_name(id: String) -> String:
	var n: Variant = entry(id).get("display_name", null)
	return n if n is String else ""


## True when the status carries a battle counter in the table (scope includes "battle").
static func in_battle(id: String) -> bool:
	var scope: Variant = entry(id).get("scope", null)
	return scope is Array and Array(scope).has("battle")


## Id of a live status that suppresses `id`, or "".
static func suppressor_of(id: String, statuses: Dictionary) -> String:
	for other in statuses.keys():
		for rule in Array(entry(String(other)).get("interactions", [])):
			if rule is Dictionary and String(rule.get("rule", "")) == "suppress" and String(rule.get("with", "")) == id:
				return String(other)
	return ""


static func _num(v: Variant) -> bool:
	return v is int or v is float


## Sum of the non-null deltas for `stat` over every live, unsuppressed status.
static func stat_delta(statuses: Dictionary, stat: String) -> int:
	if not STAT_KEYS.has(stat):
		return 0
	var total := 0
	for id in statuses.keys():
		if suppressor_of(String(id), statuses) != "":
			continue
		var v: Variant = Dictionary(entry(String(id)).get("stats", {})).get(stat, null)
		if _num(v):
			total += int(v)
	return total


## Accuracy steps (added to the hit roll's steps) from the table; null entries add 0.
static func accuracy_steps(statuses: Dictionary) -> int:
	var total := 0
	for id in statuses.keys():
		if suppressor_of(String(id), statuses) != "":
			continue
		var v: Variant = entry(String(id)).get("accuracy_steps", null)
		if _num(v):
			total += int(v)
	return total


## Chances (0-1) to lose the turn, one per live status that has a number.
static func skip_chances(statuses: Dictionary) -> Array:
	var out := []
	for id in statuses.keys():
		if suppressor_of(String(id), statuses) != "":
			continue
		var v: Variant = entry(String(id)).get("skip_turn_chance", null)
		if _num(v):
			out.append({"id": String(id), "chance": float(v)})
	return out


## Bravado change at the start of the bearer's turn (negative drains); null adds 0.
static func bravado_per_turn(statuses: Dictionary) -> int:
	var total := 0
	for id in statuses.keys():
		if suppressor_of(String(id), statuses) != "":
			continue
		var v: Variant = Dictionary(entry(String(id)).get("bravado_tick", {})).get("battle_per_turn", null)
		if _num(v):
			total += int(v)
	return total


## What applying `id` over a live status cancels: {"cancels": existing, "into": new} or {}
## (no rule, or the rule's "into" is still null, which is inert).
static func cancel_into(id: String, statuses: Dictionary) -> Dictionary:
	for rule in Array(entry(id).get("interactions", [])):
		if rule is Dictionary and String(rule.get("rule", "")) == "cancel_into" and statuses.has(String(rule.get("with", ""))):
			var into: Variant = rule.get("into", null)
			if into is String and not String(into).is_empty():
				return {"cancels": String(rule["with"]), "into": String(into)}
	return {}


## True when `item` (a consumables.json row) cures status `id` by kind. A "drink" cure also takes an
## alcoholic item (spec cured_by.1 PROPOSED reading). "rest" cures belong to the rest-scene bead.
static func cured_by_item(id: String, item_id: String, item: Dictionary) -> bool:
	for c in Array(entry(id).get("cured_by", [])):
		if not (c is Dictionary):
			continue
		var value: Variant = c.get("value", null)
		if not (value is String):
			continue
		match String(c.get("kind", "")):
			"item_id":
				if String(value) == item_id:
					return true
			"item_subtype":
				if String(item.get("subtype", "")) == String(value):
					return true
				if String(value) == "drink" and bool(item.get("alcohol", false)):
					return true
	return false
