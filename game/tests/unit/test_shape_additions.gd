extends GutTest
## The five data-shape additions for the ruled Grist and Genever values (Eurobound-cvkq; author,
## Eurobound Desk Eurobound-cvkq-q1, 2026-11-15: "Approve as proposed";
## docs/superpowers/specs/2026-11-14-grist-genever-data-shape-additions-proposal.md §3):
## accuracy_points, stats_pct, intoxicant.also, stack_cap, shortens_status.
## Fixture entries prove the reading rules; the shipped-data tests pin the approved numbers.


class FakeWallet:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []


class FakeRepo:
	var d: Dictionary

	func _init(items: Dictionary) -> void:
		d = items

	func get_item(id: String) -> Dictionary:
		return d.get(id, {})


const T0 := 600

var st


func before_each() -> void:
	StatusTable.reset()
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "chadwick", "display_name": "Chadwick", "hp": 10, "max_hp": 30, "bravado": 5, "max_bravado": 10}]
	GameClock.set_time(st, T0)


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _fixture() -> Dictionary:
	return {
		"aim_down": {"display_name": "Aim Down", "scope": ["battle"], "accuracy_points": -95},
		"aim_up": {"display_name": "Aim Up", "scope": ["battle"], "accuracy_steps": 11},
		"aim_null": {"display_name": "Aim Null", "accuracy_points": null},
		"quick": {"display_name": "Quick", "scope": ["battle", "field"],
			"default_duration": {"battle_turns": 3, "field_steps": 120}, "stack_rule": "refresh",
			"stats_pct": {"speed": {"pct": 15, "min_points": 1}}},
		"slow": {"display_name": "Slow", "stats_pct": {"speed": {"pct": -20}}},
		"flat": {"display_name": "Flat", "stats": {"speed": 3}},
		"wobble": {"display_name": "Wobble", "scope": ["field"], "default_duration": {"field_steps": 200},
			"stack_rule": "extend", "stack_cap": {"field_steps": 800}},
		"shake": {"display_name": "Shake", "scope": ["battle", "field"],
			"default_duration": {"battle_turns": 3, "field_steps": 120}, "stack_rule": "extend",
			"stack_cap": {"battle_turns": 12, "field_steps": 480}},
		"after": {"display_name": "After", "scope": ["battle", "field"],
			"default_duration": {"battle_turns": 2, "field_steps": 50}},
		"haze": {"display_name": "Haze", "scope": ["field"], "default_duration": {"clock_minutes": 90},
			"stack_rule": "extend", "stack_cap": {"clock_minutes": 180}, "then": {"status": "after", "stacks": false}},
		"loose": {"display_name": "Loose", "scope": ["field"], "default_duration": {"clock_minutes": 90},
			"stack_rule": "extend"},
	}


func _bro(statuses: Dictionary = {}, speed: int = 5) -> BattleUnit:
	return BattleUnit.from_member({"id": "bro", "display_name": "Bro", "max_hp": 30, "hp": 30, "max_bravado": 12,
		"bravado": 10, "offense": 8, "defense": 2, "speed": speed, "luck": 0, "grit": 1, "charm": 4, "skills": [],
		"statuses": statuses})


func _core(items: Dictionary = {}, statuses: Dictionary = {}) -> BattleCore:
	var r := RandomNumberGenerator.new()
	r.seed = 1
	var core := BattleCore.new(r)
	core.wallet = FakeWallet.new()
	for id in items.keys():
		core.wallet.inventory[id] = 9
	core.items = items
	core.party.append(_bro(statuses))
	core.add_enemy(BattleUnit.from_enemy("foe", {"display_name": "Foe", "max_hp": 500, "offense": 1, "defense": 0,
		"speed": 1, "luck": 0, "ticket_reward": 0}, {}))
	core.start()
	core.tick(5.0)
	core.step()
	return core


func _use(core: BattleCore, id: String) -> bool:
	core.minor_used = false
	return core.use_item(id, core.party[0])


func _drink(status: String, turns: Variant, steps: Variant, rule: String, also: Array = []) -> Dictionary:
	var item := {"display_name": "Drink", "heal_hp": 0, "heal_bravado": 0,
		"intoxicant": {"status": status, "duration": {"battle_turns": turns, "field_steps": steps, "ends_on_rest": true},
			"stack_rule": rule}}
	if not also.is_empty():
		item["intoxicant"]["also"] = also
	return item


func _food(rows: Array) -> Dictionary:
	return {"display_name": "Food", "heal_hp": 1, "heal_bravado": 0, "shortens_status": rows}


func _row(target: String, id: String) -> Dictionary:
	return Dictionary(Dictionary(st.flags.get(FieldStatus.KEY, {})).get(target, {})).get(id, {})


