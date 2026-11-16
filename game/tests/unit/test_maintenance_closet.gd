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
	assert_eq(room.props.prop_ids().size(), 12)
	assert_true(room.props.states_of("ddr_arrow_left").has("on"))
	assert_ne(room.props.texture_path("ddr_arrow_left", "on", "emit"), "")
	assert_eq(room.props.states_of("crt").size(), 2)


func test_maintenance_closet_every_interaction_id_resolves_to_a_node() -> void:
	# Arrange
	var room: Node3D = CLOSET.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	# The haiku and joystick leave the "interact_points" group while hidden, so read every marker.
	var marked: Array = room._markers.values().map(func(n): return String(n.get_meta("interact_id")))
	# Act / Assert
	for id: String in ClosetProps.IDS:
		assert_true(marked.has(id), id)
	assert_true(marked.has(ClosetProps.BLACKLIGHT_SWITCH))
	# the switch and tube answer to the switch; the prize tag has no pickup yet (C10 is not built)
	var talking: Array = ClosetProps.IDS + [ClosetProps.BLACKLIGHT_SWITCH, ""]
	for id: String in room.PROPS.keys():
		assert_true(talking.has(String(room.PROPS[id][3])), id)


func test_maintenance_closet_every_art_state_has_its_sprite() -> void:
	# Arrange
	var room: Node3D = CLOSET.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	var want := {"bl_switch": ["off", "on"], "bl_tube": ["off", "on"], "wiring": ["idle", "spark"],
		"haiku": ["off", "on"], "joystick": ["faint", "glowing", "faint_uv", "glowing_uv"],
		"prize_tag": ["hanging", "hanging_uv", "collected"]}
	# Act / Assert
	for id: String in want.keys():
		for st: String in want[id]:
			assert_true(room.props.states_of(id).has(st), id + " " + st)
			assert_true(ResourceLoader.exists(room.props.texture_path(id, st, "night")), id + " " + st)
	assert_ne(room.props.texture_path("bl_tube", "on", "emit"), "")
	assert_ne(room.props.texture_path("wiring", "spark", "emit"), "")
	assert_true(ResourceLoader.exists(room.plate_prefix + "night_uv.png"))


func test_maintenance_closet_wall_decals_lie_on_their_walls() -> void:
	# Arrange
	var room: Node3D = CLOSET.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	# Act / Assert: every corner of a wall decal's quad is a hair off its wall line
	for id: String in ["bl_switch", "wiring", "haiku", "joystick"]:
		var span: Array = room.PROPS[id][4]
		var line: Array = room.LEFT_WALL if span[0] == "left" else room.RIGHT_WALL
		for c: Vector3 in room.wall_quad(span):
			assert_almost_eq(absf(c.x - room._x_at(line, c.z)), room.WALL_QUAD_INSET, 0.001, id)
		var mesh: Mesh = room.props.node_of(id).mesh
		assert_false(mesh is QuadMesh, id + " should use its wall quad")


func test_maintenance_closet_blacklight_switch_swaps_the_plate_and_the_art() -> void:
	# Arrange
	GameState.flags.erase(ClosetProps.BLACKLIGHT_FLAG)
	var room: Node3D = CLOSET.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await wait_physics_frames(2)
	var haiku_marker: Node3D = room._markers[ClosetProps.GRAFFITI_HAIKU]
	assert_eq(room.props.state_of("haiku"), "off")
	assert_false(haiku_marker.is_in_group("interact_points"), "a hidden haiku blocks nothing")
	# Act
	room._on_interacted(ClosetProps.BLACKLIGHT_SWITCH)
	# Assert
	assert_true(ClosetProps.blacklight_on(GameState))
	assert_eq(room.props.state_of("bl_switch"), "on")
	assert_eq(room.props.state_of("bl_tube"), "on")
	assert_eq(room.props.state_of("haiku"), "on")
	assert_true(haiku_marker.is_in_group("interact_points"))
	var tex: Texture2D = room._materials[0].get_shader_parameter("albedo_tex")
	assert_eq(tex.resource_path, room.plate_prefix + "night_uv.png")
	# Act again: off
	room._on_interacted(ClosetProps.BLACKLIGHT_SWITCH)
	assert_eq(room.props.state_of("bl_tube"), "off")
	tex = room._materials[0].get_shader_parameter("albedo_tex")
	assert_eq(tex.resource_path, room.plate_prefix + "night.png")
	GameState.flags.erase(ClosetProps.BLACKLIGHT_FLAG)
