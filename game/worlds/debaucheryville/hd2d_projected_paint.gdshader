shader_type spatial;
// Camera-projected painting: every surface looks up its colour in ONE painting by projecting its
// world position through the camera the painting was made from (the "paint camera"). Seen from
// that camera the geometry reproduces the painting pixel for pixel, while the geometry still gives
// characters correct depth sorting, so they can walk behind the bar, doors and alcoves.
//
// Unshaded on purpose: the painting already carries its light. Night emission is added on top as
// HDR colour so the WorldEnvironment glow picks it up.
//
// For a depth-layer cutout, `albedo_tex` is the layer's crop of the painting, `rect_px` is where
// that crop sits in the painting, and `use_alpha` discards everything outside the cutout.
render_mode unshaded, cull_disabled;

uniform sampler2D albedo_tex : source_color, filter_linear_mipmap, repeat_disable;
uniform sampler2D emit_tex : source_color, filter_linear_mipmap, repeat_disable;
uniform bool use_emission = false;
uniform float emission_energy = 1.4;
uniform bool use_alpha = false;
// World -> paint-camera space (Camera3D convention: looks down -Z, +Y up).
uniform mat4 paint_view;
uniform float focal_px = 4150.0;
uniform vec2 image_px = vec2(2752.0, 1536.0);
// x, y, width, height of this texture inside the painting, in painting pixels.
uniform vec4 rect_px = vec4(0.0, 0.0, 2752.0, 1536.0);

varying vec3 world_pos;

void vertex() {
	world_pos = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
}

void fragment() {
	vec4 c = paint_view * vec4(world_pos, 1.0);
	float depth = max(-c.z, 0.001);
	vec2 px = vec2(image_px.x * 0.5 + focal_px * c.x / depth, image_px.y * 0.5 - focal_px * c.y / depth);
	vec2 uv = (px - rect_px.xy) / rect_px.zw;
	bool outside = any(lessThan(uv, vec2(0.0))) || any(greaterThan(uv, vec2(1.0)));
	if (use_alpha && outside) {
		discard;
	}
	vec4 a = texture(albedo_tex, clamp(uv, vec2(0.0), vec2(1.0)));
	if (use_alpha && a.a < 0.5) {
		discard;
	}
	vec3 col = a.rgb;
	if (use_emission) {
		col += texture(emit_tex, clamp(uv, vec2(0.0), vec2(1.0))).rgb * emission_energy;
	}
	ALBEDO = col;
}
