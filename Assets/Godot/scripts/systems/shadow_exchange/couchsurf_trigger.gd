extends Area2D
class_name CouchsurfTrigger

signal couchsurf_started(npc_id: String)
signal couchsurf_resolved(npc_id: String)

@export var npc_id: String = "cryptobro_ex"
@export var dialogue_controller: NodePath

func interact() -> void:
	emit_signal("couchsurf_started", npc_id)
	# If you wired DialogueController, ask it to run this micro-scene immediately:
	if not dialogue_controller.is_empty():
		var dc := get_node_or_null(dialogue_controller)
		if dc and dc.has_method("apply_outcome"):
			dc.call("apply_outcome", npc_id) # your DC can branch or show UI
	emit_signal("couchsurf_resolved", npc_id)
