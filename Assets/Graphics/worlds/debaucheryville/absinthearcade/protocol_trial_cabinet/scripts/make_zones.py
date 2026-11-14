"""Writes the SAM zone configs (protocol step 2) for the cabinet front and side references. Run from the worktree root."""
import json, hashlib, os
D = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
def h(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
fr = f"{D}/source_references/aa_prop_cabinet_front_day.png"
sd = f"{D}/source_references/aa_prop_cabinet_side_day.png"
front = {"asset_id": "cabinet_trial_front", "image": fr, "sha256": h(fr), "model": "sam2.1_hiera_base_plus", "zones": {
 "marquee": {"pos": [[24, 60]], "box": [14, 18, 272, 100]},
 "marquee_ink": {"pos": [[100, 48]], "box": [14, 18, 272, 100], "keep_hsv": {"v": [0, 0.4]}, "close_px": 1},
 "crt_bezel": {"pos": [[42, 250]], "box": [34, 170, 252, 340]},
 "crt_screen": {"pos": [[195, 300]], "box": [46, 186, 242, 330]},
 "screen_invader": {"pos": [[145, 255]], "box": [105, 225, 185, 278]},
 "control_panel": {"pos": [[40, 378]], "box": [6, 338, 282, 402]},
 "joystick_red": {"pos": [[62, 350]], "box": [44, 338, 80, 386]},
 "lower_fascia": {"pos": [[40, 430]], "box": [6, 402, 284, 470]},
 "coin_door": {"pos": [[145, 600]], "box": [98, 480, 192, 694]},
 "kick_panel_stickers": {"pos": [[40, 600], [240, 640]], "box": [6, 583, 284, 737], "minus": ["coin_door"]},
 "rail_left": {"pos": [[6, 300]], "box": [0, 0, 16, 740]},
 "rail_right": {"pos": [[283, 300]], "box": [272, 0, 290, 740]}}}
side = {"asset_id": "cabinet_trial_side", "image": sd, "sha256": h(sd), "model": "sam2.1_hiera_base_plus", "zones": {
 "side_trim": {"pos": [[7, 420]], "box": [0, 0, 383, 740], "keep_hsv": {"h": [0.09, 0.17], "s": [0.55, 1], "v": [0.6, 1]}, "close_px": 3, "largest_cc": True},
 "side_stickers": {"box": [75, 215, 345, 650], "keep_hsv": {"v": [0.32, 1]}, "close_px": 9, "minus": ["side_trim"]},
 "side_body": {"pos": [[250, 120]], "box": [0, 0, 383, 740], "minus": ["side_trim", "side_stickers"]}}}
os.makedirs(f"{D}/scripts/zones", exist_ok=True)
json.dump(front, open(f"{D}/scripts/zones/cabinet_front_ref.json", "w"), indent=1)
json.dump(side, open(f"{D}/scripts/zones/cabinet_side_ref.json", "w"), indent=1)
print("ok")
