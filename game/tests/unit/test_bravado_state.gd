extends GutTest
## Bravado bands are percent-of-max (author ruling, 2026-08-06), not absolute values —
## max_bravado varies per party member (Lord Pilsner's is 12), so an absolute band
## would permanently lock some characters out of their own Ultimate. These tests
## prove the percentage math at two different maxes to show it's scale-independent.

## --- max_bravado = 12 (Lord Pilsner's actual value) ---
## 0 -> zero, 1-3 -> low, 4-8 -> mid, 9-12 -> high

func test_zero_band_at_max_12() -> void:
	assert_eq(GameState.bravado_state(0, 12), "zero")

func test_low_band_at_max_12() -> void:
	assert_eq(GameState.bravado_state(1, 12), "low")
	assert_eq(GameState.bravado_state(3, 12), "low")

func test_mid_band_at_max_12() -> void:
	assert_eq(GameState.bravado_state(4, 12), "mid")
	assert_eq(GameState.bravado_state(8, 12), "mid")

func test_high_band_at_max_12() -> void:
	assert_eq(GameState.bravado_state(9, 12), "high")
	assert_eq(GameState.bravado_state(12, 12), "high")

func test_ultimate_locked_at_zero_and_low_max_12() -> void:
	assert_false(GameState.can_use_ultimate(0, 12))
	assert_false(GameState.can_use_ultimate(3, 12))

func test_ultimate_unlocked_at_mid_and_high_max_12() -> void:
	assert_true(GameState.can_use_ultimate(4, 12))
	assert_true(GameState.can_use_ultimate(12, 12))

## --- max_bravado = 100 (proves scale-independence: same percentages, different max) ---
## 0 -> zero, 1-25 -> low, 26-70 -> mid, 71-100 -> high

func test_zero_band_at_max_100() -> void:
	assert_eq(GameState.bravado_state(0, 100), "zero")

func test_low_band_at_max_100() -> void:
	assert_eq(GameState.bravado_state(1, 100), "low")
	assert_eq(GameState.bravado_state(25, 100), "low")

func test_mid_band_at_max_100() -> void:
	assert_eq(GameState.bravado_state(26, 100), "mid")
	assert_eq(GameState.bravado_state(70, 100), "mid")

func test_high_band_at_max_100() -> void:
	assert_eq(GameState.bravado_state(71, 100), "high")
	assert_eq(GameState.bravado_state(100, 100), "high")

func test_ultimate_locked_at_zero_and_low_max_100() -> void:
	assert_false(GameState.can_use_ultimate(0, 100))
	assert_false(GameState.can_use_ultimate(25, 100))

func test_ultimate_unlocked_at_mid_and_high_max_100() -> void:
	assert_true(GameState.can_use_ultimate(26, 100))
	assert_true(GameState.can_use_ultimate(100, 100))

## --- max <= 0 guard (division-by-zero safety) ---

func test_zero_max_does_not_divide_by_zero() -> void:
	assert_eq(GameState.bravado_state(0, 0), "zero")
	assert_eq(GameState.bravado_state(5, 0), "zero")
	assert_eq(GameState.bravado_state(5, -1), "zero")

## --- fixture-ability gating test (spec §4: prove the is_ultimate gating mechanism
## without inventing real Ultimate content) ---
## This mirrors the exact gating check in battle_manager.gd's _on_roast(): an
## ability is refused only when it is flagged is_ultimate AND the band forbids it.

func test_fixture_ultimate_ability_is_refused_at_low_band() -> void:
	var fixture_ability := {
		"display_name": "Fixture Ultimate",
		"bravado_cost": 5,
		"power_multiplier": 2.0,
		"battle_text": "{user} does the fixture thing!",
		"is_ultimate": true,
	}
	var bravado := 3 # low band at max 12
	var max_bravado := 12
	var refused := bool(fixture_ability.get("is_ultimate", false)) \
		and not GameState.can_use_ultimate(bravado, max_bravado)
	assert_true(refused, "Ultimate-flagged ability must be refused in the low band")

func test_fixture_ultimate_ability_is_allowed_at_mid_band() -> void:
	var fixture_ability := {
		"display_name": "Fixture Ultimate",
		"bravado_cost": 5,
		"power_multiplier": 2.0,
		"battle_text": "{user} does the fixture thing!",
		"is_ultimate": true,
	}
	var bravado := 6 # mid band at max 12
	var max_bravado := 12
	var refused := bool(fixture_ability.get("is_ultimate", false)) \
		and not GameState.can_use_ultimate(bravado, max_bravado)
	assert_false(refused, "Ultimate-flagged ability must be allowed in the mid band")

func test_fixture_non_ultimate_ability_is_never_gated() -> void:
	var fixture_ability := {
		"display_name": "Fixture Ordinary Special",
		"bravado_cost": 3,
		"power_multiplier": 1.2,
		"battle_text": "{user} does the ordinary fixture thing.",
		"is_ultimate": false,
	}
	var bravado := 0 # zero band — would refuse an Ultimate, but this isn't one
	var max_bravado := 12
	var refused := bool(fixture_ability.get("is_ultimate", false)) \
		and not GameState.can_use_ultimate(bravado, max_bravado)
	assert_false(refused, "Non-Ultimate abilities are never gated by Bravado band")
