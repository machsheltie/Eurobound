extends GutTest
## ArcadeBattle: the cabinet release tables, the Kebab Kombat ladder and settling a fight.


class FakeState:
	var gold := 20
	var inventory := {}
	var flags := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "hp": 45, "max_hp": 45, "bravado": 12,
		 "max_bravado": 12, "offense": 8, "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3,
		 "skills": ["roast_line"]},
	]

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func test_arcade_battle_frogger_full_crossing_locked_until_first_win() -> void:
	# Arrange
	var state := FakeState.new()
	var full_crossings := 0
	# Act
	for i in 300:
		var ids := ArcadeBattle.pick_release("cabinet_frogger", state, _rng(i))
		if ids.size() == 3:
			full_crossings += 1
	# Assert
	assert_eq(full_crossings, 0)


func test_arcade_battle_frogger_full_crossing_appears_after_a_win() -> void:
	# Arrange
	var state := FakeState.new()
	state.flags[ArcadeBattle.won_flag("cabinet_frogger")] = true
	var full_crossings := 0
	# Act
	for i in 300:
		if ArcadeBattle.pick_release("cabinet_frogger", state, _rng(i)).size() == 3:
			full_crossings += 1
	# Assert
	assert_gt(full_crossings, 0)


func test_arcade_battle_kebab_kombat_ladder_advances_on_win_resets_on_loss() -> void:
	# Arrange
	var state := FakeState.new()
	var core := ArcadeBattle.build("cabinet_kebab_kombat", state, _rng(1))
	var first := core.enemies.map(func(e: BattleUnit) -> String: return e.id)
	# Act: win rung 1, then lose rung 2.
	core.outcome = "won"
	ArcadeBattle.settle("cabinet_kebab_kombat", core, state)
	var after_win := ArcadeBattle.rung(state)
	var second := ArcadeBattle.build("cabinet_kebab_kombat", state, _rng(2))
	second.outcome = "lost"
	ArcadeBattle.settle("cabinet_kebab_kombat", second, state)
	# Assert
	assert_eq(first, ["condiment_clan_ninja", "condiment_clan_ninja"])
	assert_eq(after_win, 1)
	assert_eq(second.enemies.size(), 3)
	assert_eq(ArcadeBattle.rung(state), 0)


func test_arcade_battle_ninjas_get_garlic_and_chili_nameplates() -> void:
	# Arrange
	var state := FakeState.new()
	# Act
	var core := ArcadeBattle.build("cabinet_kebab_kombat", state, _rng(5))
	# Assert: each slot is GARLIC/CHILI unless its 5% Mystery Brown roll hit.
	for e in core.enemies:
		assert_true(["GARLIC", "CHILI", "MYSTERY BROWN"].has(e.display_name), e.display_name)


func test_arcade_battle_settle_win_pays_tickets_and_keeps_hp() -> void:
	# Arrange
	var state := FakeState.new()
	var core := ArcadeBattle.build("cabinet_street_fighter", state, _rng(3))
	core.party[0].take_damage(5)
	core.party[0].meter = 40.0
	core.outcome = "won"
	# Act
	var result := ArcadeBattle.settle("cabinet_street_fighter", core, state)
	# Assert
	assert_eq(ArcadeRules.tickets(state), int(result["tickets"]))
	assert_gt(int(result["tickets"]), 0)
	assert_eq(int(state.party[0]["hp"]), 40)


func test_arcade_battle_settle_loss_leaves_one_hp() -> void:
	# Arrange
	var state := FakeState.new()
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(4))
	core.outcome = "lost"
	# Act
	ArcadeBattle.settle("cabinet_frogger", core, state)
	# Assert
	assert_eq(int(state.party[0]["hp"]), 1)
	assert_eq(ArcadeRules.tickets(state), 0)


func test_arcade_battle_every_villain_has_battle_data_and_engine_stats() -> void:
	# Arrange
	var ids := {}
	for cab_id in ["cabinet_frogger", "cabinet_street_fighter", "cabinet_kebab_kombat"]:
		var cab := ArcadeBattle.cabinet(cab_id)
		for r in cab.get("releases", []) + cab.get("rungs", []):
			for id in r["enemies"]:
				ids[id] = true
	# Act
	var state := FakeState.new()
	var missing := []
	for id in ids.keys():
		var u := BattleUnit.from_enemy(id, ArcadeBattle._json(ArcadeBattle.ENEMY_DATA)["enemies"].get(id, {}),
			ArcadeBattle._json(ArcadeBattle.BATTLE_DATA)["villains"].get(id, {}))
		if u.moves.is_empty() or u.max_hp <= 1 or u.ticket_reward <= 0:
			missing.append(id)
	# Assert
	assert_eq(ids.size(), 9)
	assert_eq(missing, [])


