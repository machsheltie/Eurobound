class_name CharacterLooks
extends RefCounted
## Per-bro look switch: "pixel" (Aseprite sprite) or "3d" (look B, clean Tripo + Blender renders,
## author ruling 2026-11-12). Data lives in res://assets/data/party/character_looks.json.
## Look-B frames: res://assets/characters/party/<bro>/look_b/<idle|walk>/<S|SE|E|NE|N|NW|W|SW>/NN.png,
## 640x640 transparent, 300 px/m, feet at the bottom edge. Animations reuse PartySprite3D's
## "<action>_<direction>" names, so the controller needs no other change.

const CONFIG_PATH := "res://assets/data/party/character_looks.json"
const FRAMES_ROOT := "res://assets/characters/party/%s/look_b/"
const LOOK_PIXEL := "pixel"
const LOOK_3D := "3d"
const ACTIONS := ["idle", "walk"]
const DIR_FOLDERS := {
	"south": "S", "south_east": "SE", "east": "E", "north_east": "NE",
	"north": "N", "north_west": "NW", "west": "W", "south_west": "SW",
}
const DEFAULT_PPM := 300.0
const DEFAULT_FPS := {"idle": 6.0, "walk": 10.0}


static func load_config() -> Dictionary:
	var f := FileAccess.open(CONFIG_PATH, FileAccess.READ)
	if f == null:
		return {}
	var parsed = JSON.parse_string(f.get_as_text())
	return parsed if parsed is Dictionary else {}


## "pixel" unless the config explicitly says "3d" for this bro.
static func look_for(who: String, config: Dictionary = {}) -> String:
	if config.is_empty():
		config = load_config()
	var looks: Dictionary = config.get("looks", {})
	return LOOK_3D if str(looks.get(who, LOOK_PIXEL)) == LOOK_3D else LOOK_PIXEL


## Folder holding a bro's look-B frames; config["frames_root"] (a "%s" pattern) overrides it for tests.
static func frames_root(who: String, config: Dictionary = {}) -> String:
	return str(config.get("frames_root", FRAMES_ROOT)) % who


static func has_look_b(who: String, config: Dictionary = {}) -> bool:
	return ResourceLoader.exists(frames_root(who, config) + "idle/S/00.png")


## Builds idle_*/walk_* animations from the look-B folder. Frame count per animation is however
## many consecutive NN.png files exist.
static func build_frames(who: String, config: Dictionary = {}) -> SpriteFrames:
	if config.is_empty():
		config = load_config()
	var look_b: Dictionary = config.get("look_b", {})
	var frames := SpriteFrames.new()
	frames.remove_animation("default")
	for action: String in ACTIONS:
		var fps := float(look_b.get("%s_fps" % action, DEFAULT_FPS[action]))
		for dir: String in DIR_FOLDERS:
			var anim := "%s_%s" % [action, dir]
			frames.add_animation(anim)
			frames.set_animation_speed(anim, fps)
			frames.set_animation_loop(anim, true)
			var i := 0
			while true:
				var path := "%s%s/%s/%02d.png" % [frames_root(who, config), action, DIR_FOLDERS[dir], i]
				if not ResourceLoader.exists(path):
					break
				frames.add_frame(anim, load(path))
				i += 1
	return frames


## Dresses a sprite as `who`: look B when the switch says "3d" and the folder exists, otherwise the
## pixel .aseprite frames at `pixel_frames_path`. `config` overrides the JSON (tests).
static func dress(s: PartySprite3D, who: String, pixel_frames_path: String, config: Dictionary = {}) -> void:
	if config.is_empty():
		config = load_config()
	if look_for(who, config) == LOOK_3D and has_look_b(who, config):
		var frames := build_frames(who, config)
		var tex: Texture2D = frames.get_frame_texture("idle_south", 0)
		s.sprite_frames = frames
		s.smooth = true
		var ppm := float((config.get("look_b", {}) as Dictionary).get("pixels_per_metre", DEFAULT_PPM))
		s.pixel_size_override = 1.0 / ppm
		# Feet sit on the bottom edge of the render; the anchor is bottom-centre.
		s.feet_row_px = float(tex.get_height())
	else:
		var frames: SpriteFrames = load(pixel_frames_path)
		if frames == null:
			return
		s.sprite_frames = frames
		s.smooth = false
		s.pixel_size_override = 0.0
		var used := frames.get_frame_texture(frames.get_animation_names()[0], 0).get_image().get_used_rect()
		s.content_height_px = used.size.y
		s.feet_row_px = used.end.y - 1
	s.action = s.action  # replay now that frames exist
