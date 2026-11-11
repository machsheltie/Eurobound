@tool
extends Node3D
## HD-2D Absinthe Arcade main hall, built by projecting the approved hall painting (v8) from the
## camera it was painted from onto a graybox of the room. PROTOTYPE for the author's build-method
## ruling (decisions page, int_build_method, option A). Tick "Night" in the Inspector or press N.
##
## How it works:
## - The paint camera was measured from v8's checkerboard floor (tile width grows linearly toward
##   the bottom of the image, which fixes the horizon and focal length) and from the painted
##   furniture for scale. See PAINT_* below.
## - The room (floor, back wall, splayed side walls) and simple prisms for the bar, doors and claw
##   alcove are built in "painting units" inside `diorama`, scaled by WORLD_SCALE so the world is in
##   real metres (characters 1.8 m), as on the exterior.
## - Every surface uses hd2d_projected_paint.gdshader, so from the gameplay camera (which IS the
##   paint camera) the room shows v8 unchanged. The depth-layer cutouts
##   (assets/.../interior/depth_layers, cut by tools/content_generation/absinthe_arcade/hd2d/
##   cut_interior_layers.py) sit on the prisms, so the bros pass behind the bar and doors.
## - The camera is fixed for the whole room (the painting fits one screen), Bravely Default style.

const HALL_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/hall/"
const LAYER_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/depth_layers/"
const PAINT_SHADER := preload("res://worlds/debaucheryville/hd2d_projected_paint.gdshader")

## Paint camera, measured from aa_interior_hall_v8 (2752x1536): focal length in pixels, downward
## pitch, and height above the floor in painting units. Painting units are metres at the scale of
## the painted patrons; the painted furniture is larger than that (the bar counter measures ~1.7 m,
## the foosball table ~1.3 m), so WORLD_SCALE shrinks the room until the furniture is real-sized.
const PAINT_IMAGE_PX := Vector2(2752, 1536)
const PAINT_FOCAL_PX := 4150.0
const PAINT_PITCH_DEG := 29.0
const PAINT_CAM_HEIGHT := 14.1
## Distance (painting units) from the camera to the hall's centre line; puts the origin mid-floor.
const PAINT_CAM_Z := 22.4
const WORLD_SCALE := 0.75

## Room outline on the floor, painting units, origin mid-floor, -Z toward the back wall. The
## painting's side walls splay outward toward the camera, so the graybox follows them.
const BACK_WALL_Z := -5.32
const LEFT_WALL := [Vector2(-4.69, -2.72), Vector2(-6.9, 1.16)]   # (x, z) two points on its base
const RIGHT_WALL := [Vector2(5.55, -1.76), Vector2(6.58, 1.7)]
const FRONT_Z := 6.5
const WALL_HEIGHT := 30.0

## North archway (v8b, pixels 1330-1485 x 340-590): the exit to the mirror-corridor screen. The back
## wall gets an opening here, with a short corridor box behind it that wears the painted corridor.
const NORTH_ARCH := {"x0": -0.35, "x1": 0.83, "height": 2.3, "depth": 4.5}
## Stepping onto the arch threshold hands over to the mirror-corridor screen. It fires at the
## threshold on purpose: the painted arch is ~1.7 m tall at the ruled scale, shorter than the bros,
## so they must never be seen walking under the lintel.
const NORTH_EXIT_Z := -5.32
const NORTH_EXIT_TARGET := "absinthe_arcade_mirror_corridor"
## Front of the hall: the painting's bottom edge shows the floor to z ~5.3, so the room's front
## edge is a wall there, with the gap between the stained-glass door leaves (x -0.8..0.8) leading
## out to the street.
const FRONT_EDGE_Z := 5.4
const FRONT_DOOR_X := 0.8
const FRONT_EXIT_TARGET := "absinthe_arcade_exterior"
const RESTROOM_TARGET := "absinthe_arcade_restroom"
## Spawn points [painting units (x, z), facing]: through the front doors from the street, and back
## out of the north arch from the mirror corridor.
const SPAWNS := {
	"from_street": [Vector2(0.0, 3.4), "north"],
	"from_mirror_corridor": [Vector2(0.24, -4.3), "south"],
	# Back from the restroom: on the door spot just south of TOKENS HERE (round v29).
	"from_restroom": [Vector2(-6.6, 4.4), "south"],
}

