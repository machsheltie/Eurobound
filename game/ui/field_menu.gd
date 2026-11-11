class_name FieldMenu
extends CanvasLayer
## The field menu (round v36, author: the nine sections as proposed in ad's menu_proposal.md).
## Esc / Start opens it while the bros are free to move; the clock doesn't move while it's up.
## Root: the section list (left), the three party cards (middle), and the info box with the SOVS
## line and Lord Pilsner's watch (the only clock in the game: round v34 clock_watch = watch_menu).
## Rulings: no Save (round v36 menu_save = no_save: Load / Quit only); the second bar is Bravado
## (menu_bravado); the intoxication tier sits on each bro's card (menu_intox = card); the Equip
## slots are the equipment template's (menu_equip = template); the watch sits in the shared box and
## can't be unequipped; skills are read-only in Status; no Achievements, Street Rep, ICQ log or
## map; plain labels (menu_rest = defaults).
## Sections whose systems don't exist yet (equipment, NFTs, quests, the passport) open empty.

signal closed

const SECTIONS := ["Items", "Equip", "Status", "Party", "Wallet", "Brewery Passport", "Quest Log",
	"Settings", "Load / Quit"]
const PASSPORT_ITEM := "brewery_passport_book"
const EQUIP_SLOTS := ["Weapon", "Head", "Torso", "Legs", "Feet", "Necklace", "Ring", "Watch / Bracelet",
	"Phone", "Accessory"]
const ITEM_FILES := {"consumables": "res://assets/data/items/consumables.json",
	"key_items": "res://assets/data/items/key_items.json", "equipment": "res://assets/data/items/equipment.json"}
const SKILLS := "res://assets/data/skills/party_abilities.json"
const BRO_COLORS := [Color(0.55, 0.25, 0.75), Color(0.2, 0.55, 0.45), Color(0.75, 0.4, 0.15)]
const PANEL_BG := Color(0.04, 0.02, 0.08, 0.92)
const VIOLET := Color(0.62, 0.38, 0.9)
const GOLD := Color(1.0, 0.85, 0.3)

var state
var section := 0
var mode := "root"        ## "root", a section name, "use_on" (picking a bro for an item), "swap"
var cursor := 0
var picked := -1          ## Party: the first bro picked for a swap; Items: the item row
var notice := ""

var _list: RichTextLabel
var _body: RichTextLabel
var _help: Label
var _sovs: Label
var _watch: Label


func setup(game_state) -> void:
	state = game_state


func _init() -> void:
	layer = 40
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.45)
	dim.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	add_child(dim)
	_list = _panel_text(Rect2(0.026, 0.07, 0.218, 0.905), 30)
	_body = _panel_text(Rect2(0.264, 0.07, 0.71, 0.65), 26)
	_help = Label.new()
	var help_panel := _panel(Rect2(0.264, 0.755, 0.355, 0.22))
	_help.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_help.offset_left = 22
	_help.offset_top = 18
	_help.offset_right = -22
	_help.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_help.add_theme_font_size_override("font_size", 22)
	_help.add_theme_color_override("font_color", Color(0.75, 0.7, 0.85))
	help_panel.add_child(_help)
	var info := _panel(Rect2(0.619, 0.755, 0.355, 0.22))
	_sovs = Label.new()
	_sovs.position = Vector2(26, 16)
	_sovs.add_theme_font_size_override("font_size", 30)
	info.add_child(_sovs)
	var who := Label.new()
	who.text = "Lord Pilsner's watch"
	who.position = Vector2(26, 98)
	who.add_theme_font_size_override("font_size", 18)
	who.add_theme_color_override("font_color", Color(0.75, 0.7, 0.85))
	info.add_child(who)
	# The watch: a black digital sports watch with a grey-green LCD (sprite note, lord_pilsner.txt).
	var strap := Panel.new()
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.08, 0.08, 0.09)
	sb.set_corner_radius_all(14)
	strap.add_theme_stylebox_override("panel", sb)
	strap.anchor_left = 1.0
	strap.anchor_right = 1.0
	strap.offset_left = -250
	strap.offset_right = -24
	strap.offset_top = 64
	strap.offset_bottom = 150
	info.add_child(strap)
	var lcd := Panel.new()
	var lb := StyleBoxFlat.new()
	lb.bg_color = Color(0.62, 0.66, 0.52)
	lb.set_corner_radius_all(6)
	lcd.add_theme_stylebox_override("panel", lb)
	lcd.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	lcd.offset_left = 16
	lcd.offset_right = -16
	lcd.offset_top = 12
	lcd.offset_bottom = -12
	strap.add_child(lcd)
	_watch = Label.new()
	_watch.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_watch.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_watch.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	_watch.add_theme_font_size_override("font_size", 44)
	_watch.add_theme_color_override("font_color", Color(0.1, 0.12, 0.08))
	lcd.add_child(_watch)


