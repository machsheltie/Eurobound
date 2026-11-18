@tool
extends HD2DProjectedRoom
## HD-2D Absinthe Arcade: the Claw Machine Maintenance Closet Restroom, behind the north wing's
## MAINTENANCE ONLY door (unlocked by the broken DDR). Built from closet v5 (approved round v38,
## night only: the room is windowless), with the uncensored pixel-graffiti decal (round v37) baked
## onto the left wall below the space invader.
##
## Paint camera, measured 2026-11-11 from v5's square-to-camera checkerboard (12 tile rows and tile
## widths at three heights, rows within ~2 px): focal 2108 px at 2752 px wide, pitch 19.5 deg,
## camera 8.43 tiles above the floor, 24.83 tiles from the back wall. The toilet (~0.8 m to the top
## of the tank) puts a tile at 0.28 m.
## Round v38 art_closet5 = approve_back: the bros walk only the back half of the floor (the front
## half would draw them too large); the door, toilet, sink, claw and graffiti are all back there.

const BACK_Z := 0.0
const LEFT_WALL := [Vector2(-2.56, 0.0), Vector2(-5.94, 13.76)]
const RIGHT_WALL := [Vector2(4.28, 0.0), Vector2(6.12, 13.76)]
const WALL_HEIGHT := 14.0
## The walkable floor stops here (round v38).
const WALK_LIMIT_Z := 7.6
## The door in the left wall (its base runs z 4.86 - 7.12).
const DOOR_Z := Vector2(4.86, 7.12)
const NORTH_WING_TARGET := "absinthe_arcade_north_wing"

const SPAWNS := {
	# A bro is ~0.9 tiles wide here (tiles are 0.28 m), so arrivals stand well clear of the door.
	"from_north_wing": [Vector2(-1.2, 6.0), "east"],
}

## Floor-standing fixtures, convex footprints (x, z) in tiles.
const FLOOR_BLOCKERS := [
	[Vector2(-0.5, 0.0), Vector2(1.0, 0.0), Vector2(1.0, 2.0), Vector2(-0.5, 2.0)],   # toilet
	[Vector2(2.0, 0.0), Vector2(3.4, 0.0), Vector2(3.4, 1.6), Vector2(2.0, 1.6)],     # mop bucket and bottles
]

## Interaction anchors [anchor (x, z), where the bro stands] in tiles, read off the night plate
## (2752 px wide; the toilet sits at the middle, ~60 px a tile at the back wall). The graffiti spots
## are approximate: the left wall's SMAAAASH, invader and pixel boobs, the right wall's cheat codes.
## The switch, joystick and haiku (Eurobound-ms3r) sit on the free left wall in front of the door, the
## wiring's junction box on the right wall at z ~7.6. The bros walk only z <= 7.6, so the joystick and
## haiku points stand out on the floor in front of their art, within reach of the walk limit: face
## west for the switch, south for the joystick (when it shows) or the haiku.
const INTERACT_POINTS := {
	ClosetProps.BLACKLIGHT_SWITCH: [Vector2(-4.25, 7.7), Vector2(-3.6, 7.4)],
	ClosetProps.DDR_TOILET: [Vector2(0.25, 0.0), Vector2(0.25, 2.6)],
	ClosetProps.CRT_MIRROR: [Vector2(-2.0, 0.0), Vector2(-2.0, 2.2)],
	ClosetProps.SOCK_CHUTE: [Vector2(2.8, 0.0), Vector2(2.8, 2.4)],
	ClosetProps.SPARKING_WIRING: [Vector2(4.9, 7.6), Vector2(4.0, 7.3)],
	ClosetProps.GRAFFITI_SMAAAASH: [Vector2(-3.0, 1.6), Vector2(-2.2, 1.6)],
	ClosetProps.GRAFFITI_JOYSTICK: [Vector2(-3.6, 9.0), Vector2(-3.4, 7.4)],
	ClosetProps.GRAFFITI_BOOBS: [Vector2(-3.2, 3.2), Vector2(-2.4, 3.2)],
	ClosetProps.GRAFFITI_HAIKU: [Vector2(-4.5, 10.0), Vector2(-3.9, 7.4)],
	ClosetProps.GRAFFITI_CHEAT_CODES: [Vector2(4.6, 2.6), Vector2(3.7, 2.6)],
}

