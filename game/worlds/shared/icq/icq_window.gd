class_name IcqWindow
extends CanvasLayer
## Pilsner's outdated phone showing a pixelated ICQ chat window (design/worlds/shared/interactables/
## wifihotspots.md:1-3). Placeholder visuals only (Control/ColorRect styling, no art). It is a frame:
## the spoken lines are shown by the DialogueBox above it, and it holds no dialogue text of its own.

var _root: Control


func _init() -> void:
	layer = 34
	visible = false
	_root = Control.new()
	_root.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_root.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(_root)
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.55)
	dim.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	dim.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_root.add_child(dim)
	# The phone: a chunky grey slab with a green ICQ title bar and a flat chat pane.
	var phone := ColorRect.new()
	phone.color = Color(0.45, 0.47, 0.5)
	phone.set_anchors_and_offsets_preset(Control.PRESET_CENTER)
	phone.offset_left = -260
	phone.offset_right = 260
	phone.offset_top = -330
	phone.offset_bottom = 330
	_root.add_child(phone)
	var bar := ColorRect.new()
	bar.color = Color(0.1, 0.55, 0.15)
	bar.position = Vector2(20, 20)
	bar.size = Vector2(480, 48)
	phone.add_child(bar)
	var title := Label.new()
	title.text = "ICQ"
	title.position = Vector2(14, 4)
	title.add_theme_font_size_override("font_size", 32)
	bar.add_child(title)
	var pane := ColorRect.new()
	pane.color = Color(0.78, 0.84, 0.7)
	pane.position = Vector2(20, 80)
	pane.size = Vector2(480, 560)
	phone.add_child(pane)


func open() -> void:
	visible = true


func close() -> void:
	visible = false


func is_open() -> bool:
	return visible
