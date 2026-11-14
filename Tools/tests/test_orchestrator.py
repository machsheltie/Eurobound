"""Tests for Tools/orchestrator. Run: python -I -m unittest discover Tools/tests

Every git test runs in its own temporary repository. Nothing here reads or writes the
real repository's index.
"""
import contextlib
import importlib.util
import io
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parents[2]


def _load(name):
    spec = importlib.util.spec_from_file_location(name, REPO / "Tools" / "orchestrator" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cp = _load("commit_paths")
la = _load("ledger_add")
bn = _load("bead_new")
gut = _load("gut")
sc = _load("sync_check")

ANCHOR = la.ANCHOR
LEDGER_TEXT = f"# Ledger\n\n- **(old) first.** Body.\n\n{ANCHOR}\n\n- resolved thing\n"


class TempRepo(unittest.TestCase):
    """A throwaway git repository with one commit."""

    def setUp(self):
        # Git variables inherited from a hook would point these commands at another repository.
        clean = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        patcher = mock.patch.dict(os.environ, clean, clear=True)
        patcher.start()
        self.addCleanup(patcher.stop)
        tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve() / "repo"
        self.root.mkdir()
        self.other = Path(tmp.name).resolve() / "other"
        self.other.mkdir()
        self.git("init", "-q", "-b", "main")
        for key, value in (("user.name", "tester"), ("user.email", "t@example.invalid"),
                           ("commit.gpgsign", "false"), ("core.autocrlf", "false"),
                           ("core.hooksPath", str(self.other / "no_hooks"))):
            self.git("config", key, value)
        self.write("Tools/a.py", "a = 1\n")
        self.write("docs/superpowers/NEXT_WORK.md", LEDGER_TEXT)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "init")

    def git(self, *args):
        p = subprocess.run(["git", "-C", str(self.root), *args], capture_output=True)
        self.assertEqual(p.returncode, 0, p.stderr.decode("utf-8", "replace"))
        return p.stdout.decode("utf-8")

    def write(self, rel, text, encoding="utf-8"):
        f = self.root / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(text.encode(encoding))
        return f

    def aux(self, name, text, encoding="utf-8"):
        f = self.other / name
        f.write_bytes(text.encode(encoding))
        return f

    def head_files(self):
        return sorted(self.git("show", "--name-only", "--format=", "HEAD").split())

    def count(self):
        return int(self.git("rev-list", "--count", "HEAD").strip())


