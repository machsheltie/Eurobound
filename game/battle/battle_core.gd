class_name BattleCore
extends RefCounted
## One battle, start to finish, with no drawing: BattleScreen shows it, tests drive it directly.
##
## Rules (design/mechanics/Battle/battle_system.md + the round v26 numbers in BattleRules):
##  - Rounds. At the start of each round every fighter is sorted by Speed (Bravado-adjusted for the
##    bros); ties go to the bros, then to the earlier slot.
##  - A bro's turn: an optional minor action (Item or Bravado Flex) and one main action (Attack, a
##    skill such as Roast Line, or Run). The turn ends with the main action.
##  - Villains follow their doc move tables (assets/data/enemies/debaucheryville_arcade_battle.json):
##    weighted-random picks, telegraphed big moves on clocks or HP gates (wound up on one turn, fired
##    on the next), phases at HP thresholds, and each doc's gimmick.
##  - Rolling HP for the bros (BattleUnit). `tick(delta)` rolls the meters; the screen calls it every
##    frame, including while the player is choosing.
## Every message for the player goes into `events` as {"text": String}; the screen drains it.

const NEGATIVE := ["embarrassed", "sloppy", "confused", "stun", "grease_fingers", "tourist_trap_victim",
	"food_poisoning", "broke_af"]

var party: Array[BattleUnit] = []
var enemies: Array[BattleUnit] = []
var events: Array = []
var round_number := 0
var outcome := ""                  ## "", "won", "lost" or "ran"
var minor_used := false
## The wallet and bag: GameState in the game, a stand-in in tests (sovs, inventory, add_item()).
var wallet: Object
## Consumable data by id (heal_hp, heal_bravado, display_name).
var items: Dictionary = {}
## Street Fighter cabinet-wide Second Thoughts re-roll chance (0 elsewhere).
var second_thoughts := 0.0
## SOVS the Sinking Fund's Buy the Dip took this fight (its soggy pile pays them back on a win).
var sovs_taken := 0
## A bill being collected in this fight (Accounts Receivable): what's still owed, and what Shake Down
## Payment has collected toward it (round v31 ar_steal = a).
var balance_due := 0
var sovs_collected := 0

const JARMILA := "super_turbo_hyper_jarmila"
## Her marquee grows one word per revision (doc: "…EX", "…EX Plus Alpha Final Revision").
const JARMILA_WORDS := ["EX", "Plus", "Alpha", "Final", "Revision"]

var _rng: RandomNumberGenerator
var _order: Array[BattleUnit] = []
var _turn := 0
var _turn_started := false
var _fought: Array[BattleUnit] = []


func _init(rng: RandomNumberGenerator = null) -> void:
	_rng = rng if rng != null else RandomNumberGenerator.new()
	if rng == null:
		_rng.randomize()


# --- setup -------------------------------------------------------------------------------------

func add_enemy(u: BattleUnit) -> void:
	u.side = BattleUnit.ENEMY
	u.slot = enemies.size()
	enemies.append(u)
	_fought.append(u)


## Names duplicates "A", "B"... so the log can tell two Hatchbacks apart.
func label_duplicates() -> void:
	var counts := {}
	for e in enemies:
		counts[e.display_name] = int(counts.get(e.display_name, 0)) + 1
	var seen := {}
	for e in enemies:
		if int(counts[e.display_name]) > 1:
			var k := int(seen.get(e.display_name, 0))
			seen[e.display_name] = k + 1
			e.display_name += " " + "ABC"[k]


func start() -> void:
	label_duplicates()
	var intro := String(enemies[0].data.get("intro_bark", "")) if not enemies.is_empty() else ""
	for e in enemies:
		_say("%s appears!" % e.display_name)
	if intro != "":
		_say("%s: \"%s\"" % [enemies[0].display_name, intro])
	_new_round()


# --- flow --------------------------------------------------------------------------------------

func current() -> BattleUnit:
	if outcome != "" or _turn >= _order.size():
		return null
	return _order[_turn]


## True while the game waits for the player to pick an action for current().
func needs_input() -> bool:
	var u := current()
	return u != null and u.is_party() and _turn_started


## Moves the battle on until a bro needs a command, or one villain turn has played out (so the
## screen can show its events before the next).
func step() -> void:
	while outcome == "":
		if _turn >= _order.size():
			_new_round()
		var u := _order[_turn]
		if u.is_down():
			_turn += 1
			continue
		if u.is_party():
			if _turn_started:
				return
			_turn_started = true
			minor_used = false
			if _turn_lost(u):
				_finish_turn(u)
			return
		_enemy_turn(u)
		_finish_turn(u)
		return


## Rolls the bros' HP meters. Returns true when anything changed the outcome.
func tick(delta: float) -> bool:
	if outcome != "":
		return false
	for b in party:
		if b.roll_meter(delta):
			_say("%s is down!" % b.display_name)
	return _check_outcome()


# --- the bros' commands ------------------------------------------------------------------------

func can_flex() -> bool:
	return needs_input() and not minor_used


func usable_items() -> Array:
	var out := []
	if wallet == null:
		return out
	for id in items.keys():
		if int(wallet.inventory.get(id, 0)) > 0 and has_battle_effect(items[id]):
			out.append(id)
	return out


## Items that do something in a fight (heal, Bravado, revive, cure). A coupon doesn't.
static func has_battle_effect(item: Dictionary) -> bool:
	return int(item.get("heal_hp", 0)) > 0 or int(item.get("heal_bravado", 0)) > 0 		or float(item.get("revive_pct", 0.0)) > 0.0 or not String(item.get("cures_status", "")).is_empty()


