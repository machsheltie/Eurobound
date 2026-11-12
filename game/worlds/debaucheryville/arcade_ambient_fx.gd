class_name ArcadeAmbientFx
extends Node3D
## Absinthe Arcade ambient visual effects, purely cosmetic (design/World Design/Debaucheryville/
## environment/absinthe_arcade_environment.json: particle_effects.cabinet_green_mist,
## lighting_system.green_retrofit "slow_breath_with_short_faults", accessibility.motion_reduction;
## absinthearcade.md "Floor tiles pulse randomly, cabinet screens flicker").
##  - green mist drifting low over the floor from the cabinet bases (particles),
##  - a slow pulse on a scatter of floor tiles (additive floor overlay, night only),
##  - a slow breath with short faults on the plate's night emission (screens, bar, conduit).
##  - rare electrical sparks (short GPUParticles3D bursts) at cabinet tops, absinthearcade.md
##    "electrical sparks" / PNG asset doc Spark Small-Large,
##  - a very short scanline glitch on one cabinet screen now and then (the "Screen Flicker Effect"):
##    a small additive scanline quad, far cheaper than a full-screen pass and it keeps the painting.
## Reduced motion (GameState.flags["settings.reduced_motion"], toggled in the field menu): mist
## becomes a static low haze, floor tiles stay steadily lit, emission stays constant.

const SETTING_KEY := "settings.reduced_motion"
const BASE_EMISSION := 1.4
const GLOW_SHADER := preload("res://worlds/debaucheryville/arcade_floor_glow.gdshader")
const MIST_COLOR := Color(0.12, 0.55, 0.06)
const MIST_PER_SOURCE := 6
const MIST_ALPHA := 0.25
const HAZE_ALPHA := 0.2
const GLITCH_SHADER := preload("res://worlds/debaucheryville/arcade_screen_glitch.gdshader")
const SPARK_MIN_GAP := 7.0  ## seconds between bursts at one cabinet
const SPARK_MAX_GAP := 18.0
const GLITCH_MIN_GAP := 8.0  ## seconds between screen glitches (any cabinet)
const GLITCH_MAX_GAP := 16.0
const GLITCH_LENGTH := 0.07
const SPARK_ABOVE_SCREEN := 0.9  ## sparks fly from this far above a cabinet's screen centre

var state
var night := true
var time := 0.0
var _materials: Array[ShaderMaterial] = []
var _glow: ShaderMaterial
var _glow_mesh: MeshInstance3D
var _mist: Array[GPUParticles3D] = []
var _haze: Array[MeshInstance3D] = []
var _sparks: Array[GPUParticles3D] = []
var _spark_next: Array[float] = []
var _glitch_quads: Array[MeshInstance3D] = []
var _glitch_mat: ShaderMaterial
var _glitch_next := 0.0
var _glitch_until := -1.0
var bursts_fired := 0
var glitches_fired := 0
var rng := RandomNumberGenerator.new()


static func is_reduced(game_state) -> bool:
	return game_state != null and bool(game_state.flags.get(SETTING_KEY, false))


static func set_reduced(game_state, on: bool) -> void:
	game_state.flags[SETTING_KEY] = on


## Multiplier on the night emission at time `t`: a slow breath with a short dip ("fault") every ~9 s.
static func emission_factor(t: float) -> float:
	var f := 1.0 + 0.06 * sin(t * 0.8)
	if fmod(t + 2.0, 9.0) < 0.12 or fmod(t + 5.3, 13.0) < 0.08:
		f *= 0.72
	return f


## `floor_rect` (x, z, w, h) in diorama units, or an empty-size rect for no floor glow;
## `mist_points` are floor positions of the cabinet bases that leak mist. `screen_points` are the
## centres of cabinet screens (sparks and glitches). `grid_rot_deg` turns the glow's checker grid
## (45 for a diamond floor); `grid_phase` shifts it, in tiles.
func setup(game_state, materials: Array[ShaderMaterial], mist_points: Array[Vector3],
		floor_rect := Rect2(), tile_size := 0.9, screen_points: Array[Vector3] = [],
		grid_rot_deg := 0.0, grid_phase := Vector2.ZERO) -> void:
	state = game_state
	_materials = materials
	if floor_rect.size != Vector2.ZERO:
		_build_glow(floor_rect, tile_size, grid_rot_deg, grid_phase)
	for p in mist_points:
		_build_mist(p)
	if rng.seed == 0:
		rng.randomize()
	for p in screen_points:
		_build_spark(p + Vector3(0, SPARK_ABOVE_SCREEN, 0))
		_build_glitch(p)
	_glitch_next = rng.randf_range(GLITCH_MIN_GAP * 0.5, GLITCH_MAX_GAP)
	apply()


