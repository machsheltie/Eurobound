class_name SkeeBall
extends RefCounted
## Skee-ball rules: nine balls, each rolled with an aim (-1 left rail .. 1 right rail) and a power
## (0..1). Power picks the ring like a real lane; off-centre rolls clip a ring lip and drop one
## ring; only a full-power roll aimed at a corner finds a 100 pocket. Payout 0-20 tickets by score,
## a 450 game (nine 50s) or better pays the full 20 (round v25, numbers delegated to Claude).

const BALLS := 9
const MAX_TICKETS := 20
const FULL_PAY_SCORE := 450
## Power bands, weakest first: [upper bound, points]. Above the last band the ball hits the hood.
const RINGS := [[0.15, 0], [0.4, 10], [0.55, 20], [0.7, 30], [0.82, 40], [0.9, 50]]
const CORNER_AIM := 0.7
const CLIP_AIM := 0.5
const RAIL_AIM := 0.9

var score := 0
var rolls: Array[int] = []


static func pocket(aim: float, power: float) -> int:
	var side := absf(aim)
	if power > RINGS[-1][0]:
		return 100 if side >= CORNER_AIM else 10
	var points := 0
	var ring := 0
	for i in RINGS.size():
		if power <= RINGS[i][0]:
			ring = i
			points = RINGS[i][1]
			break
	if points == 0:
		return 0
	if side > RAIL_AIM:
		return 10
	if side > CLIP_AIM and points > 10:
		return RINGS[ring - 1][1]
	return points


func balls_left() -> int:
	return BALLS - rolls.size()


func finished() -> bool:
	return balls_left() <= 0


## Rolls the next ball. Returns its points, or -1 when all nine are gone.
func roll(aim: float, power: float) -> int:
	if finished():
		return -1
	var points := pocket(aim, power)
	rolls.append(points)
	score += points
	return points


func tickets() -> int:
	return mini(MAX_TICKETS, roundi(float(score) * MAX_TICKETS / FULL_PAY_SCORE))
