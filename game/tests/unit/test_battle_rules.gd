extends GutTest
## The approved round v26 battle numbers (battle_numbers_proposal.md, all ef3_ items approved).


func test_battle_rules_tier_pilsner_bravado_splits_at_thirds() -> void:
	# Arrange: Pilsner's max Bravado is 12, so Low 0-3, Mid 4-7, High 8-12.
	var max_bravado := 12
	# Act
	var tiers := []
	for b in [0, 3, 4, 7, 8, 12]:
		tiers.append(BattleRules.tier(b, max_bravado))
	# Assert
	assert_eq(tiers, ["low", "low", "mid", "mid", "high", "high"])


func test_battle_rules_modifier_each_tier_returns_approved_bonus() -> void:
	# Arrange / Act
	var high := BattleRules.modifier(12, 12)
	var mid := BattleRules.modifier(5, 12)
	var low := BattleRules.modifier(1, 12)
	var chadwick_high := BattleRules.modifier(20, 20)
	var enemy := BattleRules.modifier(0, 0)
	# Assert
	assert_eq([high, mid, low, chadwick_high, enemy], [6, 3, -2, 10, 0])


func test_battle_rules_damage_against_croc_matches_sanity_check() -> void:
	# Arrange: Croc Monsieur Def 6, all three bros at High Bravado (proposal: ~8 / ~13 / ~10).
	var croc_def := 6
	# Act
	var pilsner := BattleRules.damage(8, BattleRules.modifier(12, 12), croc_def, 1.0, 0)
	var bradley := BattleRules.damage(12, BattleRules.modifier(14, 14), croc_def, 1.0, 0)
	var chadwick := BattleRules.damage(6, BattleRules.modifier(20, 20), croc_def, 1.0, 0)
	# Assert
	assert_eq([pilsner, bradley, chadwick], [8, 13, 10])


func test_battle_rules_damage_spread_applies_and_floor_is_one() -> void:
	# Arrange / Act
	var high_roll := BattleRules.damage(8, 6, 6, 1.0, 2)
	var low_roll := BattleRules.damage(8, 6, 6, 1.0, -2)
	var hopeless := BattleRules.damage(1, -2, 9, 1.0, -2)
	# Assert
	assert_eq([high_roll, low_roll, hopeless], [10, 6, 1])


func test_battle_rules_damage_roast_line_multiplier_rounds() -> void:
	# Arrange: Roast Line x1.8 at High; (8 + 6 - 6) * 1.8 = 14.4.
	# Act
	var dmg := BattleRules.damage(8, 6, 6, 1.8, 0)
	# Assert
	assert_eq(dmg, 14)


func test_battle_rules_crit_pct_high_bravado_and_grit_and_floor() -> void:
	# Arrange / Act
	var high := BattleRules.crit_pct(4, true, 3)
	var normal := BattleRules.crit_pct(4, false, 3)
	var floored := BattleRules.crit_pct(1, false, 9)
	# Assert
	assert_eq([high, normal, floored], [12.5, 2.5, 1.0])


func test_battle_rules_speed_bravado_tier_shifts_by_two() -> void:
	# Arrange / Act
	var speeds := [BattleRules.speed(5, "high"), BattleRules.speed(5, "mid"), BattleRules.speed(5, "low")]
	# Assert
	assert_eq(speeds, [7, 5, 3])


func test_battle_rules_run_pct_scales_with_speed_and_clamps() -> void:
	# Arrange / Act
	var even := BattleRules.run_pct(7.0, 7.0)
	var faster := BattleRules.run_pct(8.0, 6.0)
	var floor_pct := BattleRules.run_pct(3.0, 20.0)
	var ceiling := BattleRules.run_pct(20.0, 3.0)
	# Assert
	assert_eq([even, faster, floor_pct, ceiling], [50.0, 60.0, 10.0, 90.0])
