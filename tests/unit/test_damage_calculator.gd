extends GutTest

func _rng(seed_value: int) -> RandomNumberGenerator:
	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value
	return rng

func test_damage_is_at_least_one() -> void:
	var weak := {"offense": 1, "luck": 0}
	var tank := {"defense": 99}
	for i in range(20):
		var result := DamageCalculator.compute(weak, tank, _rng(i))
		assert_gt(int(result["damage"]), 0)

func test_damage_scales_with_offense() -> void:
	var rng_a := _rng(42)
	var rng_b := _rng(42)
	var low := DamageCalculator.compute({"offense": 4, "luck": 0}, {"defense": 2}, rng_a)
	var high := DamageCalculator.compute({"offense": 10, "luck": 0}, {"defense": 2}, rng_b)
	assert_gt(int(high["damage"]), int(low["damage"]))

func test_multiplier_increases_damage() -> void:
	var base := DamageCalculator.compute({"offense": 8, "luck": 0}, {"defense": 3}, _rng(7), 1.0)
	var boosted := DamageCalculator.compute({"offense": 8, "luck": 0}, {"defense": 3}, _rng(7), 1.8)
	assert_gt(int(boosted["damage"]), int(base["damage"]))

func test_zero_luck_never_crits() -> void:
	for i in range(50):
		var result := DamageCalculator.compute({"offense": 5, "luck": 0}, {"defense": 1}, _rng(i))
		assert_false(result["crit"])

func test_max_luck_always_crits() -> void:
	for i in range(50):
		var result := DamageCalculator.compute({"offense": 5, "luck": 100}, {"defense": 1}, _rng(i))
		assert_true(result["crit"])
