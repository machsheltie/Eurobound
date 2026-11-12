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
## Using something means facing it, EarthBound style (author ruling ef_interact_cue = none,
## 2026-11-10): it must be within this angle of the way the leader faces.
const INTERACT_HALF_ANGLE_DEG := 60.0
## Walking pace in real metres per second (feel tuning, not a game stat).
const WALK_SPEED := 3.2
const GRAVITY := 20.0
## Path distance between bros in the conga line, real metres (feel tuning).
const FOLLOW_GAP := 0.75
## The trail keeps a point every this many metres the leader walks.
const TRAIL_STEP := 0.05

## Which bro walks (vertical-slice spec: Lord Pilsner).
@export var bro := "lord_pilsner"
## The other two walk behind the leader in a line, EarthBound style (author ruling ef_party_walk =
## leader_follow, 2026-11-10). Party order as the bros are always listed.
@export var follower_bros: Array[String] = ["chadwick", "bradley"]

## The player pressed interact next to an interaction point (group "interact_points", meta
## interact_id). What it does is up to the screen that listens.
signal interacted(interact_id: String)

var sprite: PartySprite3D
## World direction the leader faces on the ground plane (last direction walked).
var facing_dir := Vector3.BACK
## While a menu or screen is up the bros don't walk or use things.
var input_locked := false
## The followers' sprites, front to back. top_level, so they move along the trail, not with the body.
var followers: Array[PartySprite3D] = []
## Where the leader has been, newest first, a point every TRAIL_STEP metres.
var _trail: Array[Vector3] = []


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
	for b in follower_bros:
		var f := PartySprite3D.new()
		f.name = "follower_" + b
		f.top_level = true
		f.add_to_group("hall_actors")
		add_child(f)
		followers.append(f)


func _ready() -> void:
	ensure_input_actions()
	floor_snap_length = 0.3
	_dress(sprite, bro)
	for i in followers.size():
		_dress(followers[i], follower_bros[i])
	_seed_trail()


## Loads a bro's frames onto a sprite and sizes it from the frame's visible pixels.
func _dress(s: PartySprite3D, who: String) -> void:
	var frames: SpriteFrames = load(BROS.get(who, BROS["lord_pilsner"]))
	if frames == null:
		return
	s.sprite_frames = frames
	var used := frames.get_frame_texture(frames.get_animation_names()[0], 0).get_image().get_used_rect()
	s.content_height_px = used.size.y
	s.feet_row_px = used.end.y - 1
	s.action = s.action  # replay now that frames exist


## Lines the followers up straight behind the leader (opposite its facing), as if they had
## walked in after it.
func _seed_trail() -> void:
	facing_dir = facing_vector(sprite.facing)
	var back := -facing_dir
	_trail.clear()
	var length := FOLLOW_GAP * followers.size()
	var d := 0.0
	while d <= length + TRAIL_STEP:
		_trail.append(global_position + back * d)
		d += TRAIL_STEP
	for f in followers:
		f.facing = sprite.facing
	_place_followers()


func _unhandled_input(event: InputEvent) -> void:
	if not input_locked and event.is_action_pressed("interact"):
		get_viewport().set_input_as_handled()
		try_interact()
	elif not input_locked and event.is_action_pressed("menu"):
		get_viewport().set_input_as_handled()
		open_menu()


## Opens the field menu; the bros stay put (and the clock with them) until it closes.
func open_menu() -> FieldMenu:
	var state := get_tree().root.get_node_or_null("GameState")
	if state == null or state.party.is_empty():
		return null
	input_locked = true
	var menu := FieldMenu.new()
	menu.name = "field_menu"
	menu.setup(state)
	get_parent().add_child(menu)
	menu.closed.connect(func() -> void: input_locked = false)
	return menu


## Turns the leader to face a named direction ("north" walks away from a north-looking camera).
func face(direction: String) -> void:
	sprite.facing = direction
	facing_dir = facing_vector(direction)


## World ground-plane vector for a facing name, for a camera looking north (-Z).
static func facing_vector(direction: String) -> Vector3:
	var a := maxi(PartySprite3D.DIRECTIONS.find(direction), 0) * TAU / 8.0
	return Vector3(sin(a), 0.0, cos(a))


