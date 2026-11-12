class_name PlatePropLayer
extends Node3D
## Interactable props cut out of a projected-paint plate, so each can change state in game
## (author round v43: "the token machine, prize counter and bar might be interacted with so should be
## assets. And several of the cabinets will be playable").
##
## Each prop is one cut-out per state and time of day, `<prefix>_<state>_<day|night|emit>.png`, all
## sharing one box (top-left x,y and size on the plate) listed in the prop's JSON. Same trick as the
## restroom's statue hands: the cut-out is painted with the room's projected paint shader
## (rect_px = the box, use_alpha = true) on a quad standing at `z`, so it lands on exactly its plate
## pixels and the default state is indistinguishable from the plate. Because the quad is real
## geometry the bros still sort against it: they draw in front of it when nearer than `z`, behind
## it when farther. Night adds the _emit file as emission so screens glow like the plate.
##
## Add this node under the room's diorama, after the room is in the tree.

const PAINT_SHADER := preload("res://worlds/debaucheryville/hd2d_projected_paint.gdshader")
const VARIANTS := ["day", "night", "emit"]

var night := true
var _camera: Camera3D
var _focal_px := 4150.0
var _image_px := Vector2(2752, 1536)
## prop id -> {mesh: MeshInstance3D, mat: ShaderMaterial, dir: String, prefix: String,
##             states: {state: {variant: file name}}, state: String}
var _props: Dictionary = {}


func configure(camera: Camera3D, focal_px: float, image_px: Vector2) -> void:
	_camera = camera
	_focal_px = focal_px
	_image_px = image_px


## Reads `json_path` (a props JSON with a "sprites" map) and builds the quad for the sprites whose
## file name starts with `prefix` (e.g. "aa_hall_cab_frogger"). `z` is the quad's depth in the
## diorama's painting units; `default_state` is shown first. Returns false when nothing matched.
func add_prop(id: String, json_path: String, prefix: String, z: float, default_state: String) -> bool:
	if _camera == null or not FileAccess.file_exists(json_path):
		return false
	var data = JSON.parse_string(FileAccess.get_file_as_string(json_path))
	if typeof(data) != TYPE_DICTIONARY:
		return false
	var states := {}
	var box := Rect2()
	for file: String in Dictionary(data.get("sprites", {})).keys():
		if not file.begins_with(prefix + "_") or not file.ends_with(".png"):
			continue
		var stem := file.trim_prefix(prefix + "_").trim_suffix(".png")
		var cut := stem.rfind("_")
		if cut < 0:
			continue
		var state := stem.substr(0, cut)
		var variant := stem.substr(cut + 1)
		if not VARIANTS.has(variant):
			continue
		if not states.has(state):
			states[state] = {}
		states[state][variant] = file
		var s: Dictionary = data["sprites"][file]
		box = Rect2(float(s["x"]), float(s["y"]), float(s["w"]), float(s["h"]))
	if states.is_empty():
		return false
	var mat := ShaderMaterial.new()
	mat.shader = PAINT_SHADER
	mat.set_shader_parameter("paint_view", Projection(_camera.global_transform.affine_inverse()))
	mat.set_shader_parameter("focal_px", _focal_px)
	mat.set_shader_parameter("image_px", _image_px)
	mat.set_shader_parameter("use_alpha", true)
	mat.set_shader_parameter("rect_px", Vector4(box.position.x, box.position.y, box.size.x, box.size.y))
	mat.render_priority = 1
	var mi := MeshInstance3D.new()
	mi.name = "prop_" + id
	mi.material_override = mat
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	add_child(mi)
	_fit_quad(mi, box, z)
	_props[id] = {"mesh": mi, "mat": mat, "dir": json_path.get_base_dir() + "/", "prefix": prefix,
		"states": states, "state": ""}
	set_state(id, default_state)
	return true


func has_prop(id: String) -> bool:
	return _props.has(id)


func prop_ids() -> Array:
	return _props.keys()


func states_of(id: String) -> Array:
	return Dictionary(_props[id]["states"]).keys() if _props.has(id) else []


func state_of(id: String) -> String:
	return String(_props[id]["state"]) if _props.has(id) else ""


## The texture path a prop shows for `state` in `variant` ("day", "night" or "emit"), "" if absent.
func texture_path(id: String, state: String, variant: String) -> String:
	if not _props.has(id):
		return ""
	var file: String = Dictionary(Dictionary(_props[id]["states"]).get(state, {})).get(variant, "")
	return "" if file.is_empty() else String(_props[id]["dir"]) + file


## The albedo texture currently on the prop's material (for tests and QA).
func current_texture(id: String) -> Texture2D:
	if not _props.has(id):
		return null
	return (_props[id]["mat"] as ShaderMaterial).get_shader_parameter("albedo_tex")


## Switches a prop to `state`. Returns false (and changes nothing) for an unknown prop or state.
func set_state(id: String, state: String) -> bool:
	if not _props.has(id) or not Dictionary(_props[id]["states"]).has(state):
		return false
	_props[id]["state"] = state
	_apply(id)
	return true


func set_night(value: bool) -> void:
	night = value
	for id: String in _props.keys():
		_apply(id)


func _apply(id: String) -> void:
	var p: Dictionary = _props[id]
	var mat: ShaderMaterial = p["mat"]
	var state: String = p["state"]
	mat.set_shader_parameter("albedo_tex", load(texture_path(id, state, "night" if night else "day")))
	var emit := texture_path(id, state, "emit")
	var lit := night and not emit.is_empty()
	mat.set_shader_parameter("use_emission", lit)
	if lit:
		mat.set_shader_parameter("emit_tex", load(emit))


## Sizes the quad to the world-space bounds of the plate box seen through the paint camera on the
## vertical plane z (the shader discards everything outside the box, so a snug rectangle is enough).
func _fit_quad(mi: MeshInstance3D, box: Rect2, z: float) -> void:
	var plane_point := to_global(Vector3(0, 0, z))
	var normal := global_transform.basis.z.normalized()
	var origin := _camera.global_position
	var lo := Vector2(INF, INF)
	var hi := Vector2(-INF, -INF)
	for corner: Vector2 in [box.position, Vector2(box.end.x, box.position.y), box.end, Vector2(box.position.x, box.end.y)]:
		var d := Vector3((corner.x - _image_px.x * 0.5) / _focal_px, -(corner.y - _image_px.y * 0.5) / _focal_px, -1.0)
		var dir := (_camera.global_transform.basis * d).normalized()
		var t := (plane_point - origin).dot(normal) / dir.dot(normal)
		var local := to_local(origin + dir * t)
		lo = lo.min(Vector2(local.x, local.y))
		hi = hi.max(Vector2(local.x, local.y))
	var pad := 0.1
	var quad := QuadMesh.new()
	quad.size = (hi - lo) + Vector2(pad, pad) * 2.0
	mi.mesh = quad
	mi.position = Vector3((lo.x + hi.x) * 0.5, (lo.y + hi.y) * 0.5, z)
