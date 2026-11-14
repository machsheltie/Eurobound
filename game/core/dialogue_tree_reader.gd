class_name DialogueTreeReader
extends RefCounted
## Reads the NPC dialogue-tree JSON (assets/data/npcs/dialogue_trees/<city>_dialogue.json) into one
## plain structure, so whichever dialogue path the game standardises on (Eurobound-04t2,
## docs/superpowers/plans/2026-11-14-dialogue-consolidation-plan.md) has a single reader.
## Text is copied as written. Broken data is reported in `problems` and left as it is: no link is
## repaired and no line, start node or default is filled in. Wired to no UI and no autoload.
##
## read_doc / read_file return {"trees": {npc_id: tree}, "problems": [String]}.
##   tree   = {"npc_id", "start", "nodes": {node_id: node}, "status_lines", "world_state_lines"}
##   node   = {"id", "line_id", "speaker", "text", "options": [option], "extra"}
##   option = {"text", "next", "requires", "extra"}
## `start` is START_NODE, or "" when the tree has no such node. `extra` holds every field this
## reader does not name (emotion, set_flags, party_reaction, ...), untouched.

const START_NODE := "default_greeting"
const NODE_FIELDS := ["line_id", "speaker", "text", "options"]
const OPTION_FIELDS := ["text", "leads_to", "requires"]


static func read_file(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return {"trees": {}, "problems": ["%s: file not found" % path]}
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
	if not (parsed is Dictionary):
		return {"trees": {}, "problems": ["%s: not a JSON object" % path]}
	return read_doc(parsed)


static func read_doc(doc: Dictionary) -> Dictionary:
	var trees := {}
	var problems: Array = []
	var raw_trees: Variant = doc.get("dialogue_trees", {})
	if not (raw_trees is Dictionary):
		return {"trees": {}, "problems": ["dialogue_trees is not an object"]}
	for npc_id: String in raw_trees:
		var raw_tree: Variant = raw_trees[npc_id]
		if not (raw_tree is Dictionary):
			problems.append("%s: tree is not an object" % npc_id)
			continue
		trees[npc_id] = _tree(npc_id, raw_tree, doc, problems)
	return {"trees": trees, "problems": problems}


static func _tree(npc_id: String, raw_tree: Dictionary, doc: Dictionary, problems: Array) -> Dictionary:
	var nodes := {}
	for node_id: String in raw_tree:
		var raw_node: Variant = raw_tree[node_id]
		if not (raw_node is Dictionary):
			problems.append("%s/%s: node is not an object" % [npc_id, node_id])
			continue
		nodes[node_id] = _node(node_id, raw_node)
	if not nodes.has(START_NODE):
		problems.append("%s: no %s node, so the tree has no start" % [npc_id, START_NODE])
	for node_id: String in nodes:
		var node: Dictionary = nodes[node_id]
		if node["text"] == "":
			problems.append("%s/%s: no text" % [npc_id, node_id])
		for i: int in node["options"].size():
			var next: String = node["options"][i]["next"]
			if not nodes.has(next):
				problems.append("%s/%s: option %d leads to '%s', which does not exist"
					% [npc_id, node_id, i + 1, next])
	return {
		"npc_id": npc_id,
		"start": START_NODE if nodes.has(START_NODE) else "",
		"nodes": nodes,
		"status_lines": _status_lines(npc_id, doc.get("status_reactions", {})),
		"world_state_lines": _copy_dict(_dict(doc.get("world_state_responses", {})).get(npc_id, {})),
	}


static func _node(node_id: String, raw: Dictionary) -> Dictionary:
	var options: Array = []
	var raw_options: Variant = raw.get("options", [])
	if raw_options is Array:
		for raw_option: Variant in raw_options:
			if raw_option is Dictionary:
				options.append(_option(raw_option))
	return {
		"id": node_id,
		"line_id": String(raw.get("line_id", "")),
		"speaker": String(raw.get("speaker", "")),
		"text": String(raw.get("text", "")),
		"options": options,
		"extra": _rest(raw, NODE_FIELDS),
	}


static func _option(raw: Dictionary) -> Dictionary:
	return {
		"text": String(raw.get("text", "")),
		"next": String(raw.get("leads_to", "")),
		"requires": _copy_dict(raw.get("requires", {})),
		"extra": _rest(raw, OPTION_FIELDS),
	}


## status_reactions is {status_id: {npc_id: line}}; this returns {status_id: line} for one NPC.
static func _status_lines(npc_id: String, reactions: Variant) -> Dictionary:
	var lines := {}
	var table := _dict(reactions)
	for status_id: String in table:
		var per_npc := _dict(table[status_id])
		if per_npc.has(npc_id):
			lines[status_id] = per_npc[npc_id]
	return lines


static func _rest(raw: Dictionary, known: Array) -> Dictionary:
	var rest := {}
	for key: String in raw:
		if not known.has(key):
			var value: Variant = raw[key]
			rest[key] = value.duplicate(true) if (value is Dictionary or value is Array) else value
	return rest


static func _dict(value: Variant) -> Dictionary:
	return value if value is Dictionary else {}


static func _copy_dict(value: Variant) -> Dictionary:
	return _dict(value).duplicate(true)
