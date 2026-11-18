extends Node
## Preview-only (untracked): Woo Woo Whitney Tripo GLB (idle / walk clips) in the
## Absinthe Arcade hall at night, from the hall's own camera. Viewing only; the model is not changed.
## Run: godot --path game --resolution 1920x1080 res://tests/_preview_whitney/capture_whitney.tscn -- <out_dir> <glb> <frames_dir> <target_height_m>

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
const WORLD_SCALE := 0.75
var TARGET_HEIGHT := 1.65  # overridden by arg 4
const SPOT_STAND := Vector3(-1.9, 0, 2.6)
const SPOT_WALK := Vector3(-3.6, 0, 3.9)  # the 8c3z walk spot (-2.7) moved left so he walks across it
const FPS := 15.0

var _hall: Node3D


func _load(path: String) -> Node3D:
	var doc: GLTFDocument = FBXDocument.new() if path.ends_with(".fbx") else GLTFDocument.new()
	var state: GLTFState = FBXState.new() if path.ends_with(".fbx") else GLTFState.new()
	doc.append_from_file(path, state)
	var n: Node3D = doc.generate_scene(state)
	# Same render treatment the 8c3z mock gave its model (capture_character_approaches.gd _model).
	for mi: MeshInstance3D in n.find_children("*", "MeshInstance3D", true, false):
		for i in mi.mesh.get_surface_count():
			var m := mi.mesh.surface_get_material(i) as BaseMaterial3D
			if m:
				m.roughness = 1.0
				m.roughness_texture = null
				m.metallic = 0.0
				m.metallic_texture = null
				m.metallic_specular = 0.0
				m.diffuse_mode = BaseMaterial3D.DIFFUSE_BURLEY
				m.texture_filter = BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC
	return n


func _skinned_bounds(n: Node3D) -> AABB:
	var box := AABB()
	var first := true
	for mi: MeshInstance3D in n.find_children("*", "MeshInstance3D", true, false):
		var sk := mi.get_node_or_null(mi.skeleton) as Skeleton3D
		var arr := mi.mesh.surface_get_arrays(0)
		var verts: PackedVector3Array = arr[Mesh.ARRAY_VERTEX]
		var bones = arr[Mesh.ARRAY_BONES]
		var weights = arr[Mesh.ARRAY_WEIGHTS]
		var skin := mi.skin
		var nb: int = bones.size() / verts.size() if bones else 0
		var step := maxi(1, verts.size() / 3000)
		for vi in range(0, verts.size(), step):
			var p := verts[vi]
			var wp := Vector3.ZERO
			for k in nb:
				var w: float = weights[vi * nb + k]
				if w <= 0.0:
					continue
				var bind_i: int = bones[vi * nb + k]
				var bone := skin.get_bind_bone(bind_i)
				if bone < 0:
					bone = sk.find_bone(skin.get_bind_name(bind_i))
				wp += w * (sk.global_transform * sk.get_bone_global_pose(bone) * skin.get_bind_pose(bind_i) * p)
			if first:
				box = AABB(wp, Vector3.ZERO)
				first = false
			else:
				box = box.expand(wp)
	return box


func _screen_rect(box: AABB) -> Rect2:
	var cam := get_viewport().get_camera_3d()
	var r := Rect2()
	for i in 8:
		var p := cam.unproject_position(box.get_endpoint(i))
		r = Rect2(p, Vector2.ZERO) if i == 0 else r.expand(p)
	return r


## holder (spot; the hall's depth scaler owns its scale) -> turn (yaw, size) -> fbx root (Z-up to Y-up)
func _actor(path: String, at: Vector3, yaw: float, k: float) -> Array:
	var n := _load(path)
	var turn := Node3D.new()
	turn.rotation_degrees.y = yaw
	turn.scale = Vector3.ONE * k
	turn.add_child(n)
	var holder := Node3D.new()
	holder.add_child(turn)
	holder.position = at * WORLD_SCALE
	holder.add_to_group("hall_actors")
	_hall.add_child(holder)
	var ap: AnimationPlayer = n.find_children("*", "AnimationPlayer", true, false)[0]
	var sk: Skeleton3D = n.find_children("*", "Skeleton3D", true, false)[0]
	return [holder, n, ap, sk]


func _pose(ap: AnimationPlayer, clip: String, t: float) -> void:
	ap.play(clip)
	ap.pause()
	ap.seek(t, true)


