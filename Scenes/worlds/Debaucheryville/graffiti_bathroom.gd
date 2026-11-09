extends Node2D

@export var graffiti_id = "publandia_stall_1"
@export var graffiti_text = "Dear Pint #6, I blame you..."

var graffiti_revealed := false

func _ready():
    if GameState.graffiti_found.has(graffiti_id):
        graffiti_revealed = true
        $GraffitiLabel.text = graffiti_text
    else:
        $InteractArea.connect("area_entered", Callable(self, "_on_interact"))

func _on_interact(area):
    if graffiti_revealed:
        return
    graffiti_revealed = true
    $GraffitiLabel.text = graffiti_text
    $GraffitiFX.play("glitch_reveal")
    $GraffitiWhispers.play()
    GameState.graffiti_found.append(graffiti_id)
    emit_signal("graffiti_discovered", graffiti_id)