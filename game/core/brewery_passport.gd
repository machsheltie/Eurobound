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
## Round v44 keychain numbers (tier B "Credentials", 5% off bar drinks per completed city, max 20%,
## Party Prep +1 Bravado per completed city at fight start) are data: the bottle_opener_keychain
## entry in assets/data/items/key_items.json. Nothing is hard-coded here; a missing number counts as 0.
const KEY_ITEMS_PATH := "res://assets/data/items/key_items.json"
## Party Prep is built but OFF: author, Eurobound Desk v45-party_prep_on (2026-11-12), "Leave it off".
## The data entry carries the same switch (party_prep.enabled); test_bar_discount checks they agree.
const PARTY_PREP_ENABLED := false

static var _keychain_cache: Dictionary = {}


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


static func completed_cities(state) -> int:
	return cities().filter(func(c): return city_complete(state, String(c["id"]))).size()


## The keychain's entry in key_items.json (read once).
static func keychain_def() -> Dictionary:
	if _keychain_cache.is_empty() and FileAccess.file_exists(KEY_ITEMS_PATH):
		var d = JSON.parse_string(FileAccess.get_file_as_string(KEY_ITEMS_PATH))
		if d is Dictionary and d.get("key_items", {}).get(KEYCHAIN) is Dictionary:
			_keychain_cache = d["key_items"][KEYCHAIN]
	return _keychain_cache


static func _keychain_number(def: Dictionary, block: String, field: String) -> float:
	var b = (keychain_def() if def.is_empty() else def).get(block, {})
	return float(b.get(field, 0)) if b is Dictionary else 0.0


## Discount per completed city as a fraction (0.05 for 5%).
static func bar_discount_per_city(def: Dictionary = {}) -> float:
	return _keychain_number(def, "bar_discount", "percent_per_completed_city") / 100.0


## Most the discount can reach, as a fraction (0.20 for 20%).
static func bar_discount_cap(def: Dictionary = {}) -> float:
	return _keychain_number(def, "bar_discount", "max_percent") / 100.0


static func party_prep_bravado_per_city(def: Dictionary = {}) -> int:
	return int(_keychain_number(def, "party_prep", "bravado_per_completed_city"))


## Bartender discount as a fraction (0.0 to the cap). Only while the bros hold the keychain.
## `def` replaces the keychain's data entry (tests); leave it empty in game code.
static func bar_discount(state, def: Dictionary = {}) -> float:
	if int(state.inventory.get(KEYCHAIN, 0)) <= 0:
		return 0.0
	return minf(bar_discount_per_city(def) * completed_cities(state), bar_discount_cap(def))


## Price of a bar drink after the keychain discount: nearest SOV, never below 1 SOV for a priced item.
static func discounted_bar_price(state, price: int) -> int:
	if price <= 0:
		return price
	return maxi(roundi(price * (1.0 - bar_discount(state))), 1)


## Bravado added to each bro at fight start (round v44 Party Prep). 0 while the switch is off.
static func party_prep_bravado(state, enabled: bool = PARTY_PREP_ENABLED, def: Dictionary = {}) -> int:
	if not enabled or int(state.inventory.get(KEYCHAIN, 0)) <= 0:
		return 0
	return party_prep_bravado_per_city(def) * completed_cities(state)
