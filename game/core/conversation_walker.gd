class_name ConversationWalker
extends RefCounted
## Plays an NpcConversation through the shared DialogueBox (Eurobound-r1qf; format:
## design/mechanics/Social/npc_conversation_files.md). Wired to no NPC yet.
##
## Usage:  var w := ConversationWalker.new()
##         await w.play(DataRepo.get_dialogue_tree(id), box, GameState)
## `conversation` is NpcConversation's "conversation" dictionary (what get_dialogue_tree returns).
## `state` is anything with a `flags` dictionary (GameState). Flag writes follow the ruled shape:
## true sets, false clears. Visible choice labels go to DialogueBox.choose; the picked index is
## mapped back to its choice. Text is shown as written.
## Keep a reference to the walker while it plays (an un-awaited, unreferenced walker is freed mid-talk).
## Bad data never crashes: the talk ends, `errors` records why, a warning is pushed.

signal finished(npc_id: String)

## Safety stop for a no-choice loop (a node chain that never ends). Not a gameplay value.
var max_nodes := 1000
var errors: Array = []


func play(conversation: Dictionary, box: DialogueBox, state) -> void:
	errors = []
	var npc_id := String(conversation.get("npc_id", ""))
	var nodes: Dictionary = conversation.get("nodes", {})
	var node_id := String(conversation.get("start", ""))
	var steps := 0
	while node_id != "":
		if not nodes.has(node_id):
			_fail("%s: node '%s' does not exist" % [npc_id, node_id])
			break
		steps += 1
		if steps > max_nodes:
			_fail("%s: more than %d nodes in one talk, cut off" % [npc_id, max_nodes])
			break
		var node: Dictionary = nodes[node_id]
		_write_flags(state, node.get("set_flags", {}))
		var speaker := String(node.get("speaker", ""))
		if speaker == "":
			speaker = String(conversation.get("speaker", ""))
		for line: String in node.get("lines", []):
			await box.say(speaker, line)
		var choices: Array = node.get("choices", [])
		if choices.is_empty():
			node_id = String(node.get("next", ""))
			continue
		var shown: Array = choices.filter(func(c: Dictionary) -> bool: return _allowed(c, state))
		if shown.is_empty():
			_fail("%s/%s: every choice is hidden by flags" % [npc_id, node_id])
			break
		var labels: Array = shown.map(func(c: Dictionary) -> String: return c["text"])
		var index: int = await box.choose(labels)
		var picked: Dictionary = shown[clampi(index, 0, shown.size() - 1)]
		_write_flags(state, picked.get("set_flags", {}))
		node_id = String(picked.get("next", ""))
	box.close()
	finished.emit(npc_id)


func _fail(message: String) -> void:
	errors.append(message)
	push_warning("ConversationWalker: " + message)


static func _allowed(choice: Dictionary, state) -> bool:
	for flag: Variant in choice.get("requires_flags", []):
		if not bool(state.flags.get(String(flag), false)):
			return false
	for flag: Variant in choice.get("blocks_flags", []):
		if bool(state.flags.get(String(flag), false)):
			return false
	return true


static func _write_flags(state, writes: Dictionary) -> void:
	for key: Variant in writes:
		var value: Variant = writes[key]
		if not (value is bool):
			continue
		if value:
			state.flags[String(key)] = true
		else:
			state.flags.erase(String(key))
