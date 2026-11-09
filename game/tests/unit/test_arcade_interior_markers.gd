extends GutTest
## The Absinthe Arcade hall exposes its north-arch exit and the interaction anchors for the three
## battle cabinets and the DDR dance-off, so the scene-transition and interaction systems can find them.

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
const EXPECTED_IDS := ["cabinet_frogger", "cabinet_street_fighter", "cabinet_kebab_kombat", "ddr_dance_off"]

var _hall: Node3D


func before_each() -> void:
	_hall = SCENE.instantiate()
	add_child_autofree(_hall)


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
	var exits := get_tree().get_nodes_in_group("scene_exits").filter(func(n): return _hall.is_ancestor_of(n))

	# Assert
	assert_eq(exits.size(), 1)
	assert_eq(exits[0].get_meta("target_scene"), "absinthe_arcade_mirror_corridor")


func test_arcade_interior_north_exit_sits_inside_the_arch_opening() -> void:
	# Arrange
	var exits := get_tree().get_nodes_in_group("scene_exits").filter(func(n): return _hall.is_ancestor_of(n))
	var shape: CollisionShape3D = exits[0].get_child(0)

	# Act
	var p := shape.global_position

	# Assert: between the jambs and behind the back-wall line (real metres = painting units * 0.75)
	assert_between(p.x, -0.35 * 0.75, 0.83 * 0.75)
	assert_lt(p.z, -5.32 * 0.75)
