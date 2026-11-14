extends GutTest
## DebugCommands (Eurobound-08bo): console command logic over the existing game APIs.

const GameStateScript := preload("res://core/game_state.gd")

var state


class FakeRepo:
	func get_item(id: String) -> Dictionary:
		return {"max_stack": 3} if id == "real_item" else {}


func before_each() -> void:
	state = autofree(GameStateScript.new())


func test_debug_commands_set_and_clear_flag_round_trips() -> void:
	# Act
	DebugCommands.set_flag(state, "met_vanek")
	var set_ok: bool = state.has_flag("met_vanek")
	var missing := DebugCommands.clear_flag(state, "nope")
	DebugCommands.clear_flag(state, "met_vanek")
	# Assert
	assert_true(set_ok)
	assert_false(state.flags.has("met_vanek"))
	assert_string_contains(missing, "no such flag")


func test_debug_commands_list_flags_is_sorted() -> void:
	# Arrange
	state.flags = {"b": true, "a": true}
	# Act
	var out := DebugCommands.list_flags(state)
	# Assert
	assert_true(out.find("a = true") < out.find("b = true"))


func test_debug_commands_remove_sovs_refuses_when_short() -> void:
	# Arrange
	DebugCommands.add_sovs(state, 40)
	# Act
	DebugCommands.remove_sovs(state, 100)
	var after_refusal: int = state.sovs
	DebugCommands.remove_sovs(state, 15)
	DebugCommands.add_sovs(state, -5)
	# Assert
	assert_eq(after_refusal, 40)
	assert_eq(state.sovs, 25)


func test_debug_commands_give_item_known_only_and_capped() -> void:
	# Arrange
	var repo := FakeRepo.new()
	# Act
	DebugCommands.give_item(state, repo, "real_item", 5)
	var unknown := DebugCommands.give_item(state, repo, "made_up")
	# Assert
	assert_eq(state.inventory.get("real_item"), 3)
	assert_string_contains(unknown, "unknown item")
	assert_false(state.inventory.has("made_up"))


func test_debug_commands_unknown_status_is_refused() -> void:
	assert_string_contains(DebugCommands.apply_status(state, "not_a_status"), "unknown status")


func test_debug_commands_apply_then_clear_table_status() -> void:
	# Arrange: first status the table can apply in the field
	var applied := ""
	for id in StatusTable.entries().keys():
		if FieldStatus.apply_from_table(state, "party", id):
			applied = id
			break
	if applied == "":
		pending("no table status applies in the field")
		return
	var was_on := FieldStatus.has(state, applied)
	# Act
	DebugCommands.clear_status(state, applied)
	# Assert
	assert_true(was_on)
	assert_false(FieldStatus.has(state, applied))


func test_debug_commands_set_clock_rejects_bad_hour() -> void:
	# Act
	DebugCommands.set_clock(state, 22, 30, 1)
	var good := GameClock.minutes(state)
	DebugCommands.set_clock(state, 99)
	# Assert
	assert_eq(good, 1440 + 22 * 60 + 30)
	assert_eq(GameClock.minutes(state), good)
