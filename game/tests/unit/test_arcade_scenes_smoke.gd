extends GutTest
## Smoke tests for the five Absinthe Arcade screens: each loads and runs a few frames without an
## engine or script error, spawns exactly one player, wires its exits through SceneRouter without
## travelling, and every exit lands on a spawn point that exists in its target screen.

const SCREENS := [
	"absinthe_arcade_exterior",
	"absinthe_arcade_interior",
	"absinthe_arcade_mirror_corridor",
	"absinthe_arcade_north_wing",
	"absinthe_arcade_restroom",
]


## Records every error (not warning) the engine logs while it is installed.
class ErrorTrap:
	extends Logger
	var errors: Array[String] = []
	var _lock := Mutex.new()

	func _log_error(function: String, file: String, line: int, code: String, rationale: String,
			_editor_notify: bool, error_type: int, _script_backtraces: Array[ScriptBacktrace]) -> void:
		if error_type == ERROR_TYPE_WARNING:
			return
		_lock.lock()
		errors.append("%s (%s:%d %s) %s" % [code, file, line, function, rationale])
		_lock.unlock()

	func _log_message(_message: String, _error: bool) -> void:
		pass


var _trap: ErrorTrap
var _saved := {}


func before_each() -> void:
	_saved = {"sovs": GameState.sovs, "inventory": GameState.inventory.duplicate(true),
		"party": GameState.party.duplicate(true), "flags": GameState.flags.duplicate(true)}
	SceneRouter.pending_spawn = ""
	_trap = ErrorTrap.new()
	OS.add_logger(_trap)


func after_each() -> void:
	OS.remove_logger(_trap)
	_trap = null
	GameState.sovs = _saved["sovs"]
	GameState.inventory = _saved["inventory"]
	GameState.party = _saved["party"]
	GameState.flags = _saved["flags"]
	SceneRouter.pending_spawn = ""


func _in(world: Node, group: String) -> Array:
	return get_tree().get_nodes_in_group(group).filter(func(n): return world.is_ancestor_of(n))


func _spawn_ids(world: Node) -> Array:
	return _in(world, "spawn_points").map(func(n): return String(n.get_meta("spawn_id")))


func test_arcade_scenes_error_trap_catches_an_error_but_not_a_warning() -> void:
	# Act: the guard the load test relies on (this test's expected ERROR line is printed on purpose).
	push_warning("smoke-test trap check: a warning")
	push_error("smoke-test trap check: an error")
	# Assert
	assert_eq(_trap.errors.size(), 1)


func test_arcade_scenes_every_screen_is_routed() -> void:
	# Act / Assert
	for id: String in SCREENS:
		var path := SceneRouter.scene_path(id)
		assert_false(path.is_empty(), id)
		assert_true(ResourceLoader.exists(path), path)


func test_arcade_scenes_load_and_run_without_errors() -> void:
	for id: String in SCREENS:
		# Arrange
		var world: Node3D = load(SceneRouter.scene_path(id)).instantiate()
		if "travel_out" in world:
			world.travel_out = false
		add_child_autofree(world)
		# Act
		await wait_physics_frames(3)
		# Assert
		assert_eq(_trap.errors, [] as Array[String], "%s logged errors" % id)
		_trap.errors.clear()
		world.free()


func test_arcade_scenes_spawn_one_player_and_wire_exits_without_travelling() -> void:
	for id: String in SCREENS:
		# Arrange
		var world: Node3D = load(SceneRouter.scene_path(id)).instantiate()
		add_child_autofree(world)
		# Act
		await wait_physics_frames(3)
		var players := _in(world, "player")
		var exits := _in(world, "scene_exits")
		# Assert
		assert_eq(players.size(), 1, "%s players" % id)
		assert_gt(exits.size(), 0, "%s has a way out" % id)
		for exit: Area3D in exits:
			assert_gt(exit.body_entered.get_connections().size(), 0, "%s exit %s is wired" % [id, exit.name])
		assert_eq(SceneRouter.pending_spawn, "", "%s: spawning must not trip an exit" % id)
		world.free()


func test_arcade_scenes_every_exit_lands_on_a_spawn_in_its_target() -> void:
	# Arrange: every screen's exits and spawn ids, built without a player.
	var exits_by_screen := {}
	var spawns_by_screen := {}
	for id: String in SCREENS:
		var world: Node3D = load(SceneRouter.scene_path(id)).instantiate()
		world.spawn_player = false
		add_child_autofree(world)
		exits_by_screen[id] = _in(world, "scene_exits").map(func(n): return [
			String(n.get_meta("target_scene")), String(n.get_meta("target_spawn", ""))])
		spawns_by_screen[id] = _spawn_ids(world)
		world.free()
	# Act / Assert: streets beyond the Arcade aren't built yet, so only arcade targets are checked.
	for id: String in SCREENS:
		assert_gt(spawns_by_screen[id].size(), 0, "%s has a spawn point" % id)
		for exit: Array in exits_by_screen[id]:
			var target: String = exit[0]
			if not SCREENS.has(target):
				continue
			assert_has(spawns_by_screen[target], exit[1], "%s -> %s:%s" % [id, target, exit[1]])
