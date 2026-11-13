extends GutTest
## Economy Phase 1 (Eurobound-it49): the data-driven SOVS shop (ShopCatalog + SovsShop).
## Rules: economy_system.md §1.3 ("40 SOVS", "1 SOV"), §1.4 (select, pay, done), §8.4 (no fee row),
## currency.md (the 1-SOV floor). Every shop, item price and count here is a TEST FIXTURE, not
## game stock: the first shop, its stock and prices wait on the author (Eurobound Desk).

const FIXTURE := "res://tests/fixtures/shops/shops_fixture.json"

var state


func before_each() -> void:
	var repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load("res://core/game_state.gd").new())
	state.new_game(repo)


func _items() -> Dictionary:
	return {
		"kebab": {"display_name": "Fixture Kebab"},
		"shot": {"display_name": "Fixture Shot"},
		"coupon": {"display_name": "Fixture Coupon", "max_stack": 2},
		"goulash": {"display_name": "Fixture Goulash"},
	}


func _doc(stock: Array, extra := {}) -> Dictionary:
	var shop := {"display_name": "Test Shop", "currency": "SOVS", "stock": stock}
	shop.merge(extra, true)
	return {"schema_version": "1.0", "shops": {"test_shop": shop}}


func _stock() -> Array:
	return [
		{"item_id": "kebab", "price": 20.0},
		{"item_id": "shot", "price": 1.0, "count": 2.0},
		{"item_id": "coupon", "price": 3.0},
		{"item_id": "goulash", "price": null},
	]


func _shop(doc: Dictionary) -> SovsShop:
	var s := SovsShop.new()
	s.setup(state, "test_shop", doc, _items())
	add_child_autofree(s)
	return s


# --- ShopCatalog: schema ---

func test_shop_catalog_fixture_file_loads_and_validates() -> void:
	# Arrange
	var items := ShopCatalog.item_tables()
	# Act
	var doc := ShopCatalog.load_doc(FIXTURE)
	# Assert
	assert_true(doc.get("shops", {}).has("fixture_shop"))
	assert_eq(ShopCatalog.errors(doc, items), [])


func test_shop_catalog_shipped_shops_json_validates() -> void:
	# Arrange
	var items := ShopCatalog.item_tables()
	# Act
	var doc := ShopCatalog.load_doc()
	# Assert: whatever the author has ruled in (or nothing yet), the shipped file is valid.
	assert_true(doc.get("shops") is Dictionary, "Shops.json carries a shops object")
	assert_eq(ShopCatalog.errors(doc, items), [])


func test_shop_catalog_valid_doc_has_no_errors() -> void:
	# Arrange
	var doc := _doc(_stock())
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs, [])


func test_shop_catalog_null_price_is_pending_not_an_error() -> void:
	# Arrange
	var doc := _doc([{"item_id": "kebab", "price": null}])
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs, [])


func test_shop_catalog_price_below_one_sov_is_an_error() -> void:
	# Arrange
	var zero := _doc([{"item_id": "kebab", "price": 0}])
	var half := _doc([{"item_id": "kebab", "price": 0.5}])
	# Act
	var zero_errs := ShopCatalog.errors(zero, _items())
	var half_errs := ShopCatalog.errors(half, _items())
	# Assert: the 1-SOV floor (currency.md) and no change.
	assert_eq(zero_errs.size(), 1)
	assert_eq(half_errs.size(), 1)


func test_shop_catalog_non_sovs_currency_is_an_error() -> void:
	# Arrange
	var doc := _doc(_stock(), {"currency": "EUR"})
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs.size(), 1)
	assert_string_contains(errs[0], "currency")


func test_shop_catalog_unknown_item_is_an_error() -> void:
	# Arrange
	var doc := _doc([{"item_id": "no_such_item", "price": 5}])
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs.size(), 1)
	assert_string_contains(errs[0], "no_such_item")


func test_shop_catalog_missing_display_name_is_an_error() -> void:
	# Arrange
	var doc := _doc(_stock())
	doc["shops"]["test_shop"].erase("display_name")
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs.size(), 1)
	assert_string_contains(errs[0], "display_name")


func test_shop_catalog_duplicate_item_row_is_an_error() -> void:
	# Arrange
	var doc := _doc([{"item_id": "kebab", "price": 5}, {"item_id": "kebab", "price": 6}])
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs.size(), 1)
	assert_string_contains(errs[0], "kebab")


func test_shop_catalog_bad_count_is_an_error() -> void:
	# Arrange
	var doc := _doc([{"item_id": "kebab", "price": 5, "count": 0}])
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs.size(), 1)
	assert_string_contains(errs[0], "count")


func test_shop_catalog_bad_shop_id_is_an_error() -> void:
	# Arrange
	var doc := {"shops": {"Test Shop": {"display_name": "X", "currency": "SOVS", "stock": []}}}
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs.size(), 1)


func test_shop_catalog_missing_shops_object_is_an_error() -> void:
	# Arrange
	var doc := {"schema_version": "1.0"}
	# Act
	var errs := ShopCatalog.errors(doc, _items())
	# Assert
	assert_eq(errs.size(), 1)


# --- ShopCatalog: rows and buying ---

