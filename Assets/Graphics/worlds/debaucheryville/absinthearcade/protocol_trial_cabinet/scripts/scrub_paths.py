"""Rewrites machine-specific absolute paths in the projection report JSONs to package-relative form.
python scrub_paths.py <json> [<json> ...]
Any string value that is an absolute Windows/posix path becomes "<tmp>/<basename>" (temp work files) or a package-relative path when it contains 'protocol_trial_cabinet/'."""
import json, re, sys

def fix(v):
    if isinstance(v, str) and re.match(r"^([A-Za-z]:[/\\]|/)", v):
        v = v.replace("\\", "/")
        if "protocol_trial_cabinet/" in v:
            return v.split("protocol_trial_cabinet/", 1)[1]
        return "<tmp>/" + v.rsplit("/", 1)[-1]
    if isinstance(v, list):
        return [fix(x) for x in v]
    if isinstance(v, dict):
        return {k: fix(x) for k, x in v.items()}
    return v

for p in sys.argv[1:]:
    d = json.load(open(p))
    json.dump(fix(d), open(p, "w"), indent=1)
    print("scrubbed", p)