## Prop cut-outs (PlatePropLayer; bead Eurobound-kzh9): prop id -> [file prefix in aa_closet_props.json,
## quad depth z in tiles, default state, closet interaction id, and optionally the wall it is painted on
## as [wall, z from, z to, y from, y to], which lays its quad on that wall]. The four DDR arrows are one
## pad, so they all answer to the DDR toilet. The claw-arm chandelier has no approved line and no
## cut-out here; the Broken Prize Tag hangs on it with no interaction until that pickup is built.
## The closet's five approved pieces (Eurobound-ms3r) come from
## Tools/content_generation/absinthe_arcade/hd2d/closet_wall_props.py, which places them with the same
## walls and spans as below. Their states follow the game state (ClosetProps.art_state).
const PROP_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/closet/props/"
const PROP_JSON := PROP_DIR + "aa_closet_props.json"
const PROPS := {
	"ddr_arrow_left": ["aa_closet_ddr_arrow_left", 0.3, "off", ClosetProps.DDR_TOILET],
	"ddr_arrow_right": ["aa_closet_ddr_arrow_right", 0.3, "off", ClosetProps.DDR_TOILET],
	"ddr_arrow_up": ["aa_closet_ddr_arrow_up", 0.3, "off", ClosetProps.DDR_TOILET],
	"ddr_arrow_down": ["aa_closet_ddr_arrow_down", 0.3, "off", ClosetProps.DDR_TOILET],
	"crt": ["aa_closet_crt", 0.05, "insert_coin", ClosetProps.CRT_MIRROR],
	"sock_chute": ["aa_closet_sock_chute", 0.1, "default", ClosetProps.SOCK_CHUTE],
	"bl_switch": ["aa_closet_bl_switch", 7.9, "off", ClosetProps.BLACKLIGHT_SWITCH, ["left", 7.47, 7.82, 4.3, 4.85]],
	"bl_tube": ["aa_closet_bl_tube", 0.05, "off", ClosetProps.BLACKLIGHT_SWITCH],
	"wiring": ["aa_closet_wiring", 13.1, "idle", ClosetProps.SPARKING_WIRING, ["right", 7.0, 13.0, 2.4, 4.0]],
	"haiku": ["aa_closet_haiku", 12.6, "off", ClosetProps.GRAFFITI_HAIKU, ["left", 9.9, 12.5, 3.35, 4.75]],
	"joystick": ["aa_closet_joystick", 9.5, "faint", ClosetProps.GRAFFITI_JOYSTICK, ["left", 8.6, 9.4, 1.42, 2.28]],
	"prize_tag": ["aa_closet_prize_tag", 1.0, "hanging", ""],
}
## Which ClosetProps.art_state each piece follows.
const ART_OF := {"bl_switch": "switch", "bl_tube": "tube", "haiku": "haiku", "joystick": "joystick",
	"prize_tag": "prize_tag"}
## Slack around a wall decal's span (tiles), so the quad covers the sprite's whole box on that wall.
const WALL_QUAD_PAD := 0.6
## How far a wall decal's quad stands off its wall, toward the room (tiles).
const WALL_QUAD_INSET := 0.03

## Runtime only.
var props: PlatePropLayer
var dialogue: DialogueBox
var _player: PlayerController
var _talking := false
## The leader's zap bark over his head (bcnr-q9); runtime only.
var zap_bark: Label3D
var _zap_show := 0.0
var _zap_rng := RandomNumberGenerator.new()
var _visits := {}
var _shame := ClosetProps.new()
var _spark_rng := RandomNumberGenerator.new()
var _markers := {}
var _art_check := 0.0


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/closet/aa_int_closet_"
	focal_px = 2108.0
	pitch_deg = 19.52
	cam_height = 8.43
	cam_z = 24.83
	world_scale = 0.28
	default_spawn = "from_north_wing"


static func _x_at(line: Array, z: float) -> float:
	var a: Vector2 = line[0]
	var b: Vector2 = line[1]
	return a.x + (b.x - a.x) * (z - a.y) / (b.y - a.y)


