class_name FoosballScreen
extends CanvasLayer
## The foosball screen: the table from above. Up/down slides the bros' rods, interact shoots.
## Rules and payout live in Foosball. The hall pays the tokens before opening this and adds the
## tickets after `finished`.

signal finished(tickets: int)

const KICKOFF_S := 1.2
const TABLE_PX := Vector2(1000, 600)
const BROS_COLOR := Color(1.0, 0.8, 0.25)
const HOUSE_COLOR := Color(0.75, 0.35, 1.0)

var game := Foosball.new()
var state := "kickoff"

var _t := 0.0
var _canvas: Control
var _text: Label


func _init() -> void:
	layer = 30
	_canvas = Control.new()
	_canvas.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_canvas.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_canvas.draw.connect(_draw_table)
	add_child(_canvas)
	_text = Label.new()
	_text.set_anchors_and_offsets_preset(Control.PRESET_TOP_WIDE)
	_text.offset_top = 16
	_text.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_text.add_theme_font_size_override("font_size", 34)
	_text.add_theme_color_override("font_outline_color", Color.BLACK)
	_text.add_theme_constant_override("outline_size", 10)
	add_child(_text)
	_refresh()


func confirm() -> void:
	match state:
		"play":
			game.shoot()
		"results":
			state = "done"
			finished.emit(game.tickets())
			queue_free()


## One frame: `axis` is the stick (-1 up .. 1 down).
func advance(delta: float, axis: float = 0.0) -> void:
	_t += delta
	match state:
		"kickoff":
			if _t >= KICKOFF_S:
				state = "play"
		"play":
			game.move_rods(axis, delta)
			game.step(delta)
			if game.finished():
				state = "results"
	_refresh()
	_canvas.queue_redraw()


func _process(delta: float) -> void:
	advance(delta, Input.get_axis("move_up", "move_down"))


func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("interact"):
		confirm()
		get_viewport().set_input_as_handled()


func _refresh() -> void:
	var score := "BROS %d  -  %d HOUSE" % [game.bros_goals, game.house_goals]
	match state:
		"kickoff":
			_text.text = score + "\nFIRST TO %d" % Foosball.WIN_GOALS
		"play":
			_text.text = score
		"results":
			_text.text = "%s\n%s\n%d TICKETS" % [score, "BROS WIN" if game.bros_won() else "HOUSE WINS", game.tickets()]


func _draw_table() -> void:
	var origin := (_canvas.size - TABLE_PX) * 0.5 + Vector2(0, 30)
	var k := TABLE_PX.x / Foosball.FIELD.x
	_canvas.draw_rect(Rect2(Vector2.ZERO, _canvas.size), Color(0.02, 0.01, 0.05, 0.75))
	_canvas.draw_rect(Rect2(origin, TABLE_PX), Color(0.1, 0.45, 0.2))
	_canvas.draw_rect(Rect2(origin, TABLE_PX), Color.WHITE, false, 4.0)
	_canvas.draw_line(origin + Vector2(TABLE_PX.x * 0.5, 0), origin + Vector2(TABLE_PX.x * 0.5, TABLE_PX.y), Color(1, 1, 1, 0.4), 2.0)
	var mouth := Foosball.GOAL_HALF * k
	var mid := origin.y + TABLE_PX.y * 0.5
	_canvas.draw_rect(Rect2(origin.x - 14, mid - mouth, 14, mouth * 2), BROS_COLOR)
	_canvas.draw_rect(Rect2(origin.x + TABLE_PX.x, mid - mouth, 14, mouth * 2), HOUSE_COLOR)
	for i in Foosball.RODS.size():
		var x: float = origin.x + float(Foosball.RODS[i][0]) * k
		_canvas.draw_line(Vector2(x, origin.y - 20), Vector2(x, origin.y + TABLE_PX.y + 20), Color(0.8, 0.8, 0.85), 4.0)
	for side: String in ["bros", "house"]:
		for m in game.men(side):
			_canvas.draw_circle(origin + m * k, Foosball.MAN_RADIUS * k, BROS_COLOR if side == "bros" else HOUSE_COLOR)
	_canvas.draw_circle(origin + game.ball * k, Foosball.BALL_RADIUS * k, Color.WHITE)
