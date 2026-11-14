extends GutTest
## Navigation statuses granted by the roll itself (Eurobound-1esc). Ruled values only:
## design/worlds/shamsterdam/voetgangerstunnel.md Status Effects (:438-455) and Successful
## Navigation Rewards (:179-183); the Tunnel Confusion count comes from
## design/worlds/shamsterdam/items/voetgangerstunnel_items.json:261 and
## design/worlds/shamsterdam/events/voetgangerstunnel_events.json:343-344.

const C := NavigationRoll.SIGN_CENTRAAL
const CONFUSION := NavigationRoll.TUNNEL_CONFUSION
const VISION := NavigationRoll.TUNNEL_VISION
const RIGHT := 0   # draw 0 lands on the correct exit
const WRONG := 99  # draw 99 lands on the last wrong exit

var st
var nav: NavigationRoll


func before_each() -> void:
	StatusTable.reset()
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "lord_pilsner"}, {"id": "chadwick"}, {"id": "bradley"}]
	GameClock.set_time(st, 600)
	NavigationRoll.note_item_used(st, {"alcohol": true})  # Sober off, so sums read cleanly
	nav = NavigationRoll.new(st)


func after_each() -> void:
	st.free()


func _wrong(n: int) -> void:
	for i in n:
		assert_false(nav.roll(C, {}, WRONG)["correct"])


# --- status table ---------------------------------------------------------------------------------

func test_navigation_grants_every_navigation_status_has_a_table_entry() -> void:
	var names := {
		"wobbly_windmill_navigation": "Windmill Grist",
		"contact_high": "Contact High",
		"space_cake_gamble": "Space Cake Gamble",
		"canal_confusion": "Canal Confusion",
		"tunnel_confusion": "Tunnel Confusion",
		"tunnel_vision": "Tunnel Vision",
	}
	var statuses: Dictionary = Dictionary(nav.data["modifiers"])["statuses"]
	assert_eq(statuses.size(), names.size(), "every status the roll reads is listed here")
	for id in statuses:
		assert_true(StatusTable.has_entry(String(id)), "%s has a status_effects.json entry" % id)
		assert_eq(StatusTable.display_name(String(id)), names[id])


func test_navigation_grants_data_is_valid() -> void:
	assert_eq(NavigationRoll.validate(nav.data), [])
	var g: Dictionary = nav.data["grants"]
	assert_eq(int(g[CONFUSION]["wrong_turns"]), 3)


func test_navigation_grants_lengths_come_from_the_status_table_only() -> void:
	# Eurobound-zcdf: the lengths live in status_effects.json default_duration.clock_minutes.
	var g: Dictionary = nav.data["grants"]
	assert_false(Dictionary(g[CONFUSION]).has("minutes"), "no duplicate length in the navigation data")
	assert_false(g.has(VISION), "no duplicate length in the navigation data")
	assert_eq(FieldStatus.table_minutes(CONFUSION), 120)
	assert_eq(FieldStatus.table_minutes(VISION), 60)


func test_navigation_grants_validate_rejects_a_bad_grant() -> void:
	var d: Dictionary = nav.data.duplicate(true)
	d["grants"][CONFUSION]["wrong_turns"] = 0
	assert_eq(NavigationRoll.validate(d).size(), 1)
	d["grants"][CONFUSION]["wrong_turns"] = "three"
	assert_eq(NavigationRoll.validate(d).size(), 1)


# --- wrong-turn counter ---------------------------------------------------------------------------

func test_navigation_grants_wrong_turns_count_per_visit_and_reset_on_leaving() -> void:
	assert_eq(nav.wrong_turns_this_visit(), 0)
	_wrong(2)
	assert_eq(nav.wrong_turns_this_visit(), 2)
	nav.roll(C, {}, RIGHT)
	assert_eq(nav.wrong_turns_this_visit(), 2, "a success does not clear the visit's wrong turns")
	nav.leave_tunnel()
	assert_eq(nav.wrong_turns_this_visit(), 0)


# --- Tunnel Confusion -----------------------------------------------------------------------------

func test_navigation_grants_tunnel_confusion_on_the_third_wrong_turn_of_a_visit() -> void:
	_wrong(2)
	assert_false(FieldStatus.has(st, CONFUSION))
	var r := nav.roll(C, {}, WRONG)
	assert_true(FieldStatus.has(st, CONFUSION))
	assert_eq(r["granted"], [CONFUSION])
	assert_eq(nav.modifier_sum({}), -15)


func test_navigation_grants_wrong_turns_in_separate_visits_do_not_add_up() -> void:
	_wrong(2)
	nav.leave_tunnel()
	_wrong(2)
	assert_false(FieldStatus.has(st, CONFUSION))


