extends GutTest
## PartySprite3D: picks the right directional animation and sizes the sprite in real metres.

const SpriteScript := preload("res://characters/party/party_sprite_3d.gd")


func _make_frames() -> SpriteFrames:
	var frames := SpriteFrames.new()
	frames.remove_animation("default")
	var img := Image.create(128, 128, false, Image.FORMAT_RGBA8)
	var tex := ImageTexture.create_from_image(img)
	for action in ["idle", "walk"]:
		for dir in SpriteScript.DIRECTIONS:
			var anim: String = "%s_%s" % [action, dir]
			frames.add_animation(anim)
			frames.add_frame(anim, tex)
	return frames


func _make_sprite() -> PartySprite3D:
	var sprite: PartySprite3D = SpriteScript.new()
	sprite.sprite_frames = _make_frames()
	add_child_autofree(sprite)
	return sprite


func _make_camera_looking_north() -> Camera3D:
	# Camera at +Z looking toward -Z (north), the way the fixed HD-2D camera looks into a scene.
	var cam := Camera3D.new()
	add_child_autofree(cam)
	cam.look_at_from_position(Vector3(0, 5, 10), Vector3.ZERO, Vector3.UP)
	return cam


func test_party_sprite_move_toward_camera_faces_south() -> void:
	# Arrange
	var sprite := _make_sprite()
	var cam := _make_camera_looking_north()
	# Act
	sprite.face_world_direction(Vector3(0, 0, 1), cam)
	# Assert
	assert_eq(sprite.facing, "south")


func test_party_sprite_move_away_from_camera_faces_north() -> void:
	# Arrange
	var sprite := _make_sprite()
	var cam := _make_camera_looking_north()
	# Act
	sprite.face_world_direction(Vector3(0, 0, -1), cam)
	# Assert
	assert_eq(sprite.facing, "north")


func test_party_sprite_move_screen_right_faces_east() -> void:
	# Arrange
	var sprite := _make_sprite()
	var cam := _make_camera_looking_north()
	# Act
	sprite.face_world_direction(Vector3(1, 0, 0), cam)
	# Assert
	assert_eq(sprite.facing, "east")


func test_party_sprite_zero_direction_keeps_facing() -> void:
	# Arrange
	var sprite := _make_sprite()
	var cam := _make_camera_looking_north()
	sprite.facing = "west"
	# Act
	sprite.face_world_direction(Vector3.ZERO, cam)
	# Assert
	assert_eq(sprite.facing, "west")


func test_party_sprite_action_and_facing_play_matching_animation() -> void:
	# Arrange
	var sprite := _make_sprite()
	# Act
	sprite.action = "walk"
	sprite.facing = "north_east"
	# Assert
	assert_eq(sprite.animation, &"walk_north_east")


func test_party_sprite_pixel_size_matches_real_height() -> void:
	# Arrange
	var sprite := _make_sprite()
	# Act
	sprite.height_m = 1.8
	sprite.content_height_px = 117.0
	# Assert
	assert_almost_eq(sprite.pixel_size, 1.8 / 117.0, 0.000001)