static func revives(item: Dictionary) -> bool:
	return float(item.get("revive_pct", 0.0)) > 0.0


## Who an item can go on: a reviving item only on a downed bro, anything else only on a standing one.
func item_targets(item_id: String) -> Array:
	var item: Dictionary = items.get(item_id, {})
	if revives(item):
		return party.filter(func(b: BattleUnit) -> bool: return b.is_down())
	return living_party()


## Roast Line and the like: needs the skill's Bravado, and Embarrassed locks Bravado moves.
func can_use_skill(u: BattleUnit, skill: Dictionary) -> bool:
	var cost := int(skill.get("bravado_cost", 0))
	return u.bravado >= cost and u.bravado > 0 and not u.has_status("embarrassed")


func flex() -> void:
	var u := current()
	if not can_flex():
		return
	minor_used = true
	u.gain_bravado(BattleRules.FLEX_BRAVADO)
	_say("%s flexes. +%d Bravado." % [u.display_name, BattleRules.FLEX_BRAVADO])


func use_item(item_id: String, target: BattleUnit) -> bool:
	var u := current()
	if not needs_input() or minor_used or not usable_items().has(item_id) or not item_targets(item_id).has(target):
		return false
	minor_used = true
	var item: Dictionary = items[item_id]
	wallet.inventory[item_id] = int(wallet.inventory[item_id]) - 1
	if int(wallet.inventory[item_id]) <= 0:
		wallet.inventory.erase(item_id)
	_say("%s uses %s on %s." % [u.display_name, item.get("display_name", item_id), target.display_name])
	if revives(item):
		# e.g. the Already-Spent Credit (count_continue.md): back up at a share of max HP.
		var hp := maxi(ceili(target.max_hp * float(item["revive_pct"])), 1)
		target.hp = hp
		target.meter = float(hp)
		_say("%s is back up with %d HP." % [target.display_name, hp])
	target.heal(int(item.get("heal_hp", 0)))
	target.gain_bravado(int(item.get("heal_bravado", 0)))
	var cure := String(item.get("cures_status", ""))
	if not cure.is_empty() and target.has_status(cure):
		# e.g. the Revision Sticker (super_turbo_hyper_jarmila.md) cures Confused.
		target.statuses.erase(cure)
		_say("%s is no longer %s." % [target.display_name, _status_name(cure)])
	return true


func attack(target: BattleUnit) -> void:
	var u := current()
	if not needs_input():
		return
	_party_hit(u, target, 1.0, "%s attacks!" % u.display_name)
	_finish_turn(u)


func use_skill(skill: Dictionary, target: BattleUnit) -> bool:
	var u := current()
	if not needs_input() or not can_use_skill(u, skill):
		return false
	u.gain_bravado(-int(skill.get("bravado_cost", 0)))
	var text := String(skill.get("battle_text", "{user} uses %s!" % skill.get("display_name", ""))).replace("{user}", u.display_name)
	_party_hit(u, target, float(skill.get("power_multiplier", 1.0)), text)
	_finish_turn(u)
	return true


func run_away() -> void:
	var u := current()
	if not needs_input():
		return
	var pct := BattleRules.run_pct(_avg_speed(party), _avg_speed(enemies))
	if _rng.randf() * 100.0 < pct:
		_say("The bros run for it!")
		outcome = "ran"
		return
	_say("The bros can't get away!")
	_finish_turn(u)


func targetable_enemies() -> Array:
	return enemies.filter(func(e: BattleUnit) -> bool: return e.targetable())


func living_party() -> Array:
	return party.filter(func(b: BattleUnit) -> bool: return not b.is_down())


# --- results -----------------------------------------------------------------------------------

## The tickets this fight pays on a win: the sum of every villain fought (ef4_multi_tickets).
func tickets() -> int:
	var total := 0
	var best := 0
	for e in _fought:
		total += e.ticket_reward
		best = maxi(best, e.ticket_reward)
	return total if BattleRulings.TICKETS_SUM else best


## Item drops rolled once per villain fought (each doc's drop and chance).
func roll_drops() -> Array:
	var out := []
	for e in _fought:
		if e.item_drop != "" and _rng.randf() < e.drop_chance:
			out.append(e.item_drop)
	return out


# --- turns -------------------------------------------------------------------------------------

func _new_round() -> void:
	round_number += 1
	_turn = 0
	_turn_started = false
	var all: Array[BattleUnit] = []
	for x in party + enemies:
		if not x.is_down():
			all.append(x)
	all.sort_custom(func(a: BattleUnit, b: BattleUnit) -> bool:
		if a.battle_speed() != b.battle_speed():
			return a.battle_speed() > b.battle_speed()
		if a.is_party() != b.is_party():
			return a.is_party()
		return a.slot < b.slot)
	_order = all


## Start-of-turn effects. True when the turn is lost.
func _turn_lost(u: BattleUnit) -> bool:
	u.guarding = false
	if u.gone_turns > 0:
		u.gone_turns -= 1
		if u.gone_turns == 0 and not u.gone_status.is_empty():
			_say("%s is spat back out." % u.display_name)
			for id in u.gone_status.keys():
				_apply_status(u, id, int(u.gone_status[id]), 1.0)
			u.gone_status = {}
		return true
	if u.has_status("food_poisoning"):
		_dot(u, 2, "Food Poisoning")
		if _rng.randf() < 0.5:
			_say("%s loses the turn to Food Poisoning." % u.display_name)
			return true
	if u.has_status("hardcore_gamer"):
		_dot(u, 1, "Hardcore Gamer")
	if u.is_party() and u.has_status("embarrassed"):
		u.gain_bravado(-BattleRulings.EMBARRASSED_DRAIN)
	if u.has_status("stun"):
		_say("%s is stunned." % u.display_name)
		return true
	if u.skip_turns > 0:
		u.skip_turns -= 1
		_say("%s loses the turn." % u.display_name)
		return true
	return false


