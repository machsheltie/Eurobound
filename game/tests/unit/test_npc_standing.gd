extends GutTest
## Eurobound-3385: per-NPC grudge and fan flags. Author ruling f3tq-q6 (Eurobound Desk, 2026-11-13):
## "Flags only: an NPC can hold a grudge or become a fan (no numbers)". The flags are booleans in
## GameState.flags, so they save with every other flag; no numeric standing exists anywhere.

const STATE_SCRIPT := "res://core/game_state.gd"
const REGISTRY := "res://assets/data/world_data/quest_flags.json"


class FakeState:
	var flags := {}

	func has_flag(flag_name: String) -> bool:
		return flags.get(flag_name, false)


func test_npc_standing_starts_with_no_grudge_and_no_fan() -> void:
	var s := FakeState.new()
	assert_false(NpcStanding.has_grudge(s, "test_npc_a"))
	assert_false(NpcStanding.is_fan(s, "test_crowd_a"))
	assert_eq(NpcStanding.standing(s, "test_npc_a"), {"grudge": false, "fan": false})


func test_npc_standing_sets_and_reads_a_grudge_under_the_registry_id() -> void:
	var s := FakeState.new()
	assert_true(NpcStanding.set_grudge(s, "test_npc_a"))
	assert_true(NpcStanding.has_grudge(s, "test_npc_a"))
	assert_true(s.flags.get("grudge:test_npc_a"), "stored as grudge:<npc_id>")
	assert_false(NpcStanding.has_grudge(s, "test_npc_b"), "a grudge is per NPC")
	assert_false(NpcStanding.is_fan(s, "test_npc_a"), "a grudge sets no fan flag")


func test_npc_standing_sets_and_reads_a_fan_under_the_registry_id() -> void:
	var s := FakeState.new()
	assert_true(NpcStanding.set_fan(s, "test_crowd_a"))
	assert_true(NpcStanding.is_fan(s, "test_crowd_a"))
	assert_true(s.flags.get("fan:test_crowd_a"), "stored as fan:<id>")
	assert_false(NpcStanding.has_grudge(s, "test_crowd_a"), "a fan flag sets no grudge")


func test_npc_standing_clears_each_flag_on_its_own() -> void:
	var s := FakeState.new()
	NpcStanding.set_grudge(s, "test_npc_a")
	NpcStanding.set_fan(s, "test_npc_a")
	assert_eq(NpcStanding.standing(s, "test_npc_a"), {"grudge": true, "fan": true},
		"the two flags are independent: no ruling makes them exclusive")
	NpcStanding.clear_grudge(s, "test_npc_a")
	assert_eq(NpcStanding.standing(s, "test_npc_a"), {"grudge": false, "fan": true})
	NpcStanding.clear_fan(s, "test_npc_a")
	assert_eq(NpcStanding.standing(s, "test_npc_a"), {"grudge": false, "fan": false})
	assert_false(s.flags.has("grudge:test_npc_a"))
	assert_false(s.flags.has("fan:test_npc_a"))


func test_npc_standing_setting_twice_is_still_one_boolean() -> void:
	var s := FakeState.new()
	NpcStanding.set_grudge(s, "test_npc_a")
	NpcStanding.set_grudge(s, "test_npc_a")
	assert_true(s.flags["grudge:test_npc_a"] is bool, "no count, no numbers")
	NpcStanding.clear_grudge(s, "test_npc_a")
	assert_false(NpcStanding.has_grudge(s, "test_npc_a"), "one clear undoes any number of sets")


func test_npc_standing_refuses_ids_the_registry_pattern_cannot_hold() -> void:
	var s := FakeState.new()
	for bad in ["", "Test Npc A", "test-npc-a", "grudge:nested"]:
		assert_false(NpcStanding.set_grudge(s, bad), "refused: '%s'" % bad)
		assert_false(NpcStanding.set_fan(s, bad), "refused: '%s'" % bad)
		assert_false(NpcStanding.has_grudge(s, bad))
	assert_true(s.flags.is_empty(), "nothing written for a refused id")


func test_npc_standing_reads_through_has_flag_for_dialogue_conditions() -> void:
	# Dialogue conditions read flags by id (GameState.has_flag, or a tree option's requires flag).
	var s := FakeState.new()
	NpcStanding.set_grudge(s, "test_npc_a")
	NpcStanding.set_fan(s, "test_crowd_a")
	assert_true(s.has_flag(NpcStanding.grudge_flag("test_npc_a")))
	assert_true(s.has_flag(NpcStanding.fan_flag("test_crowd_a")))
	assert_eq(NpcStanding.grudge_flag("test_npc_a"), "grudge:test_npc_a")
	assert_eq(NpcStanding.fan_flag("test_crowd_a"), "fan:test_crowd_a")


func test_npc_standing_applies_the_grudge_and_fan_entries_of_an_outcome_set_flags() -> void:
	# An event outcome writes flags with the ruled shape "set_flags": {"<id>": <value>}.
	var s := FakeState.new()
	s.flags["fan:test_crowd_b"] = true
	var applied: Array = NpcStanding.apply_set_flags(s, {
		"grudge:test_npc_a": true,
		"fan:test_crowd_a": true,
		"fan:test_crowd_b": false,
		"some_quest_flag": true,
		"grudge:not_a_bool": 1,
		"grudge:Bad Id": true,
	})
	applied.sort()
	assert_eq(applied, ["fan:test_crowd_a", "fan:test_crowd_b", "grudge:test_npc_a"])
	assert_true(NpcStanding.has_grudge(s, "test_npc_a"))
	assert_true(NpcStanding.is_fan(s, "test_crowd_a"))
	assert_false(NpcStanding.is_fan(s, "test_crowd_b"), "false clears")
	assert_false(s.flags.has("some_quest_flag"), "other flags are not this store's to write")
	assert_false(s.flags.has("grudge:not_a_bool"), "only booleans: no numeric standing")
	assert_false(s.flags.has("grudge:Bad Id"))


func test_npc_standing_flags_survive_a_json_save_round_trip() -> void:
	var before = autofree(load(STATE_SCRIPT).new())
	NpcStanding.set_grudge(before, "test_npc_a")
	NpcStanding.set_fan(before, "test_crowd_a")
	var text := JSON.stringify(before.to_dict())
	var after = autofree(load(STATE_SCRIPT).new())
	after.from_dict(JSON.parse_string(text))
	assert_true(NpcStanding.has_grudge(after, "test_npc_a"))
	assert_true(NpcStanding.is_fan(after, "test_crowd_a"))
	assert_false(NpcStanding.is_fan(after, "test_npc_a"))
	assert_true(after.flags["grudge:test_npc_a"] is bool)


func test_npc_standing_registry_declares_both_patterns_as_booleans() -> void:
	var doc: Variant = JSON.parse_string(FileAccess.get_file_as_string(REGISTRY))
	assert_true(doc is Dictionary)
	var patterns: Dictionary = doc["flag_patterns"]
	for pid in [NpcStanding.GRUDGE_PREFIX + "{npc_id}", NpcStanding.FAN_PREFIX + "{crowd_or_npc_id}"]:
		assert_true(patterns.has(pid), "%s declared in flag_patterns" % pid)
		if patterns.has(pid):
			assert_eq(patterns[pid]["type"], "bool", pid)
			assert_eq(patterns[pid]["default"], false, pid)
