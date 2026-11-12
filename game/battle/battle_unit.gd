class_name BattleUnit
extends RefCounted
## One fighter in a battle: a bro or a villain.
##
## Rolling HP (ef3_rolling_hp, EarthBound style), bros only: `hp` is where the meter is heading
## and `meter` is what it shows. Damage moves `hp` at once; the meter rolls toward it at 10 HP a
## second. A bro is only down when the METER reaches 0, so a bro dealt lethal damage can still act,
## be healed, or survive if the fight ends first. Villains have no meter: they drop at 0 HP.

const PARTY := "party"
const ENEMY := "enemy"

var id := ""
var display_name := ""
var side := PARTY
var max_hp := 1
var hp := 1
var meter := 1.0
var max_bravado := 0
var bravado := 0
var offense := 0
var defense := 0
var speed := 0
var luck := 0
var grit := 0
var skills: Array = []
var charm := 0
## Statuses: id -> turns left (counted down at the end of the bearer's own turn; -1 = until cured).
var statuses: Dictionary = {}
## Temporary effects, each counted down at the end of the bearer's own turn:
var def_buffs: Array = []          ## [{"amount": 2, "turns": 2}]
var def_half_turns := 0
var crit_bonus := 0.0              ## extra crit % the party gets against this unit
var crit_bonus_turns := 0
var grit_zero_turns := 0
## Grit while grit_zero_turns runs (0, or e.g. 2 in Accounts Receivable's vulnerability window).
var grit_low := 0
var speed_bonus := 0               ## e.g. the Sinking Fund's dive gives the others +2
var speed_bonus_turns := 0
## Turns this unit skips (Digesting, Attract Mode, Stun is a status instead).
var skip_turns := 0
## Swallowed by Croc Monsieur / diving Fund: can't act and can't be targeted.
var gone_turns := 0
var gone_status: Dictionary = {}   ## applied when a swallowed bro is spat out
## Halves damage taken until this unit's next turn (Hold Back to Block, Spiritually).
var guarding := false

## Villain only.
var data: Dictionary = {}          ## the villain's battle data (moves, phases, immunities...)
var moves: Array = []
var sp := 0
var phase := 1
var telegraph: Dictionary = {}     ## the move wound up last turn; it fires on this unit's next turn
var cooldown_until: Dictionary = {}   ## move id -> first round it may be used again
var uses: Dictionary = {}          ## move id -> times used this fight
var last_target := ""
var layers := 0                    ## Shish Kahn's Extra Layer stacks
var palette := ""                  ## Condiment Clan Ninja
var ticket_reward := 0
var item_drop := ""
var drop_chance := 0.0
var bill_used := false             ## Croc Monsieur's first-KO hold
var downed_by := ""
var slot := 0                      ## position in the enemy row
## Green Fairy Wisp's split (the_absinthium_taproom.md:174-176): an illusion pops on any hit, pays
## nothing and doesn't count toward the win. It waits `dormant` (unseen, untargetable, no turns)
## until the real Wisp splits.
var illusion := false
var dormant := false


static func from_member(m: Dictionary) -> BattleUnit:
	var u := BattleUnit.new()
	u.id = String(m.get("id", ""))
	u.display_name = String(m.get("display_name", u.id))
	u.side = PARTY
	u.max_hp = int(m.get("max_hp", 1))
	u.hp = int(m.get("hp", u.max_hp))
	u.meter = float(u.hp)
	u.max_bravado = int(m.get("max_bravado", 0))
	u.bravado = int(m.get("bravado", u.max_bravado))
	u.offense = int(m.get("offense", 0))
	u.defense = int(m.get("defense", 0))
	u.speed = int(m.get("speed", 0))
	u.luck = int(m.get("luck", 0))
	u.grit = int(m.get("grit", 0))
	u.charm = int(m.get("charm", 0))
	u.skills = Array(m.get("skills", [])).duplicate()
	u.statuses = Dictionary(m.get("statuses", {})).duplicate()
	return u


## `e` is the engine enemy entry; `battle` is its debaucheryville_arcade_battle.json entry.
static func from_enemy(id_: String, e: Dictionary, battle: Dictionary = {}) -> BattleUnit:
	var u := BattleUnit.new()
	u.id = id_
	u.display_name = String(e.get("display_name", id_))
	u.side = ENEMY
	u.max_hp = int(e.get("max_hp", 1))
	u.hp = u.max_hp
	u.meter = float(u.hp)
	u.offense = int(e.get("offense", 0))
	u.defense = int(e.get("defense", 0))
	u.speed = int(e.get("speed", 0))
	u.luck = int(e.get("luck", 0))
	u.grit = int(battle.get("grit", e.get("grit", 0)))
	u.charm = int(battle.get("charm", e.get("charm", 0)))
	u.data = battle
	u.moves = Array(battle.get("moves", [])).duplicate(true)
	u.sp = int(battle.get("sp", 0))
	u.ticket_reward = int(e.get("ticket_reward", 0))
	var drop = e.get("item_drop", "")
	u.item_drop = drop if drop is String else ""  # null: no drop
	u.drop_chance = float(e.get("drop_chance", 0.0))
	return u


