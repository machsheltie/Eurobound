class_name NpcConversation
extends RefCounted
## Reader for the NPC conversation hand-in file (Eurobound-04t2, author ruling 2026-11-15: the
## Arcade's DialogueBox is the one talk box for the whole game; writers hand in each NPC's
## conversation as a data file, the way ICQ messages are handed in). Format and rules:
## design/mechanics/Social/npc_conversation_files.md. Files live in assets/data/npcs/conversations/
## as <npc_id>.json, one per NPC.
##
## Reads and reports only. Text is copied as written; nothing is repaired, filled in or invented.
## Wired to no UI: a walker that plays a conversation through DialogueBox comes later.
##
## read_doc / read_file return {"conversation": {...}, "problems": [String]}.
##   conversation = {"npc_id", "speaker", "start", "nodes": {node_id: node}, "extra"}
##   node   = {"id", "speaker", "lines": [String], "next", "choices": [choice], "set_flags",
##             "source", "extra"}
##   choice = {"text", "next", "requires_flags", "blocks_flags", "set_flags", "extra"}
## `next` of "" ends the conversation. `extra` holds every field this reader does not name.

const DIR := "res://assets/data/npcs/conversations/"
const TOP_FIELDS := ["_source", "npc_id", "speaker", "start", "nodes"]
const NODE_FIELDS := ["id", "speaker", "lines", "next", "choices", "set_flags", "source"]
const CHOICE_FIELDS := ["text", "next", "requires_flags", "blocks_flags", "set_flags"]


static func path_for(npc_id: String) -> String:
	return DIR + npc_id + ".json"


static func read_file(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return {"conversation": {}, "problems": ["%s: file not found" % path]}
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
	if not (parsed is Dictionary):
		return {"conversation": {}, "problems": ["%s: not a JSON object" % path]}
	return read_doc(parsed)


static func read_doc(doc: Dictionary) -> Dictionary:
	var problems: Array = []
	var npc_id := String(doc.get("npc_id", ""))
	if npc_id == "":
		problems.append("no npc_id")
	var nodes := {}
	var raw_nodes: Variant = doc.get("nodes", [])
	if not (raw_nodes is Array) or (raw_nodes as Array).is_empty():
		problems.append("%s: nodes must be a non-empty list" % npc_id)
		raw_nodes = []
	for i: int in (raw_nodes as Array).size():
		var raw: Variant = raw_nodes[i]
		if not (raw is Dictionary):
			problems.append("%s: nodes[%d] is not an object" % [npc_id, i])
			continue
		var node := _node(raw, problems, npc_id, i)
		if nodes.has(node["id"]):
			problems.append("%s: duplicate node id '%s'" % [npc_id, node["id"]])
			continue
		nodes[node["id"]] = node
	var start := String(doc.get("start", ""))
	if not nodes.has(start):
		problems.append("%s: start '%s' is not a node" % [npc_id, start])
	for node_id: String in nodes:
		_check_links(nodes[node_id], nodes, problems, npc_id)
	return {
		"conversation": {
			"npc_id": npc_id,
			"speaker": String(doc.get("speaker", "")),
			"start": start,
			"nodes": nodes,
			"extra": _rest(doc, TOP_FIELDS),
		},
		"problems": problems,
	}


static func _node(raw: Dictionary, problems: Array, npc_id: String, index: int) -> Dictionary:
	var node_id := String(raw.get("id", ""))
	var where := "%s/%s" % [npc_id, node_id if node_id != "" else "nodes[%d]" % index]
	if node_id == "":
		problems.append("%s: node has no id" % where)
	var lines: Array = []
	var raw_lines: Variant = raw.get("lines", [])
	if raw_lines is Array:
		for line: Variant in raw_lines:
			if line is String and (line as String).strip_edges() != "":
				lines.append(line)
			else:
				problems.append("%s: a line is blank or not text" % where)
	if lines.is_empty():
		problems.append("%s: no lines" % where)
	var choices: Array = []
	var raw_choices: Variant = raw.get("choices", [])
	if raw_choices is Array:
		for j: int in (raw_choices as Array).size():
			var raw_choice: Variant = raw_choices[j]
			if raw_choice is Dictionary:
				choices.append(_choice(raw_choice, problems, where, j))
			else:
				problems.append("%s: choice %d is not an object" % [where, j + 1])
	if not choices.is_empty() and String(raw.get("next", "")) != "":
		problems.append("%s: has both choices and next; choices decide where the talk goes" % where)
	if choices.size() == 1:
		problems.append("%s: a single choice is not a choice; use next" % where)
	return {
		"id": node_id,
		"speaker": String(raw.get("speaker", "")),
		"lines": lines,
		"next": String(raw.get("next", "")),
		"choices": choices,
		"set_flags": _flag_writes(raw.get("set_flags", {}), problems, where),
		"source": String(raw.get("source", "")),
		"extra": _rest(raw, NODE_FIELDS),
	}


static func _choice(raw: Dictionary, problems: Array, where: String, index: int) -> Dictionary:
	var label := "%s choice %d" % [where, index + 1]
	var text := String(raw.get("text", ""))
	if text.strip_edges() == "":
		problems.append("%s: no text" % label)
	return {
		"text": text,
		"next": String(raw.get("next", "")),
		"requires_flags": _flag_list(raw.get("requires_flags", []), problems, label),
		"blocks_flags": _flag_list(raw.get("blocks_flags", []), problems, label),
		"set_flags": _flag_writes(raw.get("set_flags", {}), problems, label),
		"extra": _rest(raw, CHOICE_FIELDS),
	}


static func _check_links(node: Dictionary, nodes: Dictionary, problems: Array, npc_id: String) -> void:
	var next: String = node["next"]
	if next != "" and not nodes.has(next):
		problems.append("%s/%s: next '%s' is not a node" % [npc_id, node["id"], next])
	for i: int in node["choices"].size():
		var to: String = node["choices"][i]["next"]
		if to != "" and not nodes.has(to):
			problems.append("%s/%s: choice %d leads to '%s', which does not exist"
				% [npc_id, node["id"], i + 1, to])


static func _flag_list(value: Variant, problems: Array, where: String) -> Array:
	var out: Array = []
	if value is Array:
		for flag: Variant in value:
			if flag is String and (flag as String) != "":
				out.append(flag)
			else:
				problems.append("%s: flag ids must be non-empty text" % where)
	else:
		problems.append("%s: a flag list must be a list" % where)
	return out


static func _flag_writes(value: Variant, problems: Array, where: String) -> Dictionary:
	if value is Dictionary:
		return (value as Dictionary).duplicate(true)
	problems.append("%s: set_flags must be an object of flag id to value" % where)
	return {}


static func _rest(raw: Dictionary, known: Array) -> Dictionary:
	var rest := {}
	for key: String in raw:
		if not known.has(key):
			var value: Variant = raw[key]
			rest[key] = value.duplicate(true) if (value is Dictionary or value is Array) else value
	return rest
