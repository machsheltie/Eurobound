extends GutTest
## ArcadeBattle: the cabinet release tables, the Kebab Kombat ladder and settling a fight.


class FakeState:
	var sovs := 20
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
	state.sovs = 15
	core.outcome = "won"
	# Act
	var result := ArcadeBattle.settle("cabinet_frogger", core, state)
	# Assert: 5 back, minus the 20% fee (1).
	assert_eq(int(result["refund"]), 4)
	assert_eq(state.sovs, 19)


func test_arcade_battle_soggy_pile_stays_in_the_fund_on_a_loss() -> void:
	# Arrange
	var state := FakeState.new()
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(6))
	core.sovs_taken = 5
	state.sovs = 15
	core.outcome = "lost"
	# Act
	ArcadeBattle.settle("cabinet_frogger", core, state)
	# Assert
	assert_eq(state.sovs, 15)


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


func test_arcade_battle_every_villain_has_a_battle_sprite() -> void:
	# Arrange: every villain id, every Ninja palette and every Palette Swap colourway.
	var units := []
	for id: String in ArcadeBattle._json(ArcadeBattle.BATTLE_DATA)["villains"].keys():
		if id == ArcadeBattle.NINJA:
			continue  # a Ninja always has a palette; those are added below
		if ArcadeBattle._json(ArcadeBattle.BATTLE_DATA)["villains"][id].get("not_cabinet", false):
			continue  # the Taproom fights: Mirror Chad wears the leader's sprite, the Wisp has no battle art yet
		var u := BattleUnit.new()
		u.id = id
		units.append(u)
	for pal in ["garlic", "chili", "mystery_brown"]:
		var n := BattleUnit.new()
		n.id = ArcadeBattle.NINJA
		n.palette = pal
		units.append(n)
	# Act
	var missing := []
	for u: BattleUnit in units:
		for i in BattleScreen.SWAP_COLORS.size():
			var path := BattleScreen.enemy_sprite_path(u, i)
			if not ResourceLoader.exists(path):
				missing.append(path)
	# Assert
	assert_eq(missing, [])


func _ar_fight(seed_value: int) -> BattleCore:
	var state := FakeState.new()
	state.party = [
		{"id": "lord_pilsner", "hp": 45, "max_hp": 45, "bravado": 12, "max_bravado": 12, "offense": 8,
		 "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3, "skills": []},
		{"id": "bradley", "hp": 30, "max_hp": 30, "bravado": 14, "max_bravado": 14, "offense": 12,
		 "defense": 2, "speed": 8, "charm": 4, "luck": 5, "grit": 3, "skills": []},
	]
	return ArcadeBattle.build_fight([ArcadeBattle.ACCOUNTS_RECEIVABLE, ArcadeBattle.ACCOUNTS_RECEIVABLE], state, _rng(seed_value))


func test_arcade_battle_accounts_receivable_have_their_nameplates_and_own_hp() -> void:
	# Arrange / Act
	var core := _ar_fight(1)
	# Assert: ACCOUNTS and RECEIVABLE, 46 HP each (the cabinet +50% doesn't apply).
	assert_eq(core.enemies.map(func(e: BattleUnit) -> String: return e.display_name), ["ACCOUNTS", "RECEIVABLE"])
	assert_eq(core.enemies.map(func(e: BattleUnit) -> int: return e.max_hp), [46, 46])


func test_arcade_battle_past_due_always_targets_pilsner_while_he_stands() -> void:
	# Arrange
	var core := _ar_fight(2)
	var past_due: Dictionary = core.enemies[0].moves.filter(func(m: Dictionary) -> bool: return m["id"] == "past_due")[0]
	# Act
	var targets := core._move_targets(core.enemies[0], past_due)
	# Assert
	assert_eq(targets[0].id, "lord_pilsner")


func test_arcade_battle_survivor_gets_two_offense_when_his_colleague_clocks_out() -> void:
	# Arrange
	var core := _ar_fight(3)
	var survivor: BattleUnit = core.enemies[1]
	var before := survivor.offense
	# Act
	core.enemies[0].take_damage(999)
	core._enemy_down(core.enemies[0], core.party[0])
	# Assert
	assert_eq(survivor.phase, 2)
	assert_eq(survivor.offense, before + 2)


func test_arcade_battle_pincer_hits_with_both_enforcers() -> void:
	# Arrange
	var core := _ar_fight(4)
	var pincer: Dictionary = core.enemies[0].moves.filter(func(m: Dictionary) -> bool: return m["id"] == "matching_polo_pincer")[0]
	var hp_before := 0
	for b in core.party:
		hp_before += b.hp
	# Act
	core._resolve(core.enemies[0], pincer)
	# Assert: two hits landed on one bro (log has two damage lines or the bro lost HP twice).
	var hp_after := 0
	for b in core.party:
		hp_after += b.hp
	assert_lt(hp_after, hp_before)
	assert_eq(core.enemies[0].moves.filter(func(m: Dictionary) -> bool: return m.get("special", "") == "pincer").size(), 1)


func test_arcade_battle_grease_fingers_always_lands_on_accounts_receivable() -> void:
	# Arrange
	var core := _ar_fight(5)
	# Act: a 1% chance still lands.
	var landed := core._apply_status(core.enemies[0], "grease_fingers", 2, 0.01)
	# Assert
	assert_true(landed)
