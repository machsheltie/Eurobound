extends GutTest
## FieldCues (Eurobound-k3qa): the one place the screen layer hears about the Space Cake cues the
## engine already produces (Eurobound-2xah). Approved spec:
## docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md SC4, SC5c, SC7, T6.
## These tests cover the hand-off only. What a cue looks, reads or sounds like is not built.

const CUES := preload("res://core/field_cues.gd")
const TIMER := FieldStatus.SPACE_CAKE_TIMER
const GAMBLE := FieldStatus.SPACE_CAKE_GAMBLE
const T0 := 600

var st
var cues


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
	cues = CUES.new()
	cues.state = st
	add_child_autofree(cues)
	watch_signals(cues)


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _listen() -> Array:
	var heard := []
	cues.space_cake_landed.connect(func(target: String, cakes: int) -> void:
		heard.append([target, cakes]))
	return heard


func _land(id: String = "chadwick", cakes: int = 1) -> void:
	for i in cakes:
		FieldStatus.apply_from_table(st, id, TIMER)
	GameClock.set_time(st, GameClock.minutes(st) + 120)


# --- landings (SC5c) ------------------------------------------------------------------------------

func test_field_cues_hands_a_landing_to_the_listener_and_drains_the_queue() -> void:
	var heard := _listen()
	_land("chadwick")
	cues.pump()
	assert_eq(heard, [["chadwick", 1]])
	assert_false(st.flags.has(FieldStatus.LANDINGS_KEY), "the queue is drained")
	cues.pump()
	assert_eq(heard.size(), 1, "a landing is handed over once")


func test_field_cues_landing_carries_the_cake_count() -> void:
	var heard := _listen()
	_land("bradley", 2)
	cues.pump()
	assert_eq(heard, [["bradley", 2]])


func test_field_cues_hands_landings_over_oldest_first() -> void:
	var heard := _listen()
	_land("chadwick")
	_land("lord_pilsner")
	cues.pump()
	assert_eq(heard, [["chadwick", 1], ["lord_pilsner", 1]])


func test_field_cues_keeps_landings_queued_while_nobody_listens() -> void:
	var quiet = CUES.new()  # not watched: GUT's watch_signals counts as a listener
	quiet.state = st
	add_child_autofree(quiet)
	_land("chadwick")
	quiet.pump()
	assert_eq(Array(st.flags.get(FieldStatus.LANDINGS_KEY, [])).size(), 1,
			"no screen layer is connected, so the cue waits")
	var heard := []
	quiet.space_cake_landed.connect(func(target: String, cakes: int) -> void:
		heard.append([target, cakes]))
	quiet.pump()
	assert_eq(heard, [["chadwick", 1]])


func test_field_cues_process_pumps_every_frame() -> void:
	var heard := _listen()
	_land("chadwick")
	cues._process(0.016)
	assert_eq(heard, [["chadwick", 1]])


func test_field_cues_without_a_state_does_nothing() -> void:
	var bare = CUES.new()
	autofree(bare)
	bare.state = null
	bare.pump()
	assert_eq(bare.timer_readout(null), [])
	pass_test("no state, no crash")


# --- teleport (T6) --------------------------------------------------------------------------------

func test_field_cues_reports_a_teleported_roll() -> void:
	var result := {"exit": "frietomat", "label": "Frietomat", "correct": false,
			"teleported": true, "lost_minutes": 30}
	assert_true(cues.report_roll(result))
	assert_signal_emitted_with_parameters(cues, "tunnel_teleported", ["frietomat", "Frietomat", 30])


func test_field_cues_ignores_a_roll_that_did_not_teleport() -> void:
	assert_false(cues.report_roll({"exit": "roodelicht_row", "label": "x", "correct": false,
			"teleported": false, "lost_minutes": 0}))
	assert_false(cues.report_roll({}))
	assert_signal_not_emitted(cues, "tunnel_teleported")


