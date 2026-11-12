extends GutTest
## ArcadeAmbientFx: the reduced-motion setting (flag settings.reduced_motion, field menu toggle) and
## that the ambient effects respect it.

class FakeState:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []
	var current_scene_path := ""


func _fx(s, night := true) -> ArcadeAmbientFx:
	var mats: Array[ShaderMaterial] = [ShaderMaterial.new()]
	var mist: Array[Vector3] = [Vector3(1, 0, 1), Vector3(-2, 0, 0)]
	var fx := ArcadeAmbientFx.new()
	add_child_autofree(fx)
	fx.night = night
	fx.setup(s, mats, mist, Rect2(-3, -3, 6, 6))
	return fx


func test_ambient_fx_setting_defaults_off_and_round_trips_through_flags() -> void:
	var s := FakeState.new()
	assert_false(ArcadeAmbientFx.is_reduced(s))
	ArcadeAmbientFx.set_reduced(s, true)
	assert_true(s.flags["settings.reduced_motion"])
	assert_true(ArcadeAmbientFx.is_reduced(s))


func test_field_menu_settings_interact_toggles_reduced_motion() -> void:
	var s := FakeState.new()
	var m := FieldMenu.new()
	m.setup(s)
	add_child_autofree(m)
	m.mode = "Settings"
	assert_string_contains(m._settings_text(), "Reduced motion: Off")
	m.press("interact")
	assert_true(ArcadeAmbientFx.is_reduced(s))
	assert_string_contains(m._settings_text(), "Reduced motion: On")
	m.press("interact")
	assert_false(ArcadeAmbientFx.is_reduced(s))
	m.press("cancel")
	assert_eq(m.mode, "root")


func test_ambient_fx_motion_on_mist_emits_and_floor_pulses() -> void:
	var fx := _fx(FakeState.new())
	fx._process(1.5)
	assert_eq(fx._mist.size(), 2)
	for p in fx._mist:
		assert_true(p.emitting)
	for h in fx._haze:
		assert_false(h.visible)
	assert_false(fx._glow.get_shader_parameter("steady"))
	assert_almost_eq(float(fx._glow.get_shader_parameter("pulse_time")), 1.5, 0.001)


func test_ambient_fx_reduced_motion_stills_mist_pulse_and_flicker() -> void:
	var s := FakeState.new()
	var fx := _fx(s)
	fx._process(1.0)
	ArcadeAmbientFx.set_reduced(s, true)
	var t0 := fx.time
	fx._process(3.0)
	assert_eq(fx.time, t0, "time frozen while reduced")
	for p in fx._mist:
		assert_false(p.emitting)
	for h in fx._haze:
		assert_true(h.visible, "static low haze replaces the drifting mist")
	assert_true(fx._glow.get_shader_parameter("steady"))
	assert_almost_eq(float(fx._materials[0].get_shader_parameter("emission_energy")), ArcadeAmbientFx.BASE_EMISSION, 0.0001)


func test_ambient_fx_floor_glow_is_night_only() -> void:
	var fx := _fx(FakeState.new(), false)
	assert_false(fx._glow_mesh.visible)
	fx.set_night(true)
	assert_true(fx._glow_mesh.visible)


func test_ambient_fx_emission_factor_stays_subtle_with_short_faults() -> void:
	var lo := 10.0
	var hi := 0.0
	var t := 0.0
	while t < 40.0:
		var f := ArcadeAmbientFx.emission_factor(t)
		lo = minf(lo, f)
		hi = maxf(hi, f)
		t += 0.02
	assert_gt(lo, 0.6)
	assert_lt(hi, 1.1)
	assert_lt(lo, 0.8, "a fault dips the screens")


func _fx_with_screens(s, night := true) -> ArcadeAmbientFx:
	var mats: Array[ShaderMaterial] = [ShaderMaterial.new()]
	var mist: Array[Vector3] = []
	var screens: Array[Vector3] = [Vector3(0, 1.9, 0), Vector3(3, 1.9, 0)]
	var fx := ArcadeAmbientFx.new()
	fx.rng.seed = 42
	add_child_autofree(fx)
	fx.night = night
	fx.setup(s, mats, mist, Rect2(-3, -3, 6, 6), 1.0, screens, 45.0)
	return fx


func test_ambient_fx_sparks_motion_on_burst_rarely_at_cabinet_tops() -> void:
	var fx := _fx_with_screens(FakeState.new())
	assert_eq(fx._sparks.size(), 2)
	for i in 600:
		fx._process(0.1)
	assert_gt(fx.bursts_fired, 2, "sparks do fire over a minute")
	assert_lt(fx.bursts_fired, 20, "but they stay rare")


func test_ambient_fx_glitch_is_one_short_blink_and_hidden_again() -> void:
	var fx := _fx_with_screens(FakeState.new())
	fx.time = fx._glitch_next
	fx._process(0.01)
	assert_eq(fx.glitches_fired, 1)
	var shown := 0
	for q in fx._glitch_quads:
		if q.visible:
			shown += 1
	assert_eq(shown, 1, "one screen at a time")
	fx._process(ArcadeAmbientFx.GLITCH_LENGTH + 0.05)
	for q in fx._glitch_quads:
		assert_false(q.visible)


func test_ambient_fx_reduced_motion_fires_no_sparks_or_glitches() -> void:
	var s := FakeState.new()
	var fx := _fx_with_screens(s)
	ArcadeAmbientFx.set_reduced(s, true)
	for i in 600:
		fx._process(0.1)
	assert_eq(fx.bursts_fired, 0)
	assert_eq(fx.glitches_fired, 0)
	for sp in fx._sparks:
		assert_false(sp.emitting)
	assert_true(fx._glow.get_shader_parameter("steady"), "at most a static glow")


func test_ambient_fx_diamond_floor_glow_turns_the_grid_forty_five_degrees() -> void:
	var fx := _fx_with_screens(FakeState.new())
	assert_almost_eq(float(fx._glow.get_shader_parameter("grid_rot")), PI / 4.0, 0.0001)
	assert_eq(fx._glow.get_shader_parameter("origin"), Vector2(0, 0))
