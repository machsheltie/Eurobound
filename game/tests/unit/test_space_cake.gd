extends GutTest
## Contact High and the Space Cake Timer / Gamble (Eurobound-2xah). Approved values only:
## docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md (author, Eurobound Desk
## Eurobound-vt7k-q2: "Approve as proposed"): CH5-CH8, SC4-SC11, section 5 (data).

const TIMER := FieldStatus.SPACE_CAKE_TIMER
const GAMBLE := FieldStatus.SPACE_CAKE_GAMBLE
const HIGH := FieldStatus.CONTACT_HIGH
const T0 := 600

var st


func before_each() -> void:
	StatusTable.reset()
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [
		{"id": "lord_pilsner", "bravado": 10, "max_bravado": 200},
		{"id": "chadwick", "bravado": 10, "max_bravado": 200},
		{"id": "bradley", "bravado": 10, "max_bravado": 200},
	]
	GameClock.set_time(st, T0)


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _bravado(id: String) -> int:
	for m in st.party:
		if m["id"] == id:
			return int(m["bravado"])
	return -1


func _eat(id: String = "chadwick") -> bool:
	return FieldStatus.apply_from_table(st, id, TIMER)


# --- data (spec section 5) ------------------------------------------------------------------------

func test_space_cake_status_entries_match_the_approved_data() -> void:
	var high := StatusTable.entry(HIGH)
	assert_eq(high["section"], "negative")
	assert_eq(high["scope"], ["field"])
	assert_eq(high["bearer"], "bro")
	assert_eq(int(high["default_duration"]["clock_minutes"]), 30)
	assert_eq(high["default_duration"]["ends_on_rest"], true)
	assert_eq(high["default_duration"]["until_cured"], false)
	assert_eq(high["stack_rule"], "refresh")
	assert_eq(high["cured_by"], [{"kind": "rest"}])

	var timer := StatusTable.entry(TIMER)
	assert_eq(timer["display_name"], "Space Cake Timer")
	assert_eq(timer["section"], "neutral")
	assert_eq(timer["scope"], ["field"])
	assert_eq(timer["bearer"], "bro")
	assert_eq(int(timer["default_duration"]["clock_minutes"]), 120)
	assert_eq(timer["default_duration"]["ends_on_rest"], true)
	assert_eq(timer["default_duration"]["until_cured"], false)
	assert_eq(timer["stack_rule"], "none")
	assert_eq(timer["then"], {"status": GAMBLE, "stacks": true})

	var gamble := StatusTable.entry(GAMBLE)
	assert_eq(gamble["section"], "negative")
	assert_eq(gamble["scope"], ["field"])
	assert_eq(gamble["bearer"], "bro")
	assert_eq(int(gamble["default_duration"]["clock_minutes"]), 90)
	assert_eq(gamble["default_duration"]["ends_on_rest"], true)
	assert_eq(gamble["default_duration"]["until_cured"], false)
	assert_eq(gamble["stack_rule"], "extend")
	assert_eq(gamble["cured_by"], [{"kind": "rest"}])


func test_space_cake_engine_constants_are_the_approved_numbers() -> void:
	assert_eq(FieldStatus.SPACE_CAKE_LANDING_BRAVADO, 40, "SC5")
	assert_eq(FieldStatus.SPACE_CAKE_WOBBLE_SECONDS, 15.0, "SC6")
	assert_eq(int(FieldStatus.CLOCK_CAP_MINUTES[GAMBLE]), 180, "SC10")


# --- Contact High ---------------------------------------------------------------------------------

func test_contact_high_lasts_30_clock_minutes_on_the_whole_party() -> void:
	assert_true(FieldStatus.apply_from_table(st, FieldStatus.PARTY, HIGH))
	assert_true(FieldStatus.has(st, HIGH, "bradley"))
	GameClock.set_time(st, T0 + 29)
	assert_true(FieldStatus.has(st, HIGH))
	GameClock.set_time(st, T0 + 30)
	assert_false(FieldStatus.has(st, HIGH))


func test_contact_high_refreshes_to_30_and_never_adds() -> void:
	FieldStatus.apply_from_table(st, FieldStatus.PARTY, HIGH)
	GameClock.set_time(st, T0 + 20)
	FieldStatus.apply_from_table(st, FieldStatus.PARTY, HIGH)
	GameClock.set_time(st, T0 + 49)
	assert_true(FieldStatus.has(st, HIGH), "reset to a full 30 at minute 20")
	GameClock.set_time(st, T0 + 50)
	assert_false(FieldStatus.has(st, HIGH), "30 from the last exposure, not 60")


func test_contact_high_is_only_the_navigation_penalty() -> void:
	FieldStatus.apply_from_table(st, FieldStatus.PARTY, HIGH)
	assert_false(FieldStatus.controls_reversed(st), "CH5: not the reversed-controls Confusion")
	assert_eq(FieldStatus.choice_index(st, 1, 4), 1, "CH5: dialogue is untouched")
	assert_eq(FieldStatus.battle_statuses(st, "chadwick"), {}, "CH6: not carried into battle")


