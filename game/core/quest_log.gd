class_name QuestLog
extends RefCounted
## Quest Log registry (author round v42). Definitions live in assets/data/quest_log/quest_log.json;
## every state is DERIVED from GameState.flags, so there is no tracking store of its own.
## Objective text is the Writers' Room's: until a step carries an "objective" string the log shows the
## humanised step id (plain labels only).

const PATH := "res://assets/data/quest_log/quest_log.json"


static func quests() -> Array:
	if not FileAccess.file_exists(PATH):
		return []
	var d = JSON.parse_string(FileAccess.get_file_as_string(PATH))
	return d.get("quests", []) if d is Dictionary else []


static func _flag(state, id: String) -> bool:
	return bool(state.flags.get(id, false))


static func _any(state, ids: Array) -> bool:
	return ids.any(func(f): return _flag(state, String(f)))


static func _all(state, ids: Array) -> bool:
	return not ids.is_empty() and ids.all(func(f): return _flag(state, String(f)))


## "hidden" (not started), "active" or "completed".
static func status(state, quest: Dictionary) -> String:
	if _any(state, quest.get("completed_when", [])):
		return "completed"
	if _any(state, quest.get("started_when", [])):
		return "active"
	return "hidden"


## Ordered steps with their state: "done", "current" (the first undone step of an active quest) or
## "pending". A completed quest gets its matching outcome appended as a done step.
static func steps(state, quest: Dictionary) -> Array:
	var out: Array = []
	var current_set := false
	var stat := status(state, quest)
	for s in quest.get("steps", []):
		var st := "pending"
		if _any(state, s.get("done_when", [])):
			st = "done"
		elif stat == "active" and not current_set:
			st = "current"
			current_set = true
		out.append({"id": s["id"], "objective": String(s.get("objective", "")), "state": st})
	if stat == "completed":
		for o in quest.get("outcomes", []):
			if _all(state, o.get("all", [])):
				out.append({"id": o["id"], "objective": String(o.get("objective", "")), "state": "done"})
				break
	return out


## The step the log shows beside the quest name: the current one, else the last (the outcome).
static func current_step(state, quest: Dictionary) -> Dictionary:
	var rows := steps(state, quest)
	for r in rows:
		if r["state"] == "current":
			return r
	return rows.back() if not rows.is_empty() else {}


## Quests in the given status ("active" / "completed"), registry order.
static func listing(state, wanted: String) -> Array:
	return quests().filter(func(q): return status(state, q) == wanted)


static func label(step: Dictionary) -> String:
	var text := String(step.get("objective", ""))
	return text if text != "" else String(step.get("id", "")).replace("_", " ").capitalize()