func test_field_cues_reports_a_real_navigation_teleport() -> void:
	NavigationRoll.note_item_used(st, {"alcohol": true})
	FieldStatus.apply_from_table(st, "chadwick", GAMBLE)
	var nav := NavigationRoll.new(st)
	var result := nav.roll(NavigationRoll.SIGN_CENTRAAL, {}, 99, {"teleport": 0, "destination": 0})
	assert_true(bool(result["teleported"]), "the forced draw teleports")
	assert_true(cues.report_roll(result))
	assert_signal_emitted_with_parameters(cues, "tunnel_teleported",
			[String(result["exit"]), String(result["label"]), int(result["lost_minutes"])])


# --- timer readout (SC4) --------------------------------------------------------------------------

func test_field_cues_timer_readout_is_empty_without_a_timer() -> void:
	assert_eq(cues.timer_readout(st), [])


func test_field_cues_timer_readout_gives_minutes_left_and_cakes() -> void:
	FieldStatus.apply_from_table(st, "chadwick", TIMER)
	assert_eq(cues.timer_readout(st), [{"target": "chadwick", "minutes_left": 120, "cakes": 1}])
	GameClock.set_time(st, T0 + 50)
	FieldStatus.apply_from_table(st, "chadwick", TIMER)  # SC10: joins, does not restart
	assert_eq(cues.timer_readout(st), [{"target": "chadwick", "minutes_left": 70, "cakes": 2}])


func test_field_cues_timer_readout_lists_bros_in_party_order() -> void:
	FieldStatus.apply_from_table(st, "bradley", TIMER)
	GameClock.set_time(st, T0 + 10)
	FieldStatus.apply_from_table(st, "lord_pilsner", TIMER)
	var out: Array = cues.timer_readout(st)
	assert_eq(out.size(), 2)
	assert_eq(out[0]["target"], "lord_pilsner")
	assert_eq(out[0]["minutes_left"], 120)
	assert_eq(out[1]["target"], "bradley")
	assert_eq(out[1]["minutes_left"], 110)


func test_field_cues_timer_readout_drops_a_landed_timer() -> void:
	_land("chadwick")
	assert_eq(cues.timer_readout(st), [])


func test_field_cues_emits_timer_changed_only_when_the_readout_changes() -> void:
	cues.pump()
	assert_signal_emit_count(cues, "space_cake_timer_changed", 0)
	FieldStatus.apply_from_table(st, "chadwick", TIMER)
	cues.pump()
	cues.pump()
	assert_signal_emit_count(cues, "space_cake_timer_changed", 1)
	assert_signal_emitted_with_parameters(cues, "space_cake_timer_changed",
			[[{"target": "chadwick", "minutes_left": 120, "cakes": 1}]])
	GameClock.set_time(st, T0 + 10)
	cues.pump()
	assert_signal_emit_count(cues, "space_cake_timer_changed", 2)
	GameClock.rest(st)  # SC11: rest clears a timer that has not landed
	cues.pump()
	assert_signal_emit_count(cues, "space_cake_timer_changed", 3)
	assert_signal_emitted_with_parameters(cues, "space_cake_timer_changed", [[]])


# --- Gamble live (SC7) ----------------------------------------------------------------------------

func test_field_cues_gamble_live_follows_the_status() -> void:
	assert_false(cues.gamble_live(st))
	_land("chadwick")
	assert_true(cues.gamble_live(st))
	GameClock.set_time(st, GameClock.minutes(st) + 90)
	assert_false(cues.gamble_live(st))


func test_field_cues_emits_gamble_changed_on_and_off_once_each() -> void:
	cues.pump()
	assert_signal_emit_count(cues, "space_cake_gamble_changed", 0)
	_land("chadwick")
	cues.pump()
	cues.pump()
	assert_signal_emit_count(cues, "space_cake_gamble_changed", 1)
	assert_signal_emitted_with_parameters(cues, "space_cake_gamble_changed", [true])
	GameClock.set_time(st, GameClock.minutes(st) + 90)
	cues.pump()
	assert_signal_emit_count(cues, "space_cake_gamble_changed", 2)
	assert_signal_emitted_with_parameters(cues, "space_cake_gamble_changed", [false])
