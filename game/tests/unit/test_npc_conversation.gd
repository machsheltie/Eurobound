extends GutTest
## NpcConversation: reads the NPC conversation hand-in file (Eurobound-04t2). Fixtures are test
## strings in tests/fixtures/conversations/, never game content.

const FIXTURE := "res://tests/fixtures/conversations/fixture_npc.json"


func _read() -> Dictionary:
	return NpcConversation.read_file(FIXTURE)


func _doc(nodes: Array, start: String = "a") -> Dictionary:
	return {"npc_id": "t", "start": start, "nodes": nodes}


func _problems(nodes: Array, start: String = "a") -> Array:
	return NpcConversation.read_doc(_doc(nodes, start))["problems"]


func test_npc_conversation_fixture_loads_without_problems() -> void:
	assert_eq(_read()["problems"], [])


func test_npc_conversation_reads_header_and_start() -> void:
	var c: Dictionary = _read()["conversation"]
	assert_eq(c["npc_id"], "fixture_npc")
	assert_eq(c["speaker"], "FIXTURE SPEAKER")
	assert_eq(c["start"], "greet")
	assert_eq(c["nodes"].keys(), ["greet", "more", "bye"])


func test_npc_conversation_node_lines_are_copied_in_order() -> void:
	var node: Dictionary = _read()["conversation"]["nodes"]["greet"]
	assert_eq(node["lines"], ["FIXTURE LINE ONE", "FIXTURE LINE TWO"])
	assert_eq(node["source"], "fixture")


func test_npc_conversation_choice_carries_next_and_flag_rules() -> void:
	var choices: Array = _read()["conversation"]["nodes"]["greet"]["choices"]
	assert_eq(choices.size(), 2)
	assert_eq(choices[0]["text"], "FIXTURE ASK")
	assert_eq(choices[0]["next"], "more")
	assert_eq(choices[0]["set_flags"], {"fixture_asked": true})
	assert_eq(choices[1]["requires_flags"], ["fixture_gate"])
	assert_eq(choices[1]["blocks_flags"], ["fixture_block"])
	assert_eq(choices[1]["next"], "")


func test_npc_conversation_unknown_fields_land_in_extra() -> void:
	var choices: Array = _read()["conversation"]["nodes"]["greet"]["choices"]
	assert_eq(choices[1]["extra"], {"mood": "FIXTURE EXTRA"})


func test_npc_conversation_node_speaker_override_and_set_flags() -> void:
	var node: Dictionary = _read()["conversation"]["nodes"]["more"]
	assert_eq(node["speaker"], "FIXTURE OTHER")
	assert_eq(node["set_flags"], {"fixture_heard_more": true})
	assert_eq(node["next"], "bye")


func test_npc_conversation_last_node_ends_with_empty_next_and_no_choices() -> void:
	var node: Dictionary = _read()["conversation"]["nodes"]["bye"]
	assert_eq(node["next"], "")
	assert_eq(node["choices"], [])


func test_npc_conversation_path_for_names_the_npc_file() -> void:
	assert_eq(NpcConversation.path_for("x"), "res://assets/data/npcs/conversations/x.json")


func test_npc_conversation_missing_file_is_reported() -> void:
	var r := NpcConversation.read_file("res://tests/fixtures/conversations/nope.json")
	assert_eq(r["conversation"], {})
	assert_eq(r["problems"].size(), 1)


func test_npc_conversation_start_must_be_a_node() -> void:
	assert_eq(_problems([{"id": "a", "lines": ["X"]}], "zzz").size(), 1)


func test_npc_conversation_node_without_lines_is_reported() -> void:
	assert_eq(_problems([{"id": "a", "lines": []}]).size(), 1)


func test_npc_conversation_blank_line_is_reported() -> void:
	assert_eq(_problems([{"id": "a", "lines": ["X", "  "]}]).size(), 1)


func test_npc_conversation_dangling_next_and_choice_are_reported() -> void:
	var nodes := [
		{"id": "a", "lines": ["X"], "choices": [
			{"text": "C1", "next": "gone"}, {"text": "C2", "next": "b"}]},
		{"id": "b", "lines": ["X"], "next": "gone2"},
	]
	assert_eq(_problems(nodes).size(), 2)


func test_npc_conversation_duplicate_id_is_reported() -> void:
	var nodes := [{"id": "a", "lines": ["X"]}, {"id": "a", "lines": ["Y"]}]
	assert_eq(_problems(nodes).size(), 1)


func test_npc_conversation_choices_and_next_together_are_reported() -> void:
	var nodes := [
		{"id": "a", "lines": ["X"], "next": "b",
			"choices": [{"text": "C1", "next": "b"}, {"text": "C2", "next": "b"}]},
		{"id": "b", "lines": ["X"]},
	]
	assert_eq(_problems(nodes).size(), 1)


func test_npc_conversation_single_choice_is_reported() -> void:
	var nodes := [{"id": "a", "lines": ["X"], "choices": [{"text": "C1", "next": ""}]}]
	assert_eq(_problems(nodes).size(), 1)


func test_npc_conversation_choice_without_text_is_reported() -> void:
	var nodes := [{"id": "a", "lines": ["X"], "choices": [{"next": ""}, {"text": "C2"}]}]
	assert_eq(_problems(nodes).size(), 1)


func test_npc_conversation_set_flags_must_be_an_object() -> void:
	assert_eq(_problems([{"id": "a", "lines": ["X"], "set_flags": ["f"]}]).size(), 1)


func test_npc_conversation_missing_npc_id_and_nodes_are_reported() -> void:
	var r := NpcConversation.read_doc({})
	assert_true(r["problems"].size() >= 2)


func test_data_repo_get_dialogue_tree_unknown_npc_is_empty() -> void:
	var repo = autofree(load("res://core/data_repo.gd").new())
	assert_eq(repo.get_dialogue_tree("no_such_npc_fixture"), {})
