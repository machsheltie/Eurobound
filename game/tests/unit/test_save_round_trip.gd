extends GutTest
## Eurobound-x2ws: a save written to disk and read back restores the whole run (wallet, flags,
## inventory, statuses, clock, location, party), and SaveSystem.save_now() is the one call a save
## trigger (hotspot, bed, autosave) makes.

const SAVE_SCRIPT := "res://core/save_system.gd"
const STATE_SCRIPT := "res://core/game_state.gd"

var saver
var state


class FakeSaver:
	var reasons := []
	func save_now(reason: String = "", _state = null) -> bool:
		reasons.append(reason)
		return true


func before_each() -> void:
	saver = autofree(load(SAVE_SCRIPT).new())
	saver.save_path = "user://saves/test_round_trip.json"
	var repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load(STATE_SCRIPT).new())
	state.new_game(repo)
	_wipe()


func after_each() -> void:
	_wipe()
	SceneRouter.pending_spot = {}
	SceneRouter.pending_spawn = ""


func _wipe() -> void:
	for p in [saver.save_path, saver.save_path + ".tmp"]:
		if FileAccess.file_exists(p):
			DirAccess.remove_absolute(p)


func _reload():
	var fresh = autofree(load(STATE_SCRIPT).new())
	assert_true(saver.load_game(fresh), "the save loads")
	return fresh


## Values as JSON sees them (one number type). Systems that keep their own rows in `flags`
## (FieldStatus, ...) read numbers with int()/float(), so 4390 and 4390.0 are the same save.
func _as_json(value: Variant) -> String:
	return JSON.stringify(JSON.parse_string(JSON.stringify(value)), "", true, true)


# --- the round trip through the file ---------------------------------------------------------

func test_save_round_trip_file_restores_the_exact_state() -> void:
	# Arrange: something in every part of the state
	state.sovs = 137
	state.add_item("absinthe_shot", 3)
	state.set_flag("met_someone")
	state.deposit_coin("some_coin", 4)
	state.party[1]["hp"] = 7
	state.party[2]["xp"] = 55
	GameClock.set_time(state, 2 * GameClock.DAY + 23 * 60 + 40)
	FieldStatus.apply(state, "lord_pilsner", FieldStatus.EMBARRASSED, 90)
	state.current_scene_path = "res://worlds/somewhere.tscn"
	state.player_spot = {"x": 1.5, "y": 0.0, "z": -4.25, "facing": "west"}
	var before: Dictionary = state.to_dict()
	# Act
	assert_true(saver.save_game(state))
	var fresh = _reload()
	# Assert
	var after: Dictionary = fresh.to_dict()
	for key in before:
		assert_eq(_as_json(after[key]), _as_json(before[key]), key)
	assert_eq(after.keys().size(), before.keys().size())


func test_save_round_trip_numbers_come_back_as_ints() -> void:
	# JSON has one number type; counts and stats must not come back as floats.
	state.add_item("absinthe_shot", 3)
	saver.save_game(state)
	var fresh = _reload()
	assert_eq(typeof(fresh.sovs), TYPE_INT)
	assert_eq(typeof(fresh.inventory["absinthe_shot"]), TYPE_INT)
	for member in fresh.party:
		for key in ["level", "xp", "hp", "max_hp", "bravado", "max_bravado", "offense", "defense",
				"speed", "charm", "luck", "grit"]:
			assert_eq(typeof(member[key]), TYPE_INT, "%s.%s" % [member["id"], key])


func test_save_round_trip_clock_and_statuses_keep_working() -> void:
	GameClock.set_time(state, 23 * 60 + 40)
	FieldStatus.apply(state, "lord_pilsner", FieldStatus.EMBARRASSED, 90)
	saver.save_game(state)
	var fresh = _reload()
	assert_eq(GameClock.watch_text(fresh), "23:40")
	assert_true(GameClock.is_night(fresh))
	assert_true(FieldStatus.has(fresh, FieldStatus.EMBARRASSED, "lord_pilsner"))
	GameClock.act(fresh, "fight")
	assert_eq(GameClock.watch_text(fresh), "00:00")


func test_save_round_trip_loaded_state_is_detached_from_the_file_data() -> void:
	saver.save_game(state)
	var a = _reload()
	var b = _reload()
	a.party[0]["hp"] = 1
	a.flags["only_a"] = true
	assert_ne(int(b.party[0]["hp"]), 1)
	assert_false(b.has_flag("only_a"))


func test_save_round_trip_second_save_replaces_the_first() -> void:
	state.sovs = 1
	assert_true(saver.save_game(state))
	state.sovs = 2
	assert_true(saver.save_game(state))
	assert_eq(_reload().sovs, 2)
	assert_false(FileAccess.file_exists(saver.save_path + ".tmp"), "no temp file left behind")


