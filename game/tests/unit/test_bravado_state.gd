extends GutTest

func test_zero_band() -> void:
	assert_eq(GameState.bravado_state(0), "zero")

func test_low_band() -> void:
	assert_eq(GameState.bravado_state(1), "low")
	assert_eq(GameState.bravado_state(25), "low")

func test_mid_band() -> void:
	assert_eq(GameState.bravado_state(26), "mid")
	assert_eq(GameState.bravado_state(70), "mid")

func test_high_band() -> void:
	assert_eq(GameState.bravado_state(71), "high")
	assert_eq(GameState.bravado_state(100), "high")

func test_ultimate_locked_at_zero_and_low() -> void:
	assert_false(GameState.can_use_ultimate(0))
	assert_false(GameState.can_use_ultimate(25))

func test_ultimate_unlocked_at_mid_and_high() -> void:
	assert_true(GameState.can_use_ultimate(26))
	assert_true(GameState.can_use_ultimate(100))
