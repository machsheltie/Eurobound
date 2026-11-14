extends GutTest
## Cottonmouth stacks (Eurobound-qiof). Author, Eurobound Desk 64vo-q3: "Stacks last longer: more
## Crash turns per stack; one drink per Cottonmouth stack". 64vo-q4: "Double the stacks: Cottonmouth
## arrives with twice as many stacks". Fixture numbers only; no shipped number is read or set.

var st


func before_each() -> void:
	StatusTable.set_entries({
		"gush": {"display_name": "Gush", "scope": ["battle", "field"],
			"default_duration": {"battle_turns": 2, "field_steps": 80, "ends_on_rest": null, "until_cured": false},
			"interactions": [{"with": "hung", "rule": "suppress", "timer": "pause"},
				{"with": "hung", "rule": "modify_then", "then": "cotton", "effect": "double_stacks"}]},
		"cotton": {"display_name": "Cotton", "scope": ["battle", "field"],
			"default_duration": {"ends_on_rest": true, "until_cured": true}, "stack_rule": "extend",
			"stats": {"all": -1},
			"cured_by": [{"kind": "rest"}, {"kind": "item_subtype", "value": "drink"}]},
		"hung": {"display_name": "Hung", "scope": ["battle", "field"],
			"default_duration": {"battle_turns": 5, "field_steps": 200}},
		"plain": {"scope": ["battle", "field"], "default_duration": {"until_cured": true},
			"cured_by": [{"kind": "item_subtype", "value": "drink"}]},
	})
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "chadwick", "display_name": "Chadwick", "hp": 30, "max_hp": 30, "bravado": 5,
		"max_bravado": 10, "offense": 8, "defense": 4, "speed": 5, "luck": 2, "grit": 3, "charm": 4}]


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _vape(turns: Variant = 1, steps: Variant = 80) -> Dictionary:
	return {"display_name": "Vape", "subtype": "vape", "heal_hp": 0, "heal_bravado": 0,
		"intoxicant": {"status": "gush", "duration": {"battle_turns": turns, "field_steps": steps},
			"stack_rule": "extend", "then": {"status": "cotton", "stacks": true}}}


const WATER := {"display_name": "Water", "subtype": "drink", "heal_hp": 1, "heal_bravado": 0}
const BEER := {"display_name": "Beer", "subtype": "booze", "alcohol": true, "heal_hp": 1, "heal_bravado": 0}
const SNACK := {"display_name": "Jerky", "subtype": "snack", "heal_hp": 1, "heal_bravado": 0}


## N hits of the vape on the field, then the Gush runs out.
func _field_cotton(hits: int) -> void:
	for i in hits:
		Intoxicant.apply_field(st, "chadwick", _vape())
	FieldStatus.add_steps(st, 80 * hits)


func _core() -> BattleCore:
	var r := RandomNumberGenerator.new()
	r.seed = 1
	var core := BattleCore.new(r)
	core.wallet = st
	st.inventory = {"vape": 9, "water": 9, "beer": 9, "jerky": 9}
	core.items = {"vape": _vape(), "water": WATER, "beer": BEER, "jerky": SNACK}
	var member: Dictionary = st.party[0].duplicate()
	member["statuses"] = FieldStatus.battle_statuses(st, "chadwick")
	core.party.append(BattleUnit.from_member(member))
	core.add_enemy(BattleUnit.from_enemy("foe", {"display_name": "Foe", "max_hp": 50, "offense": 1, "defense": 0,
		"speed": 1, "luck": 0, "ticket_reward": 0}, {}))
	core.start()
	core.tick(5.0)
	core.step()
	return core


func _use(core: BattleCore, id: String) -> bool:
	core.minor_used = false
	return core.use_item(id, core.party[0])


# --- field ---------------------------------------------------------------------------------------

func test_status_stacks_n_follow_ups_arrive_as_n_stacks_on_the_field_row() -> void:
	_field_cotton(3)
	assert_false(FieldStatus.has(st, "gush"))
	assert_true(FieldStatus.has(st, "cotton", "chadwick"))
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 3)


func test_status_stacks_a_later_follow_up_adds_to_the_live_row() -> void:
	_field_cotton(2)
	_field_cotton(1)
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 3)


func test_status_stacks_each_drink_removes_one_stack_and_it_ends_at_zero() -> void:
	_field_cotton(3)
	assert_eq(FieldStatus.cure_by_item(st, "chadwick", "jerky", SNACK), [], "a snack is not a drink")
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 3)
	assert_eq(FieldStatus.cure_by_item(st, "chadwick", "water", WATER), [])
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 2)
	assert_eq(FieldStatus.cure_by_item(st, "chadwick", "beer", BEER), [], "alcohol true is a drink")
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 1)
	assert_true(FieldStatus.has(st, "cotton", "chadwick"))
	assert_eq(FieldStatus.cure_by_item(st, "chadwick", "water", WATER), ["cotton"])
	assert_false(FieldStatus.has(st, "cotton"))
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 0)


func test_status_stacks_a_rest_clears_every_stack() -> void:
	_field_cotton(3)
	GameClock.rest(st)
	assert_false(FieldStatus.has(st, "cotton"))
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 0)


func test_status_stacks_double_over_a_live_hangover_on_the_field() -> void:
	FieldStatus.apply_steps(st, "chadwick", "hung", 200, 5)
	_field_cotton(3)
	assert_true(FieldStatus.has(st, "hung", "chadwick"), "the hidden hangover is still there")
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 6)


func test_status_stacks_do_not_double_without_the_hangover() -> void:
	FieldStatus.apply_steps(st, "bradley", "hung", 200, 5)   # another bro's hangover does not count
	_field_cotton(2)
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 2)