# --- 3.1 accuracy_points ------------------------------------------------------------------------

func test_accuracy_points_sums_live_statuses_and_null_adds_nothing() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.accuracy_points({"aim_down": 3, "aim_null": 3, "flat": 3}), -95)
	assert_eq(StatusTable.accuracy_points({}), 0)


func test_accuracy_points_hit_roll_is_95_plus_9_per_step_plus_points() -> void:
	# Arrange: 95 + 0 steps - 95 points = 0%: every swing misses.
	StatusTable.set_entries(_fixture())
	var core := _core({}, {"aim_down": 99})
	# Act / Assert
	for i in 20:
		assert_false(core._hit(core.party[0], core.enemies[0], 1.0, false, 0)["hit"], "0% never lands")


func test_accuracy_points_add_to_steps_and_neither_replaces_the_other() -> void:
	# Arrange: 95 + 9 x 11 steps - 95 points = 99%+: steps still count beside the points.
	StatusTable.set_entries(_fixture())
	var core := _core({}, {"aim_down": 99, "aim_up": 99})
	var hits := 0
	# Act
	for i in 40:
		if core._hit(core.party[0], core.enemies[0], 1.0, false, 0)["hit"]:
			hits += 1
	# Assert: 99% over 40 swings with seed 1.
	assert_gt(hits, 35)


func test_accuracy_points_the_shakes_is_minus_15_points_and_no_steps() -> void:
	assert_eq(StatusTable.accuracy_points({"the_shakes": 3}), -15)
	assert_eq(StatusTable.accuracy_steps({"the_shakes": 3}), 0)


# --- 3.2 stats_pct ------------------------------------------------------------------------------

func test_stats_pct_is_a_rounded_share_of_the_base_stat_with_halves_up() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.stat_delta({"quick": 3}, "speed", 5), 1, "0.75 rounds to 1")
	assert_eq(StatusTable.stat_delta({"quick": 3}, "speed", 7), 1, "1.05")
	assert_eq(StatusTable.stat_delta({"quick": 3}, "speed", 8), 1, "1.2")
	assert_eq(StatusTable.stat_delta({"quick": 3}, "speed", 10), 2, "1.5 rounds up")
	assert_eq(StatusTable.stat_delta({"quick": 3}, "speed", 20), 3)


func test_stats_pct_is_never_smaller_than_min_points() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.stat_delta({"quick": 3}, "speed", 2), 1, "0.3 rounds to 0, the floor is +1")


func test_stats_pct_negative_pct_is_a_penalty_and_absent_min_points_is_zero() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.stat_delta({"slow": 3}, "speed", 10), -2)
	assert_eq(StatusTable.stat_delta({"slow": 3}, "speed", 1), 0, "0.2 rounds to 0 and there is no floor")


func test_stats_pct_adds_to_flat_deltas_and_reads_only_its_own_stat() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.stat_delta({"quick": 3, "flat": 3}, "speed", 10), 5)
	assert_eq(StatusTable.stat_delta({"quick": 3}, "offense", 10), 0)


func test_stats_pct_without_a_base_stat_adds_nothing() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.stat_delta({"quick": 3}, "speed"), 0)


func test_stats_pct_battle_speed_reads_the_sheet_speed_before_other_statuses() -> void:
	# Arrange: sheet Speed 10 with a flat +3 beside the 15%: the share is of 10, not of 13.
	StatusTable.set_entries(_fixture())
	var bro := _bro({"quick": 3, "flat": 3}, 10)
	# Act / Assert
	assert_eq(bro.battle_speed(), BattleRules.speed(10 + 2 + 3, bro.tier()))


func test_stats_pct_grist_speed_buff_is_plus_1_for_all_three_bros() -> void:
	for speed in [5, 7, 8]:
		assert_eq(StatusTable.stat_delta({"wobbly_windmill_speed": 3}, "speed", speed), 1, "Speed %d" % speed)


# --- 3.3 intoxicant.also ------------------------------------------------------------------------

func _also_row() -> Dictionary:
	return {"status": "quick", "duration": {"battle_turns": 3, "field_steps": 120, "ends_on_rest": true},
		"stack_rule": "refresh"}


func test_also_field_use_applies_every_row_with_its_own_duration() -> void:
	StatusTable.set_entries(_fixture())
	assert_true(Intoxicant.apply_field(st, "chadwick", _drink("wobble", null, 200, "extend", [_also_row()])))
	assert_eq(int(_row("chadwick", "wobble")["left"]), 200)
	assert_false(_row("chadwick", "wobble").has("turns"))
	assert_eq(int(_row("chadwick", "quick")["left"]), 120)
	assert_eq(int(_row("chadwick", "quick")["turns"]), 3)


