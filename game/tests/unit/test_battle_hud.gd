extends GutTest
## The battle screen's turn-order strip, hold-to-peek and status icons (Eurobound-ibgl;
## design/game_design_document.md:301-313, controls ruled in round v35, NEXT_WORK.md:684-686).
## Driven with the screen's own methods and advance(), never real input or real time.


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


func after_each() -> void:
	StatusTable.reset()


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func _screen(state: FakeState, seed_value: int = 1) -> BattleScreen:
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(seed_value))
	var screen := BattleScreen.new()
	screen.setup(core, load(ArcadeBattle.backdrop_path("cabinet_frogger")), ArcadeBattle.skills())
	add_child_autoqfree(screen)
	screen.set_process(false)
	screen.set_process_input(false)
	screen.set_process_unhandled_input(false)
	return screen


func _to_command(screen: BattleScreen) -> void:
	for i in 500:
		if screen.state != "events":
			return
		screen.advance(BattleScreen.EVENT_S)


func _unit(id: String, speed: int, side: String = BattleUnit.PARTY) -> BattleUnit:
	var u := BattleUnit.new()
	u.id = id
	u.display_name = id.capitalize()
	u.side = side
	u.max_hp = 20
	u.hp = 20
	u.meter = 20.0
	u.speed = speed
	return u


func _hp(units: Array) -> Array:
	var out := []
	for u in units:
		out.append(u.hp)
	return out


# --- BattleCore.turn_order ---------------------------------------------------------------------

func test_turn_order_starts_with_whoever_acts_now_and_runs_fastest_first() -> void:
	# Arrange
	var core := ArcadeBattle.build("cabinet_frogger", FakeState.new(), _rng(1))
	# Act
	core.step()
	var order := core.turn_order()
	# Assert
	assert_gt(order.size(), 1)
	assert_eq(order[0], core.current())
	for i in range(1, order.size()):
		assert_true(order[i - 1].battle_speed() >= order[i].battle_speed(),
			"%s goes before %s" % [order[i - 1].display_name, order[i].display_name])


func test_turn_order_drops_a_bro_once_he_has_acted() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var core := screen.core
	var first := core.current()
	# Act
	core.attack(core.targetable_enemies()[0])
	# Assert
	assert_false(core.turn_order().has(first), "the bro who just went is not coming up again this round")


func test_turn_order_leaves_out_a_downed_unit() -> void:
	# Arrange
	var core := ArcadeBattle.build("cabinet_frogger", FakeState.new(), _rng(1))
	core.step()
	var victim: BattleUnit = core.turn_order()[-1]
	# Act
	victim.hp = 0
	victim.meter = 0.0
	# Assert
	assert_false(core.turn_order().has(victim))


func test_cures_for_lists_only_the_carried_items_that_cure_the_status() -> void:
	# Arrange
	var state := FakeState.new()
	state.inventory["revision_sticker"] = 1
	state.inventory["lukewarm_kebab"] = 1
	var core := ArcadeBattle.build("cabinet_frogger", state, _rng(1))
	# Act
	var cures := core.cures_for("confused")
	# Assert
	assert_eq(cures, ["revision_sticker"])
	assert_eq(core.cures_for("stun"), [])


# --- the strip ---------------------------------------------------------------------------------

func test_strip_shows_one_portrait_per_unit_in_the_order_given() -> void:
	# Arrange
	var strip := TurnOrderStrip.new()
	add_child_autoqfree(strip)
	var a := _unit("alpha", 9)
	var b := _unit("beta", 5, BattleUnit.ENEMY)
	# Act
	strip.show_order([a, b])
	# Assert
	assert_eq(strip.units, [a, b])
	assert_eq(strip.portraits.size(), 2)
	assert_eq(strip.name_on(0), "Alpha")
	assert_eq(strip.name_on(1), "Beta")
	assert_eq(strip.active_unit(), a)


func test_strip_rebuilds_when_the_order_changes() -> void:
	# Arrange
	var strip := TurnOrderStrip.new()
	add_child_autoqfree(strip)
	var a := _unit("alpha", 9)
	var b := _unit("beta", 5)
	strip.show_order([a, b])
	# Act
	strip.show_order([b])
	# Assert
	assert_eq(strip.units, [b])
	assert_eq(strip.portraits.size(), 1)
	assert_eq(strip.name_on(0), "Beta")


func test_screen_strip_matches_battle_core_through_a_turn() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var at_menu: Array = screen.strip.units.duplicate()
	var expected: Array = Array(screen.core.turn_order())
	var first := screen.core.current()
	# Act: attack the first villain, then let the fight run on to the next command.
	screen.press("interact")
	screen.press("interact")
	_to_command(screen)
	# Assert
	assert_eq(at_menu, expected)
	assert_eq(at_menu[0], first)
	assert_eq(screen.strip.units, Array(screen.core.turn_order()))
	if screen.state == "menu":
		assert_eq(screen.strip.active_unit(), screen.core.current())


# --- status icons ------------------------------------------------------------------------------

func test_status_row_falls_back_to_the_table_name_when_there_is_no_icon() -> void:
	# Arrange
	var row := StatusIconRow.new()
	add_child_autoqfree(row)
	var u := _unit("alpha", 5)
	u.statuses["cottonmouth"] = -1
	# Act
	row.show_unit(u)
	# Assert
	assert_eq(row.shown, ["cottonmouth"])
	assert_false(StatusIconRow.has_icon("cottonmouth"))
	assert_eq(row.text_on(0), StatusTable.display_name("cottonmouth").to_upper())


