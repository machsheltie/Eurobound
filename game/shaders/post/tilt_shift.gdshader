// Tilt-shift miniature blur for the HD-2D look.
// Put on a full-rect ColorRect inside a CanvasLayer drawn above the 3D world.
// Blurs the top and bottom bands of the screen and keeps a sharp focus band.
// Godot 4 port, adapted from ChaffDev's CC0 tilt-shift shader (godotshaders.com).
shader_type canvas_item;

uniform sampler2D screen_tex : hint_screen_texture, filter_linear_mipmap;

// Screen-space Y (0 = top, 1 = bottom) of the centre of the sharp band.
uniform float focus_center : hint_range(0.0, 1.0) = 0.5;
// Half-height of the fully sharp band.
uniform float focus_half_height : hint_range(0.0, 0.5) = 0.31;
// Distance over which blur ramps from none to full.
uniform float falloff : hint_range(0.001, 0.5) = 0.2;
// Mip level used at full blur (higher = blurrier).
uniform float max_blur : hint_range(0.0, 6.0) = 1.6;
// Separate strength for the top (sky/backdrop) and bottom (foreground) bands.
uniform float top_strength : hint_range(0.0, 1.0) = 1.0;
uniform float bottom_strength : hint_range(0.0, 1.0) = 0.45;
// Slight saturation lift sells the miniature/diorama read.
uniform float saturation : hint_range(0.0, 2.0) = 1.08;
// Shows the blur mask in red when enabled.
uniform bool debug_mask = false;

void fragment() {
	float d = SCREEN_UV.y - focus_center;
	float amount = smoothstep(focus_half_height, focus_half_height + falloff, abs(d));
	amount *= (d < 0.0) ? top_strength : bottom_strength;

	vec3 col = textureLod(screen_tex, SCREEN_UV, amount * max_blur).rgb;
	float luma = dot(col, vec3(0.299, 0.587, 0.114));
	col = mix(vec3(luma), col, saturation);

	COLOR = debug_mask ? vec4(amount, 0.0, 0.0, 1.0) : vec4(col, 1.0);
}
