extends GutTest
## Intoxicant consumables (Eurobound-umy) and rest events (Eurobound-5kf4). Fixture numbers only;
## the shipped data is all null and a test proves that is inert.


class FakeWallet:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []


class FakeRepo:
	var d: Dictionary

	func _init(items: Dictionary) -> void:
		d = items

	func get_item(id: String) -> Dictionary:
		return d.get(id, {})


var st


func before_each() -> void:
	StatusTable.set_entries({
		"rush": {"display_name": "Rush", "scope": ["battle", "field"], "default_duration": {"battle_turns": null, "ends_on_rest": true}, "on_rest": [{"event": "deep_clean", "flag": "deep_clean_pending", "discards": null}]},
		"crash": {"display_name": "Crash", "default_duration": {"battle_turns": 3, "field_steps": 80}},
		"gush": {"display_name": "Gush", "default_duration": {"ends_on_rest": null}, "on_rest": [{"event": "munchies_tax", "flag": "tax_pending", "sovs": null}]},
		"cotton": {"default_duration": {"ends_on_rest": true, "until_cured": true}, "cured_by": [{"kind": "rest"}]},
	})
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "chadwick", "display_name": "Chadwick", "hp": 10, "max_hp": 30, "bravado": 5, "max_bravado": 10}]


func after_each() -> void:
	StatusTable.reset()
	st.free()


func _item(turns: Variant = 3, steps: Variant = 80, rule: String = "extend", then: Variant = {"status": "crash", "stacks": true}) -> Dictionary:
	return {"display_name": "Cake", "heal_hp": 0, "heal_bravado": 0, "usable_in": null, "max_stack": null,
		"intoxicant": {"status": "rush", "duration": {"battle_turns": turns, "field_steps": steps, "ends_on_rest": true}, "stack_rule": rule, "then": then}}


func _core(item: Dictionary) -> BattleCore:
	var r := RandomNumberGenerator.new()
	r.seed = 1
	var core := BattleCore.new(r)
	core.wallet = FakeWallet.new()
	core.wallet.inventory = {"cake": 5}
	core.items = {"cake": item}
	core.party.append(BattleUnit.from_member({"id": "bro", "display_name": "Bro", "max_hp": 30, "hp": 30, "max_bravado": 12,
		"bravado": 10, "offense": 8, "defense": 2, "speed": 5, "luck": 0, "grit": 1, "charm": 4, "skills": []}))
	core.add_enemy(BattleUnit.from_enemy("foe", {"display_name": "Foe", "max_hp": 50, "offense": 1, "defense": 0,
		"speed": 1, "luck": 0, "ticket_reward": 0}, {}))
	core.start()
	core.tick(5.0)
	core.step()
	return core


func _use(core: BattleCore) -> bool:
	core.minor_used = false
	return core.use_item("cake", core.party[0])


func test_battle_effect_and_usable_in() -> void:
	assert_true(BattleCore.has_battle_effect(_item()))
	assert_true(_core(_item()).usable_items().has("cake"))
	var field_only := _item()
	field_only["usable_in"] = ["field"]
	assert_false(_core(field_only).usable_items().has("cake"))


func test_apply_in_battle() -> void:
	var core := _core(_item())
	assert_true(_use(core))
	assert_eq(core.party[0].statuses["rush"], 3)


func test_extend_adds_turns_and_stacks_then() -> void:
	var core := _core(_item())
	_use(core)
	_use(core)
	assert_eq(core.party[0].statuses["rush"], 6)
	assert_eq(core.party[0].then_pending["rush"]["count"], 2)


func test_refresh_and_none() -> void:
	var core := _core(_item(3, 80, "refresh"))
	_use(core)
	core.party[0].statuses["rush"] = 1
	_use(core)
	assert_eq(core.party[0].statuses["rush"], 3)
	var core2 := _core(_item(3, 80, "none"))
	_use(core2)
	core2.party[0].statuses["rush"] = 1
	_use(core2)
	assert_eq(core2.party[0].statuses["rush"], 1)


func test_then_fires_on_expiry_from_table_default() -> void:
	var core := _core(_item(1))
	_use(core)
	var u: BattleUnit = core.party[0]
	u.end_own_turn()
	core._fire_due_then(u)
	assert_false(u.statuses.has("rush"))
	assert_eq(u.statuses.get("crash", 0), 3)


func test_cure_cancels_then() -> void:
	var core := _core(_item(2))
	_use(core)
	core.party[0].statuses.erase("rush")
	core.party[0].then_pending.erase("rush")
	core.party[0].end_own_turn()
	assert_true(core.party[0].due_then.is_empty())


