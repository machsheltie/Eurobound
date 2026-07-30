extends Area2D

@export var open_time : int = 3 # 3 AM game time required
@onready var player = get_node("/root/Player")
@onready var game_time = get_node("/root/Global/TimeManager")

func _ready():
    $CrawlPrompt.hide()

func _on_body_entered(body):
    if body.name == "Player" and _is_accessible_time():
        $CrawlPrompt.show()

func _on_body_exited(body):
    if body.name == "Player":
        $CrawlPrompt.hide()

func _is_accessible_time() -> bool:
    return game_time.get_current_hour() == open_time

func _on_interact():
    if _is_accessible_time():
        get_tree().change_scene_to_file("res://Assets/Godot/Scenes/overworld/Debaucheryville/grease_trap_restroom.tscn")
    else:
        print("It's too early to relive bad decisions. Come back at 3 AM.")
