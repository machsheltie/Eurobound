@tool
extends Node3D
## HD-2D painted-box diorama for the Absinthe Arcade exterior.
## Runs in the editor too (@tool), so the building shows in the viewport; tick "Night" in the
## Inspector to preview the night textures without running the game.
##
## Builds the building at runtime from the finalized face textures and faces.json written by
## tools/content_generation/absinthe_arcade/hd2d/finalize_faces.py, so regenerating any face only
## needs a re-run of that script. Day and night are pixel-registered texture swaps; night also turns
## on the emission maps that feed the WorldEnvironment glow.
##
## Footprint: the front faces +Z (toward the camera), 15.4 m wide, 18 m deep back toward -Z.
## Y is up, origin at the centre of the front wall base. Press N to toggle day/night.

const FACE_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/exterior/faces/"
const PROP_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/exterior/props/"
## The painted facade is drawn at ~2.4x real-world scale (its double doorway measures 7.25 m;
## a real one is ~3 m). Author ruling 2026-11-02: the WORLD is in real metres. Building and props
## are laid out in "painting units" inside the `diorama` node, which is scaled by 1/PAINT_SCALE,
## so characters, physics, speeds and the camera all use ordinary real-world metres.
const PAINT_SCALE := 2.4

## Street dressing in painting units (x across the front, y up from the pavement, z out from the
## front wall; the front corner is at x = -7.7 / +7.7). Matched to the Clocktower Plaza reference
## renders (references/Exterior/absinthearcadedaytime.png, ...Plaza(3).png):
##   left of the door, under the arched window: cabinet with the awning just above it, the bucket,
##   then the chalkboard leaning in front of the left door leaf; the TOKENS sign and its lantern on
##   the left wall right at the front corner, facing the side street; the second lantern between
##   the "13" plaque and the right downpipe; the shrub at the foot of the right door panel;
##   bollards along the curb, clear of the doorway.
## Every prop texture is ORTHOGRAPHIC (a front elevation or a pure side profile), so each is
## mounted to match its view instead of being turned toward the camera:
##   kind "card":      flat card. rot_y: 0 faces the street (+Z), -90 faces out of the left wall,
##                     90 faces out of the right wall. flip mirrors it. pos = bottom centre.
##   kind "billboard": round objects (bucket, bollard, shrub) that turn to face the camera.
##   kind "cabinet":   box: front elevation on the street face, side profile on both sides,
##                     back flush against the wall at z = back_z.
##   kind "aframe":    the chalkboard as two boards leaning together (tilt degrees).
##   kind "awning":    clear corrugated bullnose canopy (built in code, painted sheet) on two side-profile
##                     iron brackets, painted valance with bulbs on its front edge; pos = top centre at the wall.
## Front-wall items start at z 0.35 so the displaced relief (sills, pipes) never swallows them.
const PROP_LAYOUT := [
	{"id": "aa_prop_cabinet", "kind": "cabinet", "pos": Vector3(-4.95, 0.0, 0.35)},
	{"id": "aa_prop_awning", "kind": "awning", "pos": Vector3(-4.95, 5.9, 0.35)},
	{"id": "aa_prop_metal_bucket", "kind": "billboard", "pos": Vector3(-3.7, 0.0, 2.6)},
	{"id": "aa_prop_chalkboard", "kind": "aframe", "pos": Vector3(-2.3, 0.0, 2.0), "tilt": 12.0},
	{"id": "aa_prop_wall_sign_tokens", "kind": "card", "pos": Vector3(-8.05, 0.6, -1.0), "rot_y": -90.0},
	{"id": "aa_prop_wall_lantern_side", "kind": "card", "pos": Vector3(-8.55, 4.7, -1.0), "flip": true},
	{"id": "aa_prop_wall_lantern_front", "kind": "card", "pos": Vector3(6.15, 6.6, 1.0)},
	{"id": "aa_prop_potted_shrub", "kind": "billboard", "pos": Vector3(5.4, 0.0, 0.9)},
	{"id": "aa_prop_bollard", "kind": "billboard", "pos": Vector3(-7.0, 0.0, 8.0)},
	{"id": "aa_prop_bollard", "kind": "billboard", "pos": Vector3(-4.6, 0.0, 8.0)},
	{"id": "aa_prop_bollard", "kind": "billboard", "pos": Vector3(4.6, 0.0, 8.0)},
	{"id": "aa_prop_bollard", "kind": "billboard", "pos": Vector3(7.0, 0.0, 8.0)},
]
const DEPTH_M := 18.0
## Height of the flat roof deck: just under the iron cresting painted on the elevations, so the
## cresting and chimneys still read as silhouettes above the box.
const ROOF_DECK_M := 23.6

## Runtime only: put the player on a spawn point (off for QA captures that place their own bros).
@export var spawn_player := true

@export var night: bool = false:
	set(value):
		night = value
		if is_inside_tree() and _env != null:
			_apply_time_of_day()

var _faces: Dictionary = {}
var _ppm: float = 66.49
var _materials: Dictionary = {}
var _props: Dictionary = {}
var _prop_ppm: float = 400.0
var _prop_materials: Array[StandardMaterial3D] = []
var _sun: DirectionalLight3D
var _env: WorldEnvironment
var _diorama: Node3D


