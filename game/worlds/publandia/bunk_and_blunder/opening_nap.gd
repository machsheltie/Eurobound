class_name OpeningNap
extends RefCounted
## Story opening step 1, Scene 8: the nap at The Bunk & Blunder (design/narrative/opening_step1.md,
## approved Desk Eurobound-3ho-q11). Plays the scene's lines through a DialogueBox with the
## NAP / DON'T NAP prompt. Both choices nap (author: "nap prompt in"); the only difference is how
## long PILSNER pretends he's not going to. Every line is the scene's, word for word.
## Stage directions are beats: the game has no narrator.

const PILSNER := "PILSNER"
const BRADLEY := "BRADLEY"
const CHADWICK := "CHADWICK"

const CHOICES := ["NAP", "DON'T NAP"]
const CHOICE_NAP := 0
const CHOICE_DONT_NAP := 1

const LINE_BRADLEY_NAP := "Just a nap. Twenty minutes. Tactical. It's what athletes do."
const LINE_NOT_NAPPING := "We are NOT napping. We are in EUROMEMEIA. There are women out there who have never met an American with a paddle."
const LINE_TWENTY_MINUTES := "...Twenty minutes. Then we go out. Twenty minutes."

## What DON'T NAP plays before the nap: PILSNER pretending longer. The scene has no lines for it yet;
## they wait on the author (Eurobound Desk Eurobound-40tc-q1). Each entry is [speaker, line].
## Empty = DON'T NAP goes straight to the nap, like NAP.
const LINES_DONT_NAP_PRETEND: Array = []

const LINES_WAKE := [
	[PILSNER, "BOYS. It's NIGHT. We slept through the afternoon. We are THREE HOURS BEHIND SCHEDULE."],
	[CHADWICK, "We good. We back. I got the whole nap. Three hours of content."],
	[BRADLEY, "Tactical. I feel incredible. I feel twenty-five."],
]
const LINE_GOING_OUT := "Gentlemen. Publandia, Debaucheryville, Sinfonia, Shamsterdam — it all starts tonight. We are going OUT."
const LINE_CALL_MOMMY := "...I should call Mommy."


## Plays Scene 8 from the bunk room to the door. `nap_cut` (optional) is awaited where the screen
## dims and comes back up in full dark; the room scene passes its fade. Returns true: they napped.
static func play(d: DialogueBox, nap_cut: Callable = Callable()) -> bool:
	await d.beat()  # CHADWICK snoring on the lower bunk, BRADLEY's calf raises
	await d.say(BRADLEY, LINE_BRADLEY_NAP)
	await d.beat()  # BRADLEY asleep in under four seconds
	await d.say(PILSNER, LINE_NOT_NAPPING)
	await d.beat()  # the pager beeps; nobody wakes; bunk, window, bunk
	await d.say(PILSNER, LINE_TWENTY_MINUTES)
	var pick: int = await d.choose(CHOICES)
	if pick == CHOICE_DONT_NAP:
		for entry: Array in LINES_DONT_NAP_PRETEND:
			await d.say(String(entry[0]), String(entry[1]))
	d.close()
	if nap_cut.is_valid():
		await nap_cut.call()
	else:
		await d.beat()  # the screen dims; the neon sign; the hen party; full dark
	for entry: Array in LINES_WAKE:
		await d.say(String(entry[0]), String(entry[1]))
	await d.beat()  # PILSNER at the mirror, the divorce papers back in the outside pocket
	await d.say(PILSNER, LINE_GOING_OUT)
	await d.beat()  # he opens the door
	await d.say(PILSNER, LINE_CALL_MOMMY)
	d.close()
	return true
