class_name IcqQueue
extends RefCounted
## The ICQ message queue: which popup a FREE Wi-Fi hotspot delivers next. Messages live in
## icq_hotspot_messages.json (sender, lines, hotspots, once, requires_flags, blocks_flags, source).
## State is the GameState-shaped object with a `flags` dictionary, so "seen" survives saves.
## Tony420's first hijack is separate (Tony420Hijack) and is handled by IcqHub before this queue.

const DATA := "res://assets/data/world_data/events/icqdialogues/icq_hotspot_messages.json"
const SEEN_PREFIX := "icq_seen_"

var messages: Array = []


static func from_file(path: String = DATA) -> IcqQueue:
	var q := IcqQueue.new()
	var parsed = JSON.parse_string(FileAccess.get_file_as_string(path))
	if parsed is Dictionary:
		q.messages = parsed.get("messages", [])
	return q


static func seen(state, id: String) -> bool:
	return bool(state.flags.get(SEEN_PREFIX + id, false))


static func mark_seen(state, id: String) -> void:
	state.flags[SEEN_PREFIX + id] = true


func eligible(msg: Dictionary, state, hotspot_id: String) -> bool:
	var spots: Array = msg.get("hotspots", [])
	if not spots.is_empty() and not spots.has(hotspot_id):
		return false
	if bool(msg.get("once", false)) and seen(state, String(msg.get("id", ""))):
		return false
	for f in msg.get("requires_flags", []):
		if not bool(state.flags.get(String(f), false)):
			return false
	for f in msg.get("blocks_flags", []):
		if bool(state.flags.get(String(f), false)):
			return false
	return true


## The first eligible message for this hotspot, in file order, or {}. Does not mark it seen.
func next_for(state, hotspot_id: String) -> Dictionary:
	for msg: Dictionary in messages:
		if eligible(msg, state, hotspot_id):
			return msg
	return {}


## Picks the next message and marks it seen. {} when nothing is eligible.
func take(state, hotspot_id: String) -> Dictionary:
	var msg := next_for(state, hotspot_id)
	if not msg.is_empty():
		mark_seen(state, String(msg.get("id", "")))
	return msg
