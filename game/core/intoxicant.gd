class_name Intoxicant
extends RefCounted
## Read side of the approved consumables.json intoxicant fields (Eurobound-umy; proposal
## docs/superpowers/specs/2026-11-12-consumable-intoxicant-fields-proposal.md).
## Every null is inert: no number is invented here. An item with no duration for a scope applies
## nothing in that scope. Absent or null usable_in means usable in battle and field (proposal :64).

const CTX_BATTLE := "battle"
const CTX_FIELD := "field"
const STACK_EXTEND := "extend"
const STACK_REFRESH := "refresh"
const STACK_NONE := "none"


static func block(item: Dictionary) -> Dictionary:
	var b: Variant = item.get("intoxicant", null)
	return b if b is Dictionary else {}


static func is_intoxicant(item: Dictionary) -> bool:
	return not status_id(item).is_empty()


static func status_id(item: Dictionary) -> String:
	var s: Variant = block(item).get("status", null)
	return String(s) if s is String else ""


## "extend" / "refresh" / "none"; absent means refresh (proposal table).
static func stack_rule(item: Dictionary) -> String:
	var r: Variant = block(item).get("stack_rule", null)
	return String(r) if r is String and not String(r).is_empty() else STACK_REFRESH


static func usable_in(item: Dictionary, ctx: String) -> bool:
	var u: Variant = item.get("usable_in", null)
	return not (u is Array) or Array(u).has(ctx)


## Max copies carried, or null (not ruled, no cap).
static func max_stack(item: Dictionary) -> Variant:
	var m: Variant = item.get("max_stack", null)
	return int(m) if (m is int or m is float) and int(m) >= 1 else null


static func _num(v: Variant) -> bool:
	return v is int or v is float


## Battle turns: the item's own number, else the status table's default_duration, else null.
static func battle_turns(item: Dictionary) -> Variant:
	return _duration(item, "battle_turns")


static func field_steps(item: Dictionary) -> Variant:
	return _duration(item, "field_steps")


static func _duration(item: Dictionary, key: String) -> Variant:
	var own: Variant = Dictionary(block(item).get("duration", {})).get(key, null)
	if _num(own) and int(own) >= 1:
		return int(own)
	return table_duration(status_id(item), key)


## The status table's default for a status (used by `then` follow-ups), or null.
static func table_duration(id: String, key: String) -> Variant:
	var d: Variant = Dictionary(StatusTable.entry(id).get("default_duration", {})).get(key, null)
	return int(d) if _num(d) and int(d) >= 1 else null


## The item's ends_on_rest (true/false) or null when the item does not rule it.
static func ends_on_rest(item: Dictionary) -> Variant:
	var v: Variant = Dictionary(block(item).get("duration", {})).get("ends_on_rest", null)
	return v if v is bool else null


## {"status": id, "stacks": bool} or {} when the item has no follow-up.
static func then(item: Dictionary) -> Dictionary:
	var t: Variant = block(item).get("then", null)
	if t is Dictionary and Dictionary(t).get("status", null) is String and not String(t["status"]).is_empty():
		return {"status": String(t["status"]), "stacks": bool(Dictionary(t).get("stacks", false))}
	return {}


## Applies the item's status to a bro's FIELD rows (steps unit). Inert (false) without field steps,
## or when the stack rule is "none" and the status is already live. Returns true when it changed a row.
static func apply_field(state, target: String, item: Dictionary) -> bool:
	var sid := status_id(item)
	var steps: Variant = field_steps(item)
	if sid.is_empty() or steps == null or not usable_in(item, CTX_FIELD):
		return false
	var turns: Variant = battle_turns(item)
	var live := FieldStatus.has(state, sid, target)
	var rule := stack_rule(item)
	if live and rule == STACK_NONE:
		return false
	var row: Dictionary = {}
	if live and rule == STACK_EXTEND:
		row = _own_row(state, target, sid)
	if not row.is_empty():
		row["left"] = int(row["left"]) + int(steps)
		if turns != null:
			row["turns"] = int(row.get("turns", 0)) + int(turns)
	else:
		FieldStatus.apply_steps(state, target, sid, int(steps), int(turns) if turns != null else -1)
		row = _own_row(state, target, sid)
	var eor: Variant = ends_on_rest(item)
	if eor != null:
		row["ends_on_rest"] = eor
	var t := then(item)
	if not t.is_empty():
		var prior := int(Dictionary(row.get("then", {})).get("stacks_count", 0)) if live and rule == STACK_EXTEND else 0
		row["then"] = {"status": t["status"], "stacks_count": prior + 1 if t["stacks"] else 1}
	return true


static func _own_row(state, target: String, sid: String) -> Dictionary:
	var rows: Variant = FieldStatus._all(state).get(target, {})
	return Dictionary(rows).get(sid, {})
