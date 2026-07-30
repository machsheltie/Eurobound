extends GutTest

var saver
var state

func before_each() -> void:
	saver = load("res://Scripts/core/save_system.gd").new()
	var repo = load("res://Scripts/core/data_repo.gd").new()
	repo.load_all()
	state = load("res://Scripts/systems/GameState.gd").new()
	state.new_game(repo)
	if FileAccess.file_exists(saver.SAVE_PATH):
		DirAccess.remove_absolute(saver.SAVE_PATH)

func test_no_save_initially() -> void:
	assert_false(saver.has_save())

func test_save_then_load_round_trip() -> void:
	state.gold = 77
	state.set_flag("saved_once")
	assert_true(saver.save_game(state))
	assert_true(saver.has_save())
	var fresh = load("res://Scripts/systems/GameState.gd").new()
	assert_true(saver.load_game(fresh))
	assert_eq(fresh.gold, 77)
	assert_true(fresh.has_flag("saved_once"))

func test_corrupt_save_is_not_loadable() -> void:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var f := FileAccess.open(saver.SAVE_PATH, FileAccess.WRITE)
	f.store_string("{ this is not json")
	f.close()
	assert_false(saver.has_save())
	assert_false(saver.load_game(state))
	assert_eq(state.gold, 20, "failed load must leave state untouched")
