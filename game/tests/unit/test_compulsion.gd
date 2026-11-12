extends GutTest
## Overworld compulsions (Eurobound-fe10) and the until-cured field row (Eurobound-t162).
## Fixture numbers only; the shipped status_effects.json has every number null and a test proves
## that is inert. Intoxication law sections 3 and 7: bounded, always releases.

var st


class FakeRepo:
	var d: Dictionary

	func _init(items: Dictionary) -> void:
		d = items

	func get_item(id: String) -> Dictionary:
		return d.get(id, {})


func before_each() -> void:
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "lord_pilsner", "display_name": "Lord Pilsner"}]
	StatusTable.set_entries({
		"stare_s": {"scope": ["field"], "field": {"compulsion": {"kind": "stare", "every": {"amount": 5, "unit": "real_seconds"}, "lasts_seconds": 2, "input_lock": true}}},
		"steps_s": {"scope": ["field"], "field": {"compulsion": {"kind": "stare", "every": {"amount": 4, "unit": "steps"}, "lasts_seconds": 1, "input_lock": true}}},
		"clean_s": {"scope": ["field"], "field": {"compulsion": {"kind": "clean_nearest_interactable", "every": {"amount": 1, "unit": "real_seconds"}, "lasts_seconds": 4, "input_lock": true}}},
		"null_s": {"scope": ["field"], "field": {"compulsion": {"kind": "stare", "every": {"amount": null, "unit": null}, "lasts_seconds": null, "input_lock": true}}},
		"nolock_s": {"scope": ["field"], "field": {"compulsion": {"kind": "stare", "every": {"amount": 1, "unit": "real_seconds"}, "lasts_seconds": 2, "input_lock": false}}},
		"cotton_s": {"scope": ["battle", "field"], "default_duration": {"ends_on_rest": true, "until_cured": true}, "cured_by": [{"kind": "rest"}, {"kind": "item_subtype", "value": "drink"}]},
		"gush_s": {},
	})


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _player() -> PlayerController:
	var p: PlayerController = load("res://characters/player/player_controller.gd").new()
	add_child_autofree(p)
	return p


func _tick(p: PlayerController, seconds: float) -> void:
	var left := seconds
	while left > 0.0:
		var d := minf(0.1, left)
		p._update_compulsion(st, d, 0.0)
		left -= d


# --- Compulsion data ---

func test_compulsion_shipped_table_is_inert() -> void:
	StatusTable.reset()
	assert_eq(Compulsion.parse("sugar_rush_hour"), {})
	assert_eq(Compulsion.parse("gush_locked"), {})


func test_compulsion_parse_needs_every_part() -> void:
	assert_eq(Compulsion.parse("null_s"), {})
	assert_eq(Compulsion.parse("nolock_s"), {})
	assert_eq(Compulsion.parse("missing"), {})
	assert_eq(Compulsion.parse("stare_s")["lasts"], 2.0)


func test_compulsion_specs_only_live_statuses() -> void:
	assert_eq(Compulsion.specs(st, "lord_pilsner").size(), 0)
	FieldStatus.apply_steps(st, "lord_pilsner", "stare_s", 100)
	assert_eq(Compulsion.specs(st, "lord_pilsner").size(), 1)


# --- Runner ---

func test_compulsion_stare_fires_locks_and_releases() -> void:
	var p := _player()
	watch_signals(p)
	FieldStatus.apply_steps(st, "lord_pilsner", "stare_s", 1000)
	_tick(p, 4.0)
	assert_false(p.compulsion_locked)
	_tick(p, 1.5)
	assert_true(p.compulsion_locked)
	assert_true(p.is_locked())
	assert_signal_emitted_with_parameters(p, "compulsion_started", ["stare", "stare_s"])
	_tick(p, 2.2)
	assert_false(p.compulsion_locked)
	assert_signal_emitted(p, "compulsion_ended")


func test_compulsion_steps_unit_counts_metres_not_seconds() -> void:
	var p := _player()
	FieldStatus.apply_steps(st, "lord_pilsner", "steps_s", 1000)
	_tick(p, 30.0)
	assert_false(p.compulsion_locked)
	p._update_compulsion(st, 0.016, 4.5)
	assert_true(p.compulsion_locked)


func test_compulsion_null_numbers_never_fire() -> void:
	var p := _player()
	FieldStatus.apply_steps(st, "lord_pilsner", "null_s", 1000)
	FieldStatus.apply_steps(st, "lord_pilsner", "nolock_s", 1000)
	_tick(p, 600.0)
	assert_false(p.compulsion_locked)


func test_compulsion_cure_mid_run_releases() -> void:
	var p := _player()
	FieldStatus.apply_steps(st, "lord_pilsner", "stare_s", 1000)
	_tick(p, 5.2)
	assert_true(p.compulsion_locked)
	FieldStatus.remove(st, "stare_s")
	_tick(p, 0.1)
	assert_false(p.compulsion_locked)


