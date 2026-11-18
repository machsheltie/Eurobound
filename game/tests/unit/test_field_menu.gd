extends GutTest
## FieldMenu (round v36): the nine sections, Pilsner's watch, field items, party order.

class FakeState:
	var sovs := 20
	var inventory := {}
	var flags := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "hp": 20, "max_hp": 45, "bravado": 12, "max_bravado": 12,
		 "offense": 8, "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3, "skills": []},
		{"id": "chadwick", "display_name": "Chadwick", "hp": 35, "max_hp": 35, "bravado": 20, "max_bravado": 20,
		 "offense": 6, "defense": 3, "speed": 7, "charm": 10, "luck": 6, "grit": 2, "skills": []},
	]
	var current_scene_path := ""


func _menu(s) -> FieldMenu:
	var m := FieldMenu.new()
	m.setup(s)
	add_child_autofree(m)
	return m


func test_field_menu_passport_only_once_the_book_is_held() -> void:
	# Arrange
	var s := FakeState.new()
	var m := _menu(s)
	# Act
	var without := m.sections().has("Brewery Passport")
	s.inventory[FieldMenu.PASSPORT_ITEM] = 1
	# Assert
	assert_false(without)
	assert_true(m.sections().has("Brewery Passport"))
	assert_false(m.sections().has("Save"), "no Save (round v36)")


func test_field_menu_shows_the_watch_time_and_sovs() -> void:
	# Arrange
	var s := FakeState.new()
	GameClock.set_time(s, 23 * 60 + 40)
	# Act
	var m := _menu(s)
	# Assert
	assert_eq(m._watch.text, "23:40")
	assert_eq(m._sovs.text, "SOVS    20")


func test_field_menu_uses_a_kebab_on_the_chosen_bro() -> void:
	# Arrange: Lukewarm Kebab restores 20 HP.
	var s := FakeState.new()
	s.inventory["lukewarm_kebab"] = 1
	var m := _menu(s)
	# Act
	var used := m.use_on("lukewarm_kebab", 0)
	# Assert
	assert_true(used)
	assert_eq(int(s.party[0]["hp"]), 40)
	assert_false(s.inventory.has("lukewarm_kebab"))


func test_field_menu_party_swap_reorders_the_bros() -> void:
	# Arrange
	var s := FakeState.new()
	var m := _menu(s)
	m.mode = "Party"
	# Act: pick Pilsner, then Chadwick.
	m.press("interact")
	m.press("move_down")
	m.press("interact")
	# Assert
	assert_eq(s.party.map(func(p): return p["id"]), ["chadwick", "lord_pilsner"])


func test_field_menu_currency_stays_out_of_the_bag() -> void:
	# Arrange
	var s := FakeState.new()
	s.inventory = {"item_absinthe_arcade_token": 4, "arcade_tickets": 10, "lukewarm_kebab": 2}
	# Act
	var ids := _menu(s).bag().map(func(r): return r["id"])
	# Assert
	assert_eq(ids, ["lukewarm_kebab"])


func test_field_menu_drinking_absinthe_costs_ten_minutes_and_food_doesnt() -> void:
	# Arrange: an Absinthe Shot (alcohol) and a Lukewarm Kebab (food).
	var s := FakeState.new()
	s.inventory = {"absinthe_shot": 1, "lukewarm_kebab": 1}
	s.party[0]["bravado"] = 2
	var m := _menu(s)
	# Act
	m.use_on("lukewarm_kebab", 0)
	var after_food := GameClock.watch_text(s)
	m.use_on("absinthe_shot", 0)
	# Assert
	assert_eq(after_food, "10:00")
	assert_eq(GameClock.watch_text(s), "10:10")


func test_field_menu_watch_caption_stays_readable_on_the_1080_base_window() -> void:
	# Arrange: 18 px on the 1920x1080 base showed at about 13 px at 1366x768 (Eurobound-z3ec).
	var m := _menu(FakeState.new())
	# Act
	var caption: Label = null
	for n in m.find_children("*", "Label", true, false):
		if (n as Label).text == "Lord Pilsner's watch":
			caption = n
	# Assert
	assert_not_null(caption)
	assert_gte(caption.get_theme_font_size("font_size"), 20)


# --- Eurobound-81oy: field-menu use goes through the same status calls as GameState.use_item ---

func test_field_menu_drinking_grist_puts_both_statuses_on_the_chosen_bro_only() -> void:
	# Arrange: Windmill Grist = Navigation penalty + Speed buff (intoxicant.also), picked for bro 1.
	var s := FakeState.new()
	s.inventory = {"beer_wobbly_windmill_brewery": 1}
	var m := _menu(s)
	# Act
	var used := m.use_on("beer_wobbly_windmill_brewery", 1)
	# Assert
	assert_true(used)
	assert_true(FieldStatus.has(s, "wobbly_windmill_navigation", "chadwick"))
	assert_true(FieldStatus.has(s, "wobbly_windmill_speed", "chadwick"))
	assert_false(FieldStatus.has(s, "wobbly_windmill_navigation", "lord_pilsner"))


func test_field_menu_use_cures_what_the_status_table_says_the_item_cures() -> void:
	# Arrange: Cottonmouth is cured by any drink (cured_by item_subtype drink); the shot is on bro 1.
	var s := FakeState.new()
	s.inventory = {"absinthe_shot": 1}
	FieldStatus.apply_steps(s, "chadwick", "cottonmouth", 100, -1)
	FieldStatus.apply_steps(s, "lord_pilsner", "cottonmouth", 100, -1)
	var m := _menu(s)
	# Act
	var used := m.use_on("absinthe_shot", 1)
	# Assert
	assert_true(used)
	assert_false(FieldStatus.has(s, "cottonmouth", "chadwick"))
	assert_true(FieldStatus.has(s, "cottonmouth", "lord_pilsner"), "only the chosen bro is cured")


func test_field_menu_usable_in_field_counts_status_effects_not_only_healing() -> void:
	# Arrange / Assert: no heal, but it does something in the field.
	var drink := {"_group": "consumables", "usable_in": ["field"], "intoxicant": {"status": "x"}}
	var cut := {"_group": "consumables", "shortens_status": [{"status": "the_shakes", "battle_turns": 1, "field_steps": 40}]}
	var battle_only := {"_group": "consumables", "usable_in": ["battle"], "intoxicant": {"status": "x"}}
	var dud := {"_group": "consumables"}
	assert_true(FieldMenu.usable_in_field(drink))
	assert_true(FieldMenu.usable_in_field(cut))
	assert_false(FieldMenu.usable_in_field(battle_only))
	assert_false(FieldMenu.usable_in_field(dud))
