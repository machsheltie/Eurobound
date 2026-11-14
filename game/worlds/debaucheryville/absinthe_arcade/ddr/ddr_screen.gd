class_name DdrScreen
extends CanvasLayer
## The DDR dance-off screen: difficulty select (stuck on EXPERT), the player picks which bro plays
## (the other two are game-controlled; ledger 2026-11-09), then four arrow lanes scroll up to the
## receptors like real DDR, then the results and the ticket payout (0-30 by score).
## The hall pays the tokens before opening this and adds the tickets after `finished`.

signal finished(tickets: int, bro: String)

const BROS := ["lord_pilsner", "chadwick", "bradley"]
const BRO_NAMES := {"lord_pilsner": "LORD PILSNER", "chadwick": "CHADWICK", "bradley": "BRADLEY"}
const LANE_ACTIONS := ["move_left", "move_down", "move_up", "move_right"]
## Seconds of song a note is on screen before it reaches the receptors.
const SCROLL_LEAD_S := 1.6
const LANE_GAP_PX := 96.0
const RECEPTOR_Y := 120.0
const LANE_COLORS := [Color(0.85, 0.3, 1.0), Color(0.25, 0.75, 1.0), Color(0.3, 1.0, 0.45), Color(1.0, 0.35, 0.3)]
## Arrow rotation per lane: left, down, up, right.
const LANE_ANGLES := [PI, PI * 0.5, -PI * 0.5, 0.0]

var state := "difficulty"
var bro := "lord_pilsner"
var difficulty := DdrDifficulty.new()
var chart: DdrChart
var judge: DdrJudge

var _bro_index := 0
var _clock := 0.0
var _last_judgement := ""
var _song_id := ""
var _song_playing := false
var _canvas: Control
var _text: Label


func _init() -> void:
	layer = 30
	_canvas = Control.new()
	_canvas.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_canvas.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_canvas.draw.connect(_draw_lanes)
	add_child(_canvas)
	_text = Label.new()
	_text.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_text.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_text.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	_text.add_theme_font_size_override("font_size", 40)
	_text.add_theme_color_override("font_outline_color", Color.BLACK)
	_text.add_theme_constant_override("outline_size", 10)
	add_child(_text)


## Opens the screen for one song.
func start(song: DdrChart) -> void:
	chart = song
	judge = DdrJudge.new(chart)
	state = "difficulty"
	_refresh()


## Song time in seconds: the audio's own clock when the song is playing, else a plain timer.
func song_time() -> float:
	var player := Audio.music_player()
	if player != null and player.playing and Audio.current_music() == _song_id:
		return player.get_playback_position() + AudioServer.get_time_since_last_mix() - AudioServer.get_output_latency()
	return _clock


func confirm() -> void:
	match state:
		"difficulty":
			state = "bro"
		"bro":
			bro = BROS[_bro_index]
			_begin_song()
		"results":
			state = "done"
			finished.emit(judge.tickets(), bro)
			queue_free()
	_refresh()


func move_cursor(delta: int) -> void:
	match state:
		"difficulty":
			difficulty.move(delta)
		"bro":
			_bro_index = wrapi(_bro_index + delta, 0, BROS.size())
	_refresh()


## A step on `lane` (0 left, 1 down, 2 up, 3 right) right now.
func press_lane(lane: int) -> String:
	if state != "play":
		return ""
	var j := judge.hit(lane, song_time())
	if j != "":
		_last_judgement = j
	return j


## Moves the song on by `delta` seconds when there's no audio (and runs the judge either way).
func advance(delta: float) -> void:
	if state != "play":
		return
	if not _song_playing:
		_clock += delta
	if judge.update(song_time()) > 0:
		_last_judgement = "MISS"
	if judge.finished() and song_time() > chart.length_s() + 1.0:
		Audio.stop_music(0.0)
		_song_playing = false
		state = "results"
		_refresh()
	_canvas.queue_redraw()


