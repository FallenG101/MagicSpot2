> Historical untouched Spotifast baseline at `225a65c`. Commands and app identity below reproduce that baseline, not the current MagicSpot build. Current builds use `magicspot2`; see [STATUS.md](STATUS.md).

# Untouched upstream baseline

Base: `7048219716fb8bbf2f1af0934f545801f52cb29b`.
Date: October 5, 2026. Platform: Windows, MSVC.
Toolchain: Rust 1.98.0. Dependency resolution: existing `Cargo.lock`, `--locked`.

## Reproduce

```powershell
cargo build --locked --release --no-default-features --features demo
./target/release/spotifast.exe --demo --demo-show lyrics --demo-size 1280x800 --demo-shot .cache/baseline/lyrics-dark.png
./target/release/spotifast.exe --demo --demo-show lyrics,light --demo-size 1280x800 --demo-shot .cache/baseline/lyrics-light.png
./target/release/spotifast.exe --demo --demo-show lyrics --demo-size 760x800 --demo-shot .cache/baseline/lyrics-narrow.png
```

The source is unchanged for this capture. MilkDrop is omitted because this
configuration isolates the initial app/UI build from its CMake/libclang/GLEW
tooling. It is not evidence for a default-feature build. Full-feature upstream
CI remains enabled. Demo mode skips credential restoration, uses its own data
directory and does not perform Spotify playback. Demo artwork may be fetched.

## Results

- Release/demo build passed, source unchanged. Cold build: 4m 05s. Build duration
  is a development measurement, not app startup latency.
- Executable: 28,580,352 bytes. SHA-256:
  `500da44fb792bef04ff14317bb4f6f778b3f9515725b57ea2ae89bcf4d6a9932`.
- Native launch and automatic PNG capture passed for dark/light at 1280x800 and
  dark at 760x800. Local evidence is retained in `.cache/baseline/` for subsequent
  comparisons. Each capture process exited successfully.
- Visual review: active lines and wrapping render in both themes. The narrow
  baseline compresses the home content and crowds the top bar. The lyrics panel
  clips preceding text at its scrolling edge. These observations are starting
  evidence, not fixes or a complete interaction review.
- `cargo fmt --all --check` passed.
- `cargo clippy --locked --release --no-default-features --features demo --all-targets -- -D warnings`
  passed with no warnings.
- `cargo test --locked --release --no-default-features --features demo --all-targets`
  passed: 961 tests, 0 failures, 1 ignored native credential-store round trip.
  Test compilation took 5m 14s. Linux-only integration tests did not execute on
  Windows. This result does not cover MilkDrop/default-feature builds.
- Release-name packaging regressions: 4 passed.
- Flatpak metainfo regressions: 4 passed.
- Linux launcher packaging tests could not run on this Windows host: Unix
  commands/Ruby were unavailable. Retained in Linux CI.
- All workflow syntax passed actionlint 1.7.12. Shellcheck and pyflakes were not
  installed; those optional integrations were disabled for this validation.
- Drift-report fixture passed: unchanged upstream, divergent tips, overlapping
  paths, invalid base rejection, and verification that no Git state was mutated.

Native Spotify and installer checks have not been performed. No performance
measurements have yet been accepted as a release baseline.
Default/all-feature MilkDrop builds, Rustdoc/doc tests, Nix, the documentation
site build and other OS targets remain CI checks. Their local toolchains are
unavailable or outside this baseline configuration; no passing result is claimed.

## Machine

- Windows 11 Pro, 64-bit, version 10.0.26300.
- AMD Ryzen 7 7800X3D, 8 cores / 16 logical processors.
- RAM: 33,455,931,392 bytes (approximately 31.2 GiB visible to the OS).
- Graphics reported by Windows: NVIDIA GeForce RTX 4070 SUPER, AMD Radeon
  Graphics, and Virtual Desktop Monitor. The render adapter/display scale was
  not independently measured, so these captures are not a timing comparison.

## Performance method for the identity milestone

Record OS version, CPU, RAM, GPU, display scale, active theme, window size,
feature flags, compiler, SHA and executable size. Compare release builds with
the same features and settings. Use separate profiles and identical warm-cache
conditions, record five runs, and report median and range.

| Measure | Method | Current evidence |
| --- | --- | --- |
| Launch | Process start to first usable painted frame; cold/warm separately | Pending |
| Navigation | Fixed library/search/lyrics interaction sequence | Pending |
| Paused idle CPU | 60-second steady interval after settling; separate visible/hidden states | Pending |
| Memory | Private working set after settling in the same view | Pending |
| Playback start | User command to audible Spotify output on the same device/network | Pending native account test |
| Track skip | User command to next audible track; record cache/network conditions | Pending native account test |

A screenshot delay is not launch latency. Demo playback does not measure real
audio-device idling, playback start or track skips.
