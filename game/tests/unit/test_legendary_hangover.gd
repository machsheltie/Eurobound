extends GutTest
## The four Legendary Hangovers (Eurobound-jykm). Author, Eurobound Desk Eurobound-picf-q1: "Approve
## as proposed" (docs/superpowers/specs/2026-11-14-legendary-hangover-unit-and-rescale-proposal.md,
## U1-U6 and S1-S5; design/quests/general_quests/brewerytour.md, "Legendary Hangover rules").
## These tests read the SHIPPED status table: the sizes and lengths are the approved ones.

## [buff id, hangover id, buff, penalty, game-clock minutes]
const CITIES := [
	["the_full_irish_experience", "legendary_hungover", 5, -3, 30],
	["the_imperial_concerto", "imperial_hangover", 6, -4, 40],
	["the_neon_nightmare", "neon_nightmare_hungover", 7, -5, 45],
	["canal_courage", "canal_courage_hungover", 7, -5, 45],
]
const SIX := ["offense", "defense", "speed", "charm", "luck", "grit"]
## Bradley's approved stats (round v26): Defense 2 and Grit 3 meet the floor at -5.
const BRADLEY := {"id": "bradley", "display_name": "Bradley", "hp": 30, "max_hp": 30, "bravado": 7,
	"max_bravado": 14, "offense": 12, "defense": 2, "speed": 8, "luck": 5, "grit": 3, "charm": 4}
const CURE := {"display_name": "Cure", "subtype": "food", "heal_hp": 1, "heal_bravado": 0}

var st


func before_each() -> void:
	StatusTable.reset()
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [BRADLEY.duplicate()]
	st.inventory = {}


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _core(start: bool = true) -> BattleCore:
	var r := RandomNumberGenerator.new()
	r.seed = 1
	var core := BattleCore.new(r)
	core.wallet = st
	var member: Dictionary = st.party[0].duplicate()
	member["statuses"] = FieldStatus.battle_statuses(st, "bradley")
	core.party.append(BattleUnit.from_member(member))
	core.add_enemy(BattleUnit.from_enemy("foe", {"display_name": "Foe", "max_hp": 50, "offense": 1, "defense": 0,
		"speed": 1, "luck": 0, "ticket_reward": 0}, {}))
	if start:
		core.start()
		core.tick(5.0)
		core.step()
	return core


func _row(id: String) -> Dictionary:
	return Dictionary(Dictionary(st.flags.get(FieldStatus.KEY, {})).get("bradley", {})).get(id, {})


func _left(id: String) -> int:
	return int(_row(id).get("until", 0)) - GameClock.minutes(st)


func _walk(minutes: int) -> void:
	var left := minutes
	while left > 0:
		GameClock.set_time(st, GameClock.minutes(st) + mini(left, 10))
		left -= 10


# --- data (S1, S2, U1, U4, U5) ----------------------------------------------------------------------

func test_legendary_hangover_table_holds_the_approved_sizes_and_lengths() -> void:
	for c in CITIES:
		var buff := StatusTable.entry(c[0])
		var hang := StatusTable.entry(c[1])
		assert_eq(int(buff["stats"]["all"]), c[2], "%s buff" % c[0])
		assert_eq(Array(buff["scope"]), ["battle"], "%s is battle-scoped" % c[0])
		assert_eq(String(buff["then"]["status"]), c[1])
		assert_eq(int(hang["stats"]["all"]), c[3], "%s penalty" % c[1])
		assert_eq(FieldStatus.table_minutes(c[1]), c[4], "%s clock minutes" % c[1])
		assert_true(hang["default_duration"]["ends_on_rest"])
		assert_eq(String(hang["stack_rule"]), "refresh")
		assert_true(StatusTable.whole_battle(c[0]))
		assert_true(FieldStatus.FIGHT_FIRST.has(c[1]))


func test_legendary_hangover_names_are_the_approved_ones() -> void:
	assert_eq(StatusTable.display_name("the_full_irish_experience"), "The Full Irish Experience")
	assert_eq(StatusTable.display_name("the_imperial_concerto"), "The Imperial Concerto")
	assert_eq(StatusTable.display_name("the_neon_nightmare"), "The Neon Nightmare")
	assert_eq(StatusTable.display_name("canal_courage"), "Canal Courage")
	assert_eq(StatusTable.display_name("legendary_hungover"), "Legendary Hungover")
	assert_eq(StatusTable.display_name("imperial_hangover"), "Imperial Hangover")
	assert_eq(StatusTable.display_name("neon_nightmare_hungover"), "Neon Nightmare Hungover")
	assert_eq(StatusTable.display_name("canal_courage_hungover"), "Canal Courage Hungover")


