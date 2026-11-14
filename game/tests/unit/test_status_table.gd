extends GutTest
## StatusTable and the BattleCore/BattleUnit reads of status_effects.json (Eurobound-984j).
## Fixture entries carry real numbers; the shipped file is all null, and a separate test proves
## null is inert.


class FakeWallet:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []


func after_each() -> void:
	StatusTable.reset()


func _fixture() -> Dictionary:
	return {
		"buffy": {"display_name": "Buff-y", "scope": ["battle"], "stats": {"speed": 3, "defense": 2, "offense": 1, "grit": 4, "all": 9},
			"accuracy_steps": -2, "skip_turn_chance": 1.0, "bravado_tick": {"battle_per_turn": -2},
			"interactions": [{"with": "gloom", "rule": "suppress"}, {"with": "fizz", "rule": "cancel_into", "into": "flat"}],
			"cured_by": [{"kind": "item_subtype", "value": "drink"}, {"kind": "item_id", "value": "aspirin"}]},
		"gloom": {"stats": {"speed": -5}},
		"fizz": {},
		"flat": {"display_name": "Flat"},
	}


func _bro(statuses: Dictionary = {}) -> BattleUnit:
	return BattleUnit.from_member({"id": "bro", "display_name": "Bro", "max_hp": 30, "hp": 30, "max_bravado": 12,
		"bravado": 10, "offense": 8, "defense": 2, "speed": 5, "luck": 0, "grit": 1, "charm": 4, "skills": [],
		"statuses": statuses})


func _core(bro: BattleUnit) -> BattleCore:
	var r := RandomNumberGenerator.new()
	r.seed = 1
	var core := BattleCore.new(r)
	core.wallet = FakeWallet.new()
	core.party.append(bro)
	core.add_enemy(BattleUnit.from_enemy("foe", {"display_name": "Foe", "max_hp": 50, "offense": 1, "defense": 0,
		"speed": 1, "luck": 0, "ticket_reward": 0}, {}))
	core.start()
	return core


func test_loader_reads_the_four_shipped_entries() -> void:
	for id in ["sugar_rush_hour", "gush_locked", "crash", "cottonmouth"]:
		assert_true(StatusTable.has_entry(id), id)
	assert_eq(StatusTable.display_name("gush_locked"), "Gush-Locked")


func test_null_numbers_are_inert() -> void:
	var sts := {"sugar_rush_hour": -1, "gush_locked": 3, "crash": 2, "cottonmouth": -1}
	var bro := _bro(sts)
	assert_eq(bro.battle_speed(), BattleRules.speed(5, bro.tier()))
	assert_eq(bro.defense_stat(), 2)
	assert_eq(bro.grit_stat(), 1)
	assert_eq(StatusTable.accuracy_steps(sts), 0)
	assert_eq(StatusTable.bravado_per_turn(sts), 0)
	assert_true(StatusTable.skip_chances(sts).is_empty())
	var core := _core(bro)
	assert_false(core._turn_lost(bro))
	assert_eq(bro.bravado, 10)


## Author, Eurobound Desk 64vo-q1: "The six combat stats: offense, defense, speed, charm, luck, grit".
func test_stat_deltas_sum_and_all_covers_the_six_combat_stats() -> void:
	StatusTable.set_entries(_fixture())
	var bro := _bro({"buffy": 3})
	assert_eq(bro.battle_speed(), BattleRules.speed(5 + 3 + 9, bro.tier()))
	assert_eq(bro.defense_stat(), 2 + 2 + 9)
	assert_eq(bro.grit_stat(), 1 + 4 + 9)
	assert_eq(bro.attack_stat(false), 8.0 + 1.0 + 9.0)
	assert_eq(bro.attack_stat(true), 4.0 + 9.0)
	assert_eq(StatusTable.stat_delta({"buffy": 3}, "luck"), 9)
	# Not combat stats: "all" never reaches max HP, max Bravado or accuracy.
	assert_eq(StatusTable.stat_delta({"buffy": 3}, "max_hp"), 0)
	assert_eq(StatusTable.stat_delta({"buffy": 3}, "max_bravado"), 0)
	assert_eq(StatusTable.accuracy_steps({"buffy": 3}), -2)


