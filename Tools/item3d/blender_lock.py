"""One Blender at a time on this laptop (bead Eurobound-1nvh).

Checking `tasklist` for blender.exe is racy: two agents see none and both launch. This takes an atomic
lock file instead (os.open O_CREAT|O_EXCL), holding the PID, a timestamp and a label.

CLI (from the repo root, system python, no dependencies):
  python -I Tools/item3d/blender_lock.py run [--label L] [--timeout S] -- <command ...>
  python -I Tools/item3d/blender_lock.py status
  python -I Tools/item3d/blender_lock.py clear-stale
e.g.
  python -I Tools/item3d/blender_lock.py run --label handheld -- "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python Tools/item3d/render_item.py -- in.glb out_512.png

Python callers:
  from blender_lock import blender_lock
  with blender_lock("nft_slab"):
      subprocess.run([BLENDER, ...], check=True)

Lock file: <system temp>/eurobound_blender.lock, so every worktree and every agent window shares it (a
repo-relative file would be per-worktree and protect nothing). Override with env EUROBOUND_BLENDER_LOCK.
A lock is stale (and cleared) when its PID is dead, when it is older than MAX_AGE_S, or when it is
unreadable for more than a few seconds. Nested use is safe: `run` exports EUROBOUND_BLENDER_LOCK_HELD, so a
script that takes the lock again under a wrapper does not deadlock.
Exit codes: the child's own code; 75 = timed out waiting for the lock; 2 = usage error.
"""
import argparse, contextlib, json, os, subprocess, sys, tempfile, time

EXIT_TIMEOUT = 75
HELD_ENV = "EUROBOUND_BLENDER_LOCK_HELD"
PATH_ENV = "EUROBOUND_BLENDER_LOCK"
MAX_AGE_S = 4 * 3600
DEFAULT_TIMEOUT_S = 1800
UNREADABLE_GRACE_S = 5


class LockTimeout(Exception):
    pass


def default_path():
    return os.environ.get(PATH_ENV) or os.path.join(tempfile.gettempdir(), "eurobound_blender.lock")


def pid_alive(pid):
    """Is this PID a running process? No psutil needed."""
    if not isinstance(pid, int) or pid <= 0:
        return False
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        k32.OpenProcess.restype = wintypes.HANDLE
        k32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        k32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
        k32.CloseHandle.argtypes = [wintypes.HANDLE]
        h = k32.OpenProcess(0x1000, False, pid)          # PROCESS_QUERY_LIMITED_INFORMATION
        if not h:
            return ctypes.get_last_error() == 5           # access denied means it exists
        try:
            code = wintypes.DWORD()
            if not k32.GetExitCodeProcess(h, ctypes.byref(code)):
                return True
            return code.value == 259                       # STILL_ACTIVE
        finally:
            k32.CloseHandle(h)
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def read_lock(path):
    """dict = readable lock, {} = exists but unreadable, None = no lock."""
    try:
        with open(path) as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except FileNotFoundError:
        return None
    except (OSError, ValueError):
        return {}


def _is_stale(path, d):
    if d is None:
        return False
    if not d:                                              # half-written or corrupt
        try:
            return time.time() - os.path.getmtime(path) > UNREADABLE_GRACE_S
        except OSError:
            return False
    if not pid_alive(d.get("pid")):
        return True
    return time.time() - float(d.get("time", 0)) > MAX_AGE_S


def clear_stale(path=None):
    """Remove the lock if stale. Guarded by a second O_EXCL file so two cleaners cannot delete a fresh lock."""
    path = path or default_path()
    guard = path + ".guard"
    try:
        gfd = os.open(guard, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        try:
            if time.time() - os.path.getmtime(guard) > 30:     # abandoned guard
                os.remove(guard)
        except OSError:
            pass
        return False
    try:
        os.close(gfd)
        if _is_stale(path, read_lock(path)):                   # re-check inside the guard
            try:
                os.remove(path)
                return True
            except FileNotFoundError:
                return False
        return False
    finally:
        try:
            os.remove(guard)
        except OSError:
            pass


class Lock:
    def __init__(self, path, owned=True):
        self.path, self.owned = path, owned

    def release(self):
        if not self.owned:
            return
        self.owned = False
        d = read_lock(self.path)
        if d and d.get("pid") == os.getpid():
            try:
                os.remove(self.path)
            except OSError:
                pass


def acquire(label="blender", timeout=DEFAULT_TIMEOUT_S, poll=2.0, path=None, log=None):
    path = path or default_path()
    log = log or (lambda m: print(m, file=sys.stderr, flush=True))
    held = os.environ.get(HELD_ENV)
    if held:
        d = read_lock(path)
        if d and str(d.get("pid")) == held and pid_alive(d.get("pid")):
            return Lock(path, owned=False)                     # an ancestor wrapper already holds it
    t0, announced = time.time(), 0.0
    while True:
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            if clear_stale(path):
                continue
            if time.time() - t0 >= timeout:
                d = read_lock(path) or {}
                raise LockTimeout("blender lock still held by pid %s (%s) after %.0f s" %
                                  (d.get("pid"), d.get("label"), timeout))
            if time.time() - announced >= 15:
                d = read_lock(path) or {}
                log("blender lock held by pid %s (%s); waiting" % (d.get("pid"), d.get("label")))
                announced = time.time()
            time.sleep(poll)
            continue
        with os.fdopen(fd, "w") as f:
            json.dump({"pid": os.getpid(), "time": time.time(), "label": label}, f)
        return Lock(path)


@contextlib.contextmanager
def blender_lock(label="blender", timeout=DEFAULT_TIMEOUT_S, poll=2.0, path=None):
    lk = acquire(label, timeout, poll, path)
    try:
        yield lk
    finally:
        lk.release()


def main(argv=None):
    ap = argparse.ArgumentParser(description="One Blender at a time (lock file wrapper)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="wait for the lock, run the command, release")
    r.add_argument("--label")
    r.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_S)
    r.add_argument("--poll", type=float, default=2.0)
    r.add_argument("command", nargs=argparse.REMAINDER)
    sub.add_parser("status")
    sub.add_parser("clear-stale")
    a = ap.parse_args(argv)
    path = default_path()
    if a.cmd == "status":
        d = read_lock(path)
        if d is None:
            print("free")
        else:
            print("held" if not _is_stale(path, d) else "stale", json.dumps(d))
        return 0
    if a.cmd == "clear-stale":
        print("cleared" if clear_stale(path) else "nothing to clear")
        return 0
    cmd = a.command[1:] if a.command[:1] == ["--"] else a.command
    if not cmd:
        print("usage: blender_lock.py run [--label L] [--timeout S] -- <command ...>", file=sys.stderr)
        return 2
    label = a.label or os.path.basename(cmd[0])
    try:
        lk = acquire(label, a.timeout, a.poll, path)
    except LockTimeout as e:
        print("blender_lock: " + str(e), file=sys.stderr)
        return EXIT_TIMEOUT
    try:
        env = dict(os.environ)
        env[HELD_ENV] = str(os.getpid())
        env[PATH_ENV] = path
        return subprocess.run(cmd, env=env).returncode
    finally:
        lk.release()


if __name__ == "__main__":
    sys.exit(main())
