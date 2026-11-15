extends GutTest
## The Munchies, the status after Space Cake Gamble (Eurobound-0zt0; author, Eurobound Desk
## Eurobound-0zt0-q1, 2026-11-15: "Approve as proposed";
## docs/superpowers/specs/2026-11-14-the-munchies-proposal.md M1-M5, M8-M10, section 3).
## Approved values only. The double order (M6), the menu default (M7) and vendor counters are not
## built: none of the food vendors has a scene yet.

const GAMBLE := FieldStatus.SPACE_CAKE_GAMBLE
const MUNCHIES := FieldStatus.MUNCHIES
const T0 := 600


class FakeRepo:
	var d: Dictionary

	func _init(items: Dictionary) -> void:
		d = items

	func get_item(id: String) -> Dictionary:
		return d.get(id, {})


var st


func before_each() -> void:
	StatusTable.reset()
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [
		{"id": "bradley", "hp": 1, "max_hp": 200, "bravado": 14, "max_bravado": 14},
		{"id": "chadwick", "hp": 1, "max_hp": 200, "bravado": 100, "max_bravado": 200},
	]
	GameClock.set_time(st, T0)


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _member(id: String) -> Dictionary:
	for m in st.party:
		if m["id"] == id:
			return m
	return {}


func _kroket() -> Dictionary:
	return {"display_name": "Kroket", "subtype": "food", "heal_hp": 20, "heal_bravado": 0}


## Space Cake Gamble on `id`, run out on the clock.
func _gamble_runs_out(id: String = "bradley") -> void:
	FieldStatus.apply_from_table(st, id, GAMBLE)
	GameClock.set_time(st, GameClock.minutes(st) + 90)


# --- data (spec section 3) ----------------------------------------------------------------------

func test_munchies_entry_matches_the_approved_data() -> void:
	var m := StatusTable.entry(MUNCHIES)
	assert_eq(m["display_name"], "The Munchies")
	assert_eq(m["section"], "neutral")
	assert_eq(m["scope"], ["field"])
	assert_eq(m["bearer"], "bro")
	assert_eq(int(m["default_duration"]["clock_minutes"]), 120, "M3")
	assert_eq(m["default_duration"]["ends_on_rest"], true)
	assert_eq(m["stack_rule"], "refresh", "M9")
	assert_eq(m["cured_by"], [{"kind": "rest"}], "M10")
	assert_eq(StatusTable.entry(GAMBLE)["then"], {"status": "munchies", "stacks": false})


func test_munchies_engine_constants_are_the_approved_numbers() -> void:
	assert_eq(FieldStatus.MUNCHIES_BRAVADO_DROP, 40, "M4")
	assert_eq(FieldStatus.MUNCHIES_FOOD_HEAL_BONUS_PCT, 50, "M5")
	assert_eq(FieldStatus.MUNCHIES_FULL_AFTER_ITEMS, 3, "M8")


# --- M1: source ---------------------------------------------------------------------------------

func test_munchies_fires_when_the_gamble_ends_by_time() -> void:
	_gamble_runs_out()
	assert_false(FieldStatus.has(st, GAMBLE, "bradley"))
	assert_true(FieldStatus.has(st, MUNCHIES, "bradley"))
	assert_false(FieldStatus.has(st, MUNCHIES, "chadwick"), "only the bro whose Gamble ran out")


func test_munchies_does_not_fire_when_rest_ends_the_gamble() -> void:
	# Arrange
	FieldStatus.apply_from_table(st, "bradley", GAMBLE)
	# Act
	RestEvents.run(st)
	GameClock.set_time(st, GameClock.minutes(st) + 300)
	# Assert
	assert_false(FieldStatus.has(st, GAMBLE, "bradley"))
	assert_false(FieldStatus.has(st, MUNCHIES, "bradley"))
	assert_eq(int(_member("bradley")["bravado"]), 14, "no comedown without The Munchies")


func test_munchies_fires_once_however_many_cakes_fed_the_gamble() -> void:
	# Arrange: two cakes' worth of Gamble (180 minutes left).
	_member("chadwick")["bravado"] = 100
	FieldStatus.apply_from_table(st, "chadwick", GAMBLE)
	FieldStatus.apply_from_table(st, "chadwick", GAMBLE)
	# Act
	GameClock.set_time(st, T0 + 180)
	# Assert: one firing, one drop of 40, one 120-minute row.
	assert_eq(int(_member("chadwick")["bravado"]), 60)
	GameClock.set_time(st, T0 + 180 + 119)
	assert_true(FieldStatus.has(st, MUNCHIES, "chadwick"))
	GameClock.set_time(st, T0 + 180 + 120)
	assert_false(FieldStatus.has(st, MUNCHIES, "chadwick"))


# --- M2, M3, M10: scope, length, cures ----------------------------------------------------------

func test_munchies_lasts_120_clock_minutes() -> void:
	_gamble_runs_out()
	GameClock.set_time(st, T0 + 90 + 119)
	assert_true(FieldStatus.has(st, MUNCHIES, "bradley"))
	GameClock.set_time(st, T0 + 90 + 120)
	assert_false(FieldStatus.has(st, MUNCHIES, "bradley"))


func test_munchies_ends_at_rest() -> void:
	_gamble_runs_out()
	RestEvents.run(st)
	assert_false(FieldStatus.has(st, MUNCHIES, "bradley"))


func test_munchies_is_not_carried_into_battle() -> void:
	_gamble_runs_out()
	assert_false(FieldStatus.battle_statuses(st, "bradley").has(MUNCHIES))