func test_shop_catalog_rows_take_names_from_item_data_and_skip_pending() -> void:
	# Arrange
	var shop: Dictionary = _doc(_stock())["shops"]["test_shop"]
	# Act
	var rows := ShopCatalog.rows(shop, _items())
	# Assert
	assert_eq(rows.size(), 3, "the null-price row is pending and not offered")
	assert_eq(rows[0], {"id": "kebab", "name": "Fixture Kebab", "price": 20, "count": 1, "max_stack": null})
	assert_eq(rows[1]["count"], 2)
	assert_eq(rows[2]["max_stack"], 2)


func test_shop_catalog_sovs_text_singular_and_plural() -> void:
	# Arrange / Act / Assert
	assert_eq(ShopCatalog.sovs_text(1), "1 SOV")
	assert_eq(ShopCatalog.sovs_text(40), "40 SOVS")


func test_shop_catalog_buy_pays_and_grants() -> void:
	# Arrange
	state.sovs = 50
	var row := {"id": "kebab", "name": "Fixture Kebab", "price": 20, "count": 1, "max_stack": null}
	# Act
	var ok := ShopCatalog.buy(state, row)
	# Assert
	assert_true(ok)
	assert_eq(state.sovs, 30)
	assert_eq(int(state.inventory.get("kebab", 0)), 1)


func test_shop_catalog_buy_unaffordable_changes_nothing() -> void:
	# Arrange
	state.sovs = 5
	var row := {"id": "kebab", "name": "Fixture Kebab", "price": 20, "count": 1, "max_stack": null}
	# Act
	var ok := ShopCatalog.buy(state, row)
	# Assert
	assert_false(ok)
	assert_eq(state.sovs, 5)
	assert_false(state.inventory.has("kebab"))


func test_shop_catalog_buy_respects_count_and_max_stack() -> void:
	# Arrange
	state.sovs = 50
	var row := {"id": "coupon", "name": "Fixture Coupon", "price": 3, "count": 3, "max_stack": 2}
	# Act
	ShopCatalog.buy(state, row)
	# Assert
	assert_eq(state.sovs, 47, "one price per row")
	assert_eq(int(state.inventory.get("coupon", 0)), 2)


# --- SovsShop screen ---

func test_sovs_shop_setup_lists_rows_from_shop_data() -> void:
	# Arrange / Act
	var s := _shop(_doc(_stock()))
	# Assert
	assert_eq(s.rows.size(), 3)
	assert_eq(s.rows[0]["id"], "kebab")


func test_sovs_shop_interact_buys_the_cursor_row() -> void:
	# Arrange
	state.sovs = 50
	var s := _shop(_doc(_stock()))
	# Act
	s.press("interact")
	# Assert
	assert_eq(state.sovs, 30)
	assert_eq(int(state.inventory.get("kebab", 0)), 1)
	assert_eq(s.bought, ["kebab"])
	assert_eq(s.notice, "")


func test_sovs_shop_cannot_afford_shows_notice_and_changes_nothing() -> void:
	# Arrange
	state.sovs = 5
	var s := _shop(_doc(_stock()))
	# Act
	s.press("interact")
	# Assert
	assert_eq(s.notice, SovsShop.DEFAULT_CANNOT_AFFORD)
	assert_eq(state.sovs, 5)
	assert_false(state.inventory.has("kebab"))
	assert_string_contains(s.text(), SovsShop.DEFAULT_CANNOT_AFFORD)


func test_sovs_shop_cannot_afford_notice_comes_from_shop_data() -> void:
	# Arrange
	state.sovs = 5
	var s := _shop(_doc(_stock(), {"cannot_afford_notice": "FIXTURE NOTICE"}))
	# Act
	s.press("interact")
	# Assert
	assert_eq(s.notice, "FIXTURE NOTICE")


func test_sovs_shop_moving_clears_the_notice_and_wraps() -> void:
	# Arrange
	state.sovs = 5
	var s := _shop(_doc(_stock()))
	s.press("interact")
	# Act
	s.press("move_up")
	# Assert
	assert_eq(s.cursor, 2, "up from the top wraps to the last row")
	assert_eq(s.notice, "")


func test_sovs_shop_cancel_emits_closed_with_purchases() -> void:
	# Arrange
	state.sovs = 50
	var s := _shop(_doc(_stock()))
	watch_signals(s)
	s.press("interact")
	# Act
	s.press("cancel")
	# Assert
	assert_signal_emitted_with_parameters(s, "closed", [["kebab"]])


func test_sovs_shop_text_shows_prices_in_sovs_and_no_fee_row() -> void:
	# Arrange
	state.sovs = 1
	var s := _shop(_doc(_stock()))
	# Act
	var t := s.text()
	# Assert
	assert_string_contains(t, "Test Shop")
	assert_string_contains(t, "20 SOVS")
	assert_string_contains(t, "1 SOV")
	assert_false(t.to_lower().contains("fee"), "§8.4: no fee row on a SOVS purchase")
	assert_false(t.to_lower().contains("pending"), "§1.4: no pending state")


func test_sovs_shop_empty_stock_ignores_input() -> void:
	# Arrange
	state.sovs = 50
	var s := _shop(_doc([]))
	# Act
	s.press("move_down")
	s.press("interact")
	# Assert
	assert_eq(s.rows, [])
	assert_eq(state.sovs, 50)