func _build_room() -> void:
	var mat := _paint_material()
	var far := cam_z
	var lb := Vector2(_x_at(LEFT_WALL, BACK_Z), BACK_Z)
	var rb := Vector2(_x_at(RIGHT_WALL, BACK_Z), BACK_Z)
	var lf := Vector2(_x_at(LEFT_WALL, far), far)
	var rf := Vector2(_x_at(RIGHT_WALL, far), far)
	_wall("back_wall", Vector2(lb.x - 4.0, BACK_Z), Vector2(rb.x + 4.0, BACK_Z), WALL_HEIGHT, mat)
	_wall("left_wall", lf, lb, WALL_HEIGHT, mat)
	_wall("right_wall", rb, rf, WALL_HEIGHT, mat)
	_floor("floor", Vector2(0, far * 0.5), Vector2(30.0, far + 1.0), mat)

	var body := _collision_body("room_collision")
	_box(body, Vector3(0, -0.1, far * 0.5), Vector3(30.0, 0.2, far + 1.0))
	var lw := Vector2(_x_at(LEFT_WALL, WALK_LIMIT_Z), WALK_LIMIT_Z)
	var rw := Vector2(_x_at(RIGHT_WALL, WALK_LIMIT_Z), WALK_LIMIT_Z)
	for seg: Array in [[lb, rb], [lw, lb], [rb, rw], [lw, rw]]:
		_wall_collider(body, seg[0], seg[1])
	for fp: Array in FLOOR_BLOCKERS:
		_footprint(body, fp)


func _build_props() -> void:
	props = PlatePropLayer.new()
	props.name = "props"
	_diorama.add_child(props)
	props.configure(_camera, focal_px, PAINT_IMAGE_PX)
	for id: String in PROPS.keys():
		var spec: Array = PROPS[id]
		if props.add_prop(id, PROP_JSON, String(spec[0]), float(spec[1]), String(spec[2])):
			props.node_of(id).set_meta("interact_id", String(spec[3]))
			if spec.size() > 4:
				props.set_wall_quad(id, wall_quad(spec[4]))
	props.set_night(true)


## The four corners (TL, TR, BR, BL) of a wall decal's quad: its span on the wall plus slack, stood a
## hair off the wall into the room.
static func wall_quad(span: Array) -> Array:
	var line: Array = LEFT_WALL if String(span[0]) == "left" else RIGHT_WALL
	var z0 := float(span[1]) - WALL_QUAD_PAD
	var z1 := float(span[2]) + WALL_QUAD_PAD
	var y0 := float(span[3]) - WALL_QUAD_PAD
	var y1 := float(span[4]) + WALL_QUAD_PAD
	var into := WALL_QUAD_INSET if String(span[0]) == "left" else -WALL_QUAD_INSET
	var a := Vector3(_x_at(line, z0) + into, 0, z0)
	var b := Vector3(_x_at(line, z1) + into, 0, z1)
	return [Vector3(a.x, y1, a.z), Vector3(b.x, y1, b.z), Vector3(b.x, y0, b.z), Vector3(a.x, y0, a.z)]


## Puts every art piece in the state the game is in, swaps the plate for the blacklight, and lets only
## the graffiti that shows be used (a hidden haiku or joystick does not block what is behind it).
func refresh_art() -> void:
	if props == null:
		return
	for id: String in ART_OF.keys():
		props.set_state(id, ClosetProps.art_state(GameState, String(ART_OF[id])))
	_apply_blacklight()
	for id: String in [ClosetProps.GRAFFITI_HAIKU, ClosetProps.GRAFFITI_JOYSTICK]:
		var m: Node3D = _markers.get(id)
		if m == null:
			continue
		var show := ClosetProps.available(GameState, id)
		if show and not m.is_in_group("interact_points"):
			m.add_to_group("interact_points")
		elif not show and m.is_in_group("interact_points"):
			m.remove_from_group("interact_points")


func _apply_time_of_day() -> void:
	super()
	_apply_blacklight()


## The blacklight swaps the night plate for its UV-washed twin (aa_int_closet_night_uv.png).
func _apply_blacklight() -> void:
	if not night or _materials.is_empty():
		return
	var plate := plate_prefix + ("night_uv.png" if ClosetProps.blacklight_on(GameState) else "night.png")
	for mat in _materials:
		mat.set_shader_parameter("albedo_tex", load(plate))


func _build_markers() -> void:
	_build_props()
	var z := (DOOR_Z.x + DOOR_Z.y) * 0.5
	var x := _x_at(LEFT_WALL, z)
	_exit("exit_door_to_north_wing", NORTH_WING_TARGET, "from_maintenance_closet",
		Vector3(x - 0.2, 1.0, z), Vector3(0.6, 2.0, DOOR_Z.y - DOOR_Z.x))
	_spawns(SPAWNS)
	for id: String in INTERACT_POINTS.keys():
		var at: Vector2 = INTERACT_POINTS[id][0]
		var stand: Vector2 = INTERACT_POINTS[id][1]
		var m := Marker3D.new()
		m.name = id
		m.position = Vector3(at.x, 0, at.y)
		m.add_to_group("interact_points")
		m.set_meta("interact_id", id)
		_diorama.add_child(m)
		_markers[id] = m
		var toward := (at - stand).normalized()
		SceneRouter.add_spawn_point(_diorama, "at_" + id, Vector3(stand.x, 0, stand.y),
			_facing(Vector3(toward.x, 0, toward.y)))


