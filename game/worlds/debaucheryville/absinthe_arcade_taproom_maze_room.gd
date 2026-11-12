@tool
class_name TaproomMazeRoom
extends HD2DProjectedRoom
## Shared base for the two Absinthium Taproom mirror-maze screens (M1 = sections 1-4, M5 = section 5;
## design/worlds/debaucheryville/the_absinthium_taproom.md 63-68, 94-103, 140-150; art approved round
## v43, connection round v44: curtain -> maze -> Taproom). One scene per plate: the section is
## re-dressed from data/taproom_maze/sections.json, never copied. Subclasses give the paint camera
## (fitted from each plate's checker floor), the floor extent and the niche table.
##
## Niche table entry: id -> {wall: back|left|right, pos: Vector3(x, base_y, z) in tiles on the wall
## plane (base_y = bottom of the mirror), h: mirror height in tiles}. The mirror art is 535x1515.

const MIRROR_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/taproom_maze/props/"
const MIRROR_ASPECT := 535.0 / 1515.0
const OTHER_SCENE := {"m1": "absinthe_arcade_taproom_maze_m5", "m5": "absinthe_arcade_taproom_maze_m1"}
const TAPROOM_TARGET := "absinthe_arcade_taproom"

var plate_id := "m1"  ## which plate this screen is (m1 / m5)
var floor_half_width := 6.9
var floor_depth := 12.0  ## the floor runs z = 0 .. floor_depth
var niches := {}  ## see header
var stand_spots := {}  ## niche id -> Vector2 floor spot (x, z) in front of it
var default_spawn_xz := Vector2(0, 10)
var has_exit_arch := false
var arch_half_width := 2.4

var maze: TaproomMaze
var sprites := {}  ## niche id -> Sprite3D
var _player: PlayerController


func _build_room() -> void:
	var mat := _paint_material()
	var far := cam_z
	var w := floor_half_width
	var wx := w + 0.4
	for n: Dictionary in niches.values():
		wx = maxf(wx, absf(Vector3(n["pos"]).x) + 0.3)  # keep the painted wall behind every mirror
	_wall("back_wall", Vector2(-w - 3.0, 0), Vector2(w + 3.0, 0), 20.0, mat)
	_wall("left_wall", Vector2(-wx, far), Vector2(-wx, 0), 20.0, mat)
	_wall("right_wall", Vector2(wx, 0), Vector2(wx, far), 20.0, mat)
	_floor("floor", Vector2(0, far * 0.5), Vector2(2.0 * w + 6.0, far + 0.5), mat)
	var body := _collision_body("room_collision")
	_box(body, Vector3(0, -0.1, far * 0.5), Vector3(2.0 * w + 6.0, 0.2, far + 0.5))
	_wall_collider(body, Vector2(-w, 0.0), Vector2(w, 0.0))
	_wall_collider(body, Vector2(-w, floor_depth + 1.2), Vector2(w, floor_depth + 1.2))
	_wall_collider(body, Vector2(-w, 0.0), Vector2(-w, floor_depth + 1.2))
	_wall_collider(body, Vector2(w, 0.0), Vector2(w, floor_depth + 1.2))


func _build_markers() -> void:
	SceneRouter.add_spawn_point(_diorama, "default", Vector3(default_spawn_xz.x, 0, default_spawn_xz.y), "north")
	SceneRouter.add_spawn_point(_diorama, "from_curtain", Vector3(default_spawn_xz.x, 0, default_spawn_xz.y), "north")
	SceneRouter.add_spawn_point(_diorama, "from_maze", Vector3(default_spawn_xz.x, 0, default_spawn_xz.y), "north")
	for id: String in niches.keys():
		var p: Vector3 = niches[id]["pos"]
		var m := Marker3D.new()
		m.name = "interact_" + id
		m.position = Vector3(p.x, 0.0, p.z)
		m.add_to_group("interact_points")
		m.set_meta("interact_id", "maze:" + id)
		_diorama.add_child(m)
	if has_exit_arch:
		var a := Area3D.new()
		a.name = "exit_archway"
		var cs := CollisionShape3D.new()
		var box := BoxShape3D.new()
		box.size = Vector3(arch_half_width * 2.0, 2.0, 1.2)
		cs.shape = box
		cs.position = Vector3(0, 1.0, 0.5)
		a.add_child(cs)
		_diorama.add_child(a)
		if not Engine.is_editor_hint():
			a.body_entered.connect(func(body: Node3D) -> void:
				if body is PlayerController:
					use_exit())


