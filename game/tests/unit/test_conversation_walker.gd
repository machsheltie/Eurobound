extends GutTest
## ConversationWalker: plays an NpcConversation through DialogueBox (Eurobound-r1qf). Fixture
## strings only, never game content.

const FIXTURE := "res://tests/fixtures/conversations/fixture_npc.json"

var _ended: Array = []


func _conv(doc: Dictionary = {}) -> Dictionary:
	if doc.is_empty():
		return NpcConversation.read_file(FIXTURE)["conversation"]
	return NpcConversation.read_doc(doc)["conversation"]


func _box() -> DialogueBox:
	var box := DialogueBox.new()
	add_child_autofree(box)
	return box


func _state() -> Dictionary:
	return {"flags": {}}


func _walker() -> ConversationWalker:
	var w := ConversationWalker.new()
	_ended = []
	w.finished.connect(func(npc_id: String) -> void: _ended.append(npc_id))
	return w


func test_conversation_walker_plays_lines_one_box_each_then_offers_choices() -> void:
	var box := _box()
	var w := _walker()
	w.play(_conv(), box, _state())
	assert_eq([box.speaker, box.text], ["FIXTURE SPEAKER", "FIXTURE LINE ONE"])
	box.press("interact")
	assert_eq(box.text, "FIXTURE LINE TWO")
	box.press("interact")
	assert_eq(box.mode, "choose", "the greet node ends in choices")
	assert_eq(box.options, ["FIXTURE ASK"])


func test_conversation_walker_requires_flag_shows_a_choice() -> void:
	var box := _box()
	var state := _state()
	state["flags"]["fixture_gate"] = true
	var w := _walker()
	w.play(_conv(), box, state)
	box.press("interact")
	box.press("interact")
	assert_eq(box.options, ["FIXTURE ASK", "FIXTURE GATED"])


func test_conversation_walker_blocks_flag_hides_a_choice() -> void:
	var box := _box()
	var state := _state()
	state["flags"]["fixture_gate"] = true
	state["flags"]["fixture_block"] = true
	var w := _walker()
	w.play(_conv(), box, state)
	box.press("interact")
	box.press("interact")
	assert_eq(box.options, ["FIXTURE ASK"])


func test_conversation_walker_choice_applies_set_flags_and_follows_next() -> void:
	var box := _box()
	var state := _state()
	var w := _walker()
	w.play(_conv(), box, state)
	box.press("interact")
	box.press("interact")
	box.press("interact")  # pick the only visible choice
	assert_true(state["flags"].get("fixture_asked", false))
	assert_true(state["flags"].get("fixture_heard_more", false), "node set_flags apply on reaching it")
	assert_eq([box.speaker, box.text], ["FIXTURE OTHER", "FIXTURE MORE"])
	assert_eq(_ended, [])
	box.press("interact")
	assert_eq(box.text, "FIXTURE BYE")
	assert_eq(box.speaker, "FIXTURE SPEAKER", "node speaker overrides only its own node")
	box.press("interact")
	assert_eq(_ended, ["fixture_npc"])
	assert_eq(box.mode, "")


func test_conversation_walker_false_clears_a_flag() -> void:
	var doc := {"npc_id": "t", "start": "a", "nodes": [
		{"id": "a", "lines": ["X"], "set_flags": {"f": false, "g": true}}]}
	var box := _box()
	var state := _state()
	state["flags"]["f"] = true
	var w := _walker()
	w.play(_conv(doc), box, state)
	assert_false(state["flags"].has("f"))
	assert_true(state["flags"]["g"])


func test_conversation_walker_choice_to_empty_next_ends() -> void:
	var box := _box()
	var state := _state()
	state["flags"]["fixture_gate"] = true
	var w := _walker()
	w.play(_conv(), box, state)
	box.press("interact")
	box.press("interact")
	box.cursor = 1
	box.press("interact")
	assert_eq(_ended, ["fixture_npc"])


func test_conversation_walker_bad_next_ends_safely() -> void:
	var conv := _conv({"npc_id": "t", "start": "a", "nodes": [
		{"id": "a", "lines": ["X"], "next": "b"}, {"id": "b", "lines": ["Y"]}]})
	conv["nodes"]["a"]["next"] = "nowhere"
	var box := _box()
	var w := _walker()
	w.play(conv, box, _state())
	box.press("interact")
	assert_eq(_ended, ["t"])
	assert_eq(box.mode, "")
	assert_eq(w.errors.size(), 1)


func test_conversation_walker_empty_conversation_ends_safely() -> void:
	var box := _box()
	var w := _walker()
	w.play({}, box, _state())
	assert_eq(_ended, [""])
	assert_eq(w.errors.size(), 0, "an empty start is just an empty talk")


func test_conversation_walker_all_choices_hidden_ends_safely() -> void:
	var conv := _conv({"npc_id": "t", "start": "a", "nodes": [
		{"id": "a", "lines": ["X"], "choices": [
			{"text": "P", "next": "", "requires_flags": ["no"]},
			{"text": "Q", "next": "", "requires_flags": ["no"]}]}]})
	var box := _box()
	var w := _walker()
	w.play(conv, box, _state())
	box.press("interact")
	assert_eq(_ended, ["t"])
	assert_eq(w.errors.size(), 1)


func test_conversation_walker_endless_loop_is_cut_off() -> void:
	var conv := _conv({"npc_id": "t", "start": "a", "nodes": [
		{"id": "a", "lines": ["X"], "next": "a"}]})
	var box := _box()
	var w := _walker()
	w.max_nodes = 3
	w.play(conv, box, _state())
	for i in 3:
		box.press("interact")
	assert_eq(_ended, ["t"])
	assert_eq(w.errors.size(), 1)
