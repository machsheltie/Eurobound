class_name QuestData
extends RefCounted
## Reads the quest files in assets/data/quests/ (canonical quest schema, validate_data.py
## check_quest) into the shape the Quest Log registry uses (quest_log.gd). Eurobound-zkhb.
##
## Field map, nothing derived beyond it:
##   quest_id, display_name          <- the same top-level keys
##   started_when                    <- quest_flags.on_start
##   completed_when                  <- quest_flags.on_complete plus every on_complete_<path> list
##   steps[] {id, objective, done_when} <- quest_stages[] {name, objective, done_when}
## A stage's "objective" is the Writers' Room's line and may be absent (the log then shows the
## humanised stage name). Everything else is required. The loader NEVER fills a gap: a quest
## missing a required field is left out of the log and listed under "incomplete" with the
## fields it lacks.

const DIR := "res://assets/data/quests"

static var _cache: Dictionary = {}


static func _strings(v) -> Array:
	var out: Array = []
	if v is Array:
		for x in v:
			if x is String and x != "" and not out.has(x):
				out.append(x)
	return out


## {"entry": <Quest Log quest, {} if anything is missing>, "missing": [field paths]}.
static func to_log_entry(doc: Dictionary) -> Dictionary:
	var missing: Array = []
	var quest_id := String(doc.get("quest_id", ""))
	var display_name := String(doc.get("display_name", ""))
	if quest_id == "":
		missing.append("quest_id")
	if display_name == "":
		missing.append("display_name")
	# "groups", not "flags": validate_data.py tier 3 reads flags.get("x") as a flag id.
	var groups = doc.get("quest_flags", {})
	if not groups is Dictionary:
		groups = {}
	var started := _strings(groups.get("on_start", []))
	if started.is_empty():
		missing.append("quest_flags.on_start")
	var completed: Array = []
	for key in groups:
		if String(key) == "on_complete" or String(key).begins_with("on_complete_"):
			for f in _strings(groups[key]):
				if not completed.has(f):
					completed.append(f)
	if completed.is_empty():
		missing.append("quest_flags.on_complete*")
	var steps: Array = []
	var stages = doc.get("quest_stages", [])
	if not stages is Array or stages.is_empty():
		missing.append("quest_stages")
	else:
		for stage in stages:
			if not stage is Dictionary:
				missing.append("quest_stages[?].name")
				continue
			var step_name := String(stage.get("name", ""))
			var ref := step_name if step_name != "" else _stage_ref(stage)
			if step_name == "":
				missing.append("quest_stages[%s].name" % ref)
			var done := _strings(stage.get("done_when", []))
			if done.is_empty() and step_name != "":
				missing.append("quest_stages[%s].done_when" % ref)
			steps.append({"id": step_name, "objective": String(stage.get("objective", "")), "done_when": done})
	if not missing.is_empty():
		return {"entry": {}, "missing": missing}
	return {"entry": {"quest_id": quest_id, "display_name": display_name, "started_when": started,
		"completed_when": completed, "steps": steps}, "missing": []}


## stage_id is an int in JSON (parsed as a float) or a string such as "6a".
static func _stage_ref(stage: Dictionary) -> String:
	var id = stage.get("stage_id", "?")
	return str(int(id)) if id is float else str(id)


## {"quests": [Quest Log quests], "incomplete": [{"file", "quest_id", "missing"}]}, file-name order.
static func load_dir(dir: String = DIR) -> Dictionary:
	if dir == DIR and not _cache.is_empty():
		return _cache
	var out := {"quests": [], "incomplete": []}
	if not DirAccess.dir_exists_absolute(dir):
		return out
	var files := Array(DirAccess.get_files_at(dir)).filter(func(f): return String(f).ends_with(".json"))
	files.sort()
	for file in files:
		var doc = JSON.parse_string(FileAccess.get_file_as_string(dir + "/" + file))
		if not doc is Dictionary:
			out["incomplete"].append({"file": file, "quest_id": "", "missing": ["valid JSON object"]})
			continue
		var r := to_log_entry(doc)
		if r["missing"].is_empty():
			out["quests"].append(r["entry"])
		else:
			out["incomplete"].append({"file": file, "quest_id": String(doc.get("quest_id", "")),
				"missing": r["missing"]})
	if dir == DIR:
		_cache = out
		for line in report(out["incomplete"]):
			push_warning("QuestData: not in the Quest Log: " + line)
	return out


## One plain line per incomplete quest, for logs and tools.
static func report(incomplete: Array) -> Array:
	var lines: Array = []
	for row in incomplete:
		lines.append("%s (%s): missing %s" % [row["file"], row["quest_id"], ", ".join(row["missing"])])
	return lines
