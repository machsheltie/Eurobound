class_name BattleRules
extends RefCounted
## The battle numbers, as approved by the author in round v26 (2026-11-11, every ef3_ item
## "approve"; see design/mechanics/Battle/battle_numbers_proposal.md). Pure functions only:
## BattleCore does the bookkeeping, this file does the arithmetic.
##
##  - Base Damage = (ATK + Bravado Modifier) - DEF   (battle_system.md)
##  - ef3_bravado_tiers:      Low below 1/3 of max Bravado, High at 2/3 and above, Mid between
##  - ef3_bravado_modifier:   High + half max Bravado, Mid + a quarter, Low -2
##  - ef3_damage_floor_spread: +-2 spread, a hit always does at least 1
##  - ef3_crit:               Luck, +10 at High Bravado, - half the target's Grit, at least 1%;
##                            a SMAAAASH doubles the damage
##  - ef3_bravado_speed:      High +2 Speed, Low -2 Speed
##  - ef3_flex:               Bravado Flex restores 3 Bravado
##  - ef3_rolling_hp:         the HP meter rolls 10 HP a second
##  - ef3_run:                50%, +5% per point the party's average Speed beats the enemies',
##                            clamped 10%..90%
## Enemies have no Bravado: their modifier is 0 and their tier never changes Speed or crits.

const LOW := "low"
const MID := "mid"
const HIGH := "high"

const LOW_PENALTY := -2
const SPREAD := 2
const MIN_DAMAGE := 1
const HIGH_CRIT_BONUS := 10.0
const MIN_CRIT_PCT := 1.0
const CRIT_MULTIPLIER := 2
const SPEED_SHIFT := 2
const FLEX_BRAVADO := 3
const ROLL_HP_PER_S := 10.0
const RUN_BASE_PCT := 50.0
const RUN_PCT_PER_SPEED := 5.0
const RUN_MIN_PCT := 10.0
const RUN_MAX_PCT := 90.0


## "low", "mid" or "high". Zero Bravado is Low (and, separately, can't pay for anything).
static func tier(bravado: int, max_bravado: int) -> String:
	if max_bravado <= 0:
		return LOW
	if bravado * 3 < max_bravado:
		return LOW
	if bravado * 3 >= max_bravado * 2:
		return HIGH
	return MID


static func modifier(bravado: int, max_bravado: int) -> int:
	if max_bravado <= 0:
		return 0
	match tier(bravado, max_bravado):
		HIGH:
			return max_bravado / 2
		MID:
			return max_bravado / 4
	return LOW_PENALTY


## (ATK + modifier) - DEF, times the move's multiplier, plus the spread roll, at least 1.
## `spread_roll` is the -2..2 roll; pass 0 for the expected value.
static func damage(atk: int, bravado_mod: int, def: int, multiplier: float, spread_roll: int) -> int:
	var base := float(atk + bravado_mod - def) * multiplier
	return maxi(MIN_DAMAGE, roundi(base) + spread_roll)


static func crit_pct(luck: int, high_bravado: bool, target_grit: int) -> float:
	var pct := float(luck) + (HIGH_CRIT_BONUS if high_bravado else 0.0) - float(target_grit) * 0.5
	return maxf(MIN_CRIT_PCT, pct)


static func speed(base_speed: int, bravado_tier: String) -> int:
	match bravado_tier:
		HIGH:
			return base_speed + SPEED_SHIFT
		LOW:
			return base_speed - SPEED_SHIFT
	return base_speed


static func run_pct(party_avg_speed: float, enemy_avg_speed: float) -> float:
	var pct := RUN_BASE_PCT + RUN_PCT_PER_SPEED * (party_avg_speed - enemy_avg_speed)
	return clampf(pct, RUN_MIN_PCT, RUN_MAX_PCT)
