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
