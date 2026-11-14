class_name PeekCard
extends PanelContainer
## The peek on a turn-order portrait: HP, buffs/debuffs and Speed, and nothing else
## (design/game_design_document.md:304, author round v35).

var unit: BattleUnit
var _label: Label


func _init() -> void:
	mouse_filter = Control.MOUSE_FILTER_IGNORE
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.04, 0.02, 0.08, 0.94)
	sb.border_color = Color(1.0, 0.85, 0.3)
	sb.set_border_width_all(4)
	sb.set_corner_radius_all(10)
	sb.set_content_margin_all(14)
	add_theme_stylebox_override("panel", sb)
	_label = Label.new()
	_label.add_theme_font_size_override("font_size", 22)
	_label.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(_label)
	visible = false


## Shows `u`, or hides the card when `u` is null.
func show_unit(u: BattleUnit) -> void:
	unit = u
	visible = u != null
	if u != null:
		_label.text = text_for(u)


## Name, HP, Speed, then each live status by its status-table name. A bro's HP is what his rolling
## meter shows, the same number as his panel.
static func text_for(u: BattleUnit) -> String:
	var hp := ceili(u.meter) if u.is_party() else u.hp
	var lines := [u.display_name.to_upper(), "HP %d / %d" % [hp, u.max_hp], "SPEED %d" % u.battle_speed()]
	var names := []
	for s in u.statuses.keys():
		names.append(BattleCore._status_name(String(s)).to_upper())
	if not names.is_empty():
		lines.append(", ".join(names))
	return "\n".join(lines)
