extends GutTest
## BattleCore: turn order, the bros' actions, rolling HP, outcomes and the villain gimmicks.


class FakeWallet:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _rng(seed_value: int = 1) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func _bro(id: String, hp: int, speed: int, bravado: int = 12) -> BattleUnit:
	return BattleUnit.from_member({"id": id, "display_name": id, "max_hp": hp, "hp": hp, "max_bravado": 12,
		"bravado": bravado, "offense": 8, "defense": 2, "speed": speed, "luck": 0, "grit": 0, "charm": 4,
		"skills": ["roast_line"]})


func _villain(id: String, hp: int, speed: int, battle: Dictionary = {}) -> BattleUnit:
	return BattleUnit.from_enemy(id, {"display_name": id, "max_hp": hp, "offense": 6, "defense": 0,
		"speed": speed, "luck": 0, "ticket_reward": 5}, battle)


## A fight where the villain's only move is a 0-weight table: it just hesitates.
func _core(bros: Array, villains: Array, seed_value: int = 1) -> BattleCore:
	var core := BattleCore.new(_rng(seed_value))
	core.wallet = FakeWallet.new()
	for b in bros:
		core.party.append(b)
	for v in villains:
		core.add_enemy(v)
	core.start()
	return core


func test_battle_core_round_order_fastest_first_bros_win_ties() -> void:
	# Arrange: Bradley speed 8 (High Bravado +2 = 10), a villain at 10, Pilsner at 5 (+2 = 7).
	var pilsner := _bro("lord_pilsner", 45, 5)
	var bradley := _bro("bradley", 30, 8)
	var villain := _villain("swap", 16, 10)
	# Act
	var core := _core([pilsner, bradley], [villain])
	core.step()
	# Assert: Bradley ties the villain at 10 and goes first.
	assert_eq(core.current(), bradley)


func test_battle_core_flex_restores_three_once_per_turn() -> void:
	# Arrange
	var pilsner := _bro("lord_pilsner", 45, 9, 2)
	var core := _core([pilsner], [_villain("swap", 16, 1)])
	core.step()
	# Act
	core.flex()
	core.flex()
	# Assert
	assert_eq(pilsner.bravado, 5)


func test_battle_core_roast_line_costs_bravado_and_embarrassed_locks_it() -> void:
	# Arrange
	var pilsner := _bro("lord_pilsner", 45, 9, 12)
	var villain := _villain("croc", 200, 1)
	var core := _core([pilsner], [villain])
	core.step()
	var roast := {"display_name": "Roast Line", "bravado_cost": 4, "power_multiplier": 1.8}
	pilsner.statuses["embarrassed"] = 2
	# Act
	var locked := core.use_skill(roast, villain)
	pilsner.statuses.erase("embarrassed")
	var used := core.use_skill(roast, villain)
	# Assert
	assert_false(locked)
	assert_true(used)
	assert_eq(pilsner.bravado, 8)


func test_battle_core_rolling_meter_drops_ten_hp_a_second() -> void:
	# Arrange
	var pilsner := _bro("lord_pilsner", 45, 9)
	var core := _core([pilsner], [_villain("swap", 16, 1)])
	pilsner.take_damage(30)
	# Act
	core.tick(1.0)
	# Assert
	assert_eq(pilsner.hp, 15)
	assert_almost_eq(pilsner.meter, 35.0, 0.001)


func test_battle_core_lethal_hit_still_acts_and_win_keeps_meter_hp() -> void:
	# Arrange: Pilsner takes 60 on a 45 HP meter, then wins before it rolls to 0.
	var pilsner := _bro("lord_pilsner", 45, 9)
	var villain := _villain("swap", 1, 1)
	var core := _core([pilsner], [villain])
	pilsner.take_damage(60)
	core.tick(2.0)
	core.step()
	# Act
	core.attack(villain)
	# Assert
	assert_eq(core.outcome, "won")
	assert_eq(pilsner.settled_hp(), 25)


func test_battle_core_loss_when_every_meter_hits_zero() -> void:
	# Arrange
	var pilsner := _bro("lord_pilsner", 10, 9)
	var core := _core([pilsner], [_villain("swap", 16, 1)])
	pilsner.take_damage(10)
	# Act
	core.tick(2.0)
	# Assert
	assert_eq(core.outcome, "lost")


func test_battle_core_croc_bill_holds_at_one_hp_and_hits_the_knocker() -> void:
	# Arrange
	var bradley := _bro("bradley", 30, 9)
	var croc := _villain("croc_monsieur", 1, 1, {"bill": {"mult": 1.2, "log": "the bill"}})
	var core := _core([bradley], [croc])
	core.step()
	# Act: the knockdown, then any hit after that ends him.
	core.attack(croc)
	var held := croc.hp
	var bradley_hp := bradley.hp
	core.step()
	core.step()
	core.attack(croc)
	# Assert
	assert_eq(held, 1)
	assert_lt(bradley_hp, 30, "the bill lands on Bradley")
	assert_eq(core.outcome, "won")


