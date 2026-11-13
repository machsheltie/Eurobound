extends GutTest
## CharacterLooks: the per-bro pixel / 3D (look B) switch. Tests run on tiny 8x16 fixture frames
## (idle 2, walk 3 per direction) so they do not depend on any bro's real render folder.

const PIXEL_PATH := "res://assets/characters/party/chadwick/chadwick.aseprite"
const FIX := "res://tests/fixtures/looks/%s/look_b/"
const BRO := "test_bro"
const ON := {"looks": {"test_bro": "3d"}, "frames_root": FIX}
const OFF := {"looks": {"test_bro": "pixel"}, "frames_root": FIX}


func _make_sprite() -> PartySprite3D:
	var sprite := PartySprite3D.new()
	add_child_autofree(sprite)
	return sprite


## Ground point of the feet in local metres: top of frame is offset + h/2, the feet row hangs below it.
func _feet_y_m(s: PartySprite3D) -> float:
	var tex: Texture2D = s.sprite_frames.get_frame_texture("idle_south", 0)
	return (s.offset.y + tex.get_height() * 0.5 - s.feet_row_px) * s.pixel_size


## Lord Pilsner's 3D look was approved on the Eurobound Desk (2026-11-13); Chadwick and Bradley stay pixel.
func test_character_looks_committed_config_pilsner_3d_others_pixel() -> void:
	# Arrange / Act
	var pilsner := CharacterLooks.look_for("lord_pilsner")
	var chadwick := CharacterLooks.look_for("chadwick")
	var bradley := CharacterLooks.look_for("bradley")
	# Assert
	assert_eq(pilsner, "3d")
	assert_eq(chadwick, "pixel")
	assert_eq(bradley, "pixel")


func test_character_looks_pilsner_look_b_has_every_direction() -> void:
	# Arrange
	var root := CharacterLooks.frames_root("lord_pilsner")
	# Act / Assert: every action has a frame folder for all 8 directions
	for action in CharacterLooks.ACTIONS:
		for dir in CharacterLooks.DIR_FOLDERS.values():
			assert_true(ResourceLoader.exists(root + "%s/%s/00.png" % [action, dir]), "%s/%s" % [action, dir])


func test_character_looks_missing_entry_defaults_to_pixel() -> void:
	assert_eq(CharacterLooks.look_for("nobody", ON), "pixel")


func test_character_looks_build_frames_has_all_sixteen_animations_with_frame_counts() -> void:
	# Arrange / Act
	var frames := CharacterLooks.build_frames(BRO, ON)
	# Assert
	assert_eq(frames.get_animation_names().size(), 16)
	for dir: String in PartySprite3D.DIRECTIONS:
		assert_true(frames.has_animation("idle_" + dir), "idle_" + dir)
		assert_true(frames.has_animation("walk_" + dir), "walk_" + dir)
		assert_eq(frames.get_frame_count("idle_" + dir), 2, "idle frames " + dir)
		assert_eq(frames.get_frame_count("walk_" + dir), 3, "walk frames " + dir)


func test_character_looks_build_frames_uses_idle_6_and_walk_10_fps() -> void:
	var frames := CharacterLooks.build_frames(BRO, ON)
	assert_eq(frames.get_animation_speed("idle_south"), 6.0)
	assert_eq(frames.get_animation_speed("walk_north_east"), 10.0)


func test_character_looks_dress_pixel_keeps_pixel_frames_and_nearest_filter() -> void:
	# Arrange
	var s := _make_sprite()
	# Act
	CharacterLooks.dress(s, BRO, PIXEL_PATH, OFF)
	# Assert
	assert_eq(s.texture_filter, BaseMaterial3D.TEXTURE_FILTER_NEAREST)
	assert_eq(s.pixel_size_override, 0.0)
	assert_almost_eq(s.pixel_size, 1.8 / s.content_height_px, 0.00001)
	assert_eq(s.sprite_frames.get_frame_texture("idle_south", 0).get_width(), 128)


func test_character_looks_dress_3d_swaps_frames_pixel_size_and_filter() -> void:
	# Arrange
	var s := _make_sprite()
	# Act
	CharacterLooks.dress(s, BRO, PIXEL_PATH, ON)
	# Assert
	assert_eq(s.sprite_frames.get_frame_texture("idle_south", 0).get_width(), 8)
	assert_almost_eq(s.pixel_size, 1.0 / 300.0, 0.0000001)
	assert_eq(s.texture_filter, BaseMaterial3D.TEXTURE_FILTER_LINEAR)
	assert_eq(s.animation, "idle_south")


func test_character_looks_dress_3d_without_folder_falls_back_to_pixel() -> void:
	var s := _make_sprite()
	CharacterLooks.dress(s, "no_such_bro", PIXEL_PATH, {"looks": {"no_such_bro": "3d"}, "frames_root": FIX})
	assert_eq(s.sprite_frames.get_frame_texture("idle_south", 0).get_width(), 128)
	assert_eq(s.texture_filter, BaseMaterial3D.TEXTURE_FILTER_NEAREST)


func test_character_looks_dress_3d_then_pixel_restores_pixel_settings() -> void:
	var s := _make_sprite()
	CharacterLooks.dress(s, BRO, PIXEL_PATH, ON)
	CharacterLooks.dress(s, BRO, PIXEL_PATH, OFF)
	assert_eq(s.texture_filter, BaseMaterial3D.TEXTURE_FILTER_NEAREST)
	assert_eq(s.sprite_frames.get_frame_texture("idle_south", 0).get_width(), 128)


func test_character_looks_feet_stay_on_the_ground_point_in_both_looks() -> void:
	# Arrange
	var pixel := _make_sprite()
	var threed := _make_sprite()
	# Act
	CharacterLooks.dress(pixel, BRO, PIXEL_PATH, OFF)
	CharacterLooks.dress(threed, BRO, PIXEL_PATH, ON)
	# Assert: the feet row sits at local y = 0 (the node origin) for both
	assert_almost_eq(_feet_y_m(pixel), 0.0, 0.0001)
	assert_almost_eq(_feet_y_m(threed), 0.0, 0.0001)
