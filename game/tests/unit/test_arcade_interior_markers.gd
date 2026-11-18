extends GutTest
## The Absinthe Arcade hall exposes its north-arch exit and the interaction anchors for the three
## battle cabinets and the DDR dance-off, so the scene-transition and interaction systems can find them.

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
const EXPECTED_IDS := [
	"cabinet_frogger", "cabinet_street_fighter", "cabinet_kebab_kombat", "ddr_dance_off", "token_machine",
	"skee_ball", "foosball", "beanie_baby_claw", "rigged_absinthe_claw_machine", "restroom_door", "prize_counter", "vip_arrows", "bidet_stool",
]

var _hall: Node3D


func before_each() -> void:
	_hall = SCENE.instantiate()
	_hall.spawn_player = false
	add_child_autofree(_hall)


func _north_exits() -> Array:
	return get_tree().get_nodes_in_group("scene_exits").filter(
		func(n): return _hall.is_ancestor_of(n) and n.name == "exit_north_arch")


func test_arcade_interior_interact_points_all_ids_present() -> void:
	# Arrange
	var found: Array[String] = []

	# Act
	for node in get_tree().get_nodes_in_group("interact_points"):
		if _hall.is_ancestor_of(node):
			found.append(String(node.get_meta("interact_id")))
	found.sort()

	# Assert
	var expected: Array[String] = []
	expected.assign(EXPECTED_IDS)
	expected.sort()
	assert_eq(found, expected)


func test_arcade_interior_north_exit_targets_mirror_corridor() -> void:
	# Arrange / Act
	var exits := _north_exits()

	# Assert
	assert_eq(exits.size(), 1)
	assert_eq(exits[0].get_meta("target_scene"), "absinthe_arcade_mirror_corridor")


func test_arcade_interior_depth_scale_full_size_in_front() -> void:
	# Arrange
	var script: GDScript = _hall.get_script()

	# Act / Assert: at the curve's start and nearer the camera, sprites stay full size
	assert_almost_eq(script.depth_scale_at(2.0), 1.0, 0.0001)
	assert_almost_eq(script.depth_scale_at(5.0), 1.0, 0.0001)


func test_arcade_interior_depth_scale_ruled_minimum_at_back_wall() -> void:
	# Arrange
	var script: GDScript = _hall.get_script()

	# Act / Assert: 68% at the back wall (author ruling), never smaller inside the arch
	assert_almost_eq(script.depth_scale_at(-5.32), 0.68, 0.0001)
	assert_almost_eq(script.depth_scale_at(-7.0), 0.68, 0.0001)


func test_arcade_interior_depth_scale_applies_to_hall_actors() -> void:
	# Arrange
	var actor := Node3D.new()
	actor.add_to_group("hall_actors")
	_hall.add_child(actor)
	actor.position = Vector3(0, 0, -5.32 * 0.75)

	# Act
	await wait_physics_frames(2)

	# Assert
	assert_almost_eq(actor.scale.x, 0.68, 0.001)


func test_arcade_interior_north_exit_sits_inside_the_arch_opening() -> void:
	# Arrange
	var exits := _north_exits()
	var shape: CollisionShape3D = exits[0].get_child(0)

	# Act
	var p := shape.global_position

	# Assert: between the jambs and behind the back-wall line (real metres = painting units * 0.75)
	assert_between(p.x, -0.35 * 0.75, 0.83 * 0.75)
	assert_lt(p.z, -5.32 * 0.75)


# ---- Code geometry matched to the approved hall plate (Eurobound-ikba). The plate pixels were taken
# to the floor through the paint camera (paint_px_to_floor.py); painting units, real metres = * 0.75.

## Where each painted bar seat's legs meet the floor (plate px of the leg tips through the paint camera).
const SEAT_LEGS := {
	"chair_west_end": [Vector2(-1.38, -1.08), Vector2(-1.23, -1.45), Vector2(-0.82, -1.38), Vector2(-0.92, -1.13)],
	"stool_green": [Vector2(-1.29, 0.58), Vector2(-1.12, 0.89), Vector2(-0.76, 0.66), Vector2(-0.91, 0.48)],
	"stool_brown": [Vector2(-0.75, 1.47), Vector2(-0.48, 1.78), Vector2(-0.16, 1.51), Vector2(-0.40, 1.24)],
	"chair_front": [Vector2(0.34, 2.52), Vector2(0.73, 2.77), Vector2(1.11, 2.34), Vector2(0.85, 2.17)],
	"stool_red_front": [Vector2(1.73, 2.87), Vector2(1.85, 3.06), Vector2(2.29, 2.82), Vector2(1.86, 2.52)],
	"stool_purple_kk": [Vector2(4.84, 0.07), Vector2(4.92, 0.44), Vector2(5.25, 0.01), Vector2(5.15, 0.13)],
	"stool_red_bb": [Vector2(5.03, 0.82), Vector2(5.15, 0.99), Vector2(5.50, 0.93), Vector2(5.15, 0.57)],
}
## The painted arch base (right jamb plinth, plate px 1476,594) and the foosball table's leg footprint.
const ARCH_BASE_Z := -5.76
const FOOSBALL_LEGS_MIN := Vector2(-4.04, -2.33)
const FOOSBALL_LEGS_MAX := Vector2(-2.47, -1.44)
## The PRIZE REDEMPTION placard (px 1695-1820) where the bar meets the floor (px row 1215).
const PLACARD_X := Vector2(1.90, 2.61)
const PLACARD_Z := 2.37


