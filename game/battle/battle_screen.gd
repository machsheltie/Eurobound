class_name BattleScreen
extends CanvasLayer
## The side-view battle screen (round v24 ruling: HD-2D side view, bros and enemies both on screen
## in a 3D arena; an Arcade cabinet fight uses that cabinet's own art as the backdrop).
## The painted backdrop sits behind a transparent 3D viewport: the bros stand on the left facing
## east, the villains on the right. Text box on top, the bros' HP and Bravado along the bottom,
## the command menu bottom right. BattleCore does the rules; this only shows them and takes input.
##
## Villains use their battle sprites (still frames facing west, ad 3913d0a; pending author review),
## at the bros' pixel density with their feet on the floor. A villain with no sprite falls back to
## a coloured placeholder card.

signal finished(outcome: String)

const EVENT_S := 1.1
const BRO_SPRITES := {
	"lord_pilsner": "res://assets/characters/party/lord_pilsner/lord_pilsner.aseprite",
	"chadwick": "res://assets/characters/party/chadwick/chadwick.aseprite",
	"bradley": "res://assets/characters/party/bradley/bradley.aseprite",
}
const PIXEL_SIZE := 0.016
const MIRROR_TINT := Color(0.55, 0.9, 0.85, 0.85)
## The camera puts the floor (y = 0) in the painting's lower third, the backdrops' floor band.
const CAMERA_POS := Vector3(0, 3.0, 9.0)
const CAMERA_LOOK := Vector3(0, 1.9, 0)
const BRO_SPOTS := [Vector3(-3.0, 0, 0.3), Vector3(-4.1, 0, -0.6), Vector3(-1.9, 0, -1.1)]
const ENEMY_SPOTS := [Vector3(2.0, 0, -0.9), Vector3(3.4, 0, -1.9), Vector3(4.6, 0, -2.6)]
const ENEMY_SPRITE_DIR := "res://assets/characters/enemies/absinthe_arcade/"
## Palette Swap copies take these gi colourways in release order (villain doc).
const SWAP_COLORS := ["teal", "cocktail_pink", "scrubs_green", "nicotine_beige"]
## The highest a villain nameplate sits (arena units), clear of the text box.
const MAX_TAG_Y := 2.9
const CARD_COLORS := [Color(0.55, 0.25, 0.75), Color(0.2, 0.55, 0.45), Color(0.75, 0.4, 0.15)]

var core: BattleCore
var skills: Dictionary = {}
var state := "events"
var menu: Array = []          ## [[label, action, enabled]]
var cursor := 0
var target_cursor := 0
var pending_action := ""

var _queue: Array = []
var _t := 0.0
var _text: Label
var _menu_label: RichTextLabel
var _bro_labels: Array[Label] = []
var _bro_panels: Array[Panel] = []
var _arena: SubViewport
var _bodies := {}             ## BattleUnit -> Node3D
var _last_hp := {}
var _marker: Label3D


func setup(core_: BattleCore, backdrop: Texture2D, skills_: Dictionary = {}) -> void:
	core = core_
	skills = skills_
	layer = 30
	var bg := TextureRect.new()
	bg.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	bg.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	bg.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
	bg.texture = backdrop
	bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(bg)
	_build_arena()
	_build_ui()
	_pull()
	_refresh()


# --- input -------------------------------------------------------------------------------------

func _unhandled_input(event: InputEvent) -> void:
	for action in ["interact", "cancel", "move_up", "move_down", "move_left", "move_right"]:
		if event.is_action_pressed(action):
			press(action)
			get_viewport().set_input_as_handled()
			return