class CommitPathsTest(TempRepo):
    def commit(self, paths_text, message="feat: thing\n", encoding="utf-8"):
        return cp.commit_paths(self.root, self.aux("paths.txt", paths_text, encoding), self.aux("msg.txt", message))

    def test_commits_only_the_listed_path_and_leaves_other_edits_unstaged(self):
        self.write("Tools/a.py", "a = 2\n")
        self.write("Tools/b.py", "b = 1\n")
        out = self.commit("Tools/a.py\n")
        self.assertEqual(self.head_files(), ["Tools/a.py"])
        self.assertIn("Tools/a.py", out)
        self.assertIn("?? Tools/b.py", self.git("status", "--porcelain"))

    def test_refuses_and_names_the_file_when_something_else_is_staged(self):
        self.write("Tools/a.py", "a = 2\n")
        self.write("Tools/b.py", "b = 1\n")
        self.git("add", "Tools/b.py")
        with self.assertRaises(cp.Refuse) as ctx:
            self.commit("Tools/a.py\n")
        self.assertIn("Tools/b.py", str(ctx.exception))
        self.assertEqual(self.count(), 1)
        self.assertEqual(self.git("diff", "--cached", "--name-only").split(), ["Tools/b.py"])

    def test_a_listed_path_that_is_already_staged_is_fine(self):
        self.write("Tools/a.py", "a = 2\n")
        self.git("add", "Tools/a.py")
        self.commit("Tools/a.py\n")
        self.assertEqual(self.head_files(), ["Tools/a.py"])

    def test_strips_bom_backslashes_quotes_and_the_absolute_repo_prefix(self):
        self.write("Tools/a.py", "a = 2\n")
        self.write("Tools/sub/c.py", "c = 1\n")
        absolute = str(self.root).replace("/", "\\") + "\\Tools\\a.py"
        self.commit(f"﻿{absolute}\r\n\r\n\"Tools\\sub\\c.py\"\r\n")
        self.assertEqual(self.head_files(), ["Tools/a.py", "Tools/sub/c.py"])

    def test_reads_a_utf16_paths_file_as_powershell_writes_it(self):
        self.write("Tools/a.py", "a = 2\n")
        self.commit("Tools/a.py\r\n", encoding="utf-16")
        self.assertEqual(self.head_files(), ["Tools/a.py"])

    def test_wrong_case_folder_resolves_to_the_tracked_spelling(self):
        self.write("Tools/a.py", "a = 2\n")
        self.commit("tools/A.PY\n")
        self.assertEqual(self.head_files(), ["Tools/a.py"])

    def test_new_file_under_a_wrong_case_folder_takes_gits_folder_spelling(self):
        self.write("Tools/new_thing.py", "n = 1\n")
        self.commit("tools/new_thing.py\n")
        self.assertEqual(self.head_files(), ["Tools/new_thing.py"])

    def test_resolve_prefers_the_index_then_the_filesystem(self):
        self.write("Tools/deep/x.py", "x = 1\n")
        tracked = ["Tools/a.py"]
        self.assertEqual(cp.resolve("tools/a.py", tracked, self.root), "Tools/a.py")
        self.assertEqual(cp.resolve("TOOLS/DEEP/X.PY", tracked, self.root), "Tools/deep/x.py")

    def test_commits_a_deletion(self):
        (self.root / "Tools" / "a.py").unlink()
        self.commit("Tools/a.py\n")
        self.assertEqual(self.git("ls-files").split(), ["docs/superpowers/NEXT_WORK.md"])

    def test_message_is_used_as_written_with_nothing_appended(self):
        self.write("Tools/a.py", "a = 2\n")
        self.commit("Tools/a.py\n", message="﻿fix: one\n\n#12 is the body, not a comment\n")
        self.assertEqual(self.git("log", "-1", "--format=%B").strip("\n"),
                         "fix: one\n\n#12 is the body, not a comment")

    def test_refuses_a_path_that_does_not_exist(self):
        with self.assertRaises(cp.Refuse) as ctx:
            self.commit("Tools/ghost.py\n")
        self.assertIn("Tools/ghost.py", str(ctx.exception))

    def test_refuses_a_directory(self):
        with self.assertRaises(cp.Refuse):
            self.commit("Tools\n")

    def test_refuses_a_path_outside_the_repository(self):
        with self.assertRaises(cp.Refuse):
            self.commit(str(self.other / "paths.txt") + "\n")

    def test_refuses_when_the_listed_paths_have_no_changes(self):
        with self.assertRaises(cp.Refuse):
            self.commit("Tools/a.py\n")
        self.assertEqual(self.count(), 1)

    def test_refuses_an_empty_list_or_message(self):
        self.write("Tools/a.py", "a = 2\n")
        with self.assertRaises(cp.Refuse):
            self.commit("\n\n")
        with self.assertRaises(cp.Refuse):
            self.commit("Tools/a.py\n", message="  \n")
        self.assertEqual(self.count(), 1)

    def test_main_returns_2_and_prints_the_staged_file_on_refusal(self):
        self.write("Tools/b.py", "b = 1\n")
        self.git("add", "Tools/b.py")
        self.write("Tools/a.py", "a = 2\n")
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            code = cp.main([str(self.aux("paths.txt", "Tools/a.py\n")), str(self.aux("msg.txt", "m\n")),
                            "--repo", str(self.root)])
        self.assertEqual(code, 2)
        self.assertIn("Tools/b.py", err.getvalue())

    def test_never_pushes(self):
        source = (REPO / "Tools" / "orchestrator" / "commit_paths.py").read_text(encoding="utf-8")
        self.assertNotIn('"push"', source)


