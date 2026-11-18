class_name StreetEnemy
extends CharacterBody3D
## A street enemy on the map, Option A point 1 (author, Eurobound Desk Eurobound-skjd-q2,
## 2026-11-16; docs/superpowers/specs/2026-11-16-Eurobound-skjd-proposal.md section 3;
## design/mechanics/Battle/street_encounters.md). It is visible, and it stands still, wanders, or
## walks toward the bros. Walking into the leader (or the leader into it) reports a contact;
## StreetEncounters on the same screen decides what the contact does.
##
## Which enemy appears where, how it moves, how fast and how far are the enemy doc's (its
## "Zone / Encounter Table" and "Overworld Sprite", design/templates/enemy_template.md) and the
## author's; none is ruled yet (Eurobound-iqgo). So everything about movement is per instance and
## defaults to "not set": speed 0, radius 0, sight 0. An enemy with nothing set stands still.
##
## Respawn (point 6): a beaten enemy is freed, and nothing about it is saved. It is part of its
## screen, so it is back the next time the screen loads (the bros leave and return).

const GROUP := "street_enemies"
## No level in its enemy doc yet: auto-win never applies to it.
const NO_LEVEL := -1
## Close enough to a wander point to pick the next one (engine tolerance, metres).
const ARRIVE_M := 0.1

enum Movement { STAND, WANDER, APPROACH }
const STAND := Movement.STAND
const WANDER := Movement.WANDER
const APPROACH := Movement.APPROACH

## The leader touched this enemy, or it touched the leader.
signal touched_bros(enemy: StreetEnemy)

## The engine enemy ids this contact fights (game/assets/data/enemies), from the enemy doc.
@export var enemy_ids: Array[String] = []
## How it moves on the map (enemy doc).
@export var movement: Movement = Movement.STAND
## Metres per second while it moves (enemy doc). 0 = not set: it stays put.
@export var move_speed := 0.0
## WANDER: how far from its spawn spot it roams, metres (enemy doc). 0 = not set: it stays put.
@export var wander_radius := 0.0
## APPROACH: how close the leader must be before it walks toward him, metres (enemy doc).
## 0 = not set: it stays put.
@export var sight_range := 0.0
## Its level for the auto-win test (enemy doc). NO_LEVEL = none yet.
@export var level := NO_LEVEL
## Its overworld sprite (enemy doc "Overworld Sprite"). None yet: a plain stand-in card.
@export var overworld_texture: Texture2D

## Ground-plane direction it faces: the way it last walked. The first-strike test reads it.
var facing_dir := Vector3.BACK
## True while a fight is up on this screen: it neither moves nor counts contact.
var frozen := false
## Where it spawned: the centre of its wander.
var home := Vector3.ZERO
var rng := RandomNumberGenerator.new()

var _wander_target: Variant = null
var _excepted: Array = []


func _init() -> void:
	add_to_group(GROUP)
	# It hits the world but nothing hits it, so the leader walks into its contact area instead of
	# being pushed off.
	collision_layer = 0
	collision_mask = 1
	var shape := CollisionShape3D.new()
	shape.name = "body_shape"
	shape.shape = _capsule()
	shape.position.y = 0.8
	add_child(shape)
	var contact := Area3D.new()
	contact.name = "contact"
	contact.collision_layer = 0
	contact.collision_mask = 1
	var cshape := CollisionShape3D.new()
	cshape.shape = _capsule()
	cshape.position.y = 0.8
	contact.add_child(cshape)
	contact.body_entered.connect(_on_body_entered)
	add_child(contact)


## The bros' own body size (PlayerController), so a touch is a touch.
static func _capsule() -> CapsuleShape3D:
	var c := CapsuleShape3D.new()
	c.radius = 0.25
	c.height = 1.6
	return c


func _ready() -> void:
	home = position
	rng.randomize()
	_build_look()


## The overworld sprite, or a plain stand-in card while the enemy doc has none.
func _build_look() -> void:
	if overworld_texture != null:
		var spr := Sprite3D.new()
		spr.name = "look"
		spr.texture = overworld_texture
		spr.pixel_size = BattleScreen.PIXEL_SIZE
		spr.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
		spr.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		spr.shaded = false
		spr.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
		spr.offset = Vector2(0, overworld_texture.get_height() * 0.5)
		add_child(spr)
		return
	var quad := MeshInstance3D.new()
	quad.name = "look"
	var mesh := QuadMesh.new()
	mesh.size = Vector2(0.5, 1.6)
	quad.mesh = mesh
	quad.position.y = 0.8
	var mat := StandardMaterial3D.new()
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	mat.albedo_color = Color(0.55, 0.55, 0.6)
	mat.billboard_mode = BaseMaterial3D.BILLBOARD_FIXED_Y
	quad.material_override = mat
	add_child(quad)


func _physics_process(delta: float) -> void:
	var leader := _leader()
	if leader != null and not _excepted.has(leader):
		add_collision_exception_with(leader)
		_excepted.append(leader)
	walk(delta, leader.global_position if leader != null else global_position)


func _leader() -> PlayerController:
	for n in get_tree().get_nodes_in_group("player"):
		if n is PlayerController:
			return n
	return null


## The ground-plane direction it wants to walk this tick (unit length, or zero to stand).
func desired_direction(leader_pos: Vector3) -> Vector3:
	if frozen:
		return Vector3.ZERO
	match movement:
		Movement.APPROACH:
			if sight_range <= 0.0:
				return Vector3.ZERO
			var to := _flat(leader_pos - global_position)
			if to.length() > sight_range or to.length() < ARRIVE_M:
				return Vector3.ZERO
			return to.normalized()
		Movement.WANDER:
			if wander_radius <= 0.0:
				return Vector3.ZERO
			if _wander_target == null or _flat(_wander_target - global_position).length() < ARRIVE_M:
				_wander_target = next_wander_target()
			var to := _flat(_wander_target - global_position)
			return Vector3.ZERO if to.length() < ARRIVE_M else to.normalized()
	return Vector3.ZERO


## A random point within wander_radius of home.
func next_wander_target() -> Vector3:
	var a := rng.randf() * TAU
	var r := wander_radius * sqrt(rng.randf())
	return home + Vector3(cos(a) * r, 0.0, sin(a) * r)


## One tick of walking toward `leader_pos` (APPROACH) or its wander point (WANDER).
func walk(delta: float, leader_pos: Vector3) -> void:
	var dir := desired_direction(leader_pos)
	if dir == Vector3.ZERO or move_speed <= 0.0 or delta <= 0.0:
		velocity = Vector3.ZERO
		return
	velocity = dir * move_speed
	move_and_slide()
	facing_dir = dir


## Beaten: gone from this screen until the screen loads again.
func defeat() -> void:
	frozen = true
	visible = false
	var contact := get_node_or_null("contact") as Area3D
	if contact != null:
		contact.set_deferred("monitoring", false)
	queue_free()


func _on_body_entered(body: Node) -> void:
	if body is PlayerController and not is_queued_for_deletion():
		touched_bros.emit(self)


static func _flat(v: Vector3) -> Vector3:
	return Vector3(v.x, 0.0, v.z)
