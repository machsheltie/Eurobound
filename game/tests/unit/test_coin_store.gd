extends GutTest
## Economy Phase 0b (Eurobound-1g9t): the non-SOVS coin store on GameState.
## Shape ruled by the author on Eurobound-cyb6 (2026-11-13): bagholder_assets is a
## Dictionary of coin_id -> quantity held. It lives in flags under the registry key
## (quest_flags.json, design/economy/economy_system.md §8.2), like economy_seed.
## Coin ids and amounts here are test fixtures only, not game coins or payloads.

const COIN_A := "fixture_coin_a"
const COIN_B := "fixture_coin_b"

var repo
var state

func before_each() -> void:
	repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load("res://core/game_state.gd").new())
	state.new_game(repo)

func _fresh_state():
	return autofree(load("res://core/game_state.gd").new())

# --- read helpers ---

func test_coin_store_new_game_holds_nothing() -> void:
	# Arrange / Act: before_each started a new game.
	# Assert
	assert_eq(state.bagholder_assets(), {}, "registry default is {}")
	assert_eq(state.coin_quantity(COIN_A), 0)

func test_coin_store_quantity_of_unheld_coin_is_zero() -> void:
	state.deposit_coin(COIN_A, 5)
	assert_eq(state.coin_quantity(COIN_B), 0)

func test_coin_store_read_returns_copy_not_live_store() -> void:
	state.deposit_coin(COIN_A, 5)
	var snapshot: Dictionary = state.bagholder_assets()
	snapshot[COIN_A] = 999
	snapshot[COIN_B] = 1
	assert_eq(state.coin_quantity(COIN_A), 5, "editing the returned copy must not change holdings")
	assert_eq(state.coin_quantity(COIN_B), 0)

# --- deposit_coin ---

func test_coin_store_deposit_records_quantity_under_coin_id() -> void:
	state.deposit_coin(COIN_A, 250000)
	assert_eq(state.coin_quantity(COIN_A), 250000)
	assert_eq(state.bagholder_assets(), {COIN_A: 250000})

func test_coin_store_deposit_same_coin_twice_adds_up() -> void:
	state.deposit_coin(COIN_A, 100)
	state.deposit_coin(COIN_A, 23)
	assert_eq(state.coin_quantity(COIN_A), 123)
	assert_eq(state.bagholder_assets().size(), 1, "one entry per coin_id")

func test_coin_store_deposit_keeps_coins_separate() -> void:
	state.deposit_coin(COIN_A, 100)
	state.deposit_coin(COIN_B, 7)
	assert_eq(state.bagholder_assets(), {COIN_A: 100, COIN_B: 7})

func test_coin_store_deposit_lives_in_flags_registry_key() -> void:
	state.deposit_coin(COIN_A, 100)
	assert_eq(state.flags.get("bagholder_assets"), {COIN_A: 100})

func test_coin_store_deposit_ignores_zero_and_negative_amounts() -> void:
	state.deposit_coin(COIN_A, 10)
	state.deposit_coin(COIN_A, 0)
	state.deposit_coin(COIN_A, -4)
	state.deposit_coin(COIN_B, 0)
	assert_eq(state.bagholder_assets(), {COIN_A: 10}, "a deposit never drains and never adds an empty entry")

func test_coin_store_deposit_ignores_empty_coin_id() -> void:
	state.deposit_coin("", 10)
	assert_eq(state.bagholder_assets(), {})

func test_coin_store_deposit_leaves_sovs_untouched() -> void:
	state.sovs = 50
	state.deposit_coin(COIN_A, 100)
	assert_eq(state.sovs, 50, "non-SOVS coins are not SOVS")

# --- save/load ---

func test_coin_store_round_trip_keeps_holdings() -> void:
	state.deposit_coin(COIN_A, 250000)
	state.deposit_coin(COIN_B, 7)
	var d: Dictionary = state.to_dict()
	var restored = _fresh_state()
	restored.from_dict(d)
	assert_eq(restored.bagholder_assets(), {COIN_A: 250000, COIN_B: 7})
	assert_eq(restored.to_dict(), d)

func test_coin_store_to_dict_is_detached_from_live_state() -> void:
	state.deposit_coin(COIN_A, 5)
	var d: Dictionary = state.to_dict()
	state.deposit_coin(COIN_A, 5)
	assert_eq(d["flags"]["bagholder_assets"], {COIN_A: 5})

func test_coin_store_json_round_trip_restores_int_quantities() -> void:
	# SaveSystem writes JSON; JSON numbers come back as floats.
	state.deposit_coin(COIN_A, 250000)
	var parsed: Dictionary = JSON.parse_string(JSON.stringify(state.to_dict()))
	var restored = _fresh_state()
	restored.from_dict(parsed)
	assert_eq(typeof(restored.bagholder_assets()[COIN_A]), TYPE_INT)
	assert_eq(restored.coin_quantity(COIN_A), 250000)
	restored.deposit_coin(COIN_A, 1)
	assert_eq(restored.coin_quantity(COIN_A), 250001)

func test_coin_store_load_of_save_without_store_holds_nothing() -> void:
	var d: Dictionary = state.to_dict()
	d["flags"].erase("bagholder_assets")
	var restored = _fresh_state()
	restored.from_dict(d)
	assert_eq(restored.bagholder_assets(), {})
	restored.deposit_coin(COIN_A, 3)
	assert_eq(restored.coin_quantity(COIN_A), 3)

func test_coin_store_load_of_malformed_store_holds_nothing() -> void:
	var d: Dictionary = state.to_dict()
	d["flags"]["bagholder_assets"] = "not a dictionary"
	var restored = _fresh_state()
	restored.from_dict(d)
	assert_eq(restored.bagholder_assets(), {})
	assert_eq(restored.coin_quantity(COIN_A), 0)

func test_coin_store_new_game_clears_previous_holdings() -> void:
	state.deposit_coin(COIN_A, 100)
	state.new_game(repo)
	assert_eq(state.bagholder_assets(), {})
