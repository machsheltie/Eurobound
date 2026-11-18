extends GutTest
## BattleCore.roll_drops: the optional weighted `item_pool` beside `item_drop` (Eurobound-mt12).
## Test fixtures only; no real pool data exists yet (numbers await Desk jlzw-q2).


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func _villain(extra: Dictionary) -> BattleUnit:
	var e := {"display_name": "v", "max_hp": 10, "offense": 1, "defense": 0, "speed": 1, "luck": 0}
	e.merge(extra, true)
	return BattleUnit.from_enemy("v", e, {})


func _core(v: BattleUnit, seed_value: int = 1) -> BattleCore:
	var core := BattleCore.new(_rng(seed_value))
	core.add_enemy(v)
	return core


func test_battle_drop_pool_parses_items_and_weights() -> void:
	var v := _villain({"item_pool": [{"item": "a", "weight": 1}, {"item": "b", "weight": 3}]})
	assert_eq(v.item_pool.size(), 2)
	assert_eq(v.item_pool[1]["item"], "b")
	assert_eq(float(v.item_pool[1]["weight"]), 3.0)


func test_battle_drop_pool_skips_malformed_entries() -> void:
	var v := _villain({"item_pool": [{"item": "a", "weight": 0}, {"item": "", "weight": 1}, "x", {"item": "ok", "weight": 2}]})
	assert_eq(v.item_pool.size(), 1)
	assert_eq(v.item_pool[0]["item"], "ok")


func test_battle_drop_pool_single_item_drop_behaves_as_before() -> void:
	var core := _core(_villain({"item_drop": "solo", "drop_chance": 1.0}))
	assert_eq(core.roll_drops(), ["solo"])
	var none := _core(_villain({"item_drop": "solo", "drop_chance": 0.0}))
	assert_eq(none.roll_drops(), [])


func test_battle_drop_pool_yields_exactly_one_pooled_item_per_roll() -> void:
	var pool := [{"item": "a", "weight": 1}, {"item": "b", "weight": 1}, {"item": "c", "weight": 1}]
	var core := _core(_villain({"item_pool": pool, "drop_chance": 1.0}))
	var drops := core.roll_drops()
	assert_eq(drops.size(), 1)
	assert_true(drops[0] in ["a", "b", "c"])


func test_battle_drop_pool_wins_over_item_drop() -> void:
	var core := _core(_villain({"item_drop": "solo", "item_pool": [{"item": "a", "weight": 1}], "drop_chance": 1.0}))
	assert_eq(core.roll_drops(), ["a"])


func test_battle_drop_pool_respects_drop_chance() -> void:
	var core := _core(_villain({"item_pool": [{"item": "a", "weight": 1}], "drop_chance": 0.0}))
	assert_eq(core.roll_drops(), [])


func test_battle_drop_pool_is_weighted_and_deterministic_per_seed() -> void:
	var pool := [{"item": "rare", "weight": 1}, {"item": "common", "weight": 9}]
	var counts := {"rare": 0, "common": 0}
	for s in range(400):
		var first := _core(_villain({"item_pool": pool, "drop_chance": 1.0}), s).roll_drops()
		var again := _core(_villain({"item_pool": pool, "drop_chance": 1.0}), s).roll_drops()
		assert_eq(first, again)
		counts[first[0]] += 1
	assert_gt(counts["common"], counts["rare"] * 3)
	assert_gt(counts["rare"], 0)
