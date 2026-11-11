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
