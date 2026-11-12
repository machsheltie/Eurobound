extends GutTest
## NFT Legacy Vault (author round v42): registry, ownership, once-only award, Wallet section, claw hook.

class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []
	var current_scene_path := ""

	func add_item(id: String, n := 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + n


func _menu(s) -> FieldMenu:
	var m := FieldMenu.new()
	m.setup(s)
	add_child_autofree(m)
	m.mode = "Wallet"
	m._draw()
	return m


func test_nft_vault_registry_has_seventeen_unique_cards() -> void:
	var ids := {}
	for c in NftVault.all_cards():
		ids[c["id"]] = true
	assert_eq(NftVault.all_cards().size(), 17)
	assert_eq(ids.size(), 17)


func test_nft_vault_award_is_once_only() -> void:
	var s := FakeState.new()
	assert_false(NftVault.owns(s, "sea_monkeys"))
	assert_true(NftVault.award(s, "sea_monkeys"))
	assert_false(NftVault.award(s, "sea_monkeys"))
	assert_true(NftVault.owns(s, "sea_monkeys"))


func test_nft_vault_unknown_id_is_refused() -> void:
	var s := FakeState.new()
	assert_false(NftVault.award(s, "not_a_card"))
	assert_eq(NftVault.list(s).size(), 0)


func test_nft_vault_author_pending_cards_have_no_copy() -> void:
	for id in ["napster", "holographic_charizard", "winamp", "crystal_pepsi", "pogs_the_slammer"]:
		assert_false(NftVault.has_copy(NftVault.card(id)), id)


## The author wrote The Millennium Bug's card copy on the Eurobound Desk (v45, millennium_bug_nft_item.md §4).
func test_nft_vault_millennium_bug_carries_the_authors_copy_without_markdown() -> void:
	var c := NftVault.card("millennium_bug")
	assert_true(NftVault.field_text(c, "tagline").begins_with("\"Everyone else spent December 31, 1999"))
	assert_true(NftVault.field_text(c, "collectors_note").begins_with("A brutally compressed 16-bit"))
	assert_true(NftVault.field_text(c, "future_value").begins_with("\"The media lied to you"))
	for card in NftVault.all_cards():
		for f in NftVault.COPY_FIELDS:
			assert_false(NftVault.field_text(card, f).contains("**"), "%s.%s has markdown" % [card["id"], f])


## The author wrote Sea-Monkeys' card copy in round v43 (design/items/sea_monkeys_nft_item.md §4).
func test_nft_vault_sea_monkeys_carries_the_authors_v43_copy() -> void:
	var c := NftVault.card("sea_monkeys")
	assert_true(NftVault.field_text(c, "tagline").begins_with("\"Instant life in a foil packet"))
	assert_true(NftVault.field_text(c, "collectors_note").begins_with("A high-contrast, aggressively compressed"))
	assert_true(NftVault.field_text(c, "future_value").begins_with("\"Everyone looks at the 1998"))


func test_nft_vault_only_locked_fields_carry_text() -> void:
	for c in NftVault.all_cards():
		for f in NftVault.COPY_FIELDS:
			assert_eq(NftVault.field_text(c, f) != "", NftVault.field_locked(c, f), "%s.%s" % [c["id"], f])


func test_nft_vault_lane_written_fields_are_blank() -> void:
	var tractor := NftVault.card("tractor_nft")
	var call := NftVault.card("who_you_gonna_call")
	# The Lane-written Collector's Note was replaced by the author's v43 Description (tractor_nft_item.md).
	assert_true(NftVault.field_text(tractor, "collectors_note").begins_with("A scratched, unplated aluminum token"))
	assert_eq(NftVault.field_text(call, "edition"), "")
	assert_eq(NftVault.field_text(call, "acquisition_story"), "")
	assert_false(NftVault.has_copy(NftVault.card("meme_lords_first_selfie")))
	assert_false(NftVault.has_copy(NftVault.card("america_online")))


func test_nft_vault_tractor_locked_strings_are_verbatim() -> void:
	var c := NftVault.card("tractor_nft")
	assert_eq(NftVault.field_text(c, "edition"), "Edition 1 of 1 · Acquired via high-stakes poker")
	assert_eq(NftVault.field_text(c, "future_value"), "████████ (Loading… still loading… extremely bullish)")


func test_nft_vault_sea_monkeys_mint_is_73() -> void:
	assert_eq(NftVault.title(NftVault.card("sea_monkeys")), "Sea-Monkeys (Mint #73)")


func test_nft_vault_wallet_is_empty_dash_with_no_cards() -> void:
	var m := _menu(FakeState.new())
	assert_string_contains(m._body.text, "THE LEGACY VAULT[/b]\n—")


func test_nft_vault_wallet_lists_card_with_dash_when_copy_is_empty() -> void:
	var s := FakeState.new()
	NftVault.award(s, "sea_monkeys")
	var m := _menu(s)
	assert_string_contains(m._body.text, "Sea-Monkeys (Mint #73)")
	assert_string_contains(m._body.text, "—")


func test_nft_vault_wallet_cursor_shows_card_copy() -> void:
	var s := FakeState.new()
	NftVault.award(s, "sea_monkeys")
	NftVault.award(s, "who_you_gonna_call")
	var m := _menu(s)
	m.press("move_down")
	assert_string_contains(m._body.text, "> Who You Gonna Call? (Mint #84)")
	assert_string_contains(m._body.text, "Generational spectral wealth.")
	assert_false(m._body.text.contains("Franchise Class"))


func test_nft_vault_claw_top_prize_awards_the_card() -> void:
	var s := FakeState.new()
	var pit := [{"x": ArcadeClaw.TOP_PRIZE_SLOT, "id": ArcadeClaw.TOP_PRIZE_ID}]
	ArcadeClaw.grab(ArcadeClaw.RIGGED, pit, ArcadeClaw.TOP_PRIZE_SLOT, true, s, RandomNumberGenerator.new())
	assert_true(NftVault.owns(s, "sea_monkeys"))
