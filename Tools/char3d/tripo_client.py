"""DO NOT USE (author, 2026-11-13: "We may not use the Tripo API. I am NOT buying a subscription AND paying API credits.").
Kept for history only; Tripo work goes through the website on subscription credits.

Tripo v3 API client for the 3D character pipeline (one command, short output).

    python tools/char3d/tripo_client.py balance
    python tools/char3d/tripo_client.py build <image.png> <out_dir> [--faces 20000] [--texture detailed]
                                              [--anims idle,walk] [--no-rig]

`build` = upload -> image_to_model -> mesh/decimate -> animations/rig (biped, mixamo spec)
         -> animations/retarget (preset idle + walk, in place) -> download GLBs.
Writes <out_dir>/tripo_build.json with every task id, URL and credit count; prints <= 6 lines.
Key: env TRIPO_API_KEY (falls back to the Windows user environment). The key is never printed.
API docs: https://developers.tripo3d.ai/en/docs (v3; base openapi.tripo3d.ai, verified 2026-11-13).
Author rule: use this instead of the Tripo website (saves Claude usage, tools/char3d/README.md).
"""
import argparse, json, os, sys, time, urllib.request, urllib.error, uuid

# The author's key is an international-platform key: it authenticates on openapi.tripo3d.ai (verified
# 2026-11-13); openapi.tripo3d.com returns 401 for it. Override with env TRIPO_API_BASE if that changes.
BASE = os.environ.get("TRIPO_API_BASE", "https://openapi.tripo3d.ai/v3")
MODEL_GEN = "v3.1-20260211"
MODEL_RIG = "v3.0-20260909"


def key():
    k = os.environ.get("TRIPO_API_KEY")
    if not k and sys.platform == "win32":
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as h:
                k = winreg.QueryValueEx(h, "TRIPO_API_KEY")[0]
        except OSError:
            k = None
    if not k:
        sys.exit("TRIPO_API_KEY not set (user env var). Ask the author; never paste it in chat.")
    return k


def call(method, path, body=None, data=None, headers=None):
    h = {"Authorization": f"Bearer {key()}", "User-Agent": "eurobound-char3d/1.0"}
    h.update(headers or {})
    if body is not None:
        data = json.dumps(body).encode()
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(BASE + path, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            out = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} on {path}: {e.read().decode()[:300]}")
    if out.get("code") != 0:
        sys.exit(f"API error on {path}: {json.dumps(out)[:300]}")
    return out["data"]


def upload(path):
    b = "----eurobound" + uuid.uuid4().hex
    fn = os.path.basename(path)
    ctype = "image/png" if fn.lower().endswith(".png") else "image/jpeg"
    payload = (f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{fn}\"\r\n"
               f"Content-Type: {ctype}\r\n\r\n").encode() + open(path, "rb").read() + f"\r\n--{b}--\r\n".encode()
    return call("POST", "/files", data=payload, headers={"Content-Type": f"multipart/form-data; boundary={b}"})["file_token"]


def wait(task_id, label, log):
    t0 = time.time()
    while True:
        d = call("GET", f"/tasks/{task_id}")
        st = d.get("status")
        if st == "success":
            log[label] = {"task_id": task_id, "credits": d.get("credits_consumed"), "output": d.get("output", {})}
            return d
        if st in ("failed", "cancelled", "banned", "expired"):
            sys.exit(f"{label} {st}: {json.dumps(d)[:300]}")
        if time.time() - t0 > 1800:
            sys.exit(f"{label} timed out (task {task_id})")
        time.sleep(8)


def fetch(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest


def build(a):
    os.makedirs(a.out_dir, exist_ok=True)
    log = {"image": os.path.abspath(a.image)}
    tok = upload(a.image)
    gen = call("POST", "/generation/image-to-model", {
        "input": tok, "model": MODEL_GEN, "texture": True, "pbr": True,
        "texture_quality": a.texture, "texture_alignment": "original_image"})
    wait(gen["task_id"], "image_to_model", log)
    dec = call("POST", "/mesh/decimate", {"input": gen["task_id"], "model": "v3.0",
                                           "face_limit": a.faces, "smart_uv": True, "bake": True})
    d = wait(dec["task_id"], "decimate", log)
    fetch(d["output"]["model_url"], os.path.join(a.out_dir, "model_lowpoly.glb"))
    last = dec["task_id"]
    if not a.no_rig:
        rig = call("POST", "/animations/rig", {"input": last, "model": MODEL_RIG, "rig_type": "biped",
                                                "spec": "mixamo", "out_format": "glb"})
        d = wait(rig["task_id"], "rig", log)
        fetch(d["output"]["model_url"], os.path.join(a.out_dir, "model_rigged.glb"))
        for anim in [x for x in a.anims.split(",") if x]:
            rt = call("POST", "/animations/retarget", {"input": rig["task_id"], "animation": f"preset:{anim}",
                                                         "out_format": "glb", "animate_in_place": True})
            d = wait(rt["task_id"], f"anim_{anim}", log)
            fetch(d["output"]["model_url"], os.path.join(a.out_dir, f"model_{anim}.glb"))
    total = sum((v.get("credits") or 0) for v in log.values() if isinstance(v, dict))
    log["credits_total"] = total
    json.dump(log, open(os.path.join(a.out_dir, "tripo_build.json"), "w"), indent=1)
    steps = [k for k in log if k not in ("image", "credits_total")]
    print(f"OK {len(steps)} tasks: {', '.join(steps)}")
    print(f"credits used: {total}")
    print(f"files: {', '.join(sorted(f for f in os.listdir(a.out_dir) if f.endswith('.glb')))}")
    print(f"log: {os.path.join(a.out_dir, 'tripo_build.json')}")


def main():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("balance")
    b = s.add_parser("build")
    b.add_argument("image"); b.add_argument("out_dir")
    b.add_argument("--faces", type=int, default=20000)
    b.add_argument("--texture", default="detailed", choices=["fast", "standard", "detailed", "extreme"])
    b.add_argument("--anims", default="idle,walk")
    b.add_argument("--no-rig", action="store_true")
    a = p.parse_args()
    if a.cmd == "balance":
        d = call("GET", "/account/balance")
        print("balance:", json.dumps(d)[:200])
    else:
        build(a)


if __name__ == "__main__":
    main()
