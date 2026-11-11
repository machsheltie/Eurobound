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
