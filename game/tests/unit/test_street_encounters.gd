extends GutTest
## Street encounters, Option A (Eurobound-iqgo; docs/superpowers/specs/2026-11-16-Eurobound-skjd-proposal.md
## section 3; design/mechanics/Battle/street_encounters.md): the enemy on the map (StreetEnemy),
## contact starting the existing battle, first strike by facing, the grace period, respawn on
## re-entry and the loss handler (StreetEncounters, StreetLoss).
##
## No real enemy is placed anywhere: the fixture enemy id below only borrows an existing engine
## stat line so a BattleCore can be built. Every unruled number is a fixture value set on the
## StreetEncounters under test, never in the rules.

const FIXTURE_ENEMY := "feral_segway_tourist"   ## engine row in debaucheryville_enemies.json
const FIXTURE_SCREEN := "res://tests/fixtures/street/street_encounter_test_screen.tscn"
const SAVE_SCRIPT := "res://core/save_system.gd"
const TEST_SAVE_DIR := "user://saves/test_street_iqgo"
const SAVED_SCENE := "res://tests/fixtures/street/street_encounter_test_screen.tscn"
const NORTH := Vector3(0, 0, -1)
const SOUTH := Vector3(0, 0, 1)


class FakeState:
	var sovs := 80
	var inventory := {"lukewarm_kebab": 1}
	var flags := {}
	var current_scene_path := "res://tests/fixtures/street/here.tscn"
	var player_spot := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "level": 5, "xp": 40, "hp": 45, "max_hp": 45,
		 "bravado": 12, "max_bravado": 12, "offense": 8, "defense": 6, "speed": 5, "charm": 9, "luck": 4,
		 "grit": 3, "skills": []},
		{"id": "chadwick", "display_name": "Chadwick", "level": 5, "xp": 40, "hp": 35, "max_hp": 35,
		 "bravado": 12, "max_bravado": 12, "offense": 6, "defense": 3, "speed": 7, "charm": 10, "luck": 4,
		 "grit": 2, "skills": []},
		{"id": "bradley", "display_name": "Bradley", "level": 5, "xp": 40, "hp": 30, "max_hp": 30,
		 "bravado": 12, "max_bravado": 12, "offense": 12, "defense": 2, "speed": 8, "charm": 4, "luck": 5,
		 "grit": 3, "skills": []},
	]

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


var state: FakeState
var world: Node3D
var player: PlayerController
var enemy: StreetEnemy
var enc: StreetEncounters
var saver
var traveled: Array = []


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func before_each() -> void:
	traveled = []
	state = FakeState.new()
	saver = load(SAVE_SCRIPT).new()
	saver.save_dir = TEST_SAVE_DIR
	saver.save_path = saver.slot_path(1)
	add_child_autofree(saver)
	_wipe_saves()
	world = Node3D.new()
	add_child_autofree(world)
	player = PlayerController.new()
	player.set_physics_process(false)
	world.add_child(player)
	enemy = StreetEnemy.new()
	enemy.enemy_ids = [FIXTURE_ENEMY]
	enemy.position = Vector3(0, 0, -1)
	enemy.set_physics_process(false)
	world.add_child(enemy)
	enc = _director()
	world.add_child(enc)
	SceneRouter.pending_spot = {}


func after_each() -> void:
	_wipe_saves()
	DirAccess.remove_absolute(TEST_SAVE_DIR)
	SceneRouter.pending_spot = {}


func _director() -> StreetEncounters:
	var d := StreetEncounters.new()
	d.state = state
	d.save_system = saver
	d.rng = _rng(1)
	d.player = player
	d.traveler = func(plan: Dictionary) -> void: traveled.append(plan)
	d.set_physics_process(false)
	return d


func _wipe_saves() -> void:
	for slot in range(1, 4):
		for p in [saver.slot_path(slot), saver.slot_path(slot) + ".tmp"]:
			if FileAccess.file_exists(p):
				DirAccess.remove_absolute(p)


