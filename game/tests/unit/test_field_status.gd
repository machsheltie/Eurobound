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
