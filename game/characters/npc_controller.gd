extends Area2D
## Static overworld NPC. Player's InteractZone (mask 2) finds us on layer 2;
## interact() opens our dialogue tree.

const DIALOGUE_BOX_SCENE := preload("res://ui/dialogue/dialogue_box.tscn")

@export var npc_id: String = ""

func _ready() -> void:
	collision_layer = 2
	collision_mask = 0

	var visual := ColorRect.new()
	visual.color = Color(0.3, 0.6, 0.9)  # bouncer-blue placeholder
	visual.size = Vector2(24, 32)
	visual.position = Vector2(-12, -28)
	add_child(visual)

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = Vector2(32, 40)
	shape.shape = rect
	add_child(shape)

	var body := StaticBody2D.new()
	body.collision_layer = 1
	var body_shape := CollisionShape2D.new()
	var body_rect := RectangleShape2D.new()
	body_rect.size = Vector2(24, 16)
	body_shape.shape = body_rect
	body_shape.position = Vector2(0, -4)
	body.add_child(body_shape)
	add_child(body)

func interact() -> void:
	var location := get_parent()
	var box := DIALOGUE_BOX_SCENE.instantiate()
	location.add_child(box)
	box.open(npc_id, location.player)
