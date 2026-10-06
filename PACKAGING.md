# MagicSpot packaging and releases

Preview 1 (`2.0.0-preview.1`) packages the normal app with real Spotify sign-in and playback enabled, without demo mode or MilkDrop. It produces two assets and a combined `checksums.txt`:

| Target | Asset | Signing |
| --- | --- | --- |
| Windows x64 | `magicspot2-v2.0.0-preview.1-x86_64-pc-windows-msvc.zip` | Unsigned |
| macOS Apple Silicon + Intel | `magicspot2-v2.0.0-preview.1-macos-universal.dmg` | Ad-hoc signed, not notarized |

Linux and Nix remain source/CI targets. There is no MagicSpot Windows installer, Windows ARM asset, Linux install package, Flatpak release, Homebrew cask or AUR publication for this preview. Inherited Spotifast packaging tools and historical release notes remain for provenance, with their publishers disabled and guarded to the upstream repository.

## Build and package

Use the pinned Rust toolchain and locked dependencies. On Windows:

```powershell
cargo build --locked --release --no-default-features
./packaging/magicspot/package-windows.ps1 -Binary target/release/magicspot2.exe -OutputDir dist/windows
```

The packager checks `--version`, creates a fresh distribution folder, includes README and the app/font/icon licenses, writes the ZIP, and hashes it. The ZIP contains a folder with `magicspot2.exe`; it does not register URL handlers or shortcuts and does not include the portable updater marker. Updates are manual for this preview.

On macOS:

```sh
rustup target add aarch64-apple-darwin x86_64-apple-darwin
cargo build --locked --release --no-default-features --target aarch64-apple-darwin
cargo build --locked --release --no-default-features --target x86_64-apple-darwin
mkdir -p dist/macos-universal
lipo -create target/aarch64-apple-darwin/release/magicspot2 target/x86_64-apple-darwin/release/magicspot2 -output dist/macos-universal/magicspot2
bash packaging/magicspot/package-macos.sh dist/macos-universal/magicspot2 dist/macos-universal
```

The packager builds `MagicSpot.app` with bundle ID `com.falleng101.magicspot2`, preserves license notices, ad-hoc signs it and creates a compressed DMG. It verifies and mounts the image read-only, checks the app's version, both architectures and signature, then unmounts it. These checks do not establish Apple notarization or an interactive Mac sign-in test.

Output locations must be fresh; do not overwrite a distribution under review. SHA-256 checksums establish consistency with the uploaded files, not independent publisher authentication.

## Preview 1 publication gate

1. CI builds ordinary release and demo configurations on Linux, macOS and Windows, runs quality/tests/docs/Nix checks, and uploads `MagicSpot-Windows-x64` and `MagicSpot-macos-universal` artifacts.
2. `.github/workflows/magicspot-preview.yml` runs after CI completes. It accepts only successful push-to-main CI from this repository with Cargo version exactly `2.0.0-preview.1`.
3. It checks that the CI source commit still equals current remote main and that an existing tag, if any, names that same commit. An existing release is left alone.
4. `packaging/magicspot/prepare-preview.py` verifies both expected assets against their one-entry checksum files, validates the ZIP and executable path, and creates the combined publication directory.
5. The workflow checks main again, then creates the prerelease `v2.0.0-preview.1` at the tested commit with the written [release notes](packaging/release-notes/v2.0.0-preview.1.md), ZIP, DMG and checksums.

A new push cancels older running CI; only the successful current-main run can publish. A failed job blocks publication even if both packages built. Check [Actions](https://github.com/FallenG101/MagicSpot2/actions) and [Releases](https://github.com/FallenG101/MagicSpot2/releases) for live status. Do not describe an unpublished tag or pending artifact as an available download.

## Future releases

The automatic publisher is restricted to the requested first preview. Future versions need an explicitly scoped release change: version/lockfile, Nix vendor hash, relevant metainfo, written notes, package names, publication workflow and documentation. Run the required checks on that commit before publishing. Do not enable the inherited external publishers or update Spotifast's website, tap or AUR as part of a MagicSpot release.

Preview updates use manual downloads. The app's inherited stable-release checker points to this fork and excludes prereleases. Document any later updater or signing changes based on the actual package configuration.
