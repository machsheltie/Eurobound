extends GutTest
## Backpack Girl's one-night stand in the Arcade couchsurf flow (Eurobound-spr0). The scene is the
## approved WritingRoom/tasks/20261112_1518_backpack_girl_one_night_stand/final.md, handed in as
## assets/data/npcs/conversations/debaucheryville_npc_backpack_girl_01.json; States 2 and 4 are in
## design/quests/debaucheryville/couchsurfingchroniclesdebaucheryville.md:148-200 (Desk 3ho-q13,
## 3ho-q14). These tests play the real data file through the real DialogueBox.

const PICK_LINE := "You. Divorce. Four times, you told me. Four times in six minutes."
const APPROACH_LINE := "Oh — hey. Hey. You want the rest of this? I'm serious, take it. I've eaten. Sit down. You look like a story."
const CUTAWAY_LINE := "Two days. I said two days."
const MORNING_LINE := "Don't go anywhere. I'm at the bit where you're tall."
const REFUSAL_LINE := "Thank you for this. Truly. You gave me a *whole second movement*. The room's a no, obviously. But thank you."
const STING_LINE := "Oh, hey! You look better. You look — yeah. Good for you, genuinely."
const CLOSING_LINE := "You understand this doesn't retire the old verses. Nothing retires. That's not a threat, that's just — that's how an archive works. Thank you for coming back. Genuinely. You're the gift that keeps on being a *song*."
const LAST_RATIONALISATION := "After the show. Obviously after the show."
const INFECTED_RATIONALISATION := "'Subject of an original Euromemeian folk composition.' I'm putting the whole chorus in my bio."


class FakeState:
	var sovs := 20
	var inventory := {}
	var flags := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "bravado": 30, "max_bravado": 30},
		{"id": "chadwick", "display_name": "Chadwick", "bravado": 25, "max_bravado": 25},
		{"id": "bradley", "display_name": "Bradley", "bravado": 5, "max_bravado": 20},
	]

	func add_item(id: String, count: int = 1, _max_stack: Variant = null) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _state(herp := false, refused := false) -> FakeState:
	var s := FakeState.new()
	GameClock.set_time(s, 21 * 60)  # 21:00 on day 0, inside her 14:00-22:00 floor spot
	if herp:
		for m: Dictionary in s.party:
			FieldStatus.apply_until_cured(s, String(m["id"]), "the_herp")
	if refused:
		s.flags[BackpackGirlCouchsurf.FLAG_REFUSED] = true
	return s


func _conversation() -> Dictionary:
	var read := NpcConversation.read_file(NpcConversation.path_for(BackpackGirlCouchsurf.NPC_ID))
	assert_eq(read["problems"], [], "the hand-in file reads clean")
	return read["conversation"]


## Plays the scene, pressing through every box; returns {"said": [[speaker, line]], "clock": {line: minutes}}.
func _play(state: FakeState, coin_equipped := false) -> Dictionary:
	var box := DialogueBox.new()
	box.beat_scale = 0.01
	add_child_autofree(box)
	var flow := BackpackGirlCouchsurf.new()
	var done := [false]
	var run := func() -> void:
		await flow.play(_conversation(), box, state, coin_equipped)
		done[0] = true
	run.call()
	var said := []
	var clock := {}
	for i in 600:
		if done[0]:
			break
		if box.mode == "say":
			said.append([box.speaker, box.text])
			clock[box.text] = GameClock.minutes(state)
			box.press("interact")
		elif box.mode == "choose":
			box.press("interact")
		await wait_process_frames(1)
	assert_true(done[0], "the scene ran to its end")
	assert_eq(flow.errors, [], "no walker errors")
	return {"said": said, "clock": clock, "flow": flow}


func _lines(result: Dictionary) -> Array:
	return result["said"].map(func(row: Array) -> String: return row[1])


# --- routing ------------------------------------------------------------------------------------

func test_backpack_girl_couchsurf_state_1_when_the_party_never_caught_the_herp() -> void:
	assert_eq(BackpackGirlCouchsurf.state_for(_state(), false), 1)
	assert_eq(BackpackGirlCouchsurf.state_for(_state(), true), 1, "no Herp: the Coin changes nothing")


