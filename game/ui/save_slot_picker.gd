class_name SaveSlotPicker
extends CanvasLayer
## The save-slot picker (Eurobound-x2ws). The author: "A slot picker every time you save (hotspot or
## bed) and in Load" (Eurobound Desk Eurobound-x2ws-q3); 3 slots (NEXT_WORK.md:892).
## Rows: Slot 1-3 (each "Empty" or what its save holds) and Cancel. Await `pick()`: the slot number,
## or 0 when cancelled. In Load an empty slot can't be picked. Styled like the field menu's panels.
## Saving goes through SaveSystem.save_with_picker(); Load is FieldMenu's.

signal picked(slot: int)

## Plain functional labels (the only words this screen may show on its own).
const LABEL_SLOT := "Slot %d"
const LABEL_EMPTY := "Empty"
const LABEL_CANCEL := "Cancel"

## --- Words waiting on the author --------------------------------------------------------------
## Flavour lines are never invented by agents. Each stays "" until the author (or the Writers'
## Room, if the author sends it there) supplies it: Eurobound Desk Eurobound-x2ws-q4. While a line
## is "" its step is skipped.
const PENDING_LINES := {
	"title_save": "",         ## heading over the picker when saving at a hotspot or bed
	"title_load": "",         ## heading over the picker in Load
	"overwrite_confirm": "",  ## asked before saving over a slot that holds a save
	"overwrite_yes": "",      ## the two answers to overwrite_confirm
	"overwrite_no": "",
	"saved": "",              ## said once the save is written
}
## Screen file -> the place name a filled slot shows. Empty until the author gives the names (same
## Desk question); until then a slot shows no place, never a file name.
const LOCATION_NAMES := {}

var saver
var purpose := "save"     ## "save" or "load"
var cursor := 0
var mode := "slots"       ## "slots", or "confirm" (overwrite question, only once it has words)
var confirm_cursor := 0
var _infos: Array = []

var _title: Label
var _body: RichTextLabel


## `the_saver`: a SaveSystem (has slot_info). `what`: "save" or "load".
func setup(the_saver, what: String) -> void:
	saver = the_saver
	purpose = what
	refresh()


func refresh() -> void:
	_infos = []
	if saver != null:
		for slot in range(1, int(saver.SLOT_COUNT) + 1):
			_infos.append(saver.slot_info(slot))
	_draw()


func pick() -> int:
	return await picked


func _init() -> void:
	layer = 45
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.45)
	dim.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	add_child(dim)
	var p := Panel.new()
	var box := StyleBoxFlat.new()
	box.bg_color = FieldMenu.PANEL_BG
	box.border_color = FieldMenu.VIOLET
	box.set_border_width_all(4)
	box.set_corner_radius_all(8)
	p.add_theme_stylebox_override("panel", box)
	p.anchor_left = 0.3
	p.anchor_right = 0.7
	p.anchor_top = 0.28
	p.anchor_bottom = 0.72
	add_child(p)
	_title = Label.new()
	_title.position = Vector2(26, 18)
	_title.add_theme_font_size_override("font_size", 30)
	_title.add_theme_color_override("font_color", FieldMenu.GOLD)
	p.add_child(_title)
	_body = RichTextLabel.new()
	_body.bbcode_enabled = true
	_body.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_body.offset_left = 26
	_body.offset_top = 70
	_body.offset_right = -26
	_body.offset_bottom = -18
	_body.add_theme_font_size_override("normal_font_size", 30)
	p.add_child(_body)


func is_empty(slot: int) -> bool:
	return slot < 1 or slot > _infos.size() or Dictionary(_infos[slot - 1]).is_empty()


## The four rows as shown, without the cursor mark.
func row_labels() -> Array:
	var out := []
	for i in _infos.size():
		var info: Dictionary = _infos[i]
		var row := LABEL_SLOT % (i + 1)
		if info.is_empty():
			row += "   " + LABEL_EMPTY
		else:
			var place := String(LOCATION_NAMES.get(String(info.get("scene", "")), ""))
			if place != "":
				row += "   " + place
			row += "   %s   SOVS %d" % [String(info.get("time", "")), int(info.get("sovs", 0))]
		out.append(row)
	out.append(LABEL_CANCEL)
	return out


func press(action: String) -> void:
	if mode == "confirm":
		_press_confirm(action)
		return
	var count := _infos.size() + 1
	if action == "move_up":
		cursor = posmod(cursor - 1, count)
	elif action == "move_down":
		cursor = posmod(cursor + 1, count)
	elif action in ["cancel", "menu"]:
		_finish(0)
		return
	elif action == "interact":
		var slot := cursor + 1
		if cursor == _infos.size():
			_finish(0)
			return
		if purpose == "load" and is_empty(slot):
			return
		if purpose == "save" and not is_empty(slot) and String(PENDING_LINES["overwrite_confirm"]) != "":
			mode = "confirm"
			confirm_cursor = 1
		else:
			_finish(slot)
			return
	_draw()


func _press_confirm(action: String) -> void:
	if action in ["move_up", "move_down"]:
		confirm_cursor = 1 - confirm_cursor
	elif action in ["cancel", "menu"] or (action == "interact" and confirm_cursor == 1):
		mode = "slots"
	elif action == "interact":
		_finish(cursor + 1)
		return
	_draw()


func _finish(slot: int) -> void:
	picked.emit(slot)
	queue_free()


func _unhandled_input(event: InputEvent) -> void:
	for action in ["menu", "cancel", "interact", "move_up", "move_down"]:
		if event.is_action_pressed(action):
			press(action)
			get_viewport().set_input_as_handled()
			return


func _draw() -> void:
	if _body == null:
		return
	_title.text = String(PENDING_LINES["title_load" if purpose == "load" else "title_save"])
	var gold := FieldMenu.GOLD.to_html(false)
	var lines := []
	if mode == "confirm":
		lines.append(String(PENDING_LINES["overwrite_confirm"]))
		for i in 2:
			var word := String(PENDING_LINES["overwrite_yes" if i == 0 else "overwrite_no"])
			lines.append(("[color=#%s]> %s[/color]" % [gold, word]) if i == confirm_cursor else "   " + word)
	else:
		var rows := row_labels()
		for i in rows.size():
			var dim := purpose == "load" and i < _infos.size() and is_empty(i + 1)
			var color := gold if i == cursor else ("7a6f8a" if dim else "ffffff")
			lines.append("[color=#%s]%s%s[/color]" % [color, "> " if i == cursor else "   ", rows[i]])
	_body.text = "\n".join(lines)