func test_navigation_grants_tunnel_confusion_is_whole_party_and_lasts_two_hours() -> void:
	_wrong(3)
	assert_true(FieldStatus.has(st, CONFUSION, FieldStatus.PARTY))
	nav.leave_tunnel()
	GameClock.set_time(st, 600 + 119)
	assert_true(FieldStatus.has(st, CONFUSION), "still on after leaving the tunnel")
	GameClock.set_time(st, 600 + 120)
	assert_false(FieldStatus.has(st, CONFUSION))


func test_navigation_grants_a_successful_navigation_ends_tunnel_confusion() -> void:
	_wrong(3)
	var r := nav.roll(C, {}, RIGHT)
	assert_true(r["correct"])
	assert_false(FieldStatus.has(st, CONFUSION))
	assert_eq(r["cured"], [CONFUSION])
	assert_eq(int(r["chance"]), 25, "the curing roll itself still took the -15")


func test_navigation_grants_more_wrong_turns_while_confused_do_not_refresh_it() -> void:
	_wrong(3)
	GameClock.set_time(st, 600 + 100)
	var r := nav.roll(C, {}, WRONG)
	assert_eq(r["granted"], [])
	GameClock.set_time(st, 600 + 120)
	assert_false(FieldStatus.has(st, CONFUSION))


func test_navigation_grants_unruled_grant_values_are_inert() -> void:
	var d: Dictionary = nav.data.duplicate(true)
	d["grants"][CONFUSION]["wrong_turns"] = null
	var n := NavigationRoll.new(st, null, d)
	for i in 5:
		n.roll(C, {}, WRONG)
	assert_false(FieldStatus.has(st, CONFUSION))


func test_navigation_grants_unruled_table_lengths_are_inert() -> void:
	StatusTable.set_entries({
		CONFUSION: {"display_name": "Tunnel Confusion", "default_duration": {"clock_minutes": null}},
		VISION: {"display_name": "Tunnel Vision", "default_duration": {"clock_minutes": null}},
	})
	_wrong(3)
	assert_false(FieldStatus.has(st, CONFUSION))
	nav.leave_tunnel()
	nav.roll(C, {}, RIGHT)
	assert_false(FieldStatus.has(st, VISION))
	StatusTable.reset()


# --- Tunnel Vision --------------------------------------------------------------------------------

func test_navigation_grants_tunnel_vision_on_a_success_with_no_wrong_turns() -> void:
	var r := nav.roll(C, {}, RIGHT)
	assert_eq(r["granted"], [VISION])
	assert_true(FieldStatus.has(st, VISION, FieldStatus.PARTY))
	assert_eq(nav.modifier_sum({}), 15, "+10 Tunnel Vision, +5 this visit's success")


func test_navigation_grants_no_tunnel_vision_after_a_wrong_turn_this_visit() -> void:
	_wrong(1)
	var r := nav.roll(C, {}, RIGHT)
	assert_eq(r["granted"], [])
	assert_false(FieldStatus.has(st, VISION))


func test_navigation_grants_tunnel_vision_lasts_one_hour() -> void:
	nav.roll(C, {}, RIGHT)
	nav.leave_tunnel()
	GameClock.set_time(st, 600 + 59)
	assert_true(FieldStatus.has(st, VISION))
	GameClock.set_time(st, 600 + 60)
	assert_false(FieldStatus.has(st, VISION))


func test_navigation_grants_a_perfect_success_can_cure_old_confusion_and_grant_vision() -> void:
	_wrong(3)
	nav.leave_tunnel()
	var r := nav.roll(C, {}, RIGHT)
	assert_eq(r["cured"], [CONFUSION])
	assert_eq(r["granted"], [VISION])


# --- Underground Navigator (Eurobound-gpfc) --------------------------------------------------------
# Author, bead page 2026-11-13: "After 5 successful navigations (Buffs Earned, :459)".

func test_navigation_grants_underground_navigator_data_is_five_successes() -> void:
	assert_eq(int(nav.data["grants"]["underground_navigator"]["successes"]), 5)


func test_navigation_grants_underground_navigator_not_set_before_the_fifth_success() -> void:
	for i in 4:
		nav.roll(C, {}, RIGHT)
	assert_eq(nav.lifetime_successes(), 4)
	assert_false(st.flags.has(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR))


func test_navigation_grants_underground_navigator_set_on_the_fifth_success() -> void:
	var r := {}
	for i in 5:
		r = nav.roll(C, {}, RIGHT)
	assert_true(bool(st.flags.get(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR, false)))
	assert_true(bool(r["underground_navigator_earned"]))
	assert_eq(nav.lifetime_successes(), 5)