func set_night(value: bool) -> void:
	night = value
	apply()


## Pushes the current setting and time of day onto every effect. Also called each frame.
func apply() -> void:
	var reduced := is_reduced(state)
	var f := 1.0 if reduced or not night else emission_factor(time)
	for m in _materials:
		m.set_shader_parameter("emission_energy", BASE_EMISSION * f)
	if _glow_mesh != null:
		_glow_mesh.visible = night
		_glow.set_shader_parameter("steady", reduced)
		_glow.set_shader_parameter("pulse_time", time)
	for p in _mist:
		p.emitting = not reduced
		p.visible = not reduced
	for h in _haze:
		h.visible = reduced
	if reduced:
		for sp in _sparks:
			sp.emitting = false
		for q in _glitch_quads:
			q.visible = false


func _process(delta: float) -> void:
	if not is_reduced(state):
		time += delta
		_tick_events()
	apply()


## Schedules the rare events: a spark burst at a random cabinet, a one-blink screen glitch.
func _tick_events() -> void:
	for i in _sparks.size():
		if time >= _spark_next[i]:
			_sparks[i].restart()
			bursts_fired += 1
			_spark_next[i] = time + rng.randf_range(SPARK_MIN_GAP, SPARK_MAX_GAP)
	if not _glitch_quads.is_empty() and night and time >= _glitch_next:
		var q := _glitch_quads[rng.randi() % _glitch_quads.size()]
		_glitch_mat.set_shader_parameter("seed", rng.randf() * 100.0)
		q.visible = true
		glitches_fired += 1
		_glitch_until = time + GLITCH_LENGTH
		_glitch_next = time + rng.randf_range(GLITCH_MIN_GAP, GLITCH_MAX_GAP)
	if time >= _glitch_until:
		for g in _glitch_quads:
			g.visible = false


func _build_glow(rect: Rect2, tile_size: float, rot_deg := 0.0, phase := Vector2.ZERO) -> void:
	var plane := PlaneMesh.new()
	plane.size = rect.size
	_glow = ShaderMaterial.new()
	_glow.shader = GLOW_SHADER
	_glow.set_shader_parameter("tile_size", tile_size)
	if rot_deg != 0.0 or phase != Vector2.ZERO:
		# The grid lives in diorama coordinates, not the plane's own, so it lines up with the painted tiles.
		_glow.set_shader_parameter("origin", rect.get_center() + phase)
		_glow.set_shader_parameter("grid_rot", deg_to_rad(rot_deg))
	_glow_mesh = MeshInstance3D.new()
	_glow_mesh.name = "floor_glow"
	_glow_mesh.mesh = plane
	_glow_mesh.material_override = _glow
	_glow_mesh.position = Vector3(rect.get_center().x, 0.02, rect.get_center().y)
	_glow_mesh.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	add_child(_glow_mesh)


static func _puff_texture() -> GradientTexture2D:
	var g := Gradient.new()
	g.set_color(0, Color(1, 1, 1, 1))
	g.set_color(1, Color(0, 0, 0, 1))
	var t := GradientTexture2D.new()
	t.gradient = g
	t.fill = GradientTexture2D.FILL_RADIAL
	t.fill_from = Vector2(0.5, 0.5)
	t.fill_to = Vector2(1.0, 0.5)
	t.width = 64
	t.height = 64
	return t