func test_status_row_follows_the_unit_as_statuses_come_and_go() -> void:
	# Arrange
	var row := StatusIconRow.new()
	add_child_autoqfree(row)
	var u := _unit("alpha", 5)
	u.statuses["crash"] = 2
	row.show_unit(u)
	# Act
	u.statuses.erase("crash")
	row.show_unit(u)
	# Assert
	assert_eq(row.shown, [])
	assert_eq(row.chips.size(), 0)


func test_screen_shows_each_live_status_on_its_fighter() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var bro: BattleUnit = screen.core.party[1]
	var villain: BattleUnit = screen.core.enemies[0]
	# Act
	bro.statuses["cottonmouth"] = -1
	villain.statuses["stun"] = 1
	screen.advance(0.01)
	# Assert
	assert_eq(screen.status_row(bro).shown, ["cottonmouth"])
	assert_eq(screen.status_row(villain).shown, ["stun"])
	assert_eq(screen.status_row(screen.core.party[0]).shown, [])


# --- peek --------------------------------------------------------------------------------------

func test_peek_card_shows_hp_statuses_and_speed() -> void:
	# Arrange
	var u := _unit("alpha", 7)
	u.hp = 12
	u.meter = 12.0
	u.statuses["cottonmouth"] = -1
	# Act
	var text := PeekCard.text_for(u)
	# Assert
	assert_string_contains(text, "ALPHA")
	assert_string_contains(text, "HP 12 / 20")
	assert_string_contains(text, "SPEED %d" % u.battle_speed())
	assert_string_contains(text, StatusTable.display_name("cottonmouth").to_upper())


func test_hovering_a_portrait_peeks_and_leaving_closes_it() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var who: BattleUnit = screen.strip.units[1]
	# Act
	screen.hover_portrait(who)
	var during := screen.peek_unit
	screen.hover_portrait(null)
	# Assert
	assert_eq(during, who)
	assert_null(screen.peek_unit)


func test_holding_pin_keeps_the_peek_after_the_pointer_leaves() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var who: BattleUnit = screen.strip.units[1]
	screen.hover_portrait(who)
	# Act
	screen.pin(true)
	screen.hover_portrait(null)
	var held := screen.peek_unit
	screen.pin(false)
	# Assert
	assert_eq(held, who)
	assert_null(screen.peek_unit)


func test_pin_does_nothing_with_no_portrait_under_the_pointer() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	# Act
	screen.pin(true)
	# Assert
	assert_null(screen.peek_unit)


func test_holding_the_peek_button_opens_after_point_four_seconds_and_release_closes() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	# Act
	screen.peek_button(true)
	screen.advance(0.3)
	var early := screen.peek_unit
	screen.advance(0.1)
	var open := screen.peek_unit
	screen.peek_button(false)
	# Assert
	assert_eq(BattleScreen.PEEK_HOLD_S, 0.4)
	assert_null(early, "a tap is not a peek")
	assert_eq(open, screen.core.current())
	assert_null(screen.peek_unit)


func test_the_peek_hold_never_fires_an_action() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var cursor := screen.cursor
	var hp := _hp(screen.core.enemies)
	# Act
	screen.peek_button(true)
	screen.advance(1.0)
	screen.peek_button(false)
	# Assert
	assert_eq(screen.state, "menu")
	assert_eq(screen.cursor, cursor)
	assert_eq(_hp(screen.core.enemies), hp)
	assert_false(screen.core.minor_used)


func test_the_peek_button_follows_the_target_cursor_while_choosing_a_target() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	screen.press("interact")   # ATTACK -> who?
	var target: BattleUnit = screen.core.targetable_enemies()[screen.target_cursor]
	# Act
	screen.peek_button(true)
	screen.advance(BattleScreen.PEEK_HOLD_S)
	# Assert
	assert_eq(screen.state, "target")
	assert_eq(screen.peek_unit, target)


# --- hold a status for its cures ----------------------------------------------------------------

func test_holding_a_status_opens_its_cures_aimed_at_the_bearer() -> void:
	# Arrange
	var state := FakeState.new()
	state.inventory["revision_sticker"] = 1
	state.inventory["lukewarm_kebab"] = 1
	var screen := _screen(state)
	_to_command(screen)
	var bearer: BattleUnit = screen.core.party[2]
	bearer.statuses["confused"] = 3
	# Act
	screen.status_button(bearer, "confused", true)
	screen.advance(0.3)
	var early := screen.state
	screen.advance(0.1)
	var listed := screen.state
	var rows := []
	for row in screen.menu:
		rows.append(String(row[1]))
	screen.status_button(bearer, "confused", false)
	screen.press("interact")
	var aimed: BattleUnit = screen.core.item_targets("revision_sticker")[screen.target_cursor]
	screen.press("interact")
	# Assert
	assert_eq(early, "menu")
	assert_eq(listed, "items")
	assert_eq(rows, ["revision_sticker"])
	assert_eq(aimed, bearer)
	assert_false(bearer.statuses.has("confused"))


func test_holding_a_status_with_no_cure_in_the_bag_changes_nothing() -> void:
	# Arrange
	var screen := _screen(FakeState.new())
	_to_command(screen)
	var bearer: BattleUnit = screen.core.party[2]
	bearer.statuses["confused"] = 3
	# Act
	screen.status_button(bearer, "confused", true)
	screen.advance(1.0)
	# Assert
	assert_eq(screen.state, "menu")


func test_letting_go_of_a_status_early_opens_nothing() -> void:
	# Arrange
	var state := FakeState.new()
	state.inventory["revision_sticker"] = 1
	var screen := _screen(state)
	_to_command(screen)
	var bearer: BattleUnit = screen.core.party[2]
	bearer.statuses["confused"] = 3
	# Act
	screen.status_button(bearer, "confused", true)
	screen.advance(0.2)
	screen.status_button(bearer, "confused", false)
	screen.advance(1.0)
	# Assert
	assert_eq(screen.state, "menu")
