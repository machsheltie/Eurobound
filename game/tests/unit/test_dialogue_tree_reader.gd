extends GutTest
## DialogueTreeReader: turns the NPC dialogue-tree JSON (assets/data/npcs/dialogue_trees/) into one
## plain structure any dialogue path can use. It copies text as written, reports what is broken and
## fills nothing in. The fixtures below are test strings, not game lines.

const REAL_FILE := "res://assets/data/npcs/dialogue_trees/debaucheryville_dialogue.json"


func _doc() -> Dictionary:
	return {
		"dialogue_trees": {
			"test_npc": {
				"default_greeting": {
					"line_id": "test_greeting_001",
					"text": "FIXTURE GREETING",
					"speaker": "Test Npc",
					"emotion": "smug",
					"party_specific_overrides": {"bradley_present": {"text": "FIXTURE BRADLEY"}},
					"options": [
						{"text": "FIXTURE ASK", "leads_to": "more", "requires": null,
							"party_reaction": {"Bradley": "FIXTURE REACTION"}},
						{"text": "FIXTURE PAY", "leads_to": "nowhere",
							"requires": {"item": "fixture_item"}},
					],
				},
				"more": {
					"line_id": "test_more_001",
					"text": "FIXTURE MORE",
					"speaker": "Test Npc",
					"set_flags": {"fixture_flag": true},
				},
			},
		},
		"status_reactions": {"hungover": {"test_npc": "FIXTURE HUNGOVER", "other_npc": "X"}},
		"world_state_responses": {"test_npc": {"fixture_state": "FIXTURE STATE"}},
	}


func _tree() -> Dictionary:
	return DialogueTreeReader.read_doc(_doc())["trees"]["test_npc"]


func test_dialogue_tree_reader_read_doc_returns_one_tree_per_npc() -> void:
	var result := DialogueTreeReader.read_doc(_doc())
	assert_eq(result["trees"].keys(), ["test_npc"])
	assert_eq(result["trees"]["test_npc"]["npc_id"], "test_npc")


func test_dialogue_tree_reader_tree_starts_at_default_greeting() -> void:
	assert_eq(_tree()["start"], "default_greeting")


func test_dialogue_tree_reader_node_carries_id_speaker_and_text_as_written() -> void:
	var node: Dictionary = _tree()["nodes"]["default_greeting"]
	assert_eq(node["id"], "default_greeting")
	assert_eq(node["line_id"], "test_greeting_001")
	assert_eq(node["speaker"], "Test Npc")
	assert_eq(node["text"], "FIXTURE GREETING")


func test_dialogue_tree_reader_option_names_its_next_node_and_requirement() -> void:
	var options: Array = _tree()["nodes"]["default_greeting"]["options"]
	assert_eq(options.size(), 2)
	assert_eq(options[0]["text"], "FIXTURE ASK")
	assert_eq(options[0]["next"], "more")
	assert_eq(options[0]["requires"], {}, "null requires reads as no requirement")
	assert_eq(options[1]["requires"], {"item": "fixture_item"})


func test_dialogue_tree_reader_node_without_options_has_an_empty_list() -> void:
	assert_eq(_tree()["nodes"]["more"]["options"], [])


func test_dialogue_tree_reader_unknown_fields_pass_through_in_extra() -> void:
	var tree := _tree()
	var greeting: Dictionary = tree["nodes"]["default_greeting"]
	assert_eq(greeting["extra"]["emotion"], "smug")
	assert_eq(greeting["extra"]["party_specific_overrides"],
		{"bradley_present": {"text": "FIXTURE BRADLEY"}})
	assert_false(greeting["extra"].has("text"), "known fields are not repeated in extra")
	assert_eq(tree["nodes"]["more"]["extra"]["set_flags"], {"fixture_flag": true})
	assert_eq(greeting["options"][0]["extra"]["party_reaction"], {"Bradley": "FIXTURE REACTION"})
	assert_false(greeting["options"][0]["extra"].has("leads_to"))


func test_dialogue_tree_reader_status_and_world_state_lines_are_grouped_per_npc() -> void:
	var tree := _tree()
	assert_eq(tree["status_lines"], {"hungover": "FIXTURE HUNGOVER"})
	assert_eq(tree["world_state_lines"], {"fixture_state": "FIXTURE STATE"})


func test_dialogue_tree_reader_reports_an_option_that_leads_nowhere() -> void:
	var result := DialogueTreeReader.read_doc(_doc())
	var problems: Array = result["problems"]
	assert_eq(problems.size(), 1)
	assert_string_contains(problems[0], "test_npc")
	assert_string_contains(problems[0], "default_greeting")
	assert_string_contains(problems[0], "nowhere")
	assert_eq(result["trees"]["test_npc"]["nodes"]["default_greeting"]["options"][1]["next"],
		"nowhere", "the broken link is kept as written, not repaired")


func test_dialogue_tree_reader_reports_a_missing_start_and_missing_text() -> void:
	var doc := {"dialogue_trees": {"bare_npc": {"some_node": {"speaker": "Bare"}}}}
	var result := DialogueTreeReader.read_doc(doc)
	var tree: Dictionary = result["trees"]["bare_npc"]
	assert_eq(tree["start"], "", "no default_greeting means no start; none is invented")
	assert_eq(tree["nodes"]["some_node"]["text"], "")
	assert_eq(result["problems"].size(), 2)
	assert_string_contains(" | ".join(result["problems"]), "default_greeting")
	assert_string_contains(" | ".join(result["problems"]), "no text")


func test_dialogue_tree_reader_does_not_change_the_document_it_reads() -> void:
	var doc := _doc()
	var before := JSON.stringify(doc)
	var result := DialogueTreeReader.read_doc(doc)
	result["trees"]["test_npc"]["nodes"]["more"]["extra"]["set_flags"]["fixture_flag"] = false
	assert_eq(JSON.stringify(doc), before)


func test_dialogue_tree_reader_empty_document_gives_no_trees_and_no_problems() -> void:
	var result := DialogueTreeReader.read_doc({"dialogue_trees": {}})
	assert_eq(result["trees"], {})
	assert_eq(result["problems"], [])


func test_dialogue_tree_reader_read_file_reports_a_missing_file() -> void:
	var result := DialogueTreeReader.read_file("res://assets/data/npcs/dialogue_trees/nope.json")
	assert_eq(result["trees"], {})
	assert_eq(result["problems"].size(), 1)
	assert_string_contains(result["problems"][0], "nope.json")


func test_dialogue_tree_reader_read_file_reads_the_shipped_debaucheryville_trees() -> void:
	var result := DialogueTreeReader.read_file(REAL_FILE)
	assert_gt(result["trees"].size(), 0)
	for npc_id: String in result["trees"]:
		var tree: Dictionary = result["trees"][npc_id]
		assert_eq(tree["npc_id"], npc_id)
		assert_gt(tree["nodes"].size(), 0, npc_id + " has nodes")
	for problem in result["problems"]:
		assert_typeof(problem, TYPE_STRING)
