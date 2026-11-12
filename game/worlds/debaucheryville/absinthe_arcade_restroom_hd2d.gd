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


# --- Jakub's restroom scene (Writers' Room, approved by the author 2026-11-12) --------------------
## From 01:00 until morning Jakub "Tokens" Dvořák sleeps it off at the bronze Green Fairy. The first
## visit in those hours plays the scene (one-shot); he stays asleep there afterwards. Spoken lines
## are verbatim from WritingRoom/tasks/20261111_1412_jakub_restroom_scene/final.md; stage directions
## are beats (no narrator).

const JAKUB_FLAG := "jakub_restroom_discovered"
const JAKUB_HOURS := Vector2i(1, 6)
const JAKUB_ASLEEP := "res://assets/characters/npcs/absinthe_arcade/jakub_tokens_dvorak_asleep_statue.png"
## Left of the Fairy's plinth, slumped against her (ad: the pose reaches right, toward her leg).
const JAKUB_AT := Vector2(-2.6, 1.1)
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
	jakub_asleep.pixel_size = 1.8 / 117.0  # the bros' pixel density
	jakub_asleep.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	jakub_asleep.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	jakub_asleep.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	jakub_asleep.offset = Vector2(0, 64.0 - 126.0 + 64.0)  # feet row 126 of the 128 px frame on the floor
	add_child(jakub_asleep)
	jakub_asleep.global_position = _diorama.to_global(Vector3(JAKUB_AT.x, 0, JAKUB_AT.y))


func jakub_scene() -> void:
	if _player != null:
		_player.input_locked = true
	var d := dialogue
	await d.beat(1.0)
	await d.say(PILSNER, "Look at that. High class. Back home you pass out in a stall and someone steals your shoes. Over here, the decor cradles you.")
	await d.say(BRADLEY, "That statue's got insane traps. Look at her lats. Holding up a whole dude and two rolls of paper without spotting. Respect.")
	await d.say(CHADWICK, "Dude, this goes so hard. I’m filming this right now. If I put techno over this, we hit ten thousand views by morning.")
	await d.say(PILSNER, "Shh. Don't crowd him. He's doing European union business.")
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
