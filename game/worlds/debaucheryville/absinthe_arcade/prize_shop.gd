class_name PrizeShop
extends CanvasLayer
## The Prize Redemption counter: trade tickets for the catalogue prizes and the junk shelf (prices
## and names in key_items.json). Catalogue prizes are one each; junk-shelf prizes can be bought again.

signal closed(bought: Array)

const ITEMS := "res://assets/data/items/key_items.json"
const CATALOGUE := "absinthe_arcade_prize_redemption"
const JUNK := "absinthe_arcade_prize_redemption_junk_shelf"

var state
var rows: Array = []      ## [{"id", "name", "price", "junk"}]
var cursor := 0
var bought: Array = []
var notice := ""

var _label: RichTextLabel


func setup(game_state) -> void:
	state = game_state
	rows = stock()


static func stock() -> Array:
	var items: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(ITEMS))["key_items"]
	var out := []
	for id: String in items.keys():
		var it: Dictionary = items[id]
		var src := String(it.get("source", ""))
		if (src == CATALOGUE or src == JUNK) and it.has("ticket_price"):
			out.append({"id": id, "name": String(it["display_name"]), "price": int(it["ticket_price"]), "junk": src == JUNK})
	# The catalogue first, then the junk shelf, each cheapest first.
	out.sort_custom(func(a: Dictionary, b: Dictionary) -> bool:
		if a["junk"] != b["junk"]:
			return not a["junk"]
		return int(a["price"]) < int(b["price"]))
	return out


func _init() -> void:
	layer = 30
	var panel := Panel.new()
	panel.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	panel.offset_left = 360
	panel.offset_right = -360
	panel.offset_top = 80
	panel.offset_bottom = -80
	var box := StyleBoxFlat.new()
	box.bg_color = Color(0.04, 0.02, 0.07, 0.94)
	box.border_color = Color(0.62, 0.38, 0.9)
	box.set_border_width_all(4)
	box.set_corner_radius_all(10)
	panel.add_theme_stylebox_override("panel", box)
	add_child(panel)
	_label = RichTextLabel.new()
	_label.bbcode_enabled = true
	_label.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_label.offset_left = 32
	_label.offset_top = 24
	_label.offset_right = -32
	_label.offset_bottom = -24
	_label.add_theme_font_size_override("normal_font_size", 28)
	panel.add_child(_label)


func _ready() -> void:
	_draw()


func owned(row: Dictionary) -> bool:
	return not row["junk"] and int(state.inventory.get(row["id"], 0)) > 0


func buy() -> bool:
	var row: Dictionary = rows[cursor]
	notice = ""
	if owned(row):
		return false
	if ArcadeRules.tickets(state) < int(row["price"]):
		notice = "NOT ENOUGH TICKETS"
		_draw()
		return false
	ArcadeRules._take(state, ArcadeRules.TICKET_ID, int(row["price"]))
	state.add_item(row["id"])
	bought.append(row["id"])
	_draw()
	return true


func press(action: String) -> void:
	match action:
		"move_up":
			cursor = (cursor - 1 + rows.size()) % rows.size()
		"move_down":
			cursor = (cursor + 1) % rows.size()
		"interact":
			buy()
			return
		"cancel":
			closed.emit(bought)
			queue_free()
			return
	notice = ""
	_draw()


func _unhandled_input(event: InputEvent) -> void:
	for action in ["interact", "move_up", "move_down", "cancel"]:
		if event.is_action_pressed(action):
			press(action)
			get_viewport().set_input_as_handled()
			return


func _draw() -> void:
	if _label == null or state == null:
		return
	var out := "[b]PRIZE REDEMPTION[/b]    TICKETS: %d\n\n" % ArcadeRules.tickets(state)
	var shelf := false
	for i in rows.size():
		var row: Dictionary = rows[i]
		if row["junk"] and not shelf:
			shelf = true
			out += "\n"
		var price := "OWNED" if owned(row) else "%d TICKETS" % int(row["price"])
		var line := "%s%s  [color=#c9b8e8]%s[/color]" % ["> " if i == cursor else "   ", row["name"], price]
		out += line + "\n"
	if not notice.is_empty():
		out += "\n[color=#ff8a8a]%s[/color]" % notice
	_label.text = out
