extends GutTest
## Eurobound-vxa4: the 12-Bed Mixed Dorm rest point (rules 9-16, Desk Eurobound-8snp-q1).

const STATE_SCRIPT := "res://core/game_state.gd"
const SAVE_SCRIPT := "res://core/save_system.gd"
const TEST_DIR := "user://saves/test_rest_point_vxa4"
const DORM := "hmc_dorm_12_bed"

var state
var saver
var rp: RestPoint


func before_each() -> void:
	saver = load(SAVE_SCRIPT).new()
	saver.save_dir = TEST_DIR
	add_child_autofree(saver)
	var repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load(STATE_SCRIPT).new())
	state.new_game(repo)
	rp = RestPoint.from_id(DORM)
	_wipe()


func after_each() -> void:
	_wipe()
	DirAccess.remove_absolute(TEST_DIR)


func _wipe() -> void:
	for slot in range(1, 5):
		for p in [saver.slot_path(slot), saver.slot_path(slot) + ".tmp"]:
			if FileAccess.file_exists(p):
				DirAccess.remove_absolute(p)


func test_rest_point_dorm_is_12_sovs_with_no_events_and_no_roll() -> void:
	assert_not_null(rp)
	assert_eq(rp.price(), 12)
	assert_false(bool(rp.data["roommate_events"]))
	assert_false(bool(rp.data["sleep_roll"]))


func test_rest_point_cannot_afford_means_no_bed() -> void:
	state.sovs = 11
	assert_false(rp.book(state))
	assert_eq(state.sovs, 11, "nothing taken")
	assert_false(rp.is_booked(state))
	var slept: bool = await rp.sleep(state, null)
	assert_false(slept, "no booking, no rest")


func test_rest_point_pays_and_rests() -> void:
	state.sovs = 50
	assert_true(rp.book(state))
	assert_eq(state.sovs, 38)
	assert_true(rp.is_booked(state))
	var slept: bool = await rp.sleep(state, null)
	assert_true(slept)
	assert_false(rp.is_booked(state), "the booking buys one rest")
	assert_eq(state.sovs, 38, "no second charge")


func test_rest_point_a_booked_bed_is_not_paid_twice() -> void:
	state.sovs = 50
	rp.book(state)
	assert_false(rp.book(state))
	assert_eq(state.sovs, 38)


func test_rest_point_clock_goes_to_ten_oclock() -> void:
	state.sovs = 12
	GameClock.set_time(state, 3 * 1440 + 90)
	rp.book(state)
	await rp.sleep(state, null)
	assert_eq(GameClock.minutes(state), 3 * 1440 + 600)
	assert_eq(GameClock.watch_text(state), "10:00")


func test_rest_point_ruled_statuses_clear_and_rule_16_ones_stay() -> void:
	state.sovs = 12
	FieldStatus.apply_from_table(state, "bradley", "imperial_hangover")
	FieldStatus.apply_from_table(state, "bradley", "cottonmouth")
	FieldStatus.apply_from_table(state, "bradley", "munchies")
	FieldStatus.apply_from_table(state, "bradley", "contact_high")
	FieldStatus.apply_from_table(state, "bradley", "gush_locked")
	var before := FieldStatus.has(state, "gush_locked", "bradley")
	rp.book(state)
	await rp.sleep(state, null)
	for gone in ["imperial_hangover", "cottonmouth", "munchies", "contact_high"]:
		assert_false(FieldStatus.has(state, gone, "bradley"), gone)
	assert_eq(FieldStatus.has(state, "gush_locked", "bradley"), before, "Gush-Locked is not ended by a rest")


func test_rest_point_save_is_offered_before_the_rest() -> void:
	state.sovs = 12
	GameClock.set_time(state, 1440 + 60)
	rp.book(state)
	var got := [null]
	var run := func() -> void: got[0] = await rp.sleep(state, saver)
	run.call()
	assert_not_null(saver.picker, "the picker is up")
	assert_eq(GameClock.minutes(state), 1440 + 60, "not rested yet")
	saver.picker.press("interact")
	await wait_process_frames(2)
	assert_eq(got[0], true)
	assert_true(saver.has_slot(1))
	assert_eq(GameClock.minutes(state), 1440 + 600)
	var saved: Variant = JSON.parse_string(FileAccess.get_file_as_string(saver.slot_path(1)))
	assert_true(saved is Dictionary, "slot 1 holds a save")
	assert_true(JSON.stringify(saved).contains("rest_booked_" + DORM), "the save was made before the rest (still booked)")


func test_rest_point_cancelling_the_save_still_rests_and_saves_nothing() -> void:
	state.sovs = 12
	rp.book(state)
	var run := func() -> void: await rp.sleep(state, saver)
	run.call()
	saver.picker.press("cancel")
	await wait_process_frames(2)
	assert_false(saver.has_any_save())
	assert_false(rp.is_booked(state))
	assert_eq(GameClock.watch_text(state), "10:00")


func test_rest_point_restore_stays_disabled_until_ruled() -> void:
	state.sovs = 12
	assert_false(rp.restore_enabled())
	assert_null(rp.data["restore"]["hp_pct"])
	assert_null(rp.data["restore"]["bravado_pct"])
	state.party[0]["hp"] = 1
	state.party[0]["bravado"] = 0
	rp.book(state)
	await rp.sleep(state, null)
	assert_eq(state.party[0]["hp"], 1)
	assert_eq(state.party[0]["bravado"], 0)
	assert_eq(rp.data["restore"]["status"], "pending")


func test_rest_point_a_ruled_number_drops_in_from_data() -> void:
	# Wiring check only: a made-up test value in a copy of the row, not a ruling.
	var row: Dictionary = rp.data.duplicate(true)
	row["restore"] = {"status": "test", "hp_pct": 50, "bravado_pct": 25}
	var wired := RestPoint.from_data(row)
	state.sovs = 12
	state.party[0]["hp"] = 1
	state.party[0]["bravado"] = 0
	wired.book(state)
	await wired.sleep(state, null)
	assert_true(wired.restore_enabled())
	var mx := int(state.party[0]["max_hp"])
	assert_eq(state.party[0]["hp"], mini(mx, 1 + ceili(mx * 0.5)))
	assert_gt(int(state.party[0]["bravado"]), 0)


func test_rest_point_stand_in_scene_books_then_sleeps() -> void:
	var scene: RestPointStandIn = load("res://tests/fixtures/rest_point_stand_in.tscn").instantiate()
	scene.state = state
	scene.saver = null
	scene.rest_point = rp
	add_child_autofree(scene)
	watch_signals(scene)
	state.sovs = 5
	assert_false(scene.interact_reception())
	assert_signal_emitted(scene, "refused")
	state.sovs = 12
	assert_true(scene.interact_reception())
	assert_signal_emitted_with_parameters(scene, "booked", [rp.line("booked")])
	var ok: bool = await scene.interact_bed()
	assert_true(ok)
	assert_signal_emitted(scene, "slept")
	assert_eq(state.sovs, 0)


func test_rest_point_no_groggy_is_applied() -> void:
	state.sovs = 12
	rp.book(state)
	await rp.sleep(state, null)
	assert_false(FieldStatus.has(state, "groggy"))
