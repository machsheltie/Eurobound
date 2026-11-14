extends GutTest
## Space Cake Gamble's random teleportation on the Navigation roll, and the Coffeeshop Quarter
## exit's Contact High check (Eurobound-2xah). Approved values only:
## docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md T1-T5, T7, CH2, section 5.

const C := NavigationRoll.SIGN_CENTRAAL
const M := NavigationRoll.SIGN_MUSEUM_PLEIN
const GAMBLE := FieldStatus.SPACE_CAKE_GAMBLE
const HIGH := FieldStatus.CONTACT_HIGH
const RIGHT := 0   # draw 0 lands on the correct exit
const WRONG := 99  # draw 99 lands on the last wrong exit
const T0 := 600

var st
var nav: NavigationRoll


func before_each() -> void:
	StatusTable.reset()
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "lord_pilsner"}, {"id": "chadwick"}, {"id": "bradley"}]
	GameClock.set_time(st, T0)
	NavigationRoll.note_item_used(st, {"alcohol": true})  # Sober off
	nav = NavigationRoll.new(st)


func after_each() -> void:
	st.free()


func _gamble() -> void:
	FieldStatus.apply(st, "chadwick", GAMBLE, 9000)


## A draw (0-99) that the sign's odds land on `exit_id` with.
func _draw_for(sign_id: String, exit_id: String) -> int:
	var acc := 0
	for e: Dictionary in nav.exit_odds(sign_id, {}):
		if e["id"] == exit_id:
			return acc
		acc += int(e["chance"])
	return -1


# --- data -----------------------------------------------------------------------------------------

func test_navigation_teleport_data_is_the_approved_block() -> void:
	assert_eq(NavigationRoll.validate(nav.data), [])
	var t: Dictionary = nav.data["teleport"]
	assert_eq(t["status"], GAMBLE)
	assert_eq(int(t["chance_on_wrong"]), 50)
	assert_eq(int(t["lost_minutes"]), 30)
	assert_eq(t.size(), 3)


func test_navigation_teleport_validate_rejects_bad_numbers() -> void:
	var d: Dictionary = nav.data.duplicate(true)
	d["teleport"]["chance_on_wrong"] = 150
	assert_eq(NavigationRoll.validate(d).size(), 1)
	d = nav.data.duplicate(true)
	d["teleport"]["lost_minutes"] = -1
	assert_eq(NavigationRoll.validate(d).size(), 1)
	d = nav.data.duplicate(true)
	d["grants"][HIGH]["chance"] = 101
	assert_eq(NavigationRoll.validate(d).size(), 1)
	d = nav.data.duplicate(true)
	d.erase("teleport")
	assert_eq(NavigationRoll.validate(d), [], "no teleport block = no teleport")


# --- T1: only with Space Cake Gamble --------------------------------------------------------------

func test_navigation_teleport_never_happens_without_the_gamble() -> void:
	var r := nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 3})
	assert_false(r["teleported"])
	assert_eq(r["exit"], "where_you_started")
	assert_eq(GameClock.minutes(st), T0)


# --- T2: order ------------------------------------------------------------------------------------

func test_navigation_teleport_leaves_a_correct_roll_untouched() -> void:
	_gamble()
	var r := nav.roll(C, {}, RIGHT, {"teleport": 0, "destination": 0})
	assert_true(r["correct"])
	assert_false(r["teleported"])
	assert_eq(r["exit"], "centraal_chaos")
	assert_eq(GameClock.minutes(st), T0)
	assert_eq(nav.successes_this_visit(), 1)
	assert_eq(nav.wrong_turns_this_visit(), 0)


func test_navigation_teleport_replaces_a_wrong_exit_half_the_time() -> void:
	_gamble()
	var hit := nav.roll(C, {}, WRONG, {"teleport": 49, "destination": 3})
	assert_true(hit["teleported"], "draw 49 of 0-99 is inside 50%")
	assert_eq(hit["exit"], "museum_mile")
	var miss := nav.roll(C, {}, WRONG, {"teleport": 50, "destination": 3})
	assert_false(miss["teleported"])
	assert_eq(miss["exit"], "where_you_started", "the rolled wrong exit stands")


