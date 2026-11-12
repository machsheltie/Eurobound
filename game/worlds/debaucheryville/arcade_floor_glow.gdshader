shader_type spatial;
// Absinthe Arcade ambient floor glow: a faint additive overlay on the floor in which a scattering of
// tiles slowly pulse absinthe green / neon purple (design: absinthe_arcade_environment.json, the
// floor pulse; absinthearcade.md "Floor tiles pulse randomly"). Reduced motion ("steady_lit_tiles")
// freezes the pulse at a constant level.
render_mode unshaded, blend_add, depth_draw_never, cull_disabled;

uniform float tile_size = 0.9;
uniform float strength = 0.25;  // peak intensity, additive over the painting
uniform float lit_fraction = 0.1;
uniform float pulse_time = 0.0;
uniform bool steady = false;
uniform vec2 origin = vec2(0.0);  // added to the plane's local xz (diorama coordinates of its centre)
uniform float grid_rot = 0.0;     // radians; PI/4 turns the checker into the north wing's diamonds
uniform vec3 green : source_color = vec3(0.22, 1.0, 0.08);
uniform vec3 purple : source_color = vec3(0.75, 0.0, 1.0);

varying vec3 local_pos;

float hash(vec2 p) {
	return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453);
}

void vertex() {
	local_pos = VERTEX;
}

void fragment() {
	vec2 p = local_pos.xz + origin;
	float c = cos(grid_rot);
	float sn = sin(grid_rot);
	p = vec2(c * p.x + sn * p.y, -sn * p.x + c * p.y);
	vec2 cell = floor(p / tile_size);
	vec2 inside = fract(p / tile_size);
	float h = hash(cell);
	float lit = step(1.0 - lit_fraction, h);
	float wave = 0.5 + 0.5 * sin(pulse_time * 0.6 + h * 40.0);
	float level = steady ? 0.6 : wave * wave;
	// Feathered falloff from the tile centre, so it reads as light, not a painted square.
	vec2 off = abs(inside - 0.5) * 2.0;
	float grout = 1.0 - smoothstep(0.0, 1.0, length(off) * 0.8);
	vec3 tint = mix(green, purple, step(0.5, hash(cell + 7.3)));
	ALBEDO = tint * lit * level * grout * strength;
}