class LedgerAddTest(TempRepo):
    path = "docs/superpowers/NEXT_WORK.md"

    def staged_diff(self):
        return self.git("diff", "--cached", "--", self.path)

    def added_lines(self, diff):
        return [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]

    def test_entry_lands_before_the_anchor_in_working_tree_and_index(self):
        la.ledger_add(self.root, "- **(new) second.** Body.")
        want = LEDGER_TEXT.replace(f"\n\n{ANCHOR}", f"\n- **(new) second.** Body.\n\n{ANCHOR}")
        self.assertEqual((self.root / self.path).read_text(encoding="utf-8"), want)
        self.assertEqual(self.git("show", f":{self.path}"), want)

    def test_only_the_entry_is_staged_when_the_file_has_other_uncommitted_edits(self):
        self.write(self.path, LEDGER_TEXT.replace("# Ledger", "# Ledger\n\nSomeone else's unsaved work."))
        la.ledger_add(self.root, "- **(new) second.** Body.")
        self.assertEqual(self.added_lines(self.staged_diff()), ["- **(new) second.** Body."])
        work = (self.root / self.path).read_text(encoding="utf-8")
        self.assertIn("Someone else's unsaved work.", work)
        self.assertIn("- **(new) second.** Body.", work)
        self.assertIn("Someone else's unsaved work.", self.git("diff", "--", self.path))

    def test_two_calls_before_one_commit_keep_both_entries_in_order(self):
        la.ledger_add(self.root, "- **(new) second.** Body.")
        la.ledger_add(self.root, "- **(new) third.** Body.")
        self.assertEqual(self.added_lines(self.staged_diff()),
                         ["- **(new) second.** Body.", "- **(new) third.** Body."])
        self.git("commit", "-q", "-m", "ledger")
        head = self.git("show", f"HEAD:{self.path}")
        self.assertLess(head.index("second"), head.index("third"))
        self.assertLess(head.index("third"), head.index(ANCHOR))

    def test_refuses_when_the_anchor_is_missing_and_changes_nothing(self):
        self.write(self.path, "# Ledger\n\nno anchor here\n")
        with self.assertRaises(la.Refuse):
            la.ledger_add(self.root, "- entry")
        self.assertEqual(self.staged_diff(), "")
        self.assertEqual((self.root / self.path).read_text(encoding="utf-8"), "# Ledger\n\nno anchor here\n")

    def test_refuses_when_only_the_index_version_lacks_the_anchor(self):
        self.write(self.path, "# no anchor\n")
        self.git("add", self.path)
        self.write(self.path, LEDGER_TEXT)
        with self.assertRaises(la.Refuse):
            la.ledger_add(self.root, "- entry")
        self.assertEqual((self.root / self.path).read_text(encoding="utf-8"), LEDGER_TEXT)

    def test_refuses_an_empty_entry_and_an_untracked_ledger(self):
        with self.assertRaises(la.Refuse):
            la.ledger_add(self.root, "   ")
        self.write("other.md", LEDGER_TEXT)
        with self.assertRaises(la.Refuse):
            la.ledger_add(self.root, "- entry", path="other.md")

    def test_same_entry_twice_is_added_once(self):
        la.ledger_add(self.root, "- **(new) second.** Body.")
        out = la.ledger_add(self.root, "- **(new) second.** Body.")
        self.assertIn("already present", out)
        self.assertEqual((self.root / self.path).read_text(encoding="utf-8").count("(new) second"), 1)

    def test_crlf_working_tree_keeps_crlf_and_the_blob_keeps_lf(self):
        self.write(self.path, LEDGER_TEXT.replace("\n", "\r\n"))
        la.ledger_add(self.root, "- **(new) second.** Body.")
        raw = (self.root / self.path).read_bytes()
        self.assertIn(b"- **(new) second.** Body.\r\n\r\n" + ANCHOR.encode(), raw)
        self.assertNotIn(b"\r", self.git("show", f":{self.path}").encode())

    def test_file_mode_and_other_staged_files_are_untouched(self):
        self.write("Tools/a.py", "a = 2\n")
        self.git("add", "Tools/a.py")
        la.ledger_add(self.root, "- **(new) second.** Body.")
        self.assertEqual(sorted(self.git("diff", "--cached", "--name-only").split()),
                         ["Tools/a.py", self.path])
        self.assertTrue(self.git("ls-files", "-s", self.path).startswith("100644 "))

    def test_ledger_add_then_commit_paths_commits_just_the_entry(self):
        self.write(self.path, LEDGER_TEXT.replace("# Ledger", "# Ledger\n\nSomeone else's unsaved work."))
        la.ledger_add(self.root, "- **(new) second.** Body.")
        self.assertEqual(self.added_lines(self.git("diff", "--cached", "--", self.path)),
                         ["- **(new) second.** Body."])


