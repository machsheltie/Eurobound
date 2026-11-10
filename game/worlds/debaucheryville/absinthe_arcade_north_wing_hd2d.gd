@tool
extends HD2DProjectedRoom
## HD-2D Absinthe Arcade north wing: the cabinet room past the mirror corridor. Built from north
## wing v5 (approved v4 night, reframed to 16:9 and upscaled to 2752x1536, plus a registered day
## relight).
##
## Paint camera, measured 2026-11-10 from v5's diagonal checkerboard (least-squares fit of the
## diamond widths and edge angles in nine bands): focal 4634 px at 2752 px wide, pitch 23.1 deg,
## camera 14.9 tiles above the floor (a tile is one diamond's side). The back-row cabinets
## (~2.7 tiles tall, real ~1.8 m) put a tile at 0.67 m. The painting is not a perfect pinhole, so
## the fit is approximate (about 1 deg of edge angle, 10-30 px of diamond width).

## Room in tiles: back wall (behind the back-row cabinets) at z = BACK_Z, the screen's bottom edge
## on the floor at z = FRONT_Z.
const BACK_Z := -1.2
const FRONT_Z := 16.67
const LEFT_WALL := [Vector2(-7.4, BACK_Z), Vector2(-8.7, 20.0)]
const RIGHT_WALL := [Vector2(7.3, BACK_Z), Vector2(8.0, 20.0)]
const WALL_HEIGHT := 22.0
const SOUTH_EXIT_TARGET := "absinthe_arcade_mirror_corridor"

const SPAWNS := {
	"from_mirror_corridor": [Vector2(0.0, 14.6), "north"],
}

## Cabinet rows with their stools, the DDR machine and the cabinet by the curtained doorway:
## convex floor footprints (x, z) in tiles, from the painting (bases projected to the floor).
const FLOOR_BLOCKERS := [
	[Vector2(-3.9, BACK_Z), Vector2(3.7, BACK_Z), Vector2(3.7, 1.4), Vector2(-3.9, 1.4)],    # back row
	[Vector2(-3.8, BACK_Z), Vector2(-4.9, 8.9), Vector2(-7.6, 8.9), Vector2(-7.4, BACK_Z)],  # left row
	[Vector2(3.5, BACK_Z), Vector2(4.5, 8.7), Vector2(7.6, 8.7), Vector2(7.3, BACK_Z)],      # right row
	[Vector2(3.9, 9.9), Vector2(7.6, 9.9), Vector2(7.7, 13.9), Vector2(3.9, 13.9)],          # DDR machine
	[Vector2(-6.8, 8.8), Vector2(-6.8, 14.4), Vector2(-8.6, 14.4), Vector2(-8.6, 8.8)],      # curtain cabinet
]


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/north_wing/aa_int_north_wing_"
	focal_px = 4634.0
	pitch_deg = 23.1
	cam_height = 14.9
	cam_z = 40.05  # the back-row cabinet fronts (z = 0) are 40.05 tiles ahead of the camera
	world_scale = 0.67
	default_spawn = "from_mirror_corridor"


func _build_room() -> void:
	var mat := _paint_material()
	var lb: Vector2 = LEFT_WALL[0]
	var lf: Vector2 = LEFT_WALL[1]
	var rb: Vector2 = RIGHT_WALL[0]
	var rf: Vector2 = RIGHT_WALL[1]
	_wall("back_wall", lb, rb, WALL_HEIGHT, mat)
	_wall("left_wall", lf, lb, WALL_HEIGHT, mat)
	_wall("right_wall", rb, rf, WALL_HEIGHT, mat)
	var depth := lf.y - BACK_Z
	_floor("floor", Vector2(0, (BACK_Z + lf.y) * 0.5), Vector2(20.0, depth), mat)

	var body := _collision_body("room_collision")
	_box(body, Vector3(0, -0.1, (BACK_Z + lf.y) * 0.5), Vector3(20.0, 0.2, depth))
	for seg: Array in [[lb, rb], [lf, lb], [rb, rf]]:
		_wall_collider(body, seg[0], seg[1])
	for fp: Array in FLOOR_BLOCKERS:
		_footprint(body, fp)
	# Behind the south exit, so walking through it never steps off the floor.
	_wall_collider(body, Vector2(-8.5, FRONT_Z + 1.4), Vector2(8.0, FRONT_Z + 1.4))


func _build_markers() -> void:
	_exit("exit_south_to_corridor", SOUTH_EXIT_TARGET, "from_north_wing",
		Vector3(0, 1.0, FRONT_Z + 0.5), Vector3(16.0, 2.0, 0.8))
	_spawns(SPAWNS)
