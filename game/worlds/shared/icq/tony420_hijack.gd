class_name Tony420Hijack
extends RefCounted
## Tony420 hijacks the bros' ICQ at a FREE Wi-Fi hotspot (wifihotspots.md). Ruled at the Writers'
## Room desk 2026-11-11 (NEXT_WORK.md, "Tony420 / FREE Wi-Fi hijack"): the first hijack sets
## `tony420_unlocked`, and the Meme Black Market trade reads that flag plus the rare-memes check.
## The script lives in tony420_hotspot_hijack.json; lines past the canon greeting are placeholders
## until the author writes them (Production Desk Eurobound-ign-q1).

const DATA := "res://assets/data/world_data/events/icqdialogues/tony420_hotspot_hijack.json"
const UNLOCK_FLAG := "tony420_unlocked"
const PENDING_MARK := "pending author"

static var _data: Dictionary = {}


static func data() -> Dictionary:
	if _data.is_empty():
		var parsed = JSON.parse_string(FileAccess.get_file_as_string(DATA))
		_data = parsed if parsed is Dictionary else {}
	return _data


static func unlocked(state) -> bool:
	return bool(state.flags.get(UNLOCK_FLAG, false))


## Records a hijack. True when it was the first (the one that sets `tony420_unlocked`).
static func mark_hijacked(state) -> bool:
	if unlocked(state):
		return false
	state.flags[UNLOCK_FLAG] = true
	return true


## The first hijack's spoken lines, in order: [{who, line}].
static func spoken_lines() -> Array:
	var out := []
	for step: Dictionary in data().get("first_hijack", []):
		if step.has("line"):
			out.append({"who": String(step.get("who", "")), "line": String(step["line"])})
	return out


## True while any line of the script still waits on the author.
static func pending() -> bool:
	return spoken_lines().any(func(l): return String(l["line"]).contains(PENDING_MARK))


## The Meme Black Market's .SWF vault trade (debaucheryville_interactions.json, tony420_trading):
## Tony's been unlocked and the bros hold the rare memes. The rare-memes check is the caller's.
static func meme_trade_open(state, has_rare_memes: bool) -> bool:
	return unlocked(state) and has_rare_memes


## Plays the hijack. `stage` has `dialogue` (DialogueBox), `state`, and optionally `cue(id)` for
## sounds. The flag is set the moment Tony takes over the connection. Returns true on the first.
static func play(stage) -> bool:
	var first := mark_hijacked(stage.state)
	var d: DialogueBox = stage.dialogue
	for step: Dictionary in data().get("first_hijack", []):
		if step.has("cue"):
			if stage.has_method("cue"):
				stage.cue(String(step["cue"]))
			await d.beat()
		elif step.has("line"):
			await d.say(String(step.get("who", "")), String(step["line"]))
		elif step.get("beat", false):
			await d.beat()
	d.close()
	return first