class BeadNewTest(unittest.TestCase):
    BASE = ["Fix the thing", "--acceptance", "Thing is fixed", "--agent", "tools-programmer",
            "--effort", "low", "--found-by", "Eurobound-nwqs"]

    def build(self, extra=(), description="Tools/x.py:12 does the wrong thing."):
        return bn.build(bn.parser().parse_args([*self.BASE, *extra]), description)

    def value(self, argv, flag):
        return argv[argv.index(flag) + 1]

    def test_metadata_and_matching_labels_are_added(self):
        argv, meta = self.build(["--labels", "tooling, bug"])
        self.assertEqual(meta, {"agent": "tools-programmer", "effort": "low", "found_by": "Eurobound-nwqs"})
        self.assertEqual(self.value(argv, "--labels"), "agent:tools-programmer,effort:low,tooling,bug")
        self.assertEqual(self.value(argv, "--acceptance"), "Thing is fixed")
        self.assertIn("--stdin", argv)

    def test_never_passes_an_assignee(self):
        argv, _ = self.build()
        self.assertFalse({"-a", "--assignee"} & set(argv))

    def test_discovered_from_becomes_a_dependency_and_skills_pass_through(self):
        argv, _ = self.build(["--discovered-from", "Eurobound-abc", "--skills", "tdd, code-review"])
        self.assertEqual(self.value(argv, "--deps"), "discovered-from:Eurobound-abc")
        self.assertEqual(self.value(argv, "--skills"), "tdd, code-review")
        self.assertNotIn("--deps", self.build()[0])

    def test_required_flags_are_required(self):
        for flag in ("--acceptance", "--agent", "--effort", "--found-by"):
            args = list(self.BASE)
            at = args.index(flag)
            del args[at:at + 2]
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                bn.parser().parse_args(args)

    def test_unknown_effort_is_rejected(self):
        args = [a if a != "low" else "huge" for a in self.BASE]
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            bn.parser().parse_args(args)

    def test_refuses_an_empty_description_or_blank_required_value(self):
        with self.assertRaises(bn.Refuse):
            self.build(description="  \n")
        args = [a if a != "Thing is fixed" else " " for a in self.BASE]
        with self.assertRaises(bn.Refuse):
            bn.build(bn.parser().parse_args(args), "desc")

    def test_refuses_author_ruling_without_an_ask(self):
        with self.assertRaises(bn.Refuse):
            self.build(["--labels", "author-ruling"])
        with self.assertRaises(bn.Refuse):
            self.build(["--labels", "author-ruling", "--ask-question", "Which?"])

    def test_refuses_author_ruling_with_one_or_five_options(self):
        one = ["--labels", "author-ruling", "--ask-question", "Which?", "--ask-option", "A"]
        with self.assertRaises(bn.Refuse):
            self.build(one)
        five = one + [x for o in "BCDE" for x in ("--ask-option", o)]
        with self.assertRaises(bn.Refuse):
            self.build(five)

    def test_author_ruling_with_question_and_options_builds_the_ask(self):
        argv, meta = self.build(["--labels", "author-ruling", "--ask-question", "Which?",
                                 "--ask-option", "A", "--ask-option", "B", "--ask-recommended", "2"])
        self.assertEqual(meta["ask"], {"question": "Which?", "options": [
            {"label": "A", "recommended": False}, {"label": "B", "recommended": True}]})
        self.assertIn("author-ruling", self.value(argv, "--labels").split(","))

    def test_an_ask_adds_the_author_ruling_label(self):
        argv, _ = self.build(["--ask-question", "Which?", "--ask-option", "A", "--ask-option", "B"])
        self.assertIn("author-ruling", self.value(argv, "--labels").split(","))

    def test_create_sends_description_on_stdin_and_metadata_by_file(self):
        seen = {}

        def fake(argv, description):
            seen["argv"], seen["description"] = argv, description
            seen["meta"] = Path(argv[argv.index("--metadata") + 1][1:]).read_text(encoding="utf-8")
            return subprocess.CompletedProcess(argv, 0, "Eurobound-zzzz\n", "")

        with mock.patch.object(bn, "run_bd", fake):
            out = bn.create(bn.parser().parse_args(self.BASE), "The description.")
        self.assertEqual(out, "Eurobound-zzzz")
        self.assertEqual(seen["description"], "The description.")
        self.assertIn('"found_by": "Eurobound-nwqs"', seen["meta"])
        self.assertTrue(self.value(seen["argv"], "--metadata").startswith("@"))

    def test_main_refuses_without_calling_bd(self):
        called = []
        err = io.StringIO()
        with mock.patch.object(bn, "run_bd", lambda *a: called.append(a)), contextlib.redirect_stderr(err):
            code = bn.main([*self.BASE, "--labels", "author-ruling"], stdin="desc")
        self.assertEqual(code, 2)
        self.assertEqual(called, [])
        self.assertIn("ask-question", err.getvalue())

    def test_dry_run_creates_nothing(self):
        called = []
        out = io.StringIO()
        with mock.patch.object(bn, "run_bd", lambda *a: called.append(a)), contextlib.redirect_stdout(out):
            code = bn.main([*self.BASE, "--dry-run"], stdin="desc")
        self.assertEqual((code, called), (0, []))
        self.assertIn("bd create", out.getvalue())