## A save on disk in slot 1, made at SAVED_SCENE with the leader at `spot`.
func _write_save(spot: Dictionary) -> void:
	DirAccess.make_dir_recursive_absolute(TEST_SAVE_DIR)
	var f := FileAccess.open(saver.slot_path(1), FileAccess.WRITE)
	f.store_string(JSON.stringify({"save_version": GameState.SAVE_VERSION, "party": [], "inventory": {},
		"sovs": 999, "flags": {}, "current_scene_path": SAVED_SCENE, "player_spot": spot}))
	f.close()


## The battle screen the contact opened, driven by hand.
func _screen() -> BattleScreen:
	var s := enc.battle_screen
	s.set_process(false)
	s.set_process_unhandled_input(false)
	return s


## Ends the open fight with `outcome` and clicks through the results, as the player would.
func _finish(outcome: String) -> void:
	var s := _screen()
	s.core.outcome = outcome
	s.advance(BattleScreen.EVENT_S)
	for i in 50:
		if s.state == "results":
			break
		s.advance(BattleScreen.EVENT_S)
	s.press("interact")


# --- contact starts the existing battle (point 2) ----------------------------------------------

func test_street_contact_starts_the_battle_against_the_touched_enemy() -> void:
	# Act
	var what := enc.touch(enemy)
	# Assert
	assert_eq(what, StreetEncounters.STARTED)
	assert_not_null(enc.battle_screen)
	assert_eq(enc.battle_screen.core.enemies.map(func(e: BattleUnit) -> String: return e.id), [FIXTURE_ENEMY])
	assert_eq(enc.battle_screen.core.party.size(), 3)


func test_street_contact_holds_the_bros_and_freezes_the_map_during_the_fight() -> void:
	enc.touch(enemy)
	assert_true(player.input_locked)
	assert_true(enemy.frozen)


func test_street_contact_comes_from_the_enemy_touching_the_leader() -> void:
	# Act: the contact area reports the leader walking in.
	enemy._on_body_entered(player)
	# Assert
	assert_not_null(enc.battle_screen)


func test_street_contact_ignores_anything_but_the_leader() -> void:
	var other: StaticBody3D = autofree(StaticBody3D.new())
	enemy._on_body_entered(other)
	assert_null(enc.battle_screen)


func test_street_contact_during_a_fight_is_ignored() -> void:
	var second := StreetEnemy.new()
	second.enemy_ids = [FIXTURE_ENEMY]
	second.set_physics_process(false)
	world.add_child(second)
	enc.register(second)
	enc.touch(enemy)
	var first_screen := enc.battle_screen
	assert_eq(enc.touch(second), StreetEncounters.IGNORED)
	assert_eq(enc.battle_screen, first_screen)


func test_street_contact_with_an_enemy_with_no_fight_is_ignored() -> void:
	enemy.enemy_ids = []
	assert_eq(enc.touch(enemy), StreetEncounters.IGNORED)
	assert_null(enc.battle_screen)


func test_street_fights_do_not_say_the_arcade_loss_line() -> void:
	enc.touch(enemy)
	assert_eq(enc.battle_screen.core.loss_line, "")


# --- first strike by facing (point 3) ----------------------------------------------------------

func _party_all_first(core: BattleCore) -> bool:
	var seen_enemy := false
	for u in core.turn_order():
		if not u.is_party():
			seen_enemy = true
		elif seen_enemy:
			return false
	return true


func test_street_first_strike_bros_from_behind_act_first() -> void:
	# Arrange: the enemy faces north; the leader is behind it (south), facing north.
	enc.first_strike_rounds = 1
	enemy.position = Vector3.ZERO
	enemy.facing_dir = NORTH
	player.position = Vector3(0, 0, 1)
	player.facing_dir = NORTH
	# Act
	enc.touch(enemy)
	# Assert
	var core := enc.battle_screen.core
	assert_eq(core.first_strike, StreetEncounterRules.PARTY)
	assert_true(_party_all_first(core))


