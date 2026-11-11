class_name ClawScreen
extends CanvasLayer
## A claw machine play, seen from the front: steer the claw left/right over the pit for up to
## ArcadeClaw.CONTROL_S seconds, press to drop (it drops by itself at 0). Rules live in ArcadeClaw.
## The hall pays the tokens before opening this, and reads the light before paying.

signal finished(result: Dictionary)

## How fast the claw crosses the pit (pit widths a second) and how long the drop is shown.
const CLAW_SPEED := 0.45
const DROP_S := 1.2
const BLINK_HZ := 2.0
const PIT_W := 640.0
const PIT_H := 420.0
const ITEM_FILES := ["res://assets/data/items/key_items.json", "res://assets/data/items/consumables.json"]

var machine_id := ""
var pit: Array = []
var blinking := false
var state := "steer"
var claw_x := 0.08
var time_left := ArcadeClaw.CONTROL_S
var result := {}

var _game_state
var _rng: RandomNumberGenerator
var _t := 0.0
var _canvas: Control
var _text: Label


func setup(id: String, game_state, rng: RandomNumberGenerator, light_blinking: bool) -> void:
	machine_id = id
	_game_state = game_state
	_rng = rng
	blinking = light_blinking
	pit = ArcadeClaw.layout(id, game_state, rng)


func _init() -> void:
	layer = 30
	_canvas = Control.new()
	_canvas.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_canvas.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_canvas.draw.connect(_draw_machine)
	add_child(_canvas)
	_text = Label.new()
	_text.set_anchors_and_offsets_preset(Control.PRESET_TOP_WIDE)
	_text.offset_top = 24
	_text.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_text.add_theme_font_size_override("font_size", 34)
	_text.add_theme_color_override("font_outline_color", Color.BLACK)
	_text.add_theme_constant_override("outline_size", 10)
	add_child(_text)


func _ready() -> void:
	_refresh()


## Moves the claw: -1 left, +1 right.
func steer(dir: float, delta: float) -> void:
	if state == "steer":
		claw_x = clampf(claw_x + dir * CLAW_SPEED * delta, 0.0, 1.0)


func confirm() -> void:
	match state:
		"steer":
			_drop()
		"result":
			state = "done"
			finished.emit(result)
			queue_free()
	_refresh()


func advance(delta: float) -> void:
	_t += delta
	match state:
		"steer":
			time_left -= delta
			if time_left <= 0.0:
				time_left = 0.0
				_drop()
		"drop":
			if _t >= DROP_S:
				state = "result"
	_refresh()
	_canvas.queue_redraw()


func _drop() -> void:
	result = ArcadeClaw.grab(machine_id, pit, claw_x, blinking, _game_state, _rng)
	state = "drop"
	_t = 0.0


func _process(delta: float) -> void:
	steer(Input.get_axis("move_left", "move_right"), delta)
	advance(delta)


func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("interact"):
		confirm()
		get_viewport().set_input_as_handled()


func _refresh() -> void:
	if _text == null:
		return
	match state:
		"steer":
			_text.text = "%d" % ceili(time_left)
		"drop":
			_text.text = ""
		_:
			if result.get("held", false):
				var id := String(result["id"])
				_text.text = "PRIZE: %s" % (item_name(id) if not id.is_empty() else "NAME PENDING")
			else:
				_text.text = "NO PRIZE"


## An item's display name from the item data (the id when it isn't registered).
static func item_name(id: String) -> String:
	for path: String in ITEM_FILES:
		var data = JSON.parse_string(FileAccess.get_file_as_string(path))
		if data is Dictionary:
			for group in data.values():
				if group is Dictionary and group.has(id):
					return String(group[id].get("display_name", id)).to_upper()
	return id.to_upper()


func _draw_machine() -> void:
	var c := _canvas.size * 0.5 + Vector2(0, 30)
	var box := Rect2(c.x - PIT_W * 0.5, c.y - PIT_H * 0.5, PIT_W, PIT_H)
	_canvas.draw_rect(Rect2(Vector2.ZERO, _canvas.size), Color(0.02, 0.01, 0.05, 0.75))
	_canvas.draw_rect(box.grow(18), Color(0.42, 0.22, 0.62))
	_canvas.draw_rect(box, Color(0.1, 0.08, 0.16))
	var floor_y := box.end.y - 30
	# Prizes along the bottom of the pit (grey stand-ins until the names are approved).
	var lift := clampf(_t / DROP_S, 0.0, 1.0) if state != "steer" else 0.0
	var top := box.position.y + 10
	var cx := box.position.x + claw_x * box.size.x
	var cy := top + 50
	if state != "steer":
		cy += (1.0 - absf(lift * 2.0 - 1.0)) * (floor_y - top - 90)
	for p: Dictionary in pit:
		var px := box.position.x + float(p["x"]) * box.size.x
		var w := ArcadeClaw.SLOT_HALF * 2.0 * box.size.x
		var y := floor_y
		var grabbed: bool = state != "steer" and result.get("held", false) and absf(float(p["x"]) - claw_x) <= ArcadeClaw.SLOT_HALF
		if grabbed and lift >= 0.5:
			y = cy + 34 + w * 0.8
		var col := Color(0.55, 0.55, 0.6) if String(p["id"]).is_empty() else Color(0.95, 0.75, 0.3)
		if String(p["id"]) == ArcadeClaw.RELIC_ID:
			col = Color(0.9, 0.2, 0.25)
		_canvas.draw_rect(Rect2(px - w * 0.5, y - w * 0.8, w, w * 0.8), col)
	# The claw on its cable.
	_canvas.draw_line(Vector2(cx, top), Vector2(cx, cy), Color(0.85, 0.85, 0.9), 3.0)
	_canvas.draw_rect(Rect2(cx - 18, cy - 8, 36, 12), Color(0.85, 0.85, 0.9))
	for sx in [-1.0, 1.0]:
		_canvas.draw_line(Vector2(cx + sx * 16, cy + 4), Vector2(cx + sx * 24, cy + 34), Color(0.85, 0.85, 0.9), 4.0)
	# The rigged claw's PAYOUT light.
	if machine_id == ArcadeClaw.RIGGED:
		var on := blinking and fmod(_t * BLINK_HZ, 1.0) < 0.5
		var lamp := Vector2(box.end.x - 70, box.position.y - 40)
		_canvas.draw_circle(lamp, 14.0, Color(1.0, 0.85, 0.2) if on else Color(0.25, 0.2, 0.1))
		_canvas.draw_string(ThemeDB.fallback_font, lamp + Vector2(22, 7), "PAYOUT", HORIZONTAL_ALIGNMENT_LEFT, -1, 20)
