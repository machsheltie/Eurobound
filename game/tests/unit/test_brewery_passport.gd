extends GutTest
## Brewery Passport + openers (author round v42): trigger, gating, awards, city completion, menu.

class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []
	var current_scene_path := ""


func _menu(s) -> FieldMenu:
	var m := FieldMenu.new()
	m.setup(s)
	add_child_autofree(m)
	m.mode = "Brewery Passport"
	m._draw()
	return m


func test_brewery_passport_registry_has_16_breweries_four_per_city() -> void:
	assert_eq(BreweryPassport.breweries().size(), 16)
	assert_eq(BreweryPassport.cities().size(), 4)
	for c in BreweryPassport.cities():
		assert_eq(BreweryPassport.breweries(c["id"]).size(), 4)


func test_brewery_passport_awards_are_refused_before_the_tour_starts() -> void:
	var s := FakeState.new()
	assert_false(BreweryPassport.tour_started(s))
	assert_false(BreweryPassport.award_opener(s, "stoutworks_brewery"))
	assert_false(BreweryPassport.award_stamp(s, "blarney_trap"))
	assert_false(BreweryPassport.has_opener(s, "stoutworks_brewery"))
	assert_false(BreweryPassport.has_stamp(s, "blarney_trap"))


func test_brewery_passport_start_tour_grants_keychain_book_and_first_opener_only() -> void:
	var s := FakeState.new()
	assert_true(BreweryPassport.start_tour(s))
	assert_eq(int(s.inventory[BreweryPassport.KEYCHAIN]), 1)
	assert_eq(int(s.inventory[BreweryPassport.PASSPORT_BOOK]), 1)
	assert_true(BreweryPassport.has_opener(s, "blarney_trap"))
	assert_false(BreweryPassport.has_stamp(s, "blarney_trap"))
	assert_false(BreweryPassport.start_tour(s), "the trigger fires once")
	assert_eq(int(s.inventory[BreweryPassport.KEYCHAIN]), 1)


func test_brewery_passport_awards_work_after_start_and_reject_unknown_or_repeat() -> void:
	var s := FakeState.new()
	BreweryPassport.start_tour(s)
	assert_true(BreweryPassport.award_opener(s, "shenanigans"))
	assert_false(BreweryPassport.award_opener(s, "shenanigans"))
	assert_true(BreweryPassport.award_stamp(s, "shenanigans"))
	assert_false(BreweryPassport.award_stamp(s, "nowhere_pub"))


func test_brewery_passport_city_complete_needs_all_four_stamps() -> void:
	var s := FakeState.new()
	BreweryPassport.start_tour(s)
	for b in BreweryPassport.breweries("publandia").slice(0, 3):
		BreweryPassport.award_stamp(s, b["id"])
	assert_false(BreweryPassport.city_complete(s, "publandia"))
	BreweryPassport.award_stamp(s, BreweryPassport.breweries("publandia")[3]["id"])
	assert_true(BreweryPassport.city_complete(s, "publandia"))
	assert_false(BreweryPassport.city_complete(s, "sinfonia"))


func test_brewery_passport_menu_shows_dash_before_tour_and_list_after() -> void:
	var s := FakeState.new()
	var m := _menu(s)
	assert_eq(m._body.text, "[b]Brewery Passport[/b]\n\n—")
	BreweryPassport.start_tour(s)
	BreweryPassport.award_stamp(s, "blarney_trap")
	m._draw()
	assert_string_contains(m._body.text, "The Blarney Trap")
	assert_string_contains(m._body.text, "Shamsterdam")
	assert_string_contains(m._body.text, "Stamp [x]  Opener [x]")


func test_brewery_passport_registered_key_items_exist() -> void:
	var d = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/items/key_items.json"))
	assert_true(d["key_items"].has(BreweryPassport.KEYCHAIN))
	assert_true(d["key_items"].has(BreweryPassport.PASSPORT_BOOK))