func test_backpack_girl_couchsurf_state_2_when_infected_without_the_coin() -> void:
	assert_eq(BackpackGirlCouchsurf.state_for(_state(true), false), 2)
	assert_eq(BackpackGirlCouchsurf.state_for(_state(true, true), false), 2, "refused before: still refused")


func test_backpack_girl_couchsurf_state_3_when_the_coin_is_on_and_she_never_refused() -> void:
	assert_eq(BackpackGirlCouchsurf.state_for(_state(true), true), 3)


func test_backpack_girl_couchsurf_state_4_when_the_coin_is_on_and_she_refused_before() -> void:
	assert_eq(BackpackGirlCouchsurf.state_for(_state(true, true), true), 4)


# --- the four states played ---------------------------------------------------------------------

func test_backpack_girl_couchsurf_state_1_plays_pick_cutaway_morning_and_pays() -> void:
	var s := _state()
	var r := await _play(s)
	var lines := _lines(r)
	assert_eq(lines[0], APPROACH_LINE, "opens on the kebab offer")
	assert_eq(r["said"][0][0], "Backpack Girl")
	assert_has(lines, PICK_LINE)
	assert_has(lines, CUTAWAY_LINE)
	assert_has(lines, MORNING_LINE)
	assert_eq(lines[-1], LAST_RATIONALISATION, "ends on the rationalisations")
	assert_does_not_have(lines, STING_LINE)
	assert_does_not_have(lines, REFUSAL_LINE)
	assert_does_not_have(lines, CLOSING_LINE)
	assert_eq(r["flow"].played_state, 1)
	assert_eq(int(s.inventory.get(BackpackGirlCouchsurf.BALLAD_ID, 0)), 1, "Ballad of the Bros")
	assert_eq(s.party.map(func(m: Dictionary) -> int: return int(m["bravado"])), [20, 15, 0],
		"-10 Bravado, never below zero")
	assert_true(bool(s.flags.get(BackpackGirlCouchsurf.FLAG_COMPLETED, false)))
	assert_false(bool(s.flags.get(BackpackGirlCouchsurf.FLAG_REFUSED, false)))
	assert_eq(s.sovs, 20, "no SOVS change hands")


func test_backpack_girl_couchsurf_state_2_skips_the_pick_and_refuses_the_party() -> void:
	var s := _state(true)
	var r := await _play(s)
	var lines := _lines(r)
	assert_eq(lines[0], APPROACH_LINE, "the approach and offer still play")
	assert_has(lines, "My roommates run a book on how long guests stay. You're all in it. It's not personal, it's *data*.")
	assert_does_not_have(lines, PICK_LINE, "the pick beat is skipped (Desk 3ho-q14)")
	assert_does_not_have(lines, CUTAWAY_LINE)
	assert_does_not_have(lines, MORNING_LINE)
	assert_has(lines, REFUSAL_LINE)
	assert_eq(lines[-1], INFECTED_RATIONALISATION)
	assert_eq(r["flow"].played_state, 2)
	assert_true(bool(s.flags.get(BackpackGirlCouchsurf.FLAG_REFUSED, false)), "sets the refusal flag")
	assert_false(bool(s.flags.get(BackpackGirlCouchsurf.FLAG_COMPLETED, false)), "no payload")
	assert_eq(int(s.inventory.get(BackpackGirlCouchsurf.BALLAD_ID, 0)), 0)
	assert_eq(s.party.map(func(m: Dictionary) -> int: return int(m["bravado"])), [30, 25, 5])
	assert_eq(GameClock.minutes(s), 21 * 60, "no night passes")


func test_backpack_girl_couchsurf_state_3_plays_exactly_as_state_1() -> void:
	var clear := await _play(_state())
	var s := _state(true)
	var r := await _play(s, true)
	assert_eq(r["said"], clear["said"], "no callback, no reference")
	assert_eq(r["flow"].played_state, 3)
	assert_eq(int(s.inventory.get(BackpackGirlCouchsurf.BALLAD_ID, 0)), 1)
	assert_eq(s.party.map(func(m: Dictionary) -> int: return int(m["bravado"])), [20, 15, 0])


