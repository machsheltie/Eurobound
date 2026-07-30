extends Area2D

@onready var menu_ui = preload("res://Assets/Godot/Scenes/templates/kebab_menu_popup.tscn")
@onready var player = get_node("/root/Player")

func _on_interact():
    if player:
        var ui_instance = menu_ui.instantiate()
        get_tree().current_scene.add_child(ui_instance)
        ui_instance.init_kebab_menu()

func _on_body_entered(body):
    if body.name == "Player":
        $InteractPrompt.show()

func _on_body_exited(body):
    if body.name == "Player":
        $InteractPrompt.hide()
