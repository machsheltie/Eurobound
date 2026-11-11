extends GutTest
## The Absinthe Arcade restroom screen (round v26 restroom, round v28 door): it exits back to the
## hall, and the hall has a spot to come back out at.

const RESTROOM := preload("res://worlds/debaucheryville/absinthe_arcade_restroom_hd2d.tscn")
const HALL := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")


func _spawn_ids(root: Node) -> Array:
	return get_tree().get_nodes_in_group("spawn_points").filter(
		func(n): return root.is_ancestor_of(n)).map(func(n): return String(n.get_meta("spawn_id")))


func test_arcade_restroom_exits_to_the_hall_and_back() -> void:
	# Arrange
	var room: Node3D = RESTROOM.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	var hall: Node3D = HALL.instantiate()
	hall.spawn_player = false
	add_child_autofree(hall)
	await wait_physics_frames(2)
	# Act
	var exits := get_tree().get_nodes_in_group("scene_exits").filter(func(n): return room.is_ancestor_of(n))
	# Assert
	assert_eq(exits.size(), 1)
	assert_eq(exits[0].get_meta("target_scene"), "absinthe_arcade_interior")
	assert_eq(exits[0].get_meta("target_spawn"), "from_restroom")
	assert_has(_spawn_ids(hall), "from_restroom")
	assert_has(_spawn_ids(room), "from_hall")
	assert_false(SceneRouter.scene_path("absinthe_arcade_restroom").is_empty())


func test_arcade_restroom_spawn_is_on_open_floor() -> void:
	# Arrange
	var room: Node3D = RESTROOM.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	var spot: Node3D = get_tree().get_nodes_in_group("spawn_points").filter(func(n): return room.is_ancestor_of(n))[0]
	var q := PhysicsShapeQueryParameters3D.new()
	var capsule := CapsuleShape3D.new()
	capsule.radius = 0.25
	capsule.height = 1.6
	q.shape = capsule
	q.transform = Transform3D(Basis(), spot.global_position + Vector3(0, 0.85, 0))
	# Act
	var hits := room.get_world_3d().direct_space_state.intersect_shape(q)
	# Assert
	assert_eq(hits.size(), 0)