func _dot(u: BattleUnit, amount: int, why: String) -> void:
	u.take_damage(amount)
	_say("%s takes %d from %s." % [u.display_name, amount, why])
	if not u.is_party() and u.hp <= 0:
		_enemy_down(u, null)
		_check_outcome()


func _finish_turn(u: BattleUnit) -> void:
	if outcome != "":
		return
	u.end_own_turn()
	if not u.is_party():
		_apply_after(u)
	_turn += 1
	_turn_started = false
	_check_outcome()


func _check_outcome() -> bool:
	if outcome != "":
		return true
	if enemies.all(func(e: BattleUnit) -> bool: return e.is_down()):
		outcome = "won"
		_say("The bros win!")
		return true
	if party.all(func(b: BattleUnit) -> bool: return b.is_down()):
		outcome = "lost"
		_say("GAME OVER. INSERT TOKEN.")
		return true
	return false


# --- hitting -----------------------------------------------------------------------------------

func _party_hit(u: BattleUnit, target: BattleUnit, mult: float, text: String) -> void:
	_say(text)
	var aimed := _redirect(u, target, false)
	if aimed == null:
		return
	_hit(u, aimed, mult, false, 0)


## Confused and Sloppy can change who a single-target action lands on. Null when nobody's left.
func _redirect(u: BattleUnit, target: BattleUnit, from_enemy: bool) -> BattleUnit:
	if u.has_status("confused"):
		var pool: Array[BattleUnit] = []
		for x in party + enemies:
			if x != u and x.targetable():
				pool.append(x)
		if pool.is_empty():
			return null
		var pick: BattleUnit = pool[_rng.randi_range(0, pool.size() - 1)]
		if pick != target:
			_say("%s is Confused and goes for %s." % [u.display_name, pick.display_name])
		return pick
	if u.has_status("sloppy") and _rng.randf() < 0.15:
		var side: Array[BattleUnit] = enemies if from_enemy else party
		var allies := side.filter(func(x: BattleUnit) -> bool: return x != u and x.targetable())
		if not allies.is_empty():
			var pick: BattleUnit = allies[_rng.randi_range(0, allies.size() - 1)]
			_say("%s is Sloppy and hits %s instead." % [u.display_name, pick.display_name])
			return pick
	if target == null or not target.targetable():
		var pool := (living_party() if from_enemy else targetable_enemies()).filter(func(x: BattleUnit) -> bool: return x.targetable())
		if pool.is_empty():
			return null
		return pool[_rng.randi_range(0, pool.size() - 1)]
	return target


## One hit: accuracy, damage, crit, resistances. Returns {"hit", "damage", "crit"}.
func _hit(u: BattleUnit, target: BattleUnit, mult: float, social: bool, acc_steps: int) -> Dictionary:
	var steps := acc_steps
	if u.has_status("sloppy"):
		steps -= 3
	if u.has_status("grease_fingers"):
		steps -= 2
	var hit_pct := BattleRulings.BASE_HIT_PCT + BattleRulings.HIT_PCT_PER_STEP * steps
	if _rng.randf() * 100.0 >= hit_pct:
		_say("%s misses." % u.display_name)
		return {"hit": false, "damage": 0, "crit": false}
	var atk := roundi(u.attack_stat(social))
	var def := target.grit_stat() if social else target.defense_stat()
	var dmg := BattleRules.damage(atk, u.bravado_mod(), def, mult, _rng.randi_range(-BattleRules.SPREAD, BattleRules.SPREAD))
	var crit := BattleRules.crit_pct(u.luck, u.tier() == BattleRules.HIGH, target.grit_stat())
	if u.has_status("hardcore_gamer"):
		crit += 1.0
	if u.is_party():
		crit += target.crit_bonus
	var is_crit := _rng.randf() * 100.0 < crit
	if is_crit:
		dmg *= BattleRules.CRIT_MULTIPLIER
	dmg = _resisted(target, dmg, social)
	if target.guarding:
		dmg = maxi(dmg / 2, 1)
	target.take_damage(dmg)
	if is_crit:
		_say("SMAAAASH! %s takes %d." % [target.display_name, dmg])
	else:
		_say("%s takes %d." % [target.display_name, dmg])
	if not target.is_party():
		_check_phase(target)
		if target.hp <= 0:
			_enemy_down(target, u)
	return {"hit": true, "damage": dmg, "crit": is_crit}


func _resisted(target: BattleUnit, dmg: int, social: bool) -> int:
	var d := target.data
	var r := 0.0
	if social:
		r = float(d.get("social_resist", 0.0))
	else:
		r = float(d.get("physical_resist", 0.0))
		if d.get("physical_resist_off_while_telegraphing", false) and not target.telegraph.is_empty():
			r = 0.0
	return maxi(roundi(dmg * (1.0 - r)), 1) if r > 0.0 else dmg


