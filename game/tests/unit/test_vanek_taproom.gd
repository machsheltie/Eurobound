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


func test_vanek_taproom_hours_wrap_past_midnight() -> void:
	for h in [20, 23, 0, 3]:
		assert_true(VanekTaproom.is_open(h), "open at %d" % h)
	for h in [19, 4, 12]:
		assert_false(VanekTaproom.is_open(h), "closed at %d" % h)


func test_vanek_taproom_is_open_now_reads_game_clock() -> void:
	var s := FakeState.new()
	GameClock.set_time(s, 21 * 60)
	assert_true(VanekTaproom.is_open_now(s))
	GameClock.set_time(s, 12 * 60)
	assert_false(VanekTaproom.is_open_now(s))


func test_vanek_taproom_backfill_hands_over_opener_once_and_sets_flag() -> void:
	var s := _toured(false)
	assert_true(VanekTaproom.backfill_opener(s))
	assert_true(BreweryPassport.has_opener(s, VanekTaproom.BREWERY_ID))
	assert_true(bool(s.flags[VanekTaproom.FLAG_OPENER_BACKFILLED]))
	assert_eq(VanekTaproom.gate(s), VanekTaproom.GATE_OK)


func test_vanek_taproom_backfill_without_keychain_does_nothing() -> void:
	var s := _toured(false)
	s.inventory.erase(BreweryPassport.KEYCHAIN)
	assert_false(VanekTaproom.backfill_opener(s))
	assert_false(BreweryPassport.has_opener(s, VanekTaproom.BREWERY_ID))
	assert_false(s.flags.has(VanekTaproom.FLAG_OPENER_BACKFILLED))


func test_vanek_taproom_backfill_does_not_repeat() -> void:
	var s := _toured(false)
	VanekTaproom.backfill_opener(s)
	s.flags.erase(BreweryPassport.OPENER_PREFIX + VanekTaproom.BREWERY_ID)
	assert_false(VanekTaproom.backfill_opener(s))
	assert_false(BreweryPassport.has_opener(s, VanekTaproom.BREWERY_ID))


func test_vanek_taproom_backfill_skipped_when_opener_already_held() -> void:
	var s := _toured()
	assert_false(VanekTaproom.backfill_opener(s))
	assert_false(s.flags.has(VanekTaproom.FLAG_OPENER_BACKFILLED))


func test_vanek_taproom_lager_data_is_usable_in_battle_and_field_stack_9() -> void:
	var f := FileAccess.open("res://assets/data/items/consumables.json", FileAccess.READ)
	var data: Dictionary = JSON.parse_string(f.get_as_text())
	var lager: Dictionary = _find_item(data, VanekTaproom.LAGER_ID)
	assert_eq(lager.get("usable_in"), ["battle", "field"])
	assert_eq(int(lager.get("max_stack")), 9)
	assert_false(lager.get("_pending", {}).has("usable_in"))
	assert_false(lager.get("_pending", {}).has("max_stack"))


func _find_item(node, id: String) -> Dictionary:
	if node is Dictionary:
		if node.has(id) and node[id] is Dictionary:
			return node[id]
		for v in node.values():
			var r := _find_item(v, id)
			if not r.is_empty():
				return r
	elif node is Array:
		for v in node:
			var r2 := _find_item(v, id)
			if not r2.is_empty():
				return r2
	return {}
