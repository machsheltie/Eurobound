@tool
class_name HD2DProjectedRoom
extends Node3D
## Base for a one-screen HD-2D room built from a single painting (night + day, pixel-registered,
## plus a night emission map): the painting is projected from the camera it was painted from onto a
## graybox, so from the fixed gameplay camera the room shows the painting unchanged while the bros
## walk on real geometry. A room subclass sets the paint camera in _init and builds its geometry in
## _build_room / _build_markers with the helpers below. Positions are in painting units ("tiles")
## inside `diorama`, which WORLD_SCALE turns into real metres. Press N (or tick Night) for day/night.

const PAINT_SHADER := preload("res://worlds/debaucheryville/hd2d_projected_paint.gdshader")
const PAINT_IMAGE_PX := Vector2(2752, 1536)

## Runtime only: put the player on a spawn point (off for QA captures that place their own bros).
@export var spawn_player := true

@export var night: bool = true:
	set(value):
		night = value
		if is_inside_tree() and _env != null:
			_apply_time_of_day()

# Set by the subclass in _init.
var plate_prefix := ""  ## e.g. "res://.../aa_int_corridor_" + "night.png"
var focal_px := 4150.0
var pitch_deg := 29.0
var cam_height := 14.0
var cam_z := 20.0
var world_scale := 1.0
var default_spawn := ""

var _diorama: Node3D
var _camera: Camera3D
var _env: WorldEnvironment
var _fill: DirectionalLight3D
var _fx: ArcadeAmbientFx
var fx_mist_points: Array[Vector3] = []  ## floor spots of leaking cabinet bases; empty = no ambient fx
var _materials: Array[ShaderMaterial] = []


func _ready() -> void:
	for child in get_children():
		if child.owner == null:
			child.free()
	_materials.clear()
	_diorama = Node3D.new()
	_diorama.name = "diorama"
	_diorama.scale = Vector3.ONE * world_scale
	add_child(_diorama)
	_build_camera()
	_build_room()
	_build_markers()
	_build_lighting()
	_apply_time_of_day()
	if not Engine.is_editor_hint() and not fx_mist_points.is_empty():
		_fx = ArcadeAmbientFx.new()
		_fx.name = "ambient_fx"
		_diorama.add_child(_fx)
		_fx.setup(GameState, _materials, fx_mist_points)
		_fx.night = night
		_fx.apply()
	if not Engine.is_editor_hint() and spawn_player:
		SceneRouter.ensure_game_started(get_tree())
		night = GameClock.night_for_screen(GameState, night)
		SceneRouter.spawn_player(self, default_spawn)
		SceneRouter.wire_exits(self)


## Virtual hook: each room overrides this to build its floors, walls and props.
## Called once from _ready after the camera is built. The base room builds nothing.
func _build_room() -> void:
	pass


## Virtual hook: each room overrides this to place its spawn, exit and interaction markers.
## Called from _ready right after _build_room. The base room places none.
func _build_markers() -> void:
	pass


func _unhandled_input(event: InputEvent) -> void:
	if Engine.is_editor_hint():
		return
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_N:
		night = not night


## For QA captures: the fixed gameplay camera.
func get_camera() -> Camera3D:
	return _camera


func _build_camera() -> void:
	_camera = Camera3D.new()
	_camera.name = "hd2d_camera"
	_camera.keep_aspect = Camera3D.KEEP_HEIGHT
	_camera.fov = rad_to_deg(2.0 * atan(PAINT_IMAGE_PX.y * 0.5 / focal_px))
	_camera.position = Vector3(0, cam_height, cam_z) * world_scale
	_camera.rotation_degrees = Vector3(-pitch_deg, 0, 0)
	_camera.near = 0.3
	_camera.far = 80.0
	add_child(_camera)
	_camera.make_current()


func _paint_material() -> ShaderMaterial:
	var mat := ShaderMaterial.new()
	mat.shader = PAINT_SHADER
	mat.set_shader_parameter("paint_view", Projection(_camera.global_transform.affine_inverse()))
	mat.set_shader_parameter("focal_px", focal_px)
	mat.set_shader_parameter("image_px", PAINT_IMAGE_PX)
	_materials.append(mat)
	return mat


## A vertical painted quad on the floor line a -> b, `height` tall.
func _wall(name_: String, a: Vector2, b: Vector2, height: float, mat: Material) -> MeshInstance3D:
	var st := SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)
	var p := [Vector3(a.x, 0, a.y), Vector3(b.x, 0, b.y), Vector3(b.x, height, b.y), Vector3(a.x, height, a.y)]
	for i in [0, 1, 2, 0, 2, 3]:
		st.add_vertex(p[i])
	st.generate_normals()
	var mi := MeshInstance3D.new()
	mi.name = name_
	mi.mesh = st.commit()
	mi.material_override = mat
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	_diorama.add_child(mi)
	return mi


