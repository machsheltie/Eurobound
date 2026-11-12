extends GutTest
## The Absinthium Taproom (round v39): behind the north wing's green curtain, found between 20:00
## and 04:00, then open for good; walking out lands back at the curtain.

const TAPROOM := preload("res://worlds/debaucheryville/absinthe_arcade_taproom_hd2d.tscn")
const WING := preload("res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.tscn")
const WING_SCRIPT := preload("res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.gd")

class FakeState:
	var flags := {}


func test_taproom_curtain_only_gives_itself_away_at_night_until_found() -> void:
	# Arrange
	var s := FakeState.new()
	# Act
	var morning := WING_SCRIPT.taproom_open(s)
	GameClock.set_time(s, 21 * 60)
	var evening := WING_SCRIPT.taproom_open(s)
	s.flags[WING_SCRIPT.TAPROOM_FLAG] = true
	GameClock.set_time(s, 11 * 60)
	var found := WING_SCRIPT.taproom_open(s)
	# Assert
	assert_eq([morning, evening, found], [false, true, true])


func test_taproom_round_trip_through_the_curtain() -> void:
	# Arrange
	var room: Node3D = TAPROOM.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	var wing: Node3D = WING.instantiate()
	wing.spawn_player = false
	add_child_autofree(wing)
	await wait_physics_frames(2)
	# Act
	var exits := get_tree().get_nodes_in_group("scene_exits").filter(func(n): return room.is_ancestor_of(n))
	var wing_spawns := get_tree().get_nodes_in_group("spawn_points").filter(func(n): return wing.is_ancestor_of(n)).map(
		func(n): return String(n.get_meta("spawn_id")))
	var room_spawns := get_tree().get_nodes_in_group("spawn_points").filter(func(n): return room.is_ancestor_of(n)).map(
		func(n): return String(n.get_meta("spawn_id")))
	# Assert
	assert_eq(exits.size(), 1)
	assert_eq(exits[0].get_meta("target_scene"), "absinthe_arcade_north_wing")
	assert_has(wing_spawns, "from_taproom")
	assert_has(wing_spawns, "at_taproom_curtain")
	assert_has(room_spawns, "from_north_wing")


func _clear(scene_res: PackedScene, spawn_id: String) -> int:
	var scene: Node3D = scene_res.instantiate()
	scene.spawn_player = false
	add_child_autofree(scene)
	await wait_physics_frames(2)
	var spot: Node3D = get_tree().get_nodes_in_group("spawn_points").filter(
		func(n): return scene.is_ancestor_of(n) and n.get_meta("spawn_id") == spawn_id)[0]
	var q := PhysicsShapeQueryParameters3D.new()
	var capsule := CapsuleShape3D.new()
	capsule.radius = 0.25
	capsule.height = 1.6
	q.shape = capsule
	q.collide_with_areas = true
	q.transform = Transform3D(Basis(), spot.global_position + Vector3(0, 0.85, 0))
	var hits := scene.get_world_3d().direct_space_state.intersect_shape(q).size()
	scene.free()
	return hits


func test_taproom_spots_are_on_open_floor() -> void:
	# Arrange / Act: each scene on its own (two rooms at one origin would overlap).
	var arrive := await _clear(TAPROOM, "from_north_wing")
	var curtain := await _clear(WING, "at_taproom_curtain")
	var back := await _clear(WING, "from_taproom")
	# Assert
	assert_eq([arrive, curtain, back], [0, 0, 0])
