extends Node
## Plays the Absinthe Arcade like a player: holds "up" from the street start until the front door
## loads the hall, then "down" until the hall's front doors load the street again, saving a frame
## at each stage. Visual QA for movement and doors; prints the screen each stage ends on.
## Run: Godot --path game --resolution 1600x900 res://tests/walkthrough_absinthe_arcade.tscn -- <out_dir>

var _out := ""


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	_out = args[0] if args.size() > 0 else OS.get_user_data_dir()
	PlayerController.ensure_input_actions()
	_start.call_deferred()


## This node stays a child of root but stops being the current scene, so the doors' scene changes
## replace the street and hall and never this driver.
func _start() -> void:
	var street: Node = load(SceneRouter.scene_path("absinthe_arcade_exterior")).instantiate()
	get_tree().root.add_child(street)
	get_tree().current_scene = street
	_run()


func _shot(name_: String) -> void:
	await RenderingServer.frame_post_draw
	var path := _out.path_join(name_ + ".png")
	get_viewport().get_texture().get_image().save_png(path)
	print("saved ", path, " on ", get_tree().current_scene.scene_file_path.get_file())


func _hold(action: String, seconds: float) -> void:
	Input.action_press(action)
	await get_tree().create_timer(seconds).timeout
	Input.action_release(action)


func _run() -> void:
	await get_tree().create_timer(1.0).timeout
	await _shot("walk_01_street_start")
	Input.action_press("move_up")
	await get_tree().create_timer(0.8).timeout
	await _shot("walk_02_street_walking")
	await get_tree().create_timer(2.5).timeout
	Input.action_release("move_up")
	await get_tree().create_timer(0.8).timeout
	await _shot("walk_03_after_front_door")
	await _hold("move_down", 2.0)
	await get_tree().create_timer(0.8).timeout
	await _shot("walk_04_after_hall_doors")
	await _hold("move_up", 2.0)
	await get_tree().create_timer(0.8).timeout
	await _hold("move_left", 1.2)
	await _hold("move_up", 1.5)
	await _shot("walk_05_hall_wander_up_left")
	await _hold("move_up", 3.0)
	await _hold("move_right", 1.5)
	await _hold("move_up", 2.0)
	await _shot("walk_06_hall_back_row")
	get_tree().quit()