func _ready() -> void:
	# Generated nodes are not owned by the scene, so they are never saved into the .tscn; clear
	# any left from a previous editor reload before rebuilding.
	for child in get_children():
		if child.owner == null:
			child.free()
	_materials.clear()
	_prop_materials.clear()
	_diorama = Node3D.new()
	_diorama.name = "diorama"
	_diorama.scale = Vector3.ONE / PAINT_SCALE
	add_child(_diorama)
	_load_layout()
	_build_building()
	_build_props()
	_build_ground()
	_build_lighting()
	_build_camera()
	_build_walkable()
	_apply_time_of_day()
	if not Engine.is_editor_hint() and spawn_player:
		_player = SceneRouter.spawn_player(self, "start")
		SceneRouter.wire_exits(self)
		_camera_focus.global_position = _player.global_position + CAM_FOCUS_HEIGHT
		_pcam.global_position = _camera_focus.global_position + (_pcam.get("follow_offset") as Vector3)


func _process(_delta: float) -> void:
	if is_instance_valid(_player) and is_instance_valid(_camera_focus):
		_camera_focus.global_position = _player.global_position + CAM_FOCUS_HEIGHT


func _unhandled_input(event: InputEvent) -> void:
	if Engine.is_editor_hint():
		return
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_N:
		night = not night


func _load_layout() -> void:
	var text := FileAccess.get_file_as_string(FACE_DIR + "faces.json")
	var data: Dictionary = JSON.parse_string(text)
	_ppm = float(data["ppm"])
	_faces = data["faces"]
	if FileAccess.file_exists(PROP_DIR + "props.json"):
		var pdata: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(PROP_DIR + "props.json"))
		_prop_ppm = float(pdata["ppm"])
		_props = pdata["props"]


func _build_props() -> void:
	var holder := Node3D.new()
	holder.name = "street_props"
	_diorama.add_child(holder)
	for entry: Dictionary in PROP_LAYOUT:
		var kind: String = entry.get("kind", "card")
		var node := Node3D.new()
		node.name = entry["id"]
		node.position = entry["pos"]
		holder.add_child(node)
		match kind:
			"card":
				var card := _prop_card(entry["id"], entry.get("flip", false), false)
				if card:
					card.rotation_degrees.y = float(entry.get("rot_y", 0.0))
					node.add_child(card)
			"billboard":
				var bb := _prop_card(entry["id"], false, true)
				if bb:
					node.add_child(bb)
			"cabinet":
				_build_cabinet(node)
			"aframe":
				_build_aframe(node, entry["id"], float(entry.get("tilt", 12.0)))
			"awning":
				_build_awning(node, entry["id"], float(entry.get("depth", 2.5)))


## Size of a prop texture in painting units.
func _prop_size(pid: String) -> Vector2:
	var px: Array = _props[pid]["texture_px"]
	return Vector2(float(px[0]), float(px[1])) / _prop_ppm * PAINT_SCALE


## A flat textured quad, pivot at its bottom centre, facing +Z (texture left -> right = -X -> +X).
func _prop_card(pid: String, flip: bool, billboard: bool, size_override := Vector2.ZERO) -> MeshInstance3D:
	if not _props.has(pid):
		return null
	var size := _prop_size(pid) if size_override == Vector2.ZERO else size_override
	var quad := QuadMesh.new()
	quad.size = size
	quad.center_offset = Vector3(0, size.y * 0.5, 0)
	var mat := StandardMaterial3D.new()
	mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA_SCISSOR
	mat.alpha_scissor_threshold = 0.5
	mat.cull_mode = BaseMaterial3D.CULL_DISABLED
	mat.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	mat.roughness = 1.0
	if billboard:
		mat.billboard_mode = BaseMaterial3D.BILLBOARD_FIXED_Y
		mat.billboard_keep_scale = true
	if flip:
		mat.uv1_scale = Vector3(-1, 1, 1)
		mat.uv1_offset = Vector3(1, 0, 0)
	mat.set_meta("prop_id", pid)
	_prop_materials.append(mat)
	var mi := MeshInstance3D.new()
	mi.name = pid
	mi.mesh = quad
	mi.material_override = mat
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_ON
	return mi


## Real depth of the street cabinet (a classic upright is ~0.8 m front to back).
const CABINET_DEPTH_REAL_M := 0.8


