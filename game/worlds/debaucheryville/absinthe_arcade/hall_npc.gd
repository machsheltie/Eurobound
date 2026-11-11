class_name HallNpc
extends Node3D
## A character standing in the Absinthe Arcade hall: his sprite (8-way idle/walk tags, the bros'
## pixel density), a body the bros walk around, and ambient mutters that float over his head when
## the leader comes near. He mutters to himself and the machines, never to the bros (Writers' Room
## brief), so he keeps facing his work.

signal muttered(line: String)

## How close the leader comes before he mutters (metres), how long a line shows, and the quiet
## gap before the next one.
const MUTTER_RANGE := 1.6
const SHOW_S := 3.5
const QUIET_S := 9.0
## The bros' density: 117 visible pixels are 1.8 m.
const METRES_PER_PX := 1.8 / 117.0

var jobs: Array = []
## A one-off line said the first time the leader comes near this visit (e.g. Tomáš's "Tab's open.").
var greeting := ""
## How close the leader comes before he speaks (metres).
var range_m := MUTTER_RANGE
var late := false
var sprite: PartySprite3D
## A small worn item drawn over the sprite (Tomáš's Promise-ish Ring), placed per facing.
var ring: Sprite3D
var _ring_px: Dictionary = {}
var bark: Label3D

var _rng := RandomNumberGenerator.new()
var _show_left := 0.0
var _quiet_left := 0.0
var _last := ""


## `frames`: the .aseprite path; `content_px` / `feet_px`: visible height and feet row of his frames.
func setup(frames: String, content_px: float, feet_px: float, facing: String, mutter_jobs: Array) -> void:
	jobs = mutter_jobs
	_rng.randomize()
	sprite = PartySprite3D.new()
	sprite.name = "sprite"
	sprite.sprite_frames = load(frames)
	sprite.content_height_px = content_px
	sprite.feet_row_px = feet_px
	sprite.height_m = content_px * METRES_PER_PX
	sprite.facing = facing
	add_child(sprite)
	var body := StaticBody3D.new()
	body.name = "body"
	var cs := CollisionShape3D.new()
	var capsule := CapsuleShape3D.new()
	capsule.radius = 0.25
	capsule.height = 1.6
	cs.shape = capsule
	cs.position.y = 0.8
	body.add_child(cs)
	add_child(body)
	bark = Label3D.new()
	bark.name = "bark"
	bark.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	bark.no_depth_test = true
	bark.font_size = 36
	bark.outline_size = 10
	bark.pixel_size = 0.004
	bark.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	bark.width = 520.0
	bark.modulate = Color(0.95, 0.95, 0.85)
	bark.position.y = sprite.height_m + 0.35
	bark.visible = false
	add_child(bark)


## Draws a 3 px translucent pink ring on the hand. `px_by_facing`: facing -> Vector2 pixel in the
## 128 px frame; facings without one hide it.
func add_ring(px_by_facing: Dictionary) -> void:
	_ring_px = px_by_facing
	if ring == null:
		var img := Image.create(3, 3, false, Image.FORMAT_RGBA8)
		img.fill(Color(1.0, 0.55, 0.8, 0.75))
		img.set_pixel(1, 1, Color(1.0, 0.85, 0.95, 0.9))
		ring = Sprite3D.new()
		ring.name = "ring"
		ring.texture = ImageTexture.create_from_image(img)
		ring.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
		ring.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		ring.shaded = false
		ring.render_priority = 1
		add_child(ring)
	_place_ring()


func _place_ring() -> void:
	if ring == null:
		return
	var px = _ring_px.get(sprite.facing, null)
	ring.visible = px != null
	if px == null:
		return
	ring.pixel_size = sprite.pixel_size
	ring.position = Vector3((float(px.x) - 64.0) * sprite.pixel_size,
		(sprite.feet_row_px - float(px.y)) * sprite.pixel_size, 0.03)


func _process(delta: float) -> void:
	_place_ring()
	var leader := _leader()
	tick(delta, leader.global_position if leader != null else Vector3.INF)


## Advances the mutter timers; `leader_pos` is the leader's world position (INF when there is none).
func tick(delta: float, leader_pos: Vector3) -> void:
	_quiet_left = maxf(_quiet_left - delta, 0.0)
	if _show_left > 0.0:
		_show_left -= delta
		if _show_left <= 0.0:
			bark.visible = false
			_quiet_left = QUIET_S
		return
	if _quiet_left > 0.0 or (jobs.is_empty() and greeting.is_empty()) or leader_pos == Vector3.INF:
		return
	var flat := Vector2(leader_pos.x - global_position.x, leader_pos.z - global_position.z)
	if flat.length() <= range_m and not greeting.is_empty():
		_last = greeting
		greeting = ""
		bark.text = _last
		bark.visible = true
		_show_left = SHOW_S
		muttered.emit(_last)
		return
	if flat.length() <= range_m:
		var job: String = jobs[_rng.randi_range(0, jobs.size() - 1)]
		_last = ArcadeMicrocopy.mutter(job, late, _rng, _last)
		bark.text = _last
		bark.visible = true
		_show_left = SHOW_S
		muttered.emit(_last)


func _leader() -> Node3D:
	for n in get_tree().get_nodes_in_group("player"):
		if n is Node3D and get_parent() != null and get_parent().is_ancestor_of(n):
			return n
	return null
