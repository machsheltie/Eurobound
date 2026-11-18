extends GutTest
## Settings rows (Eurobound-c1gt): reduced motion and prompt style; stored under
## GameState.flags "settings.<name>", applied, and kept through a save round trip.

const STATE_SCRIPT := "res://core/game_state.gd"
const SAVE_SCRIPT := "res://core/save_system.gd"


class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []
	var current_scene_path := ""


func _open(s) -> FieldMenu:
	var m := FieldMenu.new()
	m.setup(s)
	add_child_autofree(m)
	m.section = m.sections().find("Settings")
	m.press("interact")
	return m


func test_settings_reduced_motion_row_toggles_and_the_arcade_fx_reads_it() -> void:
	var s := FakeState.new()
	var m := _open(s)
	assert_eq(m.mode, "Settings")
	m.press("interact")
	assert_true(s.flags["settings.reduced_motion"])
	assert_true(ArcadeAmbientFx.is_reduced(s), "applied")
	m.press("interact")
	assert_false(ArcadeAmbientFx.is_reduced(s))


func test_settings_prompt_style_row_defaults_to_keyboard_and_toggles() -> void:
	var s := FakeState.new()
	var m := _open(s)
	assert_eq(GameSettings.prompt_style(s), "keyboard")
	m.press("move_down")
	assert_eq(m.cursor, 1)
	m.press("interact")
	assert_eq(s.flags["settings.prompt_style"], "controller")
	assert_string_contains(m._body.text, "Confirm  A", "the controls list follows the style")
	assert_false(m._body.text.contains("WASD"))
	m.press("interact")
	assert_string_contains(m._body.text, "WASD")


func test_settings_cursor_wraps_and_back_leaves_to_the_root() -> void:
	var s := FakeState.new()
	var m := _open(s)
	m.press("move_up")
	assert_eq(m.cursor, GameSettings.ROWS.size() - 1)
	m.press("move_down")
	assert_eq(m.cursor, 0)
	m.press("cancel")
	assert_eq(m.mode, "root")


func test_settings_prompt_style_rejects_unknown_values() -> void:
	var s := FakeState.new()
	assert_false(GameSettings.set_prompt_style(s, "touch"))
	s.flags["settings.prompt_style"] = "garbage"
	assert_eq(GameSettings.prompt_style(s), "keyboard")


func test_settings_values_survive_a_save_round_trip() -> void:
	var saver = autofree(load(SAVE_SCRIPT).new())
	saver.save_path = "user://saves/test_settings_rows.json"
	var repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	var state = autofree(load(STATE_SCRIPT).new())
	state.new_game(repo)
	GameSettings.set_reduced_motion(state, true)
	GameSettings.set_prompt_style(state, "controller")
	assert_true(saver.save_game(state))
	var fresh = autofree(load(STATE_SCRIPT).new())
	assert_true(saver.load_game(fresh))
	assert_true(GameSettings.reduced_motion(fresh))
	assert_eq(GameSettings.prompt_style(fresh), "controller")
	for p in [saver.save_path, saver.save_path + ".tmp"]:
		if FileAccess.file_exists(p):
			DirAccess.remove_absolute(p)
