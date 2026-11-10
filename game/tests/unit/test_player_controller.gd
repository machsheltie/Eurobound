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
	p.face("north")
	_interact_point("far_cabinet", Vector3(0, 0, -3.0))
	var near := _interact_point("near_cabinet", Vector3(0.3, 0, -0.5))

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
	p.face("north")
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


# --- Party follow (author ruling ef_party_walk = leader_follow, 2026-11-10) ---

func test_player_leads_chadwick_and_bradley() -> void:
	# Arrange / Act
	var p := _player()

	# Assert
	assert_eq(p.followers.size(), 2)
	assert_eq(p.followers[0].name, "follower_chadwick")
	assert_eq(p.followers[1].name, "follower_bradley")
	for f in p.followers:
		assert_true(f.is_in_group("hall_actors"), "followers take the depth curve")


func test_player_followers_line_up_behind_the_spawn_facing() -> void:
	# Arrange: facing north (away from the camera), so "behind" is +Z
	var p: PlayerController = PlayerScript.new()
	p.position = Vector3(2, 0, 1)
	p.sprite.facing = "north"

	# Act
	add_child_autofree(p)

	# Assert
	for i in p.followers.size():
		var f: Node3D = p.followers[i]
		assert_almost_eq(f.global_position.x, 2.0, 0.01)
		assert_almost_eq(f.global_position.z, 1.0 + PlayerController.FOLLOW_GAP * (i + 1), 0.01)


func test_player_followers_walk_the_leaders_path() -> void:
	# Arrange: leader faces east, followers start west of it
	_floor()
	_camera_looking_north().make_current()
	var p: PlayerController = PlayerScript.new()
	p.sprite.facing = "east"
	add_child_autofree(p)
	await wait_physics_frames(2)

	# Act: walk north for one second
	for i in 60:
		p.step(Vector2(0, -1), 1.0 / 60.0)

	# Assert: the first follower is one gap behind on the path (directly south), walking north
	var f: PartySprite3D = p.followers[0]
	assert_almost_eq(f.global_position.x, p.global_position.x, 0.05)
	assert_almost_eq(f.global_position.z, p.global_position.z + PlayerController.FOLLOW_GAP, 0.05)
	assert_eq(f.action, "walk")
	assert_eq(f.facing, "north")


func test_player_followers_idle_when_the_leader_stops() -> void:
	# Arrange
	_floor()
	_camera_looking_north().make_current()
	var p := _player()
	await wait_physics_frames(2)
	for i in 30:
		p.step(Vector2(1, 0), 1.0 / 60.0)

	# Act
	p.step(Vector2.ZERO, 1.0 / 60.0)

	# Assert
	for f in p.followers:
		assert_eq(f.action, "idle")


# --- Interact cue (author ruling ef_interact_cue = none, 2026-11-10): face it and press ---

func test_player_must_face_a_thing_to_use_it() -> void:
	# Arrange: the cabinet is in reach but behind the bro
	var p := _player()
	p.face("south")
	_interact_point("cabinet_frogger", Vector3(0, 0, -0.5))
	watch_signals(p)

	# Act
	p.try_interact()

	# Assert
	assert_signal_not_emitted(p, "interacted")


func test_player_walking_turns_toward_what_it_uses() -> void:
	# Arrange
	_floor()
	_camera_looking_north().make_current()
	var p := _player()
	p.face("south")
	_interact_point("cabinet_frogger", Vector3(0, 0, -0.6))
	await wait_physics_frames(2)

	# Act: one tap north turns the bro around
	p.step(Vector2(0, -1), 1.0 / 60.0)

	# Assert
	assert_not_null(p.nearest_interactable())


func test_player_input_lock_stops_walking_and_using() -> void:
	# Arrange: a menu is open
	_floor()
	_camera_looking_north().make_current()
	var p := _player()
	p.face("north")
	_interact_point("cabinet_frogger", Vector3(0, 0, -0.5))
	await wait_physics_frames(2)
	var start := p.global_position
	p.input_locked = true
	watch_signals(p)

	# Act
	for i in 30:
		p.step(Vector2(1, 0), 1.0 / 60.0)
	p.try_interact()

	# Assert
	assert_almost_eq(p.global_position.x, start.x, 0.001)
	assert_signal_not_emitted(p, "interacted")
