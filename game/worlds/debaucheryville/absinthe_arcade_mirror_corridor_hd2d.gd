@tool
extends HD2DProjectedRoom
## HD-2D Absinthe Arcade mirror corridor: the screen between the hall's north arch and the north
## wing (author ruling: its own screen). Built from mirror corridor v1 (night/day).
##
## Paint camera, measured 2026-11-10 from v1's square-to-camera checkerboard (least-squares fit of
## 13 tile rows and the tile widths at three heights): focal 2565 px at 2752 px wide, pitch 19.5
## deg, camera 7.13 tiles above the floor. Painting units here are floor tiles; the benches
## (3.4 x 0.8 tiles, ~1.9 m long) put a tile at 0.55 m.

## Corridor box in tiles: side walls at x = +-WALL_X, far wall at z = 0, the screen's bottom edge
## on the floor at z = FRONT_Z.
const WALL_X := 4.9
const WALL_HEIGHT := 14.0
const FRONT_Z := 15.55
## The far archway to the north wing (measured: floor-line corners x -1.39 / +1.47).
const ARCH := {"x0": -1.42, "x1": 1.42, "height": 5.0, "depth": 6.0}
const NORTH_EXIT_TARGET := "absinthe_arcade_north_wing"
const SOUTH_EXIT_TARGET := "absinthe_arcade_interior"

const SPAWNS := {
	"from_hall": [Vector2(0.0, 13.2), "north"],
	"from_north_wing": [Vector2(0.0, 1.6), "south"],
}

## Benches and potted palms against the walls, [centre (x, z), size (x, z)] in tiles, from the
## painting (bench legs and pot bases projected to the floor).
const FLOOR_BLOCKERS := [
	[Vector2(-4.55, 13.2), Vector2(0.9, 3.6)],    # near benches
	[Vector2(4.55, 13.2), Vector2(0.9, 3.6)],
	[Vector2(-4.1, 7.0), Vector2(1.3, 1.3)],      # near palms
	[Vector2(4.1, 7.0), Vector2(1.3, 1.3)],
	[Vector2(-3.4, 2.6), Vector2(1.0, 2.6)],      # far benches
	[Vector2(3.4, 2.6), Vector2(1.0, 2.6)],
	[Vector2(-2.4, 0.6), Vector2(1.0, 1.0)],      # palms flanking the arch
	[Vector2(2.4, 0.6), Vector2(1.0, 1.0)],
]


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/mirror_corridor/aa_int_corridor_"
	focal_px = 2565.0
	pitch_deg = 19.5
	cam_height = 7.13
	cam_z = 25.3
	world_scale = 0.55
	default_spawn = "from_hall"


func _build_room() -> void:
	var mat := _paint_material()
	var x0: float = ARCH["x0"]
	var x1: float = ARCH["x1"]
	var ah: float = ARCH["height"]
	var deep: float = -float(ARCH["depth"])
	var lb := Vector2(-WALL_X, 0)
	var rb := Vector2(WALL_X, 0)
	var front := FRONT_Z + 3.0
	_wall("far_wall_left", lb, Vector2(x0, 0), WALL_HEIGHT, mat)
	_wall("far_wall_right", Vector2(x1, 0), rb, WALL_HEIGHT, mat)
	var lintel := _wall("far_wall_lintel", Vector2(x0, 0), Vector2(x1, 0), WALL_HEIGHT - ah, mat)
	lintel.position.y = ah
	_wall("arch_left", Vector2(x0, 0), Vector2(x0, deep), ah, mat)
	_wall("arch_right", Vector2(x1, deep), Vector2(x1, 0), ah, mat)
	_wall("arch_end", Vector2(x0, deep), Vector2(x1, deep), ah, mat)
	_floor("arch_floor", Vector2((x0 + x1) * 0.5, deep * 0.5), Vector2(x1 - x0, -deep), mat)
	_wall("left_wall", Vector2(-WALL_X, front), lb, WALL_HEIGHT, mat)
	_wall("right_wall", rb, Vector2(WALL_X, front), WALL_HEIGHT, mat)
	_floor("floor", Vector2(0, front * 0.5), Vector2(WALL_X * 2.0 + 2.0, front + 0.5), mat)

	var body := _collision_body("room_collision")
	_box(body, Vector3(0, -0.1, front * 0.5), Vector3(WALL_X * 2.0 + 2.0, 0.2, front + 0.5))
	_box(body, Vector3((x0 + x1) * 0.5, -0.1, deep * 0.5), Vector3(x1 - x0 + 0.6, 0.2, -deep))
	for seg: Array in [[lb, Vector2(x0, 0)], [Vector2(x1, 0), rb],
			[Vector2(-WALL_X, front), lb], [rb, Vector2(WALL_X, front)],
			[Vector2(x0, 0), Vector2(x0, deep)], [Vector2(x1, deep), Vector2(x1, 0)],
			[Vector2(x0, deep), Vector2(x1, deep)]]:
		_wall_collider(body, seg[0], seg[1])
	for spec: Array in FLOOR_BLOCKERS:
		var c: Vector2 = spec[0]
		var sz: Vector2 = spec[1]
		_box(body, Vector3(c.x, 1.0, c.y), Vector3(sz.x, 2.0, sz.y))
	# Behind the south exit, so walking through it never steps off the floor.
	_wall_collider(body, Vector2(-WALL_X, FRONT_Z + 1.2), Vector2(WALL_X, FRONT_Z + 1.2))


func _build_markers() -> void:
	var x0: float = ARCH["x0"]
	var x1: float = ARCH["x1"]
	_exit("exit_south_to_hall", SOUTH_EXIT_TARGET, "from_mirror_corridor",
		Vector3(0, 1.0, FRONT_Z + 0.4), Vector3(WALL_X * 2.0, 2.0, 0.8))
	_exit("exit_north_arch", NORTH_EXIT_TARGET, "from_mirror_corridor",
		Vector3((x0 + x1) * 0.5, 1.0, -0.6), Vector3(x1 - x0, 2.0, 0.8))
	if SceneRouter.scene_path(NORTH_EXIT_TARGET).is_empty():
		# Until the north wing screen exists, a stop just behind the trigger.
		var stop := _collision_body("arch_unbuilt_stop")
		_wall_collider(stop, Vector2(x0, -1.3), Vector2(x1, -1.3))
	_spawns(SPAWNS)
