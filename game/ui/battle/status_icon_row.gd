class_name StatusIconRow
extends HBoxContainer
## One fighter's live statuses, one chip each (design/game_design_document.md:307-313).
## A chip shows the icon at ICON_DIR/<status id>.png when that art exists. No status icon has been
## made yet (Eurobound-ibgl), so a chip falls back to the status name from the status table
## (BattleCore._status_name, the same name the battle log uses). No wording is invented here.
##
## Buff/debuff border colours (GDD :309) are not drawn: status_effects.json has no field that says
## which a status is. Every chip gets the same border until the author rules it.

## The mouse button went down (pressed) or up on a status chip.
signal status_button(unit: BattleUnit, status_id: String, pressed: bool)

const ICON_DIR := "res://assets/ui/status_icons/"
const ICON_SIZE := Vector2(28, 28)
## The existing screen's word for a bro inside Croc Monsieur (battle_screen.gd, pre-ibgl).
const SWALLOWED := "SWALLOWED"

var unit: BattleUnit
var shown: Array = []          ## status ids, in chip order
var chips: Array[PanelContainer] = []
var _extra := false


func _init() -> void:
	add_theme_constant_override("separation", 6)
	mouse_filter = Control.MOUSE_FILTER_IGNORE


static func has_icon(status_id: String) -> bool:
	return ResourceLoader.exists(ICON_DIR + status_id + ".png")


## Shows `u`'s live statuses. Rebuilds only when they changed.
func show_unit(u: BattleUnit) -> void:
	var ids: Array = []
	for s in u.statuses.keys():
		ids.append(String(s))
	var extra := u.gone_turns > 0
	if u == unit and ids == shown and extra == _extra:
		return
	unit = u
	shown = ids
	_extra = extra
	for c in chips:
		remove_child(c)
		c.queue_free()
	chips.clear()
	for id in ids:
		_add_chip(id, BattleCore._status_name(id).to_upper())
	if extra:
		_add_chip("", SWALLOWED)


## The text on chip `index` ("" when it shows an icon).
func text_on(index: int) -> String:
	var label := chips[index].get_node_or_null("name") as Label
	return label.text if label != null else ""


func _add_chip(status_id: String, text: String) -> void:
	var chip := PanelContainer.new()
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.04, 0.02, 0.08, 0.86)
	sb.border_color = Color(0.75, 0.45, 1.0)
	sb.set_border_width_all(2)
	sb.set_corner_radius_all(6)
	sb.content_margin_left = 6
	sb.content_margin_right = 6
	sb.content_margin_top = 1
	sb.content_margin_bottom = 1
	chip.add_theme_stylebox_override("panel", sb)
	chip.tooltip_text = text if has_icon(status_id) else ""
	if not status_id.is_empty() and has_icon(status_id):
		var icon := TextureRect.new()
		icon.name = "icon"
		icon.texture = load(ICON_DIR + status_id + ".png")
		icon.custom_minimum_size = ICON_SIZE
		icon.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		icon.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		icon.mouse_filter = Control.MOUSE_FILTER_IGNORE
		chip.add_child(icon)
	else:
		var label := Label.new()
		label.name = "name"
		label.text = text
		label.add_theme_font_size_override("font_size", 15)
		label.mouse_filter = Control.MOUSE_FILTER_IGNORE
		chip.add_child(label)
	if status_id.is_empty():
		chip.mouse_filter = Control.MOUSE_FILTER_IGNORE
	else:
		chip.mouse_filter = Control.MOUSE_FILTER_STOP
		var u := unit
		chip.gui_input.connect(func(event: InputEvent) -> void:
			if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
				status_button.emit(u, status_id, event.pressed))
		chip.mouse_exited.connect(func() -> void: status_button.emit(u, status_id, false))
	add_child(chip)
	chips.append(chip)
