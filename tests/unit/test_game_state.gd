extends GutTest

var repo
var state

func before_each() -> void:
	repo = load("res://Scripts/core/data_repo.gd").new()
	repo.load_all()
	state = load("res://Scripts/systems/GameState.gd").new()
	state.new_game(repo)

func test_new_game_builds_party_from_data() -> void:
	assert_eq(state.party.size(), 1)
	assert_eq(state.party[0]["id"], "lord_pilsner")
	assert_eq(int(state.party[0]["hp"]), 45)
	assert_eq(int(state.party[0]["sp"]), 12)

func test_add_and_use_item() -> void:
	state.add_item("lukewarm_kebab")
	state.party[0]["hp"] = 10
	assert_true(state.use_item("lukewarm_kebab", repo))
	assert_eq(int(state.party[0]["hp"]), 30)
	assert_false(state.use_item("lukewarm_kebab", repo), "second use should fail — none left")

func test_use_item_caps_at_max_hp() -> void:
	state.add_item("lukewarm_kebab")
	state.party[0]["hp"] = 40
	state.use_item("lukewarm_kebab", repo)
	assert_eq(int(state.party[0]["hp"]), 45)

func test_flags() -> void:
	assert_false(state.has_flag("vlad_insulted"))
	state.set_flag("vlad_insulted")
	assert_true(state.has_flag("vlad_insulted"))

func test_grant_rewards() -> void:
	state.grant_rewards(12, 8, "lukewarm_kebab")
	assert_eq(int(state.party[0]["xp"]), 12)
	assert_eq(state.gold, 8)
	assert_eq(int(state.inventory.get("lukewarm_kebab", 0)), 1)

func test_round_trip() -> void:
	state.add_item("absinthe_shot", 2)
	state.set_flag("test_flag")
	state.gold = 99
	state.player_position = Vector2(120, 88)
	state.current_scene_path = "res://Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn"
	var d: Dictionary = state.to_dict()
	var restored = load("res://Scripts/systems/GameState.gd").new()
	restored.from_dict(d)
	assert_eq(restored.to_dict(), d)
