extends Control
## Title: New Game / Continue. Continue is disabled unless a valid save exists.

func _ready() -> void:
	var bg := ColorRect.new()
	bg.color = Color(0.06, 0.04, 0.1)
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)

	var vbox := VBoxContainer.new()
	vbox.anchor_left = 0.35
	vbox.anchor_right = 0.65
	vbox.anchor_top = 0.3
	vbox.anchor_bottom = 0.7
	vbox.add_theme_constant_override("separation", 16)
	add_child(vbox)

	var title := Label.new()
	title.text = "EUROBOUND"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 48)
	vbox.add_child(title)

	var subtitle := Label.new()
	subtitle.text = "One Last Round"
	subtitle.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	vbox.add_child(subtitle)

	var new_game := Button.new()
	new_game.text = "New Game"
	new_game.pressed.connect(_on_new_game)
	vbox.add_child(new_game)

	var continue_button := Button.new()
	continue_button.text = "Continue"
	continue_button.disabled = not SaveSystem.has_save()
	continue_button.pressed.connect(_on_continue)
	vbox.add_child(continue_button)

	new_game.grab_focus()

func _on_new_game() -> void:
	GameState.new_game(DataRepo)
	SceneRouter.goto_scene(GameState.current_scene_path)

func _on_continue() -> void:
	if SaveSystem.load_game(GameState):
		SceneRouter.restore_pending = true
		SceneRouter.goto_scene(GameState.current_scene_path)
