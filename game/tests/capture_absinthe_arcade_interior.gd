extends Node
## Renders the HD-2D Absinthe Arcade hall from its fixed gameplay camera, by day and by night,
## empty (to compare with the painting) and with the three bros placed in front of, beside and
## behind the bottle bar (to check depth sorting). Visual QA only; it asserts nothing.
## Run: Godot --path game --resolution 1920x1080 res://tests/capture_absinthe_arcade_interior.tscn -- <out_dir>

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
const WORLD_SCALE := 0.75
## [aseprite, position in painting units, facing]
const BROS := [
	["res://assets/characters/party/chadwick/chadwick.aseprite", Vector3(0.6, 0, 3.2), "north_east"],
	["res://assets/characters/party/bradley/bradley.aseprite", Vector3(-2.4, 0, 1.8), "east"],
	["res://assets/characters/party/lord_pilsner/lord_pilsner.aseprite", Vector3(1.15, 0, -3.1), "south_east"],
]
## On the north-arch threshold, where the exit trigger fires (painting units).
const ARCH_POSITION := Vector3(0.24, 0, -5.4)


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var out_dir: String = args[0] if args.size() > 0 else OS.get_user_data_dir()
	var hall = SCENE.instantiate()
	hall.spawn_player = false
	add_child(hall)
	var bros: Array[Node3D] = []
	for spec: Array in BROS:
		var bro := PartySprite3D.new()
		var frames: SpriteFrames = load(spec[0])
		bro.sprite_frames = frames
		var used := frames.get_frame_texture(frames.get_animation_names()[0], 0).get_image().get_used_rect()
		bro.content_height_px = used.size.y
		bro.feet_row_px = used.end.y - 1
		bro.position = (spec[1] as Vector3) * WORLD_SCALE
		bro.facing = spec[2]
		bro.add_to_group("hall_actors")  # the hall's depth curve scales them
		hall.add_child(bro)
		bros.append(bro)
	for with_bros in [false, true]:
		for b in bros:
			b.visible = with_bros
		for mode in ["night", "day"]:
			hall.night = mode == "night"
			for i in 12:
				await get_tree().process_frame
			await RenderingServer.frame_post_draw
			var path := out_dir.path_join("aa_interior_hd2d_%s_%s.png" % ["bros" if with_bros else "empty", mode])
			get_viewport().get_texture().get_image().save_png(path)
			print("saved ", path)
	# Chadwick on the north-arch threshold, the last frame before the exit trigger changes screens.
	bros[0].position = ARCH_POSITION * WORLD_SCALE
	bros[0].facing = "north"
	hall.night = true
	for i in 12:
		await get_tree().process_frame
	await RenderingServer.frame_post_draw
	var arch_path := out_dir.path_join("aa_interior_hd2d_arch_night.png")
	get_viewport().get_texture().get_image().save_png(arch_path)
	print("saved ", arch_path)
	get_tree().quit()