func _apply_status(target: BattleUnit, id: String, turns: int, chance: float) -> bool:
	if id == "" or target.is_down():
		return false
	if Array(target.data.get("immune", [])).has(id):
		_say("%s shrugs off %s." % [target.display_name, _status_name(id)])
		return false
	if Array(target.data.get("status_always", [])).has(id):
		chance = 1.0   # e.g. Accounts Receivable: Grease Fingers always lands
	if _rng.randf() >= chance:
		return false
	var resist := float(Dictionary(target.data.get("status_resist", {})).get(id, 0.0))
	if resist > 0.0 and _rng.randf() < resist:
		_say("%s resists %s." % [target.display_name, _status_name(id)])
		return false
	if id == "stun" and target.has_status("stun"):
		return false
	var lasting := BattleRulings.LASTING_STATUSES.has(id)
	target.statuses[id] = -1 if lasting else maxi(turns, 1)
	_say("%s is %s!" % [target.display_name, _status_name(id)])
	if id == "embarrassed" and not target.is_party():
		_embarrassed_cancels(target)
	return true


## Jarmila's next Re-Release and Vratislav's Full Three-Sixty fold when they're Embarrassed.
func _embarrassed_cancels(e: BattleUnit) -> void:
	for m in e.moves:
		if m.get("embarrassed_cancels", false):
			if not e.telegraph.is_empty() and e.telegraph.get("id") == m["id"]:
				e.telegraph = {}
				e.def_half_turns = 0
				_say("%s can't go through with %s." % [e.display_name, m["name"]])
			else:
				e.uses["cancel_" + String(m["id"])] = 1


static func _status_name(id: String) -> String:
	return id.replace("_", " ").capitalize().replace("Af", "AF")


# --- villains ----------------------------------------------------------------------------------

func _enemy_down(e: BattleUnit, by: BattleUnit) -> void:
	var bill: Dictionary = e.data.get("bill", {})
	if not bill.is_empty() and not e.bill_used:
		# The Bill Will Find You: up at 1 HP, one immediate extra action at whoever knocked him down.
		e.bill_used = true
		e.hp = 1
		e.meter = 1.0
		var target := by if by != null and by.is_party() else _bro("lord_pilsner")
		_say("%s does not fall. \"Before monsieur goes. The bill.\"" % e.display_name)
		if target != null and not target.is_down():
			_hit(e, target, float(bill.get("mult", 1.2)), false, 0)
			_say(String(bill.get("log", "")))
		return
	e.telegraph = {}
	_say("%s is defeated!" % e.display_name)
	for other in enemies:
		if other != e and not other.is_down():
			_check_phase(other)


func _bro(id: String) -> BattleUnit:
	for b in party:
		if b.id == id:
			return b
	return null


func _check_phase(e: BattleUnit) -> void:
	for p in e.data.get("phases", []):
		var n := int(p["phase"])
		if e.phase >= n or e.hp <= 0:
			continue
		if float(e.hp) < float(p.get("hp_below", 0.0)) * e.max_hp:
			_enter_phase(e, p)
		elif p.get("ally_down", false) and _same_kind(e).is_empty() 				and _fought.filter(func(x: BattleUnit) -> bool: return x.id == e.id).size() > 1:
			_enter_phase(e, p)


func _enter_phase(e: BattleUnit, p: Dictionary) -> void:
	e.phase = int(p["phase"])
	if e.id == JARMILA:
		_revise(e, int(e.uses.get("defeats", 0)) + (1 if e.phase == 2 else 5))
	if p.has("bark"):
		_say("%s: \"%s\"" % [e.display_name, p["bark"]])
	if p.has("speed"):
		e.speed = int(p["speed"])
	if p.has("offense_bonus"):
		e.offense += int(p["offense_bonus"])
	if p.get("drop_layers", false):
		e.layers = 0
	if p.has("force_next"):
		e.uses["force_" + String(p["force_next"])] = 1


func _allies(e: BattleUnit) -> Array:
	return enemies.filter(func(x: BattleUnit) -> bool: return x != e and not x.is_down())


func _enemy_turn(e: BattleUnit) -> void:
	if e.uses.get("surfacing", 0) == 1:
		e.gone_turns = 0
		_surface(e)
		return
	if _turn_lost(e) or e.is_down():
		return
	if e.uses.get("ponder", 0) == 1:
		e.uses["ponder"] = 0
		_say("%s idles in the lane, pondering." % e.display_name)
		return
	if not e.telegraph.is_empty():
		var m := e.telegraph
		e.telegraph = {}
		_resolve(e, m)
		return
	var forced := _forced_move(e)
	if not forced.is_empty():
		_wind_up(e, forced)
		return
	var m := _pick_move(e)
	if m.is_empty():
		_say("%s hesitates." % e.display_name)
		return
	if second_thoughts > 0.0 and _rng.randf() < second_thoughts:
		var other := _pick_move(e)
		if not other.is_empty() and other["id"] != m["id"]:
			_say("%s uses %s! ...No. %s has decided it is %s." % [e.display_name, m["name"], e.display_name, other["name"]])
			m = other
	if _is_telegraphed(m):
		_wind_up(e, m)
	else:
		_resolve(e, m)


static func _is_telegraphed(m: Dictionary) -> bool:
	var t = m.get("telegraph", null)
	return t is String or (t is bool and t)


