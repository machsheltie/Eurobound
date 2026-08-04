extends Node2D
class_name ShadowExchangeRoot
## Auto-wires Shadow Exchange scene nodes to EconomyController + DialogueController (if present).

@onready var rate_board := $RateBoard
@onready var barter_counter := $BarterCounter
@onready var ledger := $LedgerInteract
@onready var couchsurf := $CouchsurfTrigger

@export var dialogue_controller_path: NodePath

var dialogue_controller: Node = null
var economy: Node = null

func _ready() -> void:
	dialogue_controller = _resolve_dialogue_controller()
	economy = get_node_or_null("/root/EconomyController")
	
	# Assign DialogueController path to child interaction nodes (if they expose it)
	_assign_dialogue_controller(rate_board)
	_assign_dialogue_controller(barter_counter)
	_assign_dialogue_controller(ledger)
	_assign_dialogue_controller(couchsurf)
	
	# Connect node signals → local handlers
	if rate_board:
		if not rate_board.rate_checked.is_connected(_on_rate_checked):
			rate_board.rate_checked.connect(_on_rate_checked)
		if not rate_board.rate_locked.is_connected(_on_rate_locked):
			rate_board.rate_locked.connect(_on_rate_locked)
	if barter_counter:
		if not barter_counter.barter_started.is_connected(_on_barter_started):
			barter_counter.barter_started.connect(_on_barter_started)
		if not barter_counter.barter_offer_made.is_connected(_on_barter_offer_made):
			barter_counter.barter_offer_made.connect(_on_barter_offer_made)
		if not barter_counter.barter_result.is_connected(_on_barter_result):
			barter_counter.barter_result.connect(_on_barter_result)
	if ledger:
		if not ledger.ledger_opened.is_connected(_on_ledger_opened):
			ledger.ledger_opened.connect(_on_ledger_opened)
		if not ledger.ledger_flag_set.is_connected(_on_ledger_flag_set):
			ledger.ledger_flag_set.connect(_on_ledger_flag_set)
	if couchsurf:
		if not couchsurf.couchsurf_started.is_connected(_on_couchsurf_started):
			couchsurf.couchsurf_started.connect(_on_couchsurf_started)
		if not couchsurf.couchsurf_resolved.is_connected(_on_couchsurf_resolved):
			couchsurf.couchsurf_resolved.connect(_on_couchsurf_resolved)

# --- Helpers ---

func _resolve_dialogue_controller() -> Node:
	if dialogue_controller_path != NodePath():
		var dc := get_node_or_null(dialogue_controller_path)
		if dc:
			return dc
	# Fallback to autoload singleton path if you registered it as /root/DialogueController
	var dc2 := get_node_or_null("/root/DialogueController")
	return dc2

func _assign_dialogue_controller(n: Node) -> void:
	if n == null or dialogue_controller == null:
		return
	var has_prop := _object_has_property(n, "dialogue_controller")
	if has_prop:
		var np := get_path_to(dialogue_controller)
		# Set exported NodePath on child scripts that support it
		n.set("dialogue_controller", np)

func _object_has_property(obj: Object, prop: String) -> bool:
	for p in obj.get_property_list():
		if String(p.name) == prop:
			return true
	return false

func _dc_push(line: String) -> void:
	if dialogue_controller and dialogue_controller.has_method("push_system_line"):
		dialogue_controller.call("push_system_line", line)

# --- Signal handlers ---

func _on_rate_checked(current_rate: float) -> void:
	_dc_push("[RateBoard] Current rate: %.2f" % current_rate)

func _on_rate_locked(final_rate: float) -> void:
	_dc_push("[RateBoard] Rate locked at %.2f" % final_rate)
	var econ := economy if economy else get_node_or_null("/root/EconomyController")
	if econ and econ.has_method("apply_rate"):
		econ.call("apply_rate", final_rate, "shadow_exchange")

func _on_barter_started() -> void:
	_dc_push("[Barter] The clerk slides a scratched glass tray toward you.")

func _on_barter_offer_made(offer: Dictionary) -> void:
	var items := offer.get("items_offered", [])
	var exp := offer.get("expected", "")
	var chance := float(offer.get("success_chance", 0.0)) * 100.0
	_dc_push("[Barter] Offering %s for %s (%.0f%% chance)." % [", ".join(items), exp, chance])

func _on_barter_result(success: bool, reward: String) -> void:
	var econ := economy if economy else get_node_or_null("/root/EconomyController")
	if success:
		_dc_push("[Barter] Deal stamped. You receive: %s" % reward)
		if econ and econ.has_method("handle_barter_result"):
			econ.call("handle_barter_result", true, reward)
	else:
		_dc_push("[Barter] Verification failed. The fee doubles if you argue.")
		if econ and econ.has_method("handle_barter_result"):
			econ.call("handle_barter_result", false, "")

func _on_ledger_opened() -> void:
	_dc_push("[Ledger] The duct-taped ledger creaks open.")

func _on_ledger_flag_set(flag_name: String) -> void:
	_dc_push("[Ledger] Flag set: %s" % flag_name)
	if dialogue_controller and dialogue_controller.has_method("set_flag_true"):
		dialogue_controller.call("set_flag_true", flag_name)

func _on_couchsurf_started(npc_id: String) -> void:
	_dc_push("[Couchsurf] Starting micro-scene for: %s" % npc_id)

func _on_couchsurf_resolved(npc_id: String) -> void:
	_dc_push("[Couchsurf] Scene resolved for: %s" % npc_id)