GUT_FAIL = """\
\x1b[33m==============================================\x1b[0m
= Run Summary
==============================================

res://tests/unit/test_wallet.gd
- test_spend_more_than_held
    [Failed]:  Expected [3] to equal [4]
          at line 21
- test_pending_thing
    [Pending]:  not yet

res://tests/unit/test_status.gd
- test_crash_waits
    [Failed]:  nope

---- Totals ----
Scripts           2
Tests             10
  Passing         7
  Failing         2
  Risky/Pending   1
Asserts           31
Time              1.203s

---- 2 failing tests ----
"""


class GutParseTest(unittest.TestCase):
    def test_failing_tests_and_totals_are_extracted(self):
        r = gut.parse("SCRIPT ERROR: Nil to bool\n   at: _static_init (res://addons/gut/gut_loader.gd:35)\n"
                      "SCRIPT ERROR: Parse Error: Could not find type \"Wallet\"\n"
                      "   at: test_x (res://tests/unit/test_wallet.gd:9)\n   noise\n" + GUT_FAIL)
        self.assertEqual(r["failing"], ["res://tests/unit/test_wallet.gd :: test_spend_more_than_held",
                                       "res://tests/unit/test_status.gd :: test_crash_waits"])
        self.assertEqual(r["totals"], ["Scripts 2", "Tests 10", "Passing 7", "Failing 2", "Risky/Pending 1",
                                       "Asserts 31", "Time 1.203s"])
        self.assertEqual(len(r["errors"]), 1)
        self.assertIn("test_wallet.gd:9", r["errors"][0])
        self.assertNotIn("noise", gut.render(r, Path("x.log")))

    def test_missing_summary_is_reported(self):
        r = gut.parse("Godot Engine v4.7.2\ncrashed\n")
        self.assertFalse(r["summary"])
        self.assertIn("did not finish", gut.render(r, Path("x.log")))


