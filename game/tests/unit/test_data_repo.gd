extends GutTest

var repo

func before_each() -> void:
	repo = load("res://Scripts/core/data_repo.gd").new()
	assert_true(repo.load_all(), "load_all should succeed with valid data files")

func test_party_member_lord_pilsner() -> void:
	var p: Dictionary = repo.get_party_member("lord_pilsner")
	assert_eq(p.get("display_name"), "Lord Pilsner")
	assert_eq(int(p.get("max_hp")), 45)

func test_enemy_lookup() -> void:
	var e: Dictionary = repo.get_enemy("feral_segway_tourist")
	assert_eq(int(e.get("max_hp")), 28)
	assert_eq(e.get("item_drop"), "lukewarm_kebab")

func test_item_lookup() -> void:
	var i: Dictionary = repo.get_item("lukewarm_kebab")
	assert_eq(int(i.get("heal_hp")), 20)

func test_ability_lookup() -> void:
	var a: Dictionary = repo.get_ability("roast_line")
	assert_eq(int(a.get("sp_cost")), 4)

func test_dialogue_tree_vlad() -> void:
	var t: Dictionary = repo.get_dialogue_tree("vlad_validator")
	assert_true(t.has("default_greeting"))
	var greeting: Dictionary = t["default_greeting"]
	assert_true(greeting.has("text"))
	assert_true(greeting.has("options"))

func test_unknown_id_returns_empty() -> void:
	assert_eq(repo.get_enemy("nonexistent_enemy"), {})
