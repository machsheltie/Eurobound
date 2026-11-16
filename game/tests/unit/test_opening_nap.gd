extends GutTest
## OpeningNap: story opening step 1, Scene 8 (design/narrative/opening_step1.md). The NAP / DON'T NAP
## prompt at the hotel bed; both choices nap (author, Desk Eurobound-3ho-q11).


## Records every line and answers the prompt with a fixed pick, without waiting for presses.
class RecordingBox:
	extends DialogueBox
	var said: Array = []
	var prompts: Array = []
	var pick := 0
	var beats := 0
	var closed := false

	func say(who: String, line: String) -> void:
		said.append([who, line])

	func choose(choices: Array) -> int:
		prompts.append(choices.duplicate())
		said.append(["<prompt>", ""])
		return pick

	func beat(_seconds: float = BEAT_S) -> void:
		beats += 1

	func close() -> void:
		closed = true


func _recording(pick: int) -> RecordingBox:
	var box := RecordingBox.new()
	box.pick = pick
	add_child_autofree(box)
	return box


func _lines_after_prompt(box: RecordingBox) -> Array:
	var at := box.said.find(["<prompt>", ""])
	return box.said.slice(at + 1)


func test_opening_nap_prompt_offers_nap_and_dont_nap() -> void:
	# Arrange
	var box := _recording(OpeningNap.CHOICE_NAP)
	# Act
	await OpeningNap.play(box)
	# Assert
	assert_eq(box.prompts, [["NAP", "DON'T NAP"]])


func test_opening_nap_lines_before_the_prompt_match_the_scene() -> void:
	# Arrange
	var box := _recording(OpeningNap.CHOICE_NAP)
	# Act
	await OpeningNap.play(box)
	# Assert
	var at := box.said.find(["<prompt>", ""])
	assert_eq(box.said.slice(0, at), [
		["BRADLEY", "Just a nap. Twenty minutes. Tactical. It's what athletes do."],
		["PILSNER", "We are NOT napping. We are in EUROMEMEIA. There are women out there who have never met an American with a paddle."],
		["PILSNER", "...Twenty minutes. Then we go out. Twenty minutes."],
	])


func test_opening_nap_nap_choice_naps_and_wakes_for_the_night() -> void:
	# Arrange
	var box := _recording(OpeningNap.CHOICE_NAP)
	# Act
	var napped: bool = await OpeningNap.play(box)
	# Assert
	assert_true(napped)
	assert_eq(_lines_after_prompt(box), _wake_lines(), "NAP goes straight to the nap")
	assert_true(box.closed)


func test_opening_nap_dont_nap_choice_also_naps_and_wakes_for_the_night() -> void:
	# Arrange
	var box := _recording(OpeningNap.CHOICE_DONT_NAP)
	# Act
	var napped: bool = await OpeningNap.play(box)
	# Assert
	assert_true(napped, "DON'T NAP naps too")
	var after := _lines_after_prompt(box)
	var pretend: Array = OpeningNap.LINES_DONT_NAP_PRETEND
	assert_eq(after.slice(0, pretend.size()), pretend, "DON'T NAP plays its pretend lines first")
	assert_eq(after.slice(pretend.size()), _wake_lines())
	assert_true(box.closed)


func test_opening_nap_nap_cut_runs_between_prompt_and_waking() -> void:
	# Arrange
	var box := _recording(OpeningNap.CHOICE_DONT_NAP)
	var cut_at := [-1]
	var cut := func() -> void:
		cut_at[0] = box.said.size()
	# Act
	await OpeningNap.play(box, cut)
	# Assert
	var wake_at := box.said.find(_wake_lines()[0])
	assert_eq(cut_at[0], wake_at, "the screen dims after the prompt and before PILSNER wakes")


func test_opening_nap_real_box_shows_the_prompt_and_both_picks_finish() -> void:
	for pick in [OpeningNap.CHOICE_NAP, OpeningNap.CHOICE_DONT_NAP]:
		# Arrange
		var box := DialogueBox.new()
		box.beat_scale = 0.001
		add_child_autofree(box)
		var done := [false]
		var run := func() -> void:
			await OpeningNap.play(box)
			done[0] = true
		# Act
		run.call()
		var seen_options: Array = []
		for _i in 60:
			if done[0]:
				break
			if box.mode == "choose":
				seen_options = box.options.duplicate()
				if pick == OpeningNap.CHOICE_DONT_NAP:
					box.press("move_down")
				box.press("interact")
			elif box.mode == "say":
				box.press("interact")
			else:
				await wait_process_frames(2)
		# Assert
		assert_eq(seen_options, ["NAP", "DON'T NAP"])
		assert_true(done[0], "pick %d reaches the end of the scene" % pick)
		assert_eq(box.mode, "")


func _wake_lines() -> Array:
	return [
		["PILSNER", "BOYS. It's NIGHT. We slept through the afternoon. We are THREE HOURS BEHIND SCHEDULE."],
		["CHADWICK", "We good. We back. I got the whole nap. Three hours of content."],
		["BRADLEY", "Tactical. I feel incredible. I feel twenty-five."],
		["PILSNER", "Gentlemen. Publandia, Debaucheryville, Sinfonia, Shamsterdam — it all starts tonight. We are going OUT."],
		["PILSNER", "...I should call Mommy."],
	]
