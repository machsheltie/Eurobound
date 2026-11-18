"""Tests for blender_lock.py (fake commands, no Blender).

Run from the repo root:
  python -I -m unittest discover -s Tools/item3d -p test_blender_lock.py
"""
import importlib.util, json, os, subprocess, sys, tempfile, time, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "blender_lock.py")
spec = importlib.util.spec_from_file_location("blender_lock", SCRIPT)
bl = importlib.util.module_from_spec(spec); spec.loader.exec_module(bl)

# Fake "Blender": logs start/end timestamps to a file, sleeping in between.
FAKE = ("import sys,time; log,tag,dur=sys.argv[1],sys.argv[2],float(sys.argv[3]);"
        "open(log,'a').write(f'{tag} start {time.time()}'+chr(10));time.sleep(dur);"
        "open(log,'a').write(f'{tag} end {time.time()}'+chr(10))")


def dead_pid():
    p = subprocess.Popen([sys.executable, "-I", "-c", "pass"]); p.wait()
    return p.pid


class LockTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="bl_test_")
        self.lock = os.path.join(self.dir, "blender.lock")
        self.env = dict(os.environ, EUROBOUND_BLENDER_LOCK=self.lock)
        self.env.pop("EUROBOUND_BLENDER_LOCK_HELD", None)

    def tearDown(self):
        for n in os.listdir(self.dir):
            try: os.remove(os.path.join(self.dir, n))
            except OSError: pass
        os.rmdir(self.dir)

    def test_two_processes_run_one_after_the_other(self):
        log = os.path.join(self.dir, "log.txt")
        def start(tag):
            return subprocess.Popen([sys.executable, "-I", SCRIPT, "run", "--label", tag, "--poll", "0.05", "--",
                                     sys.executable, "-I", "-c", FAKE, log, tag, "1.0"], env=self.env)
        a, b = start("A"), start("B")
        self.assertEqual((a.wait(60), b.wait(60)), (0, 0))
        ev = {}
        for line in open(log).read().splitlines():
            tag, kind, t = line.split(); ev[(tag, kind)] = float(t)
        first, second = ("A", "B") if ev[("A", "start")] < ev[("B", "start")] else ("B", "A")
        self.assertLessEqual(ev[(first, "end")], ev[(second, "start")])
        self.assertFalse(os.path.exists(self.lock), "lock released")

    def test_stale_lock_from_dead_pid_is_cleared(self):
        json.dump({"pid": dead_pid(), "time": time.time(), "label": "ghost"}, open(self.lock, "w"))
        with bl.blender_lock("t", timeout=5, poll=0.05, path=self.lock):
            self.assertEqual(json.load(open(self.lock))["pid"], os.getpid())
        self.assertFalse(os.path.exists(self.lock))

    def test_live_lock_times_out(self):
        holder = subprocess.Popen([sys.executable, "-I", "-c", "import time; time.sleep(30)"])
        try:
            json.dump({"pid": holder.pid, "time": time.time(), "label": "busy"}, open(self.lock, "w"))
            t0 = time.time()
            with self.assertRaises(bl.LockTimeout):
                bl.acquire("t", timeout=0.5, poll=0.05, path=self.lock)
            self.assertLess(time.time() - t0, 5)
            self.assertTrue(os.path.exists(self.lock), "live lock untouched")
        finally:
            holder.kill(); holder.wait()

    def test_cli_timeout_exit_code(self):
        holder = subprocess.Popen([sys.executable, "-I", "-c", "import time; time.sleep(30)"])
        try:
            json.dump({"pid": holder.pid, "time": time.time(), "label": "busy"}, open(self.lock, "w"))
            r = subprocess.run([sys.executable, "-I", SCRIPT, "run", "--timeout", "0.5", "--poll", "0.05", "--",
                                sys.executable, "-I", "-c", "print(1)"], env=self.env, capture_output=True, text=True)
            self.assertEqual(r.returncode, bl.EXIT_TIMEOUT)
            self.assertNotIn("1\n", r.stdout)
        finally:
            holder.kill(); holder.wait()

    def test_old_unreadable_lock_is_stale(self):
        open(self.lock, "w").close()
        os.utime(self.lock, (time.time() - 120, time.time() - 120))
        with bl.blender_lock("t", timeout=5, poll=0.05, path=self.lock):
            pass

    def test_nested_run_is_reentrant(self):
        # wrapper -> child python that itself takes the lock must not deadlock
        code = ("import importlib.util,sys;s=importlib.util.spec_from_file_location('b',sys.argv[1]);"
                "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
                "m.acquire('inner',timeout=3,poll=0.05).release();print('ok')")
        r = subprocess.run([sys.executable, "-I", SCRIPT, "run", "--", sys.executable, "-I", "-c", code, SCRIPT],
                           env=self.env, capture_output=True, text=True, timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("ok", r.stdout)

    def test_exit_code_passthrough_and_release(self):
        r = subprocess.run([sys.executable, "-I", SCRIPT, "run", "--", sys.executable, "-I", "-c", "raise SystemExit(7)"],
                           env=self.env)
        self.assertEqual(r.returncode, 7)
        self.assertFalse(os.path.exists(self.lock))


if __name__ == "__main__":
    unittest.main()