func _wind_up(e: BattleUnit, m: Dictionary) -> void:
	e.telegraph = m
	e.uses[String(m["id"])] = int(e.uses.get(String(m["id"]), 0)) + 1
	e.cooldown_until[String(m["id"])] = round_number + 1
	var t = m.get("telegraph")
	if t is String:
		_say("%s: \"%s\"" % [e.display_name, t])
	else:
		_say("%s is winding up %s!" % [e.display_name, m["name"]])
	var w: Dictionary = m.get("while_telegraphing", {})
	if w.get("def_half", false):
		e.uses["tele_def_half"] = 1
	if w.has("crit_bonus"):
		e.uses["tele_crit"] = int(w["crit_bonus"])
	if m.get("special", "") == "re_release":
		_say("COMING SOON. %s takes no action." % e.display_name)


## Clocked, gated and queue-jumping moves, in the order the docs give them priority.
func _forced_move(e: BattleUnit) -> Dictionary:
	for m in e.moves:
		var id := String(m["id"])
		if not _phase_ok(e, m) or int(m.get("sp", 0)) > e.sp:
			continue
		if m.get("special", "") == "continue":
			if int(e.uses.get(id, 0)) < int(m.get("max_uses", 2)) and not _downed_allies(e).is_empty():
				return m
			continue
		if e.uses.get("force_" + id, 0) == 1:
			e.uses["force_" + id] = 2
			return m
		if e.uses.get("cancel_" + id, 0) == 1 and _clock_due(e, m):
			e.uses["cancel_" + id] = 0
			_say("%s skips %s." % [e.display_name, m["name"]])
			continue
		if m.has("hp_below_once") and not e.uses.has(id) and float(e.hp) < float(m["hp_below_once"]) * e.max_hp:
			return m
		if m.get("special", "") == "kebality":
			if _kebality_due(e, m):
				return m
			continue
		if m.get("special", "") == "mirror_match":
			if _clock_due(e, m) and _same_kind(e).size() >= int(m.get("requires_same_kind", 2)) - 1:
				return m
			continue
		if _clock_due(e, m):
			return m
	return {}


func _clock_due(e: BattleUnit, m: Dictionary) -> bool:
	var every := 0
	if m.has("clock"):
		var c: Dictionary = m["clock"]
		every = int(c.get(str(e.phase), c.get("1", 0)))
	elif m.has("every"):
		every = int(m["every"])
	if every <= 0:
		return false
	return round_number % every == 0 and int(e.cooldown_until.get(String(m["id"]), 0)) <= round_number


## Shish Kahn: cued by FINISH HIM! (handled there); on his own every 4th round if the Count is
## down, or every 3rd round in phase 3. Once per phase.
func _kebality_due(e: BattleUnit, m: Dictionary) -> bool:
	if e.uses.has("kebality_phase_%d" % e.phase):
		return false
	var count_up := enemies.any(func(x: BattleUnit) -> bool: return x.id == "count_continue" and not x.is_down())
	if e.phase >= 3:
		return round_number % 3 == 0
	return not count_up and round_number % 4 == 0


func _same_kind(e: BattleUnit) -> Array:
	return _allies(e).filter(func(x: BattleUnit) -> bool: return x.id == e.id)


func _downed_allies(e: BattleUnit) -> Array:
	return enemies.filter(func(x: BattleUnit) -> bool: return x != e and x.is_down())


func _phase_ok(e: BattleUnit, m: Dictionary) -> bool:
	return not m.has("phases") or Array(m["phases"]).has(e.phase)


func _weight(e: BattleUnit, m: Dictionary) -> float:
	var w = m.get("weight", null)
	if w == null:
		return 0.0
	var base := 0.0
	if w is Dictionary:
		base = float(w.get(str(e.phase), w.get("1", 0)))
	else:
		base = float(w)
	var alone := _allies(e).is_empty()
	if alone and m.has("last_standing_weight"):
		base = float(m["last_standing_weight"])
	if alone and m.has("solo_weight"):
		base = float(m["solo_weight"])
	if m.has("partner_down_weight") and _same_kind(e).is_empty() and _fought.filter(func(x: BattleUnit) -> bool: return x.id == e.id).size() > 1:
		base = float(m["partner_down_weight"])
	return base


func _pick_move(e: BattleUnit) -> Dictionary:
	var pool: Array = []
	var total := 0.0
	for m in e.moves:
		if _is_scheduled(m) or not _phase_ok(e, m):
			continue
		var w := _weight(e, m)
		if w <= 0.0 or int(m.get("sp", 0)) > e.sp or round_number < int(m.get("min_round", 0)):
			continue
		if int(e.cooldown_until.get(String(m["id"]), 0)) > round_number:
			continue
		if m.get("requires_ally", false) and _allies(e).is_empty():
			continue
		if m.get("requires_balance", false) and (balance_due <= 0 or wallet == null or int(wallet.sovs) <= 0):
			continue
		if m.get("requires_self_negative", false) and not NEGATIVE.any(func(s: String) -> bool: return e.has_status(s)):
			continue
		if m.has("target_lacks") and _bros_without(String(m["target_lacks"])).is_empty():
			continue
		if m.get("target", "") == "ally" and _allies(e).is_empty():
			continue
		pool.append([m, w])
		total += w
	if pool.is_empty():
		return {}
	var roll := _rng.randf() * total
	for pair in pool:
		roll -= float(pair[1])
		if roll < 0.0:
			return pair[0]
	return pool[-1][0]


## Moves that only fire on their clock / gate / cue, never from the weighted table.
static func _is_scheduled(m: Dictionary) -> bool:
	return m.has("clock") or m.has("every") or m.has("hp_below_once") \
		or ["continue", "kebality", "mirror_match"].has(String(m.get("special", "")))