## Arcade cabinet as a box: the node sits at the wall (back face), cabinet extends toward +Z.
## The side profile is painted with the cabinet FRONT on the image's RIGHT; it is squeezed to the
## real depth so the cabinet does not stick out into the street.
func _build_cabinet(node: Node3D) -> void:
	if not (_props.has("aa_prop_cabinet_front") and _props.has("aa_prop_cabinet_side")):
		return
	var front := _prop_size("aa_prop_cabinet_front")
	var side := _prop_size("aa_prop_cabinet_side")
	var depth := CABINET_DEPTH_REAL_M * PAINT_SCALE
	var side_size := Vector2(depth, side.y)
	var half_w := front.x * 0.5
	var f := _prop_card("aa_prop_cabinet_front", false, false)
	f.position = Vector3(0, 0, depth)
	node.add_child(f)
	# Card rotated -90 faces -X and maps texture-right to +Z (the street): no flip on the left side.
	# Card rotated +90 faces +X and maps texture-right to -Z (the wall): flip on the right side.
	var l := _prop_card("aa_prop_cabinet_side", false, false, side_size)
	l.rotation_degrees.y = -90.0
	l.position = Vector3(-half_w, 0, depth * 0.5)
	node.add_child(l)
	var r := _prop_card("aa_prop_cabinet_side", true, false, side_size)
	r.rotation_degrees.y = 90.0
	r.position = Vector3(half_w, 0, depth * 0.5)
	node.add_child(r)
	# Dark body behind the cards so nothing shows through the profile's notches.
	var body := MeshInstance3D.new()
	var box := BoxMesh.new()
	box.size = Vector3(front.x * 0.96, front.y * 0.9, depth * 0.5)
	body.mesh = box
	body.position = Vector3(0, front.y * 0.45, depth * 0.27)
	var dark := StandardMaterial3D.new()
	dark.albedo_color = Color(0.05, 0.05, 0.06)
	body.material_override = dark
	node.add_child(body)


## A-frame chalkboard: front board leans back by `tilt`, a back board leans the other way.
func _build_aframe(node: Node3D, pid: String, tilt: float) -> void:
	var front := _prop_card(pid, false, false)
	if not front:
		return
	front.rotation_degrees.x = -tilt
	node.add_child(front)
	var back := _prop_card(pid, true, false)
	back.rotation_degrees = Vector3(-tilt, 180.0, 0)
	var h := _prop_size(pid).y
	back.position = Vector3(0, 0, -2.0 * h * sin(deg_to_rad(tilt)))
	node.add_child(back)


## Awning dimensions in real metres, matched to references/Exterior/absinthearcadedaytime.png: a short
## clear corrugated bullnose canopy only a little wider than the cabinet under it, its drip edge
## just above the cabinet top, held on two scrolled iron brackets.
const AWNING_WIDTH_REAL_M := 0.95
const AWNING_REACH_REAL_M := 0.62
const AWNING_DROP_REAL_M := 0.42
const AWNING_RIBS := 7
## Regions of aa_prop_awning_*.png (a front elevation): the canopy sheet without the painted
## side brackets, and the bottom strip (drip rail, fringe and bulbs) used as the hanging valance.
const AWNING_SHEET_UV := Rect2(0.1, 0.0, 0.8, 0.79)
const AWNING_VALANCE_V := 0.77

func _iron_material() -> StandardMaterial3D:
	var iron := StandardMaterial3D.new()
	iron.albedo_color = Color(0.06, 0.06, 0.07)
	iron.roughness = 0.45
	iron.metallic = 0.6
	return iron


## A round iron tube from a to b (node-local).
func _tube(parent: Node3D, a: Vector3, b: Vector3, radius: float, mat: Material) -> void:
	var mi := MeshInstance3D.new()
	var cyl := CylinderMesh.new()
	cyl.top_radius = radius
	cyl.bottom_radius = radius
	cyl.height = a.distance_to(b)
	cyl.radial_segments = 8
	mi.mesh = cyl
	mi.material_override = mat
	var up := (b - a).normalized()
	var side := up.cross(Vector3.FORWARD if absf(up.z) < 0.9 else Vector3.RIGHT).normalized()
	mi.basis = Basis(side, up, side.cross(up))
	mi.position = (a + b) * 0.5
	parent.add_child(mi)


func _awning_profile(t: float, reach: float, drop: float) -> Vector2:
	# t 0..1 from the wall to the drip edge: level at the wall, curling down to the front (bullnose).
	var a := t * PI * 0.5
	return Vector2(reach * sin(a), -drop * (1.0 - cos(a)))  # (z, y)


