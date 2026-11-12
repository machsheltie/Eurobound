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
	assert_false(d.has("_placeholder"))
	assert_eq(d["_layout_source"], "orchestrator placeholder; fixed-then-shuffled per author v45")


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


const WING_SCRIPT := preload("res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.gd")


## All sections' niche maps for the maze as currently dressed.
func _all_niches(m: TaproomMaze) -> Array:
	var out := []
	for n in range(1, m.section_count() + 1):
		out.append(m.niches_of(n).duplicate())
	return out


func _sorted_types(niches: Dictionary) -> Array:
	var t: Array = niches.values()
	t.sort()
	return t


func test_maze_curtain_always_routes_to_maze_even_after_completion() -> void:
	# Arrange
	var before: String = WING_SCRIPT.curtain_target(st)
	st.flags[TaproomMaze.FLAG_COMPLETED] = true
	# Act
	var after: String = WING_SCRIPT.curtain_target(st)
	# Assert
	assert_eq([before, after], ["absinthe_arcade_taproom_maze_m1", "absinthe_arcade_taproom_maze_m1"])


func test_maze_exit_rewards_only_once_across_repeat_visits() -> void:
	# Arrange
	BreweryPassport.start_tour(st)
	TaproomMaze.new(st, rng).use_exit()
	var second := TaproomMaze.new(st, rng)
	# Act
	var r := second.use_exit()
	# Assert
	assert_eq([r["action"], r["anchored"], r["repeat"]], ["exit", false, true])
	assert_true(st.flags[TaproomMaze.FLAG_COMPLETED])
	assert_false(st.flags.has(TaproomMaze.RUN_KEY))


func test_maze_layout_identical_across_visits_before_truth_mirror_is_used() -> void:
	# Arrange
	var a := TaproomMaze.new(st, rng)
	a.start_run()
	var first := _all_niches(a)
	# Act
	var b := TaproomMaze.new(st, rng)
	b.start_run()
	# Assert
	assert_eq(_all_niches(b), first)
	assert_eq(first, _all_niches(TaproomMaze.new(st, rng, TaproomMaze.load_data())))


func test_maze_truth_mirror_use_sets_the_persistent_flag() -> void:
	# Arrange
	var m := _maze_with({"a": "truth"})
	# Act
	m.use_niche("a")
	# Assert
	assert_true(st.flags[TaproomMaze.FLAG_TRUTH_USED])


func test_maze_layout_differs_on_next_visit_after_truth_used_keeping_composition() -> void:
	# Arrange
	var base := _all_niches(TaproomMaze.new(st, rng))
	st.flags[TaproomMaze.FLAG_TRUTH_USED] = true
	var m := TaproomMaze.new(st, rng)
	# Act
	m.start_run()
	var shuffled := _all_niches(m)
	# Assert
	assert_ne(shuffled, base)
	for i in base.size():
		assert_eq(_sorted_types(shuffled[i]), _sorted_types(base[i]), "section %d composition" % (i + 1))
		assert_eq(shuffled[i].keys().size(), base[i].keys().size())


func test_maze_shuffle_is_repeatable_with_the_same_seed() -> void:
	# Arrange
	st.flags[TaproomMaze.FLAG_TRUTH_USED] = true
	var a := TaproomMaze.new(st, rng)
	rng.seed = 123
	a.start_run()
	var b := TaproomMaze.new(FakeState.new(), rng)
	b.state.flags[TaproomMaze.FLAG_TRUTH_USED] = true
	rng.seed = 123
	# Act
	b.start_run()
	# Assert
	assert_eq(_all_niches(a), _all_niches(b))


func test_maze_layout_stable_within_a_visit_and_restored_from_saved_state() -> void:
	# Arrange
	st.flags[TaproomMaze.FLAG_TRUTH_USED] = true
	var m := TaproomMaze.new(st, rng)
	m.start_run()
	var visit := _all_niches(m)
	# Act
	m.use_niche(m.niches_of(1).keys()[0])  # whatever it is: hop, trap, truth...
	var mid_visit := _all_niches(m)
	var reloaded := TaproomMaze.new(st, RandomNumberGenerator.new())
	# Assert
	assert_eq(mid_visit, visit)
	assert_eq(_all_niches(reloaded), visit)