func _save(path: String, n: Node3D, sk: Skeleton3D, tag: String) -> void:
	for i in 3:
		await get_tree().process_frame
	await RenderingServer.frame_post_draw
	get_viewport().get_texture().get_image().save_png(path)
	var b := _skinned_bounds(n)
	var w := func(bn: String) -> Vector3:
		var i := _bone(sk, bn)
		return Vector3.ZERO if i < 0 else sk.global_transform * sk.get_bone_global_pose(i).origin
	print("FRAME %s rect=%s height=%.3f ltoe=%s rtoe=%s lfoot=%s rfoot=%s" % [tag, _screen_rect(b), b.size.y,
		w.call("LeftToeBase").snapped(Vector3.ONE * 0.001), w.call("RightToeBase").snapped(Vector3.ONE * 0.001),
		w.call("LeftFoot").snapped(Vector3.ONE * 0.001), w.call("RightFoot").snapped(Vector3.ONE * 0.001)])


## Bone index by name suffix, so mixamorig_ and plain Tripo rig names both resolve.
func _bone(sk: Skeleton3D, suffix: String) -> int:
	for i in sk.get_bone_count():
		if sk.get_bone_name(i).ends_with(suffix):
			return i
	return -1


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var out_dir: String = args[0]
	var fbx: String = args[1]
	var frames_dir: String = args[2]
	if args.size() > 3:
		TARGET_HEIGHT = float(args[3])
	_hall = SCENE.instantiate()
	_hall.spawn_player = false
	add_child(_hall)
	_hall.night = true
	get_viewport().msaa_3d = Viewport.MSAA_4X

	# measure: rest height, unscaled; clip names; walking direction from the hips over the walk clip
	var probe := _actor(fbx, Vector3(0, 0, -50), 0.0, 1.0)
	await get_tree().process_frame
	var rest := _skinned_bounds(probe[1])
	var k := TARGET_HEIGHT / rest.size.y
	var walk := ""
	var idle := ""
	var pap: AnimationPlayer = probe[2]
	for clip in pap.get_animation_list():
		print("CLIP ", clip, " length=", pap.get_animation(clip).length, " tracks=", pap.get_animation(clip).get_track_count())
		if "walk" in clip.to_lower():
			walk = clip
		if "idle" in clip.to_lower():
			idle = clip
	if idle == "":
		# AI-prompted idles are named after their prompt: take the clip that is not the walk.
		for clip in pap.get_animation_list():
			if clip != walk and clip != "RESET":
				idle = clip
				break
	print("WALK clip='", walk, "' IDLE clip='", idle, "'")
	if walk == "":
		get_tree().quit(1)
		return
	# The Tripo export is "stay in place", so the hips do not travel: read facing from foot -> toe.
	var psk: Skeleton3D = probe[3]
	_pose(pap, idle, 0.0)
	await get_tree().process_frame
	var foot := psk.get_bone_global_pose(_bone(psk, "LeftFoot")).origin
	var toe := psk.get_bone_global_pose(_bone(psk, "LeftToeBase")).origin
	var fwd: Vector3 = psk.global_transform.basis * (toe - foot)
	fwd.y = 0.0
	var phi := atan2(fwd.x, fwd.z)
	var yaw_cam := rad_to_deg(-phi)
	var yaw_right := 90.0 + yaw_cam
	print("REST height=", rest.size.y, " scale=", k, " hips travel per clip=", fwd, " yaw_cam=", yaw_cam)
	probe[0].queue_free()

	var s := _actor(fbx, SPOT_STAND, yaw_cam, k)
	_pose(s[2], walk, 0.0)
	await _save(out_dir.path_join("a_walk_frame0_full.png"), s[1], s[3], "walk0")
	_pose(s[2], idle, 0.0)
	await _save(out_dir.path_join("a_idle_frame0_full.png"), s[1], s[3], "idle0")
	# Sample the idle across its length to find a head-level frame.
	var il: float = (s[2] as AnimationPlayer).get_animation(idle).length
	for j in range(1, 8):
		var ti := il * j / 8.0
		_pose(s[2], idle, ti)
		var hb := _bone(s[3], "Head")
		await _save(out_dir.path_join("idle_t%02d.png" % j), s[1], s[3], "idle_t=%.2f" % ti)
		var hp: Transform3D = s[3].get_bone_global_pose(hb)
		print("HEAD idle_t=%.2f fwd=%s" % [ti, (hp.basis * Vector3(0, 0, 1)).snapped(Vector3.ONE * 0.01)])
	s[0].queue_free()

	var w := _actor(fbx, SPOT_WALK, yaw_right, k)
	var a: Animation = (w[2] as AnimationPlayer).get_animation(walk)
	var count := int(floor(a.length * FPS)) + 1
	for i in count:
		var t := minf(i / FPS, a.length)
		_pose(w[2], walk, t)
		await _save(frames_dir.path_join("walk_%03d.png" % i), w[1], w[3], "walk_t=%.3f" % t)
	get_tree().quit()

