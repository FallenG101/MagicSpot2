# MagicSpot release decisions

This file records the maintainer's distribution requirements so each release
uses the same package types and is checked in the place users actually see it.

## Current decisions

- Windows downloads are a **standalone x64 `.exe`**, not a ZIP and not an
  installer. Downloaders should be able to save and run the file directly.
- Keep the Windows app license notices in a separate text asset beside the
  executable. Include SHA-256 checksums for both.
- Keep macOS as a universal Apple Silicon and Intel `.dmg`.
- Maintain Windows and macOS. Windows ARM remains a test target without a
  download; inherited Linux source/Nix packaging are best effort without
  maintained builds or release support (October 10, 2026 decision).
- Build the normal app with Spotifast's default features, including MilkDrop.
  Demo data is excluded. Include projectM's LGPL notice with both packages.
- Do not add an installer, shortcuts, URL handler, app registration or automatic
  updater unless the maintainer requests that distribution behavior.
- The current release version is **2.0.1**, with no preview suffix in the tag, app
  version, title or download filenames. Publish it as a regular GitHub release
  marked **Latest** so it appears in the repository home page's Releases panel.
  Check both that panel and the direct release URL; use the direct URL in
  README and download guidance.
- Keep the release notes, workflow artifact globs, checksum manifest, package
  scripts, documentation and actual GitHub assets in agreement. Never claim a
  release is available based on a tag, CI run or local artifact alone.

## Release verification checklist

Before calling a release published:

1. Confirm the successful CI run tested the exact source commit used by the
   release and inspect each required job result.
2. Confirm the Windows item is a runnable x64 PE executable named with the
   version and target. Check `--version`, the PE architecture, sidecar license
   notices and the SHA-256 entries. Confirm no `.zip` is attached.
3. Confirm the Mac universal DMG and its existing platform checks.
4. Confirm the public release API identifies the right tag with `draft: false`,
   `prerelease: false` and Latest status, and lists the EXE, license sidecar,
   DMG and checksums. Confirm each direct asset link works without authentication.
5. Open the repository home page without authentication. Its Releases panel
   must show MagicSpot 2.0.1 with a link to the release. Open that direct release URL
   as well and use it in user-facing download instructions.
6. Once the regular release is verified, remove any superseded preview release
   and tag so the project has one clear public download.
7. If replacing assets on an already-published version, upload and verify the
   replacement set before removing obsolete assets. Update the release notes,
   checksum file, automation and repository documentation in the same change.

Ask the maintainer only when a future request leaves a material choice open,
such as standalone executable versus installer, supported Windows architecture,
signing, or whether another version should have a different GitHub release type.

The first release is [MagicSpot 2.0](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.0), which was marked Latest when published. The current release is [MagicSpot 2.0.1](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.1), with the same package types.
