extends GutTest
## ArcadeMicrocopy: the approved Token Attendant mutters and DDR EXPERT lines load verbatim.


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func test_arcade_microcopy_every_job_has_six_mutters() -> void:
	# Arrange
	var jobs := ["ticket_machine", "token_machine", "restrooms", "claw_machines", "shift"]
	# Act
	var sizes := jobs.map(func(j: String) -> int: return ArcadeMicrocopy.mutter_pool(j).size())
	# Assert
	assert_eq(sizes, [6, 6, 6, 6, 6])


func test_arcade_microcopy_late_night_adds_the_five_drunk_lines() -> void:
	# Arrange
	var sober := ArcadeMicrocopy.mutter_pool("shift")
	# Act
	var late := ArcadeMicrocopy.mutter_pool("shift", true)
	# Assert
	assert_eq(late.size(), sober.size() + 5)
	assert_has(late, "Floor's tilting north. Good. Gravity does the mopping.")


func test_arcade_microcopy_mutter_never_repeats_back_to_back() -> void:
	# Arrange
	var last := ""
	var repeats := 0
	# Act
	for i in 200:
		var line := ArcadeMicrocopy.mutter("claw_machines", false, _rng(i), last)
		if line == last:
			repeats += 1
		last = line
	# Assert
	assert_eq(repeats, 0)


func test_arcade_microcopy_ddr_lines_for_every_bro() -> void:
	# Arrange
	var bros := ["lord_pilsner", "chadwick", "bradley"]
	# Act
	var missing := []
	for b: String in bros:
		for moment: String in ["difficulty_bounce", "failed_expert_song"]:
			if ArcadeMicrocopy.ddr_line(moment, b, _rng(1)).is_empty():
				missing.append("%s/%s" % [b, moment])
	# Assert
	assert_eq(missing, [])