func _bros_without(status: String) -> Array:
	return party.filter(func(b: BattleUnit) -> bool: return b.targetable() and not b.has_status(status))


## The villain's own end-of-turn effects that run after the regular countdown.
func _apply_after(e: BattleUnit) -> void:
	if e.uses.get("tele_def_half", 0) == 1:
		e.uses.erase("tele_def_half")
		e.def_half_turns = maxi(e.def_half_turns, 1)
	if e.uses.has("tele_crit"):
		e.crit_bonus = float(e.uses["tele_crit"])
		e.crit_bonus_turns = 1
		e.uses.erase("tele_crit")
	var after: Dictionary = e.uses.get("after", {})
	e.uses.erase("after")
	if after.is_empty():
		return
	e.skip_turns += int(after.get("skip", 0))
	if after.has("def_half"):
		e.def_half_turns = maxi(e.def_half_turns, int(after["def_half"]))
	if after.has("crit_bonus"):
		e.crit_bonus = float(after["crit_bonus"])
		e.crit_bonus_turns = 1
	if after.get("grit_zero", false):
		e.grit_zero_turns = 1
		e.grit_low = 0
	if after.has("grit_to"):
		e.grit_zero_turns = 1
		e.grit_low = int(after["grit_to"])
	if after.get("drop_layers", false):
		e.layers = 0


func _move_mult(m: Dictionary, e: BattleUnit) -> float:
	if m.has("mult"):
		if m.has("solo_mult") and _same_kind(e).is_empty():
			return float(m["solo_mult"])
		return float(m["mult"])
	return float(BattleRulings.DAMAGE_WORDS.get(String(m.get("word", "standard")), 1.0))


func _move_targets(e: BattleUnit, m: Dictionary) -> Array[BattleUnit]:
	var bros := living_party().filter(func(b: BattleUnit) -> bool: return b.targetable())
	var out: Array[BattleUnit] = []
	if bros.is_empty():
		return out
	match String(m.get("target", "one")):
		"all":
			out.assign(bros)
		"lowest_hp":
			bros.sort_custom(func(a: BattleUnit, b: BattleUnit) -> bool: return a.hp < b.hp)
			out.append(bros[0])
		"highest_hp":
			bros.sort_custom(func(a: BattleUnit, b: BattleUnit) -> bool: return a.hp > b.hp)
			out.append(bros[0])
		"prefer_or_lowest_hp":
			# e.g. Past Due: always Lord Pilsner while he stands (the tab is in his name).
			var named := bros.filter(func(b: BattleUnit) -> bool: return b.id == String(m.get("prefer", "")))
			if not named.is_empty():
				out.append(named[0])
			else:
				bros.sort_custom(func(a: BattleUnit, b: BattleUnit) -> bool: return a.hp < b.hp)
				out.append(bros[0])
		_:
			var pool := bros
			if m.has("target_lacks"):
				pool = bros.filter(func(b: BattleUnit) -> bool: return not b.has_status(String(m["target_lacks"])))
			if m.get("not_same_target_twice", false) and pool.size() > 1:
				pool = pool.filter(func(b: BattleUnit) -> bool: return b.id != e.last_target)
			if pool.is_empty():
				pool = bros
			out.append(pool[_rng.randi_range(0, pool.size() - 1)])
	return out


func _resolve(e: BattleUnit, m: Dictionary) -> void:
	var id := String(m["id"])
	if not _is_telegraphed(m):
		e.uses[id] = int(e.uses.get(id, 0)) + 1
	if m.has("cooldown"):
		e.cooldown_until[id] = round_number + int(m["cooldown"])
	e.sp -= int(m.get("sp", 0))
	if m.has("after"):
		e.uses["after"] = m["after"]
	var special := String(m.get("special", ""))
	if special == "palette_spray":
		_palette_spray(e, m)
		return
	if special == "dive":
		_dive(e)
		return
	if special == "continue":
		_continue(e, m)
		return
	if special == "re_release":
		_re_release(e, m)
		return
	if special == "sauce_swap":
		_sauce_swap(e)
		return
	if special == "guard":
		e.guarding = true
		_say(_uses(e, String(m["name"])))
		return
	if special == "finish_him" and _cue_kebality(e):
		return
	if special == "kebality":
		e.uses["kebality_phase_%d" % e.phase] = 1
	_say(_uses(e, String(m["name"])))
	if m.has("log"):
		_say(String(m["log"]))
	match String(m.get("target", "one")):
		"self":
			if m.has("def_buff"):
				if m.has("stacks"):
					e.layers = mini(e.layers + 1, int(m["stacks"]))
				else:
					e.def_buffs.append({"amount": int(m["def_buff"]), "turns": int(m.get("buff_turns", 1))})
			return
		"allies":
			for x in enemies:
				if not x.is_down():
					x.def_buffs.append({"amount": int(m["def_buff"]), "turns": int(m.get("buff_turns", 1))})
			return
		"ally", "ally_or_self":
			var allies := _allies(e)
			var who: BattleUnit = e if allies.is_empty() else allies[_rng.randi_range(0, allies.size() - 1)]
			_apply_status(who, String(m.get("status", "")), int(m.get("status_turns", 1)), 1.0)
			return
	var targets := _move_targets(e, m)
	if targets.is_empty():
		return
	if special == "mirror_match":
		_mirror_match(e, m, targets[0])
		return
	if special == "shake_down":
		var t := targets[0]
		e.last_target = t.id
		var r := _hit(e, t, _move_mult(m, e), false, int(m.get("accuracy_steps", 0)))
		if r["hit"]:
			_shake_down(e, t, int(m.get("collect_sovs", 5)))
		return
	if special == "pincer":
		# Every standing enemy of this kind hits the same bro in one action.
		var t := targets[0]
		e.last_target = t.id
		for att in [e] + _same_kind(e):
			if t.is_down():
				break
			var r := _hit(att, t, _move_mult(m, att), false, int(m.get("accuracy_steps", 0)))
			if r["hit"]:
				_move_effects(e, m, t)
		return
	var hits := 1
	if m.has("hits"):
		var hd = m["hits"]
		hits = int(hd.get(str(e.phase), hd.get("1", 1))) if hd is Dictionary else int(hd)
	var dealt := false
	for t in targets:
		e.last_target = t.id
		for i in hits:
			var aimed := t
			if String(m.get("target", "")) == "random" and i > 0:
				var bros := living_party().filter(func(b: BattleUnit) -> bool: return b.targetable())
				if bros.is_empty():
					break
				aimed = bros[_rng.randi_range(0, bros.size() - 1)]
			if String(m.get("type", "none")) != "none":
				if hits == 1 and targets.size() == 1:
					aimed = _redirect(e, aimed, true)
					if aimed == null:
						continue
				var r := _hit(e, aimed, _move_mult(m, e), m.get("type") == "social", int(m.get("accuracy_steps", 0)))
				dealt = dealt or r["hit"]
				if not r["hit"]:
					continue
			_move_effects(e, m, aimed)
	if m.has("land_log") and dealt:
		_say("%s: \"%s\"" % [e.display_name, m["land_log"]])
	if dealt and e.data.has("ponder_chance") and _rng.randf() < float(e.data["ponder_chance"]):
		e.uses["ponder"] = 1


