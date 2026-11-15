extends Node
## In-game mock shots for the character question (Eurobound-8c3z): the same Lord Pilsner, standing
## and mid-stride, in the Absinthe Arcade hall from its gameplay camera, shown several ways.
## Visual QA only; it asserts nothing and changes no game file.
## Run: Godot --path game --resolution 1920x1080 res://tests/capture_character_approaches.tscn -- \
##          <out_dir> <idle.glb> <walk.glb> [<painted_idle.png> <painted_walk.png>]
## Shots: now (look-B frames as the game draws them today), fixed (same frames pre-scaled to
## display size, smooth edges), model (the posed 3D model standing in the room), painted (repainted frames, optional).

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
const WORLD_SCALE := 0.75
const FRAMES := "res://assets/characters/party/lord_pilsner/look_b/"
const PPM := 300.0
const FEET_FROM_BOTTOM := 44.0
## Pixels per metre a full-size actor is drawn at in the hall at 1080p (measured: about 0.4 of 300).
const DISPLAY_PPM := 190.0
## [position in painting units, frame path under FRAMES, yaw of the 3D model in degrees]
const SPOTS := [
	[Vector3(-1.9, 0, 2.6), "idle/S/00.png", 0.0],
	[Vector3(-2.7, 0, 3.9), "walk/E/02.png", 90.0],
]

var _hall: Node3D
var _actors: Array[Node3D] = []


func _sprite(img: Image, fixed: bool, at: Vector3, ppm := PPM, feet := FEET_FROM_BOTTOM) -> Sprite3D:
	var s := Sprite3D.new()
	if fixed:
		# Pre-scale to about the size it is drawn at (DISPLAY_PPM), with a proper filter, instead of
		# letting the GPU shrink a 300 px/m frame to a third with plain linear sampling.
		img.fix_alpha_edges()
		var k := DISPLAY_PPM / ppm
		img.resize(int(round(img.get_width() * k)), int(round(img.get_height() * k)), Image.INTERPOLATE_LANCZOS)
		ppm *= k
		feet *= k
	s.texture = ImageTexture.create_from_image(img)
	s.pixel_size = 1.0 / ppm
	s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	s.shaded = true
	s.double_sided = false
	s.centered = true
	s.offset = Vector2(0, img.get_height() * 0.5 - feet)
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR
	s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	if fixed:
		s.alpha_cut = SpriteBase3D.ALPHA_CUT_OPAQUE_PREPASS  # soft edges instead of a hard cut-out
	s.position = at * WORLD_SCALE
	return s


func _model(path: String, at: Vector3, yaw: float) -> Node3D:
	var doc := GLTFDocument.new()
	var state := GLTFState.new()
	doc.append_from_file(path, state)
	var n: Node3D = doc.generate_scene(state)
	for mi: MeshInstance3D in n.find_children("*", "MeshInstance3D", true, false):
		for i in mi.mesh.get_surface_count():
			var m := mi.mesh.surface_get_material(i) as BaseMaterial3D
			if m:
				m.roughness = 1.0
				m.metallic = 0.0
				m.metallic_specular = 0.0
				m.diffuse_mode = BaseMaterial3D.DIFFUSE_TOON if OS.get_cmdline_user_args().has("--toon") else BaseMaterial3D.DIFFUSE_BURLEY
				m.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC
	var holder := Node3D.new()
	holder.add_child(n)
	n.rotation_degrees.y = yaw
	holder.position = at * WORLD_SCALE
	return holder


func _show(nodes: Array[Node3D]) -> void:
	for a in _actors:
		a.queue_free()
	_actors = nodes
	for a in nodes:
		a.add_to_group("hall_actors")
		_hall.add_child(a)


func _shot(out_dir: String, name_: String) -> void:
	for i in 16:
		await get_tree().process_frame
	await RenderingServer.frame_post_draw
	var path := out_dir.path_join("approach_%s.png" % name_)
	get_viewport().get_texture().get_image().save_png(path)
	print("saved ", path)


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var out_dir: String = args[0]
	_hall = SCENE.instantiate()
	_hall.spawn_player = false
	add_child(_hall)
	_hall.night = true
	for fixed in [false, true]:
		var set_: Array[Node3D] = []
		for spot: Array in SPOTS:
			set_.append(_sprite((load(FRAMES + spot[1]) as Texture2D).get_image(), fixed, spot[0]))
		get_viewport().msaa_3d = Viewport.MSAA_4X if fixed else Viewport.MSAA_DISABLED  # 'now' is the game as it ships today
		_show(set_)
		await _shot(out_dir, "fixed" if fixed else "now")
	if args.size() > 2:
		var set_m: Array[Node3D] = []
		set_m.append(_model(args[1], SPOTS[0][0], SPOTS[0][2]))
		set_m.append(_model(args[2], SPOTS[1][0], SPOTS[1][2]))
		_show(set_m)
		await _shot(out_dir, "model")
	if args.size() > 4 and args[3].ends_with(".png"):
		var set_p: Array[Node3D] = []
		for i in 2:
			var img := Image.load_from_file(args[3 + i])
			# Painted frames keep the look-B framing: feet 44/640 of the height above the bottom edge.
			var k := img.get_height() / 640.0
			set_p.append(_sprite(img, true, SPOTS[i][0], PPM * k, FEET_FROM_BOTTOM * k))
		_show(set_p)
		await _shot(out_dir, "painted")
	get_tree().quit()
