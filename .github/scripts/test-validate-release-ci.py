"""Regression checks for exact-commit publication gates."""

import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("gate", Path(__file__).with_name("validate-release-ci.py"))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class GateTest(unittest.TestCase):
    def setUp(self):
        self.sha = "a" * 40
        self.repo = "FallenG101/MagicSpot2"
        self.run = dict(head_sha=self.sha, head_branch="main", event="push",
                        path=".github/workflows/ci.yml", head_repository=dict(full_name=self.repo),
                        status="completed", conclusion="success")
        self.jobs = [dict(name=name, head_sha=self.sha, status="completed", conclusion="success")
                     for name in sorted(gate.REQUIRED)]

    def check(self, jobs=None):
        jobs = self.jobs if jobs is None else jobs
        gate.validate(self.run, [{"jobs": jobs[:5]}, {"jobs": jobs[5:]}], self.sha, self.repo)

    def test_all_required_jobs_on_exact_sha(self):
        self.check()

    def test_missing_or_skipped_job_blocks_even_successful_run(self):
        with self.assertRaisesRegex(ValueError, "Missing required"):
            self.check(self.jobs[:-1])
        for conclusion in ("skipped", "failure", "cancelled", None):
            with self.subTest(conclusion=conclusion):
                jobs = copy.deepcopy(self.jobs)
                jobs[0]["conclusion"] = conclusion
                with self.assertRaisesRegex(ValueError, "did not pass"):
                    self.check(jobs)

    def test_wrong_job_sha_blocks(self):
        self.jobs[0]["head_sha"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "release SHA"):
            self.check()

    def test_other_failed_job_also_blocks(self):
        self.jobs.append(dict(name="additional gate", head_sha=self.sha, status="completed", conclusion="failure"))
        with self.assertRaises(ValueError):
            self.check()

    def test_run_must_be_successful_main_push_in_this_repository(self):
        for key, value in (("head_sha", "b" * 40), ("head_branch", "other"),
                           ("event", "pull_request"), ("path", ".github/workflows/other.yml"),
                           ("status", "in_progress"), ("conclusion", "failure"),
                           ("head_repository", {"full_name": "crmne/spotifast"})):
            with self.subTest(key=key):
                run = self.run | {key: value}
                with self.assertRaises(ValueError):
                    gate.validate(run, [{"jobs": self.jobs}], self.sha, self.repo)


if __name__ == "__main__":
    unittest.main()
