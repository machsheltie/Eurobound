@tool
extends HD2DProjectedRoom
## HD-2D Absinthe Arcade public restroom (approved round v26: its own screen, the bronze Green Fairy
## toilet-paper holder; door ruled round v28 = the hall's left arch). Built from restroom v1
## (night/day).
##
## Paint camera, measured 2026-11-11 from v1's square-to-camera checkerboard (least-squares fit of
## 11 tile rows and the tile widths at five heights, residuals under 3 px): focal 3383 px at 2752 px
## wide, pitch 17.9 deg, camera 9.36 tiles above the floor, 27.8 tiles from the far wall. The vanity
## counter (1.9 tiles tall, ~0.9 m) puts a tile at 0.48 m.

## Room in tiles: far wall at z = 0, the stall fronts at x = LEFT_X, the vanity front at
## x = RIGHT_X, the screen's bottom edge on the floor at z = FRONT_Z.
const LEFT_X := -5.4
const RIGHT_X := 5.5
const WALL_HEIGHT := 14.0
const FRONT_Z := 12.0
const SOUTH_EXIT_TARGET := "absinthe_arcade_interior"

const SPAWNS := {
	"from_hall": [Vector2(0.0, 9.0), "north"],
}

## Fixtures standing on the floor, [centre (x, z), size (x, z)] in tiles, from the painting.
const FLOOR_BLOCKERS := [
	[Vector2(0.0, 0.45), Vector2(4.2, 0.9)],     # the Green Fairy's plinth
	[Vector2(-3.7, 0.5), Vector2(1.4, 1.0)],     # mop bucket and wet-floor sign
	[Vector2(3.95, 0.4), Vector2(0.8, 0.8)],     # bin beside the statue
	[Vector2(5.6, 1.0), Vector2(1.2, 2.0)],      # urinals
	[Vector2(4.85, 9.15), Vector2(0.8, 0.8)],    # bin at the vanity
]


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/restroom/aa_int_restroom_"
	focal_px = 3383.0
	pitch_deg = 17.88
	cam_height = 9.36
	cam_z = 27.8
	world_scale = 0.48
	default_spawn = "from_hall"


func _build_room() -> void:
	var mat := _paint_material()
	var front := FRONT_Z + 3.0
	var paint_front := cam_z  # side planes run back to the camera so the screen's edges are covered
	var lb := Vector2(LEFT_X, 0)
	var rb := Vector2(RIGHT_X, 0)
	# The far wall runs past both side planes so the plinth niche and urinals have somewhere to land.
	_wall("far_wall", Vector2(-9.0, 0), Vector2(9.0, 0), WALL_HEIGHT, mat)
	_wall("left_stalls", Vector2(LEFT_X, paint_front), lb, WALL_HEIGHT, mat)
	_wall("right_vanity", rb, Vector2(RIGHT_X, paint_front), WALL_HEIGHT, mat)
	_floor("floor", Vector2(0, front * 0.5), Vector2(18.0, front + 0.5), mat)

	var body := _collision_body("room_collision")
	_box(body, Vector3(0, -0.1, front * 0.5), Vector3(18.0, 0.2, front + 0.5))
	for seg: Array in [[lb, rb], [Vector2(LEFT_X, front), lb], [rb, Vector2(RIGHT_X, front)]]:
		_wall_collider(body, seg[0], seg[1])
	for spec: Array in FLOOR_BLOCKERS:
		var c: Vector2 = spec[0]
		var sz: Vector2 = spec[1]
		_box(body, Vector3(c.x, 1.0, c.y), Vector3(sz.x, 2.0, sz.y))
	# Behind the south exit, so walking through it never steps off the floor.
	_wall_collider(body, Vector2(LEFT_X, FRONT_Z + 1.2), Vector2(RIGHT_X, FRONT_Z + 1.2))


func _build_markers() -> void:
	_exit("exit_south_to_hall", SOUTH_EXIT_TARGET, "from_restroom",
		Vector3(0, 1.0, FRONT_Z + 0.4), Vector3(RIGHT_X - LEFT_X, 2.0, 0.8))
	_spawns(SPAWNS)
	_build_statue()
	_build_statue_hands()
	_build_interact_points()