# --- battle buff ----------------------------------------------------------------------------------

func test_legendary_hangover_buff_adds_to_the_six_stats_and_not_the_meters() -> void:
	for c in CITIES:
		var core := _core()
		var u: BattleUnit = core.party[0]
		var before := {"offense": u.attack_stat(false), "charm": u.attack_stat(true), "defense": u.defense_stat(),
			"speed": u.battle_speed(), "luck": u.luck_stat(), "grit": u.grit_stat()}
		assert_true(core.apply_whole_battle(u, c[0]))
		assert_eq(u.attack_stat(false), before["offense"] + c[2], "%s offense" % c[0])
		assert_eq(u.attack_stat(true), before["charm"] + c[2], "%s charm" % c[0])
		assert_eq(u.defense_stat(), before["defense"] + c[2], "%s defense" % c[0])
		assert_eq(u.battle_speed(), before["speed"] + c[2], "%s speed" % c[0])
		assert_eq(u.luck_stat(), before["luck"] + c[2], "%s luck" % c[0])
		assert_eq(u.grit_stat(), before["grit"] + c[2], "%s grit" % c[0])
		assert_eq(u.max_hp, 30)
		assert_eq(u.max_bravado, 14)


func test_legendary_hangover_buff_lasts_the_whole_battle() -> void:
	var core := _core()
	var u: BattleUnit = core.party[0]
	core.apply_whole_battle(u, "the_neon_nightmare")
	for i in 12:
		u.end_own_turn()
	assert_true(u.has_status("the_neon_nightmare"))
	assert_eq(u.defense_stat(), 9)


func test_legendary_hangover_buff_does_nothing_for_a_status_that_is_not_whole_battle() -> void:
	var core := _core()
	assert_false(core.apply_whole_battle(core.party[0], "contact_high"))
	assert_false(core.party[0].statuses.has("contact_high"))


func test_legendary_hangover_buff_is_inert_outside_a_fight() -> void:
	assert_false(FieldStatus.apply_from_table(st, "bradley", "the_neon_nightmare"))
	assert_true(_row("the_neon_nightmare").is_empty())


func test_legendary_hangover_buff_ends_with_the_fight_and_the_hangover_row_follows() -> void:
	for c in CITIES:
		st.flags = {}
		var core := _core()
		core.apply_whole_battle(core.party[0], c[0])
		assert_false(FieldStatus.has(st, c[1]), "no hangover during the buffed fight")
		core.write_back_field_statuses()
		assert_true(_row(c[0]).is_empty(), "the buff leaves no field row")
		assert_true(FieldStatus.has(st, c[1], "bradley"), "%s follows" % c[1])
		assert_eq(_left(c[1]), c[4])
		assert_false(FieldStatus.battle_statuses(st, "bradley").has(c[0]))


func test_legendary_hangover_no_buff_means_no_hangover_after_the_fight() -> void:
	var core := _core()
	core.write_back_field_statuses()
	for c in CITIES:
		assert_false(FieldStatus.has(st, c[1]))


func test_legendary_hangover_drink_item_starts_the_buff_through_the_intoxicant_path() -> void:
	var core := _core()
	st.inventory = {"trophy": 1}
	core.items = {"trophy": {"display_name": "Trophy", "subtype": "booze", "alcohol": true, "heal_hp": 0,
		"heal_bravado": 0, "intoxicant": {"status": "the_imperial_concerto"}}}
	core.minor_used = false
	assert_true(core.use_item("trophy", core.party[0]))
	assert_eq(int(core.party[0].statuses.get("the_imperial_concerto", 0)), -1)
	assert_eq(core.party[0].defense_stat(), 8)


# --- hangover in battle (U3, S3) --------------------------------------------------------------------

func test_legendary_hangover_live_at_fight_start_lasts_the_whole_fight() -> void:
	FieldStatus.apply_from_table(st, "bradley", "legendary_hungover")
	var core := _core()
	var u: BattleUnit = core.party[0]
	assert_eq(int(u.statuses.get("legendary_hungover", 0)), -1)
	GameClock.act(st, "fight")
	GameClock.act(st, "fight")
	for i in 12:
		u.end_own_turn()
	assert_true(u.has_status("legendary_hungover"), "it does not expire in the middle of the fight")
	assert_eq(u.attack_stat(false), 9.0)


