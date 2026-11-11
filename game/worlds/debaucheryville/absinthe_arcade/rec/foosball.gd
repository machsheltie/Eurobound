class_name Foosball
extends RefCounted
## Foosball rules: the bros against the house, first to five goals. Seen from above: the bros
## defend the left goal (x = 0) and shoot right; the house defends the right goal. Six rods, as
## on a real table they interleave: bros goalie, bros defence, house attack, bros attack, house
## defence, house goalie. The stick moves all the bros' rods together; a shot (the interact button)
## makes the next touch a hard strike. The house rods chase the ball at a fixed speed.
## Payout: 15 tickets for a win, 3 for a loss (round v25, numbers delegated to Claude).
## Units: the table is FIELD (1.0 x 0.6).

const FIELD := Vector2(1.0, 0.6)
const GOAL_HALF := 0.09
const BALL_RADIUS := 0.015
const MAN_RADIUS := 0.025
const WIN_GOALS := 5
const WIN_TICKETS := 15
const LOSS_TICKETS := 3
const ROD_SPEED := 0.9          ## the bros' stick, table units a second
const HOUSE_ROD_SPEED := 0.45
const PASS_SPEED := 0.8
const SHOT_SPEED := 1.5
const HOUSE_KICK_SPEED := 0.85
const SERVE_SPEED := 0.35
const MIN_FORWARD_SPEED := 0.15
const SHOT_WINDOW := 0.25       ## seconds a shot press stays live
const MAX_SUBSTEP := 0.008      ## table units the ball may travel per physics substep
## [x, side, men, spacing] in table order, left to right.
const RODS := [
	[0.06, "bros", 1, 0.0],
	[0.2, "bros", 2, 0.24],
	[0.38, "house", 3, 0.18],
	[0.62, "bros", 3, 0.18],
	[0.8, "house", 2, 0.24],
	[0.94, "house", 1, 0.0],
]

var ball := FIELD * 0.5
var velocity := Vector2(SERVE_SPEED, 0.0)
var bros_goals := 0
var house_goals := 0
## Rod offsets from the table's centre line, one per rod.
var offsets: Array[float] = []

var _bros_offset := 0.0
var _shot_left := 0.0
var _rng: RandomNumberGenerator


func _init(rng: RandomNumberGenerator = null) -> void:
	_rng = rng if rng != null else RandomNumberGenerator.new()
	if rng == null:
		_rng.randomize()
	for r in RODS:
		offsets.append(0.0)
	_serve(1.0)


func finished() -> bool:
	return bros_goals >= WIN_GOALS or house_goals >= WIN_GOALS


func bros_won() -> bool:
	return bros_goals >= WIN_GOALS


func tickets() -> int:
	return WIN_TICKETS if bros_won() else LOSS_TICKETS


## Every man on one side's rods, left to right then top to bottom.
func men(side: String) -> Array[Vector2]:
	var out: Array[Vector2] = []
	for i in RODS.size():
		if RODS[i][1] == side:
			out.append_array(_rod_men(i))
	return out


## The stick: `axis` -1 (up the screen) .. 1 (down), held for `delta` seconds.
func move_rods(axis: float, delta: float) -> void:
	_bros_offset = clampf(_bros_offset + axis * ROD_SPEED * delta, -FIELD.y * 0.5, FIELD.y * 0.5)
	for i in RODS.size():
		if RODS[i][1] == "bros":
			offsets[i] = _clamp_offset(i, _bros_offset)


func shoot() -> void:
	_shot_left = SHOT_WINDOW


func step(delta: float) -> void:
	if finished():
		return
	_shot_left = maxf(_shot_left - delta, 0.0)
	_move_house_rods(delta)
	var travel := velocity.length() * delta
	var n := maxi(1, ceili(travel / MAX_SUBSTEP))
	for s in n:
		ball += velocity * (delta / n)
		if _bounce_and_score():
			return
		_kicks()


func _rod_men(i: int) -> Array[Vector2]:
	var out: Array[Vector2] = []
	var count: int = RODS[i][2]
	for k in count:
		var y: float = FIELD.y * 0.5 + (k - (count - 1) * 0.5) * float(RODS[i][3]) + offsets[i]
		out.append(Vector2(RODS[i][0], y))
	return out


func _clamp_offset(i: int, offset: float) -> float:
	var half_span: float = (int(RODS[i][2]) - 1) * 0.5 * float(RODS[i][3])
	var room := FIELD.y * 0.5 - half_span - MAN_RADIUS
	return clampf(offset, -room, room)


func _move_house_rods(delta: float) -> void:
	for i in RODS.size():
		if RODS[i][1] != "house":
			continue
		# Line the man nearest the ball up with it.
		var best := INF
		var want := offsets[i]
		for m in _rod_men(i):
			var d := ball.y - m.y
			if absf(d) < absf(best):
				best = d
		if best != INF:
			want = offsets[i] + best
		var stepped := move_toward(offsets[i], want, HOUSE_ROD_SPEED * delta)
		offsets[i] = _clamp_offset(i, stepped)


## Walls and goals. True when a goal was scored (and the ball served again).
func _bounce_and_score() -> bool:
	if ball.y < BALL_RADIUS:
		ball.y = BALL_RADIUS
		velocity.y = absf(velocity.y)
	elif ball.y > FIELD.y - BALL_RADIUS:
		ball.y = FIELD.y - BALL_RADIUS
		velocity.y = -absf(velocity.y)
	var in_mouth := absf(ball.y - FIELD.y * 0.5) < GOAL_HALF
	if ball.x < BALL_RADIUS:
		if in_mouth:
			house_goals += 1
			_serve(-1.0)
			return true
		ball.x = BALL_RADIUS
		velocity.x = absf(velocity.x)
	elif ball.x > FIELD.x - BALL_RADIUS:
		if in_mouth:
			bros_goals += 1
			_serve(1.0)
			return true
		ball.x = FIELD.x - BALL_RADIUS
		velocity.x = -absf(velocity.x)
	if absf(velocity.x) < MIN_FORWARD_SPEED:
		velocity.x = MIN_FORWARD_SPEED * (1.0 if _rng.randf() < 0.5 else -1.0)
	return false


func _kicks() -> void:
	var reach := MAN_RADIUS + BALL_RADIUS
	for i in RODS.size():
		var bros: bool = RODS[i][1] == "bros"
		var dir := 1.0 if bros else -1.0
		for m in _rod_men(i):
			if ball.distance_to(m) >= reach:
				continue
			var speed := HOUSE_KICK_SPEED
			if bros:
				speed = SHOT_SPEED if _shot_left > 0.0 else PASS_SPEED
				_shot_left = 0.0
			var angle := clampf((ball.y - m.y) / reach, -1.0, 1.0) * 0.9
			velocity = Vector2(cos(angle) * dir, sin(angle)) * speed
			ball.x = m.x + dir * (reach + 0.001)
			return


## Back to the middle, rolling toward the side that just conceded.
func _serve(toward: float) -> void:
	ball = FIELD * 0.5
	velocity = Vector2(SERVE_SPEED * toward, _rng.randf_range(-0.15, 0.15))
