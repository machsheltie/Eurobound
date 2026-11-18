extends GutTest
## PlatePropLayer boxes (Eurobound-10g6). The north-wing day and night plates are not registered to each
## other on the left wall, so a props JSON may give a box per plate under "boxes" -> prefix -> day/night.
## An old-style prop (no "boxes" entry) keeps its one shared box and lands exactly where it did before.

const FIXTURE := "res://tests/fixtures/plate_props/fx_plate_props.json"
const HALL_CABINETS := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/hall/props/aa_hall_cabinets.json"
const SHARED := Rect2(100, 200, 40, 60)
const NIGHT := Rect2(110, 320, 40, 60)
const Z := -2.0

var _root: Node3D
var _layer: PlatePropLayer


func before_each() -> void:
	_root = Node3D.new()
	add_child_autofree(_root)
	var cam := Camera3D.new()
	_root.add_child(cam)
	cam.look_at_from_position(Vector3(0, 5, 20), Vector3.ZERO)
	_layer = PlatePropLayer.new()
	_root.add_child(_layer)
	_layer.configure(cam, 4150.0, Vector2(2752, 1536))


func _rect_px(id: String) -> Vector4:
	return (_layer.node_of(id).material_override as ShaderMaterial).get_shader_parameter("rect_px")


func _v4(r: Rect2) -> Vector4:
	return Vector4(r.position.x, r.position.y, r.size.x, r.size.y)


## Where the quad would stand if it were fitted to `box` (the placement rule add_prop has always used).
func _reference_quad(box: Rect2) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	_layer.add_child(mi)
	_layer._fit_quad(mi, box, Z)
	return mi


## The box the loader used before per-plate boxes existed: the last sprite file matching the prefix.
func _old_rule_box(json_path: String, prefix: String) -> Rect2:
	var data: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(json_path))
	var box := Rect2()
	for file: String in Dictionary(data["sprites"]).keys():
		if file.ends_with(".png") and (file == prefix + ".png" or file.begins_with(prefix + "_")):
			var s: Dictionary = data["sprites"][file]
			box = Rect2(float(s["x"]), float(s["y"]), float(s["w"]), float(s["h"]))
	return box


func test_arcade_plate_prop_layer_old_style_prop_keeps_its_one_box_day_and_night() -> void:
	# Arrange / Act
	var ok := _layer.add_prop("shared", FIXTURE, "fx_shared", Z, "on")
	var ref := _reference_quad(SHARED)

	# Assert
	assert_true(ok)
	assert_eq(_layer.box_of("shared", "day"), SHARED)
	assert_eq(_layer.box_of("shared", "night"), SHARED)
	assert_eq(_layer.box_of("shared", "emit"), SHARED)
	_layer.set_night(false)
	assert_eq(_rect_px("shared"), _v4(SHARED), "day rect")
	_layer.set_night(true)
	assert_eq(_rect_px("shared"), _v4(SHARED), "night rect")
	var mi := _layer.node_of("shared")
	assert_eq(mi.position, ref.position, "quad position unchanged")
	assert_eq((mi.mesh as QuadMesh).size, (ref.mesh as QuadMesh).size, "quad size unchanged")


func test_arcade_plate_prop_layer_live_hall_props_keep_the_old_box() -> void:
	# Arrange
	var ids := {"cab_frogger": "aa_hall_cab_frogger", "cab_street_fighter": "aa_hall_cab_street_fighter",
		"cab_kebab_kombat": "aa_hall_cab_kebab_kombat"}

	for id: String in ids.keys():
		# Act
		var ok := _layer.add_prop(id, HALL_CABINETS, ids[id], Z, "attract")
		var want := _old_rule_box(HALL_CABINETS, ids[id])
		var ref := _reference_quad(want)

		# Assert
		assert_true(ok, id)
		_layer.set_night(false)
		assert_eq(_rect_px(id), _v4(want), id + " day rect")
		_layer.set_night(true)
		assert_eq(_rect_px(id), _v4(want), id + " night rect")
		assert_eq(_layer.node_of(id).position, ref.position, id + " quad position")
		assert_eq((_layer.node_of(id).mesh as QuadMesh).size, (ref.mesh as QuadMesh).size, id + " quad size")