func test_maze_new_curtain_entry_after_a_visit_reshuffles() -> void:
	# Arrange
	st.flags[TaproomMaze.FLAG_TRUTH_USED] = true
	var m := TaproomMaze.new(st, rng)
	m.start_run()
	var visit_one := _all_niches(m)
	# Act
	var next := TaproomMaze.new(st, rng)
	next.start_run()
	# Assert
	assert_ne(_all_niches(next), visit_one)


func test_maze_shuffled_section_five_keeps_the_archway_true_exit() -> void:
	# Arrange
	st.flags[TaproomMaze.FLAG_TRUTH_USED] = true
	var m := TaproomMaze.new(st, rng)
	# Act
	m.start_run()
	var errors := TaproomMaze.validate({"sections": _shuffled_sections(m)})
	# Assert
	assert_eq(m.section_data(5)["exit"], "archway")
	assert_eq(m.plate_of(5), "m5")
	assert_eq(errors, [])
	assert_false(m.niches_of(5).values().has("true"))


func _shuffled_sections(m: TaproomMaze) -> Array:
	var out := []
	for n in range(1, m.section_count() + 1):
		var s: Dictionary = m.section_data(n).duplicate(true)
		s["niches"] = m.niches_of(n)
		out.append(s)
	return out


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


# --- Fight wiring (author v45, Eurobound Desk 2026-11-12) ---

func test_taproom_maze_chad_triggers_on_first_section_3_entry() -> void:
	# Arrange
	var m := TaproomMaze.new(st, rng)
	m.start_run()
	m._go(2)
	# Act
	var at_2 := m.take_chad()
	m._go(3)
	var at_3 := m.take_chad()
	# Assert
	assert_false(at_2)
	assert_true(at_3)


func test_taproom_maze_chad_does_not_retrigger_in_same_visit() -> void:
	# Arrange
	var m := TaproomMaze.new(st, rng)
	m.start_run()
	m._go(3)
	m.take_chad()
	# Act
	m._go(1)
	m._go(3)
	var again := m.take_chad()
	var reloaded := TaproomMaze.new(st, rng)  # a room change rebuilds the maze from the run state
	# Assert
	assert_false(again)
	assert_false(reloaded.chad_due())


func test_taproom_maze_chad_returns_on_a_new_visit_after_a_loss() -> void:
	# Arrange
	var m := TaproomMaze.new(st, rng)
	m.start_run()
	m._go(3)
	m.take_chad()  # fought and lost: no defeated flag
	# Act
	m.start_run()
	m._go(3)
	# Assert
	assert_true(m.take_chad())


func test_taproom_maze_chad_not_after_defeat() -> void:
	# Arrange
	st.flags[TaproomBattle.FLAG_MIRROR_CHAD_DEFEATED] = true
	var m := TaproomMaze.new(st, rng)
	m.start_run()
	m._go(3)
	# Act / Assert
	assert_false(m.take_chad())


func test_taproom_maze_run_state_survives_the_chad_fight() -> void:
	# Arrange
	st.flags[TaproomMaze.FLAG_TRUTH_USED] = true
	var m := TaproomMaze.new(st, rng)
	m.start_run()
	m._go(3)
	var layout_before: Dictionary = m.layout.duplicate(true)
	# Act
	m.take_chad()
	var back := TaproomMaze.new(st, rng)
	# Assert
	assert_eq(back.section, 3)
	assert_eq(back.layout, layout_before)
	assert_false(layout_before.is_empty())


func test_taproom_wisp_due_on_arrival_until_defeated_or_survived() -> void:
	# Arrange / Act / Assert
	assert_true(TaproomFights.wisp_due(st), "first arrival, and again after a loss (no flag set)")
	st.flags[TaproomBattle.FLAG_WISP_DEFEATED] = true
	assert_false(TaproomFights.wisp_due(st))
	st.flags.erase(TaproomBattle.FLAG_WISP_DEFEATED)
	st.flags[TaproomBattle.FLAG_WISP_SURVIVED] = true
	assert_false(TaproomFights.wisp_due(st))
