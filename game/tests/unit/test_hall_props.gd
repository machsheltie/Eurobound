extends GutTest
## The Absinthe Arcade hall's interactable prop cut-outs (PlatePropLayer, author round v43): every prop
## loads with its states, set_state swaps the texture, day/night finds every file, the token machine
## walks accepting_payment -> dispensing_tokens -> idle, and a cabinet goes in_use -> attract.

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
const EXPECTED_STATES := {
	"cab_frogger": ["attract", "in_use"],
	"cab_street_fighter": ["attract", "in_use"],
	"cab_kebab_kombat": ["attract", "in_use"],
	"ddr_screen": ["attract", "song_select", "playing", "results_good", "results_bad"],
	"ddr_pads": ["idle", "lit"],
	"token_machine": ["idle", "accepting_payment", "dispensing_tokens", "temporarily_jammed"],
	"bar_counter": ["default"],
	"prize_counter": ["default"],
}

var _hall: Node3D
var _saved := {}


func before_each() -> void:
	_saved = {"sovs": GameState.sovs, "inventory": GameState.inventory.duplicate(true),
		"party": GameState.party.duplicate(true), "flags": GameState.flags.duplicate(true)}
	GameState.sovs = 0
	GameState.inventory = {}
	_hall = SCENE.instantiate()
	add_child_autofree(_hall)
	await wait_physics_frames(3)
	_hall.prop_step_seconds = 0.05


func after_each() -> void:
	GameState.sovs = _saved["sovs"]
	GameState.inventory = _saved["inventory"]
	GameState.party = _saved["party"]
	GameState.flags = _saved["flags"]
	SceneRouter.pending_spawn = ""


func test_hall_props_every_prop_loads_with_all_its_states() -> void:
	# Arrange / Act
	var props: PlatePropLayer = _hall.props

	# Assert
	for id: String in EXPECTED_STATES.keys():
		assert_true(props.has_prop(id), id)
		var got := props.states_of(id)
		got.sort()
		var want: Array = EXPECTED_STATES[id].duplicate()
		want.sort()
		assert_eq(got, want, id + " states")


func test_hall_props_default_states_match_the_plate() -> void:
	# Arrange / Act
	var props: PlatePropLayer = _hall.props

	# Assert
	for id: String in ["cab_frogger", "cab_street_fighter", "cab_kebab_kombat", "ddr_screen"]:
		assert_eq(props.state_of(id), "attract", id)
	assert_eq(props.state_of("ddr_pads"), "idle")
	assert_eq(props.state_of("token_machine"), "idle")
	assert_eq(props.state_of("bar_counter"), "default")
	assert_eq(props.state_of("prize_counter"), "default")


func test_hall_props_set_state_swaps_the_texture_and_rejects_unknown_states() -> void:
	# Arrange
	var props: PlatePropLayer = _hall.props
	var before := props.current_texture("cab_frogger")

	# Act
	var ok := props.set_state("cab_frogger", "in_use")
	var after := props.current_texture("cab_frogger")
	var bad_state := props.set_state("cab_frogger", "exploded")
	var bad_prop := props.set_state("no_such_prop", "idle")

	# Assert
	assert_true(ok)
	assert_ne(after.resource_path, before.resource_path)
	assert_false(bad_state)
	assert_false(bad_prop)
	assert_eq(props.state_of("cab_frogger"), "in_use", "a refused state changes nothing")


func test_hall_props_day_and_night_find_every_file() -> void:
	# Arrange
	var props: PlatePropLayer = _hall.props

	# Act / Assert
	for id: String in props.prop_ids():
		for state: String in props.states_of(id):
			for variant: String in ["day", "night", "emit"]:
				var path := props.texture_path(id, state, variant)
				assert_true(ResourceLoader.exists(path), "%s %s %s -> %s" % [id, state, variant, path])


func test_hall_props_night_switch_changes_the_texture_and_lights_emission() -> void:
	# Arrange
	var props: PlatePropLayer = _hall.props
	props.set_night(true)
	var night_tex := props.current_texture("token_machine").resource_path

	# Act
	props.set_night(false)
	var day_tex := props.current_texture("token_machine").resource_path

	# Assert
	assert_true(night_tex.ends_with("_idle_night.png"))
	assert_true(day_tex.ends_with("_idle_day.png"))


func test_hall_props_token_purchase_walks_the_machine_states() -> void:
	# Arrange
	var props: PlatePropLayer = _hall.props
	GameState.sovs = 10
	var seen: Array[String] = []

	# Act
	_hall._on_tokens_chosen(2)
	seen.append(props.state_of("token_machine"))
	await get_tree().create_timer(0.075).timeout
	seen.append(props.state_of("token_machine"))
	await get_tree().create_timer(0.1).timeout
	seen.append(props.state_of("token_machine"))

	# Assert
	assert_eq(seen, ["accepting_payment", "dispensing_tokens", "idle"] as Array[String])
	assert_eq(ArcadeRules.tokens(GameState), 2)


func test_hall_props_cabinet_goes_in_use_for_the_fight_then_back_to_attract() -> void:
	# Arrange
	var props: PlatePropLayer = _hall.props
	GameState.sovs = 0
	GameState.add_item(ArcadeRules.TOKEN_ID, 5)
	var player: PlayerController = get_tree().get_nodes_in_group("player").filter(func(n): return _hall.is_ancestor_of(n))[0]
	player.global_position = _spawn("at_cabinet_frogger").global_position
	player.face("north")

	# Act
	player.try_interact()
	var during := props.state_of("cab_frogger")
	var others := props.state_of("cab_street_fighter")
	_hall.battle_screen.finished.emit("run")
	var after := props.state_of("cab_frogger")

	# Assert
	assert_eq(during, "in_use")
	assert_eq(others, "attract", "only the cabinet being played changes")
	assert_eq(after, "attract")


func _spawn(id: String) -> Node3D:
	for n in get_tree().get_nodes_in_group("spawn_points"):
		if _hall.is_ancestor_of(n) and n.get_meta("spawn_id") == id:
			return n
	return null