## Clear corrugated canopy textured with the painted awning sheet, an iron frame (wall rail, curved
## end ribs, drip rail), the painted fringe-and-bulbs valance hanging off the front, and the two
## side-profile iron brackets underneath. All painted parts swap day/night like the other props.
func _build_awning(node: Node3D, pid: String, _unused := 0.0) -> void:
	var w := AWNING_WIDTH_REAL_M * PAINT_SCALE
	var reach := AWNING_REACH_REAL_M * PAINT_SCALE
	var drop := AWNING_DROP_REAL_M * PAINT_SCALE
	var seg_x := AWNING_RIBS * 8
	var seg_a := 16
	var rib := w / float(AWNING_RIBS)
	var rib_depth := 0.022 * PAINT_SCALE
	# Arc length along the profile, so the painted sheet is not stretched where it curls.
	var arc: Array[float] = [0.0]
	for j in range(1, seg_a + 1):
		var p0 := _awning_profile(float(j - 1) / seg_a, reach, drop)
		var p1 := _awning_profile(float(j) / seg_a, reach, drop)
		arc.append(arc[j - 1] + p0.distance_to(p1))
	var st := SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)
	for j in seg_a + 1:
		var t := float(j) / seg_a
		var p := _awning_profile(t, reach, drop)
		var a := t * PI * 0.5
		var n := Vector3(0, cos(a) * drop / maxf(drop, 0.001), sin(a)).normalized()
		for i in seg_x + 1:
			var x := -w * 0.5 + w * float(i) / seg_x
			# Rounded corrugation: ribs run from the wall to the drip edge.
			var c := 0.5 + 0.5 * cos(TAU * (x + w * 0.5) / rib)
			st.set_uv(Vector2(float(i) / seg_x, arc[j] / arc[seg_a]))
			st.add_vertex(Vector3(x, p.y, p.x) + n * c * rib_depth)
	for j in seg_a:
		for i in seg_x:
			var i0 := j * (seg_x + 1) + i
			var i1 := i0 + seg_x + 1
			st.add_index(i0)
			st.add_index(i1)
			st.add_index(i0 + 1)
			st.add_index(i0 + 1)
			st.add_index(i1)
			st.add_index(i1 + 1)
	st.generate_normals()
	var canopy := MeshInstance3D.new()
	canopy.name = "awning_canopy"
	canopy.mesh = st.commit()
	var sheet := StandardMaterial3D.new()
	sheet.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA_DEPTH_PRE_PASS
	sheet.albedo_color = Color(0.9, 0.95, 1.0, 0.42)
	sheet.cull_mode = BaseMaterial3D.CULL_DISABLED
	sheet.roughness = 0.18
	sheet.specular_mode = BaseMaterial3D.SPECULAR_SCHLICK_GGX
	sheet.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	sheet.uv1_scale = Vector3(AWNING_SHEET_UV.size.x, AWNING_SHEET_UV.size.y, 1)
	sheet.uv1_offset = Vector3(AWNING_SHEET_UV.position.x, AWNING_SHEET_UV.position.y, 0)
	sheet.set_meta("prop_id", pid)
	_prop_materials.append(sheet)
	canopy.material_override = sheet
	canopy.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_ON
	node.add_child(canopy)

	# Iron frame.
	var iron := _iron_material()
	var r := 0.018 * PAINT_SCALE
	_tube(node, Vector3(-w * 0.5, 0, 0.02), Vector3(w * 0.5, 0, 0.02), r, iron)
	var front := _awning_profile(1.0, reach, drop)
	_tube(node, Vector3(-w * 0.5, front.y, front.x), Vector3(w * 0.5, front.y, front.x), r * 1.2, iron)
	for sx: float in [-w * 0.5, w * 0.5]:
		for j in 8:
			var q0 := _awning_profile(float(j) / 8.0, reach, drop)
			var q1 := _awning_profile(float(j + 1) / 8.0, reach, drop)
			_tube(node, Vector3(sx, q0.y + r, q0.x), Vector3(sx, q1.y + r, q1.x), r, iron)

	# Painted valance (drip rail ornaments + bulb string) hanging off the front edge. The awning
	# texture has no props.json entry (it is built in code), so the card is made here.
	var tex: Texture2D = load(PROP_DIR + "%s_day.png" % pid)
	var vh := w * (1.0 - AWNING_VALANCE_V) * float(tex.get_height()) / float(tex.get_width())
	var vquad := QuadMesh.new()
	vquad.size = Vector2(w, vh)
	vquad.center_offset = Vector3(0, vh * 0.5, 0)
	var vmat := StandardMaterial3D.new()
	vmat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA_SCISSOR
	vmat.alpha_scissor_threshold = 0.5
	vmat.cull_mode = BaseMaterial3D.CULL_DISABLED
	vmat.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	vmat.roughness = 1.0
	vmat.uv1_scale = Vector3(1, 1.0 - AWNING_VALANCE_V, 1)
	vmat.uv1_offset = Vector3(0, AWNING_VALANCE_V, 0)
	vmat.set_meta("prop_id", pid)
	_prop_materials.append(vmat)
	var valance := MeshInstance3D.new()
	valance.name = "awning_valance"
	valance.mesh = vquad
	valance.material_override = vmat
	valance.position = Vector3(0, front.y - vh + r, front.x + 0.01)
	node.add_child(valance)

	# Scrolled iron brackets in side profile under each end of the canopy, arm level with the drip
	# edge. The art has the wall plate on the LEFT and the arm reaching RIGHT. Left end: card faces
	# -X, texture-right -> +Z (street), no flip. Right end: card faces +X, texture-right -> -Z, so flip.
	if _props.has("aa_prop_awning_bracket"):
		var bs := _prop_size("aa_prop_awning_bracket")
		var bsize := bs * (reach / bs.x)
		for sgn: float in [-1.0, 1.0]:
			var br := _prop_card("aa_prop_awning_bracket", sgn > 0.0, false, bsize)
			br.rotation_degrees.y = 90.0 if sgn > 0.0 else -90.0
			br.position = Vector3(sgn * (w * 0.5 - r), front.y - bsize.y + r, bsize.x * 0.5)
			node.add_child(br)


