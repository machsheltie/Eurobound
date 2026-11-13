extends GutTest
## Dr. Vaněk at the Absinthium Taproom bar: keychain gate, opener check, Lager sale, stamp.
## Spec: design/worlds/debaucheryville/the_absinthium_taproom.md.


class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}

	func spend_sovs(amount: int) -> bool:
		if sovs < amount:
			return false
		sovs -= amount
		return true

	func add_item(id: String, count: int = 1, _max_stack: Variant = null) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _toured(opener := true, sovs := 50) -> FakeState:
	var s := FakeState.new()
	BreweryPassport.start_tour(s)
	if opener:
		BreweryPassport.award_opener(s, VanekTaproom.BREWERY_ID)
	s.sovs = sovs
	return s


func _all_conditions(s: FakeState) -> void:
	s.flags[TaproomMaze.FLAG_COMPLETED] = true
	s.flags[TaproomBattle.FLAG_WISP_DEFEATED] = true
	s.flags[VanekTaproom.FLAG_LAGER_BOUGHT] = true


func test_vanek_taproom_gate_without_keychain_is_no_keychain() -> void:
	var s := FakeState.new()
	assert_eq(VanekTaproom.gate(s), VanekTaproom.GATE_NO_KEYCHAIN)


func test_vanek_taproom_gate_checks_keychain_before_opener() -> void:
	var s := FakeState.new()
	s.flags[BreweryPassport.OPENER_PREFIX + VanekTaproom.BREWERY_ID] = true
	assert_eq(VanekTaproom.gate(s), VanekTaproom.GATE_NO_KEYCHAIN)


func test_vanek_taproom_gate_keychain_without_opener_is_no_opener() -> void:
	var s := _toured(false)
	assert_eq(VanekTaproom.gate(s), VanekTaproom.GATE_NO_OPENER)


func test_vanek_taproom_gate_keychain_and_opener_is_ok() -> void:
	assert_eq(VanekTaproom.gate(_toured()), VanekTaproom.GATE_OK)


func test_vanek_taproom_buy_lager_without_opener_is_refused_and_takes_nothing() -> void:
	var s := _toured(false)
	assert_eq(VanekTaproom.buy_lager(s), VanekTaproom.SALE_REFUSED)
	assert_eq(s.sovs, 50)
	assert_false(s.inventory.has(VanekTaproom.LAGER_ID))


func test_vanek_taproom_lager_price_is_12_with_no_cities_done() -> void:
	assert_eq(VanekTaproom.lager_price(_toured()), 12)


func test_vanek_taproom_lager_price_applies_keychain_discount() -> void:
	var s := _toured()
	for b in BreweryPassport.breweries(String(BreweryPassport.cities()[0]["id"])):
		s.flags[BreweryPassport.STAMP_PREFIX + String(b["id"])] = true
	assert_eq(VanekTaproom.lager_price(s), BreweryPassport.discounted_bar_price(s, 12))
	assert_lt(VanekTaproom.lager_price(s), 12)


func test_vanek_taproom_buy_lager_spends_sovs_adds_item_and_flags_purchase() -> void:
	var s := _toured()
	assert_eq(VanekTaproom.buy_lager(s), VanekTaproom.SALE_BOUGHT)
	assert_eq(s.sovs, 38)
	assert_eq(int(s.inventory[VanekTaproom.LAGER_ID]), 1)
	assert_true(bool(s.flags[VanekTaproom.FLAG_LAGER_BOUGHT]))


func test_vanek_taproom_buy_lager_when_short_of_sovs_cannot_afford() -> void:
	var s := _toured(true, 11)
	assert_eq(VanekTaproom.buy_lager(s), VanekTaproom.SALE_CANNOT_AFFORD)
	assert_eq(s.sovs, 11)
	assert_false(s.flags.has(VanekTaproom.FLAG_LAGER_BOUGHT))


func test_vanek_taproom_stamp_conditions_all_met_awards_stamp() -> void:
	var s := _toured()
	_all_conditions(s)
	assert_true(VanekTaproom.try_stamp(s))
	assert_true(BreweryPassport.has_stamp(s, VanekTaproom.BREWERY_ID))


func test_vanek_taproom_stamp_wisp_survived_counts_like_defeated() -> void:
	var s := _toured()
	_all_conditions(s)
	s.flags.erase(TaproomBattle.FLAG_WISP_DEFEATED)
	s.flags[TaproomBattle.FLAG_WISP_SURVIVED] = true
	assert_true(VanekTaproom.try_stamp(s))


func test_vanek_taproom_stamp_without_maze_is_not_awarded() -> void:
	var s := _toured()
	_all_conditions(s)
	s.flags.erase(TaproomMaze.FLAG_COMPLETED)
	assert_false(VanekTaproom.try_stamp(s))
	assert_false(BreweryPassport.has_stamp(s, VanekTaproom.BREWERY_ID))


func test_vanek_taproom_stamp_without_wisp_is_not_awarded() -> void:
	var s := _toured()
	_all_conditions(s)
	s.flags.erase(TaproomBattle.FLAG_WISP_DEFEATED)
	assert_false(VanekTaproom.try_stamp(s))


func test_vanek_taproom_stamp_without_lager_purchase_is_not_awarded() -> void:
	var s := _toured()
	_all_conditions(s)
	s.flags.erase(VanekTaproom.FLAG_LAGER_BOUGHT)
	assert_false(VanekTaproom.try_stamp(s))


func test_vanek_taproom_stamp_without_keychain_is_not_awarded() -> void:
	var s := _toured()
	_all_conditions(s)
	s.inventory.erase(BreweryPassport.KEYCHAIN)
	assert_false(VanekTaproom.try_stamp(s))


func test_vanek_taproom_stamp_twice_awards_only_once() -> void:
	var s := _toured()
	_all_conditions(s)
	VanekTaproom.try_stamp(s)
	assert_false(VanekTaproom.try_stamp(s))
