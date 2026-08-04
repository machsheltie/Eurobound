extends Area2D
class_name RateBoard

signal rate_checked(current_rate: float)
signal rate_locked(final_rate: float)

@export var base_rate: float = 1.00   # baseline conversion
@export var volatility: float = 0.15  # 0.15 = ±15% swing window
@export var lock_on_interact: bool = true
@export var dialogue_controller: NodePath  # optional, to post flavor lines

var _current_rate: float = 1.0
var _locked: bool = false
var _rng := RandomNumberGenerator.new()

func _ready() -> void:
	_rng.randomize()
	_update_rate_tick()

func _process(delta: float) -> void:
	if _locked: 
		return
	# lightweight "ticker": small random walk
	if _rng.randi() % 30 == 0:
		_update_rate_tick()

func _update_rate_tick() -> void:
	var swing := (2.0 * _rng.randf() - 1.0) * volatility
	_current_rate = max(0.01, base_rate * (1.0 + swing))
	emit_signal("rate_checked", _current_rate)

func interact() -> void:
	# Call this from your player Interact input when overlapping
	if _locked and lock_on_interact:
		_emit_dialogue("Rates are locked. No take-backs.")
		return
	if lock_on_interact:
		_locked = true
	emit_signal("rate_locked", _current_rate)
	_emit_dialogue("You lock the rate at %.2f." % _current_rate)

func get_rate() -> float:
	return _current_rate

func is_locked() -> bool:
	return _locked

func _emit_dialogue(text: String) -> void:
	if dialogue_controller.is_empty():
		return
	var dc := get_node_or_null(dialogue_controller)
	if dc and dc.has_method("push_system_line"):
		dc.call("push_system_line", "[RateBoard] " + text)
