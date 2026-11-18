class_name StreetEncounterRules
extends RefCounted
## Street encounters, Option A "EarthBound straight" (author, Eurobound Desk Eurobound-skjd-q2,
## 2026-11-16; docs/superpowers/specs/2026-11-16-Eurobound-skjd-proposal.md section 3;
## design/mechanics/Battle/street_encounters.md). The pure checks; StreetEncounters runs them on a
## screen and StreetEnemy is the enemy on the map.
##
## Every number below is the author's. Ruled so far: GRACE_UNIT (steps) and LOSS_SOVS_SHARE (half),
## Eurobound Desk Eurobound-iqgo-q2 / -q3, 2026-11-18. null or "" means "not ruled": the feature it
## drives stays off. Never fill one in without an author ruling.

## Point 4, auto-win: how many levels the party must be above the enemy. null = auto-win is off
## (the spec keeps it off until the XP curve is ruled, NEXT_WORK.md:919).
const AUTO_WIN_LEVEL_GAP = null
## Point 4: which party level is compared: "leader", "lowest" or "average". "" = not ruled (off).
const AUTO_WIN_PARTY_LEVEL := ""
## Point 5, grace after a fight or a Run: its length, in GRACE_UNIT. null = no grace period.
## Without one, a fight still never restarts on its own: contact is a fresh touch, never standing
## in an enemy (StreetEnemy).
const GRACE_LENGTH = null
## Point 5: "steps" (1 step = 1 metre the leader walks, FieldStatus) or "seconds". RULED: steps
## (author, Eurobound Desk Eurobound-iqgo-q2: "Count it in steps (walking distance)"). The NUMBER of
## steps is not ruled, so GRACE_LENGTH stays null (no grace) until it is.
const GRACE_UNIT := "steps"
## Point 3, first strike: how many rounds the side that struck from behind acts first. The spec's
## Option A text says one round; spec section 5 item 3 keeps its size open, so it is not set here.
## null = no first strike (normal Speed order).
const FIRST_STRIKE_ROUNDS = null
## Point 7, losing: the share of the SOVS on hand lost. RULED: half (author, Eurobound Desk
## Eurobound-iqgo-q3: "Half, as EarthBound does"). null = none lost.
const LOSS_SOVS_SHARE = 0.5

const UNIT_STEPS := "steps"
const UNIT_SECONDS := "seconds"

## first_strike() results: the side that acts first, or neither.
const PARTY := "party"
const ENEMY := "enemy"
const NONE := ""


## Point 3. Who touched whom from behind, on the ground plane. "Behind" means in the back half of
## the one touched. The bros behind the enemy: PARTY. The enemy behind the bros: ENEMY. Face to face,
## side on, or each behind the other (back to back): NONE.
static func first_strike(bros_pos: Vector3, bros_facing: Vector3, enemy_pos: Vector3, enemy_facing: Vector3) -> String:
	var to_bros := Vector2(bros_pos.x - enemy_pos.x, bros_pos.z - enemy_pos.z)
	var bros_behind := Vector2(enemy_facing.x, enemy_facing.z).dot(to_bros) < 0.0
	var enemy_behind := Vector2(bros_facing.x, bros_facing.z).dot(-to_bros) < 0.0
	if bros_behind and not enemy_behind:
		return PARTY
	if enemy_behind and not bros_behind:
		return ENEMY
	return NONE


## Point 4. The party level the auto-win test uses, from GameState.party: the leader's, the
## lowest, or the average. null when the measure is not ruled or there is no party.
static func party_level(party: Array, measure: String) -> Variant:
	if party.is_empty():
		return null
	var levels: Array[int] = []
	for m in party:
		levels.append(int(m.get("level", 1)))
	match measure:
		"leader":
			return levels[0]
		"lowest":
			return levels.min()
		"average":
			var total := 0
			for l in levels:
				total += l
			return float(total) / levels.size()
	return null


## Point 4. True when contact wins on the spot: the party level is at least `gap` above the
## enemy's. Off (false) while the gap or the measure is unruled, or the enemy has no level.
static func auto_win(level: Variant, enemy_level: Variant, gap: Variant = AUTO_WIN_LEVEL_GAP,
		measure: String = AUTO_WIN_PARTY_LEVEL) -> bool:
	if gap == null or measure == "" or level == null or enemy_level == null:
		return false
	return float(level) - float(enemy_level) >= float(gap)


## Point 7. The SOVS a loss takes from `on_hand` at `share` (rounded down, never more than is on
## hand). 0 while the share is unruled. Rounding is an implementation detail of "half", the
## EarthBound way (pending author confirmation): the bros keep the rounded-up half and lose the
## floor, so 81 SOVS on hand loses 40 and leaves 41; 1 SOV loses nothing.
static func sovs_lost(on_hand: int, share: Variant = LOSS_SOVS_SHARE) -> int:
	if share == null or on_hand <= 0:
		return 0
	return clampi(floori(on_hand * float(share)), 0, on_hand)
