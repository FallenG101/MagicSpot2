"""Require the complete current-main CI run before MagicSpot publication."""

import json
from pathlib import Path
import subprocess
import sys

REQUIRED = {
    "release and demo (ubuntu-latest)",
    "release and demo (macos-latest)",
    "release and demo (windows-latest)",
    "macOS universal DMG",
    "quality",
    "test (ubuntu-latest)",
    "test (macos-latest)",
    "test (windows-latest)",
    "test (windows-11-arm)",
    "Nix package",
    "docs",
    "Linux visual review",
}


def validate_visual_review(review, source_tree):
    if (
        review.get("version") != "2.0.1"
        or review.get("linux_visual_review") != "passed"
        or review.get("source_tree") != source_tree
    ):
        raise ValueError("Publication requires inspected Linux evidence for the current application source")


def validate(run, pages, sha, repository):
    if (
        run.get("head_sha") != sha
        or run.get("head_branch") != "main"
        or run.get("event") != "push"
        or run.get("path") != ".github/workflows/ci.yml"
        or run.get("head_repository", {}).get("full_name") != repository
        or run.get("status") != "completed"
        or run.get("conclusion") != "success"
    ):
        raise ValueError("Publication requires successful push-to-main CI on the release SHA")
    jobs = [job for page in pages for job in page["jobs"]]
    names = {job["name"] for job in jobs}
    missing = REQUIRED - names
    if missing:
        raise ValueError(f"Missing required CI jobs: {sorted(missing)}")
    for job in jobs:
        if (
            job.get("head_sha") != sha
            or job.get("status") != "completed"
            or job.get("conclusion") != "success"
        ):
            raise ValueError(f"CI job did not pass on the release SHA: {job['name']}")


if __name__ == "__main__":
    run_file, jobs_file, sha, repository = sys.argv[1:]
    validate(
        json.loads(Path(run_file).read_text(encoding="utf8")),
        json.loads(Path(jobs_file).read_text(encoding="utf8")),
        sha,
        repository,
    )
    review = Path("docs/magicspot/upstream-review/linux/REVIEW.json")
    source_tree = subprocess.check_output(["git", "rev-parse", "HEAD:src"], text=True).strip()
    validate_visual_review(json.loads(review.read_text(encoding="utf8")), source_tree)
    print("Every required CI job passed on the release SHA.")
