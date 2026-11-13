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
	assert_eq(int(g[CONFUSION]["minutes"]), 120)
	assert_eq(int(g[VISION]["minutes"]), 60)


func test_navigation_grants_validate_rejects_a_bad_grant() -> void:
	var d: Dictionary = nav.data.duplicate(true)
	d["grants"][CONFUSION]["minutes"] = 0
	d["grants"][VISION]["minutes"] = "an hour"
	assert_eq(NavigationRoll.validate(d).size(), 2)


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
	d["grants"][VISION]["minutes"] = null
	var n := NavigationRoll.new(st, null, d)
	for i in 5:
		n.roll(C, {}, WRONG)
	assert_false(FieldStatus.has(st, CONFUSION))
	n.leave_tunnel()
	n.roll(C, {}, RIGHT)
	assert_false(FieldStatus.has(st, VISION))


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


# --- not granted here -----------------------------------------------------------------------------

func test_navigation_grants_roll_never_sets_the_permanent_reward_flags() -> void:
	# Underground Navigator waits on Eurobound-gpfc; Opa Cees's Blessing comes from a quest.
	for i in 6:
		nav.roll(C, {}, RIGHT)
	assert_false(st.flags.has(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR))
	assert_false(st.flags.has(NavigationRoll.FLAG_OPA_CEES))