# --- The bronze Green Fairy herself (bead Eurobound-pg9a) ---------------------------------------
## The whole statue (wings, gown, plinth, both roll stacks) is cut out of the plates, which now show
## an empty arched niche behind her. She is ONE quad painted with the projected paint shader from
## props/statue.json (top-left and size on the 2752x1536 plate; day, night and emit share one alpha),
## so from the gameplay camera she lands on exactly the pixels she was cut from. Layer order, back to
## front (restroom location_nodes, feature_details.aa_node_restroom_statue.occlusion): plate niche,
## this quad, Jakub (JAKUB_AT.z), her two hand cut-outs (HANDS_Z).
const STATUE_JSON := "statue.json"
## Floor-plan z of the statue quad: in front of the niche wall (z 0) and behind Jakub (JAKUB_AT.z 0.8).
## Not below 0.55: the cut-out box's bottom plate row (831) meets the floor at z ~0.55, and a plane
## farther back would sink the plinth under the floor, which would hide it.
const STATUE_Z := 0.6
var statue: MeshInstance3D
var _statue_spec: Dictionary = {}


func _build_statue() -> void:
	var path := HANDS_DIR + STATUE_JSON
	if not FileAccess.file_exists(path):
		return
	_statue_spec = Dictionary(JSON.parse_string(FileAccess.get_file_as_string(path)))
	var xy: Array = _statue_spec["plate_xy"]
	var size: Array = _statue_spec["size"]
	var box := Rect2(float(xy[0]), float(xy[1]), float(size[0]), float(size[1]))
	var mat := ShaderMaterial.new()
	mat.shader = PAINT_SHADER
	mat.set_shader_parameter("paint_view", Projection(_camera.global_transform.affine_inverse()))
	mat.set_shader_parameter("focal_px", focal_px)
	mat.set_shader_parameter("image_px", PAINT_IMAGE_PX)
	mat.set_shader_parameter("use_alpha", true)
	mat.set_shader_parameter("rect_px", Vector4(box.position.x, box.position.y, box.size.x, box.size.y))
	mat.render_priority = 1
	# A snug quad over the plate box as seen on the plane z = STATUE_Z (the shader discards the rest).
	var lo := Vector2(INF, INF)
	var hi := Vector2(-INF, -INF)
	for corner: Vector2 in [box.position, Vector2(box.end.x, box.position.y), box.end, Vector2(box.position.x, box.end.y)]:
		var p := plate_point_on_plane(corner, STATUE_Z)
		lo = lo.min(Vector2(p.x, p.y))
		hi = hi.max(Vector2(p.x, p.y))
	var quad := QuadMesh.new()
	quad.size = (hi - lo) + Vector2(0.2, 0.2)
	statue = MeshInstance3D.new()
	statue.name = String(_statue_spec.get("object_id", "green_fairy_statue"))
	statue.mesh = quad
	statue.material_override = mat
	statue.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	statue.position = Vector3((lo.x + hi.x) * 0.5, (lo.y + hi.y) * 0.5, STATUE_Z)
	statue.set_meta("interact_id", String(_statue_spec.get("object_id", "")))
	statue.set_meta("node_id", String(_statue_spec.get("node_id", "")))
	_diorama.add_child(statue)
	_apply_statue_textures()


func _apply_statue_textures() -> void:
	if statue == null:
		return
	var files: Dictionary = _statue_spec.get("files", {})
	var mat: ShaderMaterial = statue.material_override
	mat.set_shader_parameter("albedo_tex", load(HANDS_DIR + String(files["night" if night else "day"])))
	var lit := night and files.has("emit")
	mat.set_shader_parameter("use_emission", lit)
	if lit:
		mat.set_shader_parameter("emit_tex", load(HANDS_DIR + String(files["emit"])))


## Where the paint camera's ray through plate pixel `px` meets the vertical plane z (diorama tiles).
func plate_point_on_plane(px: Vector2, z: float) -> Vector3:
	var cam := _diorama.to_local(_camera.global_position)
	var d := Vector3((px.x - PAINT_IMAGE_PX.x * 0.5) / focal_px, -(px.y - PAINT_IMAGE_PX.y * 0.5) / focal_px, -1.0)
	var dir := (_diorama.global_transform.basis.inverse() * (_camera.global_transform.basis * d)).normalized()
	return cam + dir * ((z - cam.z) / dir.z)


# --- Interaction points (ids from the restroom location files) ----------------------------------
## Id -> [point (x, z), where the bros stand (x, z)] in tiles. green_fairy_statue is the interaction
## of node aa_node_restroom_statue (absinthe_arcade_restroom_location_nodes.json); the point is the
## plinth's front edge, the stand spot just in front of it.
const INTERACT_POINTS := {
	"green_fairy_statue": [Vector2(0.0, 0.9), Vector2(0.0, 2.0)],
}


