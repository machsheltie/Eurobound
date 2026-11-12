class_name BreweryPassport
extends RefCounted
## Brewery Passport + bottle opener system (author round v42).
## Specs: design/quests/general_quests/brewerytour.md (master), design/items/brewery_tour/*,
## design/quests/publandia/brewerytourpublandia.md ("The Trigger").
## - The tour starts when the bros first order a special beer at The Blarney Trap: that grants the
##   keychain, the first opener and the passport book at once. Before that nothing is awarded.
## - Openers and stamps are EARNED on challenge completion, never sold.
## State lives in GameState (inventory for keychain + book, flags for openers and stamps), so saves
## need no schema change. Registry: assets/data/brewery_tour/breweries.json.

const PATH := "res://assets/data/brewery_tour/breweries.json"
const KEYCHAIN := "bottle_opener_keychain"
const PASSPORT_BOOK := "brewery_passport_book"
const TOUR_FLAG := "brewery_tour_started"
const OPENER_PREFIX := "brewery_opener_"
const STAMP_PREFIX := "brewery_stamp_"


static func _data() -> Dictionary:
	if not FileAccess.file_exists(PATH):
		return {}
	var d = JSON.parse_string(FileAccess.get_file_as_string(PATH))
	return d if d is Dictionary else {}


static func cities() -> Array:
	return _data().get("cities", [])


static func breweries(city: String = "") -> Array:
	var all: Array = _data().get("breweries", [])
	return all if city == "" else all.filter(func(b): return b["city"] == city)


static func brewery(brewery_id: String) -> Dictionary:
	for b in breweries():
		if b["id"] == brewery_id:
			return b
	return {}


static func tour_started(state) -> bool:
	return bool(state.flags.get(TOUR_FLAG, false))


## The Trigger. Grants keychain, the first opener and the passport book once; false if already started.
static func start_tour(state) -> bool:
	if tour_started(state):
		return false
	state.flags[TOUR_FLAG] = true
	state.inventory[KEYCHAIN] = 1
	state.inventory[PASSPORT_BOOK] = 1
	state.flags[OPENER_PREFIX + String(_data().get("first_opener", "blarney_trap"))] = true
	return true


static func has_opener(state, brewery_id: String) -> bool:
	return bool(state.flags.get(OPENER_PREFIX + brewery_id, false))


static func has_stamp(state, brewery_id: String) -> bool:
	return bool(state.flags.get(STAMP_PREFIX + brewery_id, false))


## Called on challenge completion. Refused before the tour starts or for an unknown brewery.
static func award_opener(state, brewery_id: String) -> bool:
	if not tour_started(state) or brewery(brewery_id).is_empty() or has_opener(state, brewery_id):
		return false
	state.flags[OPENER_PREFIX + brewery_id] = true
	return true


static func award_stamp(state, brewery_id: String) -> bool:
	if not tour_started(state) or brewery(brewery_id).is_empty() or has_stamp(state, brewery_id):
		return false
	state.flags[STAMP_PREFIX + brewery_id] = true
	return true


## A city is complete when all four of its breweries are stamped.
static func city_complete(state, city: String) -> bool:
	var list := breweries(city)
	return not list.is_empty() and list.all(func(b): return has_stamp(state, b["id"]))


static func stamp_count(state, city: String = "") -> int:
	return breweries(city).filter(func(b): return has_stamp(state, b["id"])).size()
