@tool
class_name PartySprite3D
extends AnimatedSprite3D
## A pixel-art character standing in the HD-2D world (design/style_guides/character_sprite_pipeline.md).
## Y-billboarded, crisp nearest-neighbour pixels, and LIT by the scene, so the neon and lanterns
## colour the bros at night the way Star Ocean 2R lights its sprites. Sprite frames come from an
## .aseprite file imported by Aseprite Wizard, with tags named "<action>_<direction>"
## (idle_south, walk_north_east, ...).

## Height of the character's visible pixels, used to size the sprite in real metres.
@export var content_height_px := 117.0:
	set(v):
		content_height_px = v
		_apply_scale()
## Pixel row (from the top of the frame) where the feet touch the ground.
@export var feet_row_px := 122.0:
	set(v):
		feet_row_px = v
		_apply_scale()
## Real-world height of the character in metres.
@export var height_m := 1.8:
	set(v):
		height_m = v
		_apply_scale()
@export var action := "idle":
	set(v):
		action = v
		_play_current()
@export_enum("south", "south_east", "east", "north_east", "north", "north_west", "west", "south_west")
var facing := "south":
	set(v):
		facing = v
		_play_current()

const DIRECTIONS := ["south", "south_east", "east", "north_east", "north", "north_west", "west", "south_west"]


func _ready() -> void:
	billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	shaded = true
	double_sided = false
	alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_ON
	centered = true
	_apply_scale()
	_play_current()


## Faces the sprite toward a world-space direction on the ground plane (e.g. movement velocity),
## relative to the camera so "south" always means toward the screen.
func face_world_direction(dir: Vector3, camera: Camera3D) -> void:
	if dir.length_squared() < 0.0001 or camera == null:
		return
	var cam_fwd := -camera.global_basis.z
	cam_fwd.y = 0.0
	var screen_angle := atan2(dir.x, dir.z) - atan2(-cam_fwd.x, -cam_fwd.z)
	var idx := int(round(wrapf(screen_angle, 0.0, TAU) / (TAU / 8.0))) % 8
	# Angle 0 = toward camera (south); positive goes counter-clockwise seen from above (east).
	facing = DIRECTIONS[idx]


func _apply_scale() -> void:
	if content_height_px > 0.0:
		pixel_size = height_m / content_height_px
	if sprite_frames:
		var tex := sprite_frames.get_frame_texture(sprite_frames.get_animation_names()[0], 0)
		if tex:
			# Feet on the node origin: the feet row sits on the ground.
			offset = Vector2(0, feet_row_px - tex.get_height() * 0.5)


func _play_current() -> void:
	if not is_inside_tree() or sprite_frames == null:
		return
	var anim := "%s_%s" % [action, facing]
	if sprite_frames.has_animation(anim):
		play(anim)
