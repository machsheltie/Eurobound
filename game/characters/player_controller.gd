extends CharacterBody2D
## Overworld player: 8-direction movement, interaction with nearby areas.
## Children are built in _ready() so the .tscn stays a trivial text file.

const SPEED := 140.0

var can_move: bool = true

var _interact_zone: Area2D

func _ready() -> void:
	collision_layer = 1
	collision_mask = 1

	var visual := ColorRect.new()
	visual.color = Color(0.9, 0.75, 0.2)  # beer-gold placeholder for Lord Pilsner
	visual.size = Vector2(24, 32)
	visual.position = Vector2(-12, -28)
	add_child(visual)

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = Vector2(22, 14)
	shape.shape = rect
	shape.position = Vector2(0, -4)
	add_child(shape)

	var camera := Camera2D.new()
	camera.zoom = Vector2(2, 2)
	add_child(camera)

	_interact_zone = Area2D.new()
	_interact_zone.collision_layer = 0
	_interact_zone.collision_mask = 2
	var zone_shape := CollisionShape2D.new()
	var zone_rect := RectangleShape2D.new()
	zone_rect.size = Vector2(48, 48)
	zone_shape.shape = zone_rect
	_interact_zone.add_child(zone_shape)
	add_child(_interact_zone)

func _physics_process(_delta: float) -> void:
	if not can_move:
		velocity = Vector2.ZERO
		return
	var direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = direction * SPEED
	move_and_slide()
	GameState.player_position = global_position

func _unhandled_input(event: InputEvent) -> void:
	if not can_move:
		return
	if event.is_action_pressed("interact"):
		for area in _interact_zone.get_overlapping_areas():
			if area.has_method("interact"):
				area.interact()
				get_viewport().set_input_as_handled()
				return
