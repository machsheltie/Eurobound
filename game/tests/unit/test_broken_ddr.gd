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


func test_broken_ddr_north_wing_strip_behind_the_ddr_is_blocked() -> void:
	# Eurobound-0wn9: the strip between the right cabinet row (ended z 8.7) and the DDR machine
	# (starts z 9.9) had no collider, so a bro could walk into the painted DDR cabinet and plant pot.
	# Arrange
	var wing: Node3D = load("res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.tscn").instantiate()
	wing.spawn_player = false
	add_child_autofree(wing)
	await wait_physics_frames(2)
	var space := wing.get_world_3d().direct_space_state
	var diorama: Node3D = wing._diorama
	var probe := func(x: float, z: float) -> int:
		var q := PhysicsShapeQueryParameters3D.new()
		var ball := SphereShape3D.new()
		ball.radius = 0.03
		q.shape = ball
		q.transform = Transform3D(Basis(), diorama.to_global(Vector3(x, 0.5, z)))
		return space.intersect_shape(q).size()
	# Act / Assert: painted cabinet body, pot and the seams with both neighbours are solid ...
	for p: Vector2 in [Vector2(5.3, 9.3), Vector2(6.3, 9.3), Vector2(7.3, 9.3),
			Vector2(6.0, 8.75), Vector2(6.0, 9.85)]:
		assert_gt(probe.call(p.x, p.y), 0, "blocked at %s" % p)
	# ... and the open green-lit floor west of the pot stays walkable.
	assert_eq(probe.call(4.7, 9.3), 0, "open floor at (4.7, 9.3)")


func test_broken_ddr_north_wing_side_row_stools_are_blocked_and_aisle_stays_open() -> void:
	# Eurobound-a4zx: the bar stools in front of both side cabinet rows stood on open floor, outside
	# the row blockers, so a bro could walk through them. Stool centres and leg tips measured on the
	# night plate through the paint camera (see FLOOR_BLOCKERS in absinthe_arcade_north_wing_hd2d.gd).
	# Arrange
	var wing: Node3D = load("res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.tscn").instantiate()
	wing.spawn_player = false
	add_child_autofree(wing)
	await wait_physics_frames(2)
	var space := wing.get_world_3d().direct_space_state
	var diorama: Node3D = wing._diorama
	var probe := func(x: float, z: float) -> int:
		var q := PhysicsShapeQueryParameters3D.new()
		var ball := SphereShape3D.new()
		ball.radius = 0.03
		q.shape = ball
		q.transform = Transform3D(Basis(), diorama.to_global(Vector3(x, 0.5, z)))
		return space.intersect_shape(q).size()
	var capsule_hits := func(at: Vector3) -> int:
		var q := PhysicsShapeQueryParameters3D.new()
		var capsule := CapsuleShape3D.new()
		capsule.radius = 0.25
		capsule.height = 1.6
		q.shape = capsule
		q.transform = Transform3D(Basis(), at + Vector3(0, 0.85, 0))
		return space.intersect_shape(q).size()
	var stools := [
		# right row, back to front: seat centres, then the front stool's leg tips
		Vector2(3.48, 2.24), Vector2(3.62, 3.39), Vector2(3.80, 4.65), Vector2(3.94, 5.91),
		Vector2(4.14, 7.27), Vector2(3.80, 7.29), Vector2(3.94, 7.12), Vector2(4.02, 7.57),
		# left row, back to front: seat centres, then the front stool's leg tips
		Vector2(-3.49, 2.03), Vector2(-3.66, 3.25), Vector2(-3.88, 4.49), Vector2(-4.13, 5.89),
		Vector2(-4.33, 7.27), Vector2(-4.57, 8.71), Vector2(-4.91, 8.98), Vector2(-4.48, 9.12),
	]
	# Act / Assert: every stool is solid ...
	for p: Vector2 in stools:
		assert_gt(probe.call(p.x, p.y), 0, "stool blocked at %s" % p)
	# ... the walkway between the rows is open, right up to the stools ...
	for p: Vector2 in [Vector2(0.0, 2.0), Vector2(0.0, 5.0), Vector2(0.0, 8.0), Vector2(2.8, 2.6),
			Vector2(-2.8, 2.6), Vector2(3.4, 7.3), Vector2(-3.7, 7.3), Vector2(-4.0, 9.6)]:
		assert_eq(probe.call(p.x, p.y), 0, "aisle open at %s" % p)
	# ... and every spawn and interaction stand point still has room for a bro.
	for spot: Node3D in get_tree().get_nodes_in_group("spawn_points").filter(
			func(n): return wing.is_ancestor_of(n)):
		assert_eq(capsule_hits.call(spot.global_position), 0, str(spot.get_meta("spawn_id")))
