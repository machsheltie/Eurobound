class_name TitleScreen
extends Control
## The title screen (Eurobound-9jzp): New Game, Continue, Quit. Plain labels only; cover art is a
## separate item (Eurobound-9z3u). Continue is disabled unless some save slot holds a save that
## loads (SaveSystem rejects corrupt and incompatible saves), and opens the slot picker in Load
## (author, Eurobound Desk Eurobound-x2ws-q3). New Game starts a fresh GameState and enters the
## Arcade street. Buttons use the built-in ui_* focus actions, so keyboard and controller both work.

signal scene_requested(path: String)
signal quit_requested

const LABEL_TITLE := "Eurobound"
const LABEL_NEW_GAME := "New Game"
const LABEL_CONTINUE := "Continue"
const LABEL_QUIT := "Quit"
const START_SCREEN := "absinthe_arcade_exterior"

## Test hooks: leave null/true in the game.
var saver = null
var state = null
var repo = null
var navigate := true

var new_game_button: Button
var continue_button: Button
var quit_button: Button
var picker: SaveSlotPicker = null
var _buttons: Array[Button] = []


func _ready() -> void:
	PlayerController.ensure_input_actions()  # the slot picker reads the interact/move actions
	set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var bg := ColorRect.new()
	bg.color = Color(0.05, 0.03, 0.09)
	bg.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(bg)
	var center := CenterContainer.new()
	center.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	add_child(center)
	var box := VBoxContainer.new()
	box.add_theme_constant_override("separation", 18)
	center.add_child(box)
	var title := Label.new()
	title.text = LABEL_TITLE
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 96)
	box.add_child(title)
	new_game_button = _make_button(box, LABEL_NEW_GAME, new_game)
	continue_button = _make_button(box, LABEL_CONTINUE, continue_game)
	quit_button = _make_button(box, LABEL_QUIT, quit_game)
	refresh()


func _make_button(parent: Control, text: String, handler: Callable) -> Button:
	var b := Button.new()
	b.text = text
	b.custom_minimum_size = Vector2(360, 64)
	b.add_theme_font_size_override("font_size", 36)
	b.pressed.connect(handler)
	parent.add_child(b)
	_buttons.append(b)
	return b


## Re-reads the saves: Continue is disabled with no loadable save. Focus goes to the first
## enabled button.
func refresh() -> void:
	var save = _saver()
	continue_button.disabled = save == null or not save.has_any_save()
	_focus_first_enabled()


func _focus_first_enabled() -> void:
	for b in _buttons:
		if not b.disabled:
			if is_inside_tree():
				b.grab_focus()
			return


func new_game() -> void:
	var game_state = _state()
	var data = _repo()
	if game_state == null or data == null:
		push_error("TitleScreen: GameState or DataRepo is missing, cannot start a new game")
		return
	game_state.new_game(data)
	SceneRouter.pending_spawn = ""
	SceneRouter.pending_spot = {}
	_go(SceneRouter.scene_path(START_SCREEN))


func continue_game() -> void:
	var save = _saver()
	if picker != null or continue_button.disabled or save == null:
		return
	_set_buttons_enabled(false)
	picker = SaveSlotPicker.new()
	picker.setup(save, "load")
	add_child(picker)
	var slot: int = await picker.pick()
	picker = null
	_set_buttons_enabled(true)
	var game_state = _state()
	if slot <= 0 or game_state == null or not save.load_slot(game_state, slot):
		refresh()
		return
	save.prepare_resume(game_state)
	var path := String(game_state.current_scene_path)
	if not ResourceLoader.exists(path):
		path = SceneRouter.scene_path(START_SCREEN)
	_go(path)


func quit_game() -> void:
	quit_requested.emit()
	if navigate:
		get_tree().quit()


func _set_buttons_enabled(on: bool) -> void:
	for b in _buttons:
		b.focus_mode = Control.FOCUS_ALL if on else Control.FOCUS_NONE
		b.disabled = not on
		if not on:
			b.release_focus()
	if on:
		refresh()  # puts Continue's state back and refocuses


func _go(path: String) -> void:
	scene_requested.emit(path)
	if navigate and not path.is_empty():
		get_tree().change_scene_to_file.call_deferred(path)


func _saver():
	return saver if saver != null else get_node_or_null("/root/SaveSystem")


func _state():
	return state if state != null else get_node_or_null("/root/GameState")


func _repo():
	return repo if repo != null else get_node_or_null("/root/DataRepo")
