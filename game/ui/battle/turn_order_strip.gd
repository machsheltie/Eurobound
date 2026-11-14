class_name TurnOrderStrip
extends HBoxContainer
## The turn-order strip (design/game_design_document.md:301-303): one portrait per fighter, left to
## right in the exact order they act. The first one is acting now and pulses; the next one glows
## fainter. Feed it BattleCore.turn_order().
##
## Portrait art does not exist yet (Eurobound-ibgl). A portrait is a plain box with the fighter's
## name until art lands at PORTRAIT_DIR/<unit id>.png, which is picked up with no code change.

signal portrait_hovered(unit: BattleUnit)
signal portrait_unhovered(unit: BattleUnit)

const PORTRAIT_DIR := "res://assets/ui/battle/portraits/"
const PORTRAIT_SIZE := Vector2(132, 56)
const ACTIVE_COLOR := Color(1.0, 0.85, 0.3)
const NEXT_COLOR := Color(1.0, 0.85, 0.3, 0.45)
const PARTY_COLOR := Color(0.75, 0.45, 1.0)
const ENEMY_COLOR := Color(0.55, 0.55, 0.6)
const PULSE_S := 0.6

var units: Array = []
var portraits: Array[PanelContainer] = []
var _pulse: Tween


func _init() -> void:
	alignment = BoxContainer.ALIGNMENT_CENTER
	add_theme_constant_override("separation", 8)
	mouse_filter = Control.MOUSE_FILTER_IGNORE


static func has_portrait(unit_id: String) -> bool:
	return ResourceLoader.exists(PORTRAIT_DIR + unit_id + ".png")


## Shows `order` (BattleUnits, acting unit first). Rebuilds only when the order changed.
func show_order(order: Array) -> void:
	if order == units and portraits.size() == units.size():
		return
	units = order.duplicate()
	if _pulse != null:
		_pulse.kill()
		_pulse = null
	for p in portraits:
		remove_child(p)
		p.queue_free()
	portraits.clear()
	for i in units.size():
		var p := _portrait(units[i], i)
		add_child(p)
		portraits.append(p)
	_start_pulse()


func _ready() -> void:
	_start_pulse()


func _start_pulse() -> void:
	if portraits.is_empty() or not is_inside_tree() or _pulse != null:
		return
	_pulse = portraits[0].create_tween().set_loops()
	_pulse.tween_property(portraits[0], "modulate:a", 0.6, PULSE_S).set_trans(Tween.TRANS_SINE)
	_pulse.tween_property(portraits[0], "modulate:a", 1.0, PULSE_S).set_trans(Tween.TRANS_SINE)


## Whose turn the strip says it is, or null when it is empty.
func active_unit() -> BattleUnit:
	return units[0] if not units.is_empty() else null


## The name written on portrait `index` ("" when it shows art instead).
func name_on(index: int) -> String:
	var label := portraits[index].get_node_or_null("name") as Label
	return label.text if label != null else ""


func _portrait(u: BattleUnit, index: int) -> PanelContainer:
	var p := PanelContainer.new()
	p.custom_minimum_size = PORTRAIT_SIZE
	p.mouse_filter = Control.MOUSE_FILTER_STOP
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.04, 0.02, 0.08, 0.86)
	sb.set_border_width_all(4)
	sb.set_corner_radius_all(8)
	sb.set_content_margin_all(6)
	if index == 0:
		sb.border_color = ACTIVE_COLOR
	elif index == 1:
		sb.border_color = NEXT_COLOR
	else:
		sb.border_color = PARTY_COLOR if u.is_party() else ENEMY_COLOR
	p.add_theme_stylebox_override("panel", sb)
	if has_portrait(u.id):
		var art := TextureRect.new()
		art.name = "art"
		art.texture = load(PORTRAIT_DIR + u.id + ".png")
		art.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		art.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		art.mouse_filter = Control.MOUSE_FILTER_IGNORE
		p.add_child(art)
	else:
		var label := Label.new()
		label.name = "name"
		label.text = u.display_name
		label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		label.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		label.add_theme_font_size_override("font_size", 15)
		label.mouse_filter = Control.MOUSE_FILTER_IGNORE
		p.add_child(label)
	p.mouse_entered.connect(func() -> void: portrait_hovered.emit(u))
	p.mouse_exited.connect(func() -> void: portrait_unhovered.emit(u))
	return p