func test_contact_high_ends_on_rest() -> void:
	FieldStatus.apply_from_table(st, FieldStatus.PARTY, HIGH)
	GameClock.rest(st)
	assert_false(st.flags[FieldStatus.KEY].get(FieldStatus.PARTY, {}).has(HIGH))


# --- the timer and its landing --------------------------------------------------------------------

func test_space_cake_timer_does_nothing_for_120_minutes() -> void:
	assert_true(_eat())
	GameClock.set_time(st, T0 + 119)
	assert_true(FieldStatus.has(st, TIMER, "chadwick"))
	assert_false(FieldStatus.has(st, GAMBLE))
	assert_eq(_bravado("chadwick"), 10)
	assert_false(FieldStatus.controls_reversed(st))


func test_space_cake_landing_gives_bravado_the_gamble_and_the_wobble() -> void:
	_eat()
	GameClock.set_time(st, T0 + 120)
	assert_false(FieldStatus.has(st, TIMER))
	assert_true(FieldStatus.has(st, GAMBLE, "chadwick"))
	assert_false(FieldStatus.has(st, GAMBLE, "bradley"), "bearer is the bro who ate it")
	assert_eq(_bravado("chadwick"), 50, "+40 Bravado")
	assert_eq(_bravado("bradley"), 10)
	assert_true(FieldStatus.controls_reversed(st), "onset wobble")
	assert_eq(FieldStatus.choice_index(st, 1, 4), 1, "SC6: dialogue choices are not shuffled")


func test_space_cake_wobble_lasts_15_real_seconds() -> void:
	_eat()
	GameClock.set_time(st, T0 + 120)
	FieldStatus.tick(st, 14.5)
	assert_true(FieldStatus.controls_reversed(st))
	FieldStatus.tick(st, 0.5)
	assert_false(FieldStatus.controls_reversed(st))
	assert_true(FieldStatus.has(st, GAMBLE), "the Gamble outlasts the wobble")


func test_space_cake_wobble_never_shortens_a_longer_trap_mirror() -> void:
	FieldStatus.apply(st, "chadwick", FieldStatus.TRAP_MIRROR, 30.0, FieldStatus.UNIT_REAL)
	_eat()
	GameClock.set_time(st, T0 + 120)
	FieldStatus.tick(st, 20.0)
	assert_true(FieldStatus.controls_reversed(st))


func test_space_cake_landing_bravado_is_capped_at_max() -> void:
	st.party[1]["bravado"] = 190
	_eat()
	GameClock.set_time(st, T0 + 120)
	assert_eq(_bravado("chadwick"), 200)


func test_space_cake_gamble_lasts_90_minutes_after_landing() -> void:
	_eat()
	GameClock.set_time(st, T0 + 120)
	GameClock.set_time(st, T0 + 120 + 89)
	assert_true(FieldStatus.has(st, GAMBLE))
	GameClock.set_time(st, T0 + 120 + 90)
	assert_false(FieldStatus.has(st, GAMBLE))
	assert_eq(_bravado("chadwick"), 50, "nothing lands twice")


func test_space_cake_lands_when_the_walking_tick_sees_the_clock_past_the_timer() -> void:
	_eat()
	st.flags[GameClock.KEY] = T0 + 125  # the clock moved without GameClock.set_time
	FieldStatus.tick(st, 0.016)
	assert_true(FieldStatus.has(st, GAMBLE, "chadwick"))
	assert_eq(_bravado("chadwick"), 50)


func test_space_cake_landing_is_queued_for_the_cue() -> void:
	_eat()
	assert_eq(FieldStatus.take_landings(st), [])
	GameClock.set_time(st, T0 + 120)
	var landed := FieldStatus.take_landings(st)
	assert_eq(landed.size(), 1)
	assert_eq(landed[0]["target"], "chadwick")
	assert_eq(landed[0]["status"], TIMER)
	assert_eq(int(landed[0]["count"]), 1)
	assert_eq(FieldStatus.take_landings(st), [], "taken once")


# --- stacking (SC10) ------------------------------------------------------------------------------

func test_space_cake_second_cake_joins_the_running_timer() -> void:
	_eat()
	GameClock.set_time(st, T0 + 60)
	assert_true(_eat())
	GameClock.set_time(st, T0 + 119)
	assert_false(FieldStatus.has(st, GAMBLE), "the timer did not restart or shorten")
	GameClock.set_time(st, T0 + 120)
	assert_true(FieldStatus.has(st, GAMBLE), "it lands on the first cake's two hours")
	assert_eq(_bravado("chadwick"), 90, "each cake's +40 lands")
	GameClock.set_time(st, T0 + 120 + 179)
	assert_true(FieldStatus.has(st, GAMBLE), "90 minutes per cake")
	GameClock.set_time(st, T0 + 120 + 180)
	assert_false(FieldStatus.has(st, GAMBLE))


