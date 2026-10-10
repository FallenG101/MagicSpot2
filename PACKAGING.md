# MagicSpot packaging and releases

The authorized MagicSpot `2.0.1` candidate packages the normal app with Spotify sign-in, playback and upstream's default MilkDrop feature enabled, without demo mode. It produces a direct Windows executable with a license sidecar, a universal Mac DMG, and a combined `checksums.txt`:

| Target | Asset | Signing |
| --- | --- | --- |
| Windows x64 | `magicspot2-v2.0.1-x86_64-pc-windows-msvc.exe` plus `magicspot2-v2.0.1-THIRD-PARTY-LICENSES.txt` | Unsigned |
| macOS Apple Silicon + Intel | `magicspot2-v2.0.1-macos-universal.dmg` | Ad-hoc signed, not notarized |

MagicSpot supports Windows and macOS. Linux source and Nix packaging are inherited, best effort and outside maintained CI/release support. There is no MagicSpot Windows installer, Windows ARM asset, Linux install package, Flatpak release, Homebrew cask or AUR publication for this release. Windows ARM remains a test target. Inherited Spotifast packaging tools and historical release notes remain for provenance, with their publishers disabled and guarded to the upstream repository.

## Build and package

Use the pinned Rust toolchain and locked dependencies. On Windows:

```powershell
cargo build --locked --release
./packaging/magicspot/package-windows.ps1 -Binary target/release/magicspot2.exe -OutputDir dist/windows
```

The packager checks `--version`, the x64 PE header and absence of external MSVC runtime DLL imports, creates a fresh distribution folder, emits the standalone EXE and a combined app/font/icon license sidecar, and hashes both files. The app does not register URL handlers or shortcuts and does not include the portable updater marker. Updates are manual for this release.

On macOS:

```sh
rustup target add aarch64-apple-darwin x86_64-apple-darwin
cargo build --locked --release --target aarch64-apple-darwin
cargo build --locked --release --target x86_64-apple-darwin
mkdir -p dist/macos-universal
lipo -create target/aarch64-apple-darwin/release/magicspot2 target/x86_64-apple-darwin/release/magicspot2 -output dist/macos-universal/magicspot2
bash packaging/magicspot/package-macos.sh dist/macos-universal/magicspot2 dist/macos-universal
```

The packager builds `MagicSpot.app` with bundle ID `com.falleng101.magicspot2`, preserves license notices, ad-hoc signs it and creates a compressed DMG. It verifies and mounts the image read-only, checks the app's version, both architectures and signature, then unmounts it. These checks do not establish Apple notarization or an interactive Mac sign-in test.

Output locations must be fresh; do not overwrite a distribution under review. SHA-256 checksums establish consistency with the uploaded files, not independent publisher authentication.

## 2.0.1 publication gate

1. CI builds ordinary release and demo configurations on macOS and Windows, runs macOS/Windows x64/Windows ARM tests plus shared quality/docs checks, and uploads `MagicSpot-Windows-x64` and `MagicSpot-macos-universal` artifacts. Shared checks run on Ubuntu; Linux platform builds/tests, Nix packages and Linux screenshots were removed from release gates by the maintainer on October 10, 2026.
2. `.github/workflows/magicspot-release.yml` runs after CI completes. It verifies that all eight named required jobs completed successfully on the exact SHA, including Windows ARM tests. It accepts only successful push-to-main CI from this repository with Cargo version exactly `2.0.1`.
3. It checks that the CI source commit still equals current remote main and that an existing tag, if any, names that same commit. An existing release is left alone. The completed #648 scope approval and inspected Linux evidence remain in the review ledger; Linux inspection is no longer a publication gate for this Windows/macOS-only release.
4. `packaging/magicspot/prepare-release.py` verifies the Windows EXE, its license sidecar and the Mac DMG against their CI checksums; it validates the Windows PE architecture and required license notices, then creates the combined publication directory.
5. The workflow checks main again, then creates the regular GitHub release `v2.0.1`, marked Latest, at the tested commit with the written [release notes](packaging/release-notes/v2.0.1.md), Windows EXE and license sidecar, DMG and checksums.

A new push cancels older running CI; only the successful current-main run can publish. A failed job blocks publication even if both packages built. Check [Actions](https://github.com/FallenG101/MagicSpot2/actions), the repository home page Releases panel for live status. The candidate is not available until publication succeeds. Do not describe an unpublished tag or pending artifact as an available download.

The first `v2.0.0` publisher run failed after all [ten CI jobs](https://github.com/FallenG101/MagicSpot2/actions/runs/37405687141) passed: the tag check treated GitHub's 404 JSON response as an existing tag, and local package validation found a checksum-order mismatch in the verifier. Both checks are corrected in the repository. The verified EXE, license sidecar, DMG and combined checksums were published manually from that successful CI run at its tested commit. The obsolete preview release and tag were then removed. [STATUS.md](docs/magicspot/STATUS.md) records the public verification.

## Future releases

The automatic publisher is restricted to the requested `2.0.1` release. Future versions need an explicitly scoped release change: version/lockfile, relevant metainfo, written notes, package names, publication workflow and documentation. Nix packaging is best effort; independently updating it still requires its own recalculated vendor hash and Nix-host verification. Run the required checks on the release commit before publishing. Do not enable the inherited external publishers or update Spotifast's website, tap or AUR as part of a MagicSpot release.

Updates use manual downloads. The app's inherited release checker points to this fork; the standalone Windows executable has no automatic replacement setup. Document any later updater or signing changes based on the actual package configuration and [maintainer distribution decisions](docs/magicspot/RELEASE_DECISIONS.md).
