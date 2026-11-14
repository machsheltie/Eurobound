extends GutTest
## Writers' Room final lines (WritingRoom/tasks/20261112_1419_absinthe_arcade_completion_lines/final.md,
## approved Desk Eurobound-3ho-q4) wired into the maintenance closet props, the Wisp and Dr. Vaněk.


class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "hp": 45, "max_hp": 45, "bravado": 12,
		 "max_bravado": 12, "offense": 8, "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3,
		 "skills": []},
		{"id": "chadwick", "display_name": "Chadwick", "hp": 35, "max_hp": 35, "bravado": 12,
		 "max_bravado": 12, "offense": 6, "defense": 3, "speed": 7, "charm": 10, "luck": 4, "grit": 2,
		 "skills": []},
	]

	func spend_sovs(amount: int) -> bool:
		if sovs < amount:
			return false
		sovs -= amount
		return true

	func add_item(id: String, count: int = 1, _max_stack: Variant = null) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


class FakeStage:
	extends Node
	var dialogue: DialogueBox
	var state


func _toured(opener := true, sovs := 50) -> FakeState:
	var s := FakeState.new()
	BreweryPassport.start_tour(s)
	if opener:
		BreweryPassport.award_opener(s, VanekTaproom.BREWERY_ID)
	s.sovs = sovs
	return s


func _stamped() -> FakeState:
	var s := _toured()
	s.flags[TaproomMaze.FLAG_COMPLETED] = true
	s.flags[TaproomBattle.FLAG_WISP_DEFEATED] = true
	s.flags[VanekTaproom.FLAG_LAGER_BOUGHT] = true
	VanekTaproom.try_stamp(s)
	return s


func _stage(state) -> FakeStage:
	var stage := FakeStage.new()
	stage.state = state
	stage.dialogue = DialogueBox.new()
	stage.dialogue.beat_scale = 0.01
	stage.add_child(stage.dialogue)
	add_child_autofree(stage)
	return stage


## Presses through say boxes and picks the first option until `done[0]`; returns every line said.
func _drive(stage: FakeStage, done: Array) -> Array:
	var said := []
	for i in 300:
		if done[0]:
			break
		if stage.dialogue.mode == "say":
			said.append(stage.dialogue.text)
			stage.dialogue.press("interact")
		elif stage.dialogue.mode == "choose":
			stage.dialogue.cursor = stage.dialogue.options.size() - 1  # Leave
			stage.dialogue.press("interact")
		await wait_process_frames(1)
	return said


func _talk(state) -> Array:
	var stage := _stage(state)
	var done := [false]
	var run := func() -> void:
		await VanekTalk.talk(stage)
		done[0] = true
	run.call()
	return await _drive(stage, done)


# --- closet props -------------------------------------------------------------------------------

func test_closet_props_ddr_toilet_examines_then_plays_the_use_exchange() -> void:
	var s := FakeState.new()
	var first := ClosetProps.lines_for(s, ClosetProps.DDR_TOILET, 0)
	var again := ClosetProps.lines_for(s, ClosetProps.DDR_TOILET, 1)
	assert_eq(first[0]["line"], "A DDR dance pad bolted over a toilet bowl. Sticky, but it still registers your weight as a PERFECT.")
	assert_eq(again.size(), 2)
	assert_eq(again[0], {"who": "Bradley", "line": "Bro, it's got combo scoring. I'm gonna get a full streak."})
	assert_eq(again[1], {"who": "Chadwick", "line": "Do the down arrow again. The sound it makes is insane."})


func test_closet_props_crt_mirror_examines_then_cycles_the_three_readouts() -> void:
	var s := FakeState.new()
	var seen := []
	for i in 5:
		seen.append(ClosetProps.lines_for(s, ClosetProps.CRT_MIRROR, i)[0]["line"])
	assert_eq(seen, [
		"The mirror is a dead arcade screen. INSERT COIN scrolls across your reflection on a loop, forever.",
		"GAME OVER — YOUR DIGNITY HAS EXPIRED",
		"HI-SCORE TABLE — 1ST: YOU — 0 PTS — RANK: TOURIST",
		"PLEASE INSERT FACE",
		"GAME OVER — YOUR DIGNITY HAS EXPIRED"])


