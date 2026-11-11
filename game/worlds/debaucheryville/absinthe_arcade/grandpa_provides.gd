class_name GrandpaProvides
extends RefCounted
## Grandpa Provides (design/quests/debaucheryville/grandpa_provides.md, APPROVED round v30 as written,
## 1dae114). Scene 1 "The Tip" and Scene 3 "The Unsettled Tab"; every spoken line is verbatim from the
## doc. Stage directions are beats (the game has no narrator). Scene 2 (the girls) waits on the
## group's sprites and placement; it sets ROUND_BOUGHT.
## Round v30 defaults: the tip plays the first time the bros redeem prizes; the tab can be paid early
## at the counter ("Pleasure doing business with you, Grandpa."); the name is the quest title only.
## Numbers (round v25): tab 40 SOVS, service charge 10 SOVS flat, no second fight.

const QUEST_ID := "debaucheryville_sidequest_grandpa_provides_01"
const RING_TIPPED := "debaucheryville.absinthe_arcade.ring_tip_given"
const ROUND_BOUGHT := "debaucheryville.absinthe_arcade.cara_round_bought"
const TAB_PAID := "debaucheryville.absinthe_arcade.cara_tab_paid"
const AR_DEFEATED := "debaucheryville.absinthe_arcade.accounts_receivable_defeated"
const TAB_OPEN := "debaucheryville.absinthe_arcade.cara_tab_open"
## SOVS Accounts Receivable shook loose and put on the tab (round v31 ar_steal = a).
const TAB_CREDIT := "debaucheryville.absinthe_arcade.cara_tab_credit"
## Scene 2's banter at the bros' game has played (trigger A); the approach is then open.
const BANTER_PLAYED := "debaucheryville.absinthe_arcade.grandpa_banter_played"
const TAB_SOVS := 40
const SERVICE_CHARGE_SOVS := 10

const TOMAS := "TOMÁŠ"
const PILSNER := "PILSNER"
const BRADLEY := "BRADLEY"
const CHADWICK := "CHADWICK"
const WHITNEY := "WHITNEY"
const GIRLS := "GIRLS"
const BRYNLEIGH := "BRYNLEIGH"


static func _flag(state, id: String) -> bool:
	return bool(state.flags.get(id, false))


## The round was bought and nothing has settled it.
static func tab_due(state) -> bool:
	return _flag(state, ROUND_BOUGHT) and not _flag(state, TAB_PAID)


## Tomáš waits at the exit: the tab is due and the bros haven't fought their way out yet.
static func exit_confrontation_due(state) -> bool:
	return tab_due(state) and not _flag(state, AR_DEFEATED)


static func tab_amount(state) -> int:
	return TAB_SOVS + (SERVICE_CHARGE_SOVS if _flag(state, TAB_OPEN) else 0) - credit(state)


static func credit(state) -> int:
	return int(state.flags.get(TAB_CREDIT, 0))


## Shake Down Payment money goes on the tab.
static func add_credit(state, sovs: int) -> void:
	state.flags[TAB_CREDIT] = credit(state) + maxi(sovs, 0)


## Pays the whole tab. False (nothing taken) when the wallet is short.
static func pay(state) -> bool:
	var amount := tab_amount(state)
	if int(state.gold) < amount:
		return false
	state.gold -= amount
	state.flags[TAB_PAID] = true
	state.flags[TAB_OPEN] = false
	return true


## Fight won (or run from): the bros are out the door, the tab stays open with the service charge.
static func fled(state) -> void:
	state.flags[AR_DEFEATED] = true
	state.flags[TAB_OPEN] = true


## Fight lost: the tab and the service charge come out of the wallet; a short wallet is emptied and
## the rest waived. Returns true when it was waived.
static func lost(state) -> bool:
	var owed := maxi(TAB_SOVS + SERVICE_CHARGE_SOVS - credit(state), 0)  # never more than 50 in all
	var waived := int(state.gold) < owed
	state.gold = maxi(int(state.gold) - owed, 0)
	state.flags[TAB_PAID] = true
	state.flags[TAB_OPEN] = false
	return waived


## Scene 2, trigger A (round v25): with the group at the bar, the first finished cabinet fight.
static func banter_due(state) -> bool:
	return not _flag(state, BANTER_PLAYED) and not _flag(state, ROUND_BOUGHT)


static func approach_due(state) -> bool:
	return _flag(state, BANTER_PLAYED) and not _flag(state, ROUND_BOUGHT)


## Scene 2, at the bros' game.
static func the_banter(stage) -> void:
	var d: DialogueBox = stage.dialogue
	await d.say(BRADLEY, "No.")
	await d.say(PILSNER, "What?")
	await d.say(BRADLEY, "Whatever you're about to do.")
	await d.say(PILSNER, "I'm getting a drink.")
	await d.say(CHADWICK, "Your drink's right there.")
	d.close()
	stage.state.flags[BANTER_PLAYED] = true