## Depth curve (author ruling int_depth_scale): v8 paints its back row smaller than its floor
## perspective explains, so sprites shrink toward the back wall. Full size at and in front of
## DEPTH_FULL_Z, DEPTH_BACK_SCALE at the back wall, linear in between (painting units).
## Every node in the "hall_actors" group (bros, NPCs) is scaled each frame.
const DEPTH_FULL_Z := 2.0
const DEPTH_BACK_SCALE := 0.68
const ACTOR_GROUP := "hall_actors"

## Interaction anchors, painting units on the floor, from paint_px_to_floor.py on v8b's pixel boxes.
## They mark WHERE things are; the interaction system that uses them doesn't exist yet.
## id: [position (x, z), facing yaw in degrees (0 = the anchor faces +Z, toward the camera)]
const INTERACT_POINTS := {
	"cabinet_frogger": [Vector2(-0.95, -5.0), 0.0],        # back row #2, px 1202-1288
	"cabinet_street_fighter": [Vector2(1.13, -5.0), 0.0],  # back row #4, px 1489-1578
	# right wall #6, px 2195-2300, faces west. The bar and its stools close the aisle in front of it,
	# so the bros stand at its south-east corner (third value: where the bro stands).
	"cabinet_kebab_kombat": [Vector2(5.14, 0.42), -90.0, Vector2(4.75, 1.45)],
	"ddr_dance_off": [Vector2(-4.86, -0.12), 90.0],        # middle of the three west-wall pads
	"token_machine": [Vector2(-6.0, 3.0), 90.0],          # TOKENS HERE, its face clear of the DDR pads
	# The skee-ball lanes' throwing end faces east, beside the Frogger stools: the bros stand a little
	# south-east of it so the Frogger cabinet stays out of their way.
	"skee_ball": [Vector2(-1.65, -4.3), 90.0, Vector2(-1.25, -4.2)],
	"foosball": [Vector2(-3.4, -1.55), 0.0],               # the bros' side of the table, south
	# West wall behind the first DDR pad (px ~585-760 x 200-540). The pad and the foosball table box
	# in its front, so the anchor is its control panel (south-east corner) and the bros stand in the
	# gap between the pad and the table, facing north-west.
	"beanie_baby_claw": [Vector2(-4.5, -2.0), 135.0, Vector2(-3.9, -1.1)],
	# Under the PRIZES arch, front right (px ~2440-2660 x 1200-1330), facing west.
	"rigged_absinthe_claw_machine": [Vector2(6.3, 2.8), -90.0],
	# The restroom (round v28 door = the left-wall arch, hidden behind TOKENS HERE; round v29
	# ef6_restroom_access = press_door): the bros stand just south of the machine and press facing
	# the wall. The anchor is the floor between the machine's south end and the wall.
	"restroom_door": [Vector2(-7.5, 3.9), 90.0, Vector2(-6.6, 4.4)],
}
## Machines that open a mini-game screen when paid for (round v25 rec_games).
const REC_GAMES := ["skee_ball", "foosball"]
## A bro using a machine stands this far in front of it (painting units). The "at_<id>" spawn
## points sit there: an arcade fight lost puts the bros back in front of that cabinet (author
## ruling ef_arcade_loss = at_cabinet, 2026-11-10).
const STAND_OFF := 1.0

## Painted furniture the bros walk around but never behind: invisible blockers on the floor,
## [centre (x, z), size (x, z)] in painting units, measured from v8f with paint_px_to_floor.py.
## (Furniture they can pass behind is an occluder prism below instead.)
const FLOOR_BLOCKERS := [
	[Vector2(-6.6, 2.05), Vector2(1.2, 3.5)],     # TOKENS HERE machine
	[Vector2(-5.28, 0.1), Vector2(2.05, 4.1)],    # the three DDR pads
	[Vector2(-4.9, -3.85), Vector2(1.2, 2.3)],    # plush claw machine
	[Vector2(-3.4, -2.5), Vector2(2.0, 1.95)],    # foosball table
	[Vector2(-2.8, -4.45), Vector2(2.4, 1.7)],    # skee-ball lanes
	[Vector2(-0.82, -5.1), Vector2(0.75, 0.5)],   # stools in front of the Frogger row
	[Vector2(1.15, -5.1), Vector2(0.5, 0.5)],     # stool in front of the Street Fighter row
	[Vector2(-1.33, -1.13), Vector2(0.6, 0.6)],   # chair behind the bar's west end
	[Vector2(-1.26, 0.56), Vector2(0.6, 0.6)],    # bar stools, west side
	[Vector2(-0.25, 1.51), Vector2(0.6, 0.6)],
	[Vector2(0.73, 2.4), Vector2(0.6, 0.6)],      # chair at the bar's front
	[Vector2(2.1, 2.9), Vector2(0.6, 0.6)],       # stool at the bar's front
	[Vector2(3.2, 2.1), Vector2(0.7, 1.4)],       # the toilet
	[Vector2(5.1, 0.2), Vector2(0.6, 1.4)],       # stools at Kebab Kombat and Bubble Bobble
]

