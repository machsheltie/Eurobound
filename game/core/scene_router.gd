class_name SceneRouter
extends RefCounted
## Moves the player between screens. Each world scene marks:
##  - exits: Area3D in group "scene_exits" with meta target_scene (a screen id below) and
##    target_spawn (a spawn id in that screen);
##  - spawn points: Marker3D in group "spawn_points" with meta spawn_id and facing.
## A world calls spawn_player() and wire_exits() from _ready. Walking into an exit stores the
## spawn id and changes scene; the new screen then spawns the player on that point.

const SCENES := {
	"absinthe_arcade_exterior": "res://worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn",
	"absinthe_arcade_interior": "res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn",
	"absinthe_arcade_mirror_corridor": "res://worlds/debaucheryville/absinthe_arcade_mirror_corridor_hd2d.tscn",
	"absinthe_arcade_north_wing": "res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.tscn",
	"absinthe_arcade_restroom": "res://worlds/debaucheryville/absinthe_arcade_restroom_hd2d.tscn",
	"absinthe_arcade_maintenance_closet": "res://worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.tscn",
	"absinthe_arcade_taproom_maze_m1": "res://worlds/debaucheryville/absinthe_arcade_taproom_maze_m1_hd2d.tscn",
	"absinthe_arcade_taproom_maze_m5": "res://worlds/debaucheryville/absinthe_arcade_taproom_maze_m5_hd2d.tscn",
	"absinthe_arcade_taproom": "res://worlds/debaucheryville/absinthe_arcade_taproom_hd2d.tscn",
}

## Spawn id the next screen should put the player on ("" = that screen's default).
static var pending_spawn := ""
## A loaded save's player spot (GameState.player_spot). Set by SaveSystem.prepare_resume; the
## next spawn_player puts the leader there instead of on a spawn point, then clears it.
static var pending_spot := {}


static func scene_path(screen_id: String) -> String:
	return SCENES.get(screen_id, "")


## Changes to `screen_id`, arriving at `spawn_id`. Returns false (and stays put) for a screen
## that is not built yet.
static func travel(tree: SceneTree, screen_id: String, spawn_id: String) -> bool:
	var path := scene_path(screen_id)
	if path.is_empty():
		push_warning("SceneRouter: screen '%s' is not built yet" % screen_id)
		return false
	pending_spawn = spawn_id
	var state := tree.root.get_node_or_null("GameState")
	if state != null:
		GameClock.act(state, "screen")  # round v35: a screen change costs 10 minutes
	tree.change_scene_to_file.call_deferred(path)
	return true


## Creates the player in `world` on the pending spawn point, or on `default_spawn`.
## Launched straight into a screen (no title screen exists yet), start a new game so the
## wallet and party exist.
static func ensure_game_started(tree: SceneTree) -> void:
	DebugCommands.register(tree)  # debug builds only (Eurobound-08bo)
	var state := tree.root.get_node_or_null("GameState")
	var repo := tree.root.get_node_or_null("DataRepo")
	if state != null and repo != null and (state.party as Array).is_empty():
		state.new_game(repo)


static func spawn_player(world: Node3D, default_spawn: String) -> PlayerController:
	var wanted := pending_spawn if not pending_spawn.is_empty() else default_spawn
	pending_spawn = ""
	var marker: Node3D = null
	for n in world.get_tree().get_nodes_in_group("spawn_points"):
		if world.is_ancestor_of(n) and String(n.get_meta("spawn_id")) == wanted:
			marker = n
			break
	var player := PlayerController.new()
	player.name = "player"
	# Placed BEFORE entering the tree: added at the origin first, the player would touch any exit
	# there (the street door sits at the origin) and travel on the first physics frame.
	var spot := pending_spot
	pending_spot = {}
	if not spot.is_empty():
		player.position = Vector3(float(spot.get("x", 0.0)), float(spot.get("y", 0.0)), float(spot.get("z", 0.0)))
		player.sprite.facing = String(spot.get("facing", "south"))
	elif marker != null:
		player.position = world.global_transform.affine_inverse() * marker.global_position
		player.sprite.facing = String(marker.get_meta("facing", "south"))
	world.add_child(player)
	return player


## Connects every exit in `world` so the player walking into it travels.
static func wire_exits(world: Node) -> void:
	for n in world.get_tree().get_nodes_in_group("scene_exits"):
		if not world.is_ancestor_of(n):
			continue
		var exit := n as Area3D
		exit.body_entered.connect(func(body: Node3D) -> void:
			if body is PlayerController:
				travel(world.get_tree(), String(exit.get_meta("target_scene")), String(exit.get_meta("target_spawn", ""))))


## Adds a spawn point (real-metre position under `parent`'s space) for `spawn_player`.
static func add_spawn_point(parent: Node3D, spawn_id: String, pos: Vector3, facing: String) -> Marker3D:
	var m := Marker3D.new()
	m.name = "spawn_" + spawn_id
	m.position = pos
	m.add_to_group("spawn_points")
	m.set_meta("spawn_id", spawn_id)
	m.set_meta("facing", facing)
	parent.add_child(m)
	return m
