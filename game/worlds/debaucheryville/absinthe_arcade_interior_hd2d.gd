@tool
extends Node3D
## HD-2D Absinthe Arcade main hall, built by projecting the approved hall painting (v8) from the
## camera it was painted from onto a graybox of the room. PROTOTYPE for the author's build-method
## ruling (decisions page, int_build_method, option A). Tick "Night" in the Inspector or press N.
##
## How it works:
## - The paint camera was measured from v8's checkerboard floor (tile width grows linearly toward
##   the bottom of the image, which fixes the horizon and focal length) and from the painted
##   furniture for scale. See PAINT_* below.
## - The room (floor, back wall, splayed side walls) and simple prisms for the bar, doors and claw
##   alcove are built in "painting units" inside `diorama`, scaled by WORLD_SCALE so the world is in
##   real metres (characters 1.8 m), as on the exterior.
## - Every surface uses hd2d_projected_paint.gdshader, so from the gameplay camera (which IS the
##   paint camera) the room shows v8 unchanged. The depth-layer cutouts
##   (assets/.../interior/depth_layers, cut by tools/content_generation/absinthe_arcade/hd2d/
##   cut_interior_layers.py) sit on the prisms, so the bros pass behind the bar and doors.
## - The camera is fixed for the whole room (the painting fits one screen), Bravely Default style.

const HALL_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/hall/"
const LAYER_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/depth_layers/"
const PAINT_SHADER := preload("res://worlds/debaucheryville/hd2d_projected_paint.gdshader")

## Paint camera, measured from aa_interior_hall_v8 (2752x1536): focal length in pixels, downward
## pitch, and height above the floor in painting units. Painting units are metres at the scale of
## the painted patrons; the painted furniture is larger than that (the bar counter measures ~1.7 m,
## the foosball table ~1.3 m), so WORLD_SCALE shrinks the room until the furniture is real-sized.
const PAINT_IMAGE_PX := Vector2(2752, 1536)
const PAINT_FOCAL_PX := 4150.0
const PAINT_PITCH_DEG := 29.0
const PAINT_CAM_HEIGHT := 14.1
## Distance (painting units) from the camera to the hall's centre line; puts the origin mid-floor.
const PAINT_CAM_Z := 22.4
const WORLD_SCALE := 0.75

## Room outline on the floor, painting units, origin mid-floor, -Z toward the back wall. The
## painting's side walls splay outward toward the camera, so the graybox follows them.
const BACK_WALL_Z := -5.32
const LEFT_WALL := [Vector2(-4.69, -2.72), Vector2(-6.9, 1.16)]   # (x, z) two points on its base
const RIGHT_WALL := [Vector2(5.55, -1.76), Vector2(6.58, 1.7)]
const FRONT_Z := 6.5
const WALL_HEIGHT := 30.0

## Occluder prisms (footprint in painting units, height) carrying the depth-layer cutouts.
const OCCLUDERS := {
	"aa_int_layer_bottle_bar": {"height": 14.0, "footprint": [
		Vector2(-0.7, 0.93), Vector2(0.26, 1.7), Vector2(1.32, 2.3), Vector2(2.97, 2.35),
		Vector2(4.87, 0.93), Vector2(4.6, -1.2), Vector2(2.5, -2.2), Vector2(0.3, -2.2), Vector2(-0.5, -0.8)]},
	"aa_int_layer_entry_doors": {"height": 6.0, "footprint": [
		Vector2(-1.7, 3.6), Vector2(-0.8, 3.6), Vector2(-0.8, 6.4), Vector2(-1.7, 6.4)],
		"also": [Vector2(0.8, 3.6), Vector2(1.75, 3.6), Vector2(1.75, 6.4), Vector2(0.8, 6.4)]},
	"aa_int_layer_claw_alcove": {"height": 9.0, "footprint": [
		Vector2(6.0, 1.9), Vector2(6.8, 2.2), Vector2(7.4, 4.4), Vector2(6.5, 4.2)]},
}

@export var night: bool = true:
	set(value):
		night = value
		if is_inside_tree() and _env != null:
			_apply_time_of_day()

var _diorama: Node3D
var _camera: Camera3D
var _env: WorldEnvironment
var _materials: Array[ShaderMaterial] = []
var _layers: Dictionary = {}
var _night_lights: Array[Light3D] = []
var _fill: DirectionalLight3D