## The closest interaction point within reach that the leader faces, or null.
func nearest_interactable() -> Node3D:
	var best: Node3D = null
	var best_d := INTERACT_RANGE
	var min_dot := cos(deg_to_rad(INTERACT_HALF_ANGLE_DEG))
	for n in get_tree().get_nodes_in_group("interact_points"):
		var p := n as Node3D
		if p == null:
			continue
		var to := Vector2(p.global_position.x - global_position.x, p.global_position.z - global_position.z)
		var d := to.length()
		if d > 0.05 and to.normalized().dot(Vector2(facing_dir.x, facing_dir.z).normalized()) < min_dot:
			continue
		if d <= best_d:
			best_d = d
			best = p
	return best


## Uses the closest interaction point in reach, if any.
func try_interact() -> void:
	if input_locked:
		return
	var p := nearest_interactable()
	if p != null:
		interacted.emit(String(p.get_meta("interact_id")))


func _physics_process(delta: float) -> void:
	var input := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	var state := get_tree().root.get_node_or_null("GameState")
	if state != null:
		FieldStatus.tick(state, delta)
		input = reversed_input(input, FieldStatus.controls_reversed(state))
	step(input, delta)


## Green Fairy Confusion reverses the controls (the_absinthium_taproom.md 283-287).
static func reversed_input(input: Vector2, reversed: bool) -> Vector2:
	return -input if reversed else input


## One physics tick of walking with stick/keys `input` (x right, y down, as Input.get_vector gives).
func step(input: Vector2, delta: float) -> void:
	var cam := get_viewport().get_camera_3d()
	var dir := Vector3.ZERO if input_locked else move_direction(input, cam)
	velocity.x = dir.x * WALK_SPEED
	velocity.z = dir.z * WALK_SPEED
	velocity.y = 0.0 if is_on_floor() else velocity.y - GRAVITY * delta
	move_and_slide()
	if dir.length_squared() > 0.0001:
		facing_dir = dir.normalized()
		sprite.face_world_direction(dir, cam)
		sprite.action = "walk"
	else:
		sprite.action = "idle"
	_record_trail()
	_place_followers()


func _record_trail() -> void:
	if _trail.is_empty() or global_position.distance_to(_trail[0]) >= TRAIL_STEP:
		_trail.push_front(global_position)
		var keep := int(ceil(FOLLOW_GAP * (followers.size() + 1) / TRAIL_STEP)) + 4
		if _trail.size() > keep * 4:
			_trail.resize(keep * 4)


## Puts follower i at path distance FOLLOW_GAP * (i + 1) back along the trail; each walks while it
## moves and faces the way it moves.
func _place_followers() -> void:
	var cam := get_viewport().get_camera_3d() if is_inside_tree() else null
	for i in followers.size():
		var f := followers[i]
		var target := _point_along_trail(FOLLOW_GAP * (i + 1))
		var moved := target - f.global_position
		moved.y = 0.0
		f.global_position = target
		if moved.length_squared() > 0.000001:
			f.action = "walk"
			if cam != null:
				f.face_world_direction(moved, cam)
		else:
			f.action = "idle"


## The point `dist` metres back along the trail from the leader (the oldest point if shorter).
func _point_along_trail(dist: float) -> Vector3:
	var prev := global_position
	var walked := 0.0
	for p in _trail:
		var seg := prev.distance_to(p)
		if walked + seg >= dist and seg > 0.0:
			return prev.lerp(p, (dist - walked) / seg)
		walked += seg
		prev = p
	return prev


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
		"cancel": [KEY_ESCAPE, KEY_BACKSPACE, KEY_Q],
		"menu": [KEY_ESCAPE],          # round v36: Esc / Start opens the field menu
	}
	var pads := {
		"move_up": JOY_BUTTON_DPAD_UP, "move_down": JOY_BUTTON_DPAD_DOWN,
		"move_left": JOY_BUTTON_DPAD_LEFT, "move_right": JOY_BUTTON_DPAD_RIGHT,
		"interact": JOY_BUTTON_A,
		"cancel": JOY_BUTTON_B,
		"menu": JOY_BUTTON_START,
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