func _build_mist(at: Vector3) -> void:
	var puff := _puff_texture()
	var mat := StandardMaterial3D.new()
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	mat.blend_mode = BaseMaterial3D.BLEND_MODE_ADD
	mat.billboard_mode = BaseMaterial3D.BILLBOARD_PARTICLES
	mat.vertex_color_use_as_albedo = true
	mat.albedo_texture = puff
	mat.no_depth_test = false
	mat.disable_receive_shadows = true
	var quad := QuadMesh.new()
	quad.size = Vector2(1.1, 1.1)
	quad.material = mat
	var pm := ParticleProcessMaterial.new()
	pm.emission_shape = ParticleProcessMaterial.EMISSION_SHAPE_BOX
	pm.emission_box_extents = Vector3(0.5, 0.05, 0.35)
	pm.direction = Vector3(0.3, 0.2, 0.15)
	pm.spread = 40.0
	pm.initial_velocity_min = 0.05
	pm.initial_velocity_max = 0.2
	pm.gravity = Vector3.ZERO
	pm.scale_min = 0.6
	pm.scale_max = 1.2
	var ramp := Gradient.new()
	ramp.set_color(0, Color(MIST_COLOR, 0.0))
	ramp.add_point(0.3, Color(MIST_COLOR, MIST_ALPHA))
	ramp.set_color(ramp.get_point_count() - 1, Color(MIST_COLOR, 0.0))
	var ramp_tex := GradientTexture1D.new()
	ramp_tex.gradient = ramp
	pm.color_ramp = ramp_tex
	var p := GPUParticles3D.new()
	p.name = "cabinet_mist"
	p.amount = MIST_PER_SOURCE
	p.lifetime = 7.0
	p.preprocess = 7.0
	p.process_material = pm
	p.draw_pass_1 = quad
	p.position = at + Vector3(0, 0.25, 0)
	p.visibility_aabb = AABB(Vector3(-3, -1, -3), Vector3(6, 3, 6))
	p.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	add_child(p)
	_mist.append(p)
	# Reduced motion: the same puff, laid flat and still, as the "low_static_haze".
	var haze_mat := StandardMaterial3D.new()
	haze_mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	haze_mat.blend_mode = BaseMaterial3D.BLEND_MODE_ADD
	haze_mat.albedo_texture = puff
	haze_mat.albedo_color = Color(MIST_COLOR, HAZE_ALPHA)
	haze_mat.cull_mode = BaseMaterial3D.CULL_DISABLED
	var plane := PlaneMesh.new()
	plane.size = Vector2(2.2, 1.6)
	plane.material = haze_mat
	var h := MeshInstance3D.new()
	h.name = "cabinet_haze"
	h.mesh = plane
	h.position = at + Vector3(0, 0.1, 0)
	h.visible = false
	h.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	add_child(h)
	_haze.append(h)


func _build_spark(at: Vector3) -> void:
	var mat := StandardMaterial3D.new()
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	mat.blend_mode = BaseMaterial3D.BLEND_MODE_ADD
	mat.billboard_mode = BaseMaterial3D.BILLBOARD_PARTICLES
	mat.vertex_color_use_as_albedo = true
	mat.albedo_texture = _puff_texture()
	mat.disable_receive_shadows = true
	var quad := QuadMesh.new()
	quad.size = Vector2(0.07, 0.07)
	quad.material = mat
	var pm := ParticleProcessMaterial.new()
	pm.emission_shape = ParticleProcessMaterial.EMISSION_SHAPE_SPHERE
	pm.emission_sphere_radius = 0.05
	pm.direction = Vector3(0, 1, 0.3)
	pm.spread = 70.0
	pm.initial_velocity_min = 0.8
	pm.initial_velocity_max = 2.2
	pm.gravity = Vector3(0, -5.0, 0)
	pm.scale_min = 0.5
	pm.scale_max = 1.3
	var ramp := Gradient.new()
	ramp.set_color(0, Color(1.0, 0.95, 0.7, 1.0))
	ramp.add_point(0.4, Color(0.85, 1.0, 0.45, 0.8))
	ramp.set_color(ramp.get_point_count() - 1, Color(0.2, 0.9, 0.1, 0.0))
	var ramp_tex := GradientTexture1D.new()
	ramp_tex.gradient = ramp
	pm.color_ramp = ramp_tex
	var p := GPUParticles3D.new()
	p.name = "cabinet_sparks"
	p.amount = 9
	p.lifetime = 0.45
	p.one_shot = true
	p.explosiveness = 0.95
	p.emitting = false
	p.process_material = pm
	p.draw_pass_1 = quad
	p.position = at
	p.visibility_aabb = AABB(Vector3(-2, -2, -2), Vector3(4, 4, 4))
	p.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	add_child(p)
	_sparks.append(p)
	_spark_next.append(rng.randf_range(2.0, SPARK_MAX_GAP))


func _build_glitch(at: Vector3) -> void:
	if _glitch_mat == null:
		_glitch_mat = ShaderMaterial.new()
		_glitch_mat.shader = GLITCH_SHADER
	var quad := QuadMesh.new()
	quad.size = Vector2(0.75, 0.55)
	var q := MeshInstance3D.new()
	q.name = "screen_glitch"
	q.mesh = quad
	q.material_override = _glitch_mat
	q.position = at
	q.visible = false
	q.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	add_child(q)
	_glitch_quads.append(q)