## One button press: interact, cancel, move_up/down/left/right.
func press(action: String) -> void:
	match state:
		"events":
			if action == "interact" and not _queue.is_empty():
				_queue.pop_front()
				_t = 0.0
		"menu":
			if action == "move_up":
				cursor = posmod(cursor - 1, menu.size())
			elif action == "move_down":
				cursor = posmod(cursor + 1, menu.size())
			elif action == "interact" and bool(menu[cursor][2]):
				_choose(String(menu[cursor][1]))
		"target", "item_target":
			var pool := _target_pool()
			if action in ["move_left", "move_up"]:
				target_cursor = posmod(target_cursor - 1, pool.size())
			elif action in ["move_right", "move_down"]:
				target_cursor = posmod(target_cursor + 1, pool.size())
			elif action == "cancel":
				state = "menu"
			elif action == "interact" and not pool.is_empty():
				_commit(pool[target_cursor])
		"items":
			if action == "move_up":
				cursor = posmod(cursor - 1, menu.size())
			elif action == "move_down":
				cursor = posmod(cursor + 1, menu.size())
			elif action == "cancel":
				_open_menu()
				return
			elif action == "interact" and not menu.is_empty():
				pending_action = "item:" + String(menu[cursor][1])
				state = "item_target"
				target_cursor = 0
		"results":
			if action == "interact":
				state = "done"
				finished.emit(core.outcome)
				queue_free()
				return
	_refresh()


func _choose(action: String) -> void:
	match action:
		"flex":
			core.flex()
			state = "events"
			_pull()
		"run":
			core.run_away()
			state = "events"
			_pull()
		"item":
			menu = []
			for id in core.usable_items():
				menu.append(["%s x%d" % [core.items[id].get("display_name", id), int(core.wallet.inventory[id])], id, true])
			cursor = 0
			state = "items"
		_:
			pending_action = action
			target_cursor = 0
			state = "target"


func _commit(target: BattleUnit) -> void:
	if pending_action == "attack":
		core.attack(target)
	elif pending_action.begins_with("skill:"):
		core.use_skill(skills.get(pending_action.trim_prefix("skill:"), {}), target)
	elif pending_action.begins_with("item:"):
		core.use_item(pending_action.trim_prefix("item:"), target)
	state = "events"
	_pull()


func _target_pool() -> Array:
	if state == "item_target":
		return core.item_targets(pending_action.trim_prefix("item:"))
	return core.targetable_enemies()


# --- frame -------------------------------------------------------------------------------------

func _process(delta: float) -> void:
	advance(delta)


func advance(delta: float) -> void:
	if core == null or state == "done":
		return
	if state != "results":
		core.tick(delta)
	_pull()
	if state == "events":
		if not _queue.is_empty():
			_t += delta
			if _t >= EVENT_S:
				_queue.pop_front()
				_t = 0.0
		elif core.outcome != "":
			state = "results"
		elif core.needs_input():
			_open_menu()
		else:
			core.step()
			_pull()
	_refresh()


func _open_menu() -> void:
	var bro := core.current()
	menu = [["ATTACK", "attack", true]]
	for id in bro.skills:
		var s: Dictionary = skills.get(id, {})
		if not s.is_empty():
			menu.append(["%s  (%d BRAVADO)" % [String(s.get("display_name", id)).to_upper(), int(s.get("bravado_cost", 0))],
				"skill:" + String(id), core.can_use_skill(bro, s)])
	menu.append(["ITEM", "item", not core.minor_used and not core.usable_items().is_empty()])
	menu.append(["FLEX", "flex", not core.minor_used])
	menu.append(["RUN", "run", true])
	cursor = clampi(cursor, 0, menu.size() - 1)
	state = "menu"


func _pull() -> void:
	if core == null:
		return
	for ev in core.events:
		_queue.append(String(ev["text"]))
	core.events.clear()


# --- drawing -----------------------------------------------------------------------------------