func test_street_first_strike_enemy_from_behind_acts_first() -> void:
	enc.first_strike_rounds = 1
	enemy.position = Vector3(0, 0, 1)
	enemy.facing_dir = NORTH
	player.position = Vector3.ZERO
	player.facing_dir = NORTH
	enc.touch(enemy)
	var core := enc.battle_screen.core
	assert_eq(core.first_strike, StreetEncounterRules.ENEMY)
	assert_false(core.turn_order()[0].is_party())


func test_street_first_strike_lasts_only_its_rounds() -> void:
	enc.first_strike_rounds = 1
	enemy.position = Vector3(0, 0, 1)
	enemy.facing_dir = NORTH
	player.position = Vector3.ZERO
	player.facing_dir = NORTH
	enc.touch(enemy)
	var core := enc.battle_screen.core
	assert_true(core.first_strike_applies())
	core.round_number = 2
	assert_false(core.first_strike_applies())


func test_street_first_strike_is_off_while_its_size_is_unruled() -> void:
	# Arrange: bros from behind, but no ruled size.
	enemy.position = Vector3.ZERO
	enemy.facing_dir = NORTH
	player.position = Vector3(0, 0, 1)
	player.facing_dir = NORTH
	# Act
	enc.touch(enemy)
	# Assert
	assert_null(enc.first_strike_rounds)
	assert_false(enc.battle_screen.core.first_strike_applies())


# --- winning, auto-win (point 4) ---------------------------------------------------------------

func test_street_win_pays_the_enemy_sovs_and_drop_and_removes_it() -> void:
	enc.touch(enemy)
	_finish("won")
	assert_eq(state.sovs, 88, "80 + the fixture enemy's 8 SOVS")
	assert_eq(int(state.inventory.get("lukewarm_kebab", 0)), 2, "its drop (chance 1.0)")
	assert_true(enemy.is_queued_for_deletion())
	assert_null(enc.battle_screen)
	assert_false(player.input_locked)


func test_street_win_writes_no_flag_so_the_enemy_respawns() -> void:
	# Act
	enc.touch(enemy)
	_finish("won")
	# Assert: only the field-status write-back every fight does; nothing remembers the enemy.
	assert_eq(state.flags.keys(), ["field_status"])
	assert_eq(state.flags["field_status"], {})


func test_street_auto_win_is_off_by_default() -> void:
	enemy.level = 1
	assert_eq(enc.touch(enemy), StreetEncounters.STARTED)
	assert_eq(enc.battle_screen.core.outcome, "")


func test_street_auto_win_with_a_fixture_gap_goes_straight_to_the_win() -> void:
	# Arrange: fixture gap 3 on the leader's level (5) against a level-1 enemy.
	enc.auto_win_gap = 3
	enc.auto_win_measure = "leader"
	enemy.level = 1
	# Act
	var what := enc.touch(enemy)
	_screen().advance(BattleScreen.EVENT_S)
	# Assert
	assert_eq(what, StreetEncounters.AUTO_WON)
	assert_eq(enc.battle_screen.state, "results")
	assert_eq(enc.battle_screen.core.outcome, "won")


func test_street_auto_win_pays_like_a_win() -> void:
	enc.auto_win_gap = 3
	enc.auto_win_measure = "leader"
	enemy.level = 1
	enc.touch(enemy)
	_screen().advance(BattleScreen.EVENT_S)
	_screen().press("interact")
	assert_eq(state.sovs, 88)
	assert_true(enemy.is_queued_for_deletion())


func test_street_auto_win_needs_the_enemy_level() -> void:
	enc.auto_win_gap = 3
	enc.auto_win_measure = "leader"
	assert_eq(enemy.level, StreetEnemy.NO_LEVEL)
	assert_eq(enc.touch(enemy), StreetEncounters.STARTED)


