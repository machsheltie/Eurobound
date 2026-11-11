extends GutTest
## Grandpa Provides (approved round v30): the tab's money rules, The Tip at the prize counter, and
## The Unsettled Tab at the exit.

const HALL := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")

class FakeState:
	var gold := 0
	var flags := {}

var _hall: Node3D
var _saved := {}


func before_each() -> void:
	_saved = {"gold": GameState.gold, "inventory": GameState.inventory.duplicate(true),
		"party": GameState.party.duplicate(true), "flags": GameState.flags.duplicate(true)}


func after_each() -> void:
	GameState.gold = _saved["gold"]
	GameState.inventory = _saved["inventory"]
	GameState.party = _saved["party"]
	GameState.flags = _saved["flags"]
	SceneRouter.pending_spawn = ""


func _open_hall() -> void:
	_hall = HALL.instantiate()
	add_child_autofree(_hall)
	await wait_physics_frames(3)
	_hall.travel_out = false
	_hall.dialogue.beat_scale = 0.01


func _player() -> PlayerController:
	return get_tree().get_nodes_in_group("player").filter(func(n): return _hall.is_ancestor_of(n))[0]


## Presses through the scene box, picking `picks` in order at each choice, until `done` is true.
func _drive(done: Callable, picks: Array) -> Array:
	var said := []
	for i in 400:
		if done.call():
			break
		var d: DialogueBox = _hall.dialogue
		if d.mode == "say":
			said.append(d.text)
			d.press("interact")
		elif d.mode == "choose":
			d.cursor = int(picks.pop_front())
			d.press("interact")
		await wait_process_frames(1)
	return said


func test_grandpa_provides_tab_is_forty_then_fifty_after_the_fight() -> void:
	# Arrange
	var s := FakeState.new()
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	# Act
	var before := GrandpaProvides.tab_amount(s)
	GrandpaProvides.fled(s)
	var after := GrandpaProvides.tab_amount(s)
	# Assert
	assert_eq([before, after], [40, 50])
	assert_false(GrandpaProvides.exit_confrontation_due(s), "no second fight")


func test_grandpa_provides_losing_empties_a_short_wallet_and_waives_the_rest() -> void:
	# Arrange
	var s := FakeState.new()
	s.gold = 30
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	# Act
	var waived := GrandpaProvides.lost(s)
	# Assert
	assert_true(waived)
	assert_eq(s.gold, 0)
	assert_false(GrandpaProvides.tab_due(s))


func test_grandpa_provides_the_tip_plays_on_the_first_redemption() -> void:
	# Arrange
	await _open_hall()  # (opening the hall starts a game if none is running, so set state after)
	GameState.flags.erase(GrandpaProvides.RING_TIPPED)
	GameState.inventory = {ArcadeRules.TICKET_ID: 20}
	# Act: open the counter, buy the cheapest prize, close it, then press through The Tip.
	_hall._use_counter()
	var shop: PrizeShop = _hall.prize_shop
	shop.cursor = shop.rows.find(shop.rows.filter(func(r: Dictionary) -> bool: return r["id"] == "aa_junk_promise_ish_ring")[0])
	shop.press("interact")
	shop.press("cancel")
	var said := await _drive(func() -> bool: return bool(GameState.flags.get(GrandpaProvides.RING_TIPPED, false)), [])
	# Assert
	assert_eq(said, ["What, no tip?", "We got you, bro.", "Wow.", "Don't spend it all in one place.",
		"That's five tickets, dude.", "I'll alert my financial adviser."])
	assert_eq(ArcadeRules.tickets(GameState), 15)


func test_grandpa_provides_paying_at_the_exit_settles_the_tab() -> void:
	# Arrange
	await _open_hall()
	GameState.gold = 100
	GameState.flags[GrandpaProvides.ROUND_BOUGHT] = true
	GameState.flags.erase(GrandpaProvides.TAB_PAID)
	GameState.flags.erase(GrandpaProvides.AR_DEFEATED)
	GameState.flags.erase(GrandpaProvides.TAB_OPEN)
	# Act
	_hall._on_exit_intercept(_player())
	var said := await _drive(func() -> bool: return _hall.left, [0])
	# Assert
	assert_eq(said[0], "Hey, Grandpa.")
	assert_has(said, "Pleasure doing business with you, Grandpa.")
	assert_eq(GameState.gold, 60)
	assert_true(bool(GameState.flags[GrandpaProvides.TAB_PAID]))