func test_legendary_hangover_penalty_takes_the_six_stats_down() -> void:
	FieldStatus.apply_from_table(st, "bradley", "imperial_hangover")
	var u: BattleUnit = _core().party[0]
	assert_eq(u.attack_stat(false), 8.0)
	assert_eq(u.battle_speed(), BattleRules.speed(4, u.tier()))
	assert_eq(u.luck_stat(), 1)
	assert_eq(u.max_hp, 30)
	assert_eq(u.max_bravado, 14)


func test_legendary_hangover_penalty_never_takes_a_stat_below_1() -> void:
	FieldStatus.apply_from_table(st, "bradley", "neon_nightmare_hungover")
	var u: BattleUnit = _core().party[0]
	assert_eq(u.defense_stat(), 1, "Defense 2 - 5")
	assert_eq(u.grit_stat(), 1, "Grit 3 - 5")
	assert_eq(u.attack_stat(true), 1.0, "Charm 4 - 5")
	assert_eq(u.luck_stat(), 1, "Luck 5 - 5")
	assert_eq(u.attack_stat(false), 7.0, "Offense 12 - 5")


func test_legendary_hangover_two_cities_add_down_to_the_floor() -> void:
	FieldStatus.apply_from_table(st, "bradley", "neon_nightmare_hungover")
	FieldStatus.apply_from_table(st, "bradley", "canal_courage_hungover")
	var u: BattleUnit = _core().party[0]
	assert_eq(u.attack_stat(false), 2.0, "Offense 12 - 10")
	assert_eq(u.battle_speed(), BattleRules.speed(1, u.tier()), "Speed 8 - 10")


func test_legendary_hangover_floor_does_not_raise_a_stat_that_is_already_below_1() -> void:
	assert_eq(StatusTable.with_delta(0, -5), 0)
	assert_eq(StatusTable.with_delta(1, -5), 1)
	assert_eq(StatusTable.with_delta(4, -5), 1)
	assert_eq(StatusTable.with_delta(12, -5), 7)
	assert_eq(StatusTable.with_delta(0, 7), 7)


func test_legendary_hangover_fight_leaves_the_clock_row_alone() -> void:
	FieldStatus.apply_from_table(st, "bradley", "canal_courage_hungover")
	var core := _core()
	core.write_back_field_statuses()
	assert_true(FieldStatus.has(st, "canal_courage_hungover", "bradley"))
	assert_eq(_left("canal_courage_hungover"), 45)


# --- waiting it out (U1, U6) ------------------------------------------------------------------------

func test_legendary_hangover_cannot_be_walked_off_before_a_fight() -> void:
	for c in CITIES:
		st.flags = {}
		FieldStatus.apply_from_table(st, "bradley", c[1])
		_walk(120)
		assert_true(FieldStatus.has(st, c[1], "bradley"), "%s is still on after 120 minutes" % c[1])
		assert_eq(_left(c[1]), 10, "held at its last 10 minutes")


func test_legendary_hangover_clock_runs_normally_above_its_last_10_minutes() -> void:
	FieldStatus.apply_from_table(st, "bradley", "canal_courage_hungover")
	_walk(20)
	assert_eq(_left("canal_courage_hungover"), 25)


func test_legendary_hangover_can_be_waited_out_once_a_fight_has_started_with_it() -> void:
	for c in CITIES:
		st.flags = {}
		FieldStatus.apply_from_table(st, "bradley", c[1])
		var core := _core()
		core.write_back_field_statuses()
		_walk(int(c[4]) - 10)
		assert_true(FieldStatus.has(st, c[1], "bradley"), "%s still has 10 minutes" % c[1])
		_walk(10)
		assert_false(FieldStatus.has(st, c[1]), "%s runs out at its full length" % c[1])


func test_legendary_hangover_held_row_gets_its_fight_then_ends_with_the_fights_minutes() -> void:
	FieldStatus.apply_from_table(st, "bradley", "legendary_hungover")
	_walk(60)
	var core := _core()
	assert_eq(int(core.party[0].statuses.get("legendary_hungover", 0)), -1)
	core.write_back_field_statuses()
	GameClock.act(st, "fight")
	assert_false(FieldStatus.has(st, "legendary_hungover"))