func test_closet_props_sock_chute_examines_then_drops_a_sock() -> void:
	var s := FakeState.new()
	assert_eq(ClosetProps.lines_for(s, ClosetProps.SOCK_CHUTE, 0)[0]["line"],
		"The paper-towel dispenser is a claw-machine prize chute. It only dispenses other men's socks. Used.")
	assert_eq(ClosetProps.lines_for(s, ClosetProps.SOCK_CHUTE, 1)[0]["line"],
		"It thunk-clunks and drops a single sock, damp, with a foreign gym logo. There is no way to dry your hands. There never was.")


func test_closet_props_wiring_and_plain_graffiti_read_outs_are_exact() -> void:
	var s := FakeState.new()
	assert_eq(ClosetProps.lines_for(s, ClosetProps.SPARKING_WIRING, 0)[0]["line"],
		"Exposed wiring snakes across the wall and spits a spark when you lean in. The fire code here is a rumor.")
	assert_eq(ClosetProps.lines_for(s, ClosetProps.GRAFFITI_SMAAAASH, 0)[0]["line"],
		"Highlighter ink, under the blacklight. Whoever wrote it meant every word.")
	assert_eq(ClosetProps.lines_for(s, ClosetProps.GRAFFITI_CHEAT_CODES, 0)[0]["line"],
		"A wall of cheat codes. Half are fake. Half of the fake ones are for games that don't exist. One is just a threat.")
	assert_eq(ClosetProps.lines_for(s, ClosetProps.GRAFFITI_BOOBS, 0)[0]["line"],
		"Crude pixel-art boobs, rendered with the confidence of a man who had exactly four colors and one idea.")


func test_closet_props_haiku_is_the_approved_poem_then_its_readout() -> void:
	var rows := ClosetProps.lines_for(FakeState.new(), ClosetProps.GRAFFITI_HAIKU, 0)
	assert_eq(rows[0]["line"], "She said \"PERFECT\" twice.\nwhen the combo was over\nshe meant the combo")
	assert_eq(rows[1]["line"], "Highlighter ink. Underlined twice.")


func test_closet_props_joystick_with_lips_needs_the_embarrassed_status() -> void:
	var s := FakeState.new()
	assert_eq(ClosetProps.lines_for(s, ClosetProps.GRAFFITI_JOYSTICK, 0), [])
	FieldStatus.apply_embarrassed(s, "lord_pilsner", FieldStatus.EMB_SOURCE_CLOSET_TIMER)
	var rows := ClosetProps.lines_for(s, ClosetProps.GRAFFITI_JOYSTICK, 0)
	assert_eq(rows[0]["line"], "A pixel joystick with lips, glowing faintly. It only shows itself to the already-humiliated. Of course.")


func test_closet_props_shame_timer_fires_every_30s_and_cycles_the_three_lines() -> void:
	var p := ClosetProps.new()
	assert_eq(p.tick_shame(29.9), "")
	var lines := [p.tick_shame(0.2)]
	for i in 3:
		lines.append(p.tick_shame(30.0))
	assert_eq(lines, [
		"You've achieved nothing but shame, player one.",
		"Still here. New personal best. Your mother is so proud, player one.",
		"Achievement unlocked: Loiterer.",
		"You've achieved nothing but shame, player one."])


func test_closet_props_every_prop_id_has_an_interaction_point_in_the_room() -> void:
	var room = load("res://worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.gd")
	for id: String in ClosetProps.IDS:
		assert_true(room.INTERACT_POINTS.has(id), id)


# --- Wisp ---------------------------------------------------------------------------------------

func test_taproom_wisp_phase_three_drop_says_her_approved_line() -> void:
	var data := TaproomBattle.fight_data(TaproomBattle.WISP)
	var rng := RandomNumberGenerator.new()
	rng.seed = 3
	var core := TaproomBattle.build_wisp(FakeState.new(), rng)
	var w: BattleUnit = core.enemies[0]
	w.hp = 47
	core._check_phase(w)
	w.hp = 23
	core.events.clear()
	core._check_phase(w)
	assert_eq(w.phase, 3)
	var t := core.events.map(func(ev: Dictionary) -> String: return String(ev["text"]))
	var said := t.filter(func(s: String) -> bool: return s.ends_with(": \"I've decided which version of you is real.\""))
	assert_eq(said.size(), 1, str(t))
	assert_true(String(said[0]).begins_with("Green Fairy Wisp"))
	assert_false(data.is_empty(), "the Wisp fight exists in the taproom config")
	# Phases live on the enemy's own data (debaucheryville_arcade_battle.json), not on the fight entry.
	var p3: Array = Array(w.data.get("phases", [])).filter(func(p: Dictionary) -> bool: return int(p.get("phase", 0)) == 3)
	assert_eq(p3.size(), 1, "the Wisp has exactly one phase-3 entry")
	assert_eq(String(p3[0].get("bark", "")) if p3.size() == 1 else "", "I've decided which version of you is real.")


