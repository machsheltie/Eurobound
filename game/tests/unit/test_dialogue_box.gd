extends GutTest
## DialogueBox: one spoken line or choice at a time; `say` waits for a press, `choose` returns the
## picked index, `beat` is a short silent pause.


func _box() -> DialogueBox:
	var box := DialogueBox.new()
	box.beat_scale = 0.01
	add_child_autofree(box)
	return box


func test_dialogue_box_say_shows_the_line_and_waits_for_a_press() -> void:
	# Arrange
	var box := _box()
	var done := [false]
	var run := func() -> void:
		await box.say("Tomas", "Tickets or get out.")
		done[0] = true
	# Act
	run.call()
	var waiting: bool = not done[0]
	box.press("interact")
	# Assert
	assert_true(waiting, "say must wait for the press")
	assert_true(done[0], "the press moves the line on")
	assert_eq(box.speaker, "Tomas")
	assert_eq(box.text, "Tickets or get out.")
	assert_eq(box.mode, "")


func test_dialogue_box_say_ignores_everything_but_interact() -> void:
	# Arrange
	var box := _box()
	var done := [false]
	var run := func() -> void:
		await box.say("Jakub", "Tokens.")
		done[0] = true
	run.call()
	# Act
	for action in ["move_up", "move_down", "cancel"]:
		box.press(action)
	# Assert
	assert_false(done[0])
	assert_eq(box.mode, "say")
	box.press("interact")


func test_dialogue_box_choose_returns_the_picked_index() -> void:
	# Arrange
	var box := _box()
	var picked := [-1]
	var run := func() -> void:
		picked[0] = await box.choose(["Pay", "Refuse", "Run"])
	run.call()
	# Act
	box.press("move_down")
	box.press("move_down")
	box.press("interact")
	# Assert
	assert_eq(picked[0], 2)
	assert_eq(box.mode, "")


func test_dialogue_box_choose_cursor_wraps_both_ways() -> void:
	# Arrange
	var box := _box()
	var picked := [-1]
	var run := func() -> void:
		picked[0] = await box.choose(["A", "B", "C"])
	run.call()
	# Act
	box.press("move_up")
	var wrapped_up := box.cursor
	box.press("move_down")
	var wrapped_down := box.cursor
	box.press("interact")
	# Assert
	assert_eq(wrapped_up, 2)
	assert_eq(wrapped_down, 0)
	assert_eq(picked[0], 0)


func test_dialogue_box_choose_starts_at_the_top_every_time() -> void:
	# Arrange
	var box := _box()
	var picked := [-1]
	var first := func() -> void:
		picked[0] = await box.choose(["A", "B"])
	first.call()
	box.press("move_down")
	box.press("interact")
	# Act
	var second := func() -> void:
		picked[0] = await box.choose(["C", "D"])
	second.call()
	# Assert
	assert_eq(box.cursor, 0)
	box.press("interact")
	assert_eq(picked[0], 0)


func test_dialogue_box_press_with_nothing_open_does_nothing() -> void:
	# Arrange
	var box := _box()
	# Act
	box.press("interact")
	box.press("move_down")
	# Assert
	assert_eq(box.mode, "")
	assert_eq(box.cursor, 0)


func test_dialogue_box_beat_finishes_at_beat_scale() -> void:
	# Arrange
	var box := _box()
	var done := [false]
	var run := func() -> void:
		await box.beat()
		done[0] = true
	# Act
	run.call()
	await wait_seconds(0.2)
	# Assert
	assert_true(done[0], "a 0.6 s beat at scale 0.01 is over within 0.2 s")


func test_dialogue_box_beat_outside_the_tree_returns_at_once() -> void:
	# Arrange
	var box: DialogueBox = autofree(DialogueBox.new())
	var done := [false]
	var run := func() -> void:
		await box.beat()
		done[0] = true
	# Act
	run.call()
	# Assert
	assert_true(done[0])


func test_dialogue_box_close_clears_the_mode() -> void:
	# Arrange
	var box := _box()
	var run := func() -> void:
		await box.say("Grandpa", "Bros.")
	run.call()
	# Act
	box.close()
	# Assert
	assert_eq(box.mode, "")