func test_arcade_plate_prop_layer_per_plate_prop_uses_the_day_box_by_day_and_the_night_box_by_night() -> void:
	# Arrange
	var ok := _layer.add_prop("split", FIXTURE, "fx_split", Z, "on")
	var ref := _reference_quad(SHARED.merge(NIGHT))

	# Act
	_layer.set_night(false)
	var day_rect := _rect_px("split")
	var day_tex := _layer.current_texture("split")
	_layer.set_night(true)
	var night_rect := _rect_px("split")
	var night_tex := _layer.current_texture("split")
	var mat := _layer.node_of("split").material_override as ShaderMaterial

	# Assert
	assert_true(ok)
	assert_eq(_layer.box_of("split", "day"), SHARED)
	assert_eq(_layer.box_of("split", "night"), NIGHT)
	assert_eq(_layer.box_of("split", "emit"), NIGHT, "emit shares the night frame")
	assert_eq(day_rect, _v4(SHARED), "day rect")
	assert_eq(night_rect, _v4(NIGHT), "night rect")
	assert_eq(day_tex.resource_path, "res://tests/fixtures/plate_props/fx_split_on_day.png")
	assert_eq(night_tex.resource_path, "res://tests/fixtures/plate_props/fx_split_on_night.png")
	assert_true(mat.get_shader_parameter("use_emission"), "night lights the emit layer")
	var mi := _layer.node_of("split")
	assert_eq(mi.position, ref.position, "quad covers both boxes")
	assert_eq((mi.mesh as QuadMesh).size, (ref.mesh as QuadMesh).size, "quad covers both boxes")


func test_arcade_plate_prop_layer_missing_variant_box_falls_back_to_the_shared_box() -> void:
	# Arrange / Act
	var ok := _layer.add_prop("part", FIXTURE, "fx_part", Z, "on")

	# Assert
	assert_true(ok)
	assert_eq(_layer.box_of("part", "day"), SHARED, "no day box given: the shared one")
	assert_eq(_layer.box_of("part", "night"), NIGHT)
	_layer.set_night(false)
	assert_eq(_rect_px("part"), _v4(SHARED))
	_layer.set_night(true)
	assert_eq(_rect_px("part"), _v4(NIGHT))


func test_arcade_plate_prop_layer_north_wing_staged_left_wall_boxes_differ_per_plate() -> void:
	# Arrange: the staged north-wing cut-outs (props_staged has a .gdignore, so only the JSON is read here).
	var staged := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/north_wing/props_staged/"
	var want := {
		"aa_cab_time_crisis_cracked.json": {"aa_cab_time_crisis_cracked": [Rect2(51, 562, 372, 706), Rect2(51, 682, 372, 706)]},
		"aa_transition_taproom_curtain.json": {
			"aa_transition_taproom_curtain": [Rect2(82, 339, 268, 622), Rect2(85, 460, 268, 622)],
			"aa_transition_taproom_glow": [Rect2(82, 339, 268, 622), Rect2(85, 460, 268, 622)],
			"aa_transition_taproom_plaque": [Rect2(336, 613, 58, 74), Rect2(350, 703, 58, 74)]},
		"aa_transition_taproom_vapor.json": {"aa_transition_taproom_vapor": [Rect2(178, 938, 304, 364), Rect2(153, 1014, 304, 364)]},
	}

	for file: String in want.keys():
		var data: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(staged + file))
		for prefix: String in Dictionary(want[file]).keys():
			# Act
			var boxes := _layer._plate_boxes(data, prefix, Rect2())

			# Assert
			assert_eq(boxes["day"], want[file][prefix][0], prefix + " day")
			assert_eq(boxes["night"], want[file][prefix][1], prefix + " night")


func test_arcade_plate_prop_layer_box_of_unknown_prop_is_empty() -> void:
	# Arrange: no props added

	# Act
	var box := _layer.box_of("nope", "day")

	# Assert
	assert_eq(box, Rect2())