func test_navigation_teleport_rate_is_about_half_of_wrong_rolls() -> void:
	_gamble()
	var rng := RandomNumberGenerator.new()
	rng.seed = 20261113
	var n := NavigationRoll.new(st, rng)
	var wrong := 0
	var ported := 0
	for i in 4000:
		GameClock.set_time(st, T0)  # lost time must not run the Gamble out mid-sample
		FieldStatus.remove(st, HIGH)
		n.leave_tunnel()
		var r := n.roll(C, {})
		if r["correct"]:
			assert_false(r["teleported"])
		else:
			wrong += 1
			ported += 1 if r["teleported"] else 0
	var rate := float(ported) / float(wrong)
	assert_between(rate, 0.46, 0.54)


# --- T3: where to ---------------------------------------------------------------------------------

func test_navigation_teleport_has_six_destinations_never_the_correct_exit() -> void:
	var centraal := nav.teleport_destinations(C)
	var ids := centraal.map(func(e): return e["id"])
	assert_eq(ids, ["roodelicht_row", "coffeeshop_quarter", "where_you_started",
			"museum_mile", "frietomat", "canal_surface"])
	var museum := nav.teleport_destinations(M).map(func(e): return e["id"])
	assert_eq(museum, ["centraal_chaos", "roodelicht_row", "coffeeshop_quarter", "where_you_started",
			"frietomat", "canal_surface"])


func test_navigation_teleport_each_destination_is_reachable() -> void:
	_gamble()
	var dests := nav.teleport_destinations(C)
	for i in dests.size():
		var r := nav.roll(C, {}, WRONG, {"teleport": 0, "destination": i})
		assert_eq(r["exit"], dests[i]["id"])
		assert_eq(r["label"], dests[i]["label"])


func test_navigation_teleport_destinations_are_uniform() -> void:
	_gamble()
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	var n := NavigationRoll.new(st, rng)
	var counts := {}
	var total := 0
	for i in 6000:
		GameClock.set_time(st, T0)  # lost time must not run the Gamble out mid-sample
		var r := n.roll(C, {}, WRONG, {"teleport": 0})
		assert_ne(r["exit"], "centraal_chaos")
		counts[r["exit"]] = int(counts.get(r["exit"], 0)) + 1
		total += 1
	assert_eq(counts.size(), 6)
	for id in counts:
		assert_between(float(counts[id]) / float(total), 0.14, 0.19, "%s is about 1/6" % id)


# --- T4: a wrong turn -----------------------------------------------------------------------------

func test_navigation_teleport_counts_as_a_wrong_turn_even_onto_the_other_signs_exit() -> void:
	_gamble()
	var r := nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 3})
	assert_eq(r["exit"], "museum_mile")
	assert_false(r["correct"])
	assert_eq(nav.wrong_turns_this_visit(), 1)
	assert_eq(nav.successes_this_visit(), 0)


func test_navigation_teleport_three_teleports_bring_tunnel_confusion() -> void:
	_gamble()
	nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	var r := nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	assert_true(Array(r["granted"]).has(NavigationRoll.TUNNEL_CONFUSION))
	assert_true(FieldStatus.has(st, NavigationRoll.TUNNEL_CONFUSION))


func test_navigation_teleport_loses_tunnel_vision() -> void:
	_gamble()
	nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	var r := nav.roll(C, {}, RIGHT)
	assert_false(Array(r["granted"]).has(NavigationRoll.TUNNEL_VISION))


# --- T5: lost time --------------------------------------------------------------------------------

func test_navigation_teleport_costs_30_clock_minutes() -> void:
	_gamble()
	var r := nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	assert_eq(GameClock.minutes(st), T0 + 30)
	assert_eq(int(r["lost_minutes"]), 30)
	var plain := nav.roll(C, {}, WRONG, {"teleport": 99})
	assert_eq(GameClock.minutes(st), T0 + 30, "a plain wrong turn loses no extra time")
	assert_eq(int(plain["lost_minutes"]), 0)


