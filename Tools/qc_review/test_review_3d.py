"""Plain assert tests (pytest is not in the paint_zones venv). Run: python Tools/qc_review/test_review_3d.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review_3d as R

# CIEDE2000 reference pairs (Sharma, Wu, Dalal 2005)
for lab1, lab2, want in [((50.0, 2.6772, -79.7751), (50.0, 0.0, -82.7485), 2.0425),
                         ((50.0, 3.1571, -77.2803), (50.0, 0.0, -82.7485), 2.8615),
                         ((60.2574, -34.0099, 36.2677), (60.4626, -34.1751, 39.4387), 1.2644)]:
    got = R.delta_e2000(lab1, lab2)
    assert abs(got - want) < 1e-3, (got, want)
assert R.hex_delta_e("#C7413A", "#C7413A") < 1e-9
assert R.hex_delta_e("#000000", "#FFFFFF") > 90
assert R.verdict_for(10.0) == "pass" and R.verdict_for(10.01) == "warn"
assert R.verdict_for(20.0) == "warn" and R.verdict_for(20.01) == "fail" and R.verdict_for(None) == "fail"
ref = {"a": {"area": 5, "median": "#808080"}, "b": {"area": 5, "median": "#808080"},
       "c": {"area": 5, "median": "#808080"}, "d": {"area": 0}}
ren = {"a": {"area": 5, "median": "#808080"}, "b": {"area": 5, "median": "#8A8A8A"},
       "c": {"area": 5, "median": "#FF0000"}}
rows = {r["zone"]: r for r in R.compare_zones(["a", "b", "c", "d", "e"], ref, ren)}
assert rows["a"]["verdict"] == "pass" and rows["c"]["verdict"] == "fail"
assert rows["d"]["verdict"] == "fail" and "empty" in rows["d"]["issue"]
assert rows["e"]["verdict"] == "fail" and "missing" in rows["e"]["issue"]
P = {"verdict": "pass"}
F = {"verdict": "fail"}
assert R.overall_outcome(True, [P]) == "BLOCKED"
assert R.overall_outcome(False, [P, F]) == "REVISION REQUIRED"
assert R.overall_outcome(False, [P, {"verdict": "warn"}]) == "APPROVED-PENDING-MANUAL"
assert R.overall_outcome(False, []) == "REVISION REQUIRED"
print("ok")
