class_name SovsShop
extends CanvasLayer
## The SOVS shop screen (economy Phase 1, Eurobound-it49). Reads one shop from Shops.json
## (schema in ShopCatalog), lists its priced rows by item name, and buys through
## GameState.purchase_sovs: select, pay, done. A short wallet gets the cannot-afford notice
## and nothing changes. Bar drinks show and charge ShopCatalog.price_for (the keychain
## bartender discount). No fee row, no pending state (economy_system.md §1.4, §8.4).
## Layout follows the Arcade prize counter (prize_shop.gd), which it does not touch.

signal closed(bought: Array)

## Plain functional fallback; a shop's own "cannot_afford_notice" replaces it.
const DEFAULT_CANNOT_AFFORD := "NOT ENOUGH SOVS"

var state
var shop_id := ""
var shop: Dictionary = {}
var rows: Array = []      ## ShopCatalog.rows: [{"id", "name", "price", "count", "max_stack", "bar_drink"}]
var cursor := 0
var bought: Array = []
var notice := ""

var _label: RichTextLabel


## `doc` and `items` default to the shipped Shops.json and item files; tests pass fixtures.
func setup(game_state, id: String, doc: Dictionary = {}, items: Dictionary = {}) -> void:
	state = game_state
	shop_id = id
	if doc.is_empty():
		doc = ShopCatalog.load_doc()
	if items.is_empty():
		items = ShopCatalog.item_tables()
	var shops: Dictionary = doc.get("shops", {}) if doc.get("shops") is Dictionary else {}
	if not shops.has(id):
		push_error("SovsShop: unknown shop id '%s'" % id)
		shop = {}
		rows = []
		return
	for err: String in ShopCatalog.shop_errors(id, shops[id], items):
		push_error("SovsShop: " + err)
	shop = shops[id]
	rows = ShopCatalog.rows(shop, items)
	cursor = 0
	_draw()


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
	box.border_color = Color(1.0, 0.85, 0.3)
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


func cannot_afford_notice() -> String:
	var line: Variant = shop.get("cannot_afford_notice")
	return line if line is String and not String(line).is_empty() else DEFAULT_CANNOT_AFFORD


func buy() -> bool:
	notice = ""
	if rows.is_empty():
		return false
	var row: Dictionary = rows[cursor]
	if not ShopCatalog.buy(state, row):
		notice = cannot_afford_notice()
		_draw()
		return false
	bought.append(row["id"])
	_draw()
	return true


func press(action: String) -> void:
	match action:
		"move_up":
			if not rows.is_empty():
				cursor = (cursor - 1 + rows.size()) % rows.size()
		"move_down":
			if not rows.is_empty():
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


## The screen's text (also what the tests read).
func text() -> String:
	if state == null:
		return ""
	var out := "[b]%s[/b]    %s\n\n" % [String(shop.get("display_name", "")), ShopCatalog.sovs_text(int(state.sovs))]
	for i in rows.size():
		var row: Dictionary = rows[i]
		var item_name := String(row["name"])
		if int(row["count"]) > 1:
			item_name += " x%d" % int(row["count"])
		out += "%s%s  [color=#e8d9a8]%s[/color]\n" % ["> " if i == cursor else "   ", item_name,
			ShopCatalog.sovs_text(ShopCatalog.price_for(state, row))]
	if not notice.is_empty():
		out += "\n[color=#ff8a8a]%s[/color]" % notice
	return out


func _draw() -> void:
	if _label != null:
		_label.text = text()