## Occluder prisms (footprint in painting units, height) carrying the depth-layer cutouts.
const OCCLUDERS := {
	"aa_int_layer_bottle_bar": {"height": 14.0, "footprint": [
		Vector2(-0.7, 0.93), Vector2(0.26, 1.7), Vector2(1.32, 2.3), Vector2(2.97, 2.35),
		Vector2(4.87, 0.93), Vector2(4.6, -1.2), Vector2(2.5, -2.2), Vector2(0.3, -2.2), Vector2(-0.5, -0.8)]},
	"aa_int_layer_entry_doors": {"height": 6.0, "footprint": [
		Vector2(-1.7, 3.6), Vector2(-0.8, 3.6), Vector2(-0.8, 6.4), Vector2(-1.7, 6.4)],
		"also": [Vector2(0.8, 3.6), Vector2(1.75, 3.6), Vector2(1.75, 6.4), Vector2(0.8, 6.4)]},
	"aa_int_layer_claw_alcove": {"height": 9.0, "footprint": [
		Vector2(6.0, 1.9), Vector2(6.8, 2.2), Vector2(7.4, 4.4), Vector2(6.5, 4.2)]},
}

## The token picker and the INSUFFICIENT CREDITS flash (runtime only).
var overlay: ArcadeOverlay
## The skee-ball or foosball screen while one is open.
var rec_screen: CanvasLayer
var battle_core: BattleCore
var battle_screen: BattleScreen
var claw_screen: ClawScreen
## The rigged claw's PAYOUT light in the hall, blinking while the next play would pay.
var payout_light: OmniLight3D
var _blink_t := 0.0
var _player: PlayerController

## Runtime only: put the player on a spawn point (off for QA captures that place their own bros).
@export var spawn_player := true

@export var night: bool = true:
	set(value):
		night = value
		if is_inside_tree() and _env != null:
			_apply_time_of_day()

var _diorama: Node3D
var _camera: Camera3D
var _env: WorldEnvironment
var _materials: Array[ShaderMaterial] = []
var _layers: Dictionary = {}
var _night_lights: Array[Light3D] = []
var _fill: DirectionalLight3D


func _ready() -> void:
	for child in get_children():
		if child.owner == null:
			child.free()
	_materials.clear()
	_night_lights.clear()
	_diorama = Node3D.new()
	_diorama.name = "diorama"
	_diorama.scale = Vector3.ONE * WORLD_SCALE
	add_child(_diorama)
	_layers = JSON.parse_string(FileAccess.get_file_as_string(LAYER_DIR + "layers.json"))["layers"]
	_build_camera()
	_build_room()
	_build_occluders()
	_build_markers()
	_build_lighting()
	_apply_time_of_day()
	if not Engine.is_editor_hint() and spawn_player:
		SceneRouter.ensure_game_started(get_tree())
		overlay = ArcadeOverlay.new()
		overlay.name = "overlay"
		add_child(overlay)
		overlay.tokens_chosen.connect(_on_tokens_chosen)
		overlay.picker_closed.connect(_release_player)
		overlay.flash_finished.connect(_release_player)
		payout_light = OmniLight3D.new()
		payout_light.name = "payout_light"
		payout_light.light_color = Color(1.0, 0.8, 0.25)
		payout_light.light_energy = 3.0
		payout_light.omni_range = 2.5
		payout_light.position = Vector3(6.6, 3.2, 2.8)
		payout_light.visible = false
		_diorama.add_child(payout_light)
		_player = SceneRouter.spawn_player(self, "from_street")
		_player.interacted.connect(_on_interacted)
		SceneRouter.wire_exits(self)


