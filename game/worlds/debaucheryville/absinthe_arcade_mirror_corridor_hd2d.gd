@tool
extends HD2DProjectedRoom
## HD-2D Absinthe Arcade mirror corridor: the screen between the hall's north arch and the north
## wing (author ruling: its own screen). Built from mirror corridor v1 (night/day).
##
## Paint camera, measured 2026-11-10 from v1's square-to-camera checkerboard (least-squares fit of
## 13 tile rows and the tile widths at three heights): focal 2565 px at 2752 px wide, pitch 19.5
## deg, camera 7.13 tiles above the floor. Painting units here are floor tiles; the benches
## (3.4 x 0.8 tiles, ~1.9 m long) put a tile at 0.55 m.

## Corridor box in tiles: side walls at x = +-WALL_X, far wall at z = 0, the screen's bottom edge
## on the floor at z = FRONT_Z.
const WALL_X := 4.9
const WALL_HEIGHT := 14.0
const FRONT_Z := 15.55
## The far archway to the north wing (measured: floor-line corners x -1.39 / +1.47).
const ARCH := {"x0": -1.42, "x1": 1.42, "height": 5.0, "depth": 6.0}
const NORTH_EXIT_TARGET := "absinthe_arcade_north_wing"
const SOUTH_EXIT_TARGET := "absinthe_arcade_interior"

const SPAWNS := {
	"from_hall": [Vector2(0.0, 13.2), "north"],
	"from_north_wing": [Vector2(0.0, 1.6), "south"],
}

## Benches and potted palms against the walls, [centre (x, z), size (x, z)] in tiles, from the
## painting (bench legs and pot bases projected to the floor).
const FLOOR_BLOCKERS := [
	[Vector2(-4.55, 13.2), Vector2(0.9, 3.6)],    # near benches
	[Vector2(4.55, 13.2), Vector2(0.9, 3.6)],
	[Vector2(-4.1, 7.0), Vector2(1.3, 1.3)],      # near palms
	[Vector2(4.1, 7.0), Vector2(1.3, 1.3)],
	[Vector2(-3.4, 2.6), Vector2(1.0, 2.6)],      # far benches
	[Vector2(3.4, 2.6), Vector2(1.0, 2.6)],
	[Vector2(-2.4, 0.6), Vector2(1.0, 1.0)],      # palms flanking the arch
	[Vector2(2.4, 0.6), Vector2(1.0, 1.0)],
]

## The three shadow switches [anchor (x, z), where the bro stands] in tiles, on open floor along the
## mirrored walls (design: mirror_shadow_puzzle, switch_count 3). Index = switch index in
## MirrorShadowPuzzle.SOLUTION.
const SWITCHES := [
	[Vector2(-3.7, 10.0), Vector2(-2.8, 10.0)],
	[Vector2(3.7, 9.0), Vector2(2.8, 9.0)],
	[Vector2(-3.7, 4.6), Vector2(-2.8, 4.6)],
]
## Placeholder switch art: put off/on sprite paths here when the art team delivers; while either
## is empty the glowing disc is used.
const SWITCH_TEXTURES := {"off": "", "on": ""}
const AFTERIMAGE_ALPHA := 0.4
const AFTERIMAGE_LEG_SEC := 1.4
const AFTERIMAGE_PAUSE_SEC := 0.6
## Gap before an afterimage run starts and between runs: the image is "a beat behind".
const AFTERIMAGE_LEAD_SEC := 1.5
const AFTERIMAGE_REST_SEC := 4.0
const SWITCH_COLOR := Color(0.7, 0.3, 1.0)

var puzzle := MirrorShadowPuzzle.new()
var _player: PlayerController
var _discs: Array[Node3D] = []
var _hint: Node3D
var _hint_tween: Tween


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/mirror_corridor/aa_int_corridor_"
	focal_px = 2565.0
	pitch_deg = 19.5
	cam_height = 7.13
	cam_z = 25.3
	world_scale = 0.55
	default_spawn = "from_hall"