func test_arcade_battle_full_fights_finish_without_errors() -> void:
	# Arrange: autoplay many fights on every cabinet (bros always attack the first target).
	var outcomes := {}
	for cab_id in ["cabinet_frogger", "cabinet_street_fighter", "cabinet_kebab_kombat"]:
		for seed_value in 40:
			var state := FakeState.new()
			state.party = [
				{"id": "lord_pilsner", "hp": 45, "max_hp": 45, "bravado": 12, "max_bravado": 12, "offense": 8,
				 "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3, "skills": ["roast_line"]},
				{"id": "chadwick", "hp": 35, "max_hp": 35, "bravado": 20, "max_bravado": 20, "offense": 6,
				 "defense": 3, "speed": 7, "charm": 10, "luck": 6, "grit": 2, "skills": []},
				{"id": "bradley", "hp": 30, "max_hp": 30, "bravado": 14, "max_bravado": 14, "offense": 12,
				 "defense": 2, "speed": 8, "charm": 4, "luck": 5, "grit": 3, "skills": []},
			]
			state.flags[ArcadeBattle.won_flag(cab_id)] = true
			state.flags[ArcadeBattle.RUNG_FLAG] = seed_value % 3
			var core := ArcadeBattle.build(cab_id, state, _rng(seed_value))
			# Act
			var guard := 0
			while core.outcome == "" and guard < 2000:
				guard += 1
				core.step()
				core.tick(0.5)
				if core.needs_input():
					var targets := core.targetable_enemies()
					if targets.is_empty():
						core.flex()
						core.run_away()
					else:
						core.attack(targets[0])
			outcomes[core.outcome] = int(outcomes.get(core.outcome, 0)) + 1
			ArcadeBattle.settle(cab_id, core, state)
	# Assert: every fight ended.
	assert_false(outcomes.has(""), str(outcomes))
	gut.p("autoplay outcomes: %s" % outcomes)


func test_arcade_battle_soggy_pile_refunds_dip_minus_fee_on_win() -> void:
	# Arrange: Buy the Dip took 5 SOVS during the fight.
	var state := FakeState.new()
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(6))
	core.sovs_taken = 5
	state.gold = 15
	core.outcome = "won"
	# Act
	var result := ArcadeBattle.settle("cabinet_frogger", core, state)
	# Assert: 5 back, minus the 20% fee (1).
	assert_eq(int(result["refund"]), 4)
	assert_eq(state.gold, 19)


func test_arcade_battle_soggy_pile_stays_in_the_fund_on_a_loss() -> void:
	# Arrange
	var state := FakeState.new()
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(6))
	core.sovs_taken = 5
	state.gold = 15
	core.outcome = "lost"
	# Act
	ArcadeBattle.settle("cabinet_frogger", core, state)
	# Assert
	assert_eq(state.gold, 15)


func test_arcade_battle_jarmila_comes_back_one_word_longer_per_defeat() -> void:
	# Arrange: find a seed whose Street Fighter release includes Jarmila, already beaten twice.
	var state := FakeState.new()
	state.flags[ArcadeBattle.defeats_flag(BattleCore.JARMILA)] = 2
	var core: BattleCore = null
	for i in 50:
		var c := ArcadeBattle.build("cabinet_street_fighter", state, _rng(i))
		if c.enemies.any(func(e: BattleUnit) -> bool: return e.id == BattleCore.JARMILA):
			core = c
			break
	var jarmila: BattleUnit = core.enemies.filter(func(e: BattleUnit) -> bool: return e.id == BattleCore.JARMILA)[0]
	var name_before := jarmila.display_name
	# Act
	core.outcome = "won"
	ArcadeBattle.settle("cabinet_street_fighter", core, state)
	# Assert
	assert_eq(name_before, "Super Turbo Hyper Jarmila EX Plus")
	assert_eq(int(state.flags[ArcadeBattle.defeats_flag(BattleCore.JARMILA)]), 3)


func test_arcade_battle_cabinet_villains_get_half_again_hp() -> void:
	# Arrange
	var state := FakeState.new()
	var engine: Dictionary = ArcadeBattle._json(ArcadeBattle.ENEMY_DATA)["enemies"]
	# Act
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(7))
	# Assert
	for e in core.enemies:
		var base := int(engine[e.id]["max_hp"])
		assert_eq(e.max_hp, roundi(base * 1.5), e.id)
		assert_eq(e.hp, e.max_hp, e.id)
