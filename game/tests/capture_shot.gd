extends Node
## Renders one or more custom camera shots of the HD-2D Absinthe Arcade exterior, then quits.
## Visual QA helper; asserts nothing.
## Run:
##   Godot --path game --resolution 1920x1080 res://tests/capture_shot.tscn -- <out_png_prefix> \
##       <day|night> <name> ex,ey,ez tx,ty,tz [fov] [<name> ex,ey,ez tx,ty,tz [fov] ...]
## "gameplay" as the only shot name keeps the scene's own gameplay camera.

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn")


func _vec(s: String) -> Vector3:
	var p := s.split(",")
	return Vector3(float(p[0]), float(p[1]), float(p[2]))


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var prefix: String = args[0]
	var diorama = SCENE.instantiate()
	diorama.spawn_player = false
	add_child(diorama)
	diorama.night = args[1] == "night"
	var i := 2
	while i < args.size():
		var shot_name: String = args[i]
		var cam: Camera3D = get_viewport().get_camera_3d()
		if shot_name != "gameplay":
			cam = diorama.free_camera()
			cam.look_at_from_position(_vec(args[i + 1]), _vec(args[i + 2]), Vector3.UP)
			i += 3
			if i < args.size() and args[i].is_valid_float():
				cam.fov = float(args[i])
				i += 1
		else:
			i += 1
		for f in 20:
			await get_tree().process_frame
		await RenderingServer.frame_post_draw
		var path := "%s_%s_%s.png" % [prefix, shot_name, args[1]]
		get_viewport().get_texture().get_image().save_png(path)
		print("saved ", path)
	get_tree().quit()
