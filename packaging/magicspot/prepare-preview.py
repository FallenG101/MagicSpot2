"""Verify CI's two Preview 1 downloads before the authorized publication."""

import hashlib
from pathlib import Path
import shutil
import sys
import zipfile


def prepare(root: Path) -> None:
    stem = "magicspot2-v2.0.0-preview.1"
    assets = {
        "windows": f"{stem}-x86_64-pc-windows-msvc.zip",
        "macos": f"{stem}-macos-universal.dmg",
    }
    verified = []
    for directory, name in assets.items():
        folder = root / directory
        path = folder / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing regular download: {name}")
        entries = (folder / "checksums.txt").read_text(encoding="ascii").splitlines()
        expected = [entry.split() for entry in entries if entry.strip()]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if expected != [[digest, name]]:
            raise ValueError(f"Checksum mismatch or unexpected inputs: {name}")
        if directory == "windows":
            with zipfile.ZipFile(path) as archive:
                prefix = name.removesuffix(".zip")
                if f"{prefix}/magicspot2.exe" not in archive.namelist():
                    raise ValueError("Windows archive is missing the application")
                if archive.testzip() is not None:
                    raise ValueError("Windows archive failed integrity verification")
        verified.append((name, digest, path))
    output = root / "release"
    output.mkdir(parents=True, exist_ok=False)
    for name, _, path in verified:
        shutil.copyfile(path, output / name)
    (output / "checksums.txt").write_text(
        "".join(f"{digest}  {name}\n" for name, digest, _ in sorted(verified)),
        encoding="ascii",
    )


if __name__ == "__main__":
    prepare(Path(sys.argv[1]))
