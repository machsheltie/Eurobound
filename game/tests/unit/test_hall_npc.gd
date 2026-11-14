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


func test_hall_npc_jakub_stands_in_the_hall_in_his_3d_look_at_the_bros_scale() -> void:
	# Arrange
	var hall: Node3D = HALL.instantiate()
	add_child_autofree(hall)
	await wait_physics_frames(2)
	# Act
	var npc: HallNpc = hall.jakub
	# Assert: look-B frames (blind G4 pass 2026-11-14) at the bros' look-B density, smooth-filtered.
	assert_not_null(npc)
	assert_almost_eq(npc.sprite.pixel_size, 1.0 / CharacterLooks.DEFAULT_PPM, 0.000001)
	assert_true(npc.sprite.smooth)
	assert_eq(npc.sprite.sprite_frames.get_frame_count("idle_south"), 6)
	assert_eq(npc.sprite.sprite_frames.get_frame_count("walk_north_west"), 7)
	assert_eq(npc.sprite.feet_row_px, 640.0)


func test_hall_npc_without_look_b_frames_keeps_the_pixel_sprite() -> void:
	# Arrange
	var npc := HallNpc.new()
	add_child_autofree(npc)
	# Act: an id with no look-B folder falls back to the .aseprite frames.
	npc.setup("res://assets/characters/npcs/absinthe_arcade/jakub_tokens_dvorak.aseprite", 112.0, 121.0,
		"north_west", [], 0.0, "no_such_character")
	# Assert
	assert_false(npc.sprite.smooth)
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


func test_hall_npc_cara_stands_in_her_3d_look_in_the_evening() -> void:
	# Arrange: the group is present in the evening.
	GameClock.set_time(GameState, 21 * 60)
	var hall: Node3D = HALL.instantiate()
	add_child_autofree(hall)
	await wait_physics_frames(2)
	# Act
	var npc: HallNpc = hall.npcs.get("cara")
	# Assert: look-B frames (blind G4 pass 2026-11-14).
	assert_not_null(npc)
	assert_true(npc.sprite.smooth)
	assert_almost_eq(npc.sprite.pixel_size, 1.0 / CharacterLooks.DEFAULT_PPM, 0.000001)


func test_hall_npc_tomas_wears_no_ring_until_the_tip_then_the_ringed_3d_set() -> void:
	# Arrange
	var hall: Node3D = HALL.instantiate()
	add_child_autofree(hall)
	await wait_physics_frames(2)
	var tomas: HallNpc = hall.npcs.get("tomas_two_fifty")
	var plain_tex: Texture2D = tomas.sprite.sprite_frames.get_frame_texture("idle_south", 0)
	# Act: Grandpa Provides gives the tip.
	hall.ring_on()
	# Assert: still 3D (no fallback to the pixel ring sprite), now the ringed frames, no overlay.
	assert_true(tomas.is_look_b())
	var ring_tex: Texture2D = tomas.sprite.sprite_frames.get_frame_texture("idle_south", 0)
	assert_ne(ring_tex.resource_path, plain_tex.resource_path)
	assert_string_contains(ring_tex.resource_path, "tomas_two_fifty_ring/look_b/")
	assert_null(tomas.ring)


func test_hall_npc_the_girls_stand_in_their_3d_looks_in_the_evening() -> void:
	# Arrange
	GameClock.set_time(GameState, 21 * 60)
	var hall: Node3D = HALL.instantiate()
	add_child_autofree(hall)
	await wait_physics_frames(2)
	# Act / Assert
	for id in ["ashleigh", "brynleigh", "kenleigh"]:
		var npc: HallNpc = hall.npcs.get(id)
		assert_not_null(npc, id)
		assert_true(npc.is_look_b(), id)
