extends Node
## Renders the HD-2D Absinthe Arcade exterior from several cameras in day and night, saves
## screenshots, then quits. Visual QA only; it asserts nothing.
## Run: Godot --path game --resolution 1920x1080 res://tests/capture_absinthe_arcade_exterior.tscn -- <out_dir>

const SCENE := preload("res://worlds/debaucheryville/absinthe_arcade_exterior_hd2d.tscn")
const SHOTS := {
	"front": [Vector3(3.75, 6.7, 24.2), Vector3(0, 4.8, -0.8)],
	"threequarter_left": [Vector3(-15.8, 10.8, 14.2), Vector3(0, 4.6, -3.75)],
	"threequarter_right_back": [Vector3(15.8, 12.5, -20.8), Vector3(0, 4.6, -3.75)],
	"closeup_cabinet_right": [Vector3(0.8, 2.1, 4.8), Vector3(-2.0, 1.1, 0.4)],
	"closeup_cabinet_left": [Vector3(-5.6, 2.0, 3.6), Vector3(-2.0, 1.2, 0.3)],
}


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var out_dir: String = args[0] if args.size() > 0 else OS.get_user_data_dir()
	var diorama = SCENE.instantiate()
	diorama.spawn_player = false
	add_child(diorama)
	# Scale check: a 1.8 m stand-in person beside the doorway (world is in real metres).
	var person := MeshInstance3D.new()
	var capsule := CapsuleMesh.new()
	capsule.height = 1.8
	capsule.radius = 0.25
	person.mesh = capsule
	person.position = Vector3(-0.4, 0.9, 1.2)
	diorama.add_child(person)
	var cam: Camera3D = diorama.free_camera()
	for shot in SHOTS.keys():
		for mode in ["day", "night"]:
			cam.look_at_from_position(SHOTS[shot][0], SHOTS[shot][1], Vector3.UP)
			diorama.night = mode == "night"
			for i in 12:
				await get_tree().process_frame
			await RenderingServer.frame_post_draw
			var img := get_viewport().get_texture().get_image()
			var path := out_dir.path_join("aa_exterior_hd2d_%s_%s.png" % [shot, mode])
			img.save_png(path)
			print("saved ", path)
	get_tree().quit()