func test_save_round_trip_old_save_without_a_spot_loads_with_none() -> void:
	var d: Dictionary = state.to_dict()
	d.erase("player_spot")
	DirAccess.make_dir_recursive_absolute("user://saves")
	var f := FileAccess.open(saver.save_path, FileAccess.WRITE)
	f.store_string(JSON.stringify(d))
	f.close()
	assert_eq(_reload().player_spot, {})


# --- location --------------------------------------------------------------------------------

func _world_with_player(pos: Vector3, facing: String) -> Node3D:
	var world := Node3D.new()
	add_child_autofree(world)
	var player := PlayerController.new()
	player.position = pos
	world.add_child(player)
	player.face(facing)
	return world


func test_save_capture_location_records_scene_and_player_spot() -> void:
	var world := _world_with_player(Vector3(2.5, 0.0, -3.0), "east")
	saver.capture_location(state, world, "res://worlds/somewhere.tscn")
	assert_eq(state.current_scene_path, "res://worlds/somewhere.tscn")
	assert_eq(state.player_spot, {"x": 2.5, "y": 0.0, "z": -3.0, "facing": "east"})


func test_save_capture_location_without_a_world_keeps_what_was_there() -> void:
	state.current_scene_path = "res://worlds/kept.tscn"
	state.player_spot = {"x": 1.0, "y": 0.0, "z": 1.0, "facing": "north"}
	saver.capture_location(state, null, "")
	assert_eq(state.current_scene_path, "res://worlds/kept.tscn")
	assert_eq(String(state.player_spot["facing"]), "north")


func test_scene_router_spawns_the_player_on_a_loaded_spot() -> void:
	var world := Node3D.new()
	add_child_autofree(world)
	SceneRouter.add_spawn_point(world, "start", Vector3(9, 0, 9), "south")
	SceneRouter.pending_spot = {"x": 2.5, "y": 0.0, "z": -3.0, "facing": "east"}
	var player := SceneRouter.spawn_player(world, "start")
	assert_almost_eq(player.position, Vector3(2.5, 0.0, -3.0), Vector3.ONE * 0.001)
	assert_eq(player.sprite.facing, "east")
	assert_eq(SceneRouter.pending_spot, {}, "used once")


func test_scene_router_without_a_loaded_spot_uses_the_spawn_point() -> void:
	var world := Node3D.new()
	add_child_autofree(world)
	SceneRouter.add_spawn_point(world, "start", Vector3(9, 0, 9), "north")
	var player := SceneRouter.spawn_player(world, "start")
	assert_almost_eq(player.position, Vector3(9, 0, 9), Vector3.ONE * 0.001)


# --- the entry point -------------------------------------------------------------------------

func test_save_now_writes_the_given_state_and_reports_it() -> void:
	watch_signals(saver)
	state.sovs = 314
	assert_true(saver.save_now("test", state))
	assert_true(saver.has_save())
	assert_eq(_reload().sovs, 314)
	assert_signal_emitted_with_parameters(saver, "saved", ["test"])


func test_save_now_failure_emits_nothing() -> void:
	watch_signals(saver)
	saver.save_path = "user://saves/no_such_dir_x2ws/slot.json"
	assert_false(saver.save_now("test", state))
	assert_signal_not_emitted(saver, "saved")


func test_prepare_resume_hands_the_spot_to_the_scene_router() -> void:
	state.player_spot = {"x": 1.0, "y": 0.0, "z": 2.0, "facing": "north"}
	saver.prepare_resume(state)
	assert_eq(SceneRouter.pending_spot, state.player_spot)


# --- the ruled save point: FREE Wi-Fi (NEXT_WORK.md:700, round v36) ----------------------------

class FakeState:
	var flags := {}


func _run_hotspot(h: WifiHotspot) -> void:
	var done := [false]
	h.hijack_finished.connect(func(_who, _first): done[0] = true)
	h.interact()
	for i in 300:
		if done[0]:
			break
		if h.dialogue.mode == "say":
			h.dialogue.press("interact")
		await wait_process_frames(1)


func test_wifi_hotspot_saves_once_the_connection_ends() -> void:
	var h: WifiHotspot = load("res://worlds/shared/icq/wifi_hotspot.tscn").instantiate()
	h.state = FakeState.new()
	var fake := FakeSaver.new()
	h.saver = fake
	h.dialogue = DialogueBox.new()
	h.dialogue.beat_scale = 0.01
	h.add_child(h.dialogue)
	add_child_autofree(h)
	await _run_hotspot(h)
	assert_eq(fake.reasons, ["hotspot"])
	assert_true(h.state.flags.get("tony420_unlocked", false), "saved after the hijack set its flags")


func test_wifi_hotspot_with_an_injected_state_and_no_saver_never_touches_the_real_save() -> void:
	var h: WifiHotspot = load("res://worlds/shared/icq/wifi_hotspot.tscn").instantiate()
	h.state = FakeState.new()
	add_child_autofree(h)
	assert_null(h.saver)