func test_null_values_are_inert() -> void:
	var core := _core(_item(null, null))
	_use(core)
	assert_false(core.party[0].statuses.has("rush"))
	assert_true(core.party[0].then_pending.is_empty())
	assert_false(Intoxicant.apply_field(st, "chadwick", _item(null, null)))
	assert_eq(Intoxicant.max_stack({"max_stack": null}), null)


func test_intoxicant_battle_use_field_only_status_carries_to_field() -> void:
	# Arrange: a Grist-like item, steps only, no battle counter (Eurobound-qloc)
	var core := _core(_item(null, 200, "extend", {}))
	core.wallet.inventory["cake"] = 5
	# Act
	_use(core)
	core.write_back_field_statuses()
	# Assert: one use writes 200 steps, a second extends to 400, no battle counter
	var row: Dictionary = core.wallet.flags[FieldStatus.KEY]["bro"]["rush"]
	assert_eq(int(row["left"]), 200)
	assert_false(row.has("turns"))
	assert_false(core.party[0].statuses.has("rush"))
	_use(core)
	core.write_back_field_statuses()
	assert_eq(int(core.wallet.flags[FieldStatus.KEY]["bro"]["rush"]["left"]), 400)


func test_intoxicant_battle_use_field_only_item_stays_refused() -> void:
	var item := _item(null, 200, "extend", {})
	item["usable_in"] = ["field"]
	var core := _core(item)
	assert_false(core.usable_items().has("cake"))
	assert_false(_use(core))
	assert_false(core.wallet.flags.has(FieldStatus.KEY))


func test_field_apply_extend_then_expiry() -> void:
	var item := _item(3, 80)
	assert_true(Intoxicant.apply_field(st, "chadwick", item))
	assert_true(Intoxicant.apply_field(st, "chadwick", item))
	var row: Dictionary = st.flags[FieldStatus.KEY]["chadwick"]["rush"]
	assert_eq(row["left"], 160)
	assert_eq(row["turns"], 6)
	assert_eq(row["then"]["stacks_count"], 2)
	FieldStatus.add_steps(st, 160)
	assert_false(FieldStatus.has(st, "rush"))
	assert_true(FieldStatus.has(st, "crash"))


func test_field_stack_none_and_refresh() -> void:
	Intoxicant.apply_field(st, "chadwick", _item(3, 80, "none"))
	assert_false(Intoxicant.apply_field(st, "chadwick", _item(3, 80, "none")))
	FieldStatus.add_steps(st, 30)
	Intoxicant.apply_field(st, "chadwick", _item(3, 80, "refresh"))
	assert_eq(st.flags[FieldStatus.KEY]["chadwick"]["rush"]["left"], 80)


func test_gamestate_use_item_applies_and_honours_usable_in() -> void:
	st.inventory = {"cake": 2}
	assert_true(st.use_item("cake", FakeRepo.new({"cake": _item()})))
	assert_true(FieldStatus.has(st, "rush", "chadwick"))
	var battle_only := _item()
	battle_only["usable_in"] = ["battle"]
	assert_false(st.use_item("cake", FakeRepo.new({"cake": battle_only})))
	assert_eq(st.inventory["cake"], 1)


func test_max_stack_caps_add_item() -> void:
	st.add_item("cake", 5, 3)
	assert_eq(st.inventory["cake"], 3)
	st.add_item("pie", 5)
	assert_eq(st.inventory["pie"], 5)


# --- rest events (Eurobound-5kf4) ---------------------------------------------------------------

func _row(id: String, extra: Dictionary = {}) -> void:
	FieldStatus.apply_steps(st, "chadwick", id, 100)
	for k in extra:
		st.flags[FieldStatus.KEY]["chadwick"][id][k] = extra[k]


func test_rest_sets_pending_flags_then_removes_ends_on_rest() -> void:
	_row("rush")
	_row("gush")
	st.inventory = {"key_thing": 1, "beer": 2}
	st.sovs = 50
	GameClock.rest(st)
	assert_true(st.flags.get("deep_clean_pending", false))
	assert_true(st.flags.get("tax_pending", false))
	assert_false(FieldStatus.has(st, "rush"), "ends_on_rest true is removed")
	assert_true(FieldStatus.has(st, "gush"), "ends_on_rest null stays")
	assert_eq(st.inventory, {"key_thing": 1, "beer": 2}, "nothing discarded")
	assert_eq(st.sovs, 50, "nothing taken")


func test_rest_cures_by_kind_and_row_override() -> void:
	_row("cotton")
	_row("gush", {"ends_on_rest": true})
	GameClock.rest(st)
	assert_false(FieldStatus.has(st, "cotton"))
	assert_false(FieldStatus.has(st, "gush"))


func test_rest_with_no_statuses_sets_nothing() -> void:
	GameClock.rest(st)
	assert_false(st.flags.has("deep_clean_pending"))
	assert_false(st.flags.has("tax_pending"))