## Hanging-sign boards painted past a face's corner, in that face's texture pixels. The CLOCKTOWER
## PLAZA board overhangs the left elevation's front edge and is seen from both sides, so its back
## face mirrors the board back (see hd2d_relief_face.gdshader). Re-measure if the face is regenerated.
const SIGN_BACK_MIRROR_PX := {
	"aa_face_left": Rect2(1212, 1180, 179, 164),
}

## Pixels per subdivision on faces that have relief: ~3 px keeps sills and mouldings crisp.
const RELIEF_PX_PER_CELL := 3.0
const RELIEF_SHADER := preload("res://worlds/debaucheryville/hd2d_relief_face.gdshader")


func _has_height(face_id: String) -> bool:
	return ResourceLoader.exists(FACE_DIR + "%s_height.png" % face_id)


func _face_material(face_id: String) -> ShaderMaterial:
	var mat := ShaderMaterial.new()
	mat.shader = RELIEF_SHADER
	var relief := _has_height(face_id)
	mat.set_shader_parameter("has_height", relief)
	if relief:
		mat.set_shader_parameter("height_tex", load(FACE_DIR + "%s_height.png" % face_id))
		mat.set_shader_parameter("normal_tex", load(FACE_DIR + "%s_normal.png" % face_id))
		var f: Dictionary = _faces.get(face_id, {})
		mat.set_shader_parameter("height_range_m", float(f.get("height_range_m", 1.0)))
		if f.has("wall_left_px") and f.has("wall_right_px"):
			# Overhangs past the corners (hanging signs, gutters) are flat cut-outs in the air.
			mat.set_shader_parameter("relief_u_range", Vector2(
				float(f["wall_left_px"]) / float(f["texture_px"][0]),
				float(f["wall_right_px"]) / float(f["texture_px"][0])))
		if f.has("texture_px"):
			mat.set_shader_parameter("texture_size_m",
				Vector2(float(f["texture_px"][0]), float(f["texture_px"][1])) / _ppm)
	if SIGN_BACK_MIRROR_PX.has(face_id) and _faces.has(face_id):
		var r: Rect2 = SIGN_BACK_MIRROR_PX[face_id]
		var tex_px := Vector2(float(_faces[face_id]["texture_px"][0]), float(_faces[face_id]["texture_px"][1]))
		mat.set_shader_parameter("use_back_mirror", true)
		mat.set_shader_parameter("back_mirror_rect",
			Vector4(r.position.x / tex_px.x, r.position.y / tex_px.y, r.end.x / tex_px.x, r.end.y / tex_px.y))
	_materials[face_id] = mat
	return mat


## A vertical face quad. `wall_left_px` lines the painted wall's left edge up with `corner`.
func _add_wall(face_id: String, corner: Vector3, along: Vector3, outward: Vector3) -> void:
	var f: Dictionary = _faces[face_id]
	var tex_w: float = float(f["texture_px"][0]) / _ppm
	var tex_h: float = float(f["texture_px"][1]) / _ppm
	var wall_left_m: float = float(f["wall_left_px"]) / _ppm
	var quad := QuadMesh.new()
	quad.size = Vector2(tex_w, tex_h)
	if _has_height(face_id):
		quad.subdivide_width = int(float(f["texture_px"][0]) / RELIEF_PX_PER_CELL)
		quad.subdivide_depth = int(float(f["texture_px"][1]) / RELIEF_PX_PER_CELL)
	var mi := MeshInstance3D.new()
	mi.name = face_id
	mi.mesh = quad
	mi.material_override = _face_material(face_id)
	# Relief faces cast real shadows (sills, cornices, marquee onto the wall).
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_ON if _has_height(face_id) \
		else GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	var centre := corner + along * (tex_w * 0.5 - wall_left_m) + Vector3.UP * (tex_h * 0.5)
	mi.basis = Basis(along, Vector3.UP, outward)
	mi.position = centre + outward * 0.01
	_diorama.add_child(mi)


func _build_building() -> void:
	var w: float = float(_faces["aa_face_front"]["wall_width_m"])
	var hw := w * 0.5
	# Front wall on z = 0 facing +Z (toward the camera); the building runs back to z = -DEPTH_M.
	# Each call gives the face's left corner as a viewer standing outside it sees it, and the
	# direction of that viewer's right hand (texture left -> right).
	_add_wall("aa_face_front", Vector3(-hw, 0, 0), Vector3.RIGHT, Vector3.BACK)
	_add_wall("aa_face_right", Vector3(hw, 0, 0), Vector3.FORWARD, Vector3.RIGHT)
	_add_wall("aa_face_back", Vector3(hw, 0, -DEPTH_M), Vector3.LEFT, Vector3.FORWARD)
	_add_wall("aa_face_left", Vector3(-hw, 0, -DEPTH_M), Vector3.BACK, Vector3.LEFT)

	# Solid core so nothing shows through gaps between face cards. Inset deeper than the deepest
	# relief recess (doorway, -1 m) so recessed openings never clip into it.
	var inset := 0.5
	var core := MeshInstance3D.new()
	core.name = "aa_core"
	var box := BoxMesh.new()
	box.size = Vector3(w - inset * 2.0, ROOF_DECK_M - 0.2, DEPTH_M - inset * 2.0)
	core.mesh = box
	core.position = Vector3(0, (ROOF_DECK_M - 0.2) * 0.5, -DEPTH_M * 0.5)
	var dark := StandardMaterial3D.new()
	dark.albedo_color = Color(0.08, 0.07, 0.09)
	core.material_override = dark
	_diorama.add_child(core)

	var roof := MeshInstance3D.new()
	roof.name = "aa_roof_top"
	var plane := PlaneMesh.new()
	plane.size = Vector2(w, DEPTH_M)
	roof.mesh = plane
	# PlaneMesh UV v runs toward +Z, so the texture's bottom (front) edge lands on the front wall.
	roof.position = Vector3(0, ROOF_DECK_M, -DEPTH_M * 0.5)
	roof.material_override = _face_material("aa_roof_top")
	_diorama.add_child(roof)


