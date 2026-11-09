extends Area2D

@export var tokens_required := 3
var inserted_tokens := 0
var door_unlocked := false

@onready var player = get_node("/root/Player")
@onready var ddr_machine = $"../DDRMachine"
@onready var door_node = $"../ClosetDoor"
@onready var squeak_audio = $"../JoystickSFX"

func _ready():
    $UnlockPrompt.hide()

func insert_token():
    if door_unlocked:
        return
    inserted_tokens += 1
    if inserted_tokens >= tokens_required:
        _unlock_door()

func _unlock_door():
    door_unlocked = true
    if door_node:
        door_node.queue_free()  # Simulates door opening
    if squeak_audio:
        squeak_audio.play()
    $UnlockPrompt.text = "Closet unlocked!"
    $UnlockPrompt.show()

func _on_body_entered(body):
    if body.name == "Player" and not door_unlocked:
        $UnlockPrompt.text = "Insert tokens to unlock (3 total)"
        $UnlockPrompt.show()

func _on_body_exited(body):
    if body.name == "Player":
        $UnlockPrompt.hide()