## Scene 2, the approach (walking Pilsner up to the group). The round goes on Pilsner's tab.
static func the_approach(stage) -> void:
	var d: DialogueBox = stage.dialogue
	await d.say(PILSNER, "How's your night going?")
	await d.say(WHITNEY, "Okay.")
	await d.beat()
	await d.say(PILSNER, "Can I buy you another one of those test-tube things?")
	await d.beat()
	await d.say(WHITNEY, "Seriously?!")
	await d.beat()
	await d.say(WHITNEY, "HEY, GIRLS! THIS GUY WHO LOOKS LIKE MY GRANDPA IS BUYING US ANOTHER ROUND FOR CARA'S BIRTHDAY!")
	await d.say(GIRLS, "WOOOOOOOOOO!")
	await d.say(BRYNLEIGH, "THANK YOU, GRANDPA GUY!")
	await d.beat()
	stage.state.flags[ROUND_BOUGHT] = true
	await d.beat(1.0)
	await d.say(BRADLEY, "How'd it go, Grandpa?")
	await d.say(PILSNER, "Shut up.")
	await d.say(CHADWICK, "You still got it, dude.")
	await d.say(PILSNER, "I said shut up.")
	await d.say(GIRLS, "WOOOOOOOOOO!")
	d.close()


## Scene 1, The Tip. `stage` is the hall: dialogue, ring_on().
static func the_tip(stage) -> void:
	var d: DialogueBox = stage.dialogue
	await d.beat()
	await d.say(TOMAS, "What, no tip?")
	await d.beat()
	await d.say(PILSNER, "We got you, bro.")
	await d.beat(1.2)
	await d.say(TOMAS, "Wow.")
	await d.say(BRADLEY, "Don't spend it all in one place.")
	await d.say(CHADWICK, "That's five tickets, dude.")
	await d.beat()
	stage.ring_on()
	await d.beat()
	await d.say(TOMAS, "I'll alert my financial adviser.")
	d.close()
	stage.state.flags[RING_TIPPED] = true


## Paying early at the counter (round v30 default).
static func pay_at_counter(stage) -> void:
	var d: DialogueBox = stage.dialogue
	if not pay(stage.state):
		await d.say("", "NOT ENOUGH SOVS")
		d.close()
		return
	await d.say(TOMAS, "Pleasure doing business with you, Grandpa.")
	d.close()


## Scene 3, The Unsettled Tab, at the exit. `stage` is the hall: dialogue, state, receivable_arrive(),
## tomas_behind_bar(), fight() -> outcome, leave(). Returns how it ended: "paid", "fled" or "lost".
static func unsettled_tab(stage) -> String:
	var d: DialogueBox = stage.dialogue
	await d.say(TOMAS, "Hey, Grandpa.")
	await d.beat()
	await d.say(TOMAS, "You forgot to settle your tab.")
	await d.beat()
	await d.say(TOMAS, "Maybe it's just the dementia.")
	await d.beat()
	await d.say(CHADWICK, "Oh, shit.")
	await d.beat()
	await d.say(PILSNER, "I bought ONE girl ONE drink.")
	await d.say(TOMAS, "Sure.")
	await d.beat()
	await d.say(TOMAS, "And then your granddaughter announced otherwise.")
	await d.say(PILSNER, "She's not my granddaughter.")
	await d.say(TOMAS, "That's good.")
	await d.beat()
	await d.say(TOMAS, "I was concerned about the flirting.")
	await d.beat()
	await d.say(PILSNER, "Can you shut the fuck up?")
	await d.say(BRADLEY, "I'm not saying anything.")
	await d.say(PILSNER, "You're laughing.")
	await d.say(BRADLEY, "That's different.")
	await d.beat()
	if await _choose_pay(stage, ["PAY THE TAB", "REFUSE AGAIN"]):
		await d.say(TOMAS, "Pleasure doing business with you, Grandpa.")
		await d.beat()
		await d.say(TOMAS, "Oh—and thanks again for the tip.")
		await d.beat()
		await d.say(TOMAS, "Really turned things around for me.")
		await d.beat()
		await d.say(CHADWICK, "Dude, I think he likes it.")
		await d.say(PILSNER, "Fuck both of you.")
		d.close()
		return "paid"
	await d.say(PILSNER, "I'm not paying for drinks I didn't order.")
	await d.beat()
	await d.say(TOMAS, "Okay.")
	await d.say(PILSNER, "Okay?")
	await d.say(TOMAS, "Yeah.")
	await d.beat()
	await d.say(TOMAS, "You can absolutely leave without paying.")
	await d.beat()
	await d.say(PILSNER, "Thank you.")
	await d.beat()
	stage.receivable_arrive()
	await d.beat(1.0)
	await d.say(TOMAS, "You just can't leave through there.")
	await d.beat()
	await d.say(BRADLEY, "Great pickup, dude.")
	await d.beat()
	await d.say(TOMAS, "So.")
	await d.beat()
	await d.say(TOMAS, "Cash, card, or traumatic brain injury?")
	if await _choose_pay(stage, ["PAY", "REFUSE"]):
		await d.say(TOMAS, "Smart.")
		await d.beat()
		await d.say(TOMAS, "Runs in the family.")
		d.close()
		return "paid"
	await d.beat()
	stage.tomas_behind_bar()
	await d.say(TOMAS, "Gentlemen, our guests are experiencing a billing dispute.")
	d.close()
	var outcome: String = await stage.fight()
	if outcome == "lost":
		lost(stage.state)  # a short wallet loses what it has; no line (round v30: the name is the title only)
		return "lost"
	fled(stage.state)
	await d.beat()
	await d.say(TOMAS, "HEY!")
	await d.beat()
	await d.say(TOMAS, "Service charge.")
	d.close()
	return "fled"


## A pay/refuse choice: true when they paid. Choosing to pay with a short wallet says so and asks again.
static func _choose_pay(stage, choices: Array) -> bool:
	var d: DialogueBox = stage.dialogue
	while true:
		if await d.choose(choices) == 1:
			return false
		if pay(stage.state):
			return true
		await d.say("", "NOT ENOUGH SOVS")
	return false
