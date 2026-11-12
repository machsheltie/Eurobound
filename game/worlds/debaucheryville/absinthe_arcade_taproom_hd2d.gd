@tool
extends HD2DProjectedRoom
## HD-2D The Absinthium Taproom, behind the green curtain in the Absinthe Arcade's north wing
## (round v34 nw_taproom_curtain = follow_design: the curtain is the Taproom entrance). Built from
## Taproom v5 (approved round v39; underground, so the night plate serves day too).
## The Taproom's own content (Dr. Vanek, the opener checks, the mirror maze, the Absinthe Lager) is
## not built yet; this is the walkable room and its way in and out.
##
## Paint camera, measured 2026-11-12 from v5's diagonal checkerboard (diamond widths at six heights
## and the diamond height/width ratio): focal 2480 px at 2752 px wide, pitch 17.3 deg, camera 5.58
## units above the floor, 17.09 units from the bar front. A unit is one diamond's diagonal; the bar
## stools (~0.75 m) put it at 0.71 m.

const BAR_Z := 0.0
const LEFT_WALL := [Vector2(-4.8, -1.0), Vector2(-6.4, 10.0)]
const RIGHT_WALL := [Vector2(4.6, -1.0), Vector2(6.4, 10.0)]
const WALL_HEIGHT := 12.0
const FRONT_Z := 8.97
const NORTH_WING_TARGET := "absinthe_arcade_north_wing"

const SPAWNS := {
	"from_north_wing": [Vector2(0.0, 7.0), "north"],
	"from_maze": [Vector2(0.0, 7.0), "north"],  # out of the mirror maze (round v44)
}

## The stool row in front of the bar and the four table groups (tables with their chairs), convex
## floor footprints (x, z) in units, from the painting.
const FLOOR_BLOCKERS := [
	[Vector2(-3.5, 1.2), Vector2(2.2, 1.2), Vector2(2.2, 2.1), Vector2(-3.5, 2.1)],      # bar stools
	[Vector2(-5.2, 1.9), Vector2(-2.8, 1.9), Vector2(-2.8, 3.6), Vector2(-5.2, 3.6)],    # back-left table
	[Vector2(-4.8, 5.4), Vector2(-2.4, 5.4), Vector2(-2.4, 7.6), Vector2(-4.8, 7.6)],    # front-left table
	[Vector2(2.2, 2.3), Vector2(4.8, 2.3), Vector2(4.8, 4.0), Vector2(2.2, 4.0)],        # back-right table
	[Vector2(2.6, 5.6), Vector2(5.2, 5.6), Vector2(5.2, 7.8), Vector2(2.6, 7.8)],        # front-right table
]


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/taproom/aa_int_taproom_"
	focal_px = 2480.0
	pitch_deg = 17.3
	cam_height = 5.58
	cam_z = 17.09
	world_scale = 0.71
	default_spawn = "from_north_wing"


static func _x_at(line: Array, z: float) -> float:
	var a: Vector2 = line[0]
	var b: Vector2 = line[1]
	return a.x + (b.x - a.x) * (z - a.y) / (b.y - a.y)


func _build_room() -> void:
	var mat := _paint_material()
	var far := cam_z
	var back := -3.0  # the bottle, the back bar and the shelves land on this plane
	_wall("back_wall", Vector2(-14.0, back), Vector2(14.0, back), WALL_HEIGHT, mat)
	_wall("bar_front", Vector2(-4.6, BAR_Z), Vector2(4.4, BAR_Z), 1.6, mat)
	var lf := Vector2(_x_at(LEFT_WALL, far), far)
	var rf := Vector2(_x_at(RIGHT_WALL, far), far)
	var lb := Vector2(_x_at(LEFT_WALL, back), back)
	var rb := Vector2(_x_at(RIGHT_WALL, back), back)
	_wall("left_wall", lf, lb, WALL_HEIGHT, mat)
	_wall("right_wall", rb, rf, WALL_HEIGHT, mat)
	_floor("floor", Vector2(0, (back + far) * 0.5), Vector2(30.0, far - back + 1.0), mat)

	var body := _collision_body("room_collision")
	_box(body, Vector3(0, -0.1, (back + far) * 0.5), Vector3(30.0, 0.2, far - back + 1.0))
	var lbar := Vector2(_x_at(LEFT_WALL, BAR_Z), BAR_Z)
	var rbar := Vector2(_x_at(RIGHT_WALL, BAR_Z), BAR_Z)
	var lfront := Vector2(_x_at(LEFT_WALL, FRONT_Z + 1.2), FRONT_Z + 1.2)
	var rfront := Vector2(_x_at(RIGHT_WALL, FRONT_Z + 1.2), FRONT_Z + 1.2)
	for seg: Array in [[lbar, rbar], [lfront, lbar], [rbar, rfront], [lfront, rfront]]:
		_wall_collider(body, seg[0], seg[1])
	for fp: Array in FLOOR_BLOCKERS:
		_footprint(body, fp)


func _build_markers() -> void:
	# Back out through the curtain: the bottom edge of the screen, where the bros came in.
	_exit("exit_curtain_to_north_wing", NORTH_WING_TARGET, "from_taproom",
		Vector3(0, 1.0, FRONT_Z + 0.5), Vector3(8.0, 2.0, 0.8))
	_spawns(SPAWNS)
