extends GutTest
## PrizeShop: the Prize Redemption counter trades tickets for the catalogue and the junk shelf.
## Catalogue prizes are one each; junk-shelf prizes can be bought again.

const RING := "aa_junk_promise_ish_ring"          # junk shelf, 5 tickets
const PUCKER := "aa_prize_paraffin_pucker"        # catalogue, 15 tickets


class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _shop(tickets: int) -> PrizeShop:
	var s := FakeState.new()
	if tickets > 0:
		s.inventory[ArcadeRules.TICKET_ID] = tickets
	var shop := PrizeShop.new()
	shop.setup(s)
	add_child_autoqfree(shop)
	return shop


func _point_at(shop: PrizeShop, id: String) -> void:
	for i in shop.rows.size():
		if shop.rows[i]["id"] == id:
			shop.cursor = i
			return
	fail_test("%s is not on the shelf" % id)


func test_prize_shop_stock_lists_catalogue_then_junk_each_cheapest_first() -> void:
	# Act
	var rows := PrizeShop.stock()
	# Assert
	assert_gt(rows.size(), 0)
	var first_junk := rows.size()
	for i in rows.size():
		if rows[i]["junk"]:
			first_junk = i
			break
	for i in rows.size():
		assert_eq(bool(rows[i]["junk"]), i >= first_junk, "catalogue before junk: %s" % rows[i]["id"])
		if i > 0 and rows[i]["junk"] == rows[i - 1]["junk"]:
			assert_true(int(rows[i - 1]["price"]) <= int(rows[i]["price"]), "cheapest first: %s" % rows[i]["id"])
	assert_true(rows.any(func(r: Dictionary) -> bool: return r["id"] == RING and r["junk"]))
	assert_true(rows.any(func(r: Dictionary) -> bool: return r["id"] == PUCKER and not r["junk"]))


func test_prize_shop_buying_spends_tickets_and_gives_the_prize() -> void:
	# Arrange
	var shop := _shop(20)
	_point_at(shop, PUCKER)
	# Act
	var ok := shop.buy()
	# Assert
	assert_true(ok)
	assert_eq(ArcadeRules.tickets(shop.state), 5)
	assert_eq(int(shop.state.inventory.get(PUCKER, 0)), 1)
	assert_eq(shop.bought, [PUCKER])
	assert_eq(shop.notice, "")


func test_prize_shop_insufficient_tickets_buys_nothing_and_says_so() -> void:
	# Arrange
	var shop := _shop(14)
	_point_at(shop, PUCKER)
	# Act
	var ok := shop.buy()
	# Assert
	assert_false(ok)
	assert_eq(shop.notice, "NOT ENOUGH TICKETS")
	assert_eq(ArcadeRules.tickets(shop.state), 14)
	assert_false(shop.state.inventory.has(PUCKER))
	assert_eq(shop.bought, [])


func test_prize_shop_no_tickets_at_all_buys_nothing() -> void:
	# Arrange
	var shop := _shop(0)
	_point_at(shop, RING)
	# Act
	shop.press("interact")
	# Assert
	assert_eq(shop.notice, "NOT ENOUGH TICKETS")
	assert_false(shop.state.inventory.has(RING))


func test_prize_shop_exact_price_spends_the_last_ticket() -> void:
	# Arrange
	var shop := _shop(5)
	_point_at(shop, RING)
	# Act
	shop.press("interact")
	# Assert
	assert_eq(ArcadeRules.tickets(shop.state), 0)
	assert_false(shop.state.inventory.has(ArcadeRules.TICKET_ID), "an empty ticket slot is removed")
	assert_eq(int(shop.state.inventory.get(RING, 0)), 1)


func test_prize_shop_catalogue_prize_is_one_each() -> void:
	# Arrange
	var shop := _shop(100)
	_point_at(shop, PUCKER)
	shop.buy()
	# Act
	var again := shop.buy()
	# Assert
	assert_false(again)
	assert_true(shop.owned(shop.rows[shop.cursor]))
	assert_eq(int(shop.state.inventory[PUCKER]), 1)
	assert_eq(ArcadeRules.tickets(shop.state), 85)


func test_prize_shop_junk_shelf_can_be_bought_again() -> void:
	# Arrange
	var shop := _shop(12)
	_point_at(shop, RING)
	# Act
	shop.press("interact")
	shop.press("interact")
	# Assert
	assert_eq(int(shop.state.inventory[RING]), 2)
	assert_false(shop.owned(shop.rows[shop.cursor]))
	assert_eq(ArcadeRules.tickets(shop.state), 2)
	assert_eq(shop.bought, [RING, RING])


func test_prize_shop_cursor_wraps_both_ways() -> void:
	# Arrange
	var shop := _shop(0)
	# Act
	shop.press("move_up")
	var from_top := shop.cursor
	shop.press("move_down")
	var back := shop.cursor
	# Assert
	assert_eq(from_top, shop.rows.size() - 1)
	assert_eq(back, 0)


func test_prize_shop_moving_clears_the_notice() -> void:
	# Arrange
	var shop := _shop(0)
	shop.press("interact")
	# Act
	shop.press("move_down")
	# Assert
	assert_eq(shop.notice, "")


func test_prize_shop_cancel_reports_what_was_bought_and_closes() -> void:
	# Arrange
	var shop := _shop(10)
	_point_at(shop, RING)
	shop.press("interact")
	watch_signals(shop)
	# Act
	shop.press("cancel")
	# Assert
	assert_signal_emitted_with_parameters(shop, "closed", [[RING]])
	assert_true(shop.is_queued_for_deletion())
