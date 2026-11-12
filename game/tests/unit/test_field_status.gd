extends GutTest

var st


func before_each() -> void:
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "lord_pilsner", "display_name": "Lord Pilsner"}]


func after_each() -> void:
	st.free()


func test_field_status_apply_has_remove_list() -> void:
	FieldStatus.apply(st, "chadwick", FieldStatus.EMBARRASSED, 60)
	assert_true(FieldStatus.has(st, FieldStatus.EMBARRASSED))
	assert_true(FieldStatus.has(st, FieldStatus.EMBARRASSED, "chadwick"))
	assert_false(FieldStatus.has(st, FieldStatus.EMBARRASSED, "bradley"))
	assert_eq(FieldStatus.list(st, "chadwick"), ["embarrassed"])
	FieldStatus.remove(st, FieldStatus.EMBARRASSED, "chadwick")
	assert_false(FieldStatus.has(st, FieldStatus.EMBARRASSED))


func test_field_status_party_wide_covers_members() -> void:
	FieldStatus.apply(st, FieldStatus.PARTY, "saw_yourself", 60)
	assert_true(FieldStatus.has(st, "saw_yourself", "bradley"))


func test_field_status_clock_expiry() -> void:
	var t := GameClock.minutes(st)
	FieldStatus.apply(st, FieldStatus.PARTY, "saw_yourself", 60)
	GameClock.set_time(st, t + 59)
	assert_true(FieldStatus.has(st, "saw_yourself"))
	GameClock.set_time(st, t + 60)
	assert_false(FieldStatus.has(st, "saw_yourself"))
	FieldStatus.tick(st, 0.0)
	assert_true(st.flags[FieldStatus.KEY].is_empty())


func test_field_status_real_seconds_expiry() -> void:
	FieldStatus.apply(st, FieldStatus.PARTY, FieldStatus.GREEN_FAIRY_CONFUSION, 30, FieldStatus.UNIT_REAL)
	FieldStatus.tick(st, 29.0)
	assert_true(FieldStatus.controls_reversed(st))
	FieldStatus.tick(st, 1.5)
	assert_false(FieldStatus.controls_reversed(st))


func test_field_status_real_seconds_do_not_expire_on_clock() -> void:
	FieldStatus.apply(st, FieldStatus.PARTY, FieldStatus.GREEN_FAIRY_CONFUSION, 30, FieldStatus.UNIT_REAL)
	GameClock.set_time(st, GameClock.minutes(st) + 600)
	assert_true(FieldStatus.controls_reversed(st))


func test_field_status_nonpositive_amount_applies_nothing() -> void:
	FieldStatus.apply(st, FieldStatus.PARTY, "saw_yourself", 0)
	assert_false(FieldStatus.has(st, "saw_yourself"))


func test_field_status_save_round_trip() -> void:
	FieldStatus.apply(st, "lord_pilsner", FieldStatus.EMBARRASSED, 90)
	FieldStatus.apply(st, FieldStatus.PARTY, FieldStatus.GREEN_FAIRY_CONFUSION, 45, FieldStatus.UNIT_REAL)
	var json := JSON.stringify(st.to_dict())
	var back = load("res://core/game_state.gd").new()
	back.from_dict(JSON.parse_string(json))
	assert_true(FieldStatus.has(back, FieldStatus.EMBARRASSED, "lord_pilsner"))
	assert_true(FieldStatus.controls_reversed(back))
	FieldStatus.tick(back, 46.0)
	assert_false(FieldStatus.controls_reversed(back))
	back.free()


func test_field_status_reversed_input() -> void:
	assert_eq(PlayerController.reversed_input(Vector2(1, -0.5), true), Vector2(-1, 0.5))
	assert_eq(PlayerController.reversed_input(Vector2(1, -0.5), false), Vector2(1, -0.5))


func test_field_status_reversed_walk_goes_the_other_way() -> void:
	var fwd := PlayerController.move_direction(Vector2(0, -1), null)
	var rev := PlayerController.move_direction(PlayerController.reversed_input(Vector2(0, -1), true), null)
	assert_almost_eq(fwd.z, -rev.z, 0.001)