func test_all_null_is_inert() -> void:
	StatusTable.set_entries({"flat": {"stats": {"all": null}}})
	for stat in StatusTable.STAT_KEYS:
		assert_eq(StatusTable.stat_delta({"flat": 2}, stat), 0, stat)


func test_suppress_hides_the_suppressed_status() -> void:
	StatusTable.set_entries(_fixture())
	# buffy suppresses gloom, so gloom's -5 speed does not count while buffy is on.
	var bro := _bro({"buffy": 3, "gloom": 3})
	assert_false(bro.has_status("gloom"))
	assert_true(bro.has_status("buffy"))
	assert_eq(bro.battle_speed(), BattleRules.speed(5 + 3 + 9, bro.tier()))   # +3 speed, +9 "all" (64vo-q1)
	bro.statuses.erase("buffy")
	assert_true(bro.has_status("gloom"))


func test_accuracy_steps_from_the_table() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(StatusTable.accuracy_steps({"buffy": 3}), -2)


func test_turn_lost_rolls_skip_and_drains_bravado() -> void:
	StatusTable.set_entries(_fixture())
	var bro := _bro({"buffy": 3})
	var core := _core(bro)
	assert_true(core._turn_lost(bro))   # skip chance 1.0
	assert_eq(bro.bravado, 8)           # -2 per turn


func test_status_name_reads_display_name_first() -> void:
	StatusTable.set_entries(_fixture())
	assert_eq(BattleCore._status_name("buffy"), "Buff-y")
	assert_eq(BattleCore._status_name("food_poisoning"), "Food Poisoning")


func test_cancel_into_swaps_the_status() -> void:
	StatusTable.set_entries(_fixture())
	var bro := _bro({"fizz": 3})
	var core := _core(bro)
	assert_true(core._apply_status(bro, "buffy", 3, 1.0))
	assert_false(bro.statuses.has("fizz"))
	assert_true(bro.statuses.has("flat"))


func test_cancel_into_with_null_target_does_nothing() -> void:
	StatusTable.set_entries({"a": {"interactions": [{"with": "b", "rule": "cancel_into", "into": null}]}, "b": {}})
	assert_true(StatusTable.cancel_into("a", {"b": 2}).is_empty())


func test_cured_by_item_matches_subtype_alcohol_and_id() -> void:
	StatusTable.set_entries(_fixture())
	assert_true(StatusTable.cured_by_item("buffy", "x", {"subtype": "drink"}))
	assert_true(StatusTable.cured_by_item("buffy", "x", {"alcohol": true}))
	assert_true(StatusTable.cured_by_item("buffy", "aspirin", {}))
	assert_false(StatusTable.cured_by_item("buffy", "x", {"subtype": "vape"}))
	assert_false(StatusTable.cured_by_item("fizz", "x", {"subtype": "drink"}))


# --- Eurobound-64vo: the eight section 8 rulings (Eurobound Desk 64vo-q1 to q8) ---------------------

func _hidden_fixture() -> Dictionary:
	return {
		"mask": {"scope": ["battle", "field"], "interactions": [{"with": "hang", "rule": "suppress", "timer": "pause"}]},
		"plain_mask": {"interactions": [{"with": "hang", "rule": "suppress"}]},
		"hang": {"scope": ["battle", "field"]},
	}


## q6, author: "Pause: the timer stops while hidden and picks up again when it returns".
func test_suppressed_timer_pauses_in_battle_and_resumes() -> void:
	StatusTable.set_entries(_hidden_fixture())
	var bro := _bro({"mask": 2, "hang": 3})
	bro.end_own_turn()
	assert_eq(bro.statuses, {"mask": 1, "hang": 3})
	bro.end_own_turn()   # the mask runs out on this tick; the hidden timer still did not move
	assert_eq(bro.statuses, {"hang": 3})
	bro.end_own_turn()
	assert_eq(bro.statuses, {"hang": 2})


func test_suppress_without_the_pause_flag_keeps_the_timer_running() -> void:
	StatusTable.set_entries(_hidden_fixture())
	var bro := _bro({"plain_mask": 5, "hang": 3})
	bro.end_own_turn()
	assert_eq(int(bro.statuses["hang"]), 2)
	assert_false(StatusTable.timer_paused("hang", {"plain_mask": 5, "hang": 3}))
	assert_true(StatusTable.timer_paused("hang", {"mask": 5, "hang": 3}))
	assert_false(StatusTable.timer_paused("hang", {"hang": 3}))


