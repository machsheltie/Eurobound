shader_type spatial;
// HD-2D painted facade with real relief: a subdivided quad displaced along its normal by a
// height map (128 = wall plane, 255 = +height_range_m proud, 0 = -height_range_m recessed),
// lit through the matching normal map. Day/night are swapped by changing albedo_tex/emission_tex.
//
// Steep relief edges (the "returns" of sills, marquee box, window reveals) have no painted
// texels of their own, so the painting would smear down them. They are shaded as dark,
// unpainted stone instead, which reads as the shadowed side of the moulding.
render_mode cull_disabled, depth_draw_opaque;

uniform sampler2D albedo_tex : source_color, filter_linear_mipmap, repeat_disable;
uniform sampler2D emission_tex : source_color, filter_linear_mipmap, repeat_disable;
uniform sampler2D height_tex : filter_linear, repeat_disable;
uniform sampler2D normal_tex : hint_normal, filter_linear_mipmap, repeat_disable;
uniform bool has_height = false;
uniform float height_range_m = 1.0;
uniform float relief_scale = 0.35;
uniform float normal_strength = 1.0;
uniform bool use_emission = false;
uniform float emission_energy = 1.6;
uniform vec2 texture_size_m = vec2(16.0, 25.75);
uniform vec3 return_tint : source_color = vec3(0.32, 0.29, 0.26);
// Relief only displaces inside the wall's own span; outside it (overhangs) stays flat.
uniform vec2 relief_u_range = vec2(0.0, 1.0);
// Double-sided hanging signs painted past a wall's corner: seen from behind, the board inside
// this UV rect (u0, v0, u1, v1) is mirrored back so its lettering reads the right way round.
// The bracket outside the rect stays a plain mirror image, which is what its back really is.
uniform bool use_back_mirror = false;
uniform vec4 back_mirror_rect = vec4(0.0);

varying float v_steep;

float sample_h(vec2 uv) {
	if (uv.x < relief_u_range.x || uv.x > relief_u_range.y) {
		return 0.0;
	}
	return (textureLod(height_tex, uv, 0.0).r * 255.0 - 128.0) / 127.0 * height_range_m * relief_scale;
}

void vertex() {
	v_steep = 0.0;
	if (has_height) {
		float h = sample_h(UV);
		VERTEX += NORMAL * h;
		// Height change across ~2 texels, in metres per metre: > ~1 means a near-vertical return.
		vec2 px = 1.0 / vec2(textureSize(height_tex, 0));
		float dx = (sample_h(UV + vec2(px.x, 0.0)) - sample_h(UV - vec2(px.x, 0.0))) / (2.0 * px.x * texture_size_m.x);
		float dy = (sample_h(UV + vec2(0.0, px.y)) - sample_h(UV - vec2(0.0, px.y))) / (2.0 * px.y * texture_size_m.y);
		v_steep = smoothstep(0.8, 2.5, length(vec2(dx, dy)));
	}
}

void fragment() {
	vec2 uv = UV;
	if (use_back_mirror && !FRONT_FACING
			&& all(greaterThanEqual(uv, back_mirror_rect.xy))
			&& all(lessThanEqual(uv, back_mirror_rect.zw))) {
		uv.x = back_mirror_rect.x + back_mirror_rect.z - uv.x;
	}
	vec4 c = texture(albedo_tex, uv);
	vec3 col = c.rgb;
	// Night textures are darker: tint returns relative to the local painted brightness.
	float lum = dot(col, vec3(0.299, 0.587, 0.114));
	col = mix(col, return_tint * (0.6 + lum), v_steep * 0.85);
	ALBEDO = col;
	ALPHA = c.a;
	ALPHA_SCISSOR_THRESHOLD = 0.5;
	ROUGHNESS = 1.0;
	SPECULAR = 0.2;
	if (has_height) {
		NORMAL_MAP = texture(normal_tex, UV).rgb;
		NORMAL_MAP_DEPTH = normal_strength;
	}
	if (use_emission) {
		EMISSION = texture(emission_tex, uv).rgb * emission_energy * (1.0 - v_steep);
	}
}
