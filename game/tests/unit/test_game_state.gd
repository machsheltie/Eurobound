extends GutTest

var repo
var state

func before_each() -> void:
	repo = autofree(load("res://core/data_repo.gd").new())
	repo.load_all()
	state = autofree(load("res://core/game_state.gd").new())
	state.new_game(repo)

func test_new_game_builds_party_from_data() -> void:
	assert_eq(state.party.size(), 3)
	assert_eq(state.party[0]["id"], "lord_pilsner")
	assert_eq(state.party[1]["id"], "chadwick")
	assert_eq(state.party[2]["id"], "bradley")
	assert_eq(int(state.party[0]["hp"]), 45)
	assert_eq(int(state.party[0]["bravado"]), 12)

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
	assert_eq(state.sovs, 28)
	assert_eq(int(state.inventory.get("lukewarm_kebab", 0)), 1)

func test_round_trip() -> void:
	state.add_item("absinthe_shot", 2)
	state.set_flag("test_flag")
	state.sovs = 99
	state.player_position = Vector2(120, 88)
	state.current_scene_path = "res://worlds/debaucheryville/clocktower_plaza.tscn"
	var d: Dictionary = state.to_dict()
	var restored = autofree(load("res://core/game_state.gd").new())
	restored.from_dict(d)
	assert_eq(restored.to_dict(), d)

## Eurobound-ong0: a save from before the 2026-11-16 starting kits grew keeps its moves and
## gains the kit skills it lacks; nothing is ever removed.
func _old_shape_save() -> Dictionary:
	var d: Dictionary = state.to_dict()
	d["party"][0]["skills"] = ["roast_line"]
	d["party"][1]["skills"] = []
	d["party"][2]["skills"] = ["a_learned_extra"]
	return JSON.parse_string(JSON.stringify(d))

func test_from_dict_merges_missing_starting_kit_skills() -> void:
	var restored = autofree(load("res://core/game_state.gd").new())
	restored.from_dict(_old_shape_save(), repo)
	assert_eq(restored.party[0]["skills"], ["roast_line", "beer_belly_bash"])
	assert_eq(restored.party[1]["skills"], ["like_and_hype"])
	assert_has(restored.party[2]["skills"], "a_learned_extra", "never removes a skill")
	assert_has(restored.party[2]["skills"], "keg_smash")
	assert_has(restored.party[2]["skills"], "bro_do_you_even_lift")
	assert_eq(restored.party[2]["skills"].size(), 3)

func test_from_dict_merge_does_not_duplicate_on_current_save() -> void:
	var restored = autofree(load("res://core/game_state.gd").new())
	restored.from_dict(state.to_dict(), repo)
	assert_eq(restored.to_dict(), state.to_dict())

func test_from_dict_without_repo_leaves_skills_alone() -> void:
	var restored = autofree(load("res://core/game_state.gd").new())
	restored.from_dict(_old_shape_save())
	assert_eq(restored.party[1]["skills"], [])
