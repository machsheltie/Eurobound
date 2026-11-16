extends GutTest
## Eurobound-x2ws: three save slots (author, NEXT_WORK.md:892), and a slot picker every time the
## game saves (hotspot or bed) and in Load (author, Eurobound Desk Eurobound-x2ws-q3).

const SAVE_SCRIPT := "res://core/save_system.gd"
const STATE_SCRIPT := "res://core/game_state.gd"
const TEST_DIR := "user://saves/test_slots_x2ws"

var saver
var state


func before_each() -> void:
	saver = load(SAVE_SCRIPT).new()
	saver.save_dir = TEST_DIR
	add_child_autofree(saver)
	var repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load(STATE_SCRIPT).new())
	state.new_game(repo)
	_wipe()


func after_each() -> void:
	_wipe()
	DirAccess.remove_absolute(TEST_DIR)


func _wipe() -> void:
	for slot in range(1, 5):
		for p in [saver.slot_path(slot), saver.slot_path(slot) + ".tmp"]:
			if FileAccess.file_exists(p):
				DirAccess.remove_absolute(p)


func _fresh():
	return autofree(load(STATE_SCRIPT).new())


# --- slots in SaveSystem ---------------------------------------------------------------------

func test_save_slots_there_are_three() -> void:
	assert_eq(saver.SLOT_COUNT, 3)


func test_save_slots_the_existing_single_save_is_slot_1() -> void:
	# Before slots the one save lived at user://saves/slot1.json: slot 1 is that same file, so an
	# existing save shows up as slot 1 with nothing to move.
	var plain = autofree(load(SAVE_SCRIPT).new())
	assert_eq(plain.slot_path(1), "user://saves/slot1.json")
	assert_eq(plain.slot_path(1), plain.save_path, "the old save path is slot 1")


func test_save_slots_a_save_written_the_old_way_loads_as_slot_1() -> void:
	# Arrange: the pre-slot code wrote save_path (slot1.json) directly.
	saver.save_path = saver.slot_path(1)
	state.sovs = 61
	assert_true(saver.save_game(state))
	# Act / Assert
	assert_true(saver.has_slot(1))
	var fresh = _fresh()
	assert_true(saver.load_slot(fresh, 1))
	assert_eq(fresh.sovs, 61)


func test_save_slots_saving_to_a_slot_touches_only_that_slot() -> void:
	state.sovs = 222
	assert_true(saver.save_to_slot(state, 2, "test"))
	assert_true(saver.has_slot(2))
	assert_false(saver.has_slot(1))
	assert_false(saver.has_slot(3))
	var fresh = _fresh()
	assert_true(saver.load_slot(fresh, 2))
	assert_eq(fresh.sovs, 222)


func test_save_slots_each_slot_keeps_its_own_save() -> void:
	state.sovs = 1
	saver.save_to_slot(state, 1)
	state.sovs = 3
	saver.save_to_slot(state, 3)
	var a = _fresh()
	var c = _fresh()
	saver.load_slot(a, 1)
	saver.load_slot(c, 3)
	assert_eq(a.sovs, 1)
	assert_eq(c.sovs, 3)


func test_save_slots_out_of_range_slots_are_refused() -> void:
	assert_false(saver.save_to_slot(state, 0))
	assert_false(saver.save_to_slot(state, 4))
	assert_false(FileAccess.file_exists(saver.slot_path(4)))
	assert_false(saver.load_slot(_fresh(), 4))
	assert_false(saver.has_slot(0))


func test_save_slots_loading_an_empty_slot_fails_and_leaves_the_state_alone() -> void:
	var fresh = _fresh()
	fresh.sovs = 9
	assert_false(saver.load_slot(fresh, 2))
	assert_eq(fresh.sovs, 9)


func test_save_slots_has_any_save() -> void:
	assert_false(saver.has_any_save())
	saver.save_to_slot(state, 3)
	assert_true(saver.has_any_save())


func test_save_slots_save_to_slot_emits_saved_with_the_reason() -> void:
	watch_signals(saver)
	saver.save_to_slot(state, 1, "bed")
	assert_signal_emitted_with_parameters(saver, "saved", ["bed"])


func test_save_slots_info_is_empty_for_an_empty_slot() -> void:
	assert_eq(saver.slot_info(1), {})


func test_save_slots_info_reads_what_the_save_holds() -> void:
	state.sovs = 137
	state.current_scene_path = "res://worlds/somewhere.tscn"
	GameClock.set_time(state, GameClock.DAY + 23 * 60 + 40)
	saver.save_to_slot(state, 2)
	var info: Dictionary = saver.slot_info(2)
	assert_eq(info.get("scene"), "res://worlds/somewhere.tscn")
	assert_eq(info.get("time"), "23:40")
	assert_eq(info.get("sovs"), 137)


# --- the picker ------------------------------------------------------------------------------

func _picker(purpose: String) -> SaveSlotPicker:
	var p := SaveSlotPicker.new()
	p.setup(saver, purpose)
	add_child_autofree(p)
	return p


