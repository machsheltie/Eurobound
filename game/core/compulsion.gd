class_name Compulsion
extends RefCounted
## Read side of field.compulsion in assets/data/skills/status_effects.json (Eurobound-fe10; spec
## docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md section 6). The runners
## themselves live in PlayerController; this class only says which compulsions are live and fully
## specified. Intoxication law sections 3 and 7: a compulsion is a bounded loss of control, so it
## needs an interval AND a length AND input_lock true. Any null (not ruled yet) means it never fires.
## No number is invented here and no behaviour beyond the two the data names.

const KIND_CLEAN := "clean_nearest_interactable"
const KIND_STARE := "stare"
const KINDS := [KIND_CLEAN, KIND_STARE]
const UNIT_STEPS := "steps"
const UNIT_REAL_SECONDS := "real_seconds"


## Fully specified compulsions of the live, unsuppressed field statuses on `member_id`:
## [{"id", "kind", "amount", "unit", "lasts"}]. A null or invalid number leaves the status out.
static func specs(state, member_id: String) -> Array:
	var out := []
	var live := {}
	for id in FieldStatus.list(state, member_id):
		live[id] = true
	for id in live.keys():
		if StatusTable.suppressor_of(String(id), live) != "":
			continue
		var spec := parse(String(id))
		if not spec.is_empty():
			out.append(spec)
	return out


## One status's compulsion as a spec, or {} when it has none or any part is null/invalid.
static func parse(status_id: String) -> Dictionary:
	var field: Variant = StatusTable.entry(status_id).get("field", null)
	if not (field is Dictionary):
		return {}
	var c: Variant = Dictionary(field).get("compulsion", null)
	if not (c is Dictionary):
		return {}
	var kind: Variant = Dictionary(c).get("kind", null)
	var every: Variant = Dictionary(c).get("every", null)
	var lasts: Variant = Dictionary(c).get("lasts_seconds", null)
	if not (kind is String) or not KINDS.has(String(kind)) or not (every is Dictionary):
		return {}
	var amount: Variant = Dictionary(every).get("amount", null)
	var unit: Variant = Dictionary(every).get("unit", null)
	if not (amount is int or amount is float) or float(amount) <= 0.0:
		return {}
	if not (unit is String) or not [UNIT_STEPS, UNIT_REAL_SECONDS].has(String(unit)):
		return {}
	if not (lasts is int or lasts is float) or float(lasts) <= 0.0:
		return {}
	if Dictionary(c).get("input_lock", null) != true:
		return {}
	return {"id": status_id, "kind": String(kind), "amount": float(amount), "unit": String(unit), "lasts": float(lasts)}
