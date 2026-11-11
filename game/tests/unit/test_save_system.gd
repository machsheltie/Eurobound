extends GutTest

var saver
var state

func before_each() -> void:
	saver = autofree(load("res://core/save_system.gd").new())
	saver.save_path = "user://saves/test_slot.json"
	var repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load("res://core/game_state.gd").new())
	state.new_game(repo)
	if FileAccess.file_exists(saver.save_path):
		DirAccess.remove_absolute(saver.save_path)

func after_each() -> void:
	if FileAccess.file_exists(saver.save_path):
		DirAccess.remove_absolute(saver.save_path)

func test_no_save_initially() -> void:
	assert_false(saver.has_save())

func test_save_then_load_round_trip() -> void:
	state.sovs = 77
	state.set_flag("saved_once")
	assert_true(saver.save_game(state))
	assert_true(saver.has_save())
	var fresh = autofree(load("res://core/game_state.gd").new())
	assert_true(saver.load_game(fresh))
	assert_eq(fresh.sovs, 77)
	assert_true(fresh.has_flag("saved_once"))

func test_corrupt_save_is_not_loadable() -> void:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var f := FileAccess.open(saver.save_path, FileAccess.WRITE)
	f.store_string("{ this is not json")
	f.close()
	assert_false(saver.has_save())
	assert_false(saver.load_game(state))
	assert_eq(state.sovs, 20, "failed load must leave state untouched")

## A pre-SP-rename save (or any save missing save_version) must be rejected
## cleanly, not crash battle_manager.gd on a missing "bravado" key. Author
## ruling, 2026-08-06: reject incompatible saves, do not migrate them.
func test_pre_rename_save_without_version_is_not_loadable() -> void:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var legacy_save := {
		"party": [{"id": "lord_pilsner", "sp": 5, "max_sp": 12}],
		"inventory": {},
		"gold": 999,
		"flags": {},
		"current_scene_path": "",
		"player_position": {"x": 0, "y": 0},
	}
	var f := FileAccess.open(saver.save_path, FileAccess.WRITE)
	f.store_string(JSON.stringify(legacy_save))
	f.close()
	assert_false(saver.has_save(), "unversioned save must not report as a usable save")
	assert_false(saver.load_game(state), "unversioned save must be rejected, not migrated")
	assert_eq(state.sovs, 20, "rejected load must leave state untouched")

## A save stamped with an older/mismatched save_version must also be rejected.
func test_old_version_save_is_not_loadable() -> void:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var old_save := {
		"save_version": state.SAVE_VERSION - 1,
		"party": [],
		"inventory": {},
		"gold": 999,
		"flags": {},
		"current_scene_path": "",
		"player_position": {"x": 0, "y": 0},
	}
	var f := FileAccess.open(saver.save_path, FileAccess.WRITE)
	f.store_string(JSON.stringify(old_save))
	f.close()
	assert_false(saver.has_save())
	assert_false(saver.load_game(state))
	assert_eq(state.sovs, 20, "rejected load must leave state untouched")

## A current-version save written before the SOVS rename keeps its wallet under "gold"; it must still load.
func test_pre_sovs_rename_save_wallet_still_loads() -> void:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var f := FileAccess.open(saver.save_path, FileAccess.WRITE)
	f.store_string(JSON.stringify({
		"save_version": state.SAVE_VERSION,
		"party": [],
		"inventory": {},
		"gold": 42,
		"flags": {},
		"current_scene_path": "",
		"player_position": {"x": 0, "y": 0},
	}))
	f.close()
	var fresh = autofree(load("res://core/game_state.gd").new())
	assert_true(saver.load_game(fresh))
	assert_eq(fresh.sovs, 42)