# --- grace after a fight or a Run (point 5) ----------------------------------------------------

func _second_enemy() -> StreetEnemy:
	var e := StreetEnemy.new()
	e.enemy_ids = [FIXTURE_ENEMY]
	e.set_physics_process(false)
	world.add_child(e)
	enc.register(e)
	return e


func test_street_grace_in_seconds_after_a_run() -> void:
	# Arrange: a fixture grace of 2 seconds.
	enc.grace_length = 2.0
	enc.grace_unit = StreetEncounterRules.UNIT_SECONDS
	enc.touch(enemy)
	_finish("ran")
	# Act + Assert
	assert_true(enc.in_grace())
	assert_eq(enc.touch(enemy), StreetEncounters.IGNORED)
	enc.advance_grace(1.0, 0.0)
	assert_eq(enc.touch(enemy), StreetEncounters.IGNORED)
	enc.advance_grace(1.0, 0.0)
	assert_false(enc.in_grace())
	assert_eq(enc.touch(enemy), StreetEncounters.STARTED)


func test_street_grace_in_steps_after_a_win() -> void:
	enc.grace_length = 5
	enc.grace_unit = StreetEncounterRules.UNIT_STEPS
	var other := _second_enemy()
	enc.touch(enemy)
	_finish("won")
	enc.advance_grace(10.0, 3.0)   # seconds do not count, metres do
	assert_eq(enc.touch(other), StreetEncounters.IGNORED)
	enc.advance_grace(0.0, 2.0)
	assert_eq(enc.touch(other), StreetEncounters.STARTED)


func test_street_grace_counts_the_leaders_metres_on_the_map() -> void:
	enc.grace_length = 5
	enc.grace_unit = StreetEncounterRules.UNIT_STEPS
	enc.touch(enemy)
	_finish("ran")
	enc._physics_process(0.016)
	player.position += Vector3(0.9, 0, 0)
	enc._physics_process(0.016)
	assert_almost_eq(enc.grace_left, 4.1, 0.001)


func test_street_no_grace_while_its_step_count_is_unruled() -> void:
	enc.touch(enemy)
	_finish("ran")
	assert_eq(enc.grace_unit, StreetEncounterRules.UNIT_STEPS)
	assert_null(enc.grace_length)
	assert_false(enc.in_grace())


func test_street_grace_default_unit_is_steps_so_a_fixture_count_counts_walking() -> void:
	enc.grace_length = 4   # fixture count; the real number is not ruled
	enc.touch(enemy)
	_finish("ran")
	assert_true(enc.in_grace())
	enc.advance_grace(30.0, 1.5)   # seconds do not count
	assert_true(enc.in_grace())
	enc.advance_grace(0.0, 2.5)
	assert_false(enc.in_grace())


func test_street_after_a_run_the_enemy_stays_and_the_map_moves_again() -> void:
	enc.touch(enemy)
	_finish("ran")
	assert_false(enemy.is_queued_for_deletion())
	assert_false(enemy.frozen)
	assert_false(player.input_locked)


# --- respawn when the bros leave the screen and return (point 6) -------------------------------

func test_street_respawn_a_beaten_enemy_is_back_when_the_screen_loads_again() -> void:
	# Arrange: the fixture screen holds one enemy.
	var packed: PackedScene = load(FIXTURE_SCREEN)
	var first := packed.instantiate()
	add_child_autofree(first)
	var screen_enemies := first.get_tree().get_nodes_in_group(StreetEnemy.GROUP).filter(
		func(n: Node) -> bool: return first.is_ancestor_of(n))
	assert_eq(screen_enemies.size(), 1)
	# Act: beat it, leave (the screen is freed), come back (the screen loads again).
	screen_enemies[0].defeat()
	first.free()
	var again := packed.instantiate()
	add_child_autofree(again)
	# Assert
	var back := again.get_tree().get_nodes_in_group(StreetEnemy.GROUP).filter(
		func(n: Node) -> bool: return again.is_ancestor_of(n) and not n.is_queued_for_deletion())
	assert_eq(back.size(), 1)


