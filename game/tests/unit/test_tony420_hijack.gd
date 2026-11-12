extends GutTest
## Tony420's FREE Wi-Fi hijack (Writers' Room desk 2026-11-11; NEXT_WORK.md "Tony420 / FREE Wi-Fi
## hijack"): the first ICQ hijack sets tony420_unlocked, the Meme Black Market trade reads that flag
## plus the rare-memes check, and the Kavarna chair holds an hourly patron until the Döner Debate.

const INTERACTIONS := "res://assets/data/locations/debaucheryville/debaucheryville_interactions.json"

class FakeState:
	var flags := {}

class FakeStage:
	extends Node
	var dialogue: DialogueBox
	var state
	var cues := []

	func cue(id: String) -> void:
		cues.append(id)


func _stage() -> FakeStage:
	var stage := FakeStage.new()
	stage.state = FakeState.new()
	stage.dialogue = DialogueBox.new()
	stage.dialogue.beat_scale = 0.01
	stage.add_child(stage.dialogue)
	add_child_autofree(stage)
	return stage


## Presses through the box until `done` is true; returns every line said.
func _drive(stage: FakeStage, done: Array) -> Array:
	var said := []
	for i in 200:
		if done[0]:
			break
		if stage.dialogue.mode == "say":
			said.append(stage.dialogue.text)
			stage.dialogue.press("interact")
		await wait_process_frames(1)
	return said


func test_tony420_hijack_first_hijack_sets_tony420_unlocked() -> void:
	# Arrange
	var s := FakeState.new()
	# Act
	var first := Tony420Hijack.mark_hijacked(s)
	var second := Tony420Hijack.mark_hijacked(s)
	# Assert
	assert_true(first, "the first hijack is the unlocking one")
	assert_false(second, "later hijacks unlock nothing new")
	assert_true(s.flags.get("tony420_unlocked", false))
	assert_true(Tony420Hijack.unlocked(s))


func test_tony420_hijack_flag_name_is_the_ruled_one() -> void:
	# Arrange / Act: the ledger names the flag; the Meme Black Market data reads it by that name
	var flag := Tony420Hijack.UNLOCK_FLAG
	# Assert
	assert_eq(flag, "tony420_unlocked")


func test_tony420_hijack_opens_with_the_canon_greeting() -> void:
	# Arrange
	var lines := Tony420Hijack.spoken_lines()
	# Assert: npc_tony420.md Approach/Greeting (darkwebdossiercrossoverevents.md:84), verbatim
	assert_gt(lines.size(), 1)
	assert_eq(lines[0], {"who": "TONY420", "line": "yo"})
	assert_eq(lines[1], {"who": "TONY420", "line": "u up?"})


func test_tony420_hijack_unwritten_lines_are_marked_pending() -> void:
	# Every line past the canon greeting is the author's to write: it must say so on its face.
	var lines := Tony420Hijack.spoken_lines()
	for i in range(2, lines.size()):
		var line: String = lines[i]["line"]
		assert_true(line.begins_with("[TONY420_HIJACK_") and line.contains("pending author"), line)
	assert_true(Tony420Hijack.pending(), "the script still waits on the author")


func test_tony420_hijack_play_runs_the_script_and_sets_the_flag() -> void:
	# Arrange
	var stage := _stage()
	var done := [false]
	var result := [null]
	var run := func() -> void:
		result[0] = await Tony420Hijack.play(stage)
		done[0] = true
	# Act
	run.call()
	var said := await _drive(stage, done)
	# Assert
	assert_true(done[0], "the hijack finished")
	assert_eq(result[0], true, "first hijack")
	assert_eq(said.slice(0, 2), ["yo", "u up?"])
	assert_eq(said.size(), Tony420Hijack.spoken_lines().size())
	assert_eq(stage.cues, ["icq_uh_oh"], "the ICQ Uh-oh! plays before Tony speaks")
	assert_true(Tony420Hijack.unlocked(stage.state))
	assert_eq(stage.dialogue.mode, "")


func test_tony420_hijack_second_play_is_not_the_first() -> void:
	# Arrange
	var stage := _stage()
	stage.state.flags["tony420_unlocked"] = true
	var done := [false]
	var result := [null]
	var run := func() -> void:
		result[0] = await Tony420Hijack.play(stage)
		done[0] = true
	# Act
	run.call()
	await _drive(stage, done)
	# Assert
	assert_eq(result[0], false)
	assert_true(Tony420Hijack.unlocked(stage.state))


func test_tony420_hijack_meme_trade_needs_flag_and_rare_memes() -> void:
	# Arrange
	var s := FakeState.new()
	# Act / Assert
	assert_false(Tony420Hijack.meme_trade_open(s, true), "no hijack yet")
	s.flags["tony420_unlocked"] = true
	assert_false(Tony420Hijack.meme_trade_open(s, false), "no rare memes")
	assert_true(Tony420Hijack.meme_trade_open(s, true))


func test_tony420_hijack_meme_black_market_condition_reads_the_flag() -> void:
	# Arrange
	var doc: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(INTERACTIONS))
	var raw := FileAccess.get_file_as_string(INTERACTIONS)
	# Act
	var found := []
	_find_key(doc, "tony420_trading", found)
	# Assert
	assert_false(raw.contains("tony420_contact_unlocked_and_rare_memes_acquired"),
		"the old condition string is gone")
	var conditions := found.filter(func(t): return t is Dictionary and t.has("condition"))
	assert_eq(conditions.size(), 1)
	var cond: Dictionary = conditions[0]["condition"]
	assert_eq(cond.get("flag"), "tony420_unlocked")
	assert_eq(cond.get("rare_memes"), conditions[0].get("trade_requirement"),
		"the rare-memes check is the trade's existing requirement")


func _find_key(node, key: String, out: Array) -> void:
	if node is Dictionary:
		for k in node:
			if k == key:
				out.append(node[k])
			_find_key(node[k], key, out)
	elif node is Array:
		for v in node:
			_find_key(v, key, out)


func test_kavarna_chair_holds_an_hourly_patron_before_the_doner_debate() -> void:
	# Arrange
	var s := FakeState.new()
	# Act / Assert
	assert_eq(KavarnaChair.occupant(s), "hourly_patron")
	s.flags[KavarnaChair.DONER_DEBATE_DONE] = true
	assert_eq(KavarnaChair.occupant(s), "goon_tablet")


func test_kavarna_chair_patron_changes_every_night() -> void:
	# Arrange
	var s := FakeState.new()
	var roster := ["a", "b", "c"]
	# Act
	var nights := []
	for day in 4:
		GameClock.set_time(s, day * GameClock.DAY + 21 * 60)
		nights.append(KavarnaChair.patron_for_night(s, roster))
	# Assert
	for i in range(1, nights.size()):
		assert_ne(nights[i], nights[i - 1], "night %d" % i)
	assert_eq(KavarnaChair.patron_for_night(s, []), "")
