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


func test_restroom_statue_is_one_layer_between_the_niche_and_jakub_day_and_night() -> void:
	# Arrange
	var room: Node3D = RESTROOM.instantiate()
	room.set("spawn_player", false)
	add_child_autofree(room)
	var spec: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(room.HANDS_DIR + "statue.json"))
	# Act / Assert: one quad, behind Jakub and the hands, in front of the far wall's niche
	var statue: MeshInstance3D = room.statue
	assert_not_null(statue)
	assert_eq(room.find_children("green_fairy_statue*", "MeshInstance3D", true, false).size(), 1)
	assert_gt(statue.position.z, 0.0, "the statue stands in front of the niche wall")
	assert_lt(statue.position.z, room.JAKUB_AT.z, "the statue is behind Jakub")
	for side in ["left", "right"]:
		assert_gt(room.statue_hands[side].position.z, statue.position.z, "%s hand is in front of the statue" % side)
	assert_eq(statue.get_meta("interact_id"), "green_fairy_statue")
	assert_eq(statue.get_meta("node_id"), "aa_node_restroom_statue")
	var mat: ShaderMaterial = statue.material_override
	assert_true(mat.get_shader_parameter("use_alpha"), "the cut-out discards outside her")
	assert_eq(mat.get_shader_parameter("rect_px"), Vector4(spec["plate_xy"][0], spec["plate_xy"][1],
		spec["size"][0], spec["size"][1]))
	for tag in ["night", "day"]:
		room.night = tag == "night"
		var tex: Texture2D = mat.get_shader_parameter("albedo_tex")
		assert_eq(tex.resource_path, room.HANDS_DIR + String(spec["files"][tag]), "%s statue texture" % tag)
		assert_eq(mat.get_shader_parameter("use_emission"), tag == "night", "%s emission" % tag)
	var emit: Texture2D = mat.get_shader_parameter("emit_tex")
	assert_eq(emit.resource_path, room.HANDS_DIR + String(spec["files"]["emit"]))


func test_restroom_statue_plinth_bottom_lands_above_the_floor_on_its_plane() -> void:
	# Arrange: the lowest plate row of the cut-out, seen through the paint camera on the statue's plane.
	var room: Node3D = RESTROOM.instantiate()
	room.set("spawn_player", false)
	add_child_autofree(room)
	var r: Vector4 = (room.statue.material_override as ShaderMaterial).get_shader_parameter("rect_px")
	# Act
	var bottom: Vector3 = room.plate_point_on_plane(Vector2(r.x + r.z * 0.5, r.y + r.w), room.STATUE_Z)
	# Assert: a plane too far back would sink the plinth under the floor and the floor would hide it.
	assert_gte(bottom.y, 0.0)


func test_jakub_restroom_asleep_sprite_is_the_3d_render_at_the_bros_density() -> void:
	# Arrange: he is there after 01:00 once the scene has been seen.
	GameState.flags["jakub_restroom_discovered"] = true
	GameClock.set_time(GameState, 2 * 60)
	# Act
	var room := await _open()
	# Assert: the 3D cradled render (562x327 at 300 px/m), smooth-filtered like the bros' look-B frames.
	assert_not_null(room.jakub_asleep)
	assert_eq(room.jakub_asleep.texture.get_size(), Vector2(562, 327))
	assert_almost_eq(room.jakub_asleep.pixel_size, 1.0 / CharacterLooks.DEFAULT_PPM, 0.000001)
	assert_ne(room.jakub_asleep.texture_filter, BaseMaterial3D.TEXTURE_FILTER_NEAREST)
