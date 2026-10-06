# MagicSpot release decisions

This file records the maintainer's distribution requirements so each release
uses the same package types and is checked in the place users actually see it.

## Current decisions

- Windows downloads are a **standalone x64 `.exe`**, not a ZIP and not an
  installer. Downloaders should be able to save and run the file directly.
- Keep the Windows app license notices in a separate text asset beside the
  executable. Include SHA-256 checksums for both.
- Keep macOS as a universal Apple Silicon and Intel `.dmg`.
- Do not add an installer, shortcuts, URL handler, app registration or automatic
  updater unless the maintainer requests that distribution behavior.
- Preview releases are intentionally prereleases. GitHub can omit them from the
  repository home page's Releases sidebar even when the release page is public.
  Check the tag's direct release URL and its asset list; use that direct URL in
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
4. Confirm the public release API or release page identifies the right tag and
   visibility, and lists the EXE, license sidecar, DMG and checksums. Confirm
   each direct asset link returns successfully without authentication.
5. Open the direct release URL and use it in user-facing download instructions.
   A repository sidebar showing tags instead of releases is not a failed or
   missing prerelease.
6. If replacing assets on an already-published version, upload and verify the
   replacement set before removing obsolete assets. Update the release notes,
   checksum file, automation and repository documentation in the same change.

Ask the maintainer only when a future request leaves a material choice open,
such as standalone executable versus installer, supported Windows architecture,
signing, or whether a stable release rather than a prerelease is intended.

## Preview 1

`v2.0.0-preview.1` follows these choices: standalone Windows x64 EXE, a separate
license-notice text file, SHA-256 checksums, and the universal Mac DMG. It is a
public prerelease, so use
<https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.0-preview.1> as the
download link.
