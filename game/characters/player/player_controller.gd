class_name PlayerController
extends CharacterBody3D
## The bro the player walks around the HD-2D screens. Movement is camera-relative, so "up" always
## walks away from the fixed camera, Bravely Default / Star Ocean 2R style. The body never scales;
## its PartySprite3D child is in the "hall_actors" group, so rooms with a depth curve can shrink
## the sprite without touching physics.

const BROS := {
	"chadwick": "res://assets/characters/party/chadwick/chadwick.aseprite",
	"bradley": "res://assets/characters/party/bradley/bradley.aseprite",
	"lord_pilsner": "res://assets/characters/party/lord_pilsner/lord_pilsner.aseprite",
}
## Reach for using things (cabinets, machines, NPCs), real metres on the ground plane.
const INTERACT_RANGE := 1.0
## Walking pace in real metres per second (feel tuning, not a game stat).
const WALK_SPEED := 3.2
const GRAVITY := 20.0

## Which bro walks (vertical-slice spec: Lord Pilsner).
@export var bro := "lord_pilsner"

## The player pressed interact next to an interaction point (group "interact_points", meta
## interact_id). What it does is up to the screen that listens.
signal interacted(interact_id: String)

var sprite: PartySprite3D


func _init() -> void:
	add_to_group("player")
	var shape := CollisionShape3D.new()
	shape.name = "body_shape"
	var capsule := CapsuleShape3D.new()
	capsule.radius = 0.25
	capsule.height = 1.6
	shape.shape = capsule
	shape.position.y = 0.8
	add_child(shape)
	sprite = PartySprite3D.new()
	sprite.name = "sprite"
	sprite.add_to_group("hall_actors")
	add_child(sprite)


func _ready() -> void:
	ensure_input_actions()
	floor_snap_length = 0.3
	var frames: SpriteFrames = load(BROS.get(bro, BROS["lord_pilsner"]))
	if frames == null:
		return
	sprite.sprite_frames = frames
	var used := frames.get_frame_texture(frames.get_animation_names()[0], 0).get_image().get_used_rect()
	sprite.content_height_px = used.size.y
	sprite.feet_row_px = used.end.y - 1
	sprite.action = sprite.action  # replay now that frames exist


func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("interact"):
		try_interact()


## The closest interaction point within reach, or null.
func nearest_interactable() -> Node3D:
	var best: Node3D = null
	var best_d := INTERACT_RANGE
	for n in get_tree().get_nodes_in_group("interact_points"):
		var p := n as Node3D
		if p == null:
			continue
		var d := Vector2(p.global_position.x - global_position.x, p.global_position.z - global_position.z).length()
		if d <= best_d:
			best_d = d
			best = p
	return best


## Uses the closest interaction point in reach, if any.
func try_interact() -> void:
	var p := nearest_interactable()
	if p != null:
		interacted.emit(String(p.get_meta("interact_id")))


func _physics_process(delta: float) -> void:
	step(Input.get_vector("move_left", "move_right", "move_up", "move_down"), delta)


## One physics tick of walking with stick/keys `input` (x right, y down, as Input.get_vector gives).
func step(input: Vector2, delta: float) -> void:
	var cam := get_viewport().get_camera_3d()
	var dir := move_direction(input, cam)
	velocity.x = dir.x * WALK_SPEED
	velocity.z = dir.z * WALK_SPEED
	velocity.y = 0.0 if is_on_floor() else velocity.y - GRAVITY * delta
	move_and_slide()
	if dir.length_squared() > 0.0001:
		sprite.face_world_direction(dir, cam)
		sprite.action = "walk"
	else:
		sprite.action = "idle"


## Ground-plane direction for `input`, relative to `camera`: up walks away from it, right walks
## screen-right. Never longer than 1, so diagonals are not faster.
static func move_direction(input: Vector2, camera: Camera3D) -> Vector3:
	if input.length_squared() < 0.0001:
		return Vector3.ZERO
	var fwd := Vector3.FORWARD
	var right := Vector3.RIGHT
	if camera != null:
		fwd = -camera.global_basis.z
		fwd.y = 0.0
		fwd = fwd.normalized()
		right = Vector3(-fwd.z, 0.0, fwd.x)
	var dir := right * input.x + fwd * -input.y
	return dir.limit_length(1.0)


## Registers the movement and interact actions (keyboard, d-pad and left stick) if the project
## does not define them, so every screen works without editing project.godot.
static func ensure_input_actions() -> void:
	var keys := {
		"move_up": [KEY_W, KEY_UP], "move_down": [KEY_S, KEY_DOWN],
		"move_left": [KEY_A, KEY_LEFT], "move_right": [KEY_D, KEY_RIGHT],
		"interact": [KEY_E, KEY_SPACE, KEY_ENTER],
	}
	var pads := {
		"move_up": JOY_BUTTON_DPAD_UP, "move_down": JOY_BUTTON_DPAD_DOWN,
		"move_left": JOY_BUTTON_DPAD_LEFT, "move_right": JOY_BUTTON_DPAD_RIGHT,
		"interact": JOY_BUTTON_A,
	}
	var axes := {
		"move_up": [JOY_AXIS_LEFT_Y, -1.0], "move_down": [JOY_AXIS_LEFT_Y, 1.0],
		"move_left": [JOY_AXIS_LEFT_X, -1.0], "move_right": [JOY_AXIS_LEFT_X, 1.0],
	}
	for action: String in keys.keys():
		if InputMap.has_action(action):
			continue
		InputMap.add_action(action, 0.25)
		for k: Key in keys[action]:
			var ev := InputEventKey.new()
			ev.physical_keycode = k
			InputMap.action_add_event(action, ev)
		var jb := InputEventJoypadButton.new()
		jb.button_index = pads[action]
		InputMap.action_add_event(action, jb)
		if axes.has(action):
			var ja := InputEventJoypadMotion.new()
			ja.axis = axes[action][0]
			ja.axis_value = axes[action][1]
			InputMap.action_add_event(action, ja)