## q5, author: "Tag each ability spoken or not, one by one as abilities are written (Roast Line first)".
func test_spoken_lock_blocks_only_spoken_bravado_skills() -> void:
	StatusTable.set_entries({"dry": {"locks": ["spoken_bravado_skills"]}})
	var bro := _bro({"dry": -1})
	var core := _core(bro)
	assert_false(core.can_use_skill(bro, {"bravado_cost": 4, "spoken": true}))
	assert_true(core.can_use_skill(bro, {"bravado_cost": 4, "spoken": false}))
	assert_true(core.can_use_skill(bro, {"bravado_cost": 4}))   # untagged: not ruled spoken, not locked
	bro.statuses.erase("dry")
	assert_true(core.can_use_skill(bro, {"bravado_cost": 4, "spoken": true}))


func test_bravado_cost_lock_blocks_every_bravado_skill_and_embarrassed_still_does() -> void:
	StatusTable.set_entries({"shy": {"locks": ["bravado_cost_skills"]}})
	var bro := _bro({"shy": 2})
	var core := _core(bro)
	assert_false(core.can_use_skill(bro, {"bravado_cost": 4}))
	assert_true(core.can_use_skill(bro, {"bravado_cost": 0}))
	bro.statuses = {"embarrassed": 2}
	assert_false(core.can_use_skill(bro, {"bravado_cost": 4}))


func test_a_suppressed_status_locks_nothing() -> void:
	StatusTable.set_entries({"dry": {"locks": ["spoken_bravado_skills"]},
		"wet": {"interactions": [{"with": "dry", "rule": "suppress"}]}})
	var bro := _bro({"dry": -1, "wet": 2})
	assert_true(_core(bro).can_use_skill(bro, {"bravado_cost": 4, "spoken": true}))


## q3, author: "Stacks last longer: more Crash turns per stack; one drink per Cottonmouth stack".
func test_extend_follow_up_lasts_its_default_turns_once_per_stack() -> void:
	StatusTable.set_entries({"comedown": {"default_duration": {"battle_turns": 3}, "stack_rule": "extend"},
		"flat_comedown": {"default_duration": {"battle_turns": 3}, "stack_rule": null},
		"untuned": {"default_duration": {"battle_turns": null}, "stack_rule": "extend"}})
	var bro := _bro()
	var core := _core(bro)
	bro.due_then = [{"status": "comedown", "count": 2}, {"status": "flat_comedown", "count": 2},
		{"status": "untuned", "count": 2}]
	core._fire_due_then(bro)
	assert_eq(int(bro.statuses.get("comedown", 0)), 6)
	assert_eq(int(bro.statuses.get("flat_comedown", 0)), 3)
	assert_false(bro.statuses.has("untuned"))   # no number, nothing starts


## The shipped table carries the rulings (numbers stay null until the balancing pass).
func test_shipped_table_holds_the_64vo_rulings() -> void:
	var crash := StatusTable.entry("crash")
	assert_eq(crash.get("scope"), ["battle"])               # q2
	assert_false(Dictionary(crash["default_duration"]).has("field_steps"))
	assert_eq(crash.get("stack_rule"), "extend")            # q3
	var cotton := StatusTable.entry("cottonmouth")
	assert_eq(cotton.get("stack_rule"), "extend")           # q3
	assert_true(StatusTable.cured_by_item("cottonmouth", "x", {"subtype": "drink"}))   # q8
	assert_true(StatusTable.cured_by_item("cottonmouth", "x", {"alcohol": true}))
	assert_false(StatusTable.cured_by_item("cottonmouth", "x", {"subtype": "food"}))
	assert_true(StatusTable.timer_paused("hungover", {"sugar_rush_hour": 2, "hungover": 3}))   # q6
	assert_true(StatusTable.timer_paused("hungover", {"gush_locked": 2, "hungover": 3}))
	var thirst: Dictionary = Array(StatusTable.entry("gush_locked")["interactions"])[1]
	assert_eq(thirst.get("effect"), "double_stacks")        # q4