## A painted floor rectangle.
func _floor(name_: String, center: Vector2, size: Vector2, mat: Material) -> void:
	var pm := PlaneMesh.new()
	pm.size = size
	var mi := MeshInstance3D.new()
	mi.name = name_
	mi.mesh = pm
	mi.position = Vector3(center.x, 0, center.y)
	mi.material_override = mat
	_diorama.add_child(mi)


func _collision_body(name_: String) -> StaticBody3D:
	var body := StaticBody3D.new()
	body.name = name_
	_diorama.add_child(body)
	return body


func _box(body: StaticBody3D, pos: Vector3, size: Vector3) -> void:
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = size
	cs.shape = box
	cs.position = pos
	body.add_child(cs)


## A 2 m-tall blocker over a convex floor footprint (points (x, z)).
func _footprint(body: StaticBody3D, points: Array) -> void:
	var pts := PackedVector3Array()
	for p: Vector2 in points:
		pts.append(Vector3(p.x, 0, p.y))
		pts.append(Vector3(p.x, 2.0, p.y))
	var shape := ConvexPolygonShape3D.new()
	shape.points = pts
	var cs := CollisionShape3D.new()
	cs.shape = shape
	body.add_child(cs)


func _wall_collider(body: StaticBody3D, a: Vector2, b: Vector2) -> void:
	var mid := (a + b) * 0.5
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(a.distance_to(b), 4.0, 0.3)
	cs.shape = box
	cs.position = Vector3(mid.x, 2.0, mid.y)
	cs.rotation.y = -atan2(b.y - a.y, b.x - a.x)
	body.add_child(cs)


## A scene exit (group scene_exits) the player walks into.
func _exit(name_: String, target: String, spawn: String, center: Vector3, size: Vector3) -> Area3D:
	var area := Area3D.new()
	area.name = name_
	area.add_to_group("scene_exits")
	area.set_meta("target_scene", target)
	area.set_meta("target_spawn", spawn)
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = size
	cs.shape = box
	cs.position = center
	area.add_child(cs)
	_diorama.add_child(area)
	return area


func _spawns(spawns: Dictionary) -> void:
	for sid: String in spawns.keys():
		var sp: Vector2 = spawns[sid][0]
		SceneRouter.add_spawn_point(_diorama, sid, Vector3(sp.x, 0, sp.y), spawns[sid][1])


func _build_lighting() -> void:
	_env = WorldEnvironment.new()
	var env := Environment.new()
	env.background_mode = Environment.BG_COLOR
	env.background_color = Color.BLACK
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.tonemap_mode = Environment.TONE_MAPPER_LINEAR
	env.glow_enabled = true
	env.glow_blend_mode = Environment.GLOW_BLEND_MODE_ADDITIVE
	env.glow_hdr_threshold = 1.0
	env.set_glow_level(1, 0.0)
	env.set_glow_level(3, 1.0)
	env.set_glow_level(4, 0.8)
	env.set_glow_level(5, 0.4)
	_env.environment = env
	add_child(_env)
	_fill = DirectionalLight3D.new()
	_fill.name = "fill"
	_fill.rotation_degrees = Vector3(-50, 20, 0)
	_fill.shadow_enabled = false
	add_child(_fill)


func _apply_time_of_day() -> void:
	var tag := "night" if night else "day"
	for mat in _materials:
		mat.set_shader_parameter("albedo_tex", load(plate_prefix + tag + ".png"))
		mat.set_shader_parameter("use_emission", night)
		if night:
			mat.set_shader_parameter("emit_tex", load(plate_prefix + "emit.png"))
	var env: Environment = _env.environment
	if night:
		env.ambient_light_color = Color(0.62, 0.55, 0.72)
		env.ambient_light_energy = 0.55
		_fill.light_color = Color(0.85, 0.75, 0.95)
		_fill.light_energy = 0.25
		env.glow_intensity = 0.8
	else:
		env.ambient_light_color = Color(0.95, 0.9, 0.82)
		env.ambient_light_energy = 0.8
		_fill.light_color = Color(1.0, 0.92, 0.8)
		_fill.light_energy = 0.6
		env.glow_intensity = 0.2
	if _fx != null:
		_fx.set_night(night)
