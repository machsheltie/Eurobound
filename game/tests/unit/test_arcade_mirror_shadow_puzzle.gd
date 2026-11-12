extends GutTest
## The mirror corridor's shadow puzzle (design: mirror_shadow_puzzle; author round v42
## arc_mirror_puzzle = yes): three switches pressed in the afterimages' order, wrong order resets,
## the Broken Handheld is given once, and reduced motion swaps the moving afterimage for static
## offset ones with numbered floor markers.

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_mirror_corridor_hd2d.tscn")

var _room: Node3D
var _saved := {}


class FakeState:
	extends RefCounted
	var flags := {}
	var inventory := {}

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func before_each() -> void:
	_saved = {"inventory": GameState.inventory.duplicate(true), "flags": GameState.flags.duplicate(true),
		"party": GameState.party.duplicate(true)}


func after_each() -> void:
	GameState.inventory = _saved["inventory"]
	GameState.flags = _saved["flags"]
	GameState.party = _saved["party"]
	SceneRouter.pending_spawn = ""


func _enter_room() -> void:
	_room = SCENE.instantiate()
	add_child_autofree(_room)
	await wait_physics_frames(3)


func _spot(id: String) -> Node3D:
	for n in get_tree().get_nodes_in_group("spawn_points"):
		if _room.is_ancestor_of(n) and n.get_meta("spawn_id") == id:
			return n
	return null


func test_mirror_shadow_puzzle_right_order_solves_and_rewards() -> void:
	# Arrange
	var s := FakeState.new()
	var p := MirrorShadowPuzzle.new()

	# Act
	var results: Array[String] = []
	for i in MirrorShadowPuzzle.SOLUTION:
		results.append(p.press(s, i))

	# Assert
	assert_eq(results, ["step", "step", "solved"] as Array[String])
	assert_true(s.flags[MirrorShadowPuzzle.SOLVED_FLAG])
	assert_true(s.flags[MirrorShadowPuzzle.FOUND_FLAG])
	assert_eq(s.inventory[MirrorShadowPuzzle.ITEM_ID], 1)


func test_mirror_shadow_puzzle_wrong_order_resets_progress() -> void:
	# Arrange
	var s := FakeState.new()
	var p := MirrorShadowPuzzle.new()
	p.press(s, MirrorShadowPuzzle.SOLUTION[0])

	# Act
	var wrong: int = (MirrorShadowPuzzle.SOLUTION[1] + 1) % 3
	if wrong == MirrorShadowPuzzle.SOLUTION[1]:
		wrong = (wrong + 1) % 3
	var r := p.press(s, wrong)

	# Assert
	assert_eq(r, "reset")
	assert_eq(p.progress, 0)
	assert_false(s.flags.has(MirrorShadowPuzzle.SOLVED_FLAG))
	assert_false(s.inventory.has(MirrorShadowPuzzle.ITEM_ID))


func test_mirror_shadow_puzzle_reset_then_full_order_still_solves() -> void:
	# Arrange
	var s := FakeState.new()
	var p := MirrorShadowPuzzle.new()
	p.press(s, MirrorShadowPuzzle.SOLUTION[1])

	# Act
	var last := ""
	for i in MirrorShadowPuzzle.SOLUTION:
		last = p.press(s, i)

	# Assert
	assert_eq(last, "solved")


func test_mirror_shadow_puzzle_reward_given_once() -> void:
	# Arrange
	var s := FakeState.new()
	var p := MirrorShadowPuzzle.new()
	for i in MirrorShadowPuzzle.SOLUTION:
		p.press(s, i)

	# Act
	var again := ""
	for i in MirrorShadowPuzzle.SOLUTION:
		again = p.press(s, i)

	# Assert
	assert_eq(again, "ignored")
	assert_eq(s.inventory[MirrorShadowPuzzle.ITEM_ID], 1)


func test_mirror_shadow_puzzle_solution_uses_each_switch_once() -> void:
	# Arrange / Act
	var sorted := MirrorShadowPuzzle.SOLUTION.duplicate()
	sorted.sort()

	# Assert
	assert_eq(sorted, [0, 1, 2])


