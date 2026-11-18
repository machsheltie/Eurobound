extends GutTest
## A battle-only follow-up that fires outside a fight waits for the next one (Eurobound-2uji).
## Author, Eurobound Desk 64vo-q2: "Battle only: Crash waits for the next fight and runs its turns
## there". Fixture numbers, plus one test of the shipped Crash's approved 3 turns (Eurobound-vdrt).

var st


func before_each() -> void:
	StatusTable.set_entries({
		"rush": {"display_name": "Rush", "scope": ["battle", "field"],
			"default_duration": {"battle_turns": 2, "field_steps": 80, "ends_on_rest": true, "until_cured": false}},
		"crash": {"display_name": "Crash", "scope": ["battle"], "stack_rule": "extend",
			"default_duration": {"battle_turns": 3, "ends_on_rest": null, "until_cured": false}},
		"crash_rest": {"scope": ["battle"], "stack_rule": "extend",
			"default_duration": {"battle_turns": 3, "ends_on_rest": true, "until_cured": false}},
		"crash_flat": {"scope": ["battle"],
			"default_duration": {"battle_turns": 3, "ends_on_rest": null, "until_cured": false}},
		"crash_null": {"scope": ["battle"], "stack_rule": "extend",
			"default_duration": {"battle_turns": null, "ends_on_rest": null, "until_cured": false}},
		"munch": {"scope": ["field"], "default_duration": {"field_steps": 50}},
	})
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "chadwick", "display_name": "Chadwick", "hp": 30, "max_hp": 30, "bravado": 5,
		"max_bravado": 10}]


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _cake(then_id: String = "crash") -> Dictionary:
	return {"display_name": "Cake", "subtype": "snack", "heal_hp": 0, "heal_bravado": 0,
		"intoxicant": {"status": "rush", "duration": {"battle_turns": 2, "field_steps": 80, "ends_on_rest": true},
			"stack_rule": "extend", "then": {"status": then_id, "stacks": true}}}


func _eat(times: int = 1, then_id: String = "crash") -> void:
	for i in times:
		Intoxicant.apply_field(st, "chadwick", _cake(then_id))


func test_waiting_status_battle_only_then_waits_when_its_status_ends_on_the_overworld() -> void:
	_eat()
	FieldStatus.add_steps(st, 80)
	assert_false(FieldStatus.has(st, "rush"))
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 3)
	assert_false(FieldStatus.has(st, "crash"), "it is waiting, not running, on the overworld")
	assert_false(FieldStatus.list(st, "chadwick").has("crash"))


func test_waiting_status_lasts_its_default_turns_once_per_stack() -> void:
	_eat(2)
	FieldStatus.add_steps(st, 160)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 6)


func test_waiting_status_without_stack_rule_extend_lasts_its_default_turns_once() -> void:
	_eat(2, "crash_flat")
	FieldStatus.add_steps(st, 160)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash_flat"), 3)


func test_waiting_status_a_later_firing_adds_its_turns_under_extend() -> void:
	_eat()
	FieldStatus.add_steps(st, 80)
	_eat()
	FieldStatus.add_steps(st, 80)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 6)


func test_waiting_status_is_saved_when_its_status_ends_at_a_rest() -> void:
	_eat()
	GameClock.rest(st)
	assert_false(FieldStatus.has(st, "rush"), "ends_on_rest true")
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 3)


func test_waiting_status_a_rest_fires_no_field_follow_up() -> void:
	_eat(1, "munch")
	GameClock.rest(st)
	assert_false(FieldStatus.has(st, "rush"))
	assert_false(FieldStatus.has(st, "munch"), "only a battle-only follow-up is held at a rest")


func test_waiting_status_walking_and_the_clock_never_count_it_down() -> void:
	_eat()
	FieldStatus.add_steps(st, 80)
	FieldStatus.add_steps(st, 100000)
	FieldStatus.add_metres(st, 5000.0)
	FieldStatus.tick(st, 100000.0)
	GameClock.set_time(st, GameClock.minutes(st) + 5000)
	FieldStatus.settle(st)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 3)


func test_waiting_status_carried_in_status_keeps_its_follow_up_for_the_fight() -> void:
	# Arrange: Rush is live with its battle turns and a Crash follow-up (Eurobound-yrib).
	_eat()
	# Act
	var pending := FieldStatus.battle_then_pending(st, "chadwick")
	var member: Dictionary = st.party[0].duplicate()
	member["statuses"] = FieldStatus.battle_statuses(st, "chadwick")
	var u := BattleUnit.from_member(member)
	u.then_pending.merge(pending)
	u.end_own_turn()
	u.end_own_turn()
	# Assert: Rush ran out inside the fight and its follow-up is due there.
	assert_eq(pending, {"rush": {"status": "crash", "count": 1}})
	assert_false(u.has_status("rush"))
	assert_eq(u.due_then.size(), 1)
	assert_eq(String(u.due_then[0]["status"]), "crash")


func test_waiting_status_lasting_status_carries_no_follow_up() -> void:
	# Arrange: nothing eaten, so no carried status with turns.
	# Act / Assert
	assert_eq(FieldStatus.battle_then_pending(st, "chadwick"), {})