func test_taproom_wisp_exit_line_comes_before_she_leaves() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 3
	var core := TaproomBattle.build_wisp(FakeState.new(), rng)
	core.round_number = 6
	core.events.clear()
	core._new_round()
	var t := core.events.map(func(ev: Dictionary) -> String: return String(ev["text"]))
	assert_eq(core.outcome, "survived")
	assert_eq(t.size(), 2, str(t))
	assert_eq(t[0], "Green Fairy Wisp: \"You may tell people you won. Nobody will check.\"")
	assert_eq(t[1], "Green Fairy Wisp leaves.")


# --- Vaněk --------------------------------------------------------------------------------------

func test_vanek_taproom_both_openers_line_drops_either_way() -> void:
	assert_eq(VanekTaproom.LINE_BOTH_OPENERS,
		"The cracked glass. You've navigated the mirrors. You've committed. The Absinthe Lager awaits. Prepare for... introspection.")


func test_vanek_taproom_keychain_without_opener_says_the_opener_check_line() -> void:
	var s := _toured(false)
	s.flags[VanekTaproom.FLAG_OPENER_BACKFILLED] = true
	var said := await _talk(s)
	assert_eq(said, ["You have the keychain. Good. The opener is earned, never sold. Complete my maze. Then we discuss stamps and signature brews."])


func test_vanek_taproom_cannot_afford_says_the_approved_line() -> void:
	var s := _toured(true, 0)
	var stage := _stage(s)
	var done := [false]
	var run := func() -> void:
		await VanekTalk._sell(stage.dialogue, s)
		done[0] = true
	run.call()
	var said := await _drive(stage, done)
	assert_eq(said, ["The lager is twelve SOVS. You have less. The maze is free. Come back when you are richer, or more interesting."])


func test_vanek_taproom_callbacks_cycle_in_order_and_wrap() -> void:
	var s := _stamped()
	var got := []
	for i in 7:
		got.append(VanekTaproom.next_callback(s))
	assert_eq(got.slice(0, 6), VanekTaproom.LINES_CALLBACK)
	assert_eq(got[6], VanekTaproom.LINES_CALLBACK[0])
	assert_eq(VanekTaproom.LINES_CALLBACK[0], "You're stamped. The stamp doesn't expire. Neither does the memory. I checked both.")
	assert_eq(VanekTaproom.LINES_CALLBACK[5], "Nothing further is required of you here. That has never once stopped a subject.")


func test_vanek_taproom_callbacks_restart_at_the_next_morning() -> void:
	var s := _stamped()
	GameClock.set_time(s, GameClock.DAY * 2 + 20 * 60)
	VanekTaproom.next_callback(s)
	assert_eq(VanekTaproom.next_callback(s), VanekTaproom.LINES_CALLBACK[1])
	GameClock.set_time(s, GameClock.DAY * 2 + 23 * 60)  # same morning, later
	assert_eq(VanekTaproom.next_callback(s), VanekTaproom.LINES_CALLBACK[2])
	GameClock.set_time(s, GameClock.DAY * 3 + 5 * 60)  # before 06:00: still the same morning
	assert_eq(VanekTaproom.next_callback(s), VanekTaproom.LINES_CALLBACK[3])
	GameClock.set_time(s, GameClock.DAY * 3 + 7 * 60)  # next morning
	assert_eq(VanekTaproom.next_callback(s), VanekTaproom.LINES_CALLBACK[0])


func test_vanek_taproom_callbacks_are_silent_before_the_stamp() -> void:
	assert_eq(VanekTaproom.next_callback(_toured()), "")


func test_vanek_taproom_stamped_return_visit_opens_with_a_callback() -> void:
	var s := _stamped()
	s.flags[VanekTaproom.FLAG_GREETED] = true
	var said := await _talk(s)
	assert_eq(said[0], VanekTaproom.LINES_CALLBACK[0])
