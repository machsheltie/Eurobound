extends CanvasLayer
## Esc pauses. Resume / Save / Quit to Title. Instanced by LocationBase.

var _panel: PanelContainer
var _save_button: Button

func _ready() -> void:
	layer = 20
	process_mode = Node.PROCESS_MODE_ALWAYS
	_panel = PanelContainer.new()
	_panel.anchor_left = 0.35
	_panel.anchor_right = 0.65
	_panel.anchor_top = 0.3
	_panel.anchor_bottom = 0.7
	_panel.visible = false
	add_child(_panel)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 12)
	_panel.add_child(vbox)

	var title := Label.new()
	title.text = "PAUSED"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	vbox.add_child(title)

	var resume := Button.new()
	resume.text = "Resume"
	resume.pressed.connect(_toggle)
	vbox.add_child(resume)

	_save_button = Button.new()
	_save_button.text = "Save"
	_save_button.pressed.connect(_on_save)
	vbox.add_child(_save_button)

	var quit := Button.new()
	quit.text = "Quit to Title"
	quit.pressed.connect(_on_quit)
	vbox.add_child(quit)

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("pause"):
		_toggle()

func _toggle() -> void:
	_panel.visible = not _panel.visible
	get_tree().paused = _panel.visible
	_save_button.text = "Save"

func _on_save() -> void:
	_save_button.text = "Saved!" if SaveSystem.save_game(GameState) else "Save failed!"

func _on_quit() -> void:
	get_tree().paused = false
	SceneRouter.goto_scene("res://ui/title_screen.tscn")