## Statuses, drains, steals and the swallow, on one bro the move reached.
func _move_effects(e: BattleUnit, m: Dictionary, t: BattleUnit) -> void:
	if String(m.get("special", "")) == "swallow":
		t.gone_turns = 1
		t.gone_status = {String(m["status"]): int(m.get("status_turns", 1))}
		_say("%s swallows %s whole." % [e.display_name, t.display_name])
		return
	if m.has("bravado_drain"):
		var amt := BattleRulings.HONK_DRAIN if m["bravado_drain"] is String else int(m["bravado_drain"])
		t.gain_bravado(-amt)
		_say("%s loses %d Bravado." % [t.display_name, amt])
	if m.has("steal_sovs"):
		_steal(t, int(m["steal_sovs"]))
	var chance := float(m.get("status_chance", 1.0))
	if m.get("always_on", "") == t.id:
		chance = 1.0
	_apply_status(t, String(m.get("status", "")), int(m.get("status_turns", 1)), chance)
	if m.has("status2"):
		_apply_status(t, String(m["status2"]), int(m.get("status2_turns", 1)), float(m.get("status2_chance", 1.0)))


func _steal(t: BattleUnit, amount: int) -> void:
	if wallet == null:
		return
	var taken := mini(amount, maxi(int(wallet.sovs), 0))
	wallet.sovs -= taken
	sovs_taken += taken
	_say("%s pays %d SOVS." % [t.display_name, taken] if taken != 1 else "%s pays 1 SOV." % t.display_name)


## Shake Down Payment (round v31): up to `amount` SOVS fall out of the wallet and go on the tab,
## never more than the balance due.
func _shake_down(e: BattleUnit, t: BattleUnit, amount: int) -> void:
	var taken := mini(mini(amount, balance_due), maxi(int(wallet.sovs), 0)) if wallet != null else 0
	if taken <= 0:
		return
	wallet.sovs -= taken
	balance_due -= taken
	sovs_collected += taken
	_say("%s holds %s upside down and shakes. %s, a Razr and a burned Linkin Park CD hit the carpet. %s keeps the SOVS. He hands back the CD after reading the tracklist. Balance due: %s." % [
		e.display_name, t.display_name, sovs(taken), e.display_name, sovs(balance_due)])
	if t.id == "lord_pilsner":
		_say("%s: \"Bro. Dinner first.\"" % t.display_name)


static func sovs(n: int) -> String:
	return "1 SOV" if n == 1 else "%d SOVS" % n


func _palette_spray(e: BattleUnit, m: Dictionary) -> void:
	var pal: Dictionary = Dictionary(e.data.get("palettes", {})).get(e.palette, {})
	_say("%s uses %s!" % [e.display_name, pal.get("spray", m["name"])])
	if pal.has("log"):
		_say(String(pal["log"]))
	var targets := _move_targets(e, m)
	if targets.is_empty():
		return
	var t := _redirect(e, targets[0], true)
	if t == null:
		return
	var r := _hit(e, t, _move_mult(m, e), pal.get("type", "physical") == "social", 0)
	if r["hit"]:
		_apply_status(t, String(pal.get("status", "")), 2, float(pal.get("chance", 0.0)))


func _sauce_swap(e: BattleUnit) -> void:
	var partner: BattleUnit = null
	for x in _same_kind(e):
		partner = x
		break
	if partner == null:
		_say("%s swaps with itself. Nothing happens." % e.display_name)
		return
	var log_line := ""
	for m in e.moves:
		if m["id"] == "sauce_swap":
			log_line = String(m.get("log", ""))
	if log_line != "":
		_say(log_line)
	for x in [e, partner]:
		for s in NEGATIVE:
			x.statuses.erase(s)
	var p := e.palette
	e.palette = partner.palette
	partner.palette = p
	var n := e.display_name
	e.display_name = partner.display_name
	partner.display_name = n