# --- losing (point 7) --------------------------------------------------------------------------

func test_street_loss_returns_to_the_last_save() -> void:
	# Arrange
	var spot := {"x": 1.5, "y": 0.0, "z": -2.0, "facing": "west"}
	_write_save(spot)
	enc.touch(enemy)
	# Act
	_finish("lost")
	# Assert
	assert_eq(traveled.size(), 1)
	assert_eq(traveled[0]["scene"], SAVED_SCENE)
	assert_eq(traveled[0]["spot"], spot)
	assert_eq(state.current_scene_path, SAVED_SCENE)
	assert_eq(SceneRouter.pending_spot, spot)


func test_street_loss_keeps_xp_and_items() -> void:
	_write_save({"x": 0.0, "y": 0.0, "z": 0.0, "facing": "south"})
	enc.touch(enemy)
	_finish("lost")
	assert_eq(state.party.map(func(m: Dictionary) -> int: return int(m["xp"])), [40, 40, 40])
	assert_eq(state.party.map(func(m: Dictionary) -> int: return int(m["level"])), [5, 5, 5])
	assert_eq(state.inventory, {"lukewarm_kebab": 1})


func test_street_loss_takes_the_fixture_share_of_sovs_on_hand() -> void:
	# Arrange: fixture share 0.25 of 80 SOVS on hand (the save's 999 is not what counts).
	enc.loss_sovs_share = 0.25
	_write_save({"x": 0.0, "y": 0.0, "z": 0.0, "facing": "south"})
	enc.touch(enemy)
	# Act
	_finish("lost")
	# Assert
	assert_eq(state.sovs, 60)
	assert_eq(traveled[0]["sovs_lost"], 20)


func test_street_loss_takes_half_of_sovs_on_hand_by_default() -> void:
	_write_save({"x": 0.0, "y": 0.0, "z": 0.0, "facing": "south"})
	enc.touch(enemy)
	_finish("lost")
	assert_eq(state.sovs, 40)


func test_street_loss_of_an_odd_amount_keeps_the_rounded_up_half() -> void:
	state.sovs = 81
	_write_save({"x": 0.0, "y": 0.0, "z": 0.0, "facing": "south"})
	enc.touch(enemy)
	_finish("lost")
	assert_eq(state.sovs, 41)
	assert_eq(traveled[0]["sovs_lost"], 40)


func test_street_loss_takes_nothing_while_the_share_is_unruled() -> void:
	enc.loss_sovs_share = null
	_write_save({"x": 0.0, "y": 0.0, "z": 0.0, "facing": "south"})
	enc.touch(enemy)
	_finish("lost")
	assert_eq(state.sovs, 80)


func test_street_loss_leaves_the_bros_at_the_existing_loss_hp() -> void:
	_write_save({"x": 0.0, "y": 0.0, "z": 0.0, "facing": "south"})
	enc.touch(enemy)
	_finish("lost")
	assert_eq(state.party.map(func(m: Dictionary) -> int: return int(m["hp"])),
		[ArcadeBattle.LOSS_HP, ArcadeBattle.LOSS_HP, ArcadeBattle.LOSS_HP])


func test_street_loss_with_no_save_goes_back_to_this_screens_start() -> void:
	enc.touch(enemy)
	_finish("lost")
	assert_eq(traveled[0]["scene"], "res://tests/fixtures/street/here.tscn")
	assert_eq(traveled[0]["spot"], {})


func test_street_loss_does_not_load_the_save_over_the_state() -> void:
	_write_save({"x": 0.0, "y": 0.0, "z": 0.0, "facing": "south"})
	enc.touch(enemy)
	_finish("lost")
	assert_eq(state.party.size(), 3, "the save's empty party is not loaded")


