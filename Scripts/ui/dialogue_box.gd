extends CanvasLayer
## Bottom-anchored dialogue panel: speaker name, typewriter text, option
## buttons. Applies collected flags to GameState when the dialogue closes.

const CHARS_PER_SECOND := 40.0

var _runner: DialogueRunner
var _player
var _panel: PanelContainer
var _speaker_label: Label
var _text_label: Label
var _options_box: VBoxContainer
var _full_text: String = ""
var _typing: bool = false
var _type_tween: Tween

func _ready() -> void:
	layer = 10
	_panel = PanelContainer.new()
	_panel.anchor_left = 0.05
	_panel.anchor_right = 0.95
	_panel.anchor_top = 0.7
	_panel.anchor_bottom = 0.97
	add_child(_panel)

	var vbox := VBoxContainer.new()
	_panel.add_child(vbox)

	_speaker_label = Label.new()
	_speaker_label.add_theme_color_override("font_color", Color(0.95, 0.8, 0.3))
	vbox.add_child(_speaker_label)

	_text_label = Label.new()
	_text_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_text_label.size_flags_vertical = Control.SIZE_EXPAND_FILL
	vbox.add_child(_text_label)

	_options_box = VBoxContainer.new()
	vbox.add_child(_options_box)

func open(npc_id: String, player) -> void:
	_player = player
	_player.can_move = false
	var tree: Dictionary = DataRepo.get_dialogue_tree(npc_id)
	if tree.is_empty():
		_close()
		return
	_runner = DialogueRunner.new(tree)
	_show_node(_runner.start())

func _show_node(node: Dictionary) -> void:
	if node.is_empty():
		_close()
		return
	_speaker_label.text = String(node.get("speaker", ""))
	_full_text = String(node.get("text", ""))
	_start_typing()

func _start_typing() -> void:
	_typing = true
	_clear_options()
	_text_label.text = ""
	_type_tween = create_tween()
	var duration := _full_text.length() / CHARS_PER_SECOND
	_type_tween.tween_method(_set_visible_chars, 0, _full_text.length(), duration)
	_type_tween.finished.connect(_on_typing_done)

func _set_visible_chars(count: int) -> void:
	_text_label.text = _full_text.substr(0, count)

func _on_typing_done() -> void:
	_typing = false
	_text_label.text = _full_text
	_build_options()

func _build_options() -> void:
	_clear_options()
	var options := _runner.available_options(GameState.inventory)
	if options.is_empty():
		var done := Button.new()
		done.text = "[End]"
		done.pressed.connect(_close)
		_options_box.add_child(done)
		done.grab_focus()
		return
	var first := true
	for option in options:
		var button := Button.new()
		button.text = String(option.get("text", "..."))
		button.pressed.connect(_on_option_pressed.bind(option))
		_options_box.add_child(button)
		if first:
			button.grab_focus()
			first = false

func _on_option_pressed(option: Dictionary) -> void:
	_show_node(_runner.choose(option))

func _clear_options() -> void:
	for child in _options_box.get_children():
		child.queue_free()

func _unhandled_input(event: InputEvent) -> void:
	if _typing and event.is_action_pressed("interact"):
		# Skip the typewriter animation.
		get_viewport().set_input_as_handled()
		if _type_tween and _type_tween.is_valid():
			_type_tween.kill()
		_on_typing_done()

func _close() -> void:
	if _runner != null:
		for flag in _runner.collected_flags:
			GameState.set_flag(flag)
	if _player != null:
		_player.can_move = true
	queue_free()
