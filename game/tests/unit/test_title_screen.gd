extends GutTest
## Eurobound-9jzp: the title screen (New Game, Continue, Quit).

const TEST_DIR := "user://saves/test_title_9jzp"

var saver
var state
var repo
var title


func before_each() -> void:
	saver = load("res://core/save_system.gd").new()
	saver.save_dir = TEST_DIR
	add_child_autofree(saver)
	repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load("res://core/game_state.gd").new())
	_wipe()


func after_each() -> void:
	_wipe()
	DirAccess.remove_absolute(TEST_DIR)


func _wipe() -> void:
	for slot in range(1, 5):
		DirAccess.remove_absolute(saver.slot_path(slot))
		DirAccess.remove_absolute(saver.slot_path(slot) + ".tmp")


func _make() -> void:
	title = load("res://ui/title_screen.tscn").instantiate()
	title.saver = saver
	title.state = state
	title.repo = repo
	title.navigate = false
	add_child_autofree(title)


func test_main_scene_is_the_title() -> void:
	assert_eq(ProjectSettings.get_setting("application/run/main_scene"), "res://ui/title_screen.tscn")


func test_plain_labels() -> void:
	_make()
	assert_eq(title.new_game_button.text, "New Game")
	assert_eq(title.continue_button.text, "Continue")
	assert_eq(title.quit_button.text, "Quit")


func test_no_save_disables_continue_and_focuses_new_game() -> void:
	_make()
	assert_true(title.continue_button.disabled)
	assert_false(title.new_game_button.disabled)
	assert_true(title.new_game_button.has_focus())


func test_valid_save_enables_continue() -> void:
	state.new_game(repo)
	assert_true(saver.save_to_slot(state, 2, "test"))
	_make()
	assert_false(title.continue_button.disabled)


func test_rejected_save_keeps_continue_disabled() -> void:
	DirAccess.make_dir_recursive_absolute(TEST_DIR)
	var f := FileAccess.open(saver.slot_path(1), FileAccess.WRITE)
	f.store_string('{"save_version": 9999}')
	f.close()
	var g := FileAccess.open(saver.slot_path(2), FileAccess.WRITE)
	g.store_string("not json")
	g.close()
	_make()
	assert_true(title.continue_button.disabled)
	assert_true(title.new_game_button.has_focus())


func test_new_game_starts_fresh_state_and_enters_arcade_street() -> void:
	state.sovs = 999
	state.flags = {"old": true}
	_make()
	watch_signals(title)
	title.new_game_button.pressed.emit()
	assert_eq(state.sovs, 20)
	assert_false(state.flags.has("old"))
	assert_eq((state.party as Array).size(), 3)
	assert_signal_emitted_with_parameters(title, "scene_requested", [SceneRouter.scene_path("absinthe_arcade_exterior")])
	assert_true(ResourceLoader.exists(SceneRouter.scene_path("absinthe_arcade_exterior")))


func test_quit_requests_quit() -> void:
	_make()
	watch_signals(title)
	title.quit_button.pressed.emit()
	assert_signal_emitted(title, "quit_requested")


func test_continue_opens_picker_and_loads_chosen_slot() -> void:
	state.new_game(repo)
	state.sovs = 77
	saver.save_to_slot(state, 1, "test")
	state.sovs = 5
	_make()
	watch_signals(title)
	title.continue_button.pressed.emit()
	assert_not_null(title.picker)
	title.picker.press("interact")  # cursor starts on slot 1
	await wait_frames(2)
	assert_eq(state.sovs, 77)
	assert_signal_emitted(title, "scene_requested")
	assert_null(title.picker)
