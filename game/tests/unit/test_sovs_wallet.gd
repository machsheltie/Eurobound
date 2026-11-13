extends GutTest
## Economy Phase 0 (Eurobound-jvwg): the SOVS wallet core API on GameState.
## Rules: design/economy/economy_system.md §1.4 (no friction on SOVS purchases),
## §8.1-8.2 (economy_seed), §8.4 (purchase path exposes no fee, pending or failure field).
## Amounts here are test fixtures only, not game prices.

var repo
var state

func before_each() -> void:
	repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load("res://core/game_state.gd").new())
	state.new_game(repo)

func _fresh_state():
	return autofree(load("res://core/game_state.gd").new())

# --- can_afford ---

func test_can_afford_at_or_below_balance() -> void:
	state.sovs = 50
	assert_true(state.can_afford(0))
	assert_true(state.can_afford(49))
	assert_true(state.can_afford(50), "exact balance is affordable")

func test_cannot_afford_above_balance() -> void:
	state.sovs = 50
	assert_false(state.can_afford(51))

func test_cannot_afford_negative_amount() -> void:
	state.sovs = 50
	assert_false(state.can_afford(-1), "a negative price is a caller bug, never affordable")

# --- spend_sovs ---

func test_spend_deducts_and_returns_true() -> void:
	state.sovs = 50
	assert_true(state.spend_sovs(30))
	assert_eq(state.sovs, 20)

func test_spend_exact_balance_leaves_zero() -> void:
	state.sovs = 50
	assert_true(state.spend_sovs(50))
	assert_eq(state.sovs, 0)

func test_spend_refuses_when_short() -> void:
	state.sovs = 10
	assert_false(state.spend_sovs(11))
	assert_eq(state.sovs, 10, "a refused spend takes nothing")

func test_spend_refuses_negative_amount() -> void:
	state.sovs = 10
	assert_false(state.spend_sovs(-5))
	assert_eq(state.sovs, 10, "a negative spend must not mint SOVS")

# --- grant_sovs ---

func test_grant_adds() -> void:
	state.sovs = 10
	state.grant_sovs(15)
	assert_eq(state.sovs, 25)

func test_grant_ignores_negative_amount() -> void:
	state.sovs = 10
	state.grant_sovs(-4)
	assert_eq(state.sovs, 10, "a negative grant must not drain the wallet")

func test_grant_rewards_routes_through_grant_sovs() -> void:
	state.sovs = 10
	state.grant_rewards(0, 5, "")
	assert_eq(state.sovs, 15)

# --- purchase_sovs: select, pay, done (§1.4, §8.4) ---

func test_purchase_deducts_price_and_grants_item() -> void:
	state.sovs = 50
	state.purchase_sovs("lukewarm_kebab", 20)
	assert_eq(state.sovs, 30)
	assert_eq(int(state.inventory.get("lukewarm_kebab", 0)), 1)

func test_purchase_count_and_stack_cap() -> void:
	state.sovs = 50
	state.purchase_sovs("lukewarm_kebab", 10, 3, 2)
	assert_eq(state.sovs, 40, "one price paid for the row")
	assert_eq(int(state.inventory.get("lukewarm_kebab", 0)), 2, "max_stack caps what is carried")

func test_purchase_returns_nothing() -> void:
	state.sovs = 50
	var result = state.purchase_sovs("lukewarm_kebab", 20)
	assert_null(result, "§8.4: no failure return, fee field or pending state")

func test_purchase_has_no_return_type() -> void:
	for m in state.get_method_list():
		if m["name"] == "purchase_sovs":
			assert_eq(int(m["return"]["type"]), TYPE_NIL, "purchase_sovs is declared -> void")
			return
	fail_test("purchase_sovs not found on GameState")

func test_purchase_when_unaffordable_changes_nothing() -> void:
	# The shop must check can_afford and show its cannot-afford notice first (Phase 1).
	state.sovs = 5
	state.purchase_sovs("lukewarm_kebab", 20)
	assert_eq(state.sovs, 5)
	assert_false(state.inventory.has("lukewarm_kebab"))

# --- economy_seed (§8.1-8.2) ---

func test_new_game_generates_economy_seed() -> void:
	assert_ne(state.economy_seed(), 0, "0 is the registry default meaning 'not generated'")

func test_economy_seed_lives_in_flags_registry_key() -> void:
	assert_eq(int(state.flags.get("economy_seed", 0)), state.economy_seed())

func test_new_games_get_independent_seeds() -> void:
	var seeds := {}
	for i in 5:
		var s = _fresh_state()
		s.new_game(repo)
		seeds[s.economy_seed()] = true
	assert_gt(seeds.size(), 1, "each new game rolls its own seed")

func test_economy_seed_survives_round_trip_unchanged() -> void:
	var seed_value: int = state.economy_seed()
	var restored = _fresh_state()
	restored.from_dict(state.to_dict())
	assert_eq(restored.economy_seed(), seed_value, "never regenerated on load")

func test_load_of_save_without_seed_generates_one_once() -> void:
	var d: Dictionary = state.to_dict()
	d["flags"] = {}
	var restored = _fresh_state()
	restored.from_dict(d)
	var seed_value: int = restored.economy_seed()
	assert_ne(seed_value, 0)
	var again = _fresh_state()
	again.from_dict(restored.to_dict())
	assert_eq(again.economy_seed(), seed_value)

# --- save/load ---

func test_wallet_round_trip() -> void:
	state.sovs = 0
	state.grant_sovs(77)
	state.spend_sovs(7)
	state.purchase_sovs("lukewarm_kebab", 10)
	var d: Dictionary = state.to_dict()
	var restored = _fresh_state()
	restored.from_dict(d)
	assert_eq(restored.sovs, 60)
	assert_eq(int(restored.inventory.get("lukewarm_kebab", 0)), 1)
	assert_eq(restored.economy_seed(), state.economy_seed())
	assert_eq(restored.to_dict(), d)

func test_legacy_gold_key_still_read() -> void:
	var d: Dictionary = state.to_dict()
	d.erase("sovs")
	d["gold"] = 42
	var restored = _fresh_state()
	restored.from_dict(d)
	assert_eq(restored.sovs, 42)
	assert_true(restored.spend_sovs(42))
	assert_eq(restored.sovs, 0)
