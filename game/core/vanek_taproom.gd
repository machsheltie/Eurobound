class_name VanekTaproom
extends RefCounted
## Dr. Miloš Vaněk's rules at The Cracked Bottle bar in The Absinthium Taproom.
## Spec: design/worlds/debaucheryville/the_absinthium_taproom.md (opener check :34-37, stamp
## conditions :207-211, stamp speech :213-214, Absinthe Lager :216-238) and
## design/items/brewery_tour/beer_absinthium_taproom_item.md.
## Order of play: keychain gate, then opener check, then the Lager sale (12 SOVS, keychain
## discount), then the stamp (all four conditions). State is GameState (flags + inventory).

const BREWERY_ID := "absinthium_taproom"
const LAGER_ID := "beer_absinthium_taproom"
const LAGER_PRICE := 12
const FLAG_LAGER_BOUGHT := "vanek_lager_bought"
const FLAG_SURVEY_CONSENTED := "vanek_survey_consented"
const FLAG_GREETED := "vanek_greeted"

const GATE_NO_KEYCHAIN := "no_keychain"
const GATE_NO_OPENER := "no_opener"
const GATE_OK := "ok"

const SALE_BOUGHT := "bought"
const SALE_CANNOT_AFFORD := "cannot_afford"
const SALE_REFUSED := "refused"  ## failed the gate

const SPEAKER := "Dr. Vaněk"

## Verbatim from the location doc (:36-37, :213-214, :235-238).
const LINE_NO_KEYCHAIN := "No Publandia key, no brewery tour access. The Continental Trail has protocols. Return when properly credentialed."
const LINE_BOTH_OPENERS := "The cracked glass. You've navigated the mirrors. Either way, you've committed. The Absinthe Lager awaits. Prepare for... introspection."
const LINES_SERVING := [
	"The Absinthe Lager. My signature creation. The green fairy is IN the beer. Metaphorically. And slightly literally.",
	"You may experience mild disorientation. This is intentional. If you DON'T feel disoriented, tell me immediately — I need to adjust the formula.",
	"30% confusion chance. 100% authenticity. Those are better odds than reality offers.",
]
const LINE_STAMP_SPEECH := "Congratulations. You've seen yourself. Not everyone does — some people navigate the mirrors without ever looking INTO them. You looked. The stamp is proof. The memory is punishment. Or reward. The distinction is philosophical."

## TODO (author / Writers' Room): gaps the docs do not fill. Empty = nothing is said, nothing invented.
## Keychain held, no Absinthium opener: the old line is struck (:35); the Writers' Room writes it (v44).
const TODO_LINE_KEYCHAIN_NO_OPENER := ""
## The player cannot pay for the Lager.
const TODO_LINE_CANNOT_AFFORD := ""
## "Vaněk's Survey" (APPROVED, author 2026-11-13, Desk 4ti-q1/q2; doc :304-331). Every answer is
## accepted, none is right, none changes a stat; Vaněk's reply is the same whichever is picked.
const SURVEY_OPENER := "Participation is voluntary. Leaving is also voluntary. Nobody has done it yet."
const SURVEY_QUESTIONS: Array = [
	{
		"prompt": "On a scale of one to ten, how many of you are there right now?",
		"answers": ["Three", "Ten", "Which ones count?"],
		"reply": "Consistent with the control group. The control group is a mirror.",
	},
	{
		"prompt": "When you looked into the mirrors, who looked back?",
		"answers": ["Me, but hotter", "My dad", "Nobody, I was busy"],
		"reply": "Noted. He usually does.",
	},
	{
		"prompt": "Describe the green fairy in one word.",
		"answers": ["Hot", "Mean", "Mom?"],
		"reply": "Everyone says the third one eventually.",
	},
	{
		"prompt": "How many drinks have you had tonight?",
		"answers": ["Like four", "What counts as a drink", "I don't count, I'm not a nerd"],
		"reply": "I will write 'like four.' I always write 'like four.'",
	},
	{
		"prompt": "Any side effects?",
		"answers": ["My teeth feel loud", "I can taste the color green", "None, I'm built different"],
		"reply": "'Built different.' Third time this week. I've added it to the list of symptoms.",
	},
	{
		"prompt": "Final question. Do you consent to this survey?",
		"answers": ["Yes", "What survey", "Yeah bro"],
		"reply": "Retroactive consent. The ethics board will be thrilled. The ethics board is me.",
	},
]
const SURVEY_CLOSER := "Thank you. Your data will be used for science, or for my memoirs. The distinction is philosophical."
## Reward (Desk 4ti-q2 option B): the Participant Wristband (inventory only; whether a bro wears it
## is NOT ruled) plus the "The Research Subject" selfie variant.
const WRISTBAND_ID := "participant_wristband"
const FLAG_SURVEY_DONE := "vanek_survey_done"
## No selfie system exists in game/ yet; the variant is only recorded as this flag.
const FLAG_SELFIE_RESEARCH_SUBJECT := "selfie_vanek_research_subject"
## Callback lines once stamped / on return visits: not written.
const TODO_LINES_CALLBACK: Array = []
## Line he says while handing over the opener on the backfill: not ruled, the Writers' Room writes it.
const TODO_LINE_OPENER_HANDOVER := ""

