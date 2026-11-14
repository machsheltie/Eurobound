extends GutTest
## Quest Log (author round v42): registry, step derivation from flags, active/completed, menu listing.

const QID := "debaucheryville_sidequest_grandpa_provides_01"

class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []
	var current_scene_path := ""


func _quest() -> Dictionary:
	return QuestLog.quests().filter(func(q): return q["quest_id"] == QID)[0]


func _states(s) -> Array:
	return QuestLog.steps(s, _quest()).map(func(r): return r["state"])


func _menu(s) -> FieldMenu:
	var m := FieldMenu.new()
	m.setup(s)
	add_child_autofree(m)
	m.mode = "Quest Log"
	m._draw()
	return m


func test_quest_log_registry_loads_grandpa_provides_with_approved_objectives() -> void:
	var q := _quest()
	assert_eq(q["display_name"], "Grandpa Provides")
	assert_eq(q["steps"].map(func(x): return x["id"]), ["the_tip", "the_girls_round", "the_unsettled_tab"])
	for st in q["steps"]:
		assert_ne(st["objective"], "")


func test_quest_log_quest_is_hidden_until_it_starts() -> void:
	assert_eq(QuestLog.status(FakeState.new(), _quest()), "hidden")


func test_quest_log_tip_starts_the_quest_and_the_next_step_is_current() -> void:
	var s := FakeState.new()
	s.flags[GrandpaProvides.RING_TIPPED] = true
	assert_eq(QuestLog.status(s, _quest()), "active")
	assert_eq(_states(s), ["done", "current", "pending"])


func test_quest_log_round_bought_makes_the_tab_current() -> void:
	var s := FakeState.new()
	s.flags[GrandpaProvides.RING_TIPPED] = true
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	assert_eq(_states(s), ["done", "done", "current"])


func test_quest_log_paying_completes_with_the_paid_outcome() -> void:
	var s := FakeState.new()
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	s.sovs = 100
	GrandpaProvides.pay(s)
	assert_eq(QuestLog.status(s, _quest()), "completed")
	assert_eq(QuestLog.steps(s, _quest()).back()["id"], "tab_paid")


func test_quest_log_fleeing_completes_with_the_tab_open() -> void:
	var s := FakeState.new()
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	GrandpaProvides.fled(s)
	assert_eq(QuestLog.status(s, _quest()), "completed")
	assert_eq(QuestLog.steps(s, _quest()).back()["id"], "tab_open")


func test_quest_log_losing_completes_with_the_tab_stolen_outcome() -> void:
	# Arrange
	var s := FakeState.new()
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	s.sovs = 100
	# Act
	GrandpaProvides.lost(s)
	# Assert
	assert_eq(QuestLog.status(s, _quest()), "completed")
	assert_eq(QuestLog.steps(s, _quest()).back()["id"], "tab_stolen")


func test_quest_log_label_humanises_the_id_until_objective_text_arrives() -> void:
	assert_eq(QuestLog.label({"id": "the_tip", "objective": ""}), "The Tip")
	assert_eq(QuestLog.label({"id": "the_tip", "objective": "Tip Tomas."}), "Tip Tomas.")


func test_quest_log_menu_lists_active_then_completed_and_backs_out() -> void:
	var s := FakeState.new()
	s.flags[GrandpaProvides.RING_TIPPED] = true
	var m := _menu(s)
	assert_string_contains(m._body.text, "Grandpa Provides")
	assert_string_contains(m._body.text, "Active")
	assert_string_contains(m._body.text, "Buy the birthday girls a round at the bar.")
	m.press("move_down")
	assert_eq(m.cursor, 0, "one quest: the cursor wraps")
	s.flags[GrandpaProvides.AR_DEFEATED] = true
	m._draw()
	assert_string_contains(m._body.text, "Completed")
	m.press("cancel")
	assert_eq(m.mode, "root")


func test_quest_log_menu_quest_log_is_empty_before_any_quest() -> void:
	var m := _menu(FakeState.new())
	assert_string_contains(m._body.text, "—")
