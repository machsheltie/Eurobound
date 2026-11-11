extends GutTest
## BattleScreen: shows BattleCore's events one at a time, opens the command menu when a bro needs
## a command, takes targets, and reports the outcome. Driven with press() and advance(), never real
## input or real time.


class FakeState:
	var sovs := 20
	var inventory := {}
	var flags := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "hp": 45, "max_hp": 45, "bravado": 12,
		 "max_bravado": 12, "offense": 8, "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3,
		 "skills": ["roast_line"]},
		{"id": "chadwick", "display_name": "Chadwick", "hp": 35, "max_hp": 35, "bravado": 20,
		 "max_bravado": 20, "offense": 6, "defense": 3, "speed": 7, "charm": 10, "luck": 6, "grit": 2,
		 "skills": []},
		{"id": "bradley", "display_name": "Bradley", "hp": 30, "max_hp": 30, "bravado": 14,
		 "max_bravado": 14, "offense": 12, "defense": 2, "speed": 8, "charm": 4, "luck": 5, "grit": 3,
		 "skills": []},
	]

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func _screen(state: FakeState, seed_value: int = 1) -> BattleScreen:
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(seed_value))
	var screen := BattleScreen.new()
	screen.setup(core, load(ArcadeBattle.backdrop_path("cabinet_frogger")), ArcadeBattle.skills())
	add_child_autoqfree(screen)
	# Frames are driven by the tests, not by _process.
	screen.set_process(false)
	screen.set_process_unhandled_input(false)
	return screen


## Advances until the screen leaves the "events" state (menu, results or done).
func _to_command(screen: BattleScreen) -> void:
	for i in 500:
		if screen.state != "events":
			return
		screen.advance(BattleScreen.EVENT_S)


func _labels(screen: BattleScreen) -> Array:
	return screen.menu.map(func(row: Array) -> String: return String(row[0]))


func test_battle_screen_opens_the_menu_for_a_bro() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	# Act
	_to_command(screen)
	# Assert
	assert_eq(screen.state, "menu")
	assert_not_null(screen.core.current())
	assert_true(screen.core.current().is_party())
	var labels := _labels(screen)
	assert_eq(labels[0], "ATTACK")
	assert_eq(labels.slice(-3), ["ITEM", "FLEX", "RUN"])


func test_battle_screen_item_is_greyed_out_with_nothing_to_use() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var item_row := _labels(screen).find("ITEM")
	screen.cursor = item_row
	# Act
	screen.press("interact")
	# Assert
	assert_false(bool(screen.menu[item_row][2]))
	assert_eq(screen.state, "menu", "a greyed-out command does nothing")


func test_battle_screen_menu_cursor_wraps() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	# Act
	screen.press("move_up")
	var wrapped := screen.cursor
	screen.press("move_down")
	# Assert
	assert_eq(wrapped, screen.menu.size() - 1)
	assert_eq(screen.cursor, 0)


func test_battle_screen_attack_asks_who_and_cancel_goes_back() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	screen.cursor = 0
	# Act
	screen.press("interact")
	var asked := screen.state
	screen.press("cancel")
	# Assert
	assert_eq(asked, "target")
	assert_eq(screen.pending_action, "attack")
	assert_eq(screen.state, "menu")


func test_battle_screen_attacking_a_target_plays_the_turn() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var bro := screen.core.current()
	screen.cursor = 0
	screen.press("interact")
	# Act
	screen.press("interact")
	# Assert
	assert_eq(screen.state, "events")
	assert_ne(screen.core.current(), bro, "the bro's turn is over")


func test_battle_screen_target_cursor_wraps_over_the_villains() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	screen.cursor = 0
	screen.press("interact")
	var count := screen.core.targetable_enemies().size()
	# Act
	screen.press("move_left")
	# Assert
	assert_eq(screen.target_cursor, count - 1)


