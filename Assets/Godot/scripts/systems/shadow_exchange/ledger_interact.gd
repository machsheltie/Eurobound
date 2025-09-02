extends Area2D
class_name LedgerInteract

signal ledger_opened()
signal ledger_flag_set(flag_name: String)

@export var dialogue_controller: NodePath
@export var flag_name: String = "shadow_ledger_seen"

func interact() -> void:
	emit_signal("ledger_opened")
	_set_flag()
	_emit_dialogue("You slide the duct-taped ledger closer. A sticky note reads: \"EXPORT: /ledger/hash_kebab_monkey\"")

func _set_flag() -> void:
	emit_signal("ledger_flag_set", flag_name)
	if dialogue_controller.is_empty():
		return
	var dc := get_node_or_null(dialogue_controller)
	if dc and dc.has_method("set_flag_true"):
		dc.call("set_flag_true", flag_name)

func _emit_dialogue(text: String) -> void:
	if dialogue_controller.is_empty():
		return
	var dc := get_node_or_null(dialogue_controller)
	if dc and dc.has_method("push_system_line"):
		dc.call("push_system_line", "[Ledger] " + text)