## The leader pressed the button facing a machine.
func _on_interacted(id: String) -> void:
	if id == "restroom_door":
		_player.input_locked = true
		SceneRouter.travel(get_tree(), RESTROOM_TARGET, "from_hall")
		return
	if id == "token_machine":
		var most := ArcadeRules.max_buyable(GameState)
		if most <= 0:
			_insufficient_credits()
			return
		_player.input_locked = true
		overlay.open_picker(most)
	elif ArcadeRules.PLAY_COST.has(id):
		if not ArcadeRules.can_play(GameState, id):
			_insufficient_credits()
			return
		if REC_GAMES.has(id):
			_play_rec_game(id)
			return
		if ArcadeClaw.is_claw(id):
			_play_claw(id)
			return
		if ArcadeBattle.is_battle_cabinet(id):
			_play_cabinet(id)
			return
		# DDR waits on the songs (deferred by the author): nothing is spent until it is wired.
		push_warning("Absinthe Arcade: %s has no game screen yet" % id)


## Pays for a cabinet fight and opens the battle screen with that cabinet's art behind it.
func _play_cabinet(id: String) -> void:
	ArcadeRules.pay_for_play(GameState, id)
	_player.input_locked = true
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	battle_core = ArcadeBattle.build(id, GameState, rng)
	battle_screen = BattleScreen.new()
	battle_screen.name = "battle_screen"
	battle_screen.setup(battle_core, load(ArcadeBattle.backdrop_path(id)), ArcadeBattle.skills())
	add_child(battle_screen)
	battle_screen.finished.connect(_on_battle_finished.bind(id))


## Pays for a claw play and opens the claw screen. The rigged claw's PAYOUT light is read before
## the bros pay (round v28 ef5_payout_light_timing).
func _play_claw(id: String) -> void:
	var blinking := id == ArcadeClaw.RIGGED and ArcadeClaw.payout_blinking(GameState)
	ArcadeRules.pay_for_play(GameState, id)
	_player.input_locked = true
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	claw_screen = ClawScreen.new()
	claw_screen.name = "claw_screen"
	claw_screen.setup(id, GameState, rng, blinking)
	add_child(claw_screen)
	claw_screen.finished.connect(_on_claw_finished)


func _on_claw_finished(_result: Dictionary) -> void:
	claw_screen = null
	_release_player()


## Win: tickets (and any drops). Loss: everyone at 1 HP, still in front of the cabinet (ruling
## ef_arcade_loss). Run: tokens stay spent, HP kept (ef3_run).
func _on_battle_finished(outcome: String, id: String) -> void:
	var result := ArcadeBattle.settle(id, battle_core, GameState)
	battle_core = null
	battle_screen = null
	match outcome:
		"won":
			var text := "%d TICKETS" % int(result["tickets"])
			if int(result["refund"]) > 0:
				text += "
SOGGY PILE: %s" % ("1 SOV" if int(result["refund"]) == 1 else "%d SOVS" % int(result["refund"]))
			overlay.flash(text)
		"lost":
			overlay.flash("GAME OVER")
		_:
			_release_player()


## Pays for a skee-ball or foosball game and opens its screen; the tickets come in at the end.
func _play_rec_game(id: String) -> void:
	ArcadeRules.pay_for_play(GameState, id)
	_player.input_locked = true
	rec_screen = SkeeBallScreen.new() if id == "skee_ball" else FoosballScreen.new()
	rec_screen.name = id + "_screen"
	add_child(rec_screen)
	rec_screen.finished.connect(_on_rec_game_finished)


func _on_rec_game_finished(tickets: int) -> void:
	rec_screen = null
	ArcadeRules.add_tickets(GameState, tickets)
	overlay.flash("%d TICKETS" % tickets)


func _insufficient_credits() -> void:
	_player.input_locked = true
	overlay.flash("INSUFFICIENT CREDITS")


func _on_tokens_chosen(count: int) -> void:
	ArcadeRules.buy_tokens(GameState, count)
	_release_player()


func _release_player() -> void:
	if _player != null:
		_player.input_locked = false


func _process(delta: float) -> void:
	if Engine.is_editor_hint():
		return
	_blink_t += delta
	if payout_light != null:
		payout_light.visible = ArcadeClaw.payout_blinking(GameState) and fmod(_blink_t * 2.0, 1.0) < 0.5
	for node in get_tree().get_nodes_in_group(ACTOR_GROUP):
		var actor := node as Node3D
		if actor != null and is_ancestor_of(actor):
			var z_paint := to_local(actor.global_position).z / WORLD_SCALE
			actor.scale = Vector3.ONE * depth_scale_at(z_paint)


