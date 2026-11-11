extends GutTest
## ArcadeRules: Absinthe Arcade tokens and cabinet plays. Rulings 2026-11-09 (1 token = 1 SOV;
## Frogger 2 tokens, Street Fighter 3, Kebab Kombat 4, DDR 2 per song) and ef_tokens =
## machine_any, 2026-11-10 (the machine sells any number; tokens sit in the inventory).

const GameStateScript := preload("res://core/game_state.gd")


func _state(sovs: int, tokens := 0) -> Node:
	var s: Node = GameStateScript.new()
	autofree(s)
	s.sovs = sovs
	if tokens > 0:
		s.add_item(ArcadeRules.TOKEN_ID, tokens)
	return s


func test_arcade_rules_cabinet_costs_match_the_rulings() -> void:
	assert_eq(ArcadeRules.play_cost("cabinet_frogger"), 2)
	assert_eq(ArcadeRules.play_cost("cabinet_street_fighter"), 3)
	assert_eq(ArcadeRules.play_cost("cabinet_kebab_kombat"), 4)
	assert_eq(ArcadeRules.play_cost("ddr_dance_off"), 2)


func test_arcade_rules_buying_tokens_spends_one_sovs_each() -> void:
	# Arrange
	var s := _state(10)

	# Act
	var ok := ArcadeRules.buy_tokens(s, 7)

	# Assert
	assert_true(ok)
	assert_eq(s.sovs, 3)
	assert_eq(ArcadeRules.tokens(s), 7)


func test_arcade_rules_cannot_buy_more_than_the_wallet_covers() -> void:
	# Arrange
	var s := _state(4)

	# Act
	var ok := ArcadeRules.buy_tokens(s, 5)

	# Assert
	assert_false(ok)
	assert_eq(s.sovs, 4)
	assert_eq(ArcadeRules.tokens(s), 0)
	assert_eq(ArcadeRules.max_buyable(s), 4)


func test_arcade_rules_playing_spends_the_tokens() -> void:
	# Arrange
	var s := _state(0, 5)

	# Act
	var ok := ArcadeRules.pay_for_play(s, "cabinet_street_fighter")

	# Assert
	assert_true(ok)
	assert_eq(ArcadeRules.tokens(s), 2)


func test_arcade_rules_short_of_tokens_plays_nothing() -> void:
	# Arrange: SOVS in the wallet don't count, only tokens
	var s := _state(50, 3)

	# Act
	var ok := ArcadeRules.pay_for_play(s, "cabinet_kebab_kombat")

	# Assert
	assert_false(ok)
	assert_eq(ArcadeRules.tokens(s), 3)
	assert_eq(s.sovs, 50)


func test_arcade_rules_spending_the_last_token_empties_the_slot() -> void:
	# Arrange
	var s := _state(0, 2)

	# Act
	ArcadeRules.pay_for_play(s, "cabinet_frogger")

	# Assert
	assert_false(s.inventory.has(ArcadeRules.TOKEN_ID))


func test_arcade_rules_tickets_add_up() -> void:
	# Arrange
	var s := _state(0)

	# Act
	ArcadeRules.add_tickets(s, 8)
	ArcadeRules.add_tickets(s, 15)

	# Assert
	assert_eq(ArcadeRules.tickets(s), 23)


func test_arcade_money_reads_1_sov_and_2_sovs() -> void:
	assert_eq(ArcadeOverlay.sovs_text(1), "1 SOV")
	assert_eq(ArcadeOverlay.sovs_text(2), "2 SOVS")