func test_save_slot_picker_rows_are_the_three_slots_and_cancel() -> void:
	saver.save_to_slot(state, 2)
	var p := _picker("save")
	var rows := p.row_labels()
	assert_eq(rows.size(), 4)
	assert_true(rows[0].begins_with("Slot 1"))
	assert_true(rows[0].contains("Empty"))
	assert_true(rows[1].begins_with("Slot 2"))
	assert_false(rows[1].contains("Empty"))
	assert_true(rows[2].contains("Empty"))
	assert_eq(rows[3], "Cancel")


func test_save_slot_picker_filled_slot_shows_its_info() -> void:
	state.sovs = 137
	GameClock.set_time(state, 23 * 60 + 40)
	saver.save_to_slot(state, 1)
	var rows := _picker("load").row_labels()
	assert_true(rows[0].contains("23:40"), rows[0])
	assert_true(rows[0].contains("SOVS 137"), rows[0])


func test_save_slot_picker_save_picks_any_slot() -> void:
	var p := _picker("save")
	watch_signals(p)
	p.press("move_down")
	p.press("interact")
	assert_signal_emitted_with_parameters(p, "picked", [2])


func test_save_slot_picker_cancel_row_returns_zero() -> void:
	var p := _picker("save")
	watch_signals(p)
	p.press("move_up")  # wraps to Cancel
	p.press("interact")
	assert_signal_emitted_with_parameters(p, "picked", [0])


func test_save_slot_picker_cancel_button_returns_zero() -> void:
	for action in ["cancel", "menu"]:
		var p := _picker("load")
		watch_signals(p)
		p.press(action)
		assert_signal_emitted_with_parameters(p, "picked", [0])


func test_save_slot_picker_load_ignores_empty_slots() -> void:
	saver.save_to_slot(state, 2)
	var p := _picker("load")
	watch_signals(p)
	p.press("interact")  # slot 1 is empty
	assert_signal_not_emitted(p, "picked")
	p.press("move_down")
	p.press("interact")
	assert_signal_emitted_with_parameters(p, "picked", [2])


func test_save_slot_picker_pick_returns_the_slot() -> void:
	var p := _picker("save")
	var got := [-1]
	var run := func() -> void: got[0] = await p.pick()
	run.call()
	p.press("move_down")
	p.press("move_down")
	p.press("interact")
	await wait_process_frames(1)
	assert_eq(got[0], 3)


func test_save_slot_picker_pending_words_are_blank_until_the_author_gives_them() -> void:
	# Eurobound Desk Eurobound-x2ws-q4: no agent writes these lines.
	for key in SaveSlotPicker.PENDING_LINES:
		assert_eq(SaveSlotPicker.PENDING_LINES[key], "", key)


# --- the one call hotspots and beds make -----------------------------------------------------

func test_save_with_picker_saves_to_the_picked_slot() -> void:
	watch_signals(saver)
	state.sovs = 404
	var got := [null]
	var run := func() -> void: got[0] = await saver.save_with_picker("bed", state)
	run.call()
	assert_not_null(saver.picker, "the picker is up")
	saver.picker.press("move_down")
	saver.picker.press("interact")
	await wait_process_frames(2)
	assert_eq(got[0], true)
	assert_true(saver.has_slot(2))
	assert_false(saver.has_slot(1))
	assert_signal_emitted_with_parameters(saver, "saved", ["bed"])
	assert_null(saver.picker, "the picker is gone")


func test_save_with_picker_cancelled_saves_nothing() -> void:
	watch_signals(saver)
	var got := [null]
	var run := func() -> void: got[0] = await saver.save_with_picker("hotspot", state)
	run.call()
	saver.picker.press("cancel")
	await wait_process_frames(2)
	assert_eq(got[0], false)
	assert_false(saver.has_any_save())
	assert_signal_not_emitted(saver, "saved")


# --- Load in the field menu ------------------------------------------------------------------

func _menu() -> FieldMenu:
	var m := FieldMenu.new()
	m.setup(state)
	m.saver = saver
	add_child_autofree(m)
	m.mode = "Load / Quit"
	m.cursor = 0
	return m


func test_field_menu_load_opens_the_slot_picker() -> void:
	var m := _menu()
	m.press("interact")
	assert_eq(m.mode, "load_pick")
	assert_not_null(m.picker)
	assert_eq(m.picker.purpose, "load")


func test_field_menu_load_picker_cancel_goes_back() -> void:
	var m := _menu()
	m.press("interact")
	m.press("cancel")
	await wait_process_frames(1)
	assert_eq(m.mode, "Load / Quit")
	assert_null(m.picker)


func test_field_menu_load_picked_slot_loads_it() -> void:
	state.sovs = 555
	saver.save_to_slot(state, 3)
	state.sovs = 1
	var m := _menu()
	watch_signals(m)
	m.press("interact")
	m.press("move_down")
	m.press("move_down")
	m.press("interact")
	assert_eq(state.sovs, 555)
	assert_signal_emitted(m, "closed")
