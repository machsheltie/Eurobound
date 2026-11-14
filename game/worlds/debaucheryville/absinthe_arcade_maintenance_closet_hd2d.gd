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
## The Tekken haiku and the wiring have no painted spot yet; they sit on free wall.
const INTERACT_POINTS := {
	ClosetProps.DDR_TOILET: [Vector2(0.25, 0.0), Vector2(0.25, 2.6)],
	ClosetProps.CRT_MIRROR: [Vector2(-2.0, 0.0), Vector2(-2.0, 2.2)],
	ClosetProps.SOCK_CHUTE: [Vector2(2.8, 0.0), Vector2(2.8, 2.4)],
	ClosetProps.SPARKING_WIRING: [Vector2(4.75, 5.5), Vector2(3.9, 5.5)],
	ClosetProps.GRAFFITI_SMAAAASH: [Vector2(-3.0, 1.6), Vector2(-2.2, 1.6)],
	ClosetProps.GRAFFITI_JOYSTICK: [Vector2(-3.1, 2.4), Vector2(-2.3, 2.4)],
	ClosetProps.GRAFFITI_BOOBS: [Vector2(-3.2, 3.2), Vector2(-2.4, 3.2)],
	ClosetProps.GRAFFITI_HAIKU: [Vector2(-3.8, 6.0), Vector2(-3.0, 6.0)],
	ClosetProps.GRAFFITI_CHEAT_CODES: [Vector2(4.6, 2.6), Vector2(3.7, 2.6)],
}

## Runtime only.
var dialogue: DialogueBox
var _player: PlayerController
var _talking := false
var _visits := {}
var _shame := ClosetProps.new()


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


func _build_markers() -> void:
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


## The 30-second shame timer: lingering in the closet earns the announcer's next line.
func _process(delta: float) -> void:
	if Engine.is_editor_hint() or dialogue == null or _talking:
		return
	var line := _shame.tick_shame(delta)
	if line != "":
		_show([{"who": ClosetProps.NO_SPEAKER, "line": line}])


func _on_interacted(id: String) -> void:
	if _talking or not ClosetProps.IDS.has(id):
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