## Sprite scale for an actor standing at depth `z_paint` (painting units, -Z toward the back wall).
static func depth_scale_at(z_paint: float) -> float:
	var t := clampf((DEPTH_FULL_Z - z_paint) / (DEPTH_FULL_Z - BACK_WALL_Z), 0.0, 1.0)
	return lerpf(1.0, DEPTH_BACK_SCALE, t)


func _unhandled_input(event: InputEvent) -> void:
	if Engine.is_editor_hint():
		return
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_N:
		night = not night


## The gameplay camera is the paint camera, in real metres.
func _build_camera() -> void:
	_camera = Camera3D.new()
	_camera.name = "hd2d_camera"
	_camera.keep_aspect = Camera3D.KEEP_HEIGHT
	_camera.fov = rad_to_deg(2.0 * atan(PAINT_IMAGE_PX.y * 0.5 / PAINT_FOCAL_PX))
	_camera.position = Vector3(0, PAINT_CAM_HEIGHT, PAINT_CAM_Z) * WORLD_SCALE
	_camera.rotation_degrees = Vector3(-PAINT_PITCH_DEG, 0, 0)
	_camera.near = 0.5
	_camera.far = 80.0
	add_child(_camera)
	_camera.make_current()


func _paint_material(layer_id := "") -> ShaderMaterial:
	var mat := ShaderMaterial.new()
	mat.shader = PAINT_SHADER
	mat.set_shader_parameter("paint_view", Projection(_camera.global_transform.affine_inverse()))
	mat.set_shader_parameter("focal_px", PAINT_FOCAL_PX)
	mat.set_shader_parameter("image_px", PAINT_IMAGE_PX)
	if layer_id != "":
		var r: Array = _layers[layer_id]["rect_px"]
		mat.set_shader_parameter("rect_px", Vector4(r[0], r[1], r[2], r[3]))
		mat.set_shader_parameter("use_alpha", true)
	mat.set_meta("layer_id", layer_id)
	_materials.append(mat)
	return mat


## A vertical quad on the floor line a -> b (painting units), `height` tall.
func _wall(name_: String, a: Vector2, b: Vector2, height: float, mat: Material) -> MeshInstance3D:
	var st := SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)
	var p := [Vector3(a.x, 0, a.y), Vector3(b.x, 0, b.y), Vector3(b.x, height, b.y), Vector3(a.x, height, a.y)]
	for i in [0, 1, 2, 0, 2, 3]:
		st.add_vertex(p[i])
	st.generate_normals()
	var mi := MeshInstance3D.new()
	mi.name = name_
	mi.mesh = st.commit()
	mi.material_override = mat
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	_diorama.add_child(mi)
	return mi


## Where the line through two floor points crosses z = `z`.
func _x_at(line: Array, z: float) -> float:
	var a: Vector2 = line[0]
	var b: Vector2 = line[1]
	return a.x + (b.x - a.x) * (z - a.y) / (b.y - a.y)


