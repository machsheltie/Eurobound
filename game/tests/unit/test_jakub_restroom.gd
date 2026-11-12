extends GutTest
## Jakub's restroom scene (approved 2026-11-12): after 01:00 the first restroom visit plays it once,
## gives the "ASK ME ABOUT TOKENS" pin, and leaves him asleep at the Green Fairy.

const RESTROOM := preload("res://worlds/debaucheryville/absinthe_arcade_restroom_hd2d.tscn")

var _saved := {}


func before_each() -> void:
	SceneRouter.ensure_game_started(get_tree())
	_saved = {"inventory": GameState.inventory.duplicate(true), "flags": GameState.flags.duplicate(true)}


func after_each() -> void:
	GameState.inventory = _saved["inventory"]
	GameState.flags = _saved["flags"]


func _open() -> Node3D:
	var room: Node3D = RESTROOM.instantiate()
	add_child_autofree(room)
	await wait_physics_frames(2)
	room.dialogue.beat_scale = 0.01
	return room


func test_jakub_restroom_scene_plays_once_after_one_am_and_gives_the_pin() -> void:
	# Arrange
	GameState.flags.erase("jakub_restroom_discovered")
	GameState.inventory.erase("jakub_tokens_flair_pin")
	GameClock.set_time(GameState, 1 * 60 + 15)
	var room := await _open()
	# Act: press through the scene.
	var said := []
	for i in 300:
		if bool(GameState.flags.get("jakub_restroom_discovered", false)):
			break
		if room.dialogue.mode == "say":
			said.append(room.dialogue.text)
			room.dialogue.press("interact")
		await wait_process_frames(1)
	# Assert
	assert_eq(said[0], "Look at that. High class. Back home you pass out in a stall and someone steals your shoes. Over here, the decor cradles you.")
	assert_has(said, "Tokens. Toilet.")
	assert_eq(said[-1], "Man's living the dream. Let's go win some plastic crap.")
	assert_eq(int(GameState.inventory.get("jakub_tokens_flair_pin", 0)), 1)
	assert_not_null(room.jakub_asleep)


func test_jakub_restroom_not_there_in_the_evening() -> void:
	# Arrange
	GameClock.set_time(GameState, 22 * 60)
	# Act
	var room := await _open()
	# Assert
	assert_null(room.jakub_asleep)
	assert_eq(room.dialogue.mode, "")


func test_statue_hands_cover_her_forearm_line_in_front_of_jakub_day_and_night() -> void:
	# Arrange
	var room: Node3D = RESTROOM.instantiate()
	room.set("spawn_player", false)
	add_child_autofree(room)
	# Act / Assert: both hands, in front of Jakub's anchor, each painting its own plate rect
	assert_eq(room.statue_hands.size(), 2)
	for side in ["left", "right"]:
		var hand: MeshInstance3D = room.statue_hands[side]
		assert_gt(hand.position.z, room.JAKUB_AT.z, "%s hand is between Jakub and the camera" % side)
		for tag in ["night", "day"]:
			room.night = tag == "night"
			var mat: ShaderMaterial = hand.material_override
			assert_not_null(mat.get_shader_parameter("albedo_tex"), "%s %s texture" % [side, tag])
			var r: Vector4 = mat.get_shader_parameter("rect_px")
			assert_gt(r.z, 0.0, "%s %s rect has width" % [side, tag])
			assert_true(mat.get_shader_parameter("use_alpha"), "%s cut-out discards outside the hand" % side)
