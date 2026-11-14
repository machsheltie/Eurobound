class_name StatusTable
extends RefCounted
## Read side of assets/data/skills/status_effects.json (Eurobound-984j; shape approved on Production
## Desk Eurobound-1m4-q1, docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md).
## Every live number is null until the balancing pass. Null means "not tuned yet": it adds nothing,
## rolls nothing and cures nothing. No default is ever invented here.
## Stat key "all" is the six combat stats (author, Eurobound Desk 64vo-q1: "The six combat stats:
## offense, defense, speed, charm, luck, grit"). It never reaches max HP, max Bravado or accuracy.

const PATH := "res://assets/data/skills/status_effects.json"
## The stat keys that are read, and exactly what "all" covers (64vo-q1).
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


## True when the status exists only in battle (scope has "battle" and not "field"). Author,
## Eurobound Desk 64vo-q2, on Crash: "Battle only: Crash waits for the next fight and runs its
## turns there".
static func battle_only(id: String) -> bool:
	var scope: Variant = entry(id).get("scope", null)
	return scope is Array and Array(scope).has("battle") and not Array(scope).has("field")


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
		var stats := Dictionary(entry(String(id)).get("stats", {}))
		for key in [stat, "all"]:
			var v: Variant = stats.get(key, null)
			if _num(v):
				total += int(v)
	return total


## True when a live status hides `id` and the hiding rule says the hidden timer stops
## ("timer": "pause"). Author, Eurobound Desk 64vo-q6, on Hungover under Sugar Rush Hour or
## Gush-Locked: "Pause: the timer stops while hidden and picks up again when it returns".
static func timer_paused(id: String, statuses: Dictionary) -> bool:
	for other in statuses.keys():
		for rule in Array(entry(String(other)).get("interactions", [])):
			if rule is Dictionary and String(rule.get("rule", "")) == "suppress" and String(rule.get("with", "")) == id 					and rule.get("timer", null) is String and String(rule["timer"]) == "pause":
				return true
	return false


## True when a live, unsuppressed status locks `skill` (a party_abilities.json row):
##  - "bravado_cost_skills": every skill that costs Bravado (what Embarrassed does in code).
##  - "spoken_bravado_skills": Bravado skills tagged "spoken": true. Abilities are tagged one by one
##    as they are written (author, Eurobound Desk 64vo-q5); an untagged skill is not locked.
static func locks_skill(statuses: Dictionary, skill: Dictionary) -> bool:
	if int(skill.get("bravado_cost", 0)) <= 0:
		return false
	for id in statuses.keys():
		if suppressor_of(String(id), statuses) != "":
			continue
		var locks: Variant = entry(String(id)).get("locks", null)
		if not (locks is Array):
			continue
		if Array(locks).has("bravado_cost_skills"):
			return true
		if Array(locks).has("spoken_bravado_skills") and skill.get("spoken", false) == true:
			return true
	return false


## How many times a follow-up's default length counts for `count` stacks: once per stack under
## stack_rule "extend" (64vo-q3: "Stacks last longer: more Crash turns per stack"), else once.
static func then_length_mult(id: String, count: int) -> int:
	var rule: Variant = entry(id).get("stack_rule", null)
	return maxi(count, 1) if rule is String and String(rule) == "extend" else 1


## How many times over a follow-up's stacks arrive when `ending` runs out with `statuses` live on
## the same bro: 2 when `ending` has a "modify_then" rule for `then_id` with effect "double_stacks"
## and the rule's "with" status is live, else 1 (author, Eurobound Desk 64vo-q4, on Gush-Locked over
## a hangover: "Double the stacks: Cottonmouth arrives with twice as many stacks").
static func then_stack_mult(ending: String, then_id: String, statuses: Dictionary) -> int:
	for rule in Array(entry(ending).get("interactions", [])):
		if not (rule is Dictionary) or String(rule.get("rule", "")) != "modify_then":
			continue
		if not (rule.get("then", null) is String) or String(rule["then"]) != then_id:
			continue
		if not (rule.get("effect", null) is String) or String(rule["effect"]) != "double_stacks":
			continue
		if statuses.has(String(rule.get("with", ""))):
			return 2
	return 1


## True when the status counts stacks (stack_rule "extend").
static func stacks_extend(id: String) -> bool:
	var rule: Variant = entry(id).get("stack_rule", null)
	return rule is String and String(rule) == "extend"


## True when the status lasts until cured (default_duration.until_cured).
static func until_cured(id: String) -> bool:
	return Dictionary(entry(id).get("default_duration", {})).get("until_cured", false) == true


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


## True when `item` (a consumables.json row) cures status `id` by kind. A "drink" cure takes any
## drink: subtype "drink" or an alcoholic item (author, Eurobound Desk 64vo-q8: "Any drink at all:
## water, soda, beer, liquor"). "rest" cures belong to RestEvents.
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