func is_party() -> bool:
	return side == PARTY


## Down for good this fight: a bro's meter at 0, or a villain at 0 HP.
func is_down() -> bool:
	if is_party():
		return meter <= 0.0
	return hp <= 0


func tier() -> String:
	return BattleRules.tier(bravado, max_bravado) if is_party() else BattleRules.MID


func bravado_mod() -> int:
	return BattleRules.modifier(bravado, max_bravado) if is_party() else 0


func battle_speed() -> int:
	var base := speed + speed_bonus + StatusTable.stat_delta(statuses, "speed")
	if statuses.has("hardcore_gamer"):
		base += 2
	return BattleRules.speed(base, tier()) if is_party() else base


## True when the status is on the unit and no live status suppresses it (status_effects.json).
func has_status(id_: String) -> bool:
	return statuses.has(id_) and StatusTable.suppressor_of(id_, statuses).is_empty()


func targetable() -> bool:
	return not is_down() and gone_turns <= 0 and not dormant


## Offense after Embarrassed / Gains Bro (ef4_status_conflict = villain_docs).
func attack_stat(social: bool) -> float:
	var a := float(charm if social else offense)
	a += StatusTable.stat_delta(statuses, "charm" if social else "offense")
	if statuses.has("embarrassed"):
		a *= BattleRulings.EMBARRASSED_ATK
	if statuses.has("gains_bro"):
		a *= BattleRulings.GAINS_BRO_ATK
	return a


func defense_stat() -> int:
	var d := defense + StatusTable.stat_delta(statuses, "defense")
	for b in def_buffs:
		d += int(b["amount"])
	d += layers * 2
	if def_half_turns > 0:
		d = d / 2
	return d


func grit_stat() -> int:
	return (grit_low if grit_zero_turns > 0 else grit) + StatusTable.stat_delta(statuses, "grit")


## Intoxicant follow-ups (Eurobound-umy): main status id -> {"status": then id, "count": stacks}.
## Set when an intoxicant is used; cleared when the main status is cured away.
var then_pending: Dictionary = {}
## Follow-ups whose main status just ran out this tick: [{"status", "count"}]. BattleCore drains it.
var due_then: Array = []


## Ticks every timed effect at the end of this unit's own turn.
func end_own_turn() -> void:
	for id_ in statuses.keys():
		if int(statuses[id_]) > 0:
			statuses[id_] = int(statuses[id_]) - 1
			if int(statuses[id_]) <= 0:
				statuses.erase(id_)
				if then_pending.has(id_):
					due_then.append(then_pending[id_])
					then_pending.erase(id_)
	var kept: Array = []
	for b in def_buffs:
		b["turns"] = int(b["turns"]) - 1
		if int(b["turns"]) > 0:
			kept.append(b)
	def_buffs = kept
	def_half_turns = maxi(def_half_turns - 1, 0)
	grit_zero_turns = maxi(grit_zero_turns - 1, 0)
	crit_bonus_turns = maxi(crit_bonus_turns - 1, 0)
	if crit_bonus_turns == 0:
		crit_bonus = 0.0
	speed_bonus_turns = maxi(speed_bonus_turns - 1, 0)
	if speed_bonus_turns == 0:
		speed_bonus = 0


func take_damage(amount: int) -> void:
	hp = maxi(hp - amount, 0)
	if not is_party():
		meter = float(hp)


func heal(amount: int) -> void:
	if is_down():
		return
	hp = mini(hp + amount, max_hp)
	if not is_party():
		meter = float(hp)


func gain_bravado(amount: int) -> void:
	bravado = clampi(bravado + amount, 0, max_bravado)


## Rolls the meter toward `hp`. Returns true the moment a bro's meter hits 0.
func roll_meter(delta: float) -> bool:
	if not is_party() or meter <= 0.0:
		return false
	meter = move_toward(meter, float(hp), BattleRules.ROLL_HP_PER_S * delta)
	return meter <= 0.0


## The HP a bro walks away with when the fight ends: wherever the meter stopped.
func settled_hp() -> int:
	return clampi(ceili(meter), 0, max_hp)