func test_grandpa_provides_refusing_twice_starts_the_billing_dispute() -> void:
	# Arrange
	await _open_hall()
	GameState.gold = 100
	GameState.flags[GrandpaProvides.ROUND_BOUGHT] = true
	GameState.flags.erase(GrandpaProvides.TAB_PAID)
	GameState.flags.erase(GrandpaProvides.AR_DEFEATED)
	GameState.flags.erase(GrandpaProvides.TAB_OPEN)
	# Act: refuse, refuse, then win the fight.
	_hall._on_exit_intercept(_player())
	await _drive(func() -> bool: return _hall.battle_screen != null, [1, 1])
	var names: Array = _hall.battle_core.enemies.map(func(e: BattleUnit) -> String: return e.display_name)
	_hall.battle_core.outcome = "won"
	_hall.battle_screen.state = "results"
	_hall.battle_screen.press("interact")
	var said := await _drive(func() -> bool: return _hall.left, [])
	# Assert
	assert_eq(names, ["ACCOUNTS", "RECEIVABLE"])
	assert_eq(said, ["HEY!", "Service charge."])
	assert_eq(GrandpaProvides.tab_amount(GameState), 50)
	assert_eq(GameState.gold, 100)


func test_grandpa_provides_shaken_sovs_go_on_the_tab_and_cap_the_loss() -> void:
	# Arrange: Accounts Receivable shook 15 SOVS loose during the fight, then the bros lost.
	var s := FakeState.new()
	s.gold = 100
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	GrandpaProvides.add_credit(s, 15)
	# Act
	GrandpaProvides.lost(s)
	# Assert: 35 more, so 50 in all.
	assert_eq(s.gold, 65)


func test_grandpa_provides_shaken_sovs_shrink_the_open_tab_after_a_win() -> void:
	# Arrange
	var s := FakeState.new()
	s.flags[GrandpaProvides.ROUND_BOUGHT] = true
	GrandpaProvides.add_credit(s, 10)
	# Act
	GrandpaProvides.fled(s)
	# Assert
	assert_eq(GrandpaProvides.tab_amount(s), 40)


func test_grandpa_provides_shake_down_takes_five_toward_the_balance() -> void:
	# Arrange
	var wallet := FakeState.new()
	wallet.gold = 100
	var core := BattleCore.new()
	core.wallet = wallet
	core.balance_due = 40
	var e := BattleUnit.new()
	e.display_name = "ACCOUNTS"
	var t := BattleUnit.new()
	t.id = "lord_pilsner"
	t.display_name = "Lord Pilsner"
	# Act
	core._shake_down(e, t, 5)
	# Assert
	assert_eq([wallet.gold, core.balance_due, core.sovs_collected], [95, 35, 5])
	assert_eq(core.events.map(func(ev): return ev["text"]), [
		"ACCOUNTS holds Lord Pilsner upside down and shakes. 5 SOVS, a Razr and a burned Linkin Park CD hit the carpet. ACCOUNTS keeps the SOVS. He hands back the CD after reading the tracklist. Balance due: 35 SOVS.",
		"Lord Pilsner: \"Bro. Dinner first.\""])


func test_grandpa_provides_banter_after_the_first_cabinet_fight_then_the_approach_buys_the_round() -> void:
	# Arrange
	await _open_hall()
	for f in [GrandpaProvides.BANTER_PLAYED, GrandpaProvides.ROUND_BOUGHT]:
		GameState.flags.erase(f)
	GameState.add_item(ArcadeRules.TOKEN_ID, 2)
	var p := _player()
	p.global_position = get_tree().get_nodes_in_group("spawn_points").filter(
		func(n): return _hall.is_ancestor_of(n) and n.get_meta("spawn_id") == "at_cabinet_frogger")[0].global_position
	p.face("north")
	# Act: play Frogger and close the results; the banter plays after the flash.
	p.try_interact()
	_hall.battle_core.outcome = "won"
	_hall.battle_screen.state = "results"
	_hall.battle_screen.press("interact")
	_hall.overlay.flash_finished.emit()
	var banter := await _drive(func() -> bool: return bool(GameState.flags.get(GrandpaProvides.BANTER_PLAYED, false)), [])
	await wait_process_frames(2)
	_hall._on_group_approach(p)
	var approach := await _drive(func() -> bool: return not _hall._scene_running, [])
	# Assert
	assert_eq(banter, ["No.", "What?", "Whatever you're about to do.", "I'm getting a drink.", "Your drink's right there."])
	assert_eq(approach[0], "How's your night going?")
	assert_has(approach, "HEY, GIRLS! THIS GUY WHO LOOKS LIKE MY GRANDPA IS BUYING US ANOTHER ROUND FOR CARA'S BIRTHDAY!")
	assert_true(GrandpaProvides.exit_confrontation_due(GameState))
	assert_eq(_hall.npcs.size(), 7)