func _ready() -> void:
	var arrived_from_maze := SceneRouter.pending_spawn == "from_maze"
	if not Engine.is_editor_hint():
		maze = TaproomMaze.new(GameState)
		if SceneRouter.pending_spawn == "from_curtain":
			maze.start_run()
	super()
	_dress()
	if Engine.is_editor_hint() or not spawn_player:
		return
	var players := get_tree().get_nodes_in_group("player").filter(func(n): return is_ancestor_of(n))
	if not players.is_empty():
		_player = players.front()
		_player.interacted.connect(_on_interacted)
		if arrived_from_maze:
			_maybe_start_chad.call_deferred()  # a Portal can land the bros in section 3 on this plate


func _process(delta: float) -> void:
	if maze == null:
		return
	var was := maze.revealed()
	maze.tick(delta)
	if was != maze.revealed():
		_refresh_textures()


func _mirror_texture(type: String, revealed: bool) -> Texture2D:
	return load(MIRROR_DIR + "mirror_%s_%s.png" % [type, "revealed" if revealed else "rest"])


## Builds (once) and re-dresses the niche mirrors for the current section.
func _dress() -> void:
	if maze == null or _diorama == null:
		return
	for id: String in niches.keys():
		var spr: Sprite3D = sprites.get(id)
		if spr == null:
			spr = _make_sprite(id)
			sprites[id] = spr
	_refresh_textures()


func _make_sprite(id: String) -> Sprite3D:
	var n: Dictionary = niches[id]
	var p: Vector3 = n["pos"]
	var h: float = n["h"]
	var spr := Sprite3D.new()
	spr.name = "mirror_" + id
	spr.shaded = false
	spr.double_sided = true
	spr.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	spr.pixel_size = h / 1515.0
	var inset := 0.05
	match String(n["wall"]):
		"back":
			spr.position = Vector3(p.x, p.y + h * 0.5, p.z + inset)
		"left":
			spr.position = Vector3(p.x + inset, p.y + h * 0.5, p.z)
			spr.rotation.y = PI * 0.5
		_:
			spr.position = Vector3(p.x - inset, p.y + h * 0.5, p.z)
			spr.rotation.y = -PI * 0.5
	_diorama.add_child(spr)
	return spr


func _refresh_textures() -> void:
	for id: String in sprites.keys():
		var spr: Sprite3D = sprites[id]
		var t := maze.mirror_at(id)
		spr.visible = t != ""
		if t != "":
			spr.texture = _mirror_texture(t, maze.revealed())


func _on_interacted(interact_id: String) -> void:
	if interact_id.begins_with("maze:"):
		use_niche(interact_id.substr(5))


## Uses the mirror in `niche_id` and applies the result to the screen.
func use_niche(niche_id: String) -> Dictionary:
	var res := maze.use_niche(niche_id)
	if res["action"] == "section":
		if maze.plate_of() != plate_id:
			SceneRouter.travel(get_tree(), OTHER_SCENE[plate_id], "from_maze")
		else:
			_dress()
			_maybe_start_chad.call_deferred()
	elif res["action"] == "status":
		_refresh_textures()
	return res


## Mirror Chad (v45): starts as the bros enter section 3, once per visit, until defeated. A loss
## (arcade loss rule) leaves them here in section 3 with the run state untouched.
func _maybe_start_chad() -> void:
	if maze == null or _player == null or not is_inside_tree() or not maze.take_chad():
		return
	await TaproomFights.run(self, _player, TaproomBattle.MIRROR_CHAD, GameState)


## Walking out through the open archway of section 5: the maze is done, on to the Taproom.
func use_exit() -> Dictionary:
	var res := maze.use_exit()
	SceneRouter.travel(get_tree(), TAPROOM_TARGET, "from_maze")
	return res