func _build_arena() -> void:
	var box := SubViewportContainer.new()
	box.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	box.stretch = true
	box.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(box)
	_arena = SubViewport.new()
	_arena.transparent_bg = true
	_arena.own_world_3d = true
	box.add_child(_arena)
	var cam := Camera3D.new()
	cam.fov = 38.0
	_arena.add_child(cam)
	cam.look_at_from_position(CAMERA_POS, CAMERA_LOOK)
	for i in core.party.size():
		var b := core.party[i]
		var spr := AnimatedSprite3D.new()
		spr.pixel_size = PIXEL_SIZE
		spr.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
		spr.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		spr.shaded = false
		spr.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
		spr.offset = Vector2(0, 64)
		if BRO_SPRITES.has(b.id):
			spr.sprite_frames = load(BRO_SPRITES[b.id])
			spr.play("idle_east")
		spr.position = BRO_SPOTS[i % BRO_SPOTS.size()]
		_arena.add_child(spr)
		_bodies[b] = spr
	var swaps := 0
	for i in core.enemies.size():
		var e := core.enemies[i]
		var card := Node3D.new()
		card.position = ENEMY_SPOTS[i % ENEMY_SPOTS.size()]
		var top := 1.7
		var path := enemy_sprite_path(e, swaps)
		if e.id == "player_two_palette_swap":
			swaps += 1
		if e.uses.has("mirror_of") and BRO_SPRITES.has(String(e.uses["mirror_of"])):
			# Mirror Chad: the leader's own sprite, flipped to face the party, tinted and wobbling.
			top = _add_mirror_body(card, String(e.uses["mirror_of"]))
		elif ResourceLoader.exists(path):
			var spr := Sprite3D.new()
			spr.name = "sprite"
			spr.texture = load(path)
			spr.pixel_size = PIXEL_SIZE * float(e.data.get("sprite_scale", 1.0))
			spr.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
			spr.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
			spr.shaded = false
			spr.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
			var h := float(spr.texture.get_height())
			spr.offset = Vector2(0, h * 0.5)
			spr.set_meta("path", path)
			card.add_child(spr)
			# Tag over the painted top of the sprite, kept under the text box.
			var used := spr.texture.get_image().get_used_rect()
			top = minf((h - used.position.y) * spr.pixel_size, MAX_TAG_Y)
		else:
			var quad := MeshInstance3D.new()
			var mesh := QuadMesh.new()
			mesh.size = Vector2(1.2, 1.7)
			quad.mesh = mesh
			quad.position.y = 0.85
			var mat := StandardMaterial3D.new()
			mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
			mat.albedo_color = CARD_COLORS[i % CARD_COLORS.size()]
			mat.billboard_mode = BaseMaterial3D.BILLBOARD_FIXED_Y
			quad.material_override = mat
			card.add_child(quad)
		card.set_meta("top", top)
		card.set_meta("slot", e.slot)
		var name_tag := Label3D.new()
		name_tag.text = e.display_name
		name_tag.billboard = BaseMaterial3D.BILLBOARD_ENABLED
		name_tag.font_size = 40
		name_tag.outline_size = 12
		name_tag.pixel_size = 0.0045
		name_tag.position.y = top + 0.15
		name_tag.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		name_tag.width = 240.0
		name_tag.no_depth_test = true
		card.add_child(name_tag)
		_arena.add_child(card)
		_bodies[e] = card
	_marker = Label3D.new()
	_marker.text = "V"
	_marker.font_size = 64
	_marker.outline_size = 14
	_marker.modulate = Color(1.0, 0.9, 0.2)
	_marker.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	_marker.no_depth_test = true
	_marker.pixel_size = 0.008
	_marker.visible = false
	_arena.add_child(_marker)
	for u in _bodies.keys():
		_last_hp[u] = u.hp