func _rng(s: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = s
	return r


func test_field_status_confusion_length_is_random_within_doc_range() -> void:
	var seen := {}
	for s in range(40):
		var s2 = load("res://core/game_state.gd").new()
		s2.flags = {}
		FieldStatus.apply_confusion(s2, "chadwick", _rng(s))
		var left: float = s2.flags[FieldStatus.KEY]["chadwick"][FieldStatus.GREEN_FAIRY_CONFUSION]["left"]
		assert_between(left, 30.0, 180.0)
		seen[left] = true
		s2.free()
	assert_gt(seen.size(), 1)


func test_field_status_confusion_targets_one_bro() -> void:
	FieldStatus.apply_confusion(st, "chadwick", _rng(1))
	assert_true(FieldStatus.has(st, FieldStatus.GREEN_FAIRY_CONFUSION, "chadwick"))
	assert_false(FieldStatus.has(st, FieldStatus.GREEN_FAIRY_CONFUSION, "bradley"))


func test_field_status_long_statuses_apply_to_one_bro() -> void:
	FieldStatus.apply_saw_yourself(st, "bradley")
	FieldStatus.apply_existentially_rested(st, "bradley")
	assert_true(FieldStatus.has(st, FieldStatus.SAW_YOURSELF, "bradley"))
	assert_true(FieldStatus.has(st, FieldStatus.EXISTENTIALLY_RESTED, "bradley"))
	assert_false(FieldStatus.has(st, FieldStatus.SAW_YOURSELF, "chadwick"))
	assert_false(FieldStatus.has(st, FieldStatus.EXISTENTIALLY_RESTED, "chadwick"))


func test_field_status_long_statuses_last_doc_minutes() -> void:
	var t := GameClock.minutes(st)
	FieldStatus.apply_saw_yourself(st, "bradley")
	FieldStatus.apply_existentially_rested(st, "bradley")
	GameClock.set_time(st, t + 60)
	assert_false(FieldStatus.has(st, FieldStatus.SAW_YOURSELF, "bradley"))
	assert_true(FieldStatus.has(st, FieldStatus.EXISTENTIALLY_RESTED, "bradley"))


func test_field_status_reality_anchor_blocks_about_ten_percent() -> void:
	FieldStatus.grant_reality_anchor(st, "chadwick")
	var rng := _rng(7)
	var blocked := 0
	for i in range(1000):
		FieldStatus.remove(st, FieldStatus.GREEN_FAIRY_CONFUSION)
		if not FieldStatus.apply_confusion(st, "chadwick", rng):
			blocked += 1
	assert_between(blocked, 70, 130)


func test_field_status_confusion_without_anchor_is_never_blocked() -> void:
	var rng := _rng(7)
	for i in range(200):
		assert_true(FieldStatus.apply_confusion(st, "bradley", rng))


func test_field_status_anchor_is_per_bro() -> void:
	FieldStatus.grant_reality_anchor(st, "chadwick")
	assert_true(FieldStatus.has_reality_anchor(st, "chadwick"))
	assert_false(FieldStatus.has_reality_anchor(st, "bradley"))


func test_field_status_choice_unchanged_without_confusion() -> void:
	assert_eq(FieldStatus.choice_index(st, 2, 4, _rng(3)), 2)


func test_field_status_choice_randomised_under_confusion() -> void:
	FieldStatus.apply(st, "chadwick", FieldStatus.GREEN_FAIRY_CONFUSION, 60, FieldStatus.UNIT_REAL)
	var rng := _rng(3)
	var seen := {}
	for i in range(60):
		var k := FieldStatus.choice_index(st, 0, 4, rng)
		assert_between(k, 0, 3)
		seen[k] = true
	assert_gt(seen.size(), 1)


func test_field_status_dialogue_box_choose_randomised_under_confusion() -> void:
	FieldStatus.apply(st, "chadwick", FieldStatus.GREEN_FAIRY_CONFUSION, 60, FieldStatus.UNIT_REAL)
	var box := DialogueBox.new()
	box.field_state = st
	box.choice_rng = _rng(5)
	add_child_autofree(box)
	var seen := {}
	for i in range(30):
		box.choose(["a", "b", "c"])
		box.press("interact")
		seen[box.cursor] = true
	assert_gt(seen.size(), 1)


func test_field_status_battle_statuses_map_and_skip_unmapped() -> void:
	FieldStatus.apply(st, "chadwick", FieldStatus.GREEN_FAIRY_CONFUSION, 60, FieldStatus.UNIT_REAL)
	FieldStatus.apply(st, "chadwick", FieldStatus.EMBARRASSED, 60)
	FieldStatus.apply_saw_yourself(st, "chadwick")
	var b := FieldStatus.battle_statuses(st, "chadwick")
	assert_eq(b, {"confused": 2, "embarrassed": 2})
	assert_eq(FieldStatus.battle_statuses(st, "bradley"), {})


func test_field_status_battle_unit_carries_field_statuses() -> void:
	FieldStatus.apply(st, "chadwick", FieldStatus.GREEN_FAIRY_CONFUSION, 60, FieldStatus.UNIT_REAL)
	var u := BattleUnit.from_member({"id": "chadwick", "max_hp": 10, "statuses": FieldStatus.battle_statuses(st, "chadwick")})
	assert_true(u.has_status("confused"))


func test_field_status_embarrassed_lasts_60_game_minutes() -> void:
	var t := GameClock.minutes(st)
	FieldStatus.apply_embarrassed(st, "chadwick", FieldStatus.EMB_SOURCE_CLOSET_TIMER)
	GameClock.set_time(st, t + 59)
	assert_true(FieldStatus.has(st, FieldStatus.EMBARRASSED, "chadwick"))
	GameClock.set_time(st, t + 60)
	assert_false(FieldStatus.has(st, FieldStatus.EMBARRASSED, "chadwick"))


func test_field_status_embarrassed_enters_battle_for_two_turns() -> void:
	FieldStatus.apply_embarrassed(st, "chadwick", FieldStatus.EMB_SOURCE_HOSTEL_WITNESS)
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {"embarrassed": 2})


