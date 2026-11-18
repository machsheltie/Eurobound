class_name RestPointStandIn
extends Node3D
## Test stand-in for the hostel (G4: the real scene does not exist; no art here). One node that
## plays reception and the bed for a RestPoint so the booking, the save offer and the rest can be
## driven the way a scene would. interact_reception() books, interact_bed() sleeps. Signals carry
## the doc line (or an empty placeholder) for a UI to show; nothing is shown here.

signal booked(line: String)
signal refused(line: String)
signal slept

@export var rest_id := "hmc_dorm_12_bed"
var state
var saver
var rest_point: RestPoint


func _ready() -> void:
	add_to_group("interactable")
	if state == null:
		state = GameState
		saver = get_node_or_null("/root/SaveSystem")
	if rest_point == null:
		rest_point = RestPoint.from_id(rest_id)


func interact_reception() -> bool:
	if rest_point.book(state):
		booked.emit(rest_point.line("booked"))
		return true
	refused.emit(rest_point.line("cannot_afford"))
	return false


func interact_bed() -> bool:
	var ok: bool = await rest_point.sleep(state, saver)
	if ok:
		slept.emit()
	return ok