func test_battle_screen_flex_is_once_per_turn() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var bro := screen.core.current()
	bro.bravado = 0
	var bravado := bro.bravado
	screen.cursor = _labels(screen).find("FLEX")
	screen.press("interact")
	# Act
	_to_command(screen)
	var flex_row := _labels(screen).find("FLEX")
	screen.cursor = flex_row
	screen.press("interact")
	# Assert
	assert_eq(screen.core.current(), bro, "flex is a minor action; the bro still has his turn")
	assert_gt(bro.bravado, bravado)
	assert_false(bool(screen.menu[flex_row][2]))
	assert_eq(screen.state, "menu")


func test_battle_screen_item_heals_the_chosen_bro() -> void:
	# Arrange
	var state := FakeState.new()
	state.inventory["lukewarm_kebab"] = 1
	var screen := _screen(state)
	_to_command(screen)
	var bro := screen.core.current()
	bro.hp = 5
	bro.meter = 5.0
	screen.cursor = _labels(screen).find("ITEM")
	screen.press("interact")
	var listed := screen.state
	# Act: pick the kebab, then pick the bro whose turn it is.
	screen.press("interact")
	var asked := screen.state
	screen.target_cursor = screen.core.living_party().find(bro)
	screen.press("interact")
	# Assert
	assert_eq(listed, "items")
	assert_eq(asked, "item_target")
	assert_gt(bro.hp, 5)
	assert_false(state.inventory.has("lukewarm_kebab"))


func test_battle_screen_cancel_from_items_reopens_the_menu() -> void:
	# Arrange
	var state := FakeState.new()
	state.inventory["lukewarm_kebab"] = 1
	var screen := _screen(state)
	_to_command(screen)
	screen.cursor = _labels(screen).find("ITEM")
	screen.press("interact")
	# Act
	screen.press("cancel")
	# Assert
	assert_eq(screen.state, "menu")
	assert_eq(_labels(screen)[0], "ATTACK")


func test_battle_screen_interact_skips_the_shown_event() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	screen.cursor = 0
	screen.press("interact")
	screen.press("interact")
	var queued: int = screen._queue.size()
	# Act
	screen.press("interact")
	# Assert
	assert_gt(queued, 0)
	assert_eq(screen._queue.size(), queued - 1)


func test_battle_screen_a_whole_fight_reaches_the_results_and_reports_them() -> void:
	# Arrange
	var screen := _screen(FakeState.new(), 7)
	watch_signals(screen)
	# Act: always attack the first villain.
	for i in 3000:
		if screen.state == "done":
			break
		match screen.state:
			"events":
				screen.advance(BattleScreen.EVENT_S)
			"menu":
				screen.cursor = 0
				screen.press("interact")
			"target":
				screen.target_cursor = 0
				screen.press("interact")
			"results":
				screen.press("interact")
	# Assert
	assert_eq(screen.state, "done")
	assert_has(["won", "lost", "ran"], screen.core.outcome)
	assert_signal_emitted_with_parameters(screen, "finished", [screen.core.outcome])
	assert_true(screen.is_queued_for_deletion())


func test_battle_screen_enemy_sprite_path_picks_palettes() -> void:
	# Arrange
	var ninja := BattleUnit.new()
	ninja.id = "condiment_clan_ninja"
	ninja.palette = "chili"
	var swap := BattleUnit.new()
	swap.id = "player_two_palette_swap"
	var croc := BattleUnit.new()
	croc.id = "croc_monsieur"
	var dir := BattleScreen.ENEMY_SPRITE_DIR
	# Act / Assert
	assert_eq(BattleScreen.enemy_sprite_path(ninja), dir + "condiment_clan_ninja_chili_battle_w.png")
	assert_eq(BattleScreen.enemy_sprite_path(swap, 1), dir + "player_two_palette_swap_cocktail_pink_battle_w.png")
	assert_eq(BattleScreen.enemy_sprite_path(swap, 5), dir + "player_two_palette_swap_cocktail_pink_battle_w.png")
	assert_eq(BattleScreen.enemy_sprite_path(croc), dir + "croc_monsieur_battle_w.png")
	assert_true(ResourceLoader.exists(BattleScreen.enemy_sprite_path(ninja)))