func _ready() -> void:
	_draw()


func _panel(r: Rect2) -> Panel:
	var p := Panel.new()
	var box := StyleBoxFlat.new()
	box.bg_color = PANEL_BG
	box.border_color = VIOLET
	box.set_border_width_all(4)
	box.set_corner_radius_all(8)
	p.add_theme_stylebox_override("panel", box)
	p.anchor_left = r.position.x
	p.anchor_top = r.position.y
	p.anchor_right = r.end.x
	p.anchor_bottom = r.end.y
	add_child(p)
	return p


func _panel_text(r: Rect2, size: int) -> RichTextLabel:
	var p := _panel(r)
	var t := RichTextLabel.new()
	t.bbcode_enabled = true
	t.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	t.offset_left = 24
	t.offset_top = 20
	t.offset_right = -24
	t.offset_bottom = -16
	t.add_theme_font_size_override("normal_font_size", size)
	t.add_theme_font_size_override("bold_font_size", size + 4)
	p.add_child(t)
	return t


# --- data -------------------------------------------------------------------------------------

func sections() -> Array:
	var has_passport := int(state.inventory.get(PASSPORT_ITEM, 0)) > 0
	return SECTIONS.filter(func(s: String) -> bool: return s != "Brewery Passport" or has_passport)


static func _json(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return {}
	var d = JSON.parse_string(FileAccess.get_file_as_string(path))
	return d if d is Dictionary else {}


## Every item definition by id, tagged with the file it came from.
static func item_defs() -> Dictionary:
	var out := {}
	for group: String in ITEM_FILES.keys():
		var doc := _json(ITEM_FILES[group])
		var items: Dictionary = doc.get(group, {})
		for id: String in items.keys():
			var it: Dictionary = Dictionary(items[id]).duplicate()
			it["_group"] = group
			out[id] = it
	return out


## The bag: [{"id", "name", "count", "group", "def"}], consumables first, then key items. Currency
## (tokens, tickets) and items with no definition stay out.
func bag() -> Array:
	var defs := item_defs()
	var out := []
	for id: String in state.inventory.keys():
		if not defs.has(id) or int(state.inventory[id]) <= 0:
			continue
		var d: Dictionary = defs[id]
		out.append({"id": id, "name": String(d.get("display_name", id)), "count": int(state.inventory[id]),
			"group": String(d["_group"]), "def": d})
	out.sort_custom(func(a: Dictionary, b: Dictionary) -> bool:
		if a["group"] != b["group"]:
			return a["group"] == "consumables"
		return String(a["name"]) < String(b["name"]))
	return out


static func usable_in_field(def: Dictionary) -> bool:
	return def.get("_group", "") == "consumables" and (int(def.get("heal_hp", 0)) > 0 or int(def.get("heal_bravado", 0)) > 0)


## Uses a field consumable on one bro: HP and Bravado, capped at their maximums.
func use_on(item_id: String, member_index: int) -> bool:
	var defs := item_defs()
	var d: Dictionary = defs.get(item_id, {})
	if not usable_in_field(d) or int(state.inventory.get(item_id, 0)) <= 0:
		return false
	var m: Dictionary = state.party[member_index]
	m["hp"] = mini(int(m["max_hp"]), int(m["hp"]) + int(d.get("heal_hp", 0)))
	m["bravado"] = mini(int(m["max_bravado"]), int(m["bravado"]) + int(d.get("heal_bravado", 0)))
	state.inventory[item_id] = int(state.inventory[item_id]) - 1
	if int(state.inventory[item_id]) <= 0:
		state.inventory.erase(item_id)
	return true


func swap_bros(a: int, b: int) -> void:
	var tmp = state.party[a]
	state.party[a] = state.party[b]
	state.party[b] = tmp


# --- input ------------------------------------------------------------------------------------

func press(action: String) -> void:
	notice = ""
	var secs := sections()
	match mode:
		"root":
			if action == "move_up":
				section = posmod(section - 1, secs.size())
			elif action == "move_down":
				section = posmod(section + 1, secs.size())
			elif action == "interact":
				mode = secs[section]
				cursor = 0
				picked = -1
			elif action in ["cancel", "menu"]:
				close()
				return
		"Items":
			var rows := bag()
			if action in ["move_up", "move_down"] and not rows.is_empty():
				cursor = posmod(cursor + (1 if action == "move_down" else -1), rows.size())
			elif action == "interact" and not rows.is_empty():
				if usable_in_field(rows[cursor]["def"]):
					picked = cursor
					mode = "use_on"
					cursor = 0
			elif action in ["cancel", "menu"]:
				mode = "root"
		"use_on":
			if action in ["move_up", "move_down"]:
				cursor = posmod(cursor + (1 if action == "move_down" else -1), state.party.size())
			elif action == "interact":
				var rows := bag()
				if picked < rows.size():
					use_on(String(rows[picked]["id"]), cursor)
				mode = "Items"
				cursor = mini(picked, maxi(bag().size() - 1, 0))
			elif action in ["cancel", "menu"]:
				mode = "Items"
				cursor = picked
		"Status", "Equip":
			if action in ["move_up", "move_down"]:
				cursor = posmod(cursor + (1 if action == "move_down" else -1), state.party.size())
			elif action in ["cancel", "menu"]:
				mode = "root"
		"Party":
			if action in ["move_up", "move_down"]:
				cursor = posmod(cursor + (1 if action == "move_down" else -1), state.party.size())
			elif action == "interact":
				if picked < 0:
					picked = cursor
				else:
					swap_bros(picked, cursor)
					picked = -1
			elif action in ["cancel", "menu"]:
				if picked >= 0:
					picked = -1
				else:
					mode = "root"
		"Load / Quit":
			if action in ["move_up", "move_down"]:
				cursor = 1 - cursor
			elif action == "interact":
				if cursor == 0:
					_load()
				else:
					get_tree().quit()
				return
			elif action in ["cancel", "menu"]:
				mode = "root"
		_:
			if action in ["cancel", "menu"]:
				mode = "root"
	_draw()


func _unhandled_input(event: InputEvent) -> void:
	for action in ["menu", "cancel", "interact", "move_up", "move_down"]:
		if event.is_action_pressed(action):
			press(action)
			get_viewport().set_input_as_handled()
			return


func close() -> void:
	closed.emit()
	queue_free()


func _load() -> void:
	var save := get_tree().root.get_node_or_null("SaveSystem")
	if save == null or not save.has_save():
		notice = "NO SAVE"
		_draw()
		return
	save.load_game(state)
	var path := String(state.current_scene_path)
	close()
	if ResourceLoader.exists(path):
		get_tree().change_scene_to_file.call_deferred(path)


# --- drawing ----------------------------------------------------------------------------------

func _draw() -> void:
	if _list == null or state == null:
		return
	var secs := sections()
	section = clampi(section, 0, secs.size() - 1)
	var rows := []
	for i in secs.size():
		var on: bool = i == section
		rows.append("[color=#%s]%s%s[/color]" % [GOLD.to_html(false) if on else "ffffff", "> " if on else "   ", secs[i]])
	_list.text = "\n".join(rows)
	_sovs.text = "SOVS    %d" % int(state.sovs)
	_watch.text = GameClock.watch_text(state)
	_help.text = notice
	match mode:
		"root":
			_body.text = _party_cards()
		"Items", "use_on":
			_body.text = _items_text()
		"Status":
			_body.text = _status_text(cursor)
		"Equip":
			_body.text = _equip_text(cursor)
		"Party":
			_body.text = _party_text()
		"Wallet":
			_body.text = _wallet_text()
		"Quest Log":
			_body.text = "[b]Quest Log[/b]\n\n—"
		"Brewery Passport":
			_body.text = "[b]Brewery Passport[/b]\n\n—"
		"Settings":
			_body.text = _settings_text()
		"Load / Quit":
			_body.text = "[b]Load / Quit[/b]\n\n%sLoad\n%sQuit" % ["> " if cursor == 0 else "   ", "> " if cursor == 1 else "   "]


static func _bar(value: int, most: int, color: Color, width := 20) -> String:
	var n := 0 if most <= 0 else clampi(roundi(float(value) / most * width), 0, width)
	return "[color=#%s]%s[/color][color=#3a3448]%s[/color]" % [color.to_html(false), "█".repeat(n), "█".repeat(width - n)]


func _card(i: int, m: Dictionary) -> String:
	var name := String(m.get("display_name", m.get("id", "")))
	var lines := "[color=#%s]▌[/color][b]%s[/b]   Lv %s\n" % [BRO_COLORS[i % 3].to_html(false), name, str(m.get("level", 1))]
	lines += "   HP       %s  %d/%d\n" % [_bar(int(m["hp"]), int(m["max_hp"]), Color(0.45, 0.85, 0.5)), int(m["hp"]), int(m["max_hp"])]
	lines += "   Bravado  %s  %d/%d\n" % [_bar(int(m["bravado"]), int(m["max_bravado"]), Color(0.9, 0.65, 0.2)), int(m["bravado"]), int(m["max_bravado"])]
	var extra := []
	var statuses: Dictionary = m.get("lasting_statuses", {})
	if not statuses.is_empty():
		extra.append(", ".join(statuses.keys().map(func(s): return String(s).replace("_", " ").capitalize())))
	if m.has("intoxication_tier"):
		extra.append(String(m["intoxication_tier"]))
	if not extra.is_empty():
		lines += "   [color=#c9b8e8]%s[/color]\n" % "  ·  ".join(extra)
	return lines


func _party_cards() -> String:
	var out := []
	for i in state.party.size():
		out.append(_card(i, state.party[i]))
	return "\n".join(out)


func _items_text() -> String:
	var rows := bag()
	if rows.is_empty():
		return "[b]Items[/b]\n\n—"
	var out := "[b]Items[/b]\n\n"
	var key_header := false
	for i in rows.size():
		var r: Dictionary = rows[i]
		if r["group"] != "consumables" and not key_header:
			key_header = true
			out += "\n[color=#c9b8e8]Key Items[/color]\n"
		var on: bool = i == (picked if mode == "use_on" else cursor)
		out += "%s%s  x%d\n" % ["> " if on else "   ", r["name"], int(r["count"])]
	if mode == "use_on":
		out += "\n"
		for i in state.party.size():
			out += "%s%s\n" % ["> " if i == cursor else "   ", String(state.party[i].get("display_name", state.party[i]["id"]))]
	elif cursor < rows.size():
		out += "\n[color=#c9b8e8]%s[/color]" % String(rows[cursor]["def"].get("description", ""))
	return out


func _status_text(i: int) -> String:
	var m: Dictionary = state.party[i]
	var out := "[b]%s[/b]   Lv %s   XP %s\n\n" % [String(m.get("display_name", m["id"])), str(m.get("level", 1)), str(m.get("xp", 0))]
	out += "HP %d/%d    Bravado %d/%d\n" % [int(m["hp"]), int(m["max_hp"]), int(m["bravado"]), int(m["max_bravado"])]
	for pair in [["Offense", "offense"], ["Defense", "defense"], ["Speed", "speed"], ["Charm", "charm"], ["Luck", "luck"], ["Grit", "grit"]]:
		out += "%s  %s\n" % [pair[0], str(m.get(pair[1], 0))]
	var abilities: Dictionary = _json(SKILLS).get("abilities", {})
	var names := Array(m.get("skills", [])).map(func(s): return String(Dictionary(abilities.get(s, {})).get("display_name", s)))
	out += "\nSkills  %s" % (", ".join(names) if not names.is_empty() else "—")
	var statuses: Dictionary = m.get("lasting_statuses", {})
	if not statuses.is_empty():
		out += "\nStatus  %s" % ", ".join(statuses.keys().map(func(s): return String(s).replace("_", " ").capitalize()))
	return out


func _equip_text(i: int) -> String:
	var m: Dictionary = state.party[i]
	var gear: Dictionary = m.get("equipment", {})
	var out := "[b]%s[/b]\n\n" % String(m.get("display_name", m["id"]))
	for slot: String in EQUIP_SLOTS:
		out += "%s  %s\n" % [slot, String(gear.get(slot.to_lower(), "—"))]
	return out


func _party_text() -> String:
	var out := "[b]Party[/b]\n\n"
	for i in state.party.size():
		var mark := "> " if i == cursor else "   "
		var pick := "  *" if i == picked else ""
		out += "%s%s%s\n" % [mark, String(state.party[i].get("display_name", state.party[i]["id"])), pick]
	return out


func _wallet_text() -> String:
	var out := "[b]SOVS[/b]  %d\n\n[b]THE LEGACY VAULT[/b]\n—" % int(state.sovs)
	if bool(state.flags.get("has_inspected_first_crypto_trash", false)):
		out += "\n\n[b]Bagholder Assets[/b]\n—"
	return out


func _settings_text() -> String:
	return "[b]Settings[/b]\n\nControls\nMove  WASD / arrows / left stick\nConfirm  E / Space / Enter / A\nBack  Esc / Backspace / Q / B\nMenu  Esc / Start"
