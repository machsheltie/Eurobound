extends GutTest
## Playing the Absinthe Arcade hall: the bros can walk up to every machine and use it, the token
## machine sells tokens, and a cabinet the bros can't pay for flashes INSUFFICIENT CREDITS
## (author rulings ef_tokens = machine_any, ef_broke = insufficient, ef_arcade_loss = at_cabinet,
## ef_interact_cue = none; 2026-11-10).

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
## Machine id -> the way a bro standing in front of it faces.
const MACHINES := {
	"cabinet_frogger": "north",
	"cabinet_street_fighter": "north",
	"cabinet_kebab_kombat": "north",  # from its south-east corner: the bar blocks the front
	"ddr_dance_off": "west",
	"token_machine": "west",
	"skee_ball": "west",
	"foosball": "north",
}

var _hall: Node3D
var _saved := {}


func before_each() -> void:
	_saved = {"gold": GameState.gold, "inventory": GameState.inventory.duplicate(true), "party": GameState.party.duplicate(true)}
	GameState.gold = 0
	GameState.inventory = {}
	_hall = SCENE.instantiate()
	add_child_autofree(_hall)
	await wait_physics_frames(3)


func after_each() -> void:
	GameState.gold = _saved["gold"]
	GameState.inventory = _saved["inventory"]
	GameState.party = _saved["party"]
	SceneRouter.pending_spawn = ""


func _player() -> PlayerController:
	return get_tree().get_nodes_in_group("player").filter(func(n): return _hall.is_ancestor_of(n))[0]


func _spawn(id: String) -> Node3D:
	for n in get_tree().get_nodes_in_group("spawn_points"):
		if _hall.is_ancestor_of(n) and n.get_meta("spawn_id") == id:
			return n
	return null


func _stand_at(machine: String) -> PlayerController:
	var p := _player()
	p.global_position = _spawn("at_" + machine).global_position
	p.face(MACHINES[machine])
	return p


func test_arcade_hall_every_machine_has_a_spot_in_front_of_it() -> void:
	for machine: String in MACHINES.keys():
		# Arrange
		var spot := _spawn("at_" + machine)
		assert_not_null(spot, machine)
		if spot == null:
			continue

		# Act
		var p := _stand_at(machine)

		# Assert: standing there facing it, the bro can use it
		assert_eq(spot.get_meta("facing"), MACHINES[machine], machine)
		var found := p.nearest_interactable()
		assert_not_null(found, machine)
		if found != null:
			assert_eq(found.get_meta("interact_id"), machine)


func test_arcade_hall_spots_are_on_open_floor() -> void:
	var space := _hall.get_world_3d().direct_space_state
	for machine: String in MACHINES.keys():
		# Arrange
		var spot := _spawn("at_" + machine)
		if spot == null:
			fail_test("no spot for " + machine)
			continue
		var q := PhysicsShapeQueryParameters3D.new()
		var capsule := CapsuleShape3D.new()
		capsule.radius = 0.25
		capsule.height = 1.6
		q.shape = capsule
		q.transform = Transform3D(Basis(), spot.global_position + Vector3(0, 0.85, 0))
		q.exclude = [_player().get_rid()]

		# Act
		var hits := space.intersect_shape(q)

		# Assert
		assert_eq(hits.size(), 0, "%s spot overlaps %s" % [machine, hits])


func test_arcade_hall_token_machine_sells_tokens() -> void:
	# Arrange
	GameState.gold = 10
	_stand_at("token_machine")

	# Act: open the machine, pick 3, confirm
	_player().try_interact()
	var overlay: ArcadeOverlay = _hall.overlay
	assert_true(overlay.is_picking())
	overlay.change_count(2)
	overlay.confirm()

	# Assert
	assert_eq(ArcadeRules.tokens(GameState), 3)
	assert_eq(GameState.gold, 7)
	assert_false(_player().input_locked, "control back after the purchase")


func test_arcade_hall_token_picker_stays_within_the_wallet() -> void:
	# Arrange
	GameState.gold = 2
	_stand_at("token_machine")
	_player().try_interact()
	var overlay: ArcadeOverlay = _hall.overlay

	# Act
	overlay.change_count(10)

	# Assert
	assert_eq(overlay.count, 2)
	overlay.change_count(-10)
	assert_eq(overlay.count, 1)


func test_arcade_hall_cancelling_the_machine_buys_nothing() -> void:
	# Arrange
	GameState.gold = 10
	_stand_at("token_machine")
	_player().try_interact()

	# Act
	_hall.overlay.cancel()

	# Assert
	assert_eq(GameState.gold, 10)
	assert_eq(ArcadeRules.tokens(GameState), 0)
	assert_false(_player().input_locked)


func test_arcade_hall_broke_bros_get_insufficient_credits() -> void:
	# Arrange: one token short of Kebab Kombat
	GameState.add_item(ArcadeRules.TOKEN_ID, 3)
	_stand_at("cabinet_kebab_kombat")

	# Act
	_player().try_interact()

	# Assert
	var overlay: ArcadeOverlay = _hall.overlay
	assert_true(overlay.is_flashing())
	assert_eq(overlay.flash_text(), "INSUFFICIENT CREDITS")
	assert_eq(ArcadeRules.tokens(GameState), 3, "nothing spent")
	assert_true(_player().input_locked, "frozen while the screen flashes")


func test_arcade_hall_token_machine_with_an_empty_wallet_flashes_too() -> void:
	# Arrange
	GameState.gold = 0
	_stand_at("token_machine")

	# Act
	_player().try_interact()

	# Assert
	assert_true(_hall.overlay.is_flashing())
	assert_false(_hall.overlay.is_picking())


func test_arcade_hall_skee_ball_spends_tokens_and_pays_tickets() -> void:
	# Arrange
	GameState.add_item(ArcadeRules.TOKEN_ID, 3)
	_stand_at("skee_ball")

	# Act: start a game, then roll nine dead-centre 50s
	_player().try_interact()
	var screen: SkeeBallScreen = _hall.rec_screen
	assert_not_null(screen)
	if screen == null:
		return
	assert_eq(ArcadeRules.tokens(GameState), 1, "two tokens spent")
	assert_true(_player().input_locked)
	for i in SkeeBall.BALLS:
		screen.aim = 0.0
		screen.state = "power"
		screen.power = 0.85
		screen.confirm()
		screen.advance(SkeeBallScreen.SHOW_ROLL_S)
	screen.confirm()

	# Assert
	assert_eq(ArcadeRules.tickets(GameState), 20)
	assert_eq(_hall.overlay.flash_text(), "20 TICKETS")


func test_arcade_hall_foosball_loss_still_pays_three() -> void:
	# Arrange
	GameState.add_item(ArcadeRules.TOKEN_ID, 2)
	_stand_at("foosball")

	# Act
	_player().try_interact()
	var screen: FoosballScreen = _hall.rec_screen
	assert_not_null(screen)
	if screen == null:
		return
	screen.game.house_goals = Foosball.WIN_GOALS
	screen.state = "play"
	screen.advance(0.01)
	screen.confirm()

	# Assert
	assert_eq(ArcadeRules.tokens(GameState), 0)
	assert_eq(ArcadeRules.tickets(GameState), 3)


func test_arcade_hall_foosball_without_tokens_flashes_insufficient_credits() -> void:
	# Arrange
	GameState.add_item(ArcadeRules.TOKEN_ID, 1)
	_stand_at("foosball")

	# Act
	_player().try_interact()

	# Assert
	assert_null(_hall.rec_screen)
	assert_eq(_hall.overlay.flash_text(), "INSUFFICIENT CREDITS")
