class_name BattleRulings
extends RefCounted
## The round v27 (ef4_) battle rulings, approved by the author 2026-11-11: the values the nine
## Arcade villain docs needed on top of the round v26 numbers in BattleRules.

## ef4_damage_words: a move that names only a size.
const DAMAGE_WORDS := {"light": 0.7, "low": 0.7, "standard": 1.0, "moderate": 1.2, "heavy": 1.5}
## ef4_accuracy: base hit chance and the size of one accuracy step (-3 steps = 68%, the Fireball).
const BASE_HIT_PCT := 95.0
const HIT_PCT_PER_STEP := 9.0
## ef4_honk_drain: Honk If You've Peaked takes this much Bravado from each bro.
const HONK_DRAIN := 2
## ef4_status_conflict = villain_docs: Embarrassed -20% ATK and -2 Bravado a turn, no Bravado-cost
## moves (the -20% and the -2 live in status_effects.json, entry "embarrassed", Eurobound-0dde);
## Gains Bro +20% ATK; Hardcore Gamer +1% crit (master list).
const GAINS_BRO_ATK := 1.2
## ef4_down_after_win: a downed bro leaves a won fight with this much HP.
const DOWN_AFTER_WIN_HP := 1
## ef4_multi_tickets = sum: a win pays the sum of every villain's ticket_reward.
const TICKETS_SUM := true
## ef4_level_band: Street Fighter always releases two Swaps until levels exist.
const SF_SWAPS := 2
## ef4_weights_short and ef4_full_crossing_locked: weights are scaled to their own total, which is
## what a weighted pick does (BattleCore._pick_move, ArcadeBattle.pick_release).
## ef4_social_damage: Social damage = (Charm + Bravado Mod) - target's Grit (BattleCore._hit).
## ef4_confused_stun: Stun loses the next turn and doesn't stack; Confused picks a random target
## from everyone on the field except the user.
## ef4_lasting_statuses = persist: these outlive the fight, kept on the party member.
const LASTING_STATUSES := ["tourist_trap_victim", "food_poisoning", "broke_af"]
const FOOD_POISONING_BATTLES := Vector2i(5, 8)
## villain_leftovers = all: the Sinking Fund's soggy pile pays back what Buy the Dip took, less a
## 20% management fee, on a win only.
const SOGGY_PILE_FEE := 0.2

## Round v28 (author 2026-11-11).
## cabinet_difficulty = hp: every Arcade cabinet villain fights with +50% HP (rounded).
const CABINET_HP_MULT := 1.5
## status_durations = approve: where a villain doc names no length, Embarrassed lasts 2 turns and
## Grease Fingers 4. A length written in a villain doc (Croc Monsieur's 3) stands.
const EMBARRASSED_TURNS := 2
const GREASE_FINGERS_TURNS := 4

## Eurobound-rl4c, Combos (author, Eurobound Desk Eurobound-rl4c-q2, 2026-11-16, "Approve as
## proposed"; docs/superpowers/specs/2026-11-16-eurobound-rl4c-numbers-proposal.md §2). The starter
## set itself is assets/data/skills/combos.json.
## rl4c_roll: one roll per combo on the participants' combined Bravado (sum of current over sum of
## max) on the v26 thirds. rl4c_fail: a failed roll is that combo's backfire.
const COMBO_SUCCESS := {"high": 0.8, "mid": 0.6, "low": 0.4}
## rl4c_self_damage, rl4c_drain, rl4c_embarrassed_len: the sizes of a backfire.
const COMBO_SELF_DAMAGE := 5
const COMBO_BRAVADO_LOSS := 3
const COMBO_EMBARRASSED_TURNS := 2

## Eurobound-wuyu, Taunt (author, Eurobound Desk Eurobound-wuyu-q2, 2026-11-16, "Approve as
## proposed"; docs/superpowers/specs/2026-11-16-eurobound-wuyu-numbers-proposal.md §2).
## wuyu_taunt_chance: 50%, +5% a point the taunter's Charm beats the enemy's Grit, 10%..90%.
const TAUNT_BASE_PCT := 50.0
const TAUNT_PCT_PER_POINT := 5.0
const TAUNT_MIN_PCT := 10.0
const TAUNT_MAX_PCT := 90.0
## wuyu_taunt_effect: the target kinds a Taunt pulls onto the taunter (a move that targets one
## bro). "all", own-side moves and moves written for a named bro ("prefer", "always_on") stay.
const TAUNT_PULLS := ["one", "lowest_hp", "highest_hp", "random"]


static func taunt_pct(charm: int, grit: int) -> float:
	return clampf(TAUNT_BASE_PCT + TAUNT_PCT_PER_POINT * float(charm - grit), TAUNT_MIN_PCT, TAUNT_MAX_PCT)


## wuyu_beat_reading / wuyu_beat_wait (Eurobound-wuyu-q2): in a beat venue each action waits for
## the next beat of the venue's track, never longer than one beat; who acts when is unchanged
## (Speed + Bravado, v26). `track_time` is seconds into the track; bpm 0 = not a beat venue.
## wuyu_beat_where: no Debaucheryville venue is one, so nothing calls this yet.
static func beat_wait(track_time: float, bpm: float) -> float:
	if bpm <= 0.0:
		return 0.0
	var beat := 60.0 / bpm
	var into := fposmod(track_time, beat)
	if is_zero_approx(into) or is_equal_approx(into, beat):
		return 0.0
	return beat - into