func _build_interact_points() -> void:
	for id: String in INTERACT_POINTS.keys():
		var at: Vector2 = INTERACT_POINTS[id][0]
		var stand: Vector2 = INTERACT_POINTS[id][1]
		var m := Marker3D.new()
		m.name = "interact_" + id
		m.position = Vector3(at.x, 0, at.y)
		m.add_to_group("interact_points")
		m.set_meta("interact_id", id)
		_diorama.add_child(m)
		SceneRouter.add_spawn_point(_diorama, "at_" + id, Vector3(stand.x, 0, stand.y), "north")


# --- The Green Fairy's hands in front of whatever she holds -----------------------------------
## Her two bronze hands with the front pair of toilet rolls, cut from the plate (statue_hands.json:
## top-left and size on the 2752x1536 plate). Each piece is painted with the room's own projected
## paint material on a quad standing just in front of her forearm line, so it shows exactly the plate
## pixels it was cut from and covers anything lying across her arms (Jakub, 01:00-06:00).
const HANDS_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/restroom/props/"
## Floor-plan z of the quads: between Jakub (JAKUB_AT.z) and the camera.
const HANDS_Z := 1.4
var statue_hands: Dictionary = {}  ## side -> MeshInstance3D
var _hand_specs: Dictionary = {}


func _build_statue_hands() -> void:
	var path := HANDS_DIR + "statue_hands.json"
	if not FileAccess.file_exists(path):
		return
	_hand_specs = Dictionary(JSON.parse_string(FileAccess.get_file_as_string(path))).get("pieces", {})
	var night_specs: Dictionary = _hand_specs.get("night", {})
	for side: String in night_specs.keys():
		var mat := ShaderMaterial.new()
		mat.shader = PAINT_SHADER
		mat.set_shader_parameter("paint_view", Projection(_camera.global_transform.affine_inverse()))
		mat.set_shader_parameter("focal_px", focal_px)
		mat.set_shader_parameter("image_px", PAINT_IMAGE_PX)
		mat.set_shader_parameter("use_alpha", true)
		mat.render_priority = 1
		var quad := QuadMesh.new()
		quad.size = Vector2(6.0, 3.0)  # generous: the shader discards everything outside the piece
		var mi := MeshInstance3D.new()
		mi.name = "statue_hand_" + side
		mi.mesh = quad
		mi.material_override = mat
		mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
		mi.position = Vector3(-3.0 if side == "left" else 3.0, JAKUB_AT.y, HANDS_Z)
		_diorama.add_child(mi)
		statue_hands[side] = mi
	_apply_hand_textures()


func _apply_hand_textures() -> void:
	var tag := "night" if night else "day"
	for side: String in statue_hands.keys():
		var spec: Dictionary = Dictionary(_hand_specs.get(tag, {})).get(side, {})
		if spec.is_empty():
			continue
		var mat: ShaderMaterial = (statue_hands[side] as MeshInstance3D).material_override
		mat.set_shader_parameter("albedo_tex", load(HANDS_DIR + String(spec["file"])))
		mat.set_shader_parameter("rect_px", Vector4(spec["plate_xy"][0], spec["plate_xy"][1],
			spec["size"][0], spec["size"][1]))


func _apply_time_of_day() -> void:
	super()
	_apply_statue_textures()
	_apply_hand_textures()


# --- Jakub's restroom scene (Writers' Room, approved by the author 2026-11-12) --------------------
## From 01:00 until morning Jakub "Tokens" Dvořák sleeps it off at the bronze Green Fairy. The first
## visit in those hours plays the scene (one-shot); he stays asleep there afterwards. Spoken lines
## are verbatim from WritingRoom/tasks/20261111_1412_jakub_restroom_scene/final.md; stage directions
## are beats (no narrator).