func _build_room() -> void:
	var mat := _paint_material()
	var lb := Vector2(_x_at(LEFT_WALL, BACK_WALL_Z), BACK_WALL_Z)
	var rb := Vector2(_x_at(RIGHT_WALL, BACK_WALL_Z), BACK_WALL_Z)
	var lf := Vector2(_x_at(LEFT_WALL, FRONT_Z), FRONT_Z)
	var rf := Vector2(_x_at(RIGHT_WALL, FRONT_Z), FRONT_Z)
	# Back wall with the north archway cut out of it, and the corridor box behind the opening.
	var ax0 := Vector2(NORTH_ARCH["x0"], BACK_WALL_Z)
	var ax1 := Vector2(NORTH_ARCH["x1"], BACK_WALL_Z)
	var arch_h: float = NORTH_ARCH["height"]
	var deep: float = BACK_WALL_Z - float(NORTH_ARCH["depth"])
	_wall("back_wall_left", lb, ax0, WALL_HEIGHT, mat)
	_wall("back_wall_right", ax1, rb, WALL_HEIGHT, mat)
	var lintel := _wall("back_wall_lintel", ax0, ax1, WALL_HEIGHT - arch_h, mat)
	lintel.position.y = arch_h
	_wall("arch_corridor_left", ax0, Vector2(ax0.x, deep), arch_h, mat)
	_wall("arch_corridor_right", Vector2(ax1.x, deep), ax1, arch_h, mat)
	_wall("arch_corridor_end", Vector2(ax0.x, deep), Vector2(ax1.x, deep), arch_h, mat)
	var cfloor := PlaneMesh.new()
	cfloor.size = Vector2(ax1.x - ax0.x, BACK_WALL_Z - deep)
	var cfloor_mi := MeshInstance3D.new()
	cfloor_mi.name = "arch_corridor_floor"
	cfloor_mi.mesh = cfloor
	cfloor_mi.position = Vector3((ax0.x + ax1.x) * 0.5, 0, (BACK_WALL_Z + deep) * 0.5)
	cfloor_mi.material_override = mat
	_diorama.add_child(cfloor_mi)
	_wall("left_wall", lf, lb, WALL_HEIGHT, mat)
	_wall("right_wall", rb, rf, WALL_HEIGHT, mat)
	var floor_mesh := PlaneMesh.new()
	floor_mesh.size = Vector2(24, FRONT_Z - BACK_WALL_Z + 2.0)
	var floor_mi := MeshInstance3D.new()
	floor_mi.name = "floor"
	floor_mi.mesh = floor_mesh
	floor_mi.position = Vector3(0, 0, (FRONT_Z + BACK_WALL_Z) * 0.5)
	floor_mi.material_override = mat
	_diorama.add_child(floor_mi)

	# Collision in real metres: floor and the three walls.
	var body := StaticBody3D.new()
	body.name = "room_collision"
	_diorama.add_child(body)
	var fs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(24, 0.2, FRONT_Z - BACK_WALL_Z + 2.0)
	fs.shape = box
	fs.position = Vector3(0, -0.1, (FRONT_Z + BACK_WALL_Z) * 0.5)
	body.add_child(fs)
	var cfs := CollisionShape3D.new()
	var cbox := BoxShape3D.new()
	cbox.size = Vector3(ax1.x - ax0.x + 0.6, 0.2, BACK_WALL_Z - deep)
	cfs.shape = cbox
	cfs.position = Vector3((ax0.x + ax1.x) * 0.5, -0.1, (BACK_WALL_Z + deep) * 0.5)
	body.add_child(cfs)
	for seg: Array in [[lb, ax0], [ax1, rb], [lf, lb], [rb, rf],
			[ax0, Vector2(ax0.x, deep)], [Vector2(ax1.x, deep), ax1], [Vector2(ax0.x, deep), Vector2(ax1.x, deep)]]:
		_wall_collider(body, seg[0], seg[1])
	for spec: Array in FLOOR_BLOCKERS:
		var c: Vector2 = spec[0]
		var sz: Vector2 = spec[1]
		var bcs := CollisionShape3D.new()
		var bbox := BoxShape3D.new()
		bbox.size = Vector3(sz.x, 2.0, sz.y)
		bcs.shape = bbox
		bcs.position = Vector3(c.x, 1.0, c.y)
		body.add_child(bcs)
	# Front edge, open between the door leaves; the leaves' own prisms close the sides of the gap.
	var fl := Vector2(_x_at(LEFT_WALL, FRONT_EDGE_Z), FRONT_EDGE_Z + 0.15)
	var fr := Vector2(_x_at(RIGHT_WALL, FRONT_EDGE_Z), FRONT_EDGE_Z + 0.15)
	_wall_collider(body, fl, Vector2(-FRONT_DOOR_X, FRONT_EDGE_Z + 0.15))
	_wall_collider(body, Vector2(FRONT_DOOR_X, FRONT_EDGE_Z + 0.15), fr)
	# Behind the front exit, so a player walking through it never falls off the floor.
	_wall_collider(body, Vector2(-FRONT_DOOR_X, FRONT_EDGE_Z + 0.6), Vector2(FRONT_DOOR_X, FRONT_EDGE_Z + 0.6))