# --- M4: the comedown ---------------------------------------------------------------------------

func test_munchies_firing_drops_bravado_by_40_and_never_below_zero() -> void:
	# Arrange: Bradley has 14 Bravado, Chadwick 100.
	FieldStatus.apply_from_table(st, "chadwick", GAMBLE)
	# Act
	_gamble_runs_out("bradley")
	# Assert
	assert_eq(int(_member("bradley")["bravado"]), 0, "14 - 40 stops at 0")
	assert_eq(int(_member("chadwick")["bravado"]), 60, "100 - 40")


# --- M5: food tastes incredible -----------------------------------------------------------------

func test_munchies_food_restores_50_percent_more_hp_rounded_up() -> void:
	# Arrange
	_gamble_runs_out()
	st.inventory = {"kroket": 1, "bitterbal": 1}
	var odd := _kroket()
	odd["heal_hp"] = 5
	# Act / Assert: a +20 HP kroket gives 30; +5 gives 8 (7.5 rounds up).
	st.use_item("kroket", FakeRepo.new({"kroket": _kroket()}))
	assert_eq(int(_member("bradley")["hp"]), 1 + 30)
	st.use_item("bitterbal", FakeRepo.new({"bitterbal": odd}))
	assert_eq(int(_member("bradley")["hp"]), 1 + 30 + 8)


func test_munchies_does_not_raise_bravado_from_food() -> void:
	_gamble_runs_out()
	var doner := _kroket()
	doner["heal_bravado"] = 10
	st.inventory = {"doner": 1}
	st.use_item("doner", FakeRepo.new({"doner": doner}))
	assert_eq(int(_member("bradley")["bravado"]), 10, "0 after the comedown, +10 and no more")


func test_munchies_bonus_is_for_food_only() -> void:
	_gamble_runs_out()
	var drink := {"display_name": "Soda", "subtype": "drink", "heal_hp": 20, "heal_bravado": 0}
	assert_eq(FieldStatus.food_heal(st, "bradley", drink), 20)
	assert_eq(FieldStatus.food_heal(st, "bradley", {"display_name": "Kebab", "heal_hp": 20}), 20, "no subtype")
	assert_true(FieldStatus.has(st, MUNCHIES, "bradley"), "neither counts toward the three")


func test_munchies_bonus_is_only_for_the_bro_who_has_it() -> void:
	_gamble_runs_out("bradley")
	assert_eq(FieldStatus.food_heal(st, "chadwick", _kroket()), 20)
	assert_eq(FieldStatus.food_heal(st, "bradley", _kroket()), 30)


func test_munchies_food_without_the_status_heals_the_plain_amount() -> void:
	assert_eq(FieldStatus.food_heal(st, "bradley", _kroket()), 20)


func test_munchies_field_menu_item_use_goes_through_food_heal() -> void:
	# Arrange: no shipped consumable is subtype "food" yet, so the shipped kebab heals its plain 20
	# and does not count toward the three. The +50% itself is proven on food_heal above.
	_gamble_runs_out()
	var menu := FieldMenu.new()
	menu.setup(st)
	add_child_autofree(menu)
	st.inventory = {"lukewarm_kebab": 1}
	# Act
	var used := menu.use_on("lukewarm_kebab", 0)
	# Assert
	assert_true(used)
	assert_eq(int(_member("bradley")["hp"]), 1 + 20)
	assert_true(FieldStatus.has(st, MUNCHIES, "bradley"))


# --- M8: full is full ---------------------------------------------------------------------------

func test_munchies_ends_after_three_food_items_and_the_third_still_gets_the_bonus() -> void:
	_gamble_runs_out()
	assert_eq(FieldStatus.food_heal(st, "bradley", _kroket()), 30)
	assert_eq(FieldStatus.food_heal(st, "bradley", _kroket()), 30)
	assert_true(FieldStatus.has(st, MUNCHIES, "bradley"))
	assert_eq(FieldStatus.food_heal(st, "bradley", _kroket()), 30)
	assert_false(FieldStatus.has(st, MUNCHIES, "bradley"))
	assert_eq(FieldStatus.food_heal(st, "bradley", _kroket()), 20, "the fourth is plain")


# --- M9: stacking -------------------------------------------------------------------------------

func test_munchies_refresh_resets_the_length_and_the_count_and_drops_bravado_again() -> void:
	# Arrange: The Munchies live with two items eaten and 60 minutes gone; Bravado built back up.
	_gamble_runs_out("chadwick")
	FieldStatus.food_heal(st, "chadwick", _kroket())
	FieldStatus.food_heal(st, "chadwick", _kroket())
	_member("chadwick")["bravado"] = 50
	FieldStatus.apply_from_table(st, "chadwick", GAMBLE)
	# Act: the second Gamble runs out while The Munchies is live.
	GameClock.set_time(st, T0 + 90 + 90)
	# Assert
	assert_eq(int(_member("chadwick")["bravado"]), 10, "M4 applies again")
	FieldStatus.food_heal(st, "chadwick", _kroket())
	FieldStatus.food_heal(st, "chadwick", _kroket())
	assert_true(FieldStatus.has(st, MUNCHIES, "chadwick"), "the count started again")
	GameClock.set_time(st, T0 + 180 + 119)
	assert_true(FieldStatus.has(st, MUNCHIES, "chadwick"), "120 minutes from the refresh")
	GameClock.set_time(st, T0 + 180 + 120)
	assert_false(FieldStatus.has(st, MUNCHIES, "chadwick"))