func _build_room() -> void:
	var mat := _paint_material()
	var x0: float = ARCH["x0"]
	var x1: float = ARCH["x1"]
	var ah: float = ARCH["height"]
	var deep: float = -float(ARCH["depth"])
	var lb := Vector2(-WALL_X, 0)
	var rb := Vector2(WALL_X, 0)
	var front := FRONT_Z + 3.0
	_wall("far_wall_left", lb, Vector2(x0, 0), WALL_HEIGHT, mat)
	_wall("far_wall_right", Vector2(x1, 0), rb, WALL_HEIGHT, mat)
	var lintel := _wall("far_wall_lintel", Vector2(x0, 0), Vector2(x1, 0), WALL_HEIGHT - ah, mat)
	lintel.position.y = ah
	_wall("arch_left", Vector2(x0, 0), Vector2(x0, deep), ah, mat)
	_wall("arch_right", Vector2(x1, deep), Vector2(x1, 0), ah, mat)
	_wall("arch_end", Vector2(x0, deep), Vector2(x1, deep), ah, mat)
	_floor("arch_floor", Vector2((x0 + x1) * 0.5, deep * 0.5), Vector2(x1 - x0, -deep), mat)
	_wall("left_wall", Vector2(-WALL_X, front), lb, WALL_HEIGHT, mat)
	_wall("right_wall", rb, Vector2(WALL_X, front), WALL_HEIGHT, mat)
	_floor("floor", Vector2(0, front * 0.5), Vector2(WALL_X * 2.0 + 2.0, front + 0.5), mat)

	var body := _collision_body("room_collision")
	_box(body, Vector3(0, -0.1, front * 0.5), Vector3(WALL_X * 2.0 + 2.0, 0.2, front + 0.5))
	_box(body, Vector3((x0 + x1) * 0.5, -0.1, deep * 0.5), Vector3(x1 - x0 + 0.6, 0.2, -deep))
	for seg: Array in [[lb, Vector2(x0, 0)], [Vector2(x1, 0), rb],
			[Vector2(-WALL_X, front), lb], [rb, Vector2(WALL_X, front)],
			[Vector2(x0, 0), Vector2(x0, deep)], [Vector2(x1, deep), Vector2(x1, 0)],
			[Vector2(x0, deep), Vector2(x1, deep)]]:
		_wall_collider(body, seg[0], seg[1])
	for spec: Array in FLOOR_BLOCKERS:
		var c: Vector2 = spec[0]
		var sz: Vector2 = spec[1]
		_box(body, Vector3(c.x, 1.0, c.y), Vector3(sz.x, 2.0, sz.y))
	# Behind the south exit, so walking through it never steps off the floor.
	_wall_collider(body, Vector2(-WALL_X, FRONT_Z + 1.2), Vector2(WALL_X, FRONT_Z + 1.2))


func _build_markers() -> void:
	var x0: float = ARCH["x0"]
	var x1: float = ARCH["x1"]
	_exit("exit_south_to_hall", SOUTH_EXIT_TARGET, "from_mirror_corridor",
		Vector3(0, 1.0, FRONT_Z + 0.4), Vector3(WALL_X * 2.0, 2.0, 0.8))
	_exit("exit_north_arch", NORTH_EXIT_TARGET, "from_mirror_corridor",
		Vector3((x0 + x1) * 0.5, 1.0, -0.6), Vector3(x1 - x0, 2.0, 0.8))
	if SceneRouter.scene_path(NORTH_EXIT_TARGET).is_empty():
		# Until the north wing screen exists, a stop just behind the trigger.
		var stop := _collision_body("arch_unbuilt_stop")
		_wall_collider(stop, Vector2(x0, -1.3), Vector2(x1, -1.3))
	_spawns(SPAWNS)
	_add_switches()


static func switch_id(i: int) -> String:
	return "shadow_switch_%d" % (i + 1)


static func _facing(dir: Vector3) -> String:
	var best := "south"
	var best_dot := -2.0
	for d: String in PartySprite3D.DIRECTIONS:
		var dot := PlayerController.facing_vector(d).dot(dir.normalized())
		if dot > best_dot:
			best_dot = dot
			best = d
	return best


func _add_switches() -> void:
	for i in SWITCHES.size():
		var at: Vector2 = SWITCHES[i][0]
		var stand: Vector2 = SWITCHES[i][1]
		var m := Marker3D.new()
		m.name = switch_id(i)
		m.position = Vector3(at.x, 0, at.y)
		m.add_to_group("interact_points")
		m.set_meta("interact_id", switch_id(i))
		_diorama.add_child(m)
		var toward := (at - stand).normalized()
		SceneRouter.add_spawn_point(_diorama, "at_" + switch_id(i), Vector3(stand.x, 0, stand.y),
			_facing(Vector3(toward.x, 0, toward.y)))


func _ready() -> void:
	super()
	if Engine.is_editor_hint() or not spawn_player:
		return
	var found := get_tree().get_nodes_in_group("player").filter(func(n): return is_ancestor_of(n))
	_player = found.front() if not found.is_empty() else null
	if _player != null:
		_player.interacted.connect(_on_interacted)
	for i in SWITCHES.size():
		_discs.append(_make_switch_visual(i))
	_refresh_discs()
	if not MirrorShadowPuzzle.solved(GameState):
		_start_hint()