func test_street_last_save_location_reads_the_slot_last_used() -> void:
	_write_save({"x": 3.0, "y": 0.0, "z": 4.0, "facing": "north"})
	var where: Dictionary = saver.last_save_location()
	assert_eq(where["scene"], SAVED_SCENE)
	assert_eq(where["spot"]["facing"], "north")


func test_street_last_save_location_is_empty_with_no_save() -> void:
	assert_eq(saver.last_save_location(), {})


func test_street_loss_screen_shows_the_placeholder_key_not_game_over() -> void:
	enc.touch(enemy)
	var s := _screen()
	s.core.outcome = "lost"
	for i in 50:
		if s.state == "results":
			break
		s.advance(BattleScreen.EVENT_S)
	assert_eq(s._text.text, BattleScreen.LOSS_TEXT_KEY)
	assert_ne(s._text.text, "GAME OVER")


# --- the enemy on the map (point 1) ------------------------------------------------------------

func test_street_enemy_is_visible_and_in_its_group() -> void:
	assert_true(enemy.is_in_group(StreetEnemy.GROUP))
	assert_true(enemy.visible)
	assert_not_null(enemy.get_node_or_null("look"))


func test_street_enemy_stands_by_default() -> void:
	assert_eq(enemy.movement, StreetEnemy.STAND)
	assert_eq(enemy.desired_direction(Vector3(0, 0, 5)), Vector3.ZERO)


func test_street_enemy_walks_toward_the_bros_in_sight() -> void:
	enemy.movement = StreetEnemy.APPROACH
	enemy.sight_range = 5.0
	enemy.position = Vector3.ZERO
	assert_almost_eq(enemy.desired_direction(Vector3(0, 0, 3)), SOUTH, Vector3.ONE * 0.001)
	assert_eq(enemy.desired_direction(Vector3(0, 0, 9)), Vector3.ZERO)


func test_street_enemy_approach_needs_a_sight_range() -> void:
	enemy.movement = StreetEnemy.APPROACH
	enemy.position = Vector3.ZERO
	assert_eq(enemy.desired_direction(Vector3(0, 0, 1)), Vector3.ZERO)


func test_street_enemy_wanders_inside_its_radius() -> void:
	enemy.movement = StreetEnemy.WANDER
	enemy.wander_radius = 2.0
	enemy.rng = _rng(3)
	enemy.home = Vector3(4, 0, 4)
	enemy.position = Vector3(4, 0, 4)
	for i in 20:
		var target := enemy.next_wander_target()
		assert_true(Vector2(target.x - 4.0, target.z - 4.0).length() <= 2.0 + 0.001)


func test_street_enemy_wander_needs_a_radius() -> void:
	enemy.movement = StreetEnemy.WANDER
	assert_eq(enemy.desired_direction(Vector3(0, 0, 9)), Vector3.ZERO)


func test_street_enemy_frozen_does_not_move() -> void:
	enemy.movement = StreetEnemy.APPROACH
	enemy.sight_range = 5.0
	enemy.frozen = true
	assert_eq(enemy.desired_direction(Vector3(0, 0, 1)), Vector3.ZERO)


func test_street_enemy_faces_the_way_it_walks() -> void:
	enemy.movement = StreetEnemy.APPROACH
	enemy.sight_range = 5.0
	enemy.move_speed = 1.0
	enemy.position = Vector3.ZERO
	enemy.walk(0.1, Vector3(3, 0, 0))
	assert_almost_eq(enemy.facing_dir, Vector3(1, 0, 0), Vector3.ONE * 0.001)


func test_street_enemy_with_no_speed_stays_put() -> void:
	enemy.movement = StreetEnemy.APPROACH
	enemy.sight_range = 5.0
	enemy.position = Vector3.ZERO
	enemy.walk(0.1, Vector3(3, 0, 0))
	assert_eq(enemy.position, Vector3.ZERO)