## The exit trigger in the archway and the interaction anchors. Both are plain markers that carry
## their ids as metadata, ready for the scene-transition and interaction systems to pick up.
func _build_markers() -> void:
	var exit := Area3D.new()
	exit.name = "exit_north_arch"
	exit.add_to_group("scene_exits")
	exit.set_meta("target_scene", NORTH_EXIT_TARGET)
	exit.set_meta("target_spawn", "from_hall")
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(float(NORTH_ARCH["x1"]) - float(NORTH_ARCH["x0"]), 2.0, 0.6)
	cs.shape = box
	cs.position = Vector3((float(NORTH_ARCH["x0"]) + float(NORTH_ARCH["x1"])) * 0.5, 1.0, NORTH_EXIT_Z - 0.3)
	exit.add_child(cs)
	_diorama.add_child(exit)
	if SceneRouter.scene_path(NORTH_EXIT_TARGET).is_empty():
		# Until the mirror-corridor screen exists, a stop just behind the trigger keeps the bros
		# out from under the arch's short lintel.
		var stop := StaticBody3D.new()
		stop.name = "arch_unbuilt_stop"
		_diorama.add_child(stop)
		var z := NORTH_EXIT_Z - 0.75
		_wall_collider(stop, Vector2(float(NORTH_ARCH["x0"]), z), Vector2(float(NORTH_ARCH["x1"]), z))
	var front := Area3D.new()
	front.name = "exit_front_doors"
	front.add_to_group("scene_exits")
	front.set_meta("target_scene", FRONT_EXIT_TARGET)
	front.set_meta("target_spawn", "from_arcade")
	var fcs := CollisionShape3D.new()
	var fbox := BoxShape3D.new()
	fbox.size = Vector3(FRONT_DOOR_X * 2.0, 2.0, 0.8)
	fcs.shape = fbox
	fcs.position = Vector3(0, 1.0, FRONT_EDGE_Z - 0.4)
	front.add_child(fcs)
	_diorama.add_child(front)
	for sid: String in SPAWNS.keys():
		var sp: Vector2 = SPAWNS[sid][0]
		SceneRouter.add_spawn_point(_diorama, sid, Vector3(sp.x, 0, sp.y), SPAWNS[sid][1])
	for id: String in INTERACT_POINTS.keys():
		var spec: Array = INTERACT_POINTS[id]
		var p: Vector2 = spec[0]
		var out := Vector2(0, 1).rotated(-deg_to_rad(float(spec[1])))  # the way the machine faces
		var stand: Vector2 = spec[2] if spec.size() > 2 else p + out * STAND_OFF
		var toward := (p - stand).normalized()
		SceneRouter.add_spawn_point(_diorama, "at_" + id, Vector3(stand.x, 0, stand.y),
			_facing_name(Vector3(toward.x, 0, toward.y)))
		var m := Marker3D.new()
		m.name = id
		m.position = Vector3(p.x, 0, p.y)
		m.rotation_degrees.y = spec[1]
		m.add_to_group("interact_points")
		m.set_meta("interact_id", id)
		_diorama.add_child(m)


## The 8-way facing name closest to a ground-plane direction (camera looking north).
static func _facing_name(dir: Vector3) -> String:
	var best := "south"
	var best_dot := -2.0
	for d: String in PartySprite3D.DIRECTIONS:
		var dot := PlayerController.facing_vector(d).dot(dir.normalized())
		if dot > best_dot:
			best_dot = dot
			best = d
	return best


func _wall_collider(body: StaticBody3D, a: Vector2, b: Vector2) -> void:
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(a.distance_to(b), 4.0, 0.3)
	cs.shape = box
	var mid := (a + b) * 0.5
	cs.position = Vector3(mid.x, 2.0, mid.y)
	cs.rotation.y = -atan2(b.y - a.y, b.x - a.x)
	body.add_child(cs)


## A closed prism over `footprint`, wearing the layer cutout, plus a matching collider.
func _prism(layer_id: String, footprint: Array, height: float) -> void:
	var st := SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)
	var n := footprint.size()
	for i in n:
		var a: Vector2 = footprint[i]
		var b: Vector2 = footprint[(i + 1) % n]
		var q := [Vector3(a.x, 0, a.y), Vector3(b.x, 0, b.y), Vector3(b.x, height, b.y), Vector3(a.x, height, a.y)]
		for k in [0, 1, 2, 0, 2, 3]:
			st.add_vertex(q[k])
	for i in range(1, n - 1):  # lid (convex footprints)
		for v: Vector2 in [footprint[0], footprint[i], footprint[i + 1]]:
			st.add_vertex(Vector3(v.x, height, v.y))
	st.generate_normals()
	var mi := MeshInstance3D.new()
	mi.name = layer_id
	mi.mesh = st.commit()
	mi.material_override = _paint_material(layer_id)
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	_diorama.add_child(mi)
	var body := StaticBody3D.new()
	body.name = layer_id + "_collision"
	var cs := CollisionShape3D.new()
	var shape := ConvexPolygonShape3D.new()
	var pts := PackedVector3Array()
	for v: Vector2 in footprint:
		pts.append(Vector3(v.x, 0, v.y))
		pts.append(Vector3(v.x, 2.5, v.y))
	shape.points = pts
	cs.shape = shape
	body.add_child(cs)
	_diorama.add_child(body)