func test_compulsion_never_starts_or_clears_a_menu_lock() -> void:
	var p := _player()
	FieldStatus.apply_steps(st, "lord_pilsner", "stare_s", 1000)
	p.input_locked = true
	_tick(p, 20.0)
	assert_false(p.compulsion_locked)
	p.input_locked = false
	_tick(p, 5.2)
	assert_true(p.compulsion_locked)
	p.input_locked = true
	_tick(p, 3.0)
	assert_false(p.compulsion_locked)
	assert_true(p.input_locked, "releasing the compulsion leaves the other lock alone")


func test_compulsion_leaving_the_tree_releases() -> void:
	var p := _player()
	FieldStatus.apply_steps(st, "lord_pilsner", "stare_s", 1000)
	_tick(p, 5.2)
	assert_true(p.compulsion_locked)
	remove_child(p)
	assert_false(p.compulsion_locked)
	p.free()


func test_compulsion_clean_walks_out_then_back_and_returns() -> void:
	var p := _player()
	var point := Node3D.new()
	point.add_to_group("interact_points")
	add_child_autofree(point)
	point.global_position = Vector3(3, 0, 0)
	FieldStatus.apply_steps(st, "lord_pilsner", "clean_s", 1000)
	_tick(p, 1.1)
	assert_true(p.compulsion_locked)
	assert_gt(p._compulsion_dir().x, 0.9, "out toward the interactable")
	p._comp["left"] = 1.0
	p.global_position = Vector3(2.9, 0, 0)
	assert_lt(p._compulsion_dir().x, -0.9, "and back")
	p._comp["left"] = 0.01
	_tick(p, 0.2)
	assert_false(p.compulsion_locked)
	assert_almost_eq(p.global_position.x, 0.0, 0.01)


func test_compulsion_clean_with_nothing_to_clean_does_nothing() -> void:
	var p := _player()
	FieldStatus.apply_steps(st, "lord_pilsner", "clean_s", 1000)
	_tick(p, 10.0)
	assert_false(p.compulsion_locked)


# --- t162: until-cured field row ---

func test_until_cured_row_persists_and_ignores_steps() -> void:
	assert_true(FieldStatus.apply_from_table(st, "lord_pilsner", "cotton_s"))
	FieldStatus.add_steps(st, 100000)
	FieldStatus.tick(st, 100000.0)
	assert_true(FieldStatus.has(st, "cotton_s"))


func test_until_cured_then_follow_up_lands_on_the_field() -> void:
	FieldStatus.apply_steps(st, "lord_pilsner", "gush_s", 2)
	st.flags[FieldStatus.KEY]["lord_pilsner"]["gush_s"]["then"] = {"status": "cotton_s", "stacks_count": 1}
	FieldStatus.add_steps(st, 3)
	assert_false(FieldStatus.has(st, "gush_s"))
	assert_true(FieldStatus.has(st, "cotton_s"))


func test_until_cured_ends_on_rest() -> void:
	FieldStatus.apply_from_table(st, "lord_pilsner", "cotton_s")
	RestEvents.run(st)
	assert_false(FieldStatus.has(st, "cotton_s"))


func test_until_cured_ends_on_drink_only() -> void:
	FieldStatus.apply_from_table(st, "lord_pilsner", "cotton_s")
	assert_eq(FieldStatus.cure_by_item(st, "lord_pilsner", "beef_jerky", {"subtype": "snack"}), [])
	assert_true(FieldStatus.has(st, "cotton_s"))
	assert_eq(FieldStatus.cure_by_item(st, "lord_pilsner", "cold_one", {"subtype": "drink"}), ["cotton_s"])
	assert_false(FieldStatus.has(st, "cotton_s"))


func test_until_cured_party_row_is_cured_by_drink() -> void:
	FieldStatus.apply_from_table(st, FieldStatus.PARTY, "cotton_s")
	FieldStatus.cure_by_item(st, "lord_pilsner", "cold_one", {"alcohol": true})
	assert_false(FieldStatus.has(st, "cotton_s"))


func test_until_cured_carries_into_battle_as_minus_one_and_survives_write_back() -> void:
	FieldStatus.apply_from_table(st, "lord_pilsner", "cotton_s")
	assert_eq(FieldStatus.battle_statuses(st, "lord_pilsner"), {"cotton_s": -1})
	FieldStatus.write_back_battle(st, "lord_pilsner", {"cotton_s": -1})
	assert_true(FieldStatus.has(st, "cotton_s"))
	FieldStatus.write_back_battle(st, "lord_pilsner", {})
	assert_false(FieldStatus.has(st, "cotton_s"))


func test_until_cured_survives_save_shape() -> void:
	FieldStatus.apply_from_table(st, "lord_pilsner", "cotton_s")
	st.flags = st.flags.duplicate(true)
	assert_true(FieldStatus.has(st, "cotton_s"))


func test_game_state_use_item_drink_cures_field_cottonmouth() -> void:
	FieldStatus.apply_from_table(st, "lord_pilsner", "cotton_s")
	var repo := FakeRepo.new({"cold_one": {"subtype": "drink"}})
	st.party = [{"id": "lord_pilsner", "hp": 1, "max_hp": 10, "bravado": 0, "max_bravado": 5}]
	st.inventory = {"cold_one": 1}
	assert_true(st.use_item("cold_one", repo))
	assert_false(FieldStatus.has(st, "cotton_s"))
