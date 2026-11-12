extends GutTest
## Bottle Opener Keychain bar discount + Party Prep switch (author round v44).


class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "hp": 45, "max_hp": 45, "bravado": 3,
		 "max_bravado": 12, "offense": 8, "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3,
		 "skills": ["roast_line"]},
	]


func _state(cities_done: int, keychain := true) -> FakeState:
	var s := FakeState.new()
	if keychain:
		BreweryPassport.start_tour(s)
	var all := BreweryPassport.cities()
	for i in cities_done:
		for b in BreweryPassport.breweries(String(all[i]["id"])):
			s.flags[BreweryPassport.STAMP_PREFIX + String(b["id"])] = true
	return s


func test_bar_discount_steps_five_percent_per_completed_city() -> void:
	assert_almost_eq(BreweryPassport.bar_discount(_state(0)), 0.0, 0.0001)
	assert_almost_eq(BreweryPassport.bar_discount(_state(1)), 0.05, 0.0001)
	assert_almost_eq(BreweryPassport.bar_discount(_state(2)), 0.10, 0.0001)
	assert_almost_eq(BreweryPassport.bar_discount(_state(4)), 0.20, 0.0001)


func test_bar_discount_is_capped_at_twenty_percent() -> void:
	assert_lte(BreweryPassport.bar_discount(_state(4)), 0.20)


func test_bar_discount_is_zero_without_the_keychain() -> void:
	var s := _state(2, false)
	assert_eq(BreweryPassport.bar_discount(s), 0.0)
	assert_eq(BreweryPassport.discounted_bar_price(s, 40), 40)


func test_bar_discount_price_rounds_to_nearest_sov() -> void:
	var s := _state(2)  # 10% off
	assert_eq(BreweryPassport.discounted_bar_price(s, 40), 36)
	assert_eq(BreweryPassport.discounted_bar_price(s, 15), 14)  # 13.5 rounds up to 14


func test_bar_discount_price_never_drops_below_one_sov() -> void:
	var s := _state(4)
	assert_eq(BreweryPassport.discounted_bar_price(s, 1), 1)
	assert_eq(BreweryPassport.discounted_bar_price(s, 2), 2)  # 1.6 rounds to 2


func test_bar_discount_free_items_stay_free() -> void:
	assert_eq(BreweryPassport.discounted_bar_price(_state(4), 0), 0)


func test_party_prep_is_switched_off_by_default() -> void:
	assert_false(BreweryPassport.PARTY_PREP_ENABLED)
	assert_eq(BreweryPassport.party_prep_bravado(_state(3)), 0)


func test_party_prep_when_enabled_gives_one_bravado_per_completed_city() -> void:
	assert_eq(BreweryPassport.party_prep_bravado(_state(3), true), 3)
	assert_eq(BreweryPassport.party_prep_bravado(_state(3, false), true), 0)


func test_party_prep_build_fight_leaves_bravado_untouched_while_off() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 1
	var s := _state(3)
	var core := ArcadeBattle.build_fight(["accounts_receivable"], s, rng)
	assert_eq(core.party[0].bravado, 3)
