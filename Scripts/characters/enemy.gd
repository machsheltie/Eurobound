extends Area2D
## Visible overworld enemy: wanders near its spawn, touching the player
## starts a battle via SceneRouter.

const WANDER_SPEED := 50.0
const WANDER_RADIUS := 120.0

@export var enemy_id: String = ""

var _home: Vector2
var _direction: Vector2 = Vector2.ZERO
var _triggered: bool = false

func _ready() -> void:
	collision_layer = 0
	collision_mask = 1
	_home = position

	var visual := ColorRect.new()
	visual.color = Color(0.85, 0.25, 0.25)  # danger-red placeholder
	visual.size = Vector2(26, 26)
	visual.position = Vector2(-13, -13)
	add_child(visual)

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = Vector2(26, 26)
	shape.shape = rect
	add_child(shape)

	body_entered.connect(_on_body_entered)

	var timer := Timer.new()
	timer.wait_time = 1.2
	timer.timeout.connect(_pick_direction)
	add_child(timer)
	timer.start()
	_pick_direction()

func _pick_direction() -> void:
	if position.distance_to(_home) > WANDER_RADIUS:
		_direction = (_home - position).normalized()
	else:
		_direction = Vector2.from_angle(randf() * TAU) if randf() > 0.3 else Vector2.ZERO

func _process(delta: float) -> void:
	if not _triggered:
		position += _direction * WANDER_SPEED * delta

func _on_body_entered(body: Node) -> void:
	if _triggered or not (body is CharacterBody2D):
		return
	_triggered = true
	body.can_move = false
	SceneRouter.goto_battle(enemy_id)
