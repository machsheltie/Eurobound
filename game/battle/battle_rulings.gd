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
## moves; Gains Bro +20% ATK; Hardcore Gamer +1% crit (master list).
const EMBARRASSED_ATK := 0.8
const EMBARRASSED_DRAIN := 2
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