func _build_ui() -> void:
	var top := Panel.new()
	top.set_anchors_and_offsets_preset(Control.PRESET_TOP_WIDE)
	top.offset_left = 120
	top.offset_right = -120
	top.offset_top = 24
	top.offset_bottom = 128
	top.add_theme_stylebox_override("panel", _box())
	add_child(top)
	_text = Label.new()
	_text.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_text.offset_left = 28
	_text.offset_right = -28
	_text.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	_text.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_text.add_theme_font_size_override("font_size", 28)
	top.add_child(_text)
	for i in core.party.size():
		var p := Panel.new()
		p.anchor_top = 1.0
		p.anchor_bottom = 1.0
		p.offset_left = 40 + i * 330
		p.offset_right = p.offset_left + 310
		p.offset_top = -190
		p.offset_bottom = -24
		p.add_theme_stylebox_override("panel", _box())
		add_child(p)
		var l := Label.new()
		l.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
		l.offset_left = 18
		l.offset_top = 10
		l.add_theme_font_size_override("font_size", 24)
		p.add_child(l)
		_bro_panels.append(p)
		_bro_labels.append(l)
	var mp := Panel.new()
	mp.anchor_left = 1.0
	mp.anchor_right = 1.0
	mp.anchor_top = 1.0
	mp.anchor_bottom = 1.0
	mp.offset_left = -460
	mp.offset_right = -40
	mp.offset_top = -300
	mp.offset_bottom = -24
	mp.add_theme_stylebox_override("panel", _box())
	add_child(mp)
	_menu_label = RichTextLabel.new()
	_menu_label.bbcode_enabled = true
	_menu_label.scroll_active = false
	_menu_label.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_menu_label.offset_left = 22
	_menu_label.offset_top = 14
	_menu_label.add_theme_font_size_override("normal_font_size", 26)
	mp.add_child(_menu_label)


static func _box(highlight := false) -> StyleBoxFlat:
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.04, 0.02, 0.08, 0.86)
	sb.border_color = Color(1.0, 0.85, 0.3) if highlight else Color(0.75, 0.45, 1.0)
	sb.set_border_width_all(4)
	sb.set_corner_radius_all(10)
	return sb


func _refresh() -> void:
	if core == null:
		return
	match state:
		"results":
			match core.outcome:
				"won":
					_text.text = "THE BROS WIN!"
				"lost":
					_text.text = "GAME OVER"
				"survived":
					_text.text = "THE BROS SURVIVED."
				_:
					_text.text = "THE BROS GOT AWAY."
		"menu", "items", "target", "item_target":
			_text.text = "What will %s do?" % core.current().display_name if core.current() != null else ""
		_:
			_text.text = String(_queue[0]) if not _queue.is_empty() else ""
	var cur := core.current()
	for i in core.party.size():
		var b := core.party[i]
		var tags := []
		for s in b.statuses.keys():
			tags.append(BattleCore._status_name(s).to_upper())
		if b.gone_turns > 0:
			tags.append("SWALLOWED")
		_bro_labels[i].text = "%s\nHP %d / %d\nBRAVADO %d / %d %s\n%s" % [
			b.display_name.to_upper(), ceili(b.meter), b.max_hp, b.bravado, b.max_bravado,
			b.tier().to_upper(), " ".join(tags)]
		_bro_labels[i].modulate = Color(0.55, 0.55, 0.55) if b.is_down() else Color.WHITE
		_bro_panels[i].add_theme_stylebox_override("panel", _box(b == cur and state in ["menu", "target", "items", "item_target"]))
	var lines := []
	match state:
		"menu", "items":
			for i in menu.size():
				var mark := "> " if i == cursor else "   "
				var line := mark + String(menu[i][0])
				lines.append(line if bool(menu[i][2]) else "[color=#777777]%s[/color]" % line)
			_menu_label.text = "\n".join(lines)
		"target", "item_target":
			var pool := _target_pool()
			if not pool.is_empty():
				_menu_label.text = "WHO?\n> " + pool[clampi(target_cursor, 0, pool.size() - 1)].display_name
		_:
			_menu_label.text = ""
	_menu_label.get_parent().visible = state in ["menu", "items", "target", "item_target"]
	_update_bodies()


