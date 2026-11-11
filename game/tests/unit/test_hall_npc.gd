extends GutTest
## HallNpc: Jakub mutters an approved line when the leader comes near, then goes quiet a while.

const HALL := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")


func _jakub() -> HallNpc:
	var npc := HallNpc.new()
	add_child_autofree(npc)
	npc.setup("res://assets/characters/npcs/absinthe_arcade/jakub_tokens_dvorak.aseprite", 112.0, 121.0,
		"north_west", ["token_machine"])
	npc.set_process(false)
	return npc


func test_hall_npc_mutters_when_the_leader_is_near() -> void:
	# Arrange
	var npc := _jakub()
	# Act
	npc.tick(0.1, npc.global_position + Vector3(1.0, 0, 0))
	# Assert
	assert_true(npc.bark.visible)
	assert_has(ArcadeMicrocopy.mutter_pool("token_machine"), npc.bark.text)


func test_hall_npc_stays_quiet_when_the_leader_is_far() -> void:
	# Arrange
	var npc := _jakub()
	# Act
	npc.tick(0.1, npc.global_position + Vector3(5.0, 0, 0))
	# Assert
	assert_false(npc.bark.visible)


func test_hall_npc_goes_quiet_after_a_line() -> void:
	# Arrange
	var npc := _jakub()
	var near := npc.global_position + Vector3(0.5, 0, 0)
	npc.tick(0.1, near)
	# Act: the line runs out, then the leader is still there a moment later.
	npc.tick(HallNpc.SHOW_S, near)
	npc.tick(1.0, near)
	# Assert
	assert_false(npc.bark.visible)


func test_hall_npc_jakub_stands_in_the_hall_at_the_bros_scale() -> void:
	# Arrange
	var hall: Node3D = HALL.instantiate()
	add_child_autofree(hall)
	await wait_physics_frames(2)
	# Act
	var npc: HallNpc = hall.jakub
	# Assert
	assert_not_null(npc)
	assert_almost_eq(npc.sprite.pixel_size, 1.8 / 117.0, 0.0001)


func test_hall_npc_tomas_stands_behind_the_prize_counter() -> void:
	# Arrange
	var hall: Node3D = HALL.instantiate()
	add_child_autofree(hall)
	await wait_physics_frames(2)
	# Act
	var npc: HallNpc = hall.npcs.get("tomas_two_fifty")
	# Assert: placed, with no ambient lines (none approved).
	assert_not_null(npc)
	assert_eq(npc.jobs, [])


func test_hall_npc_ring_shows_for_facings_it_knows_and_hides_otherwise() -> void:
	# Arrange
	var npc := _jakub()
	npc.add_ring({"south": Vector2(50, 60)})
	# Act
	npc.sprite.facing = "north"
	npc._place_ring()
	var north := npc.ring.visible
	npc.sprite.facing = "south"
	npc._place_ring()
	# Assert
	assert_false(north)
	assert_true(npc.ring.visible)
