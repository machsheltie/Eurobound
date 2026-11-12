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
const MAINTENANCE_TARGET := "absinthe_arcade_maintenance_closet"
const TAPROOM_TARGET := "absinthe_arcade_taproom"
## The Taproom curtain (design: absinthium_taproom_curtain; round v34 follow_design): the vapour
## behind the cracked cabinet gives it away between 20:00 and 04:00. The first look in those hours
## discovers it and goes through; once discovered it opens any time (the Taproom does its own
## opener checks inside).
const TAPROOM_FLAG := "absinthium_taproom_entrance_discovered"
const TAPROOM_HOURS := Vector2i(20, 4)
## "I wanna shoop baby..." (author, round v34), the clip the author supplies; silent until it exists.
const SHOOP_CLIP := "res://assets/audio/arcade/shoop_unlock.ogg"

## Interaction anchors [anchor (x, z), where the bro stands] in tiles, from v5's painting: the
## cracked DDR's pads (front corner px ~1980-2380 x 1140-1280) and the MAINTENANCE ONLY door on the
## right wall (base px ~2500 x 1380).
const INTERACT_POINTS := {
	"broken_ddr": [Vector2(4.3, 13.4), Vector2(3.4, 14.4)],
	"maintenance_door": [Vector2(7.6, 15.2), Vector2(6.6, 15.2)],
	# The green curtain in the left-wall arch, half behind the cracked Time Crisis cabinet: the bros
	# stand just east of the cabinet, facing the curtain (base px ~300-360 x 1060-1100).
	"taproom_curtain": [Vector2(-7.2, 10.8), Vector2(-6.3, 11.0)],
}

var overlay: ArcadeOverlay
var _player: PlayerController
var _door_light: OmniLight3D
var _shoop: AudioStreamPlayer

const SPAWNS := {
	"from_mirror_corridor": [Vector2(0.0, 14.6), "north"],
	"from_maintenance_closet": [Vector2(6.6, 15.2), "west"],
	"from_taproom": [Vector2(-6.3, 11.0), "east"],
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
	# Mist leaks from the base of the cracked Time Crisis cabinet (the curtain-side cabinet).
	fx_mist_points = [Vector3(-7.7, 0, 9.6)]
	# Soft floor glow over the open aisle, on the painted diamond checker (a tile = one diamond's side,
	# the squares turned 45 deg to the room), and sparks/glitches on a few cabinet screens.
	fx_floor_rect = Rect2(-4.4, 1.8, 8.4, 14.6)
	fx_tile_size = 1.0
	fx_grid_rot_deg = 45.0
	fx_screen_points = [Vector3(-2.4, 2.3, 1.6), Vector3(0.6, 2.3, 1.6), Vector3(2.8, 2.3, 1.6),
		Vector3(-5.6, 2.3, 4.5), Vector3(5.2, 2.3, 5.0)]


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
	overlay = ArcadeOverlay.new()
	overlay.name = "overlay"
	add_child(overlay)
	overlay.flash_finished.connect(_release_player)
	_player = get_tree().get_nodes_in_group("player").filter(func(n): return is_ancestor_of(n)).front()
	if _player != null:
		_player.interacted.connect(_on_interacted)
	_door_light = OmniLight3D.new()
	_door_light.name = "maintenance_indicator"
	_door_light.light_color = Color(0.3, 1.0, 0.35)
	_door_light.light_energy = 2.0
	_door_light.omni_range = 2.0
	_door_light.position = Vector3(7.5, 4.6, 14.6)
	_diorama.add_child(_door_light)
	_shoop = AudioStreamPlayer.new()
	_shoop.name = "shoop"
	add_child(_shoop)
	_update_door()


func _on_interacted(id: String) -> void:
	match id:
		"broken_ddr":
			feed_token()
		"taproom_curtain":
			if taproom_open(GameState):
				GameState.flags[TAPROOM_FLAG] = true
				_player.input_locked = true
				SceneRouter.travel(get_tree(), TAPROOM_TARGET, "from_north_wing")
		"maintenance_door":
			_player.input_locked = true
			if BrokenDdr.unlocked(GameState):
				# The Claw Machine Maintenance Closet Restroom screen waits on its art (ad, round v34).
				if not SceneRouter.travel(get_tree(), MAINTENANCE_TARGET, "from_north_wing"):
					_release_player()
			else:
				overlay.flash("LOCKED")


## One token into the hacked DDR (round v34 nw_broken_ddr = follow_design): three unlock the
## MAINTENANCE door for good, to the bars of "Shoop".
func feed_token() -> void:
	_player.input_locked = true
	var r := BrokenDdr.feed(GameState)
	if r == "broke":
		overlay.flash("INSUFFICIENT CREDITS")
		return
	if r == "done":
		_release_player()
		return
	var fed := BrokenDdr.fed(GameState)
	# Three token pips filling green (design: three_token_pips_fill_green).
	overlay.flash(" ".join(range(BrokenDdr.TOKENS).map(func(i: int) -> String: return "●" if i < fed else "○")),
		Color(0.35, 1.0, 0.4))
	if r == "unlocked":
		_update_door()
		if ResourceLoader.exists(SHOOP_CLIP):
			_shoop.stream = load(SHOOP_CLIP)
			_shoop.play()


static func taproom_open(state) -> bool:
	return bool(state.flags.get(TAPROOM_FLAG, false)) 		or GameClock.in_hours(GameClock.hour(state), TAPROOM_HOURS.x, TAPROOM_HOURS.y)


func _update_door() -> void:
	if _door_light != null:
		_door_light.visible = BrokenDdr.unlocked(GameState)


func _release_player() -> void:
	if _player != null:
		_player.input_locked = false
