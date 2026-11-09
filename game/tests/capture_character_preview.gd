extends Node
## Stands a party sprite in front of the Absinthe Arcade and renders the gameplay camera plus a
## close-up, by day and by night. Visual QA for the sprite pipeline; asserts nothing.
## Run: Godot --path game --resolution 1920x1080 res://tests/capture_character_preview.tscn -- \
##          <out_prefix> [res://a.aseprite[,res://b.aseprite,...]] [facing] [action]
## Several comma-separated characters stand in a row, 0.9 m apart, for a lineup. `action` picks
## the animation (idle, walk); each character starts on a different frame so a lineup shows a spread.

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn")
const DEFAULT_FRAMES := "res://assets/characters/party/lord_pilsner/lord_pilsner.aseprite"
const SPOT := Vector3(0.35, 0.0, 1.7)  # on the street in front of the doorway, real metres


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var prefix: String = args[0]
	var frames_path: String = args[1] if args.size() > 1 else DEFAULT_FRAMES
	var facing: String = args[2] if args.size() > 2 else "south"
	var action: String = args[3] if args.size() > 3 else "idle"
	var paths := frames_path.split(",")
	const SPACING := 0.9
	for mode in ["day", "night"]:
		# Fresh scene per time of day, so the gameplay camera rig is intact for each gameplay shot.
		var diorama = SCENE.instantiate()
		add_child(diorama)
		for i in paths.size():
			var offset := Vector3((i - (paths.size() - 1) * 0.5) * SPACING, 0, 0)
			var bro := _make_bro(load(paths[i]), facing, SPOT + offset)
			bro.action = action
			diorama.add_child(bro)
			bro.frame = (i * 3) % bro.sprite_frames.get_frame_count(bro.animation)
		diorama.night = mode == "night"
		for shot in ["gameplay", "close"]:
			if shot == "close":
				var cam: Camera3D = diorama.free_camera()
				cam.fov = 30.0
				var back := 4.2 + 1.6 * (paths.size() - 1)
				cam.look_at_from_position(SPOT + Vector3(0.6, 1.6, back), SPOT + Vector3(0, 1.0, 0), Vector3.UP)
			for i in 20:
				await get_tree().process_frame
			await RenderingServer.frame_post_draw
			var path := "%s_%s_%s.png" % [prefix, shot, mode]
			get_viewport().get_texture().get_image().save_png(path)
			print("saved ", path)
		diorama.queue_free()
		await get_tree().process_frame
	get_tree().quit()


func _make_bro(frames: SpriteFrames, facing: String, at: Vector3) -> PartySprite3D:
	var bro := PartySprite3D.new()
	bro.sprite_frames = frames
	var first: Texture2D = frames.get_frame_texture(frames.get_animation_names()[0], 0)
	var used := first.get_image().get_used_rect()
	bro.content_height_px = used.size.y
	bro.feet_row_px = used.end.y - 1
	bro.position = at
	bro.facing = facing
	return bro