func test_mirror_shadow_puzzle_item_registered_with_design_text() -> void:
	# Arrange
	var doc: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/items/key_items.json"))
	var design: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(
		"res://../design/World Design/Debaucheryville/items/absinthe_arcade_items.json"))
	var want := {}
	for it: Dictionary in design["items"]:
		if it["item_id"] == MirrorShadowPuzzle.ITEM_ID:
			want = it

	# Act
	var got: Dictionary = doc["key_items"].get(MirrorShadowPuzzle.ITEM_ID, {})

	# Assert
	assert_false(got.is_empty())
	assert_eq(got.get("display_name"), want.get("display_name"))
	assert_eq(got.get("description"), want.get("description"))


func test_mirror_shadow_puzzle_corridor_has_three_switch_points() -> void:
	# Arrange
	await _enter_room()

	# Act
	var ids: Array[String] = []
	for n in get_tree().get_nodes_in_group("interact_points"):
		if _room.is_ancestor_of(n):
			ids.append(String(n.get_meta("interact_id")))
	ids.sort()

	# Assert
	assert_eq(ids, ["shadow_switch_1", "shadow_switch_2", "shadow_switch_3"] as Array[String])


func test_mirror_shadow_puzzle_stand_spots_are_on_open_floor_and_reach_the_switch() -> void:
	# Arrange
	await _enter_room()
	var space := _room.get_world_3d().direct_space_state
	var player: PlayerController = get_tree().get_nodes_in_group("player").filter(func(n): return _room.is_ancestor_of(n))[0]

	for i in 3:
		var spot := _spot("at_" + _room.switch_id(i))
		assert_not_null(spot)
		if spot == null:
			continue
		var q := PhysicsShapeQueryParameters3D.new()
		var capsule := CapsuleShape3D.new()
		capsule.radius = 0.25
		capsule.height = 1.6
		q.shape = capsule
		q.transform = Transform3D(Basis(), spot.global_position + Vector3(0, 0.85, 0))
		q.exclude = [player.get_rid()]

		# Act
		var hits := space.intersect_shape(q)
		player.global_position = spot.global_position
		player.face(spot.get_meta("facing"))
		var found := player.nearest_interactable()

		# Assert
		assert_eq(hits.size(), 0, "stand spot %d blocked" % i)
		assert_not_null(found)
		if found != null:
			assert_eq(found.get_meta("interact_id"), _room.switch_id(i))


func test_mirror_shadow_puzzle_pressing_in_the_corridor_gives_the_item() -> void:
	# Arrange
	GameState.flags.erase(MirrorShadowPuzzle.SOLVED_FLAG)
	GameState.inventory.erase(MirrorShadowPuzzle.ITEM_ID)
	await _enter_room()
	var player: PlayerController = get_tree().get_nodes_in_group("player").filter(func(n): return _room.is_ancestor_of(n))[0]

	# Act
	for i in MirrorShadowPuzzle.SOLUTION:
		player.interacted.emit(_room.switch_id(i))

	# Assert
	assert_true(GameState.flags.get(MirrorShadowPuzzle.SOLVED_FLAG, false))
	assert_eq(int(GameState.inventory.get(MirrorShadowPuzzle.ITEM_ID, 0)), 1)


func test_mirror_shadow_puzzle_normal_motion_shows_one_moving_afterimage() -> void:
	# Arrange
	GameState.flags.erase(MirrorShadowPuzzle.SOLVED_FLAG)
	GameState.flags["settings.reduced_motion"] = false

	# Act
	await _enter_room()
	var hint := _room.find_child("afterimage_hint", true, false)

	# Assert
	assert_not_null(hint)
	assert_eq(hint.get_child_count(), 1)
	assert_null(_room.find_child("floor_number_1", true, false))


func test_mirror_shadow_puzzle_reduced_motion_shows_static_afterimages_with_numbers() -> void:
	# Arrange
	GameState.flags.erase(MirrorShadowPuzzle.SOLVED_FLAG)
	GameState.party = [{"id": "stub"}]  # a started game, so entering the room keeps the flags
	GameState.flags["settings.reduced_motion"] = true

	# Act
	await _enter_room()
	var hint := _room.find_child("afterimage_hint", true, false)

	# Assert
	assert_true(ArcadeAmbientFx.is_reduced(GameState), "flag survived room start")
	assert_not_null(hint)
	assert_eq(hint.find_children("*", "PartySprite3D", true, false).size(), 3)
	for n in [1, 2, 3]:
		assert_not_null(_room.find_child("floor_number_%d" % n, true, false))