func test_navigation_teleport_lost_time_eats_the_high() -> void:
	FieldStatus.apply(st, "chadwick", GAMBLE, 30)
	nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	assert_false(FieldStatus.has(st, GAMBLE))
	var r := nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	assert_false(r["teleported"])


# --- T7: the readout ------------------------------------------------------------------------------

func test_navigation_teleport_does_not_change_the_readout_or_the_odds() -> void:
	_gamble()
	assert_eq(nav.correct_chance(C, {}), 10, "40 - 30, at the floor")
	assert_eq(nav.display_text(C, {"map_equipped": true}), "25%", "40 + 15 - 30")
	var r := nav.roll(C, {}, WRONG, {"teleport": 0, "destination": 0})
	assert_eq(int(r["chance"]), 10)
	var total := 0
	for e: Dictionary in r["odds"]:
		total += int(e["chance"])
	assert_eq(total, 100)
	assert_eq(Array(r["odds"]).size(), 4)


# --- CH2: Coffeeshop Quarter exit -----------------------------------------------------------------

func test_navigation_contact_high_grant_data() -> void:
	var g: Dictionary = nav.data["grants"][HIGH]
	assert_eq(g["exit"], "coffeeshop_quarter")
	assert_eq(int(g["chance"]), 30)


func test_navigation_coffeeshop_quarter_exit_gives_contact_high_30_percent() -> void:
	var d := _draw_for(C, "coffeeshop_quarter")
	var r := nav.roll(C, {}, d, {"contact_high": 29})
	assert_eq(r["exit"], "coffeeshop_quarter")
	assert_true(Array(r["granted"]).has(HIGH))
	assert_true(FieldStatus.has(st, HIGH, "bradley"), "the whole party")
	assert_true(st.flags[FieldStatus.KEY][FieldStatus.PARTY].has(HIGH))
	GameClock.set_time(st, T0 + 29)
	assert_true(FieldStatus.has(st, HIGH))
	GameClock.set_time(st, T0 + 30)
	assert_false(FieldStatus.has(st, HIGH), "30 clock minutes")


func test_navigation_coffeeshop_quarter_exit_misses_70_percent() -> void:
	var r := nav.roll(C, {}, _draw_for(C, "coffeeshop_quarter"), {"contact_high": 30})
	assert_eq(r["exit"], "coffeeshop_quarter")
	assert_false(Array(r["granted"]).has(HIGH))
	assert_false(FieldStatus.has(st, HIGH))


func test_navigation_other_exits_never_give_contact_high() -> void:
	for id in ["centraal_chaos", "roodelicht_row", "where_you_started"]:
		var r := nav.roll(C, {}, _draw_for(C, id), {"contact_high": 0})
		assert_eq(r["exit"], id)
		assert_false(Array(r["granted"]).has(HIGH))
	assert_false(FieldStatus.has(st, HIGH))


func test_navigation_teleport_into_coffeeshop_quarter_runs_its_check() -> void:
	_gamble()
	var r := nav.roll(M, {}, WRONG, {"teleport": 0, "destination": 2, "contact_high": 0})
	assert_eq(r["exit"], "coffeeshop_quarter")
	assert_true(r["teleported"])
	assert_true(Array(r["granted"]).has(HIGH))
	GameClock.set_time(st, T0 + 30 + 29)
	assert_true(FieldStatus.has(st, HIGH), "30 minutes from emerging, after the lost half hour")
	GameClock.set_time(st, T0 + 30 + 30)
	assert_false(FieldStatus.has(st, HIGH))


func test_navigation_contact_high_rate_is_about_30_percent() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 30
	var n := NavigationRoll.new(st, rng)
	var d := _draw_for(C, "coffeeshop_quarter")
	var got := 0
	for i in 4000:
		FieldStatus.remove(st, HIGH)
		got += 1 if Array(n.roll(C, {}, d)["granted"]).has(HIGH) else 0
	assert_between(float(got) / 4000.0, 0.27, 0.33)