func test_status_stacks_modify_then_reads_only_its_own_rule() -> void:
	assert_eq(StatusTable.then_stack_mult("gush", "cotton", {"hung": 3}), 2)
	assert_eq(StatusTable.then_stack_mult("gush", "cotton", {}), 1, "no live hangover")
	assert_eq(StatusTable.then_stack_mult("gush", "plain", {"hung": 3}), 1, "another follow-up")
	assert_eq(StatusTable.then_stack_mult("hung", "cotton", {"hung": 3}), 1, "no rule on that status")
	assert_eq(StatusTable.then_stack_mult("nope", "cotton", {"hung": 3}), 1)


func test_status_stacks_without_stack_rule_extend_one_drink_clears_it() -> void:
	FieldStatus.apply_from_table(st, "chadwick", "plain", 3)
	FieldStatus.apply_from_table(st, "chadwick", "plain")
	assert_eq(FieldStatus.stack_count(st, "chadwick", "plain"), 1)
	assert_eq(FieldStatus.cure_by_item(st, "chadwick", "water", WATER), ["plain"])


func test_status_stacks_never_deepen_the_stat_penalty() -> void:
	_field_cotton(3)
	var core := _core()
	var u: BattleUnit = core.party[0]
	assert_eq(u.stack_count("cotton"), 3)
	assert_eq(u.defense_stat(), 3, "defense 4, Cotton -1, whatever the stacks")
	assert_eq(StatusTable.stat_delta(u.statuses, "offense"), -1)
	u.status_stacks["cotton"] = 1
	assert_eq(u.defense_stat(), 3)


func test_status_stacks_survive_save_and_load() -> void:
	_field_cotton(3)
	var back = load("res://core/game_state.gd").new()
	back.from_dict(JSON.parse_string(JSON.stringify(st.to_dict())))
	assert_eq(FieldStatus.stack_count(back, "chadwick", "cotton"), 3)
	assert_eq(FieldStatus.cure_by_item(back, "chadwick", "water", WATER), [])
	assert_eq(FieldStatus.stack_count(back, "chadwick", "cotton"), 2)
	back.free()


# --- battle --------------------------------------------------------------------------------------

func test_status_stacks_n_follow_ups_arrive_as_n_stacks_on_the_battle_unit() -> void:
	var core := _core()
	var u: BattleUnit = core.party[0]
	_use(core, "vape")
	_use(core, "vape")
	_use(core, "vape")
	assert_eq(u.statuses["gush"], 3)
	for i in 3:
		u.end_own_turn()
		core._fire_due_then(u)
	assert_false(u.statuses.has("gush"))
	assert_eq(u.statuses.get("cotton", 0), -1, "until cured")
	assert_eq(u.stack_count("cotton"), 3)


func test_status_stacks_double_over_a_live_hangover_in_battle() -> void:
	var core := _core()
	var u: BattleUnit = core.party[0]
	u.statuses["hung"] = 5
	_use(core, "vape")
	_use(core, "vape")
	for i in 2:
		u.end_own_turn()
		core._fire_due_then(u)
	assert_eq(u.statuses.get("hung", 0), 5, "the hidden hangover's timer was stopped")
	assert_eq(u.stack_count("cotton"), 4)


func test_status_stacks_each_battle_drink_removes_one_stack() -> void:
	_field_cotton(2)
	var core := _core()
	var u: BattleUnit = core.party[0]
	assert_true(_use(core, "jerky"))
	assert_eq(u.stack_count("cotton"), 2, "a snack is not a drink")
	assert_true(_use(core, "water"))
	assert_true(u.has_status("cotton"))
	assert_eq(u.stack_count("cotton"), 1)
	assert_true(_use(core, "beer"))
	assert_false(u.has_status("cotton"))
	assert_eq(u.stack_count("cotton"), 0)


func test_status_stacks_carry_into_a_fight_and_back_out() -> void:
	_field_cotton(3)
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {"cotton": -1})
	assert_eq(FieldStatus.battle_stacks(st, "chadwick"), {"cotton": 3})
	var core := _core()
	assert_eq(core.party[0].stack_count("cotton"), 3)
	_use(core, "water")
	core.write_back_field_statuses()
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 2)


func test_status_stacks_cured_in_the_fight_end_the_field_row() -> void:
	_field_cotton(1)
	var core := _core()
	_use(core, "water")
	core.write_back_field_statuses()
	assert_false(FieldStatus.has(st, "cotton"))


func test_status_stacks_started_in_a_fight_come_out_onto_the_field() -> void:
	var core := _core()
	var u: BattleUnit = core.party[0]
	_use(core, "vape")
	_use(core, "vape")
	for i in 2:
		u.end_own_turn()
		core._fire_due_then(u)
	core.write_back_field_statuses()
	assert_true(FieldStatus.has(st, "cotton", "chadwick"))
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 2)


func test_status_stacks_gained_in_a_fight_add_to_the_carried_row() -> void:
	_field_cotton(1)
	var core := _core()
	var u: BattleUnit = core.party[0]
	_use(core, "vape")
	u.end_own_turn()
	core._fire_due_then(u)
	assert_eq(u.stack_count("cotton"), 2)
	core.write_back_field_statuses()
	assert_eq(FieldStatus.stack_count(st, "chadwick", "cotton"), 2)


func test_status_stacks_shipped_data_carries_both_rulings() -> void:
	StatusTable.reset()
	assert_eq(StatusTable.entry("cottonmouth").get("stack_rule"), "extend")
	assert_eq(StatusTable.then_stack_mult("gush_locked", "cottonmouth", {"hungover": 1}), 2)
	assert_eq(StatusTable.then_stack_mult("gush_locked", "cottonmouth", {}), 1)
