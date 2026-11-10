class_name ArcadeOverlay
extends CanvasLayer
## The Absinthe Arcade's on-screen bits: the TOKENS HERE machine's how-many picker and the
## INSUFFICIENT CREDITS flash (author ruling ef_broke = insufficient, 2026-11-10: the Count
## Continue screen gag, reused whenever the bros can't pay). The hall decides what happens; this
## only shows things and reports the player's choice.

signal tokens_chosen(count: int)
signal picker_closed
signal flash_finished

const FLASH_SECONDS := 1.6
const BLINK_SECONDS := 0.2

var count := 0
var max_count := 0

var _picking := false
var _flash_left := 0.0
var _box: PanelContainer
var _picker_label: Label
var _flash_label: Label


func _init() -> void:
	layer = 20
	_box = PanelContainer.new()
	_box.set_anchors_and_offsets_preset(Control.PRESET_CENTER_BOTTOM)
	_box.offset_top = -150
	_box.offset_bottom = -40
	_box.offset_left = -260
	_box.offset_right = 260
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.03, 0.02, 0.06, 0.92)
	style.border_color = Color(0.95, 0.95, 0.9)
	style.set_border_width_all(4)
	style.set_corner_radius_all(6)
	style.set_content_margin_all(18)
	_box.add_theme_stylebox_override("panel", style)
	_picker_label = Label.new()
	_picker_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_picker_label.add_theme_font_size_override("font_size", 30)
	_box.add_child(_picker_label)
	_box.visible = false
	add_child(_box)
	_flash_label = Label.new()
	_flash_label.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_flash_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_flash_label.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	_flash_label.add_theme_font_size_override("font_size", 72)
	_flash_label.add_theme_color_override("font_color", Color(1.0, 0.18, 0.12))
	_flash_label.add_theme_color_override("font_outline_color", Color.BLACK)
	_flash_label.add_theme_constant_override("outline_size", 14)
	_flash_label.visible = false
	add_child(_flash_label)


func is_picking() -> bool:
	return _picking


func is_flashing() -> bool:
	return _flash_left > 0.0


func flash_text() -> String:
	return _flash_label.text


## Opens the how-many picker, from 1 to `most` tokens.
func open_picker(most: int) -> void:
	max_count = most
	count = 1
	_picking = true
	_box.visible = true
	_refresh()


func change_count(delta: int) -> void:
	if _picking:
		count = clampi(count + delta, 1, max_count)
		_refresh()


func confirm() -> void:
	if not _picking:
		return
	_close_picker()
	tokens_chosen.emit(count)


func cancel() -> void:
	if not _picking:
		return
	_close_picker()
	picker_closed.emit()


func flash(text: String) -> void:
	_flash_label.text = text
	_flash_label.visible = true
	_flash_left = FLASH_SECONDS


func _close_picker() -> void:
	_picking = false
	_box.visible = false


func _refresh() -> void:
	_picker_label.text = "TOKENS   <  %d  >\n%d SOVS" % [count, count * ArcadeRules.SOVS_PER_TOKEN]


func _process(delta: float) -> void:
	if _flash_left <= 0.0:
		return
	_flash_left -= delta
	_flash_label.visible = fmod(_flash_left, BLINK_SECONDS * 2.0) > BLINK_SECONDS
	if _flash_left <= 0.0:
		_flash_left = 0.0
		_flash_label.visible = false
		flash_finished.emit()


func _unhandled_input(event: InputEvent) -> void:
	if not _picking:
		return
	if event.is_action_pressed("move_right") or event.is_action_pressed("move_up"):
		change_count(1)
	elif event.is_action_pressed("move_left") or event.is_action_pressed("move_down"):
		change_count(-1)
	elif event.is_action_pressed("interact"):
		confirm()
	elif event.is_action_pressed("cancel"):
		cancel()
	else:
		return
	get_viewport().set_input_as_handled()