func test_waiting_status_the_next_fight_carries_it_in_with_its_turns() -> void:
	_eat(2)
	FieldStatus.add_steps(st, 160)
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {"crash": 6})
	var member: Dictionary = st.party[0].duplicate()
	member["statuses"] = FieldStatus.battle_statuses(st, "chadwick")
	var u := BattleUnit.from_member(member)
	assert_true(u.has_status("crash"))
	u.end_own_turn()
	assert_eq(u.statuses["crash"], 5, "it runs its turns in the fight")


func test_waiting_status_write_back_keeps_the_remainder_and_ends_at_zero() -> void:
	_eat()
	FieldStatus.add_steps(st, 80)
	FieldStatus.write_back_battle(st, "chadwick", {"crash": 1})
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 1)
	FieldStatus.write_back_battle(st, "chadwick", {"crash": 1})
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 1)
	FieldStatus.write_back_battle(st, "chadwick", {})
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 0)
	assert_false(Dictionary(st.flags[FieldStatus.KEY].get("chadwick", {})).has("crash"))


func test_waiting_status_write_back_never_grows_the_row() -> void:
	_eat()
	FieldStatus.add_steps(st, 80)
	FieldStatus.write_back_battle(st, "chadwick", {"crash": 9})
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 3)


func test_waiting_status_fired_at_write_back_is_not_eaten_by_the_same_write_back() -> void:
	# Arrange: a Crash already waiting (3), and a Rush whose battle turns run out in this fight.
	_eat()
	FieldStatus.add_steps(st, 80)
	_eat()
	# Act: the bro leaves the fight with 1 Crash turn left and no Rush.
	FieldStatus.write_back_battle(st, "chadwick", {"crash": 1})
	# Assert: 1 left over, plus the new Crash's 3.
	assert_false(FieldStatus.has(st, "rush"))
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 4)


func test_waiting_status_survives_save_and_load() -> void:
	_eat(2)
	FieldStatus.add_steps(st, 160)
	var back = load("res://core/game_state.gd").new()
	back.from_dict(JSON.parse_string(JSON.stringify(st.to_dict())))
	assert_eq(FieldStatus.waiting_turns(back, "chadwick", "crash"), 6)
	assert_eq(FieldStatus.battle_statuses(back, "chadwick"), {"crash": 6})
	FieldStatus.tick(back, 1.0)
	assert_eq(FieldStatus.waiting_turns(back, "chadwick", "crash"), 6)
	back.free()


func test_waiting_status_null_battle_turns_start_nothing() -> void:
	_eat(1, "crash_null")
	FieldStatus.add_steps(st, 80)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash_null"), 0)
	assert_true(st.flags[FieldStatus.KEY].is_empty())


## Shipped Crash: 3 turns, approved 2026-11-16 (Eurobound Desk Eurobound-vdrt-q2, "Approve: write
## it into the live status data"). A null length is still inert (crash_null, above).
func test_waiting_status_shipped_crash_waits_its_approved_three_turns() -> void:
	# Arrange
	StatusTable.reset()
	# Act
	var applied := FieldStatus.apply_from_table(st, "chadwick", "crash")
	# Assert
	assert_eq(StatusTable.entry("crash").get("scope"), ["battle"])
	assert_true(StatusTable.battle_only("crash"))
	assert_true(applied)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 3)
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {"crash": 3})


func test_waiting_status_a_rest_follows_the_table_ends_on_rest() -> void:
	_eat()
	FieldStatus.add_steps(st, 80)
	_eat(1, "crash_rest")
	FieldStatus.add_steps(st, 80)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash_rest"), 3)
	GameClock.rest(st)
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 3, "ends_on_rest null: it stays")
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash_rest"), 0, "ends_on_rest true: a rest ends it")


## Eurobound-ny6e, ruled in Eurobound-jck4 (Eurobound Desk Eurobound-jck4-q1, 2026-11-15): "They are
## dropped: the Crash ends with the fight". A Crash that starts inside a fight (Rush taken and run
## out there) has no field row, so what it has left when the fight ends is not carried on.
func test_waiting_status_a_crash_that_starts_mid_fight_is_dropped_when_the_fight_ends() -> void:
	# Arrange: a fight on the real state; Chadwick takes Cake (Rush 2 turns, then Crash 3 turns).
	var core := BattleCore.new(RandomNumberGenerator.new())
	core.wallet = st
	core.party.append(BattleUnit.from_member(st.party[0].duplicate()))
	core.add_enemy(BattleUnit.from_enemy("foe", {"display_name": "Foe", "max_hp": 50, "offense": 1,
		"defense": 0, "speed": 1, "luck": 0, "ticket_reward": 0}, {}))
	var u: BattleUnit = core.party[0]
	core._apply_intoxicant(_cake(), u)
	# Act: Rush runs out, Crash starts in the fight with 3 turns, one runs, the fight ends.
	u.end_own_turn()
	u.end_own_turn()
	core._fire_due_then(u)
	assert_eq(u.statuses.get("crash", 0), 3, "the Crash started inside the fight")
	u.end_own_turn()
	assert_eq(u.statuses.get("crash", 0), 2, "unused Crash turns are left when the fight ends")
	core.write_back_field_statuses()
	# Assert: no waiting row and no field row carries them to the next fight.
	assert_eq(FieldStatus.waiting_turns(st, "chadwick", "crash"), 0)
	assert_false(FieldStatus.has(st, "crash"))
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {})
	assert_true(FieldStatus.list(st, "chadwick").is_empty())
	assert_true(Dictionary(st.flags.get(FieldStatus.KEY, {})).is_empty())
