class_name HoldGate
extends RefCounted
## A button that only counts once it has been held for `seconds`. A tap never fires.
## Driven by advance(delta), so tests need no real time.

var seconds := 0.4
var held := false
var fired := false
var _t := 0.0


func _init(seconds_: float = 0.4) -> void:
	seconds = seconds_


func press() -> void:
	if held:
		return
	held = true
	fired = false
	_t = 0.0


func release() -> void:
	held = false
	fired = false
	_t = 0.0


## True on the one call where the hold completes.
func advance(delta: float) -> bool:
	if not held or fired:
		return false
	_t += delta
	# A hair of slack so 0.3 + 0.1 counts as 0.4.
	if _t + 0.0001 >= seconds:
		fired = true
		return true
	return false
