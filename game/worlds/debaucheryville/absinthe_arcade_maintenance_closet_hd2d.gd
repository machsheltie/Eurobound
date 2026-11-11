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