func test_also_rows_keep_their_own_stack_rule() -> void:
	# Arrange
	StatusTable.set_entries(_fixture())
	var item := _drink("wobble", null, 200, "extend", [_also_row()])
	Intoxicant.apply_field(st, "chadwick", item)
	FieldStatus.add_steps(st, 100)
	# Act: a second serving extends the main status and refreshes the row.
	Intoxicant.apply_field(st, "chadwick", item)
	# Assert
	assert_eq(int(_row("chadwick", "wobble")["left"]), 300)
	assert_eq(int(_row("chadwick", "quick")["left"]), 120)


func test_also_rows_are_independent_of_the_main_status() -> void:
	# Arrange: the row runs out first; the main status stays.
	StatusTable.set_entries(_fixture())
	Intoxicant.apply_field(st, "chadwick", _drink("wobble", null, 200, "extend", [_also_row()]))
	# Act
	FieldStatus.add_steps(st, 120)
	# Assert
	assert_false(FieldStatus.has(st, "quick", "chadwick"))
	assert_true(FieldStatus.has(st, "wobble", "chadwick"))


func test_also_row_still_lands_when_the_main_status_is_inert() -> void:
	StatusTable.set_entries(_fixture())
	assert_true(Intoxicant.apply_field(st, "chadwick", _drink("flat", null, null, "extend", [_also_row()])))
	assert_true(FieldStatus.has(st, "quick", "chadwick"))


func test_also_battle_use_puts_the_row_on_the_unit_and_the_field_only_main_on_the_field() -> void:
	# Arrange
	StatusTable.set_entries(_fixture())
	var core := _core({"grist": _drink("wobble", null, 200, "extend", [_also_row()])})
	# Act
	assert_true(_use(core, "grist"))
	# Assert: the Speed row runs in the fight; the field-only penalty waits outside, once.
	assert_eq(int(core.party[0].statuses["quick"]), 3)
	assert_false(core.party[0].statuses.has("wobble"))
	var rows: Dictionary = core.wallet.flags[FieldStatus.KEY]["bro"]
	assert_eq(int(rows["wobble"]["left"]), 200)
	assert_false(rows.has("quick"), "the row is applied once, in the fight")


func test_also_shipped_grist_applies_the_navigation_penalty_and_the_speed_buff() -> void:
	# Arrange
	var grist: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(
			"res://assets/data/items/consumables.json"))["consumables"]["beer_wobbly_windmill_brewery"]
	st.inventory = {"grist": 1}
	# Act
	assert_true(st.use_item("grist", FakeRepo.new({"grist": grist})))
	# Assert
	assert_eq(int(_row("chadwick", "wobbly_windmill_navigation")["left"]), 200)
	assert_eq(int(_row("chadwick", "wobbly_windmill_speed")["left"]), 120)
	assert_eq(int(_row("chadwick", "wobbly_windmill_speed")["turns"]), 3)


# --- 3.4 stack_cap ------------------------------------------------------------------------------

func test_stack_cap_reads_the_table_and_absent_means_no_cap() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.stack_cap("shake", "battle_turns"), 12)
	assert_eq(StatusTable.stack_cap("shake", "field_steps"), 480)
	assert_eq(StatusTable.stack_cap("shake", "clock_minutes"), 0)
	assert_eq(StatusTable.stack_cap("loose", "clock_minutes"), 0)


func test_stack_cap_field_extend_stops_at_the_cap_on_both_counters() -> void:
	StatusTable.set_entries(_fixture())
	for i in 5:
		Intoxicant.apply_field(st, "chadwick", _drink("shake", 3, 120, "extend"))
	assert_eq(int(_row("chadwick", "shake")["left"]), 480)
	assert_eq(int(_row("chadwick", "shake")["turns"]), 12)


func test_stack_cap_limits_what_is_left_not_the_total_served() -> void:
	# Arrange: four servings, then half of it walked off.
	StatusTable.set_entries(_fixture())
	for i in 4:
		Intoxicant.apply_field(st, "chadwick", _drink("shake", 3, 120, "extend"))
	FieldStatus.add_steps(st, 240)
	# Act: he can drink back up.
	Intoxicant.apply_field(st, "chadwick", _drink("shake", 3, 120, "extend"))
	# Assert
	assert_eq(int(_row("chadwick", "shake")["left"]), 360)


func test_stack_cap_battle_extend_stops_at_the_turn_cap() -> void:
	StatusTable.set_entries(_fixture())
	var core := _core({"gin": _drink("shake", 3, 120, "extend")})
	for i in 5:
		_use(core, "gin")
	assert_eq(int(core.party[0].statuses["shake"]), 12)


func test_stack_cap_clock_extend_stops_at_the_minute_cap() -> void:
	StatusTable.set_entries(_fixture())
	for i in 3:
		FieldStatus.apply_from_table(st, "chadwick", "haze")
	assert_eq(int(_row("chadwick", "haze")["until"]), T0 + 180)