func test_space_cake_gamble_is_capped_at_180_minutes() -> void:
	_eat()
	_eat()
	_eat()
	GameClock.set_time(st, T0 + 120)
	assert_eq(_bravado("chadwick"), 130, "three cakes: +120 Bravado")
	GameClock.set_time(st, T0 + 120 + 179)
	assert_true(FieldStatus.has(st, GAMBLE))
	GameClock.set_time(st, T0 + 120 + 180)
	assert_false(FieldStatus.has(st, GAMBLE), "270 is capped at 180")


func test_space_cake_after_landing_a_new_cake_starts_a_new_timer_that_adds_90() -> void:
	_eat()
	_eat()
	GameClock.set_time(st, T0 + 120)  # lands: Gamble until T0 + 300
	GameClock.set_time(st, T0 + 130)
	assert_true(_eat())
	assert_true(FieldStatus.has(st, TIMER, "chadwick"), "a new timer runs beside the Gamble")
	GameClock.set_time(st, T0 + 250)  # the new timer lands with 50 minutes of Gamble left
	assert_eq(_bravado("chadwick"), 130)
	GameClock.set_time(st, T0 + 250 + 139)
	assert_true(FieldStatus.has(st, GAMBLE), "50 left + 90")
	GameClock.set_time(st, T0 + 250 + 140)
	assert_false(FieldStatus.has(st, GAMBLE))


func test_space_cake_adding_to_a_live_gamble_is_capped_at_180_remaining() -> void:
	_eat()
	_eat()
	GameClock.set_time(st, T0 + 10)
	_eat("bradley")  # a different bro's cake is his own timer
	GameClock.set_time(st, T0 + 120)  # chadwick: Gamble 180
	assert_false(FieldStatus.has(st, GAMBLE, "bradley"))
	FieldStatus.apply_from_table(st, "chadwick", GAMBLE)  # +90 on 180 remaining
	GameClock.set_time(st, T0 + 120 + 179)
	assert_true(FieldStatus.has(st, GAMBLE, "chadwick"))
	GameClock.set_time(st, T0 + 120 + 180)
	assert_false(FieldStatus.has(st, GAMBLE, "chadwick"))


# --- rest (SC11) ----------------------------------------------------------------------------------

func test_space_cake_rest_clears_a_timer_that_has_not_landed() -> void:
	_eat()
	GameClock.set_time(st, T0 + 60)
	GameClock.rest(st)
	assert_false(FieldStatus.has(st, TIMER))
	assert_false(FieldStatus.has(st, GAMBLE))
	assert_eq(_bravado("chadwick"), 10, "no Bravado lands")
	assert_false(FieldStatus.controls_reversed(st))
	GameClock.set_time(st, GameClock.minutes(st) + 600)
	FieldStatus.tick(st, 0.016)
	assert_false(FieldStatus.has(st, GAMBLE), "nothing was banked overnight")
	assert_eq(_bravado("chadwick"), 10)
	assert_eq(FieldStatus.take_landings(st), [])


func test_space_cake_rest_ends_the_gamble() -> void:
	_eat()
	GameClock.set_time(st, T0 + 120)
	GameClock.rest(st)
	assert_false(st.flags[FieldStatus.KEY].get("chadwick", {}).has(GAMBLE))
	assert_false(FieldStatus.has(st, GAMBLE))


# --- generic: clock rows fire `then` from the status table ----------------------------------------

func test_field_status_clock_row_fires_table_then_on_expiry() -> void:
	StatusTable.set_entries({
		"a_status": {"default_duration": {"clock_minutes": 20}, "then": {"status": "b_status", "stacks": false}},
		"b_status": {"default_duration": {"clock_minutes": 10}},
	})
	FieldStatus.apply_from_table(st, "bradley", "a_status")
	FieldStatus.apply_from_table(st, "bradley", "a_status")
	GameClock.set_time(st, T0 + 19)
	assert_false(FieldStatus.has(st, "b_status"))
	GameClock.set_time(st, T0 + 20)
	assert_true(FieldStatus.has(st, "b_status", "bradley"))
	assert_eq(_bravado("bradley"), 10, "only the Space Cake Timer has a landing hook")
	GameClock.set_time(st, T0 + 30)
	assert_false(FieldStatus.has(st, "b_status"))


func test_field_status_clock_row_without_then_just_ends() -> void:
	FieldStatus.apply(st, "bradley", FieldStatus.SAW_YOURSELF, 60)
	GameClock.set_time(st, T0 + 60)
	assert_false(FieldStatus.has(st, FieldStatus.SAW_YOURSELF))
	assert_eq(FieldStatus.take_landings(st), [])


func test_field_status_settle_leaves_flags_alone_when_there_are_no_rows() -> void:
	st.flags = {}
	GameClock.set_time(st, 700)
	assert_eq(st.flags.keys(), [GameClock.KEY])
