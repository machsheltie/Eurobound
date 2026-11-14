class_name ArcadeHallLines
extends RefCounted
## The Absinthe Arcade hall + exterior completion lines, author-approved "first option in every slot"
## (Desk Eurobound-3ho-q4; WritingRoom/tasks/20261112_1419_absinthe_arcade_completion_lines/final.md,
## sections 2, 3, 4, 5 and 7a). The text lives verbatim in absinthe_arcade_hall_lines.json.

const DATA := "res://assets/data/locations/debaucheryville/absinthe_arcade_hall_lines.json"
const FIRST_ENTRY_FLAG := "absinthe_arcade_first_entry_seen"
const FLYER_FLAG := "club_flyer_placed"

static var _data: Dictionary = {}


static func data() -> Dictionary:
	if _data.is_empty():
		var parsed = JSON.parse_string(FileAccess.get_file_as_string(DATA))
		_data = parsed if parsed is Dictionary else {}
	return _data


## The first-entry bro lines ([{who, line}]) once; marks the flag so it never plays again.
static func take_first_entry(flags: Dictionary) -> Array:
	if bool(flags.get(FIRST_ENTRY_FLAG, false)):
		return []
	flags[FIRST_ENTRY_FLAG] = true
	return Array(data()["first_entry"])


static func vip_arrows() -> Array:
	return Array(data()["vip_arrows"])


static func bidet_examine() -> String:
	return String(data()["bidet_examine"])


## Exterior examine text for "street_cabinet", "chalkboard", "window_cat", or "flyer_panel" (which
## reads the flyer flag: before / after the bros post the DJ Beatdrop flyer).
static func exterior_examine(id: String, flags: Dictionary) -> String:
	match id:
		"street_cabinet", "chalkboard", "window_cat":
			return String(data()[id])
		"flyer_panel":
			return String(data()["flyer_after" if bool(flags.get(FLYER_FLAG, false)) else "flyer_before"])
	return ""


static func bark_groups() -> Dictionary:
	return data()["ambient_barks"]


## The next bark for a group, in written order and looping. `cursors` holds the per-group position.
static func next_bark(group: String, cursors: Dictionary) -> String:
	var lines: Array = Array(bark_groups().get(group, {}).get("lines", []))
	if lines.is_empty():
		return ""
	var i := int(cursors.get(group, 0)) % lines.size()
	cursors[group] = i + 1
	return String(lines[i])


static func jakub_sea_monkeys_win() -> String:
	return String(data()["jakub_sea_monkeys_win"])


static func objective(id: String) -> String:
	return String(data()["quest_objectives"].get(id, ""))


## Tomáš's loss-beat V.O. (his canon "Service charge." heard from the doorway).
static func loss_vo() -> String:
	return String(data()["grandpa_loss"]["tomas_vo"])


static func loss_staging() -> String:
	return String(data()["grandpa_loss"]["staging"])
