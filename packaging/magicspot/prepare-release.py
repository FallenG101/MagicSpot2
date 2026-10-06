"""Verify CI's MagicSpot 2.0 downloads before publication."""

import hashlib
from pathlib import Path
import shutil
import struct
import sys


def prepare(root: Path) -> None:
    stem = "magicspot2-v2.0.0"
    assets = {
        "windows": [
            f"{stem}-x86_64-pc-windows-msvc.exe",
            f"magicspot2-v2.0.0-THIRD-PARTY-LICENSES.txt",
        ],
        "macos": [f"{stem}-macos-universal.dmg"],
    }
    verified = []
    for directory, names in assets.items():
        folder = root / directory
        paths = []
        for name in names:
            path = folder / name
            if path.is_symlink() or not path.is_file():
                raise ValueError(f"Missing regular download: {name}")
            paths.append(path)
        entries = (folder / "checksums.txt").read_text(encoding="ascii").splitlines()
        expected = [entry.split() for entry in entries if entry.strip()]
        if directory == "windows":
            executable = paths[0].read_bytes()
            if len(executable) < 0x40 or executable[:2] != b"MZ":
                raise ValueError("Windows download is not a PE executable")
            pe_offset = struct.unpack_from("<I", executable, 0x3C)[0]
            if (
                pe_offset + 6 > len(executable)
                or executable[pe_offset : pe_offset + 4] != b"PE\0\0"
                or executable[pe_offset + 4 : pe_offset + 6] != b"\x64\x86"
            ):
                raise ValueError("Windows download is not an x86-64 PE executable")
            licenses = paths[1].read_text(encoding="utf-8")
            for expected_license in ("MIT License", "SIL OPEN FONT LICENSE", "ISC License"):
                if expected_license not in licenses:
                    raise ValueError(f"Windows license bundle is missing {expected_license}")
        pairs = [
            (hashlib.sha256(path.read_bytes()).hexdigest(), path.name, path)
            for path in paths
        ]
        checksums = sorted((digest, name) for digest, name, _ in pairs)
        if expected != [list(entry) for entry in checksums]:
            raise ValueError(f"Checksum mismatch or unexpected inputs: {directory}")
        verified.extend(pairs)
    output = root / "release"
    output.mkdir(parents=True, exist_ok=False)
    for _, name, path in verified:
        shutil.copyfile(path, output / name)
    (output / "checksums.txt").write_text(
        "".join(f"{digest}  {name}\n" for digest, name, _ in sorted(verified)),
        encoding="ascii",
    )


if __name__ == "__main__":
    prepare(Path(sys.argv[1]))