func _ready() -> void:
	for child in get_children():
		if child.owner == null:
			child.free()
	_materials.clear()
	_night_lights.clear()
	_diorama = Node3D.new()
	_diorama.name = "diorama"
	_diorama.scale = Vector3.ONE * WORLD_SCALE
	add_child(_diorama)
	_layers = JSON.parse_string(FileAccess.get_file_as_string(LAYER_DIR + "layers.json"))["layers"]
	_build_camera()
	_build_room()
	_build_occluders()
	_build_lighting()
	_apply_time_of_day()


func _unhandled_input(event: InputEvent) -> void:
	if Engine.is_editor_hint():
		return
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_N:
		night = not night


## The gameplay camera is the paint camera, in real metres.
func _build_camera() -> void:
	_camera = Camera3D.new()
	_camera.name = "hd2d_camera"
	_camera.keep_aspect = Camera3D.KEEP_HEIGHT
	_camera.fov = rad_to_deg(2.0 * atan(PAINT_IMAGE_PX.y * 0.5 / PAINT_FOCAL_PX))
	_camera.position = Vector3(0, PAINT_CAM_HEIGHT, PAINT_CAM_Z) * WORLD_SCALE
	_camera.rotation_degrees = Vector3(-PAINT_PITCH_DEG, 0, 0)
	_camera.near = 0.5
	_camera.far = 80.0
	add_child(_camera)
	_camera.make_current()


func _paint_material(layer_id := "") -> ShaderMaterial:
	var mat := ShaderMaterial.new()
	mat.shader = PAINT_SHADER
	mat.set_shader_parameter("paint_view", Projection(_camera.global_transform.affine_inverse()))
	mat.set_shader_parameter("focal_px", PAINT_FOCAL_PX)
	mat.set_shader_parameter("image_px", PAINT_IMAGE_PX)
	if layer_id != "":
		var r: Array = _layers[layer_id]["rect_px"]
		mat.set_shader_parameter("rect_px", Vector4(r[0], r[1], r[2], r[3]))
		mat.set_shader_parameter("use_alpha", true)
	mat.set_meta("layer_id", layer_id)
	_materials.append(mat)
	return mat


## A vertical quad on the floor line a -> b (painting units), `height` tall.
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


## Where the line through two floor points crosses z = `z`.
func _x_at(line: Array, z: float) -> float:
	var a: Vector2 = line[0]
	var b: Vector2 = line[1]
	return a.x + (b.x - a.x) * (z - a.y) / (b.y - a.y)


func _build_room() -> void:
	var mat := _paint_material()
	var lb := Vector2(_x_at(LEFT_WALL, BACK_WALL_Z), BACK_WALL_Z)
	var rb := Vector2(_x_at(RIGHT_WALL, BACK_WALL_Z), BACK_WALL_Z)
	var lf := Vector2(_x_at(LEFT_WALL, FRONT_Z), FRONT_Z)
	var rf := Vector2(_x_at(RIGHT_WALL, FRONT_Z), FRONT_Z)
	_wall("back_wall", lb, rb, WALL_HEIGHT, mat)
	_wall("left_wall", lf, lb, WALL_HEIGHT, mat)
	_wall("right_wall", rb, rf, WALL_HEIGHT, mat)
	var floor_mesh := PlaneMesh.new()
	floor_mesh.size = Vector2(24, FRONT_Z - BACK_WALL_Z + 2.0)
	var floor_mi := MeshInstance3D.new()
	floor_mi.name = "floor"
	floor_mi.mesh = floor_mesh
	floor_mi.position = Vector3(0, 0, (FRONT_Z + BACK_WALL_Z) * 0.5)
	floor_mi.material_override = mat
	_diorama.add_child(floor_mi)

	# Collision in real metres: floor and the three walls.
	var body := StaticBody3D.new()
	body.name = "room_collision"
	_diorama.add_child(body)
	var fs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(24, 0.2, FRONT_Z - BACK_WALL_Z + 2.0)
	fs.shape = box
	fs.position = Vector3(0, -0.1, (FRONT_Z + BACK_WALL_Z) * 0.5)
	body.add_child(fs)
	for seg: Array in [[lb, rb], [lf, lb], [rb, rf]]:
		_wall_collider(body, seg[0], seg[1])