func _spawn(id: String) -> Node3D:
	for n in get_tree().get_nodes_in_group("spawn_points"):
		if _hall.is_ancestor_of(n) and n.get_meta("spawn_id") == id:
			return n
	return null


func _anchor(id: String) -> Vector2:
	for n in get_tree().get_nodes_in_group("interact_points"):
		if _hall.is_ancestor_of(n) and n.get_meta("interact_id") == id:
			var p: Vector3 = (n as Node3D).position
			return Vector2(p.x, p.z)
	return Vector2(INF, INF)


func _layer_meshes(layer_id: String) -> Array:
	return _hall.find_children("*", "MeshInstance3D", true, false).filter(
		func(m): return m.material_override is ShaderMaterial and m.material_override.get_meta("layer_id", "") == layer_id)


func test_arcade_interior_every_painted_bar_seat_leg_is_blocked() -> void:
	# Arrange
	await wait_physics_frames(2)
	var space := _hall.get_world_3d().direct_space_state

	for seat: String in SEAT_LEGS.keys():
		for leg: Vector2 in SEAT_LEGS[seat]:
			var q := PhysicsPointQueryParameters3D.new()
			q.position = _hall.to_global(Vector3(leg.x, 0.5, leg.y) * 0.75)

			# Act
			var hits := space.intersect_point(q)

			# Assert
			assert_false(hits.is_empty(), "%s leg at %s is walkable" % [seat, leg])


func test_arcade_interior_foosball_anchor_sits_on_the_painted_table() -> void:
	# Arrange / Act
	var at := _anchor("foosball")

	# Assert: inside the table's leg footprint, not on the floor south of it
	assert_between(at.x, FOOSBALL_LEGS_MIN.x, FOOSBALL_LEGS_MAX.x)
	assert_between(at.y, FOOSBALL_LEGS_MIN.y, FOOSBALL_LEGS_MAX.y)


func test_arcade_interior_prize_counter_anchor_sits_under_the_placard() -> void:
	# Arrange / Act
	var at := _anchor("prize_counter")

	# Assert: on the bar front, under the PRIZE REDEMPTION placard
	assert_between(at.x, PLACARD_X.x, PLACARD_X.y)
	assert_almost_eq(at.y, PLACARD_Z, 0.05)


func test_arcade_interior_north_exit_starts_at_the_painted_arch_base() -> void:
	# Arrange
	var script: GDScript = _hall.get_script()
	var shape: CollisionShape3D = _north_exits()[0].get_child(0)

	# Act: the trigger's south face (real metres)
	var front_z := shape.global_position.z + (shape.shape as BoxShape3D).size.z * 0.5 * 0.75

	# Assert
	assert_almost_eq(float(script.NORTH_EXIT_Z), ARCH_BASE_Z, 0.0001)
	assert_almost_eq(front_z, ARCH_BASE_Z * 0.75, 0.001)


func test_arcade_interior_walking_north_from_the_corridor_spawn_takes_the_arch_exit() -> void:
	# Arrange: back out of the arch from the mirror corridor, then straight back in
	var exit: Area3D = _north_exits()[0]
	var player := PlayerController.new()
	player.set_physics_process(false)
	_hall.add_child(player)
	player.global_position = _spawn("from_mirror_corridor").global_position
	var entered := []
	exit.body_entered.connect(func(body: Node3D) -> void:
		if body == player:
			entered.append(body.global_position))
	await wait_physics_frames(2)

	# Act
	for _i in 240:
		if not entered.is_empty():
			break
		player.step(Vector2(0, -1), 1.0 / 60.0)
		await wait_physics_frames(1)

	# Assert: it fires inside the opening, with the bro's centre still south of the painted arch base
	assert_eq(entered.size(), 1, "the arch exit fired")
	if entered.size() == 1:
		var z_paint: float = (entered[0] as Vector3).z / 0.75
		assert_between(z_paint, ARCH_BASE_Z, -5.32)


func test_arcade_interior_north_arch_occluder_sorts_at_the_painted_arch_base() -> void:
	# Arrange / Act
	var meshes := _layer_meshes("aa_int_layer_north_arch")

	# Assert: one painted slab whose front face is the arch base, and no collider in the exit's way
	assert_eq(meshes.size(), 1)
	if meshes.size() == 1:
		assert_almost_eq((meshes[0] as MeshInstance3D).get_aabb().end.z, ARCH_BASE_Z, 0.001)
	assert_null(_hall.find_child("aa_int_layer_north_arch_collision", true, false))


func test_arcade_interior_mezzanine_occluders_sort_behind_every_walkable_spot() -> void:
	# Arrange
	var script: GDScript = _hall.get_script()

	# Act
	var meshes := _layer_meshes("aa_int_layer_mezzanine")

	# Assert: a strip on each side wall, no colliders, sorted at the deepest walkable spot
	assert_eq(meshes.size(), 2)
	assert_almost_eq(float(script.OCCLUDERS["aa_int_layer_mezzanine"]["sort_z"]), ARCH_BASE_Z, 0.0001)
	assert_null(_hall.find_child("aa_int_layer_mezzanine_collision", true, false))
