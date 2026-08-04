extends Node
## All scene transitions go through here. Owns the overworld↔battle handoff:
## remembers where the player was so locations can restore position.

var pending_enemy_id: String = ""
var restore_pending: bool = false

var _return_scene_path: String = ""

func goto_scene(path: String) -> void:
	GameState.current_scene_path = path
	get_tree().call_deferred("change_scene_to_file", path)

func goto_battle(enemy_id: String) -> void:
	pending_enemy_id = enemy_id
	_return_scene_path = GameState.current_scene_path
	get_tree().call_deferred("change_scene_to_file", "res://battle/battle_scene.tscn")

func end_battle(restore_position: bool = true) -> void:
	pending_enemy_id = ""
	restore_pending = restore_position
	get_tree().call_deferred("change_scene_to_file", _return_scene_path)