static func _facing(dir: Vector3) -> String:
	var best := "south"
	var best_dot := -2.0
	for d: String in PartySprite3D.DIRECTIONS:
		var dot := PlayerController.facing_vector(d).dot(dir.normalized())
		if dot > best_dot:
			best_dot = dot
			best = d
	return best


func _ready() -> void:
	super()
	if not Engine.is_editor_hint():
		_spark_rng.randomize()
		refresh_art()
	if Engine.is_editor_hint() or not spawn_player:
		return
	dialogue = DialogueBox.new()
	dialogue.field_state = GameState
	dialogue.name = "dialogue"
	add_child(dialogue)
	var players := get_tree().get_nodes_in_group("player").filter(func(n): return is_ancestor_of(n))
	if not players.is_empty():
		_player = players.front()
		_player.interacted.connect(_on_interacted)
		_zap_rng.randomize()
		zap_bark = Label3D.new()
		zap_bark.name = "zap_bark"
		zap_bark.billboard = BaseMaterial3D.BILLBOARD_ENABLED
		zap_bark.no_depth_test = true
		zap_bark.font_size = 36
		zap_bark.outline_size = 10
		zap_bark.pixel_size = 0.004
		zap_bark.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		zap_bark.width = 520.0
		zap_bark.modulate = Color(0.95, 0.95, 0.85)
		zap_bark.position.y = 2.15
		zap_bark.visible = false
		_player.add_child(zap_bark)


## The 30-second shame timer: lingering in the closet earns the announcer's next line.
func _process(delta: float) -> void:
	if Engine.is_editor_hint():
		return
	_tick_spark(delta)
	_art_check -= delta
	if _art_check <= 0.0:
		_art_check = 0.5
		refresh_art()
	if dialogue == null or _talking:
		return
	_tick_zap(delta)
	var line := _shame.tick_shame(delta)
	if line != "":
		_show([{"who": ClosetProps.NO_SPEAKER, "line": line}])


## The wiring spits a spark every 2-5 s, and at once when the leader walks into zap range.
func _tick_spark(delta: float) -> void:
	if props == null or not props.has_prop("wiring"):
		return
	var near := false
	if _player != null:
		var at: Vector2 = INTERACT_POINTS[ClosetProps.SPARKING_WIRING][0]
		var here := _diorama.to_local(_player.global_position)
		near = Vector2(here.x - at.x, here.z - at.y).length() <= ClosetProps.ZAP_RANGE_TILES
	var state := "spark" if _shame.tick_spark(delta, near, _spark_rng) else "idle"
	if props.state_of("wiring") != state:
		props.set_state("wiring", state)


## The sparking wiring zaps whoever is leading when he walks too close: one floating line, no box.
func _tick_zap(delta: float) -> void:
	if zap_bark == null or _player == null:
		return
	if _zap_show > 0.0:
		_zap_show -= delta
		if _zap_show <= 0.0:
			zap_bark.visible = false
	var at: Vector2 = INTERACT_POINTS[ClosetProps.SPARKING_WIRING][0]
	var here := _diorama.to_local(_player.global_position)
	var dist := Vector2(here.x - at.x, here.z - at.y).length()
	var line := _shame.tick_zap(delta, _player.bro, dist, _zap_rng)
	if line != "":
		zap_bark.text = line
		zap_bark.visible = true
		_zap_show = ClosetProps.ZAP_SHOW_S


func _on_interacted(id: String) -> void:
	if _talking:
		return
	if id == ClosetProps.BLACKLIGHT_SWITCH:
		ClosetProps.toggle_blacklight(GameState)
		refresh_art()
		return
	if not ClosetProps.IDS.has(id):
		return
	var visit := int(_visits.get(id, 0))
	var lines := ClosetProps.lines_for(GameState, id, visit)
	if lines.is_empty():
		return
	_visits[id] = visit + 1
	_player.input_locked = true
	await _show(lines)
	_player.input_locked = false


func _show(lines: Array) -> void:
	_talking = true
	for row: Dictionary in lines:
		await dialogue.say(String(row["who"]), String(row["line"]))
	dialogue.close()
	_talking = false