func _build_ground() -> void:
	var ground := MeshInstance3D.new()
	ground.name = "ground_placeholder"
	var plane := PlaneMesh.new()
	plane.size = Vector2(30, 30)
	ground.mesh = plane
	ground.position = Vector3(0, -0.01, 0)
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.28, 0.27, 0.27)
	mat.roughness = 0.35
	ground.material_override = mat
	add_child(ground)


## Night practical lights, in REAL metres (world space, outside the scaled diorama). Painted
## emission makes the neon glow; these make it actually light the street, props and characters,
## and scatter in the night fog. [position, colour, energy, range, casts shadow]
const NIGHT_LIGHTS := [
	[Vector3(-0.55, 3.45, 1.3), Color(0.72, 0.35, 1.0), 2.2, 4.5, false],  # marquee, purple half
	[Vector3(0.55, 3.45, 1.3), Color(0.62, 1.0, 0.32), 2.0, 4.5, false],   # marquee, green half
	[Vector3(0.0, 1.7, 0.2), Color(1.0, 0.72, 0.42), 1.6, 3.8, true],      # doorway spill
	[Vector3(2.56, 3.0, 0.45), Color(1.0, 0.78, 0.48), 1.3, 3.2, false],   # front wall lantern
	[Vector3(-3.56, 2.15, -0.45), Color(1.0, 0.78, 0.48), 1.3, 3.2, false],  # side wall lantern
	[Vector3(-2.06, 1.3, 1.15), Color(1.0, 0.35, 0.85), 0.9, 1.8, false],  # street cabinet screen
	[Vector3(-2.06, 2.0, 0.55), Color(1.0, 0.8, 0.5), 0.7, 1.6, false],    # awning bulb string
]

var _night_lights: Array[OmniLight3D] = []
var _tilt_shift: CanvasLayer


func _build_lighting() -> void:
	_sun = DirectionalLight3D.new()
	_sun.name = "sun"
	# High and from the front-left so sills, cornices and the marquee throw short shadows down
	# and to the right across the facade.
	_sun.rotation_degrees = Vector3(-55, -25, 0)
	_sun.shadow_enabled = true
	_sun.light_angular_distance = 1.2  # soft penumbra (PCSS on Forward+)
	_sun.directional_shadow_max_distance = 45.0
	_sun.directional_shadow_blend_splits = true
	add_child(_sun)

	_env = WorldEnvironment.new()
	var env := Environment.new()
	env.background_mode = Environment.BG_SKY
	var sky := Sky.new()
	sky.sky_material = ProceduralSkyMaterial.new()
	env.sky = sky
	# The facades carry painted light, so the engine light stays close to neutral and the tone
	# mapper stays linear: what was painted is what shows. Filmic washed the paint out.
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.tonemap_mode = Environment.TONE_MAPPER_LINEAR
	env.tonemap_white = 1.0
	# Contact shading where props, cabinet and walls meet the street.
	env.ssao_enabled = true
	env.ssao_radius = 0.9
	env.ssao_intensity = 1.6
	env.ssao_power = 1.4
	env.ssao_detail = 0.6
	env.adjustment_enabled = true
	env.glow_enabled = true
	env.glow_blend_mode = Environment.GLOW_BLEND_MODE_ADDITIVE
	env.glow_hdr_threshold = 1.0
	env.glow_bloom = 0.0
	env.set_glow_level(1, 0.0)
	env.set_glow_level(3, 1.0)
	env.set_glow_level(4, 0.8)
	env.set_glow_level(5, 0.4)
	_env.environment = env
	add_child(_env)

	for spec: Array in NIGHT_LIGHTS:
		var l := OmniLight3D.new()
		l.position = spec[0]
		l.light_color = spec[1]
		l.light_energy = spec[2]
		l.omni_range = spec[3]
		l.omni_attenuation = 1.4
		l.shadow_enabled = spec[4]
		l.light_volumetric_fog_energy = 2.5
		add_child(l)
		_night_lights.append(l)

	if not Engine.is_editor_hint():
		_tilt_shift = preload("res://shaders/post/tilt_shift_layer.tscn").instantiate()
		add_child(_tilt_shift)