func test_backpack_girl_couchsurf_state_4_stings_then_resolves_normally() -> void:
	var s := _state(true, true)
	var r := await _play(s, true)
	var lines := _lines(r)
	assert_eq(lines[0], STING_LINE, "the sting comes first")
	assert_has(lines, "—no, okay, no, come on. COME ON. You went to *Sinfonia*. For a *coin*. That's a whole third movement and I'm not going to sit here and pretend I don't want it.")
	assert_has(lines, APPROACH_LINE)
	assert_has(lines, PICK_LINE)
	assert_has(lines, CUTAWAY_LINE)
	assert_has(lines, CLOSING_LINE)
	assert_does_not_have(lines, REFUSAL_LINE, "never a second refusal")
	assert_eq(r["flow"].played_state, 4)
	assert_eq(int(s.inventory.get(BackpackGirlCouchsurf.BALLAD_ID, 0)), 1)
	assert_true(bool(s.flags.get(BackpackGirlCouchsurf.FLAG_COMPLETED, false)))


# --- payload and clock --------------------------------------------------------------------------

func test_backpack_girl_couchsurf_payload_applies_once() -> void:
	var s := _state()
	await _play(s)
	await _play(s)
	assert_eq(int(s.inventory.get(BackpackGirlCouchsurf.BALLAD_ID, 0)), 1, "one Ballad")
	assert_eq(s.party.map(func(m: Dictionary) -> int: return int(m["bravado"])), [20, 15, 0], "one -10")


func test_backpack_girl_couchsurf_cutaway_at_0240_and_morning_at_0740() -> void:
	var s := _state()
	var r := await _play(s)
	assert_eq(r["clock"][APPROACH_LINE], 21 * 60, "the approach is now")
	assert_eq(r["clock"][CUTAWAY_LINE], GameClock.DAY + 2 * 60 + 40, "02:40 that night")
	assert_eq(r["clock"][MORNING_LINE], GameClock.DAY + 7 * 60 + 40, "07:40 the next morning")
	assert_eq(GameClock.watch_text(s), "07:40")


func test_backpack_girl_couchsurf_ring_is_a_story_beat_only() -> void:
	var s := _state()
	await _play(s)
	assert_eq(s.inventory.keys(), [BackpackGirlCouchsurf.BALLAD_ID], "the Ballad is the only item")
	for key: String in s.flags.keys():
		assert_false(key.contains("ring"), "no ring flag: " + key)


# --- the Arcade hall ----------------------------------------------------------------------------

func test_backpack_girl_couchsurf_data_repo_reads_the_hand_in_file() -> void:
	var conv := DataRepo.get_dialogue_tree(BackpackGirlCouchsurf.NPC_ID)
	assert_eq(conv.get("npc_id", ""), BackpackGirlCouchsurf.NPC_ID)
	for seg: String in ["approach", "pick", "goes", "cutaway", "morning", "rationalisations",
			"s2_refusal", "s4_sting", "s4_closing"]:
		assert_true(conv["nodes"].has(seg), "segment " + seg)


func test_backpack_girl_couchsurf_hall_hook_opens_her_scene() -> void:
	# Arrange: the real hall, as test_arcade_hall_play sets it up.
	var saved := {"flags": GameState.flags.duplicate(true), "party": GameState.party.duplicate(true),
		"inventory": GameState.inventory.duplicate(true), "sovs": GameState.sovs}
	SceneRouter.ensure_game_started(get_tree())
	GameState.flags[ArcadeHallLines.FIRST_ENTRY_FLAG] = true
	var hall: Node3D = load("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn").instantiate()
	add_child_autofree(hall)
	await wait_physics_frames(3)
	# Act
	hall._on_interacted(BackpackGirlCouchsurf.INTERACT_ID)
	await wait_process_frames(1)
	# Assert
	assert_eq([hall.dialogue.speaker, hall.dialogue.text], ["Backpack Girl", APPROACH_LINE])
	assert_true(hall._player.input_locked, "the player is held for the scene")
	GameState.flags = saved["flags"]
	GameState.party = saved["party"]
	GameState.inventory = saved["inventory"]
	GameState.sovs = saved["sovs"]
	SceneRouter.pending_spawn = ""
