extends GutTest
## PlayerController: the bro the player walks around the HD-2D scenes. Input is camera-relative
## (up on the stick walks away from the camera), the sprite plays walk/idle facing the way it moves,
## and walls stop it.

const PlayerScript := preload("res://characters/player/player_controller.gd")


func _camera_looking_north() -> Camera3D:
	var cam := Camera3D.new()
	add_child_autofree(cam)
	cam.look_at_from_position(Vector3(0, 8, 12), Vector3.ZERO, Vector3.UP)
	return cam


func _floor() -> StaticBody3D:
	var body := StaticBody3D.new()
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(40, 0.2, 40)
	cs.shape = box
	cs.position.y = -0.1
	body.add_child(cs)
	add_child_autofree(body)
	return body


func _player() -> PlayerController:
	var p: PlayerController = PlayerScript.new()
	add_child_autofree(p)
	return p


func test_player_move_direction_up_walks_away_from_camera() -> void:
	# Arrange
	var cam := _camera_looking_north()

	# Act
	var dir := PlayerController.move_direction(Vector2(0, -1), cam)

	# Assert
	assert_almost_eq(dir.z, -1.0, 0.001)
	assert_almost_eq(dir.x, 0.0, 0.001)
	assert_almost_eq(dir.y, 0.0, 0.001)


func test_player_move_direction_right_walks_screen_right() -> void:
	# Arrange
	var cam := _camera_looking_north()

	# Act
	var dir := PlayerController.move_direction(Vector2(1, 0), cam)

	# Assert
	assert_almost_eq(dir.x, 1.0, 0.001)


func test_player_move_direction_diagonal_is_not_faster() -> void:
	# Arrange
	var cam := _camera_looking_north()

	# Act
	var dir := PlayerController.move_direction(Vector2(1, -1), cam)

	# Assert
	assert_almost_eq(dir.length(), 1.0, 0.001)


func test_player_walking_plays_walk_facing_the_move() -> void:
	# Arrange
	_floor()
	var cam := _camera_looking_north()
	cam.make_current()
	var p := _player()

	# Act
	p.step(Vector2(1, 0), 1.0 / 60.0)

	# Assert
	assert_eq(p.sprite.action, "walk")
	assert_eq(p.sprite.facing, "east")


func test_player_no_input_goes_idle() -> void:
	# Arrange
	_floor()
	_camera_looking_north().make_current()
	var p := _player()
	p.step(Vector2(1, 0), 1.0 / 60.0)

	# Act
	p.step(Vector2.ZERO, 1.0 / 60.0)

	# Assert
	assert_eq(p.sprite.action, "idle")
	assert_eq(p.sprite.facing, "east")


func test_player_wall_stops_movement() -> void:
	# Arrange: a wall 1 m in front (north) of the player
	_floor()
	_camera_looking_north().make_current()
	var wall := StaticBody3D.new()
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(10, 4, 0.3)
	cs.shape = box
	wall.add_child(cs)
	wall.position = Vector3(0, 2, -1.0)
	add_child_autofree(wall)
	var p := _player()
	await wait_physics_frames(2)

	# Act: walk north for two seconds
	for i in 120:
		p.step(Vector2(0, -1), 1.0 / 60.0)

	# Assert: stopped short of the wall's face
	assert_gt(p.global_position.z, -1.0 + 0.15)


func test_player_registers_move_and_interact_actions() -> void:
	# Arrange / Act
	PlayerController.ensure_input_actions()

	# Assert
	for action in ["move_up", "move_down", "move_left", "move_right", "interact"]:
		assert_true(InputMap.has_action(action), action)


func _interact_point(id: String, pos: Vector3) -> Marker3D:
	var m := Marker3D.new()
	m.add_to_group("interact_points")
	m.set_meta("interact_id", id)
	m.position = pos
	add_child_autofree(m)
	return m


func test_player_default_bro_is_lord_pilsner() -> void:
	# Arrange / Act: the approved vertical-slice spec walks the world as Lord Pilsner
	var p := _player()

	# Assert
	assert_eq(p.bro, "lord_pilsner")


func test_player_nearest_interactable_within_range() -> void:
	# Arrange
	var p := _player()
	_interact_point("far_cabinet", Vector3(0, 0, -3.0))
	var near := _interact_point("near_cabinet", Vector3(0.6, 0, -0.3))

	# Act
	var found := p.nearest_interactable()

	# Assert
	assert_eq(found, near)


func test_player_nothing_to_interact_with_out_of_range() -> void:
	# Arrange
	var p := _player()
	_interact_point("far_cabinet", Vector3(0, 0, -3.0))

	# Act / Assert
	assert_null(p.nearest_interactable())


func test_player_interact_emits_the_point_id() -> void:
	# Arrange
	var p := _player()
	_interact_point("cabinet_frogger", Vector3(0, 0, -0.5))
	watch_signals(p)

	# Act
	p.try_interact()

	# Assert
	assert_signal_emitted_with_parameters(p, "interacted", ["cabinet_frogger"])


func test_player_interact_with_nothing_near_emits_nothing() -> void:
	# Arrange
	var p := _player()
	watch_signals(p)

	# Act
	p.try_interact()

	# Assert
	assert_signal_not_emitted(p, "interacted")


func test_player_sprite_takes_the_hall_depth_curve() -> void:
	# Arrange / Act
	var p := _player()

	# Assert: the sprite, not the physics body, is scaled by the hall's depth curve
	assert_true(p.sprite.is_in_group("hall_actors"))
	assert_false(p.is_in_group("hall_actors"))
