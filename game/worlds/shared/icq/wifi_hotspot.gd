class_name WifiHotspot
extends Node3D
## A FREE Wi-Fi sign: reusable across cities (outside cafes, bars, suspicious storefronts).
## Implements design/worlds/shared/interactables/wifihotspots.md:1-3. `interact()` opens the ICQ
## window on Pilsner's phone and lets a recurring personality hijack the connection. Not placed in
## any scene yet: placement waits on each scene's owner (bead Eurobound-00i).
##
## This node is the "stage" Tony420Hijack.play() wants: `dialogue`, `state` and `cue(id)`.

signal interacted
signal hijack_finished(hijacker: String, first: bool)

const TONY420 := "tony420"

## Audio hook for the ICQ "Uh-oh!" chime (bead Eurobound-3it, sourcing unruled). No stream, no sound.
@export var cue_streams: Dictionary = {}  ## cue id (String) -> AudioStream

var dialogue: DialogueBox
## GameState by default; tests inject a fake with a `flags` dictionary.
var state
var icq: IcqWindow
var busy := false

var _player: AudioStreamPlayer


func _ready() -> void:
	add_to_group("interactable")
	if state == null:
		state = GameState
	if dialogue == null:
		dialogue = DialogueBox.new()
		add_child(dialogue)
	icq = IcqWindow.new()
	add_child(icq)
	_player = AudioStreamPlayer.new()
	add_child(_player)


## Which personality hijacks this connection.
## HOOK (unruled): Tony420 / Hamstradamus / CryptoBro69 rotation awaits the author's answer to
## Production Desk Eurobound-ign-q1 item 3. Until then only Tony420 (the ruled first hijack) runs.
func hijacker() -> String:
	return TONY420


func interact() -> void:
	if busy:
		return
	busy = true
	interacted.emit()
	icq.open()
	var who := hijacker()
	var first := false
	match who:
		TONY420:
			first = await Tony420Hijack.play(self)
		_:
			push_warning("WifiHotspot: no hijack script for '%s'" % who)
	icq.close()
	busy = false
	hijack_finished.emit(who, first)


func cue(id: String) -> void:
	var stream: AudioStream = cue_streams.get(id)
	if stream == null or _player == null:
		return
	_player.stream = stream
	_player.play()
