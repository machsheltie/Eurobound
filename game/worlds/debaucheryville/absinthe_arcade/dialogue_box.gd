class_name DialogueBox
extends CanvasLayer
## A scene's spoken lines and choices, one at a time, in a box along the bottom of the screen.
## Await `say` (press to go on), `choose` (returns the picked index) or `beat` (a short pause for a
## stage direction: the game has no narrator, so directions are never written on screen).

signal _next

const BEAT_S := 0.6

## Scales every beat (tests run them fast).
var beat_scale := 1.0
var mode := ""          ## "say", "choose" or ""
var cursor := 0
var options: Array = []
var speaker := ""
var text := ""

var _panel: Panel
var _who: Label
var _line: Label


func _init() -> void:
	layer = 35
	_panel = Panel.new()
	_panel.set_anchors_and_offsets_preset(Control.PRESET_BOTTOM_WIDE)
	_panel.offset_left = 120
	_panel.offset_right = -120
	_panel.offset_top = -270
	_panel.offset_bottom = -40
	var box := StyleBoxFlat.new()
	box.bg_color = Color(0.05, 0.02, 0.08, 0.92)
	box.border_color = Color(0.62, 0.38, 0.9)
	box.set_border_width_all(4)
	box.set_corner_radius_all(10)
	_panel.add_theme_stylebox_override("panel", box)
	_panel.visible = false
	add_child(_panel)
	_who = Label.new()
	_who.position = Vector2(28, 16)
	_who.add_theme_font_size_override("font_size", 30)
	_who.add_theme_color_override("font_color", Color(1.0, 0.85, 0.35))
	_panel.add_child(_who)
	_line = Label.new()
	_line.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_line.offset_left = 28
	_line.offset_right = -28
	_line.offset_top = 62
	_line.offset_bottom = -16
	_line.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_line.add_theme_font_size_override("font_size", 32)
	_panel.add_child(_line)


func say(who: String, line: String) -> void:
	speaker = who
	text = line
	mode = "say"
	_draw()
	await _next


func choose(choices: Array) -> int:
	options = choices
	cursor = 0
	mode = "choose"
	_draw()
	await _next
	return cursor


func beat(seconds: float = BEAT_S) -> void:
	_panel.visible = false
	if is_inside_tree():
		await get_tree().create_timer(seconds * beat_scale).timeout


func close() -> void:
	mode = ""
	_panel.visible = false


func press(action: String) -> void:
	match mode:
		"say":
			if action == "interact":
				mode = ""
				_next.emit()
		"choose":
			if action == "move_up":
				cursor = (cursor - 1 + options.size()) % options.size()
				_draw()
			elif action == "move_down":
				cursor = (cursor + 1) % options.size()
				_draw()
			elif action == "interact":
				mode = ""
				_next.emit()


func _unhandled_input(event: InputEvent) -> void:
	if mode == "":
		return
	for action in ["interact", "move_up", "move_down"]:
		if event.is_action_pressed(action):
			press(action)
			get_viewport().set_input_as_handled()
			return


func _draw() -> void:
	_panel.visible = true
	if mode == "choose":
		_who.text = ""
		var rows := []
		for i in options.size():
			rows.append(("> " if i == cursor else "   ") + String(options[i]))
		_line.text = "\n".join(rows)
	else:
		_who.text = speaker
		_line.text = text