func _build_occluders() -> void:
	for layer_id: String in OCCLUDERS.keys():
		var spec: Dictionary = OCCLUDERS[layer_id]
		_prism(layer_id, spec["footprint"], spec["height"])
		if spec.has("also"):
			_prism(layer_id, spec["also"], spec["height"])


## Practical lights, real metres: they light the bros (the painting is unshaded and already lit).
## [position (painting units), colour, energy, range (real m), night only]
const LIGHTS := [
	[Vector3(2.0, 3.0, 0.2), Color(0.55, 1.0, 0.35), 2.2, 5.0, true],    # green bottle bar
	[Vector3(-4.0, 2.5, -1.0), Color(0.75, 0.4, 1.0), 1.4, 3.5, true],   # DDR wall screen
	[Vector3(-5.5, 3.5, 2.0), Color(1.0, 0.72, 0.42), 1.6, 4.0, false],  # token machine lamp
	[Vector3(5.8, 4.0, 2.2), Color(1.0, 0.75, 0.45), 1.4, 4.0, false],   # PRIZES arch sconce
	[Vector3(0.0, 2.5, 5.0), Color(0.9, 0.7, 1.0), 0.9, 4.0, true],      # stained-glass doors
]


func _build_lighting() -> void:
	_env = WorldEnvironment.new()
	var env := Environment.new()
	env.background_mode = Environment.BG_COLOR
	env.background_color = Color.BLACK
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.tonemap_mode = Environment.TONE_MAPPER_LINEAR
	env.glow_enabled = true
	env.glow_blend_mode = Environment.GLOW_BLEND_MODE_ADDITIVE
	env.glow_hdr_threshold = 1.0
	env.set_glow_level(1, 0.0)
	env.set_glow_level(3, 1.0)
	env.set_glow_level(4, 0.8)
	env.set_glow_level(5, 0.4)
	_env.environment = env
	add_child(_env)
	_fill = DirectionalLight3D.new()
	_fill.name = "fill"
	_fill.rotation_degrees = Vector3(-50, 20, 0)
	_fill.shadow_enabled = false
	add_child(_fill)
	for spec: Array in LIGHTS:
		var l := OmniLight3D.new()
		l.position = (spec[0] as Vector3) * WORLD_SCALE
		l.light_color = spec[1]
		l.light_energy = spec[2]
		l.omni_range = spec[3]
		l.omni_attenuation = 1.3
		l.set_meta("night_only", spec[4])
		add_child(l)
		_night_lights.append(l)


func _apply_time_of_day() -> void:
	var tag := "night" if night else "day"
	for mat in _materials:
		var lid: String = mat.get_meta("layer_id")
		var base := HALL_DIR + "aa_int_hall_%s.png" if lid == "" else LAYER_DIR + lid + "_%s.png"
		mat.set_shader_parameter("albedo_tex", load(base % tag))
		var has_emit := lid == "" or bool(_layers[lid]["emit"])
		mat.set_shader_parameter("use_emission", night and has_emit)
		if night and has_emit:
			mat.set_shader_parameter("emit_tex", load(base % "emit"))
	for l in _night_lights:
		l.visible = night or not l.get_meta("night_only")
	var env: Environment = _env.environment
	if night:
		env.ambient_light_color = Color(0.62, 0.55, 0.72)
		env.ambient_light_energy = 0.55
		_fill.light_color = Color(0.85, 0.75, 0.95)
		_fill.light_energy = 0.25
		env.glow_intensity = 0.8
	else:
		env.ambient_light_color = Color(0.95, 0.9, 0.82)
		env.ambient_light_energy = 0.8
		_fill.light_color = Color(1.0, 0.92, 0.8)
		_fill.light_energy = 0.6
		env.glow_intensity = 0.2


## For QA captures: the fixed gameplay camera.
func get_camera() -> Camera3D:
	return _camera
