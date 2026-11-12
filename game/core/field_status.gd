class_name FieldStatus
extends RefCounted
## Statuses that last OUTSIDE battle (author round v42, arc_systems = all). Kept in the saved
## GameState.flags under "field_status": {target: {status_id: {"unit", "until" | "left"}}}.
## target is a party member id ("lord_pilsner") or PARTY for the whole party.
## Two time units, because the game clock moves only when the bros act:
##  - UNIT_CLOCK: game-clock minutes (GameClock). Stores the expiry minute; expires lazily.
##  - UNIT_REAL: real seconds, for very short effects. Stores seconds left; call tick(state, delta)
##    from a node that runs while the bros walk (PlayerController does).
## Field effects defined by the docs, and only those:
##  - GREEN_FAIRY_CONFUSION reverses movement (the_absinthium_taproom.md 283-287, "Reversed controls").
##  - EMBARRASSED is a gate other content checks with has() (clawmachinemaintenanceclosetrestroom.md
##    102-117); it has no field effect of its own.

const KEY := "field_status"
const PARTY := "party"
const UNIT_CLOCK := "clock"
const UNIT_REAL := "real"

const GREEN_FAIRY_CONFUSION := "green_fairy_confusion"
const EMBARRASSED := "embarrassed"

## Lengths the docs give. Ranges are {min, max}; the caller picks inside them.
## the_absinthium_taproom.md 283-287: Confusion 30 sec - 3 min, Saw Yourself 1 hour,
## Existentially Rested 2 hours.
const DOC_DURATIONS := {
	"green_fairy_confusion": {"unit": UNIT_REAL, "min": 30, "max": 180},
	"saw_yourself": {"unit": UNIT_CLOCK, "min": 60, "max": 60},
	"existentially_rested": {"unit": UNIT_CLOCK, "min": 120, "max": 120},
}


static func _all(state) -> Dictionary:
	if not state.flags.has(KEY):
		state.flags[KEY] = {}
	return state.flags[KEY]


## Applies (or refreshes) a status. `amount` is minutes for UNIT_CLOCK, seconds for UNIT_REAL.
## Non-positive amounts apply nothing.
static func apply(state, target: String, status_id: String, amount: float, unit: String = UNIT_CLOCK) -> void:
	if amount <= 0.0 or status_id == "":
		return
	var rows: Dictionary = _all(state).get(target, {})
	if unit == UNIT_REAL:
		rows[status_id] = {"unit": UNIT_REAL, "left": amount}
	else:
		rows[status_id] = {"unit": UNIT_CLOCK, "until": GameClock.minutes(state) + int(amount)}
	_all(state)[target] = rows


static func _live(state, row: Dictionary) -> bool:
	if String(row.get("unit", UNIT_CLOCK)) == UNIT_REAL:
		return float(row.get("left", 0.0)) > 0.0
	return GameClock.minutes(state) < int(row.get("until", 0))


## True when the target has the status. target "" means anyone: the party or any member.
static func has(state, status_id: String, target: String = "") -> bool:
	var all := _all(state)
	for t in all.keys():
		if target != "" and t != target and t != PARTY:
			continue
		var row: Dictionary = Dictionary(all[t]).get(status_id, {})
		if not row.is_empty() and _live(state, row):
			return true
	return false


static func remove(state, status_id: String, target: String = "") -> void:
	var all := _all(state)
	for t in all.keys():
		if target == "" or t == target:
			Dictionary(all[t]).erase(status_id)


## Live status ids on a target (and the whole-party ones); "" lists everything.
static func list(state, target: String = "") -> Array:
	var out := []
	var all := _all(state)
	for t in all.keys():
		if target != "" and t != target and t != PARTY:
			continue
		for id in Dictionary(all[t]).keys():
			if _live(state, all[t][id]) and not out.has(id):
				out.append(id)
	return out


## Drops expired statuses and counts real-second ones down by `delta`.
static func tick(state, delta: float) -> void:
	var all := _all(state)
	for t in all.keys():
		var rows: Dictionary = all[t]
		for id in rows.keys():
			var row: Dictionary = rows[id]
			if String(row.get("unit", UNIT_CLOCK)) == UNIT_REAL:
				row["left"] = float(row.get("left", 0.0)) - delta
			if not _live(state, row):
				rows.erase(id)
		if rows.is_empty():
			all.erase(t)


## Green Fairy Confusion: reversed controls.
static func controls_reversed(state) -> bool:
	return has(state, GREEN_FAIRY_CONFUSION)