const JAKUB_FLAG := "jakub_restroom_discovered"
const JAKUB_HOURS := Vector2i(1, 6)
const JAKUB_ASLEEP := "res://assets/characters/npcs/absinthe_arcade/jakub_tokens_dvorak_asleep_cradled.png"
## Cradled across the Green Fairy's forearms, between the toilet-paper rolls (author-approved pose,
## round v41/v42): x 0, 4.79 tiles up (her forearm line), just in front of the statue.
const JAKUB_AT := Vector3(0.0, 4.79, 0.8)
## Sprite pixels to lift the art so his back and thighs rest on her forearm line; depends on the art
## (pixel v3: +7, its figure centred on row 71). The 3D render (Tripo + Blender, blind G4-S pass,
## 2026-11-14) is centred on its 562x327 canvas, so it needs none.
const JAKUB_OFFSET_PX := 0.0
## The 3D render's density, the same as the bros' look-B frames (CharacterLooks.DEFAULT_PPM).
const JAKUB_PPM := 300.0
const FLAIR_PIN := "jakub_tokens_flair_pin"

const PILSNER := "LORD PILSNER"
const BRADLEY := "BRADLEY"
const CHADWICK := "CHADWICK"
const JAKUB := "JAKUB"
const TOMAS_VO := "TOMÁŠ (V.O.)"

var dialogue: DialogueBox
var jakub_asleep: Sprite3D
var _player: PlayerController


static func jakub_here(state) -> bool:
	return GameClock.in_hours(GameClock.hour(state), JAKUB_HOURS.x, JAKUB_HOURS.y)


func _ready() -> void:
	super()
	if Engine.is_editor_hint() or not spawn_player:
		return
	dialogue = DialogueBox.new()
	dialogue.field_state = GameState
	dialogue.name = "dialogue"
	add_child(dialogue)
	_player = get_tree().get_nodes_in_group("player").filter(func(n): return is_ancestor_of(n)).front()
	if jakub_here(GameState):
		_place_jakub()
		if not bool(GameState.flags.get(JAKUB_FLAG, false)):
			jakub_scene.call_deferred()


func _place_jakub() -> void:
	jakub_asleep = Sprite3D.new()
	jakub_asleep.name = "jakub_asleep"
	jakub_asleep.texture = load(JAKUB_ASLEEP)
	jakub_asleep.pixel_size = 1.0 / JAKUB_PPM
	jakub_asleep.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	jakub_asleep.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS  # a 3D render, not pixel art
	jakub_asleep.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	jakub_asleep.offset = Vector2(0.0, JAKUB_OFFSET_PX)
	add_child(jakub_asleep)
	jakub_asleep.global_position = _diorama.to_global(JAKUB_AT)


func jakub_scene() -> void:
	if _player != null:
		_player.input_locked = true
	var d := dialogue
	await d.beat(1.0)
	await d.say(PILSNER, "Look at that. High class. Back home you pass out in a stall and someone steals your shoes. Over here, the decor cradles you.")
	await d.say(BRADLEY, "That statue's got insane traps. Look at her lats. Holding up a whole dude and two rolls of paper without spotting. Respect.")
	await d.say(CHADWICK, "Dude, this goes so hard. I’m filming this right now. If I put techno over this, we hit ten thousand views by morning.")
	await d.say(PILSNER, "Shh. Don't crowd him. He's doing Euromemeian union business.")
	await d.beat()
	await d.say(JAKUB, "...One SOV, one token... don't squeeze the wings, sir... she's a professional...")
	await d.say(BRADLEY, "Hey bro. Skee-ball machine ate my coin and spit out an old peanut. Hit the lever for me.")
	await d.say(JAKUB, "...Always hit her on the left side... like people... left hip, orange spit... two tokens for the roll...")
	await d.say(PILSNER, "Genius. The guy runs customer service while he's unconscious. That’s work ethic.")
	await d.say(CHADWICK, "Dude, ask him if he wants to be in my video. Bro, thumbs up for the camera!")
	await d.beat()
	await d.say(JAKUB, "WELCOME TO THE ABSINTHE ARCADE! TOKENS ARE ONE SOV! TOILET PAPER IS COMPLIMENTARY FOR THE FIRST WIPE!")
	await d.beat()
	await d.say(BRADLEY, "Nice pipes. Solid diaphragm projection.")
	await d.beat()
	GameState.add_item(FLAIR_PIN)
	await d.say("", "Item Received: \"ASK ME ABOUT TOKENS\" Pin")
	await d.beat()
	await d.say(TOMAS_VO, "Tokens. Toilet.")
	await d.say(JAKUB, "...Already here, boss... she loves me...")
	await d.say(PILSNER, "Man's living the dream. Let's go win some plastic crap.")
	d.close()
	GameState.flags[JAKUB_FLAG] = true
	if _player != null:
		_player.input_locked = false
