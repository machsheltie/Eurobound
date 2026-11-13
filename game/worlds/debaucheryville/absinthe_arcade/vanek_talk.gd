class_name VanekTalk
extends RefCounted
## Dr. Vaněk's conversation at the bar (design/worlds/debaucheryville/the_absinthium_taproom.md).
## `stage` is the Taproom room: `dialogue` (DialogueBox) and `state` (GameState). Rules live in
## VanekTaproom; this only sequences the lines. Menu labels are plain UI, not spoken text.

const MENU_LAGER := "Absinthe Lager"
const MENU_STAMP := "Stamp"
const MENU_SURVEY := "Survey"
const MENU_LEAVE := "Leave"
const NOTICE_NOT_ENOUGH := "NOT ENOUGH SOVS"  ## same notice as the hall's counter


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
			if VanekTaproom.TODO_LINE_KEYCHAIN_NO_OPENER != "":
				await d.say(VanekTaproom.SPEAKER, VanekTaproom.TODO_LINE_KEYCHAIN_NO_OPENER)
			d.close()
			return
	if not bool(s.flags.get(VanekTaproom.FLAG_GREETED, false)):
		s.flags[VanekTaproom.FLAG_GREETED] = true
		await d.say(VanekTaproom.SPEAKER, VanekTaproom.LINE_BOTH_OPENERS)
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
			# Stub: consent only, no questions or rewards are defined.
			s.flags[VanekTaproom.FLAG_SURVEY_CONSENTED] = true
		else:
			break
	d.close()


static func _sell(d: DialogueBox, s) -> void:
	var result := VanekTaproom.buy_lager(s)
	if result == VanekTaproom.SALE_BOUGHT:
		for line: String in VanekTaproom.LINES_SERVING:
			await d.say(VanekTaproom.SPEAKER, line)
	elif result == VanekTaproom.SALE_CANNOT_AFFORD:
		if VanekTaproom.TODO_LINE_CANNOT_AFFORD != "":
			await d.say(VanekTaproom.SPEAKER, VanekTaproom.TODO_LINE_CANNOT_AFFORD)
		else:
			await d.say("", NOTICE_NOT_ENOUGH)
