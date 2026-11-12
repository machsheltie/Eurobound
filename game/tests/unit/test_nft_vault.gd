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
	for id in ["millennium_bug", "sea_monkeys", "napster", "holographic_charizard", "winamp", "crystal_pepsi", "pogs_the_slammer"]:
		assert_false(NftVault.has_copy(NftVault.card(id)), id)


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


func test_nft_vault_claw_top_prize_awards_the_card() -> void:
	var s := FakeState.new()
	var pit := [{"x": ArcadeClaw.TOP_PRIZE_SLOT, "id": ArcadeClaw.TOP_PRIZE_ID}]
	ArcadeClaw.grab(ArcadeClaw.RIGGED, pit, ArcadeClaw.TOP_PRIZE_SLOT, true, s, RandomNumberGenerator.new())
	assert_true(NftVault.owns(s, "sea_monkeys"))
