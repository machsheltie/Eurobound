class_name SkeeBallScreen
extends CanvasLayer
## The skee-ball screen: for each of the nine balls the aim needle sweeps the lane (press to lock),
## then the power meter pumps (press to roll). Rules and payout live in SkeeBall. The hall pays the
## tokens before opening this and adds the tickets after `finished`.

signal finished(tickets: int)

const AIM_HZ := 0.55
const POWER_HZ := 0.8
const SHOW_ROLL_S := 0.9
const LANE_W := 360.0
const LANE_H := 560.0

var game := SkeeBall.new()
var state := "aim"
var aim := 0.0
var power := 0.0
var last_points := -1

var _t := 0.0
var _canvas: Control
var _text: Label


func _init() -> void:
	layer = 30
	_canvas = Control.new()
	_canvas.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_canvas.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_canvas.draw.connect(_draw_lane)
	add_child(_canvas)
	_text = Label.new()
	_text.set_anchors_and_offsets_preset(Control.PRESET_TOP_WIDE)
	_text.offset_top = 24
	_text.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_text.add_theme_font_size_override("font_size", 34)
	_text.add_theme_color_override("font_outline_color", Color.BLACK)
	_text.add_theme_constant_override("outline_size", 10)
	add_child(_text)
	_refresh()


func confirm() -> void:
	match state:
		"aim":
			state = "power"
			_t = 0.0
		"power":
			last_points = game.roll(aim, power)
			state = "rolled"
			_t = 0.0
		"results":
			state = "done"
			finished.emit(game.tickets())
			queue_free()
	_refresh()


func advance(delta: float) -> void:
	_t += delta
	match state:
		"aim":
			aim = sin(_t * TAU * AIM_HZ)
		"power":
			power = pingpong(_t * 2.0 * POWER_HZ, 1.0)
		"rolled":
			if _t >= SHOW_ROLL_S:
				state = "results" if game.finished() else "aim"
				_t = 0.0
				_refresh()
	_canvas.queue_redraw()


func _process(delta: float) -> void:
	advance(delta)


func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("interact"):
		confirm()
		get_viewport().set_input_as_handled()


func _refresh() -> void:
	var head := "BALL %d/%d    SCORE %d" % [mini(game.rolls.size() + 1, SkeeBall.BALLS), SkeeBall.BALLS, game.score]
	match state:
		"aim":
			_text.text = head + "\nAIM"
		"power":
			_text.text = head + "\nPOWER"
		"rolled":
			_text.text = "BALL %d/%d    SCORE %d\n+%d" % [game.rolls.size(), SkeeBall.BALLS, game.score, last_points]
		"results":
			_text.text = "SCORE %d\n\n%d TICKETS" % [game.score, game.tickets()]


func _draw_lane() -> void:
	var c := _canvas.size * 0.5 + Vector2(0, 40)
	var top := c.y - LANE_H * 0.5
	var bottom := c.y + LANE_H * 0.5
	_canvas.draw_rect(Rect2(Vector2.ZERO, _canvas.size), Color(0.02, 0.01, 0.05, 0.75))
	var lane := PackedVector2Array([
		Vector2(c.x - LANE_W * 0.5, top), Vector2(c.x + LANE_W * 0.5, top),
		Vector2(c.x + LANE_W * 0.32, bottom), Vector2(c.x - LANE_W * 0.32, bottom)])
	_canvas.draw_colored_polygon(lane, Color(0.08, 0.22, 0.16))
	# Rings, 10 outermost to 50 in the middle, and the two 100 corners.
	var hood := Vector2(c.x, top + 110)
	var radii := [100.0, 78.0, 56.0, 36.0, 18.0]
	var labels := [10, 20, 30, 40, 50]
	for i in radii.size():
		_canvas.draw_circle(hood, radii[i], Color(0.95, 0.85, 0.3) if i % 2 == 0 else Color(0.85, 0.3, 0.9), false, 4.0)
	for i in labels.size():
		_canvas.draw_string(ThemeDB.fallback_font, hood + Vector2(-12, -radii[i] + 18), str(labels[i]), HORIZONTAL_ALIGNMENT_LEFT, -1, 16)
	for sx in [-1.0, 1.0]:
		var corner := Vector2(c.x + sx * (LANE_W * 0.5 - 30), top + 30)
		_canvas.draw_circle(corner, 18.0, Color(1.0, 0.35, 0.3), false, 4.0)
		_canvas.draw_string(ThemeDB.fallback_font, corner + Vector2(-16, 6), "100", HORIZONTAL_ALIGNMENT_LEFT, -1, 16)
	# Aim needle from the bottom of the lane.
	var base := Vector2(c.x, bottom - 20)
	var tip := Vector2(c.x + aim * LANE_W * 0.45, top + 40)
	_canvas.draw_line(base, tip, Color(1, 1, 1, 0.85), 4.0)
	_canvas.draw_circle(base, 12.0, Color.WHITE)
	# Power meter beside the lane.
	var meter := Rect2(c.x + LANE_W * 0.5 + 40, bottom - 300, 30, 300)
	_canvas.draw_rect(meter, Color(0, 0, 0, 0.6))
	var shown := power if state != "aim" else 0.0
	_canvas.draw_rect(Rect2(meter.position.x, meter.end.y - meter.size.y * shown, meter.size.x, meter.size.y * shown), Color(1.0, 0.45, 0.2))
	_canvas.draw_rect(meter, Color.WHITE, false, 3.0)
