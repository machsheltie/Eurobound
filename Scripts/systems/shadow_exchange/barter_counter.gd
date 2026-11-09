extends Area2D
class_name BarterCounter

signal barter_started()
signal barter_offer_made(offer: Dictionary)   # {items_offered: [String], expected: String, success_chance: float}
signal barter_result(success: bool, reward: String)

@export var required_tag: String = "shadow_exchange"  # for your loaders/routing
@export var dialogue_controller: NodePath
@export var accepted_items: Array[String] = ["concert_wristband", "metro_day_pass", "gag_item_quartz_tip"]
@export var reward_table: Dictionary = {
	"concert_wristband": {"reward":"forged_vip_wristband", "success":0.9},
	"metro_day_pass": {"reward":"queue_skip_chip", "success":0.75},
	"gag_item_quartz_tip": {"reward":"pocket_uv_wand", "success":0.6}
}

func interact_with_inventory(items_in_hand: Array[String]) -> void:
	emit_signal("barter_started")
	var best_item := ""
	var best := -1.0
	for i in items_in_hand:
		if accepted_items.has(i) and reward_table.has(i):
			var sc := float(reward_table[i]["success"])
			if sc > best:
				best = sc
				best_item = i
	if best_item == "":
		_emit_dialogue("The clerk slides the tray back. \"This is… sentimental at best.\"")
		emit_signal("barter_result", false, "")
		return

	var offer := {
		"items_offered": [best_item],
		"expected": reward_table[best_item]["reward"],
		"success_chance": best
	}
	emit_signal("barter_offer_made", offer)

	var rng := RandomNumberGenerator.new()
	rng.randomize()
	var success := rng.randf() <= best
	if success:
		var reward := String(reward_table[best_item]["reward"])
		_emit_dialogue("Stamp. Slide. \"Pleasure doing ambiguous business.\" (Got %s)" % reward)
		emit_signal("barter_result", true, reward)
	else:
		_emit_dialogue("The clerk sighs. \"Counterfeit. Verification fee doubled.\"")
		emit_signal("barter_result", false, "")

func _emit_dialogue(text: String) -> void:
	if dialogue_controller.is_empty():
		return
	var dc := get_node_or_null(dialogue_controller)
	if dc and dc.has_method("push_system_line"):
		dc.call("push_system_line", "[Barter] " + text)