func _dive(e: BattleUnit) -> void:
	_say("%s dives!" % e.display_name)
	e.gone_turns = 1          # can't be targeted until it surfaces on its next turn
	e.uses["surfacing"] = 1
	for x in _allies(e):
		x.speed_bonus = 2
		x.speed_bonus_turns = 1


func _surface(e: BattleUnit) -> void:
	e.uses.erase("surfacing")
	_say("%s surfaces." % e.display_name)
	var dip: Dictionary = {}
	for m in e.moves:
		if m["id"] == "buy_the_dip":
			dip = m
	for t in living_party().filter(func(b: BattleUnit) -> bool: return b.targetable()):
		_hit(e, t, float(BattleRulings.DAMAGE_WORDS["light"]), false, 0)
		if not dip.is_empty():
			_move_effects(e, dip, t)
	if not dip.is_empty() and dip.has("log"):
		_say(String(dip["log"]))
	e.uses["after"] = {"def_half": 1}
	_say("%s is under audit." % e.display_name)


func _continue(e: BattleUnit, m: Dictionary) -> void:
	var downed := _downed_allies(e)
	if downed.is_empty():
		return
	var ally: BattleUnit = downed[0]
	var cost := int(m.get("cost_sovs", 3))
	if wallet == null or int(wallet.sovs) < cost:
		_say("INSUFFICIENT CREDITS")
		if m.has("log"):
			_say(String(m["log"]))
		var bros := living_party()
		if not bros.is_empty():
			bros.sort_custom(func(a: BattleUnit, b: BattleUnit) -> bool: return a.hp < b.hp)
			_apply_status(bros[0], "broke_af", -1, 1.0)
		return
	wallet.sovs -= cost
	ally.hp = maxi(roundi(ally.max_hp * float(m.get("revive_pct", 0.5))), 1)
	ally.meter = float(ally.hp)
	ally.statuses.clear()
	ally.telegraph = {}
	ally.skip_turns = 0
	_say("%s revives %s for %d SOVS." % [e.display_name, ally.display_name, cost])
	if m.has("success_log"):
		_say("%s: \"%s\"" % [e.display_name, m["success_log"]])


func _re_release(e: BattleUnit, m: Dictionary) -> void:
	_say("%s uses %s!" % [e.display_name, m["name"]])
	for x in [e] + _allies(e):
		x.heal(roundi(x.max_hp * float(m.get("heal_pct", 0.25))))
	for s in NEGATIVE:
		e.statuses.erase(s)
	_say("%s and her lineup heal." % e.display_name)
	if e.id == JARMILA:
		_revise(e, int(e.uses.get("revisions", 0)) + 1)
	for p in e.data.get("phases", []):
		if p.get("or_after", "") == "re_release" and e.phase < int(p["phase"]):
			_enter_phase(e, p)


## FINISH HIM! with Shish Kahn up and Kebality ready starts his wind-up instead of the buff.
func _cue_kebality(count: BattleUnit) -> bool:
	for k in _allies(count):
		if k.id != "shish_kahn" or not k.telegraph.is_empty():
			continue
		for m in k.moves:
			if m.get("special", "") == "kebality" and not k.uses.has("kebality_phase_%d" % k.phase) and k.sp >= int(m.get("sp", 0)):
				_say("%s: \"FINISH HIM!\"" % count.display_name)
				_wind_up(k, m)
				return true
	return false


func _mirror_match(e: BattleUnit, m: Dictionary, t: BattleUnit) -> void:
	var partners := _same_kind(e)
	if partners.is_empty():
		_hit(e, t, _move_mult(m, e), false, 0)
		return
	var p: BattleUnit = partners[0]
	for x in [e, p]:
		if t.targetable():
			_hit(x, t, _move_mult(m, e), false, 0)
	p.skip_turns += 1


## Jarmila's marquee: her base name plus `words` revision words (never shrinks).
func _revise(e: BattleUnit, words: int) -> void:
	words = maxi(words, int(e.uses.get("revisions", 0)))
	e.uses["revisions"] = words
	e.display_name = jarmila_name(String(e.uses.get("base_name", e.display_name)), words)


static func jarmila_name(base: String, words: int) -> String:
	var out := base
	for i in words:
		out += " " + String(JARMILA_WORDS[i % JARMILA_WORDS.size()])
	return out


## The soggy pile: what Buy the Dip took, less the 20% management fee (villain_leftovers).
func soggy_pile() -> int:
	return sovs_taken - roundi(sovs_taken * BattleRulings.SOGGY_PILE_FEE)


# --- misc --------------------------------------------------------------------------------------

func _avg_speed(units: Array[BattleUnit]) -> float:
	var live := units.filter(func(u: BattleUnit) -> bool: return not u.is_down())
	if live.is_empty():
		return 0.0
	var total := 0.0
	for u in live:
		total += u.battle_speed()
	return total / live.size()


## "X uses Y!", without doubling a name that already shouts ("EXTRA CRISPY!").
static func _uses(e: BattleUnit, move: String) -> String:
	var bare := move.trim_suffix("\"")
	return "%s uses %s" % [e.display_name, move] + ("" if bare.ends_with("!") or bare.ends_with("?") else "!")


func _say(text: String) -> void:
	if text != "":
		events.append({"text": text})
