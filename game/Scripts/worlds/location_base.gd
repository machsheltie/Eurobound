class_name LocationBase
extends Node2D
## Template every location extends: placeholder floor, boundary walls,
## player spawn/restore, pause menu. Subclasses set spawn_point and
## spawn their NPCs/enemies, then call super._ready().

const PLAYER_SCENE := preload("res://characters/player.tscn")
const NPC_SCENE := preload("res://characters/npc_base.tscn")
const ENEMY_SCENE := preload("res://characters/enemy.tscn")
const PAUSE_MENU_SCENE := preload("res://ui/menus/pause_menu.tscn")

@export var location_id: String = ""
@export var bounds: Rect2 = Rect2(0, 0, 960, 640)

var spawn_point: Vector2 = Vector2(480, 320)
var player: CharacterBody2D

func _ready() -> void:
	_build_floor()
	_build_walls()
	player = PLAYER_SCENE.instantiate()
	if SceneRouter.restore_pending:
		player.position = GameState.player_position
		SceneRouter.restore_pending = false
	else:
		player.position = spawn_point
		GameState.player_position = spawn_point
	add_child(player)
	add_child(PAUSE_MENU_SCENE.instantiate())

func spawn_npc(npc_id: String, pos: Vector2) -> void:
	var npc := NPC_SCENE.instantiate()
	npc.npc_id = npc_id
	npc.position = pos
	add_child(npc)

func spawn_enemy(enemy_id: String, pos: Vector2) -> void:
	var enemy := ENEMY_SCENE.instantiate()
	enemy.enemy_id = enemy_id
	enemy.position = pos
	add_child(enemy)

func _build_floor() -> void:
	var floor_rect := ColorRect.new()
	floor_rect.color = Color(0.25, 0.22, 0.28)  # grimy cobblestone placeholder
	floor_rect.position = bounds.position
	floor_rect.size = bounds.size
	floor_rect.z_index = -10
	add_child(floor_rect)

func _build_walls() -> void:
	var thickness := 16.0
	var edges := [
		Rect2(bounds.position - Vector2(0, thickness), Vector2(bounds.size.x, thickness)),
		Rect2(Vector2(bounds.position.x, bounds.end.y), Vector2(bounds.size.x, thickness)),
		Rect2(bounds.position - Vector2(thickness, 0), Vector2(thickness, bounds.size.y)),
		Rect2(Vector2(bounds.end.x, bounds.position.y), Vector2(thickness, bounds.size.y)),
	]
	for edge in edges:
		var wall := StaticBody2D.new()
		wall.collision_layer = 1
		var shape := CollisionShape2D.new()
		var rect := RectangleShape2D.new()
		rect.size = edge.size
		shape.shape = rect
		wall.position = edge.position + edge.size / 2.0
		wall.add_child(shape)
		add_child(wall)
