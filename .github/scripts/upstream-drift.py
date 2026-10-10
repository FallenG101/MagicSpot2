"""Read-only upstream report. Fetch upstream/main before running this script."""

import re
import subprocess
from pathlib import Path


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


def report():
    provenance = Path("UPSTREAM.md").read_text(encoding="utf-8")
    match = re.search(r"^- Base commit: `([0-9a-f]{40})`$", provenance, re.MULTILINE)
    if not match:
        raise SystemExit("UPSTREAM.md must record a full Base commit SHA")
    base = match.group(1)
    upstream = git("rev-parse", "upstream/main")
    head = git("rev-parse", "HEAD")
    # Reviewed cherry-picks preserve patches and author credit, not ancestry.
    # Only upstream must descend from the recorded integration snapshot.
    if subprocess.run(
        ["git", "merge-base", "--is-ancestor", base, upstream], check=False
    ).returncode:
        raise SystemExit("Recorded base is not on upstream/main; review upstream history first")
    pending = git("rev-list", "--count", f"{base}..{upstream}")
    local_files = set(git("diff", "--name-only", base, head).splitlines())
    upstream_files = set(git("diff", "--name-only", base, upstream).splitlines())
    overlap = sorted(local_files & upstream_files)
    print("# Spotifast upstream drift")
    print(f"\nRecorded base: `{base}`")
    print(f"\nMagicSpot tip: `{head}`")
    print(f"\nUpstream tip: `{upstream}`")
    print(f"\nUpstream has {pending} commits after the reviewed integration snapshot.")
    print("\nMagicSpot uses reviewed cherry-picks; graph ahead/behind counts are not patch drift.")
    print(f"\nChanged paths since base: {len(local_files)} local, {len(upstream_files)} upstream.")
    print("\n## Changed-file overlap\n")
    if overlap:
        for path in overlap:
            print(f"- `{path}`")
    else:
        print("None.")
    print("\nReport only. No merge, release, issue, comment or profile changes were made.")


if __name__ == "__main__":
    report()
