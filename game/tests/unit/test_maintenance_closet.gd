extends GutTest
## The maintenance closet (round v38): reached from the north wing's MAINTENANCE door, its arrival
## spot is clear of the walls and of its own exit, and walking out lands back at that door.

const CLOSET := preload("res://worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.tscn")
const WING := preload("res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.tscn")


func test_maintenance_closet_arrival_is_clear_of_walls_and_the_exit() -> void:
	# Arrange
	var room: Node3D = CLOSET.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	var spot: Node3D = get_tree().get_nodes_in_group("spawn_points").filter(func(n): return room.is_ancestor_of(n))[0]
	var q := PhysicsShapeQueryParameters3D.new()
	var capsule := CapsuleShape3D.new()
	capsule.radius = 0.25
	capsule.height = 1.6
	q.shape = capsule
	q.collide_with_areas = true
	q.transform = Transform3D(Basis(), spot.global_position + Vector3(0, 0.85, 0))
	# Act
	var hits := room.get_world_3d().direct_space_state.intersect_shape(q)
	# Assert
	assert_eq(hits.size(), 0, str(hits))


func test_maintenance_closet_door_leads_back_to_the_north_wing() -> void:
	# Arrange
	var room: Node3D = CLOSET.instantiate()
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
	# Assert
	assert_eq(exits.size(), 1)
	assert_eq(exits[0].get_meta("target_scene"), "absinthe_arcade_north_wing")
	assert_has(wing_spawns, String(exits[0].get_meta("target_spawn")))
	assert_false(SceneRouter.scene_path("absinthe_arcade_maintenance_closet").is_empty())


func test_maintenance_closet_every_cutout_loads_as_a_node_with_its_interaction_id() -> void:
	# Arrange
	var room: Node3D = CLOSET.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	# Act / Assert
	for id: String in room.PROPS.keys():
		assert_true(room.props.has_prop(id), id)
		var node: Node3D = room.props.node_of(id)
		assert_not_null(node, id)
		if node == null:
			continue
		assert_eq(String(node.get_meta("interact_id")), String(room.PROPS[id][3]), id)
		assert_not_null(room.props.current_texture(id), id + " texture")
	assert_eq(room.props.prop_ids().size(), 6)
	assert_true(room.props.states_of("ddr_arrow_left").has("on"))
	assert_ne(room.props.texture_path("ddr_arrow_left", "on", "emit"), "")
	assert_eq(room.props.states_of("crt").size(), 2)


func test_maintenance_closet_every_interaction_id_resolves_to_a_node() -> void:
	# Arrange
	var room: Node3D = CLOSET.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	var marked := get_tree().get_nodes_in_group("interact_points").filter(func(n): return room.is_ancestor_of(n)).map(
		func(n): return String(n.get_meta("interact_id")))
	# Act / Assert
	for id: String in ClosetProps.IDS:
		assert_true(marked.has(id), id)
	for id: String in room.PROPS.keys():
		assert_true(ClosetProps.IDS.has(String(room.PROPS[id][3])), id)
