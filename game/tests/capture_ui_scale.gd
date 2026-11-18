extends Node
## Renders the field UI at a given window size, offscreen, then quits (Eurobound-z3ec). Visual QA
## helper; asserts nothing.
## The window base is 1920x1080 with canvas_items stretch and expand aspect (project.godot). The
## laptop screen is smaller than 1920x1080, so a real window would be clamped: instead each shot
## renders into a SubViewport of the target size whose 2D is stretched from the logical size exactly
## as the root window's canvas_items/expand stretch does it.
## Run:
##   Godot --path game res://tests/capture_ui_scale.tscn -- <out_png_prefix> <width> <height>
## Writes <prefix>_<shot>_<W>x<H>.png for: hall_dialogue, battle, menu_root, menu_settings,
## menu_wallet, menu_quest_log, icq.

const HALL := preload("res://worlds/debaucheryville/absinthe_arcade_interior_hd2d.tscn")
const BASE := Vector2(1920, 1080)
const CABINET := "cabinet_street_fighter"

var _vp: SubViewport
var _hall: Node


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var prefix: String = args[0]
	var w := int(args[1])
	var h := int(args[2])
	GameState.new_game(DataRepo)
	GameState.sovs = 140
	for id in ["sea_monkeys", "millennium_bug"]:
		NftVault.award(GameState, id)
	var q: Dictionary = QuestLog.quests()[0]
	for f in q.get("started_when", []).slice(0, 1):
		GameState.flags[String(f)] = true
	_vp = SubViewport.new()
	_vp.size = Vector2i(w, h)
	# canvas_items + expand: scale by the smaller ratio, then widen the logical size to fill.
	var s := minf(w / BASE.x, h / BASE.y)
	_vp.size_2d_override = Vector2i(roundi(w / s), roundi(h / s))
	_vp.size_2d_override_stretch = true
	_vp.render_target_update_mode = SubViewport.UPDATE_ALWAYS
	add_child(_vp)
	_hall = HALL.instantiate()
	_hall.spawn_player = false
	_vp.add_child(_hall)
	_hall.night = true

	# 1. The hall with the dialogue box open on the first-entry line.
	var beat: Dictionary = ArcadeHallLines.data()["first_entry"][0]
	var box := DialogueBox.new()
	_vp.add_child(box)
	box.say(String(beat["who"]), String(beat["line"]))
	await _shot(prefix, "hall_dialogue", w, h)
	box.queue_free()

	# 2. A cabinet battle, a status on a bro and a villain, the command menu up and a peek open.
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	var core := ArcadeBattle.build(CABINET, GameState, rng)
	var screen := BattleScreen.new()
	screen.setup(core, load(ArcadeBattle.backdrop_path(CABINET)), ArcadeBattle.skills())
	_vp.add_child(screen)
	core.party[0].statuses["the_shakes"] = 2
	core.enemies[0].statuses["tunnel_vision"] = 2
	for i in 40:
		if screen.state == "menu":
			break
		screen.advance(0.5)
	screen.hover_portrait(core.enemies[0])
	await _shot(prefix, "battle", w, h)
	# Desk mocks for the turn-order strip names (capture only; the game code is unchanged):
	# A = 20 px names in bigger 176x72 boxes, B = 20 px names in today's 132x56 boxes, cut to two
	# lines with an ellipsis.
	for mock in ["strip_a", "strip_b"]:
		for p: PanelContainer in screen.strip.portraits:
			var label := p.get_node_or_null("name") as Label
			if label == null:
				continue
			label.add_theme_font_size_override("font_size", 20)
			if mock == "strip_a":
				p.custom_minimum_size = Vector2(176, 72)
			else:
				p.custom_minimum_size = TurnOrderStrip.PORTRAIT_SIZE
				p.size = TurnOrderStrip.PORTRAIT_SIZE
				label.max_lines_visible = 2
				label.text_overrun_behavior = TextServer.OVERRUN_TRIM_ELLIPSIS
		if mock == "strip_a":
			screen.strip.offset_bottom = 136 + 72
		else:
			screen.strip.offset_bottom = 136 + TurnOrderStrip.PORTRAIT_SIZE.y
		await _shot(prefix, "battle_" + mock, w, h)
	screen.queue_free()

	# 3. The field menu: root, Settings, Wallet, Quest Log.
	for section in ["root", "Settings", "Wallet", "Quest Log"]:
		var menu := FieldMenu.new()
		menu.setup(GameState)
		_vp.add_child(menu)
		if section != "root":
			menu.section = menu.sections().find(section)
			menu.press("interact")
		await _shot(prefix, "menu_" + section.to_snake_case().replace(" ", "_"), w, h)
		menu.queue_free()

	# 4. The ICQ window with Tony420's first hijack line in the dialogue box above it.
	var icq := IcqWindow.new()
	_vp.add_child(icq)
	icq.open()
	var lines := Tony420Hijack.spoken_lines()
	var talk := DialogueBox.new()
	_vp.add_child(talk)
	if not lines.is_empty():
		var first: Dictionary = lines[0]
		talk.say(String(first.get("who", "")), String(first.get("line", "")))
	await _shot(prefix, "icq", w, h)
	get_tree().quit()


func _shot(prefix: String, shot: String, w: int, h: int) -> void:
	for i in 12:
		await get_tree().process_frame
	await RenderingServer.frame_post_draw
	var path := "%s_%s_%dx%d.png" % [prefix, shot, w, h]
	_vp.get_texture().get_image().save_png(path)
	print("saved ", path)
