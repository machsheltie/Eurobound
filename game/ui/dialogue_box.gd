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
## GameState (optional). While a bro has Green Fairy Confusion a choice lands on a random option
## (author round v43, fs_confusion_dialogue). Scenes set this; null = no field statuses.
var field_state = null
var choice_rng: RandomNumberGenerator = null
var speaker := ""
var text := ""
## Status ids of the bro who is speaking (empty for anyone else): what the dialogue fields read.
var _speed_ids: Array = []
## While a "replace" status is live, the pool lines shown in place of the options (else empty).
var _pool_picks: Array = []

## The box's share of the screen width.
const WIDTH_FRACTION := 0.5

var _panel: Panel
var _who: Label
var _line: Label


func _init() -> void:
	layer = 35
	_panel = Panel.new()
	# Half the screen wide, centred at the bottom (author, 2026-11-15: "maybe half that width. It
	# shouldn't be as wide as the screen").
	_panel.set_anchors_and_offsets_preset(Control.PRESET_CENTER_BOTTOM)
	_panel.anchor_left = 0.5 - WIDTH_FRACTION * 0.5
	_panel.anchor_right = 0.5 + WIDTH_FRACTION * 0.5
	_panel.offset_left = 0
	_panel.offset_right = 0
	_panel.offset_top = -300
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
	_speed_ids = _bro_status_ids(who)
	text = _filtered(line)
	mode = "say"
	_draw()
	await _next


func choose(choices: Array) -> int:
	options = choices
	cursor = 0
	_pool_picks = _replacement_lines(choices.size())
	mode = "choose"
	_draw()
	await _next
	cursor = FieldStatus.choice_index(field_state, cursor, options.size(), choice_rng)
	return cursor


## Eurobound-izct. Scale for the line's reveal speed from the speaking bro's statuses
## (field.text_speed_mult); 1.0 with no status, a null value, or reduced motion.
## TODO(Eurobound-izct): the box shows a whole line at once, so nothing reads this yet. A typewriter
## needs a base characters-per-second that no ruling gives; it is not invented here.
func text_speed_mult() -> float:
	if GameSettings.reduced_motion(field_state):
		return 1.0
	return StatusTable.text_speed_mult(_speed_ids)


## What the choice rows show: the pool lines while a "replace" status is live, else the options.
func shown_options() -> Array:
	return _pool_picks if _pool_picks.size() == options.size() and not _pool_picks.is_empty() else options


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
			rows.append(("> " if i == cursor else "   ") + String(shown_options()[i]))
		_line.text = "\n".join(rows)
	else:
		_who.text = speaker
		_line.text = text


## Live status ids of the party member named `who` (display name or id) plus the whole party's.
## Empty when `who` is not a bro or there is no field state.
func _bro_status_ids(who: String) -> Array:
	if field_state == null or not ("party" in field_state):
		return []
	for member in field_state.party:
		if member is Dictionary and (String(member.get("display_name", "")) == who or String(member.get("id", "")) == who):
			return FieldStatus.list(field_state, String(member.get("id", "")))
	return []


## field.text_filter trailing_ellipsis: the bro's line trails off. Closing periods and commas give
## way to "..." ; a line already ending in an ellipsis is left alone.
## TODO(Eurobound-izct): the exact trim rule is not ruled (the cue is only "bro..."): see the bead.
func _filtered(line: String) -> String:
	if _speed_ids.is_empty() or not StatusTable.has_text_filter(_speed_ids, "trailing_ellipsis"):
		return line
	if line.ends_with("...") or line.ends_with("…"):
		return line
	var end := line.length()
	while end > 0 and (line[end - 1] == "." or line[end - 1] == "," or line[end - 1] == " "):
		end -= 1
	return line.substr(0, end) + "..."


## field.choices mode "replace": one pool line per option, from the speaking... the active bro's
## statuses. The pool is the author's (null today), so nothing shows unless data provides it.
## Lines are drawn without repeats while the pool lasts.
## TODO(Eurobound-izct): which bro's status applies when a choice has no speaker is not ruled; this
## reads the last bro who spoke.
func _replacement_lines(count: int) -> Array:
	var pool := StatusTable.choices_replace_pool(_speed_ids)
	if pool.is_empty() or count <= 0:
		return []
	if choice_rng == null:
		choice_rng = RandomNumberGenerator.new()
		choice_rng.randomize()
	var bag: Array = []
	var out: Array = []
	for i in count:
		if bag.is_empty():
			bag = pool.duplicate()
		out.append(bag.pop_at(choice_rng.randi_range(0, bag.size() - 1)))
	return out