## Gameplay camera, Bravely Default / Star Ocean 2R style: a locked high angle with a narrow lens,
## nearly square-on to the painted fronts so the painted faces read as painted. A Phantom Camera
## follows `camera_focus` (the stand-in for the party leader until the player exists) at a fixed
## offset, so the angle never changes as the party walks; only the position tracks.
const CAM_PITCH_DEG := 32.0
const CAM_YAW_DEG := 8.0  # a touch from the right, so the left return and depth still read
const CAM_DISTANCE_M := 17.0
const CAM_FOV := 30.0
const CAM_FOCUS_START := Vector3(0.0, 1.9, 1.8)

var _camera: Camera3D
var _pcam: Node3D
var _camera_focus: Node3D
var _player: PlayerController
const CAM_FOCUS_HEIGHT := Vector3(0, 1.9, 0)


func _build_camera() -> void:
	_camera = Camera3D.new()
	_camera.name = "hd2d_camera"
	_camera.fov = CAM_FOV
	# Far blur only, set past the focus distance: it softens the distant backdrop like the
	# reference games without ever blurring what the camera is looking at. Near blur is wrong
	# for a high angle: the street under the camera is the subject, not foreground clutter.
	var attrs := CameraAttributesPractical.new()
	attrs.dof_blur_far_enabled = true
	attrs.dof_blur_far_distance = CAM_DISTANCE_M + 7.0
	attrs.dof_blur_far_transition = 12.0
	attrs.dof_blur_amount = 0.05
	_camera.attributes = attrs
	add_child(_camera)
	_camera.make_current()

	_camera_focus = Node3D.new()
	_camera_focus.name = "camera_focus"
	_camera_focus.position = CAM_FOCUS_START
	add_child(_camera_focus)

	var pitch := deg_to_rad(CAM_PITCH_DEG)
	var yaw := deg_to_rad(CAM_YAW_DEG)
	var offset := Vector3(sin(yaw) * cos(pitch), sin(pitch), cos(yaw) * cos(pitch)) * CAM_DISTANCE_M
	_camera.look_at_from_position(CAM_FOCUS_START + offset, CAM_FOCUS_START, Vector3.UP)
	if Engine.is_editor_hint():
		return  # the editor keeps a static camera; the follow rig is runtime only
	var host := PhantomCameraHost.new()
	host.name = "pcam_host"
	_camera.add_child(host)
	_pcam = PhantomCamera3D.new()
	_pcam.name = "pcam_gameplay"
	_pcam.priority = 10
	_pcam.follow_mode = PhantomCamera3D.FollowMode.SIMPLE
	_pcam.follow_offset = offset
	_pcam.follow_damping = true
	_pcam.tween_on_load = false  # start framed; no fly-in from the origin
	_pcam.attributes = attrs
	add_child(_pcam)
	_pcam.global_transform = _camera.global_transform
	_pcam.follow_target = _camera_focus


## Hands the camera to a caller (QA captures) and turns off the follow rig and screen tilt-shift.
func free_camera() -> Camera3D:
	if is_instance_valid(_pcam):
		_pcam.queue_free()
	if is_instance_valid(_camera) and _camera.has_node("pcam_host"):
		_camera.get_node("pcam_host").queue_free()
	if is_instance_valid(_tilt_shift):
		_tilt_shift.visible = false
	return _camera


func _apply_time_of_day() -> void:
	var tag := "night" if night else "day"
	for face_id in _materials.keys():
		var mat: ShaderMaterial = _materials[face_id]
		mat.set_shader_parameter("albedo_tex", load(FACE_DIR + "%s_%s.png" % [face_id, tag]))
		mat.set_shader_parameter("use_emission", night)
		if night:
			mat.set_shader_parameter("emission_tex", load(FACE_DIR + "%s_emit.png" % face_id))
	for pmat in _prop_materials:
		var pid: String = pmat.get_meta("prop_id")
		pmat.albedo_texture = load(PROP_DIR + "%s_%s.png" % [pid, tag])
		pmat.emission_enabled = night
		if night:
			pmat.emission_texture = load(PROP_DIR + "%s_emit.png" % pid)
			pmat.emission = Color.BLACK  # ADD operator: only the emission texture glows
			pmat.emission_operator = BaseMaterial3D.EMISSION_OP_ADD
			pmat.emission_energy_multiplier = 1.6
	for l in _night_lights:
		l.visible = night
	var env: Environment = _env.environment
	var sky_mat: ProceduralSkyMaterial = env.sky.sky_material
	if night:
		# The night textures already carry their blue moonlight; keep the engine light near
		# neutral so it is not tinted twice. A weak moon still rakes the relief.
		sky_mat.sky_top_color = Color(0.01, 0.015, 0.05)
		sky_mat.sky_horizon_color = Color(0.06, 0.06, 0.16)
		sky_mat.ground_horizon_color = Color(0.06, 0.06, 0.16)
		sky_mat.ground_bottom_color = Color(0.01, 0.01, 0.03)
		sky_mat.sun_angle_max = 0.0
		env.ambient_light_color = Color(0.9, 0.92, 1.0)
		env.ambient_light_energy = 0.8
		_sun.light_color = Color(0.7, 0.78, 1.0)
		_sun.light_energy = 0.3
		env.glow_intensity = 0.9
		env.fog_enabled = false
		# Thin street haze that the neon and lanterns scatter in.
		env.volumetric_fog_enabled = true
		env.volumetric_fog_density = 0.018
		env.volumetric_fog_albedo = Color(0.55, 0.55, 0.7)
		env.volumetric_fog_length = 40.0
		env.volumetric_fog_ambient_inject = 0.0
		env.adjustment_saturation = 1.1
		env.adjustment_contrast = 1.05
	else:
		sky_mat.sky_top_color = Color(0.36, 0.55, 0.82)
		sky_mat.sky_horizon_color = Color(0.82, 0.84, 0.86)
		sky_mat.ground_horizon_color = Color(0.82, 0.84, 0.86)
		sky_mat.ground_bottom_color = Color(0.35, 0.33, 0.32)
		sky_mat.sun_angle_max = 30.0
		# Warm key, slightly cool fill: the paint supplies the detail, this supplies the time of day.
		env.ambient_light_color = Color(0.93, 0.95, 1.0)
		env.ambient_light_energy = 0.55
		_sun.light_color = Color(1.0, 0.94, 0.82)
		_sun.light_energy = 0.95
		env.glow_intensity = 0.25
		env.volumetric_fog_enabled = false
		# Faint aerial perspective so the backdrop sits behind the building.
		env.fog_enabled = true
		env.fog_light_color = Color(0.8, 0.84, 0.9)
		env.fog_density = 0.004
		env.fog_aerial_perspective = 0.5
		env.fog_sky_affect = 0.0
		env.adjustment_saturation = 1.06
		env.adjustment_contrast = 1.04


