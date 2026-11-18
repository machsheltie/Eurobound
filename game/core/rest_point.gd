class_name RestPoint
extends RefCounted
## A place the bros can book a bed and rest (Eurobound-vxa4; rules 9-16 of
## docs/superpowers/specs/2026-11-15-rest-points-and-rules-proposal.md, approved on Desk
## Eurobound-8snp-q1). Data: world_data/rest_points.json. The first one is the Hostel Midnight
## Checkout 12-Bed Mixed Dorm (rule 15: no roommate events, no sleep roll).
##
## Flow: book(state) at reception pays first (rule 12): GameState.can_afford / spend_sovs, no bed
## without the SOVS. sleep(state, saver) at the bed offers the save first (rule 14,
## SaveSystem.save_with_picker; no autosave), then GameClock.rest runs the rest (rules 10, 11, 16:
## rest events, status endings, Sober, clock to 10:00). A cancelled save does not stop the sleep.
## No UI here: a screen reads `lines` and shows them itself.
##
## What the bed restores is NOT ruled (N2): restore.hp_pct / bravado_pct are null in data and
## nothing is restored until the author rules a number. Groggy (N5) is never applied.

const DATA_PATH := "res://assets/data/world_data/rest_points.json"
## Flag set by a paid booking, cleared by the rest it buys (the doc's hostel_checked_in verb gate).
const BOOKED_PREFIX := "rest_booked_"

var id := ""
var data: Dictionary = {}


## Loads one rest point from the data file; null for an unknown id.
static func from_id(rest_id: String, path: String = DATA_PATH) -> RestPoint:
	if not FileAccess.file_exists(path):
		return null
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
	if not (parsed is Dictionary):
		return null
	for row in Array(Dictionary(parsed).get("rest_points", [])):
		if row is Dictionary and String(row.get("id", "")) == rest_id:
			return from_data(row)
	return null


static func from_data(row: Dictionary) -> RestPoint:
	var rp := RestPoint.new()
	rp.data = row
	rp.id = String(row.get("id", ""))
	return rp


func price() -> int:
	return int(data.get("price_sovs", 0))


func line(key: String) -> String:
	return String(Dictionary(data.get("lines", {})).get(key, ""))


func flag_key() -> String:
	return BOOKED_PREFIX + id


func is_booked(state) -> bool:
	return bool(state.flags.get(flag_key(), false))


func can_book(state) -> bool:
	return not is_booked(state) and state.can_afford(price())


## Reception: pay the price, get the bed. False (nothing taken) with too few SOVS or a bed already
## booked.
func book(state) -> bool:
	if not can_book(state):
		return false
	if not state.spend_sovs(price()):
		return false
	state.flags[flag_key()] = true
	return true


## True once the author has ruled a restore number (N2); false while both are null.
func restore_enabled() -> bool:
	var r: Dictionary = data.get("restore", {})
	return r.get("hp_pct", null) != null or r.get("bravado_pct", null) != null


## At the bed: save offered first, then the rest. Returns false (nothing happens) with no booking.
## `saver` is the SaveSystem (null skips the offer: tests, or a stand-in without one).
func sleep(state, saver = null) -> bool:
	if not is_booked(state):
		return false
	if bool(data.get("saves_at_bed", false)) and saver != null:
		await saver.save_with_picker("bed", state)
	state.flags.erase(flag_key())
	GameClock.rest(state)
	_restore(state)
	return true


## Applies the ruled restore, if any: each percentage is of the member's max, never past it.
func _restore(state) -> void:
	if not restore_enabled() or not ("party" in state):
		return
	var r: Dictionary = data["restore"]
	for m in state.party:
		if r.get("hp_pct", null) != null:
			m["hp"] = mini(int(m["max_hp"]), int(m["hp"]) + ceili(int(m["max_hp"]) * float(r["hp_pct"]) / 100.0))
		if r.get("bravado_pct", null) != null:
			m["bravado"] = mini(int(m["max_bravado"]), int(m["bravado"]) + ceili(int(m["max_bravado"]) * float(r["bravado_pct"]) / 100.0))
