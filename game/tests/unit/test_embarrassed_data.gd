extends GutTest
## Embarrassed (Eurobound-0dde): its ruled numbers live in status_effects.json and apply once;
## the skill lock follows the ruling (round v27, docs/superpowers/NEXT_WORK.md:569; Desk g0jr-q3,
## :948): locks Bravado-cost moves and Ultimates, blocks Taunt, allows Flex and Item.


class FakeWallet:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _bro(bravado: int = 12) -> BattleUnit:
	return BattleUnit.from_member({"id": "chadwick", "display_name": "chadwick", "max_hp": 40, "hp": 40,
		"max_bravado": 12, "bravado": bravado, "offense": 10, "defense": 2, "speed": 20, "luck": 0,
		"grit": 0, "charm": 10, "skills": []})


func _villain() -> BattleUnit:
	return BattleUnit.from_enemy("croc", {"display_name": "croc", "max_hp": 200, "offense": 6, "defense": 0,
		"speed": 1, "luck": 0, "ticket_reward": 5}, {})


func _core(bro: BattleUnit) -> BattleCore:
	var r := RandomNumberGenerator.new()
	r.seed = 1
	var core := BattleCore.new(r)
	core.wallet = FakeWallet.new()
	core.party.append(bro)
	core.add_enemy(_villain())
	core.start()
	return core


func test_embarrassed_row_carries_the_ruled_numbers() -> void:
	var row := StatusTable.entry("embarrassed")
	assert_eq(int(row["stats_pct"]["offense"]["pct"]), -20, "-20% ATK")
	assert_eq(int(row["stats_pct"]["charm"]["pct"]), -20, "social attacks keep the -20%")
	assert_eq(int(row["bravado_tick"]["battle_per_turn"]), -2, "-2 Bravado a turn")


func test_embarrassed_engine_no_longer_hard_codes_the_numbers() -> void:
	var consts: Dictionary = BattleRulings.new().get_script().get_script_constant_map()
	assert_false(consts.has("EMBARRASSED_ATK"), "data is the single source")
	assert_false(consts.has("EMBARRASSED_DRAIN"), "data is the single source")


func test_embarrassed_atk_penalty_applies_once() -> void:
	var bro := _bro()
	bro.statuses["embarrassed"] = 2
	assert_eq(bro.attack_stat(false), 8.0, "10 -20% once (twice would be 6.4)")
	assert_eq(bro.attack_stat(true), 8.0, "Charm 10 -20% once")


func test_embarrassed_bravado_drain_applies_once() -> void:
	var bro := _bro(12)
	bro.statuses["embarrassed"] = 2
	var core := _core(bro)
	core.step()
	assert_eq(core.current(), bro)
	assert_eq(bro.bravado, 10, "-2 once, not -4")


func test_embarrassed_free_non_taunt_skill_is_usable() -> void:
	var bro := _bro()
	bro.statuses["embarrassed"] = 2
	var core := _core(bro)
	var free := {"display_name": "Free Jab", "bravado_cost": 0, "power_multiplier": 1.0}
	assert_true(core.can_use_skill(bro, free))


func test_embarrassed_still_locks_bravado_cost_moves_and_ultimates() -> void:
	var bro := _bro()
	bro.statuses["embarrassed"] = 2
	var core := _core(bro)
	assert_false(core.can_use_skill(bro, {"display_name": "Roast", "bravado_cost": 4}))
	assert_false(core.can_use_skill(bro, {"display_name": "Big One", "bravado_cost": 0, "is_ultimate": true}))


func test_embarrassed_blocks_taunt_allows_flex_and_item() -> void:
	var bro := _bro(5)
	bro.hp = 10
	bro.statuses["embarrassed"] = 2
	var core := _core(bro)
	core.step()
	assert_false(core.can_taunt())
	assert_true(core.can_flex())
	core.wallet.add_item("test_tonic")
	core.items["test_tonic"] = {"display_name": "Tonic", "heal_hp": 5}
	assert_true(core.use_item("test_tonic", bro), "Item allowed")
	assert_eq(bro.hp, 15)
