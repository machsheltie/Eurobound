extends GutTest

var repo

func before_each() -> void:
	repo = load("res://core/data_repo.gd").new()

func test_load_succeeds_with_empty_key_items_and_equipment() -> void:
	assert_true(repo.load_all(), "load_all should succeed even though key_items.json and equipment.json are empty")

func test_key_item_lookup_returns_empty_for_missing_id() -> void:
	repo.load_all()
	assert_eq(repo.get_key_item("nonexistent_item"), {})

func test_equipment_lookup_returns_empty_for_missing_id() -> void:
	repo.load_all()
	assert_eq(repo.get_equipment("nonexistent_item"), {})