func test_navigation_grants_underground_navigator_earned_is_reported_once() -> void:
	for i in 4:
		assert_false(bool(nav.roll(C, {}, RIGHT)["underground_navigator_earned"]))
	assert_true(bool(nav.roll(C, {}, RIGHT)["underground_navigator_earned"]))
	assert_false(bool(nav.roll(C, {}, RIGHT)["underground_navigator_earned"]))


func test_navigation_grants_underground_navigator_count_survives_leaving_the_tunnel() -> void:
	for i in 3:
		nav.roll(C, {}, RIGHT)
	nav.leave_tunnel()
	assert_eq(nav.lifetime_successes(), 3)
	nav.roll(C, {}, RIGHT)
	nav.leave_tunnel()
	assert_false(st.flags.has(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR))
	nav.roll(C, {}, RIGHT)
	assert_true(bool(st.flags.get(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR, false)))


func test_navigation_grants_underground_navigator_wrong_turns_do_not_count() -> void:
	for i in 4:
		nav.roll(C, {}, RIGHT)
	_wrong(3)
	assert_eq(nav.lifetime_successes(), 4)
	assert_false(st.flags.has(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR))


func test_navigation_grants_underground_navigator_fifth_roll_does_not_get_its_own_bonus() -> void:
	var r := {}
	for i in 5:
		nav.leave_tunnel()  # no per-visit +5
		FieldStatus.remove(st, VISION)
		r = nav.roll(C, {}, RIGHT)
	assert_eq(int(r["chance"]), 40, "the flag is set after the fifth roll")
	nav.leave_tunnel()
	FieldStatus.remove(st, VISION)
	assert_eq(nav.modifier_sum({}), 5)


func test_navigation_grants_underground_navigator_unruled_count_is_inert() -> void:
	var d: Dictionary = nav.data.duplicate(true)
	d["grants"]["underground_navigator"]["successes"] = null
	var n := NavigationRoll.new(st, null, d)
	for i in 8:
		n.roll(C, {}, RIGHT)
	assert_false(st.flags.has(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR))


func test_navigation_grants_validate_rejects_a_bad_underground_navigator_count() -> void:
	var d: Dictionary = nav.data.duplicate(true)
	d["grants"]["underground_navigator"]["successes"] = 0
	assert_eq(NavigationRoll.validate(d).size(), 1)


# --- Marloes's Blessing (Eurobound-6dx6) -----------------------------------------------------------
# Author, bead page 2026-11-13: "Yes: +20 on the roll for the rest of that tunnel visit".

func test_navigation_grants_marloes_blessing_data_is_twenty_points() -> void:
	assert_eq(int(nav.data["modifiers"]["marloes_blessing"]), 20)


func test_navigation_grants_marloes_blessing_off_by_default() -> void:
	assert_false(nav.has_marloes_blessing())
	assert_eq(nav.modifier_sum({}), 0)


func test_navigation_grants_marloes_blessing_adds_twenty_to_the_roll() -> void:
	nav.grant_marloes_blessing()
	assert_true(nav.has_marloes_blessing())
	assert_eq(nav.modifier_sum({}), 20)
	assert_eq(nav.correct_chance(C, {}), 60)
	assert_eq(int(nav.roll(C, {}, WRONG)["chance"]), 60)


func test_navigation_grants_marloes_blessing_lasts_the_rest_of_the_visit() -> void:
	nav.grant_marloes_blessing()
	_wrong(2)
	assert_eq(nav.modifier_sum({}), 20)


func test_navigation_grants_marloes_blessing_cleared_on_leaving_the_tunnel() -> void:
	nav.grant_marloes_blessing()
	nav.leave_tunnel()
	assert_false(nav.has_marloes_blessing())
	assert_false(st.flags.has(NavigationRoll.MARLOES_KEY))
	assert_eq(nav.modifier_sum({}), 0)


func test_navigation_grants_marloes_blessing_adds_to_the_map_bonus() -> void:
	nav.grant_marloes_blessing()
	assert_eq(nav.modifier_sum({"map_equipped": true}), 35, "+15 map, +20 blessing (N3: additive)")


func test_navigation_grants_marloes_blessing_as_a_roll_context_input() -> void:
	assert_eq(nav.modifier_sum({"marloes_blessing": true}), 20)
	assert_false(nav.has_marloes_blessing(), "the context input does not set the visit flag")


func test_navigation_grants_marloes_blessing_counts_once_with_flag_and_context() -> void:
	nav.grant_marloes_blessing()
	assert_eq(nav.modifier_sum({"marloes_blessing": true}), 20)


# --- not granted here -----------------------------------------------------------------------------

func test_navigation_grants_roll_never_sets_the_opa_cees_flag() -> void:
	# Opa Cees's Blessing comes from a quest (Eurobound-lofj).
	for i in 6:
		nav.roll(C, {}, RIGHT)
	assert_false(st.flags.has(NavigationRoll.FLAG_OPA_CEES))