func test_field_status_embarrassed_accepts_the_three_sources() -> void:
	assert_eq(FieldStatus.EMBARRASSED_SOURCES.size(), 3)
	for src in FieldStatus.EMBARRASSED_SOURCES:
		FieldStatus.remove(st, FieldStatus.EMBARRASSED)
		assert_true(FieldStatus.apply_embarrassed(st, "bradley", src))
		assert_true(FieldStatus.has(st, FieldStatus.EMBARRASSED, "bradley"))


func test_field_status_embarrassed_unknown_source_applies_nothing() -> void:
	assert_false(FieldStatus.apply_embarrassed(st, "bradley", "bad_source"))
	assert_false(FieldStatus.has(st, FieldStatus.EMBARRASSED))


func test_field_status_embarrassed_resistance_shortens_ten_percent_per_point() -> void:
	var t := GameClock.minutes(st)
	FieldStatus.apply_embarrassed(st, "bradley", FieldStatus.EMB_SOURCE_QTE_FAIL, 2.0)
	GameClock.set_time(st, t + 47)
	assert_true(FieldStatus.has(st, FieldStatus.EMBARRASSED, "bradley"))
	GameClock.set_time(st, t + 48)
	assert_false(FieldStatus.has(st, FieldStatus.EMBARRASSED, "bradley"))


func test_field_status_embarrassed_full_resistance_applies_nothing() -> void:
	assert_false(FieldStatus.apply_embarrassed(st, "bradley", FieldStatus.EMB_SOURCE_QTE_FAIL, 10.0))
	assert_false(FieldStatus.has(st, FieldStatus.EMBARRASSED))


func test_field_status_confusion_enters_battle_for_two_turns() -> void:
	FieldStatus.apply(st, "chadwick", FieldStatus.GREEN_FAIRY_CONFUSION, 60, FieldStatus.UNIT_REAL)
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {"confused": 2})


func test_field_status_long_statuses_stay_out_of_battle() -> void:
	FieldStatus.apply_saw_yourself(st, "chadwick")
	FieldStatus.apply_existentially_rested(st, "chadwick")
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {})
