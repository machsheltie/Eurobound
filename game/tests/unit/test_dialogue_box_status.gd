extends GutTest
## Eurobound-izct: the talk box reads the dialogue-facing `field` fields of status_effects.json
## (text_speed_mult, text_filter trailing_ellipsis, choices replace). Fixture tables only: the live
## data has null speeds and a null Cottonmouth mode/pool.

var st


func before_each() -> void:
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner"},
		{"id": "chadwick", "display_name": "Chadwick"},
		{"id": "bradley", "display_name": "Bradley"},
	]


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _table(field: Dictionary, id := "fixture_status") -> void:
	StatusTable.set_entries({id: {"display_name": "Fixture", "scope": ["field"], "bearer": "bro", "field": field}})


func _box() -> DialogueBox:
	var box := DialogueBox.new()
	box.field_state = st
	box.choice_rng = RandomNumberGenerator.new()
	box.choice_rng.seed = 7
	add_child_autofree(box)
	return box


func _say(box: DialogueBox, who: String, line: String) -> void:
	box.say(who, line)
	box.press("interact")


func test_dialogue_box_status_no_status_leaves_line_and_speed_unchanged() -> void:
	# Arrange
	_table({"text_filter": "trailing_ellipsis", "text_speed_mult": 0.5})
	var box := _box()
	# Act
	_say(box, "Chadwick", "Check this out.")
	# Assert
	assert_eq(box.text, "Check this out.")
	assert_eq(box.text_speed_mult(), 1.0)


func test_dialogue_box_status_trailing_ellipsis_applies_to_that_bros_line() -> void:
	# Arrange
	_table({"text_filter": "trailing_ellipsis"})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	# Act
	_say(box, "Chadwick", "Bro")
	# Assert
	assert_eq(box.text, "Bro...")


func test_dialogue_box_status_trailing_ellipsis_replaces_closing_period() -> void:
	# Arrange
	_table({"text_filter": "trailing_ellipsis"})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	# Act
	_say(box, "Chadwick", "Bro.")
	# Assert
	assert_eq(box.text, "Bro...")


func test_dialogue_box_status_trailing_ellipsis_skips_other_speakers_and_other_bros() -> void:
	# Arrange
	_table({"text_filter": "trailing_ellipsis"})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	# Act
	_say(box, "Tomas", "Tickets.")
	var npc := box.text
	_say(box, "Bradley", "Hey.")
	# Assert
	assert_eq(npc, "Tickets.")
	assert_eq(box.text, "Hey.")


func test_dialogue_box_status_party_wide_row_reaches_every_bro() -> void:
	# Arrange
	_table({"text_filter": "trailing_ellipsis"})
	FieldStatus.apply(st, FieldStatus.PARTY, "fixture_status", 60)
	var box := _box()
	# Act
	_say(box, "Bradley", "Hey")
	# Assert
	assert_eq(box.text, "Hey...")


func test_dialogue_box_status_text_speed_mult_scales_speaking_bros_speed() -> void:
	# Arrange
	_table({"text_speed_mult": 2.0})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	# Act
	_say(box, "Chadwick", "Fast.")
	# Assert
	assert_eq(box.text_speed_mult(), 2.0)


func test_dialogue_box_status_null_speed_mult_changes_nothing() -> void:
	# Arrange
	_table({"text_speed_mult": null})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	# Act
	_say(box, "Chadwick", "Normal.")
	# Assert
	assert_eq(box.text_speed_mult(), 1.0)


func test_dialogue_box_status_reduced_motion_holds_speed_at_normal() -> void:
	# Arrange
	_table({"text_speed_mult": 0.25})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	GameSettings.set_reduced_motion(st, true)
	var box := _box()
	# Act
	_say(box, "Chadwick", "Slow.")
	# Assert
	assert_eq(box.text_speed_mult(), 1.0)


func test_dialogue_box_status_choices_replace_swaps_option_text_for_pool_lines() -> void:
	# Arrange
	_table({"choices": {"mode": "replace", "pool": ["P1", "P2", "P3"]}})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	_say(box, "Chadwick", "Hm.")
	# Act
	box.choose(["Pay", "Refuse", "Run"])
	var shown: Array = box.shown_options()
	box.press("move_down")
	box.press("interact")
	# Assert
	assert_eq(shown.size(), 3)
	for s in shown:
		assert_true(["P1", "P2", "P3"].has(s), "every shown option is a pool line")
	assert_eq(box.options, ["Pay", "Refuse", "Run"], "the real options are kept")
	assert_eq(box.cursor, 1, "the pick still lands on the chosen index")


func test_dialogue_box_status_choices_replace_with_null_pool_or_mode_changes_nothing() -> void:
	# Arrange
	_table({"choices": {"mode": null, "pool": null}})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	_say(box, "Chadwick", "Hm.")
	# Act
	box.choose(["Pay", "Refuse"])
	var shown: Array = box.shown_options()
	box.press("interact")
	# Assert
	assert_eq(shown, ["Pay", "Refuse"])


func test_dialogue_box_status_choices_replace_with_empty_pool_changes_nothing() -> void:
	# Arrange
	_table({"choices": {"mode": "replace", "pool": []}})
	FieldStatus.apply(st, "chadwick", "fixture_status", 60)
	var box := _box()
	_say(box, "Chadwick", "Hm.")
	# Act
	box.choose(["Pay", "Refuse"])
	var shown: Array = box.shown_options()
	box.press("interact")
	# Assert
	assert_eq(shown, ["Pay", "Refuse"])


func test_dialogue_box_status_choices_without_status_show_the_real_options() -> void:
	# Arrange
	_table({"choices": {"mode": "replace", "pool": ["P1"]}})
	var box := _box()
	# Act
	box.choose(["Pay", "Refuse"])
	var shown: Array = box.shown_options()
	box.press("interact")
	# Assert
	assert_eq(shown, ["Pay", "Refuse"])


func test_dialogue_box_status_live_data_gush_locked_trails_off_and_changes_no_speed() -> void:
	# Arrange (the real table: Gush-Locked has trailing_ellipsis and a null speed)
	FieldStatus.apply(st, "bradley", "gush_locked", 60)
	var box := _box()
	# Act
	_say(box, "Bradley", "Bro")
	# Assert
	assert_eq(box.text, "Bro...")
	assert_eq(box.text_speed_mult(), 1.0)