func test_stack_cap_absent_leaves_an_extend_unbounded() -> void:
	StatusTable.set_entries(_fixture())
	for i in 3:
		FieldStatus.apply_from_table(st, "chadwick", "loose")
	assert_eq(int(_row("chadwick", "loose")["until"]), T0 + 270)


func test_stack_cap_shipped_values_are_the_approved_numbers() -> void:
	assert_eq(StatusTable.stack_cap("the_shakes", "battle_turns"), 12)
	assert_eq(StatusTable.stack_cap("the_shakes", "field_steps"), 480)
	assert_eq(StatusTable.stack_cap("wobbly_windmill_navigation", "field_steps"), 800)
	assert_eq(StatusTable.stack_cap("space_cake_gamble", "clock_minutes"), 180)


# --- 3.5 shortens_status ------------------------------------------------------------------------

func test_shortens_status_takes_the_amount_off_each_counter() -> void:
	# Arrange
	StatusTable.set_entries(_fixture())
	FieldStatus.apply_steps(st, "chadwick", "shake", 240, 6)
	st.inventory = {"fries": 1}
	# Act
	st.use_item("fries", FakeRepo.new({"fries": _food([{"status": "shake", "battle_turns": 2, "field_steps": 80}])}))
	# Assert
	assert_eq(int(_row("chadwick", "shake")["left"]), 160)
	assert_eq(int(_row("chadwick", "shake")["turns"]), 4)


func test_shortens_status_ends_the_status_at_zero_and_the_follow_up_still_fires() -> void:
	# Arrange: one serving left, with a follow-up on the row.
	StatusTable.set_entries(_fixture())
	FieldStatus.apply_steps(st, "chadwick", "shake", 80, 2)
	st.flags[FieldStatus.KEY]["chadwick"]["shake"]["then"] = {"status": "after", "stacks_count": 1}
	# Act
	FieldStatus.cure_by_item(st, "chadwick", "fries", _food([{"status": "shake", "battle_turns": 2, "field_steps": 80}]))
	# Assert: food shortens the wait, it does not cancel the bill.
	assert_false(FieldStatus.has(st, "shake", "chadwick"))
	assert_true(FieldStatus.has(st, "after", "chadwick"))


func test_shortens_status_cuts_a_clock_row_and_its_table_follow_up_fires() -> void:
	# Arrange
	StatusTable.set_entries(_fixture())
	FieldStatus.apply_from_table(st, "chadwick", "haze")
	var food := _food([{"status": "haze", "clock_minutes": 60}])
	# Act / Assert
	FieldStatus.cure_by_item(st, "chadwick", "pie", food)
	assert_eq(int(_row("chadwick", "haze")["until"]), T0 + 30)
	FieldStatus.cure_by_item(st, "chadwick", "pie", food)
	assert_false(FieldStatus.has(st, "haze", "chadwick"))
	assert_true(FieldStatus.has(st, "after", "chadwick"))


func test_shortens_status_leaves_other_statuses_and_missing_counters_alone() -> void:
	# Arrange
	StatusTable.set_entries(_fixture())
	FieldStatus.apply_steps(st, "chadwick", "wobble", 200)
	FieldStatus.apply_steps(st, "chadwick", "shake", 240, 6)
	# Act: the row names only steps for Shake.
	FieldStatus.cure_by_item(st, "chadwick", "pie", _food([{"status": "shake", "field_steps": 40}]))
	# Assert
	assert_eq(int(_row("chadwick", "wobble")["left"]), 200)
	assert_eq(int(_row("chadwick", "shake")["left"]), 200)
	assert_eq(int(_row("chadwick", "shake")["turns"]), 6)


func test_shortens_status_in_battle_takes_turns_off_and_fires_the_follow_up_at_zero() -> void:
	# Arrange
	StatusTable.set_entries(_fixture())
	var core := _core({"fries": _food([{"status": "shake", "battle_turns": 2, "field_steps": 80}])}, {"shake": 3})
	core.party[0].then_pending["shake"] = {"status": "after", "count": 1}
	# Act / Assert
	_use(core, "fries")
	assert_eq(int(core.party[0].statuses["shake"]), 1)
	_use(core, "fries")
	assert_false(core.party[0].statuses.has("shake"))
	assert_eq(int(core.party[0].statuses["after"]), 2)


func test_shortens_status_in_battle_does_nothing_to_a_bro_without_the_status() -> void:
	StatusTable.set_entries(_fixture())
	var core := _core({"fries": _food([{"status": "shake", "battle_turns": 2}])})
	assert_true(_use(core, "fries"))
	assert_false(core.party[0].statuses.has("shake"))
