shader_type spatial;
// Absinthe Arcade one-blink screen glitch (PNG asset doc "Screen Flicker Effect"): a small camera-facing
// additive quad over one cabinet screen, torn into scanline bars for a few frames. Shown rarely by
// ArcadeAmbientFx and never under reduced motion.
render_mode unshaded, blend_add, depth_draw_never, cull_disabled;

uniform float seed = 0.0;
uniform vec3 tint : source_color = vec3(0.35, 1.0, 0.3);
uniform float strength = 0.55;

float hash(float n) {
	return fract(sin(n * 127.1) * 43758.5453);
}

void vertex() {
	float s = length(MODEL_MATRIX[0].xyz);
	VERTEX *= s;
	MODELVIEW_MATRIX = VIEW_MATRIX * mat4(INV_VIEW_MATRIX[0], INV_VIEW_MATRIX[1], INV_VIEW_MATRIX[2], MODEL_MATRIX[3]);
}

void fragment() {
	float row = floor(UV.y * 14.0);
	float bar = step(0.72, hash(row + seed));
	float line = step(0.55, fract(UV.y * 70.0));
	// A tear: bars drift sideways by letting the lit span start at a per-row offset.
	float shift = (hash(row * 3.1 + seed) - 0.5) * 0.4;
	float span = step(0.0, UV.x + shift - 0.1) * step(UV.x + shift, 0.9);
	vec2 e = min(UV, 1.0 - UV);
	float edge = smoothstep(0.0, 0.12, min(e.x, e.y));
	ALBEDO = tint * (0.25 * line + 0.9 * bar * span) * edge * strength;
}