func _begin_song() -> void:
	state = "play"
	_clock = -1.0  # a second of lead-in before the song's zero
	# The song is an Audio music track; its id is the audio file's name. Played from the start, no fade.
	_song_id = chart.audio_path.get_file().get_basename()
	_song_playing = not _song_id.is_empty() and Audio.has_sound(_song_id) and Audio.play_music(_song_id, 0.0)
	_canvas.queue_redraw()


func _process(delta: float) -> void:
	advance(delta)
	if state == "play":
		_text.text = "%s\n%s" % [_last_judgement, "" if judge.combo < 4 else "%d COMBO" % judge.combo]


func _unhandled_input(event: InputEvent) -> void:
	if state == "play":
		for lane in LANE_ACTIONS.size():
			if event.is_action_pressed(LANE_ACTIONS[lane]):
				press_lane(lane)
				get_viewport().set_input_as_handled()
				return
		return
	if event.is_action_pressed("move_left") or event.is_action_pressed("move_up"):
		move_cursor(-1)
	elif event.is_action_pressed("move_right") or event.is_action_pressed("move_down"):
		move_cursor(1)
	elif event.is_action_pressed("interact"):
		confirm()
	else:
		return
	get_viewport().set_input_as_handled()


func _refresh() -> void:
	match state:
		"difficulty":
			var row := []
			for level: String in DdrDifficulty.LEVELS:
				row.append("[ %s ]" % level if level == difficulty.selected() else level)
			_text.text = "%s\n\n%s" % [chart.title, "   ".join(row)]
		"bro":
			_text.text = "WHO DANCES?\n\n<  %s  >" % BRO_NAMES[BROS[_bro_index]]
		"results":
			var c := judge.counts
			_text.text = "PERFECT %d   GREAT %d   GOOD %d   MISS %d\n\n%d TICKETS" % [
				c["PERFECT"], c["GREAT"], c["GOOD"], c["MISS"], judge.tickets()]
	_canvas.queue_redraw()


func _draw_lanes() -> void:
	if chart == null:
		return
	if state != "play":
		# Menus: a dark band behind the text so it reads over the hall's art.
		var band := Rect2(0, _canvas.size.y * 0.5 - 130, _canvas.size.x, 260)
		_canvas.draw_rect(band, Color(0.02, 0.01, 0.05, 0.8))
		return
	var vw := _canvas.size.x
	var vh := _canvas.size.y
	var left := vw * 0.5 - LANE_GAP_PX * 1.5
	var px_per_s := (vh - RECEPTOR_Y) / SCROLL_LEAD_S
	var t := song_time()
	_canvas.draw_rect(Rect2(left - LANE_GAP_PX * 0.6, 0, LANE_GAP_PX * 4.2, vh), Color(0, 0, 0, 0.45))
	for lane in 4:
		_arrow(Vector2(left + lane * LANE_GAP_PX, RECEPTOR_Y), lane, Color(1, 1, 1, 0.35), false)
	for i in chart.notes.size():
		var n: Dictionary = chart.notes[i]
		var dt := float(n["time"]) - t
		if dt < -0.2 or dt > SCROLL_LEAD_S:
			continue
		if judge._judged[i]:
			continue
		var lane := int(n["lane"])
		_arrow(Vector2(left + lane * LANE_GAP_PX, RECEPTOR_Y + dt * px_per_s), lane, LANE_COLORS[lane], true)


func _arrow(center: Vector2, lane: int, color: Color, filled: bool) -> void:
	var s := LANE_GAP_PX * 0.38
	var pts := PackedVector2Array([
		Vector2(s, 0), Vector2(0, -s), Vector2(0, -s * 0.45), Vector2(-s, -s * 0.45),
		Vector2(-s, s * 0.45), Vector2(0, s * 0.45), Vector2(0, s)])
	var rot := Transform2D(LANE_ANGLES[lane], center)
	pts = rot * pts
	if filled:
		_canvas.draw_colored_polygon(pts, color)
	var outline := pts.duplicate()
	outline.append(pts[0])
	_canvas.draw_polyline(outline, Color.WHITE if filled else color, 3.0)
