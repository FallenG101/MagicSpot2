"""Check snapshot reporting with cherry-picked upstream history."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("upstream-drift.py").resolve()

class DriftTest(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Drift test")
        self.git("config", "user.email", "drift@example.invalid")
        self.commit("shared.txt", "base")
        self.git("branch", "upstream")
        self.commit("fork.txt", "fork")
        self.git("checkout", "upstream")
        self.integrated = self.commit("shared.txt", "upstream one")
        self.git("checkout", "main")
        self.git("cherry-pick", "-x", self.integrated)
        self.commit("UPSTREAM.md", f"- Base commit: `{self.integrated}`\n")
        self.git("update-ref", "refs/remotes/upstream/main", self.integrated)

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True, stderr=subprocess.DEVNULL).strip()

    def commit(self, name, content):
        (self.root / name).write_text(content, encoding="utf8")
        self.git("add", name)
        self.git("commit", "-m", content.splitlines()[0])
        return self.git("rev-parse", "HEAD")

    def report(self):
        return subprocess.run([sys.executable, str(SCRIPT)], cwd=self.root, text=True, capture_output=True)

    def test_integrated_snapshot_need_not_be_an_ancestor_of_fork(self):
        self.assertNotEqual(subprocess.run(["git", "merge-base", "--is-ancestor", self.integrated, "HEAD"], cwd=self.root).returncode, 0)
        result = self.report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Upstream has 0 commits", result.stdout)
        self.assertIn("0 upstream", result.stdout)

    def test_new_upstream_change_reports_real_overlap(self):
        self.commit("shared.txt", "local improvement")
        self.git("checkout", "upstream")
        tip = self.commit("shared.txt", "upstream two")
        self.git("checkout", "main")
        self.git("update-ref", "refs/remotes/upstream/main", tip)
        result = self.report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Upstream has 1 commits", result.stdout)
        self.assertIn("- `shared.txt`", result.stdout)

    def test_rewritten_upstream_requires_review(self):
        self.git("update-ref", "refs/remotes/upstream/main", self.integrated + "^")
        result = self.report()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("review upstream history", result.stderr)

if __name__ == "__main__":
    unittest.main()
