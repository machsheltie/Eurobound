extends GutTest
## Club flyer panel on the Arcade's front face: remnants until club_flyer_placed, then the flyer.

const SCENE := "res://worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn"

class FakeState:
	var flags := {}


func _room() -> Node3D:
	var room: Node3D = load(SCENE).instantiate()
	room.set("spawn_player", false)
	add_child_autofree(room)
	return room


func test_both_states_built_on_the_front_face_right_of_the_door() -> void:
	var room := _room()
	assert_eq(room.flyer_cards.size(), 2)
	for st in ["empty", "posted"]:
		var card: MeshInstance3D = room.flyer_cards[st]
		# Right of the doorway (positive x), above the pavement, just proud of the front wall.
		assert_gt(card.position.x, 0.0, st)
		assert_gt(card.position.y, 1.5, st)
		assert_almost_eq(card.position.z, room.FLYER_STANDOFF, 0.001, st)


func test_remnants_until_placed_then_flyer() -> void:
	var room := _room()
	var state := FakeState.new()
	room.refresh_flyer_panel(state)
	assert_true(room.flyer_cards["empty"].visible)
	assert_false(room.flyer_cards["posted"].visible)
	state.flags["club_flyer_placed"] = true
	room.refresh_flyer_panel(state)
	assert_false(room.flyer_cards["empty"].visible)
	assert_true(room.flyer_cards["posted"].visible)


func test_day_night_swap_finds_every_texture() -> void:
	var room := _room()
	for tag in ["day", "night"]:
		room.set("night", tag == "night")
		for st in ["empty", "posted"]:
			var mat: StandardMaterial3D = room.flyer_cards[st].material_override
			assert_not_null(mat.albedo_texture, "%s %s" % [st, tag])


func test_cabinet_is_a_free_wifi_hotspot_reachable_from_the_street() -> void:
	# Arrange
	var room := _room()
	var h: WifiHotspot = room.facade_hotspot
	var cab: Vector2 = room.SOLID_PROPS[0][0]
	var cab_size: Vector2 = room.SOLID_PROPS[0][1]
	# Act
	var gap := h.position.z - (cab.y + cab_size.y * 0.5)
	# Assert
	assert_not_null(h)
	assert_eq(h.hotspot_id, "debaucheryville_absinthe_arcade_facade")
	assert_true(h.is_in_group("interact_points"))
	assert_eq(h.get_meta("interact_id"), "debaucheryville_absinthe_arcade_facade")
	assert_almost_eq(h.position.x, cab.x, 0.01, "at the cabinet")
	assert_gt(gap, 0.0, "in front of the cabinet, not inside it or the wall")
	assert_lt(gap, 1.0, "within interact reach of a player standing on the street")
	assert_gt(h.position.z, 0.0, "street side of the front wall")