class SyncCheckTest(unittest.TestCase):
    def test_unwritten_changes_stay_pending_across_runs(self):
        first = sc.merge({}, {"changed": ["board_1", "meta"], "removed": [],
                              "files": {"board_1": "o/board_1.json", "meta": "o/meta.json"}})
        second = sc.merge(first, {"changed": [], "removed": ["board_2"], "files": {}})
        self.assertEqual(second, {"files": {"board_1": "o/board_1.json", "meta": "o/meta.json"},
                                  "removed": ["board_2"]})

    def test_render_is_one_short_block(self):
        text = sc.render({"files": {"meta": "o/meta.json"}, "removed": ["board_9"]}, {"open": 3, "closed": 5})
        self.assertIn("set    meta  o/meta.json", text)
        self.assertIn("delete board_9", text)
        self.assertLessEqual(len(text.splitlines()), 4)
        self.assertIn("nothing to write", sc.render({"files": {}, "removed": []}))


hooks = _load("hooks")


class HookRulesTest(unittest.TestCase):
    STAGED = ["Tools/other_session.py"]

    def test_pre_bash_denies_commit_without_pathspec_when_files_are_staged(self):
        reason = hooks.pre_bash('git commit -m "feat: x"', self.STAGED)
        self.assertIn("Tools/other_session.py", reason)
        self.assertIn("commit_paths.py", reason)
        heredoc = "cd repo && git commit -m \"$(cat <<'EOF'\nfeat: x\n\nbody\nEOF\n)\""
        self.assertIsNotNone(hooks.pre_bash(heredoc, self.STAGED))

    def test_pre_bash_allows_commit_with_pathspec_or_empty_index(self):
        self.assertIsNone(hooks.pre_bash('git commit -m "x" -- Tools/a.py', self.STAGED))
        self.assertIsNone(hooks.pre_bash("git commit -F msg.txt --only Tools/a.py", self.STAGED))
        self.assertIsNone(hooks.pre_bash('git commit -m "x"', []))

    def test_pre_bash_denies_commit_all_and_add_everything(self):
        for command in ('git commit -am "x"', "git commit -a -m x", "git add -A", "git add .",
                        "git -C game add -u", "git status && git add --all"):
            self.assertIsNotNone(hooks.pre_bash(command, []), command)

    def test_pre_bash_denies_staging_the_ledger_and_points_at_ledger_add(self):
        reason = hooks.pre_bash("git add docs/superpowers/NEXT_WORK.md Tools/a.py", [])
        self.assertIn("ledger_add.py", reason)

    def test_pre_bash_denies_raw_gut_but_not_the_wrapper(self):
        self.assertIn("gut.py", hooks.pre_bash("godot --headless -s addons/gut/gut_cmdln.gd -gexit", []))
        self.assertIsNone(hooks.pre_bash("python -I Tools/orchestrator/gut.py --import", []))

    def test_pre_bash_allows_ordinary_commands(self):
        for command in ("git status", "git add Tools/a.py", "git log --all -3", "git diff --cached",
                        'echo "git commit -a"; ls', "git commit --amend --no-edit -- Tools/a.py",
                        "bd create \"add a thing\" --stdin", "python -I Tools/orchestrator/commit_paths.py p m"):
            self.assertIsNone(hooks.pre_bash(command, []), command)

    def test_post_bash_reminds_after_bead_writes_and_checkout_changes_only(self):
        self.assertEqual(len(hooks.post_bash("bd close Eurobound-abc")), 1)
        self.assertIn("sync_check.py", hooks.post_bash("cd x && bd update E-1 --claim")[0])
        self.assertIn("--import", hooks.post_bash("git pull --rebase")[0])
        for command in ("bd show Eurobound-abc", "bd ready", "git status", "ls"):
            self.assertEqual(hooks.post_bash(command), [], command)


if __name__ == "__main__":
    unittest.main()
