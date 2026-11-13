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

## A compulsion (Compulsion, Eurobound-fe10) started or ended on the leader. For "stare" the screen
## that listens shows the epiphany box (its lines are not written yet, so nothing is shown here).
signal compulsion_started(kind: String, status_id: String)
signal compulsion_ended(kind: String, status_id: String)

var sprite: PartySprite3D
## World direction the leader faces on the ground plane (last direction walked).
var facing_dir := Vector3.BACK
## While a menu or screen is up the bros don't walk or use things.
var input_locked := false
## The followers' sprites, front to back. top_level, so they move along the trail, not with the body.
var followers: Array[PartySprite3D] = []
## Where the leader has been, newest first, a point every TRAIL_STEP metres.
var _trail: Array[Vector3] = []
## Where the leader stood last physics tick, for counting metres walked (FieldStatus steps).
var _last_pos := Vector3.ZERO
var _last_pos_set := false
## True while a compulsion runs. Separate from input_locked so releasing it never frees a menu or
## dialogue lock somebody else set. Always cleared by _end_compulsion: expiry, cure or leaving the
## tree (law sections 3 and 7: no softlock).
var compulsion_locked := false
## The running compulsion: {id, kind, left, lasts, origin, target (Node3D or null)}.
var _comp: Dictionary = {}
## Progress toward the next compulsion per status id (metres or seconds, by the data's unit).
var _comp_acc: Dictionary = {}


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
	# CharacterLooks picks pixel or 3D (assets/data/party/character_looks.json) and sizes the sprite.
	CharacterLooks.dress(s, who, BROS.get(who, BROS["lord_pilsner"]))


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


func _exit_tree() -> void:
	if compulsion_locked:
		_end_compulsion(false)


func is_locked() -> bool:
	return input_locked or compulsion_locked


func _unhandled_input(event: InputEvent) -> void:
	if not is_locked() and event.is_action_pressed("interact"):
		get_viewport().set_input_as_handled()
		try_interact()
	elif not is_locked() and event.is_action_pressed("menu"):
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
	if is_locked():
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
	if state != null:
		_update_compulsion(state, delta, _count_steps(state))


## 1 step = 1 metre walked by the leader (author eb8-q1). A jump of more than STEP_JUMP_M in one
## tick is a teleport or scene placement, not walking, and counts nothing.
const STEP_JUMP_M := 1.0


func _count_steps(state) -> float:
	var moved := 0.0
	if _last_pos_set:
		moved = Vector2(global_position.x - _last_pos.x, global_position.z - _last_pos.z).length()
	_last_pos = global_position
	_last_pos_set = true
	if moved > 0.0 and moved <= STEP_JUMP_M:
		FieldStatus.add_metres(state, moved)
		return moved
	return 0.0


## Counts progress toward each live compulsion (Compulsion.specs: null numbers never appear) and
## starts one when its interval is reached. Never starts while a menu or dialogue holds the input.
func _update_compulsion(state, delta: float, moved: float) -> void:
	var specs := Compulsion.specs(state, bro)
	if compulsion_locked:
		_comp["left"] = float(_comp["left"]) - delta
		var still := false
		for s in specs:
			still = still or String(s["id"]) == String(_comp["id"])
		if float(_comp["left"]) <= 0.0 or not still:
			_end_compulsion(true)
		return
	var ids := []
	for s in specs:
		ids.append(String(s["id"]))
	for id in _comp_acc.keys():
		if not ids.has(id):
			_comp_acc.erase(id)
	if input_locked:
		return
	for s in specs:
		var id := String(s["id"])
		_comp_acc[id] = float(_comp_acc.get(id, 0.0)) + (moved if String(s["unit"]) == Compulsion.UNIT_STEPS else delta)
		if float(_comp_acc[id]) >= float(s["amount"]):
			_comp_acc[id] = 0.0
			_start_compulsion(s)
			return


func _start_compulsion(spec: Dictionary) -> void:
	var target: Node3D = null
	if String(spec["kind"]) == Compulsion.KIND_CLEAN:
		target = _nearest_interact_point_any()
		if target == null:
			return  # nothing to clean: no control is lost for nothing
	compulsion_locked = true
	_comp = {"id": spec["id"], "kind": spec["kind"], "left": spec["lasts"], "lasts": spec["lasts"],
		"origin": global_position, "target": target}
	compulsion_started.emit(String(spec["kind"]), String(spec["id"]))


## Always releases. `emit` is false when leaving the tree.
func _end_compulsion(emit: bool) -> void:
	var kind := String(_comp.get("kind", ""))
	var id := String(_comp.get("id", ""))
	if emit and kind == Compulsion.KIND_CLEAN:
		var origin: Vector3 = _comp["origin"]
		if Vector2(global_position.x - origin.x, global_position.z - origin.z).length() > 0.2:
			global_position = Vector3(origin.x, global_position.y, origin.z)  # he returns
	compulsion_locked = false
	_comp = {}
	if emit:
		compulsion_ended.emit(kind, id)


## Nearest interaction point in any direction (the cleaning bro need not face it).
func _nearest_interact_point_any() -> Node3D:
	var best: Node3D = null
	var best_d := INF
	for n in get_tree().get_nodes_in_group("interact_points"):
		var p := n as Node3D
		if p == null:
			continue
		var d := Vector2(p.global_position.x - global_position.x, p.global_position.z - global_position.z).length()
		if d < best_d:
			best_d = d
			best = p
	return best


## Forced walking direction of the running clean compulsion: out to the point for the first half of
## its length, back to where he started for the second. Zero for stare.
func _compulsion_dir() -> Vector3:
	if String(_comp.get("kind", "")) != Compulsion.KIND_CLEAN:
		return Vector3.ZERO
	var goal: Vector3 = _comp["origin"]
	var target: Variant = _comp.get("target", null)
	if float(_comp["left"]) > float(_comp["lasts"]) * 0.5 and is_instance_valid(target):
		goal = (target as Node3D).global_position
	var to := Vector3(goal.x - global_position.x, 0.0, goal.z - global_position.z)
	if to.length() < 0.3:
		return Vector3.ZERO
	return to.normalized()


## Green Fairy Confusion reverses the controls (the_absinthium_taproom.md 283-287).
static func reversed_input(input: Vector2, reversed: bool) -> Vector2:
	return -input if reversed else input


## One physics tick of walking with stick/keys `input` (x right, y down, as Input.get_vector gives).
func step(input: Vector2, delta: float) -> void:
	var cam := get_viewport().get_camera_3d()
	var dir := Vector3.ZERO if is_locked() else move_direction(input, cam)
	if compulsion_locked:
		dir = _compulsion_dir()
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
