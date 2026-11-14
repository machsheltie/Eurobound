class_name VanekTalk
extends RefCounted
## Dr. Vaněk's conversation at the bar (design/worlds/debaucheryville/the_absinthium_taproom.md).
## `stage` is the Taproom room: `dialogue` (DialogueBox) and `state` (GameState). Rules live in
## VanekTaproom; this only sequences the lines. Menu labels are plain UI, not spoken text.

const MENU_LAGER := "Absinthe Lager"
const MENU_STAMP := "Stamp"
const MENU_SURVEY := "Survey"
const MENU_LEAVE := "Leave"


static func talk(stage) -> void:
	var d: DialogueBox = stage.dialogue
	var s = stage.state
	if VanekTaproom.backfill_opener(s) and VanekTaproom.TODO_LINE_OPENER_HANDOVER != "":
		await d.say(VanekTaproom.SPEAKER, VanekTaproom.TODO_LINE_OPENER_HANDOVER)
	match VanekTaproom.gate(s):
		VanekTaproom.GATE_NO_KEYCHAIN:
			await d.say(VanekTaproom.SPEAKER, VanekTaproom.LINE_NO_KEYCHAIN)
			d.close()
			return
		VanekTaproom.GATE_NO_OPENER:
			await d.say(VanekTaproom.SPEAKER, VanekTaproom.LINE_KEYCHAIN_NO_OPENER)
			d.close()
			return
	if not bool(s.flags.get(VanekTaproom.FLAG_GREETED, false)):
		s.flags[VanekTaproom.FLAG_GREETED] = true
		await d.say(VanekTaproom.SPEAKER, VanekTaproom.LINE_BOTH_OPENERS)
	else:
		var callback := VanekTaproom.next_callback(s)
		if callback != "":
			await d.say(VanekTaproom.SPEAKER, callback)
	while true:
		var labels := [
			"%s (%d SOVS)" % [MENU_LAGER, VanekTaproom.lager_price(s)],
			MENU_STAMP, MENU_SURVEY, MENU_LEAVE]
		var pick: int = await d.choose(labels)
		if pick == 0:
			await _sell(d, s)
		elif pick == 1:
			if VanekTaproom.try_stamp(s):
				await d.say(VanekTaproom.SPEAKER, VanekTaproom.LINE_STAMP_SPEECH)
		elif pick == 2:
			await _survey(d, s)
		else:
			break
	d.close()


## Opener, six questions (pick a bro answer, same reply from Vaněk either way), closer, reward.
## Nothing is said if the survey was already done. Answers change no stat.
static func _survey(d: DialogueBox, s) -> void:
	if not VanekTaproom.can_take_survey(s):
		return
	s.flags[VanekTaproom.FLAG_SURVEY_CONSENTED] = true
	await d.say(VanekTaproom.SPEAKER, VanekTaproom.SURVEY_OPENER)
	for q: Dictionary in VanekTaproom.SURVEY_QUESTIONS:
		await d.say(VanekTaproom.SPEAKER, String(q["prompt"]))
		await d.choose(q["answers"])
		await d.say(VanekTaproom.SPEAKER, String(q["reply"]))
	await d.say(VanekTaproom.SPEAKER, VanekTaproom.SURVEY_CLOSER)
	VanekTaproom.complete_survey(s)  # wristband + "The Research Subject" selfie flag


static func _sell(d: DialogueBox, s) -> void:
	var result := VanekTaproom.buy_lager(s)
	if result == VanekTaproom.SALE_BOUGHT:
		for line: String in VanekTaproom.LINES_SERVING:
			await d.say(VanekTaproom.SPEAKER, line)
	elif result == VanekTaproom.SALE_CANNOT_AFFORD:
		await d.say(VanekTaproom.SPEAKER, VanekTaproom.LINE_CANNOT_AFFORD)
