extends GutTest
## SceneRouter: walking into a scene exit loads the target screen and puts the player on the
## matching spawn point. Covers the Absinthe Arcade street <-> hall doors.

const EXTERIOR := preload("res://worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn")
const INTERIOR := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")


func after_each() -> void:
	SceneRouter.pending_spawn = ""


func _exits(world: Node) -> Array:
	return get_tree().get_nodes_in_group("scene_exits").filter(func(n): return world.is_ancestor_of(n))


func _spawn_ids(world: Node) -> Array:
	var ids := []
	for n in get_tree().get_nodes_in_group("spawn_points"):
		if world.is_ancestor_of(n):
			ids.append(String(n.get_meta("spawn_id")))
	return ids


func _exit_to(world: Node, target: String) -> Area3D:
	for e in _exits(world):
		if e.get_meta("target_scene") == target:
			return e
	return null


func test_scene_router_knows_both_arcade_screens() -> void:
	# Act / Assert
	assert_eq(SceneRouter.scene_path("absinthe_arcade_exterior"), EXTERIOR.resource_path)
	assert_eq(SceneRouter.scene_path("absinthe_arcade_interior"), INTERIOR.resource_path)


func test_scene_router_unknown_target_does_not_travel() -> void:
	# Act
	var ok := SceneRouter.travel(get_tree(), "no_such_screen", "x")

	# Assert
	assert_false(ok)
	assert_eq(SceneRouter.pending_spawn, "")


func test_scene_router_spawns_player_on_pending_spawn_point() -> void:
	# Arrange
	var world := Node3D.new()
	add_child_autofree(world)
	for spec in [["a", Vector3(1, 0, 2)], ["b", Vector3(-3, 0, 4)]]:
		var m := Marker3D.new()
		m.add_to_group("spawn_points")
		m.set_meta("spawn_id", spec[0])
		m.set_meta("facing", "north")
		m.position = spec[1]
		world.add_child(m)
	SceneRouter.pending_spawn = "b"

	# Act
	var p := SceneRouter.spawn_player(world, "a")

	# Assert
	assert_almost_eq(p.global_position.x, -3.0, 0.001)
	assert_almost_eq(p.global_position.z, 4.0, 0.001)
	assert_eq(p.sprite.facing, "north")
	assert_eq(SceneRouter.pending_spawn, "", "the spawn request is used up")


func test_scene_router_spawns_on_default_when_nothing_pending() -> void:
	# Arrange
	var world := Node3D.new()
	add_child_autofree(world)
	var m := Marker3D.new()
	m.add_to_group("spawn_points")
	m.set_meta("spawn_id", "start")
	m.position = Vector3(5, 0, 0)
	world.add_child(m)

	# Act
	var p := SceneRouter.spawn_player(world, "start")

	# Assert
	assert_almost_eq(p.global_position.x, 5.0, 0.001)


func test_exterior_front_door_leads_into_the_hall() -> void:
	# Arrange
	var world := EXTERIOR.instantiate()
	world.spawn_player = false
	add_child_autofree(world)

	# Act
	var door := _exit_to(world, "absinthe_arcade_interior")

	# Assert
	assert_not_null(door)
	assert_eq(door.get_meta("target_spawn"), "from_street")
	assert_has(_spawn_ids(world), "from_arcade")
	assert_has(_spawn_ids(world), "start")


func test_hall_front_doors_lead_back_to_the_street() -> void:
	# Arrange
	var world := INTERIOR.instantiate()
	world.spawn_player = false
	add_child_autofree(world)

	# Act
	var door := _exit_to(world, "absinthe_arcade_exterior")

	# Assert
	assert_not_null(door)
	assert_eq(door.get_meta("target_spawn"), "from_arcade")
	assert_has(_spawn_ids(world), "from_street")


func test_spawn_points_sit_outside_every_exit() -> void:
	# Arrange: a spawn inside an exit would bounce the player straight back out
	for scene in [EXTERIOR, INTERIOR]:
		var world = scene.instantiate()
		world.spawn_player = false
		add_child_autofree(world)
		await wait_physics_frames(2)
		var space := (world as Node3D).get_world_3d().direct_space_state
		for n in get_tree().get_nodes_in_group("spawn_points"):
			if not world.is_ancestor_of(n):
				continue
			var q := PhysicsPointQueryParameters3D.new()
			q.position = (n as Node3D).global_position + Vector3(0, 0.5, 0)
			q.collide_with_areas = true
			q.collide_with_bodies = false

			# Act
			var hits := space.intersect_point(q)

			# Assert
			var in_exit := hits.any(func(h): return (h["collider"] as Node).is_in_group("scene_exits"))
			assert_false(in_exit, "%s spawn %s" % [scene.resource_path.get_file(), n.get_meta("spawn_id")])
		world.free()


func test_scene_router_spawning_on_the_street_does_not_trip_the_door() -> void:
	# Arrange: regression - the player used to enter the tree at the origin, inside the front-door
	# exit, and travelled into the hall on the first physics frame.
	var world := EXTERIOR.instantiate()
	add_child_autofree(world)

	# Act
	await wait_physics_frames(3)

	# Assert
	assert_eq(SceneRouter.pending_spawn, "", "no travel was requested")


func test_spawned_player_walks_on_solid_ground_in_both_screens() -> void:
	for scene in [EXTERIOR, INTERIOR]:
		# Arrange
		var world = scene.instantiate()
		add_child_autofree(world)
		await wait_physics_frames(10)

		# Act
		var players := get_tree().get_nodes_in_group("player").filter(func(n): return world.is_ancestor_of(n))

		# Assert: one player, standing on the floor (not fallen through)
		assert_eq(players.size(), 1, scene.resource_path.get_file())
		assert_almost_eq((players[0] as Node3D).global_position.y, 0.0, 0.1)
		world.free()