## Walkable street, in REAL metres: ground, the building, solid props, the street's edges, the
## front-door exit into the hall and the spawn points.
const STREET_HALF_EXTENT := 12.0
## Solid props [real-metre centre on the ground (x, z), size (x, z)]; positions are PROP_LAYOUT's
## painting units / PAINT_SCALE.
const SOLID_PROPS := [
	[Vector2(-2.06, 0.5), Vector2(0.8, 0.8)],    # arcade cabinet under the awning
	[Vector2(-1.54, 1.08), Vector2(0.4, 0.4)],   # metal bucket
	[Vector2(-0.96, 0.83), Vector2(0.7, 0.45)],  # chalkboard
	[Vector2(2.25, 0.38), Vector2(0.6, 0.6)],    # potted shrub
	[Vector2(-2.92, 3.33), Vector2(0.25, 0.25)], # bollards
	[Vector2(-1.92, 3.33), Vector2(0.25, 0.25)],
	[Vector2(1.92, 3.33), Vector2(0.25, 0.25)],
	[Vector2(2.92, 3.33), Vector2(0.25, 0.25)],
]
## The double doorway is 7.25 painting units wide, centred on the front wall.
const DOOR_HALF_WIDTH_M := 7.25 / PAINT_SCALE * 0.5


func _box_collider(body: StaticBody3D, centre: Vector3, size: Vector3) -> void:
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = size
	cs.shape = box
	cs.position = centre
	body.add_child(cs)


func _build_walkable() -> void:
	var body := StaticBody3D.new()
	body.name = "street_collision"
	add_child(body)
	var e := STREET_HALF_EXTENT
	_box_collider(body, Vector3(0, -0.1, 0), Vector3(e * 2.0, 0.2, e * 2.0))
	var w := float(_faces["aa_face_front"]["wall_width_m"]) / PAINT_SCALE
	var d := DEPTH_M / PAINT_SCALE
	_box_collider(body, Vector3(0, 2.0, -d * 0.5), Vector3(w, 4.0, d))
	for spec: Array in SOLID_PROPS:
		var c: Vector2 = spec[0]
		var sz: Vector2 = spec[1]
		_box_collider(body, Vector3(c.x, 1.0, c.y), Vector3(sz.x, 2.0, sz.y))
	for side: Vector3 in [Vector3(e, 2, 0), Vector3(-e, 2, 0)]:
		_box_collider(body, side, Vector3(0.4, 4.0, e * 2.0))
	for side: Vector3 in [Vector3(0, 2, e), Vector3(0, 2, -e)]:
		_box_collider(body, side, Vector3(e * 2.0, 4.0, 0.4))

	var door := Area3D.new()
	door.name = "exit_front_door"
	door.add_to_group("scene_exits")
	door.set_meta("target_scene", "absinthe_arcade_interior")
	door.set_meta("target_spawn", "from_street")
	var cs := CollisionShape3D.new()
	var box := BoxShape3D.new()
	box.size = Vector3(DOOR_HALF_WIDTH_M * 2.0 - 0.4, 2.0, 0.5)
	cs.shape = box
	cs.position = Vector3(0, 1.0, 0.2)
	door.add_child(cs)
	add_child(door)

	SceneRouter.add_spawn_point(self, "start", Vector3(0.5, 0, 5.0), "north")
	SceneRouter.add_spawn_point(self, "from_arcade", Vector3(0, 0, 1.4), "south")
