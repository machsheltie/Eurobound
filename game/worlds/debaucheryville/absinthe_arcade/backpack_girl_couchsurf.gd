class_name BackpackGirlCouchsurf
extends RefCounted
## Backpack Girl Who Never Left's couchsurf at the Absinthe Arcade (Eurobound-spr0): the approved
## one-night stand (WritingRoom/tasks/20261112_1518_backpack_girl_one_night_stand/final.md; Desk
## Eurobound-3ho-q13: Lord Pilsner, "The Book Takes the Ring") routed through the four Couchsurfing
## Chronicles states (design/quests/debaucheryville/couchsurfingchroniclesdebaucheryville.md:148-200;
## Desk Eurobound-3ho-q14: "Approve all: ring stays a story beat, skip the pick when infected, apply
## the 4 fixes").
##
## The lines are data: assets/data/npcs/conversations/debaucheryville_npc_backpack_girl_01.json, one
## chain per segment. This class only picks the segments for the state, plays each through
## ConversationWalker, moves the clock between them and grants the payload once.
##   State 1 CLEAR / 3 SUPPRESSED-CLEAN: approach, pick, goes, [02:40] cutaway, [07:40] morning,
##     payload, rationalisations.
##   State 2 INFECTED: approach, then the refusal (it sets FLAG_REFUSED); the pick is skipped, no night,
##     no payload.
##   State 4 SUPPRESSED-CALLBACK: the sting, then State 1, with her closing line after the morning.
## The ring is a story beat only: no item, no flag, no SOVS.

const NPC_ID := "debaucheryville_npc_backpack_girl_01"
## Her floor nest's trigger in the hall (arcade rework plan H11, debaucheryville_interactions.json
## backpack_girl_couchsurf_hook). Its anchor is placed with the nest prop (Eurobound-fbqk).
const INTERACT_ID := "backpack_girl_couchsurf_hook"
const FLAG_REFUSED := "backpack_girl_refused_while_infected"
const FLAG_COMPLETED := "chronicles_entry_completed_" + NPC_ID
const HERP := "the_herp"
const BALLAD_ID := "item_ballad_of_the_bros"
## Canonical payload: -10 Bravado (couchsurfingchroniclesdebaucheryville.md:141, final.md:217).
## TODO(author ruling, see bead filed under Eurobound-spr0): the docs do not say which bro loses it.
## It is taken from every bro until the author rules.
const BRAVADO_LOSS := 10
## Minutes into the day: the cutaway (final.md:117) and the morning-after (final.md:147).
const CUTAWAY_AT := 2 * 60 + 40
const MORNING_AT := 7 * 60 + 40

const CLOCK_CUTAWAY := "@cutaway_clock"
const CLOCK_MORNING := "@morning_clock"
const PAYLOAD := "@payload"
const NIGHT := ["pick", "goes", CLOCK_CUTAWAY, "cutaway", CLOCK_MORNING, "morning"]

## The state the last play() ran (1-4), 0 before any.
var played_state := 0
var errors: Array = []


## The four states (design/quests/general_quests/couchsurfingchronicles.md, THE FOUR STATES).
## `coin_equipped`: whether a bro wears item_gold_circle_coin. There are no equipment slots yet
## (Eurobound-t1gn), so the caller says, as NavigationRoll's ctx map_equipped does.
static func state_for(state, coin_equipped: bool) -> int:
	if not FieldStatus.has(state, HERP):
		return 1
	if not coin_equipped:
		return 2
	return 4 if bool(state.flags.get(FLAG_REFUSED, false)) else 3


static func steps_for(couch_state: int) -> Array:
	match couch_state:
		2:
			return ["approach", "s2_refusal"]
		4:
			return ["s4_sting", "approach"] + NIGHT + ["s4_closing", PAYLOAD, "rationalisations"]
		_:
			return ["approach"] + NIGHT + [PAYLOAD, "rationalisations"]


## Plays the scene for the party's state. `conversation` is DataRepo.get_dialogue_tree(NPC_ID).
## Bad data ends the scene where it broke; no payload is granted after an error.
func play(conversation: Dictionary, box: DialogueBox, state, coin_equipped := false) -> void:
	errors = []
	played_state = state_for(state, coin_equipped)
	var nodes: Dictionary = conversation.get("nodes", {})
	for step: String in steps_for(played_state):
		if step == CLOCK_CUTAWAY or step == CLOCK_MORNING:
			await box.beat()
			advance_to(state, CUTAWAY_AT if step == CLOCK_CUTAWAY else MORNING_AT)
		elif step == PAYLOAD:
			grant_payload(state)
		elif not nodes.has(step):
			errors.append("%s: segment '%s' is missing" % [NPC_ID, step])
			push_warning("BackpackGirlCouchsurf: " + errors[-1])
			break
		else:
			var segment := conversation.duplicate()
			segment["start"] = step
			var walker := ConversationWalker.new()
			await walker.play(segment, box, state)
			if not walker.errors.is_empty():
				errors.append_array(walker.errors)
				break
	box.close()


## The clock jumps forward to the next `minute_of_day` (today's if it is still ahead).
static func advance_to(state, minute_of_day: int) -> void:
	var now := GameClock.minutes(state)
	var target := GameClock.day(state) * GameClock.DAY + minute_of_day
	if target < now:
		target += GameClock.DAY
	GameClock.set_time(state, target)


## First-time payload only (Couchsurfing Chronicles payload rule): -10 Bravado, never below zero,
## and the Ballad of the Bros. Sets FLAG_COMPLETED.
static func grant_payload(state) -> void:
	if bool(state.flags.get(FLAG_COMPLETED, false)):
		return
	for member: Dictionary in state.party:
		member["bravado"] = maxi(int(member.get("bravado", 0)) - BRAVADO_LOSS, 0)
	state.add_item(BALLAD_ID)
	state.flags[FLAG_COMPLETED] = true