func _wall_collider(body: StaticBody3D, a: Vector2, b: Vector2) -> void:
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(a.distance_to(b), 4.0, 0.3)
	cs.shape = box
	var mid := (a + b) * 0.5
	cs.position = Vector3(mid.x, 2.0, mid.y)
	cs.rotation.y = -atan2(b.y - a.y, b.x - a.x)
	body.add_child(cs)


## A closed prism over `footprint`, wearing the layer cutout, plus a matching collider.
func _prism(layer_id: String, footprint: Array, height: float) -> void:
	var st := SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)
	var n := footprint.size()
	for i in n:
		var a: Vector2 = footprint[i]
		var b: Vector2 = footprint[(i + 1) % n]
		var q := [Vector3(a.x, 0, a.y), Vector3(b.x, 0, b.y), Vector3(b.x, height, b.y), Vector3(a.x, height, a.y)]
		for k in [0, 1, 2, 0, 2, 3]:
			st.add_vertex(q[k])
	for i in range(1, n - 1):  # lid (convex footprints)
		for v: Vector2 in [footprint[0], footprint[i], footprint[i + 1]]:
			st.add_vertex(Vector3(v.x, height, v.y))
	st.generate_normals()
	var mi := MeshInstance3D.new()
	mi.name = layer_id
	mi.mesh = st.commit()
	mi.material_override = _paint_material(layer_id)
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	_diorama.add_child(mi)
	var body := StaticBody3D.new()
	body.name = layer_id + "_collision"
	var cs := CollisionShape3D.new()
	var shape := ConvexPolygonShape3D.new()
	var pts := PackedVector3Array()
	for v: Vector2 in footprint:
		pts.append(Vector3(v.x, 0, v.y))
		pts.append(Vector3(v.x, 2.5, v.y))
	shape.points = pts
	cs.shape = shape
	body.add_child(cs)
	_diorama.add_child(body)


func _build_occluders() -> void:
	for layer_id: String in OCCLUDERS.keys():
		var spec: Dictionary = OCCLUDERS[layer_id]
		_prism(layer_id, spec["footprint"], spec["height"])
		if spec.has("also"):
			_prism(layer_id, spec["also"], spec["height"])


## Practical lights, real metres: they light the bros (the painting is unshaded and already lit).
## [position (painting units), colour, energy, range (real m), night only]
const LIGHTS := [
	[Vector3(2.0, 3.0, 0.2), Color(0.55, 1.0, 0.35), 2.2, 5.0, true],    # green bottle bar
	[Vector3(-4.0, 2.5, -1.0), Color(0.75, 0.4, 1.0), 1.4, 3.5, true],   # DDR wall screen
	[Vector3(-5.5, 3.5, 2.0), Color(1.0, 0.72, 0.42), 1.6, 4.0, false],  # token machine lamp
	[Vector3(5.8, 4.0, 2.2), Color(1.0, 0.75, 0.45), 1.4, 4.0, false],   # PRIZES arch sconce
	[Vector3(0.0, 2.5, 5.0), Color(0.9, 0.7, 1.0), 0.9, 4.0, true],      # stained-glass doors
]


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
	for spec: Array in LIGHTS:
		var l := OmniLight3D.new()
		l.position = (spec[0] as Vector3) * WORLD_SCALE
		l.light_color = spec[1]
		l.light_energy = spec[2]
		l.omni_range = spec[3]
		l.omni_attenuation = 1.3
		l.set_meta("night_only", spec[4])
		add_child(l)
		_night_lights.append(l)


func _apply_time_of_day() -> void:
	var tag := "night" if night else "day"
	for mat in _materials:
		var lid: String = mat.get_meta("layer_id")
		var base := HALL_DIR + "aa_int_hall_%s.png" if lid == "" else LAYER_DIR + lid + "_%s.png"
		mat.set_shader_parameter("albedo_tex", load(base % tag))
		var has_emit := lid == "" or bool(_layers[lid]["emit"])
		mat.set_shader_parameter("use_emission", night and has_emit)
		if night and has_emit:
			mat.set_shader_parameter("emit_tex", load(base % "emit"))
	for l in _night_lights:
		l.visible = night or not l.get_meta("night_only")
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


## For QA captures: the fixed gameplay camera.
func get_camera() -> Camera3D:
	return _camera