func _update_bodies() -> void:
	for u: BattleUnit in _bodies.keys():
		var n: Node3D = _bodies[u]
		var gone := (not u.is_party() and u.is_down()) or u.gone_turns > 0 or u.dormant
		n.visible = not gone
		if not u.is_party() and int(n.get_meta("slot", u.slot)) != u.slot:
			n.position = ENEMY_SPOTS[u.slot % ENEMY_SPOTS.size()]   # the Wisp's split shuffles the row
			n.set_meta("slot", u.slot)
		if not u.is_party() and n.has_node("sprite"):
			_refresh_enemy_sprite(u, n.get_node("sprite") as Sprite3D)
		if u.is_party():
			(n as AnimatedSprite3D).modulate = Color(0.4, 0.4, 0.45) if u.is_down() else Color.WHITE
		if int(_last_hp.get(u, u.hp)) > u.hp:
			var tw := n.create_tween()
			var home := n.position
			tw.tween_property(n, "position:x", home.x + 0.18, 0.05)
			tw.tween_property(n, "position:x", home.x - 0.18, 0.08)
			tw.tween_property(n, "position:x", home.x, 0.05)
		_last_hp[u] = u.hp
	_marker.visible = false
	if state in ["target", "item_target"]:
		var pool := _target_pool()
		if not pool.is_empty():
			var t: BattleUnit = pool[clampi(target_cursor, 0, pool.size() - 1)]
			if _bodies.has(t):
				_marker.visible = true
				var tn := _bodies[t] as Node3D
				_marker.position = tn.position + Vector3(0, 2.25 if t.is_party() else float(tn.get_meta("top", 1.7)) + 0.55, 0)


## The battle sprite for a villain: Ninjas by their current palette (Sauce Swap trades them),
## Palette Swaps by release order.
static func enemy_sprite_path(e: BattleUnit, swap_index: int = 0) -> String:
	if e.data.has("sprite_id"):   # the Wisp's illusions wear her sprite: no tell
		return ENEMY_SPRITE_DIR + String(e.data["sprite_id"]) + "_battle_w.png"
	match e.id:
		"condiment_clan_ninja":
			return ENEMY_SPRITE_DIR + "condiment_clan_ninja_%s_battle_w.png" % e.palette
		"player_two_palette_swap":
			return ENEMY_SPRITE_DIR + "player_two_palette_swap_%s_battle_w.png" % SWAP_COLORS[swap_index % SWAP_COLORS.size()]
	return ENEMY_SPRITE_DIR + e.id + "_battle_w.png"


## Mirror Chad's body: a bro's own sprite flipped to face west, tinted and gently warped.
## Returns the height the name tag sits at.
func _add_mirror_body(card: Node3D, bro_id: String) -> float:
	var spr := AnimatedSprite3D.new()
	spr.name = "mirror"
	spr.sprite_frames = load(BRO_SPRITES[bro_id])
	spr.pixel_size = PIXEL_SIZE
	spr.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	spr.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	spr.shaded = false
	spr.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	spr.offset = Vector2(0, 64)
	spr.flip_h = true
	spr.modulate = MIRROR_TINT
	spr.play("idle_east")
	card.add_child(spr)
	var tw := spr.create_tween().set_loops()
	tw.tween_property(spr, "scale", Vector3(0.9, 1.08, 1.0), 1.1).set_trans(Tween.TRANS_SINE)
	tw.tween_property(spr, "scale", Vector3(1.05, 0.95, 1.0), 1.4).set_trans(Tween.TRANS_SINE)
	return 2.3


## A Ninja whose palette changed (Sauce Swap) changes sprite.
func _refresh_enemy_sprite(e: BattleUnit, spr: Sprite3D) -> void:
	if e.id != "condiment_clan_ninja":
		return
	var path := enemy_sprite_path(e)
	if path != String(spr.get_meta("path", "")) and ResourceLoader.exists(path):
		spr.texture = load(path)
		spr.set_meta("path", path)
