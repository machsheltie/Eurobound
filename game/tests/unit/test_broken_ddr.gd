extends GutTest
## BrokenDdr: three tokens, one at a time, unlock the MAINTENANCE door for good (round v34).

class FakeState:
	var inventory := {}
	var flags := {}


func test_broken_ddr_third_token_unlocks_for_good() -> void:
	# Arrange
	var s := FakeState.new()
	s.inventory[ArcadeRules.TOKEN_ID] = 5
	# Act
	var results := []
	for i in 4:
		results.append(BrokenDdr.feed(s))
	# Assert
	assert_eq(results, ["fed", "fed", "unlocked", "done"])
	assert_eq(ArcadeRules.tokens(s), 2)
	assert_true(BrokenDdr.unlocked(s))


func test_broken_ddr_without_tokens_takes_nothing() -> void:
	# Arrange
	var s := FakeState.new()
	# Act
	var r := BrokenDdr.feed(s)
	# Assert
	assert_eq(r, "broke")
	assert_eq(BrokenDdr.fed(s), 0)


func test_broken_ddr_north_wing_has_both_spots_on_open_floor() -> void:
	# Arrange
	var wing: Node3D = load("res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.tscn").instantiate()
	wing.spawn_player = false
	add_child_autofree(wing)
	await wait_physics_frames(2)
	var space := wing.get_world_3d().direct_space_state
	# Act / Assert
	for id in ["broken_ddr", "maintenance_door"]:
		var spot: Node3D = get_tree().get_nodes_in_group("spawn_points").filter(
			func(n): return wing.is_ancestor_of(n) and n.get_meta("spawn_id") == "at_" + id)[0]
		var q := PhysicsShapeQueryParameters3D.new()
		var capsule := CapsuleShape3D.new()
		capsule.radius = 0.25
		capsule.height = 1.6
		q.shape = capsule
		q.transform = Transform3D(Basis(), spot.global_position + Vector3(0, 0.85, 0))
		assert_eq(space.intersect_shape(q).size(), 0, id)
