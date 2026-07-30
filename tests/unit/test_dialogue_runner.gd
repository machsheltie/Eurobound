extends GutTest

var repo
var tree: Dictionary

func before_each() -> void:
	repo = load("res://Scripts/core/data_repo.gd").new()
	repo.load_all()
	tree = repo.get_dialogue_tree("vlad_validator")

func test_start_returns_greeting() -> void:
	var runner := DialogueRunner.new(tree)
	var node := runner.start()
	assert_true(node.has("text"))
	assert_eq(node.get("speaker"), "Vlad the Validator")

func test_option_requiring_item_is_hidden_without_it() -> void:
	var runner := DialogueRunner.new(tree)
	runner.start()
	var all_options: Array = tree["default_greeting"]["options"]
	var visible := runner.available_options({})
	assert_lt(visible.size(), all_options.size(),
		"the [Show NFT Screenshot] option requires an item the player lacks")

func test_option_requiring_item_shown_with_it() -> void:
	var runner := DialogueRunner.new(tree)
	runner.start()
	var visible := runner.available_options({"Rare_NFT_Screenshot": 1})
	assert_eq(visible.size(), tree["default_greeting"]["options"].size())

func test_choose_follows_leads_to() -> void:
	var runner := DialogueRunner.new(tree)
	runner.start()
	var options := runner.available_options({})
	var next := runner.choose(options[0])
	assert_true(next.has("text"), "choosing an option should enter the next node")

func test_unknown_node_returns_empty() -> void:
	var runner := DialogueRunner.new(tree)
	assert_eq(runner.start("no_such_node"), {})

func test_conversation_end_sentinel_ends_dialogue() -> void:
	var runner := DialogueRunner.new(tree)
	runner.start()
	# [Show NFT Screenshot] requires the item and leads to vlad_nft_impressed,
	# whose only option ("Finally...") leads_to the schema sentinel
	# "conversation_end".
	var visible := runner.available_options({"Rare_NFT_Screenshot": 1})
	var nft_option: Dictionary = {}
	for option in visible:
		if option.get("leads_to") == "vlad_nft_impressed":
			nft_option = option
	assert_false(nft_option.is_empty(), "expected an option leading to vlad_nft_impressed")
	runner.choose(nft_option)
	assert_eq(runner.current_key, "vlad_nft_impressed")
	var final_options: Array = tree["vlad_nft_impressed"]["options"]
	var result := runner.choose(final_options[0])
	assert_eq(result, {}, "choosing an option leading to conversation_end should return {}")
	assert_eq(runner.current_key, "", "conversation_end should end the dialogue")