func test_legendary_hangover_fight_mark_only_counts_at_fight_start() -> void:
	FieldStatus.apply_from_table(st, "bradley", "legendary_hungover")
	_core(false)
	_walk(60)
	assert_true(FieldStatus.has(st, "legendary_hungover", "bradley"), "building a fight is not starting it")


func test_legendary_hangover_the_buffed_fight_does_not_count_as_its_fight() -> void:
	var core := _core()
	core.apply_whole_battle(core.party[0], "the_full_irish_experience")
	core.write_back_field_statuses()
	_walk(90)
	assert_true(FieldStatus.has(st, "legendary_hungover", "bradley"))


func test_legendary_hangover_fight_mark_is_saved_and_loaded() -> void:
	FieldStatus.apply_from_table(st, "bradley", "neon_nightmare_hungover")
	st.flags = JSON.parse_string(JSON.stringify(st.flags))
	_walk(90)
	assert_true(FieldStatus.has(st, "neon_nightmare_hungover", "bradley"), "unfought mark survives a save")
	FieldStatus.note_fight_started(st, "bradley")
	st.flags = JSON.parse_string(JSON.stringify(st.flags))
	_walk(20)
	assert_false(FieldStatus.has(st, "neon_nightmare_hungover"), "fought mark survives a save")


func test_legendary_hangover_other_clock_statuses_are_not_held() -> void:
	FieldStatus.apply_from_table(st, "bradley", "contact_high")
	_walk(30)
	assert_false(FieldStatus.has(st, "contact_high"))


# --- cures and stacking (U4, U5) --------------------------------------------------------------------

func test_legendary_hangover_sleep_ends_it_before_any_fight() -> void:
	for c in CITIES:
		st.flags = {}
		FieldStatus.apply_from_table(st, "bradley", c[1])
		GameClock.rest(st)
		assert_false(FieldStatus.has(st, c[1]), "%s ends at rest" % c[1])
		assert_true(_row(c[1]).is_empty())


func test_legendary_hangover_cure_item_ends_it_before_any_fight() -> void:
	var table := StatusTable.entries().duplicate(true)
	table["legendary_hungover"]["cured_by"] = [{"kind": "rest"}, {"kind": "item_id", "value": "cure"}]
	StatusTable.set_entries(table)
	FieldStatus.apply_from_table(st, "bradley", "legendary_hungover")
	assert_eq(FieldStatus.cure_by_item(st, "bradley", "cure", CURE), ["legendary_hungover"])
	assert_false(FieldStatus.has(st, "legendary_hungover"))


func test_legendary_hangover_cure_item_in_a_fight_ends_the_row_too() -> void:
	var table := StatusTable.entries().duplicate(true)
	table["legendary_hungover"]["cured_by"] = [{"kind": "rest"}, {"kind": "item_id", "value": "cure"}]
	StatusTable.set_entries(table)
	FieldStatus.apply_from_table(st, "bradley", "legendary_hungover")
	var core := _core()
	st.inventory = {"cure": 1}
	core.items = {"cure": CURE}
	core.minor_used = false
	assert_true(core.use_item("cure", core.party[0]))
	assert_false(core.party[0].statuses.has("legendary_hungover"))
	core.write_back_field_statuses()
	assert_false(FieldStatus.has(st, "legendary_hungover"))
	assert_true(_row("legendary_hungover").is_empty())


func test_legendary_hangover_same_city_again_refreshes_and_never_adds() -> void:
	FieldStatus.apply_from_table(st, "bradley", "canal_courage_hungover")
	_walk(20)
	FieldStatus.apply_from_table(st, "bradley", "canal_courage_hungover")
	assert_eq(_left("canal_courage_hungover"), 45)
	assert_eq(StatusTable.stat_delta({"canal_courage_hungover": -1}, "offense"), -5)


func test_legendary_hangover_different_cities_run_side_by_side() -> void:
	FieldStatus.apply_from_table(st, "bradley", "legendary_hungover")
	FieldStatus.apply_from_table(st, "bradley", "imperial_hangover")
	assert_true(FieldStatus.has(st, "legendary_hungover", "bradley"))
	assert_true(FieldStatus.has(st, "imperial_hangover", "bradley"))
