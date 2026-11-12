extends GutTest
## Absinthium Taproom mirror maze (the_absinthium_taproom.md 94-103, 140-150; rounds v41-44).

const M1 := preload("res://worlds/debaucheryville/absinthe_arcade_taproom_maze_m1_hd2d.tscn")
const M5 := preload("res://worlds/debaucheryville/absinthe_arcade_taproom_maze_m5_hd2d.tscn")

class FakeState:
	var flags := {}
	var inventory := {}

var st: FakeState
var rng: RandomNumberGenerator


func before_each() -> void:
	st = FakeState.new()
	rng = RandomNumberGenerator.new()
	rng.seed = 7


## A maze whose section 1 holds exactly the given niche -> type map.
func _maze_with(niches: Dictionary) -> TaproomMaze:
	var d := TaproomMaze.load_data()
	d["sections"][0]["niches"] = niches
	return TaproomMaze.new(st, rng, d)


func test_maze_data_matches_design_counts() -> void:
	# Arrange
	var d := TaproomMaze.load_data()
	# Act
	var errors := TaproomMaze.validate(d)
	# Assert
	assert_eq(errors, [])
	assert_true(bool(d.get("_placeholder", false)))


func test_maze_validate_flags_a_section_without_a_truth_mirror() -> void:
	# Arrange
	var d := TaproomMaze.load_data()
	d["sections"][1]["niches"]["left_near"] = "portal"
	# Act
	var errors := TaproomMaze.validate(d)
	# Assert
	assert_gt(errors.size(), 0)


func test_maze_section_five_archway_is_the_true_exit_on_plate_m5() -> void:
	# Arrange
	var m := TaproomMaze.new(st, rng)
	# Act
	var s5 := m.section_data(5)
	# Assert
	assert_eq([s5["plate"], s5["exit"], s5["niches"].size()], ["m5", "archway", 4])


func test_maze_true_mirror_advances_one_section() -> void:
	# Arrange
	var m := _maze_with({"a": "true"})
	# Act
	var r := m.use_niche("a")
	# Assert
	assert_eq([r["action"], m.section], ["section", 2])


func test_maze_portal_goes_to_another_section_never_the_same() -> void:
	# Arrange
	var seen := {}
	# Act
	for i in 40:
		st = FakeState.new()
		var m := _maze_with({"a": "portal"})
		m.use_niche("a")
		seen[m.section] = true
	# Assert
	assert_false(seen.has(1))
	assert_eq(seen.keys().size(), 4)


func test_maze_portal_is_repeatable_with_the_same_seed() -> void:
	# Arrange
	var a := _maze_with({"a": "portal"})
	rng.seed = 7
	var b := _maze_with({"a": "portal"})
	# Act
	a.rng.seed = 99
	b.rng.seed = 99
	a.use_niche("a")
	b.use_niche("a")
	# Assert
	assert_eq(a.section, b.section)


func test_maze_trap_reverses_controls_for_30_seconds() -> void:
	# Arrange
	var m := _maze_with({"a": "trap"})
	# Act
	m.use_niche("a")
	var during := FieldStatus.controls_reversed(st)
	FieldStatus.tick(st, 29.0)
	var late := FieldStatus.controls_reversed(st)
	FieldStatus.tick(st, 2.0)
	# Assert
	assert_eq([during, late, FieldStatus.controls_reversed(st)], [true, true, false])


func test_maze_confusion_mirror_applies_green_fairy_confusion() -> void:
	# Arrange
	var m := _maze_with({"a": "confusion"})
	# Act
	m.use_niche("a")
	# Assert
	assert_true(FieldStatus.has(st, FieldStatus.GREEN_FAIRY_CONFUSION))
	assert_true(m.confused)


func test_maze_truth_reveals_for_ten_seconds_then_rests() -> void:
	# Arrange
	var m := _maze_with({"a": "truth"})
	# Act
	m.use_niche("a")
	var at_start := m.revealed()
	m.tick(9.9)
	var near_end := m.revealed()
	m.tick(0.2)
	# Assert
	assert_eq([at_start, near_end, m.revealed()], [true, true, false])


func test_maze_exit_awards_opener_and_party_anchor_when_never_confused() -> void:
	# Arrange
	BreweryPassport.start_tour(st)
	var m := TaproomMaze.new(st, rng)
	# Act
	var r := m.use_exit()
	# Assert
	assert_true(BreweryPassport.has_opener(st, "absinthium_taproom"))
	assert_true(st.flags[TaproomMaze.FLAG_COMPLETED])
	assert_true(r["anchored"])
	for id in TaproomMaze.BROS:
		assert_true(FieldStatus.has_reality_anchor(st, id))


func test_maze_exit_after_confusion_gives_no_anchor() -> void:
	# Arrange
	BreweryPassport.start_tour(st)
	var m := _maze_with({"a": "confusion"})
	m.use_niche("a")
	# Act
	var r := m.use_exit()
	# Assert
	assert_false(r["anchored"])
	assert_false(FieldStatus.has_reality_anchor(st, "chadwick"))


func test_maze_exit_before_tour_still_completes_without_opener() -> void:
	# Arrange
	var m := TaproomMaze.new(st, rng)
	# Act
	m.use_exit()
	# Assert
	assert_true(st.flags[TaproomMaze.FLAG_COMPLETED])
	assert_false(BreweryPassport.has_opener(st, "absinthium_taproom"))


func test_maze_rooms_spawn_and_niche_spots_sit_on_open_floor() -> void:
	# Arrange / Act / Assert
	for scene: PackedScene in [M1, M5]:
		var room: TaproomMazeRoom = scene.instantiate()
		room.spawn_player = false
		add_child_autofree(room)
		await get_tree().process_frame
		var hw := room.floor_half_width
		var sp := room.default_spawn_xz
		assert_true(absf(sp.x) < hw - 0.5 and sp.y > 1.0 and sp.y < room.floor_depth - 0.5, room.plate_id + " spawn")
		var reach := PlayerController.INTERACT_RANGE / room.world_scale - 0.3
		for id: String in room.niches.keys():
			var p: Vector3 = room.niches[id]["pos"]
			var nearest := Vector2(clampf(p.x, -hw, hw), clampf(p.z, 1.0, room.floor_depth))
			assert_lt(Vector2(p.x, p.z).distance_to(nearest), reach, room.plate_id + " " + id)
		assert_eq(room.sprites.size(), room.niches.size())


func test_maze_room_dresses_per_section_and_swaps_to_revealed_textures() -> void:
	# Arrange
	var room: TaproomMazeRoom = M1.instantiate()
	room.spawn_player = false
	add_child_autofree(room)
	await get_tree().process_frame
	var rest_tex: Texture2D = room.sprites["back_l"].texture
	# Act
	room.maze.section = 1
	room.maze.use_niche("back_l")  # section 1's back_l is the Truth mirror
	room._refresh_textures()
	var revealed_tex: Texture2D = room.sprites["back_l"].texture
	room.maze.tick(10.5)
	room._refresh_textures()
	# Assert
	assert_ne(rest_tex.resource_path, revealed_tex.resource_path)
	assert_eq(room.sprites["back_l"].texture.resource_path, rest_tex.resource_path)
	assert_true(room.sprites["right_near"].visible)