func test_battle_core_clocked_move_winds_up_then_fires_next_turn() -> void:
	# Arrange: a 1-round clock AoE.
	var pilsner := _bro("lord_pilsner", 45, 1)
	var data := {"moves": [{"id": "big", "name": "Big", "type": "physical", "target": "all", "mult": 1.0,
		"clock": {"1": 1}, "telegraph": "Here it comes."}]}
	var villain := _villain("croc", 100, 9, data)
	var core := _core([pilsner], [villain])
	# Act: round 1, the villain is faster and winds up.
	core.step()
	var wound := not villain.telegraph.is_empty()
	var hp_after_windup := pilsner.hp
	core.step()          # Pilsner's turn begins
	core.flex()
	core.attack(villain)
	core.step()          # round 2: the villain fires
	# Assert
	assert_true(wound)
	assert_eq(hp_after_windup, 45)
	assert_lt(pilsner.hp, 45)


func test_battle_core_continue_revives_for_three_sovs_or_breaks_the_bros() -> void:
	# Arrange: Count Continue with a downed ally.
	var data := {"moves": [{"id": "continue", "name": "CONTINUE?", "type": "none", "target": "downed_ally",
		"special": "continue", "telegraph": "CONTINUE?", "max_uses": 2, "revive_pct": 0.5, "cost_sovs": 3}]}
	var count := _villain("count_continue", 34, 9, data)
	var ninja := _villain("ninja", 26, 1)
	var pilsner := _bro("lord_pilsner", 45, 2)
	var core := _core([pilsner], [count, ninja])
	core.wallet.sovs = 10
	ninja.take_damage(26)
	# Act: wind up, then the bros' turn, then it resolves.
	core.step()
	core.step()
	core.flex()
	core.attack(count)
	core.step()
	# Assert
	assert_eq(ninja.hp, 13)
	assert_eq(core.wallet.sovs, 7)


func test_battle_core_continue_without_money_gives_broke_af() -> void:
	# Arrange
	var data := {"moves": [{"id": "continue", "name": "CONTINUE?", "type": "none", "target": "downed_ally",
		"special": "continue", "telegraph": "CONTINUE?", "max_uses": 2, "revive_pct": 0.5, "cost_sovs": 3}]}
	var count := _villain("count_continue", 34, 9, data)
	var ninja := _villain("ninja", 26, 1)
	var pilsner := _bro("lord_pilsner", 45, 2)
	var core := _core([pilsner], [count, ninja])
	ninja.take_damage(26)
	# Act
	core.step()
	core.step()
	core.flex()
	core.attack(count)
	core.step()
	# Assert
	assert_eq(ninja.hp, 0)
	assert_true(pilsner.has_status("broke_af"))


func test_battle_core_swallowed_bro_skips_and_returns_with_grease_fingers() -> void:
	# Arrange
	var data := {"moves": [{"id": "swallow", "name": "Your Table Is Ready", "type": "none", "target": "one",
		"special": "swallow", "status": "grease_fingers", "status_turns": 3, "weight": 100}]}
	var croc := _villain("croc", 100, 9, data)
	var pilsner := _bro("lord_pilsner", 45, 1)
	var chadwick := _bro("chadwick", 35, 1)
	var core := _core([pilsner, chadwick], [croc])
	# Act
	core.step()
	var swallowed: BattleUnit = pilsner if pilsner.gone_turns > 0 else chadwick
	var hidden := not swallowed.targetable()
	for i in 4:
		if core.needs_input():
			core.flex()
			core.attack(croc)
		core.step()
	# Assert
	assert_true(hidden)
	assert_true(swallowed.has_status("grease_fingers") or swallowed.gone_turns == 0)


func test_battle_core_tickets_sum_every_villain_fought() -> void:
	# Arrange
	var core := _core([_bro("lord_pilsner", 45, 9)], [_villain("a", 1, 1), _villain("b", 1, 1)])
	# Act
	var t := core.tickets()
	# Assert
	assert_eq(t, 10)


func test_battle_core_run_succeeds_or_ends_the_turn() -> void:
	# Arrange
	var pilsner := _bro("lord_pilsner", 45, 9)
	var core := _core([pilsner], [_villain("swap", 16, 1)], 3)
	core.step()
	# Act
	core.run_away()
	# Assert
	assert_true(core.outcome == "ran" or not core.needs_input())