## Switch visual: the off/on sprite once SWITCH_TEXTURES names them, else a placeholder glowing disc.
func _make_switch_visual(i: int) -> Node3D:
	var at: Vector2 = SWITCHES[i][0]
	var mi := MeshInstance3D.new()
	mi.name = "switch_visual_%d" % (i + 1)
	var disc := CylinderMesh.new()
	disc.top_radius = 0.35
	disc.bottom_radius = 0.35
	disc.height = 0.06
	mi.mesh = disc
	mi.position = Vector3(at.x, 0.05, at.y)
	_diorama.add_child(mi)
	return mi


func _set_disc(i: int, lit: bool) -> void:
	var mat := StandardMaterial3D.new()
	mat.albedo_color = SWITCH_COLOR if lit else SWITCH_COLOR.darkened(0.75)
	mat.emission_enabled = lit
	mat.emission = SWITCH_COLOR
	mat.emission_energy_multiplier = 2.5
	(_discs[i] as MeshInstance3D).material_override = mat


func _is_lit(i: int) -> bool:
	return MirrorShadowPuzzle.solved(GameState) or MirrorShadowPuzzle.SOLUTION.slice(0, puzzle.progress).has(i)


func _refresh_discs() -> void:
	for i in _discs.size():
		_set_disc(i, _is_lit(i))


func _on_interacted(id: String) -> void:
	for i in SWITCHES.size():
		if id == switch_id(i):
			var r := puzzle.press(GameState, i)
			_refresh_discs()
			if r == "solved":
				_clear_hint()
			return


func _afterimage() -> PartySprite3D:
	var s := PartySprite3D.new()
	s.name = "afterimage"
	s.sprite_frames = _player.sprite.sprite_frames
	s.content_height_px = _player.sprite.content_height_px
	s.feet_row_px = _player.sprite.feet_row_px
	s.add_to_group("hall_actors")
	_hint.add_child(s, true)
	s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISABLED
	s.modulate = Color(0.75, 0.6, 1.0, AFTERIMAGE_ALPHA)
	s.shaded = false
	s.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	s.facing = "west"
	s.action = "idle"
	return s


func _stand_pos(i: int) -> Vector3:
	var st: Vector2 = SWITCHES[i][1]
	return Vector3(st.x, 0, st.y)


## The hint: a delayed afterimage of the leader visits the switches in solution order. With
## reduced motion on, static offset afterimages stand at each switch with numbered floor markers.
func _start_hint() -> void:
	if _player == null:
		return
	_clear_hint()
	_hint = Node3D.new()
	_hint.name = "afterimage_hint"
	_diorama.add_child(_hint)
	if ArcadeAmbientFx.is_reduced(GameState):
		for n in MirrorShadowPuzzle.SOLUTION.size():
			var i: int = MirrorShadowPuzzle.SOLUTION[n]
			var still := _afterimage()
			still.position = _stand_pos(i)
			var label := Label3D.new()
			label.name = "floor_number_%d" % (n + 1)
			label.text = str(n + 1)
			label.font_size = 96
			label.pixel_size = 0.01
			label.modulate = SWITCH_COLOR
			label.rotation_degrees = Vector3(-90, 0, 0)
			label.position = _stand_pos(i) + Vector3(0, 0.03, 0.9)
			_hint.add_child(label)
		return
	var img := _afterimage()
	img.visible = false
	_hint_tween = create_tween().set_loops()
	_hint_tween.tween_interval(AFTERIMAGE_LEAD_SEC)
	var first := true
	for i: int in MirrorShadowPuzzle.SOLUTION:
		if first:
			_hint_tween.tween_callback(func() -> void:
				img.position = _stand_pos(i) + Vector3(0, 0, 4.0)
				img.visible = true)
			first = false
		_hint_tween.tween_property(img, "position", _stand_pos(i), AFTERIMAGE_LEG_SEC)
		_hint_tween.tween_callback(func() -> void: _pulse(i, true))
		_hint_tween.tween_interval(AFTERIMAGE_PAUSE_SEC)
		_hint_tween.tween_callback(func() -> void: _pulse(i, false))
	_hint_tween.tween_callback(func() -> void: img.visible = false)
	_hint_tween.tween_interval(AFTERIMAGE_REST_SEC)


func _pulse(i: int, on: bool) -> void:
	if i < _discs.size() and not MirrorShadowPuzzle.solved(GameState):
		_set_disc(i, on or _is_lit(i))


func _clear_hint() -> void:
	if _hint_tween != null:
		_hint_tween.kill()
		_hint_tween = null
	if _hint != null:
		_hint.queue_free()
		_hint = null
