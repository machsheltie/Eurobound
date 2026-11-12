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


func test_stat_deltas_sum_and_all_is_ignored() -> void:
	StatusTable.set_entries(_fixture())
	var bro := _bro({"buffy": 3})
	assert_eq(bro.battle_speed(), BattleRules.speed(5 + 3, bro.tier()))
	assert_eq(bro.defense_stat(), 4)
	assert_eq(bro.grit_stat(), 5)
	assert_eq(bro.attack_stat(false), 9.0)
	assert_eq(bro.attack_stat(true), 4.0)


func test_suppress_hides_the_suppressed_status() -> void:
	StatusTable.set_entries(_fixture())
	# buffy suppresses gloom, so gloom's -5 speed does not count while buffy is on.
	var bro := _bro({"buffy": 3, "gloom": 3})
	assert_false(bro.has_status("gloom"))
	assert_true(bro.has_status("buffy"))
	assert_eq(bro.battle_speed(), BattleRules.speed(5 + 3, bro.tier()))
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