## Opener backfill (Desk orch-vanek-q5-backfill, 2026-11-13): the first time the party returns to him
## holding the keychain but without his opener, he hands it over (once; flag-guarded).
const FLAG_OPENER_BACKFILLED := "vanek_opener_backfilled"

## His hours (Desk orch-vanek-q6-hours, 2026-11-13): at the bar 20:00-04:00 game time, wrapping past
## midnight; the bar is empty otherwise. Uses GameClock (doc :16).
const OPEN_HOUR := 20
const CLOSE_HOUR := 4


static func is_open(hour: int) -> bool:
	return GameClock.in_hours(hour, OPEN_HOUR, CLOSE_HOUR)


static func is_open_now(state) -> bool:
	return is_open(GameClock.hour(state))


## Hands over the Absinthium opener once, when the party holds the keychain and lacks the opener.
## True only on the call that hands it over.
static func backfill_opener(state) -> bool:
	if bool(state.flags.get(FLAG_OPENER_BACKFILLED, false)):
		return false
	if not has_keychain(state) or BreweryPassport.has_opener(state, BREWERY_ID):
		return false
	if not BreweryPassport.award_opener(state, BREWERY_ID):
		return false
	state.flags[FLAG_OPENER_BACKFILLED] = true
	return true


## The survey is open once, and only past the keychain gate and opener check.
static func can_take_survey(state) -> bool:
	return gate(state) == GATE_OK and not bool(state.flags.get(FLAG_SURVEY_DONE, false))


## Finishes the survey: grants the wristband once and records the selfie variant. No stat is touched.
## True only on the call that grants. Consent is recorded by the caller as it is asked.
static func complete_survey(state) -> bool:
	if not can_take_survey(state):
		return false
	state.flags[FLAG_SURVEY_CONSENTED] = true
	state.flags[FLAG_SURVEY_DONE] = true
	state.flags[FLAG_SELFIE_RESEARCH_SUBJECT] = true
	state.add_item(WRISTBAND_ID, 1)
	return true


static func has_keychain(state) -> bool:
	return int(state.inventory.get(BreweryPassport.KEYCHAIN, 0)) > 0


## Keychain gate first, then the opener check.
static func gate(state) -> String:
	if not has_keychain(state):
		return GATE_NO_KEYCHAIN
	if not BreweryPassport.has_opener(state, BREWERY_ID):
		return GATE_NO_OPENER
	return GATE_OK


## 12 SOVS less the keychain discount.
static func lager_price(state) -> int:
	return BreweryPassport.discounted_bar_price(state, LAGER_PRICE)


static func buy_lager(state) -> String:
	if gate(state) != GATE_OK:
		return SALE_REFUSED
	if not state.spend_sovs(lager_price(state)):
		return SALE_CANNOT_AFFORD
	state.add_item(LAGER_ID, 1)
	state.flags[FLAG_LAGER_BOUGHT] = true
	return SALE_BOUGHT


## The four unlock conditions (:208-211), each true or false.
static func stamp_conditions(state) -> Dictionary:
	return {
		"maze": bool(state.flags.get(TaproomMaze.FLAG_COMPLETED, false)),
		"wisp": bool(state.flags.get(TaproomBattle.FLAG_WISP_DEFEATED, false)) \
				or bool(state.flags.get(TaproomBattle.FLAG_WISP_SURVIVED, false)),
		"lager": bool(state.flags.get(FLAG_LAGER_BOUGHT, false)),
		"keychain": has_keychain(state),
	}


static func stamp_ready(state) -> bool:
	return gate(state) == GATE_OK and not stamp_conditions(state).values().has(false)


## Awards the Absinthium Seal when every condition holds. False if unmet or already stamped.
static func try_stamp(state) -> bool:
	if not stamp_ready(state):
		return false
	return BreweryPassport.award_stamp(state, BREWERY_ID)
