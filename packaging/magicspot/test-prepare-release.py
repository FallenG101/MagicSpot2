"""Regression checks for the public MagicSpot download bundle."""

import hashlib
import importlib.util
from pathlib import Path
import struct
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    "prepare_release", Path(__file__).with_name("prepare-release.py")
)
prepare_release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare_release)


class PrepareReleaseTest(unittest.TestCase):
    def test_filename_ordered_package_checksums_verify(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            windows = root / "windows"
            macos = root / "macos"
            windows.mkdir()
            macos.mkdir()
            stem = "magicspot2-v2.0.0"
            pe = bytearray(128)
            pe[:2] = b"MZ"
            struct.pack_into("<I", pe, 0x3C, 0x40)
            pe[0x40:0x46] = b"PE\0\0\x64\x86"
            (windows / f"{stem}-x86_64-pc-windows-msvc.exe").write_bytes(pe)
            (windows / f"{stem}-THIRD-PARTY-LICENSES.txt").write_bytes(
                b"MIT License\nSIL OPEN FONT LICENSE\nISC License\n"
                b"GNU LESSER GENERAL PUBLIC LICENSE\n7"
            )
            (macos / f"{stem}-macos-universal.dmg").write_bytes(b"Mac DMG fixture")

            for folder in (windows, macos):
                files = sorted(folder.iterdir())
                if folder == windows:
                    # Filename order differs from digest order for this pair.
                    self.assertNotEqual(
                        [hashlib.sha256(path.read_bytes()).hexdigest() for path in files],
                        sorted(hashlib.sha256(path.read_bytes()).hexdigest() for path in files),
                    )
                (folder / "checksums.txt").write_text(
                    "".join(
                        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
                        for path in files
                    ),
                    encoding="ascii",
                )

            prepare_release.prepare(root)
            names = sorted(path.name for path in (root / "release").iterdir())
            self.assertEqual(
                names,
                [
                    "checksums.txt",
                    f"{stem}-THIRD-PARTY-LICENSES.txt",
                    f"{stem}-macos-universal.dmg",
                    f"{stem}-x86_64-pc-windows-msvc.exe",
                ],
            )


if __name__ == "__main__":
    unittest.main()
