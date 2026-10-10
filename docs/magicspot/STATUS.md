# MagicSpot status

## Published 2.0.1

[MagicSpot 2.0.1](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.1)
is public, regular and Latest. Its tag identifies
`d3fc2b9fa977ee7539b01783b26ce51a23e9a953`, which was current main when all
eight jobs in [CI 38087545774](https://github.com/FallenG101/MagicSpot2/actions/runs/38087545774)
passed. [Publisher 38090033352](https://github.com/FallenG101/MagicSpot2/actions/runs/38090033352)
then published the verified Windows x64 EXE, license notices, universal Mac DMG
and combined checksums. Anonymous downloads of all four files returned HTTP
200 and matched the exact-candidate SHA-256 values. The EXE reports 2.0.1, is
x64 and imports no external MSVC runtime; Mac CI verified both architectures,
version, mounted DMG and ad-hoc signature. Windows is unsigned and macOS is
not notarized. [Public verification metadata](release-verification-2.0.1.json)
records the tag, jobs and asset hashes. An isolated anonymous Chromium session
confirmed the repository's visible Releases panel says “MagicSpot 2.0.1” and
“Latest”, and About points to this fork's Releases page. Its capture was inspected.

All 23 upstream commits through `dd2d5e3` and the local OLED, rapid-lyrics and
playlist-retry improvements are included. Sixteen Windows and 56 Linux
captures were inspected. The [comparison index](upstream-review/index.html)
and [scope ledger](TRIAGE.md) record visual evidence and approval separately
from automated gates. On October 10 the maintainer made 2.0.1 Windows/macOS
only and removed Linux platform/Nix/screenshot jobs from the final gates.
The completed Linux review and successful Nix build with MagicSpot's own
recalculated hash remain historical validation. Linux source and packaging
are best effort. See the [October sync record](upstream-sync-2026-10.md).
Live Spotify sign-in, playback and Connect have not been exercised; automated
tests and demo captures do not establish live-account behavior.

## Published 2.0.0 history

The regular [MagicSpot 2.0 release](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.0) was published as **Latest**. It is retained as release history; 2.0.1 is now Latest. It offers a standalone Windows x64 EXE, a universal Apple Silicon and Intel DMG, third-party license notices and SHA-256 checksums. There is no ZIP or preview release. Windows is unsigned; the Mac app is ad-hoc signed without notarization. Linux was a source and CI target at that release.

### Source and scope at 2.0.0

MagicSpot starts from Spotifast main `7048219`, which was still upstream's main commit at the [functional parity audit](../../UPSTREAM.md). The changes are the lyrics sidebar, saved font/size and glow controls, artwork-derived background and growing cover, OLED Blue, and the fork's separate identity and packaging. The playback engine and Spotify backend source are unchanged. Both downloads include upstream's default MilkDrop feature and exclude demo data.

### Validation at 2.0.0

[CI run 37405687141](https://github.com/FallenG101/MagicSpot2/actions/runs/37405687141) passed all ten jobs on release commit `84de29c97ddf366c29813608674bfad3f4758bd4`: normal and demo builds, platform tests, quality, docs, Nix and Mac DMG packaging. The Windows EXE reports `magicspot2 2.0.0`; its x64 PE header, license sidecar and package SHA-256 values were checked. The Mac workflow verified both architectures, version, mounted DMG and app signature. At publication, GitHub's public API reported `draft: false`, `prerelease: false` and `v2.0.0` as Latest; the repository's visible Releases panel shows MagicSpot 2.0, and anonymous requests to the release page and both downloads returned HTTP 200.

The automatic publisher initially rejected a nonexistent `v2.0.0` tag because its 404 handling read GitHub's JSON error body as a tag SHA. After all CI jobs passed, the same CI artifacts were independently verified and published at that tested commit. The tag check and checksum-order comparison were fixed in the publication code afterward. The superseded preview release and tag were removed only after the regular release was verified.

Live Spotify account sign-in, playback and Connect have **not** been exercised in this development session. Their inherited flows remain enabled; automated tests and source comparison do not replace an account-backed test. No startup or memory improvement is claimed.

## Changes included in 2.0.1

### OLED palette update (included in 2.0.1)

The October 6, 2026 source update renames OLED Blue to **OLED** and replaces
blue accents and tinted controls with white and neutral gray. Black primary
surfaces, artwork colors, layout and the legacy `oled_blue` saved preference
remain compatible. This update is separate from the published 2.0.0 downloads.
The maintainer directly requested this visual scope. The
[native Windows comparison](oled-review/index.html) covers OLED at two window
sizes, unchanged Light views and Appearance controls.

### Lyric timing and playlist recovery (included in 2.0.1)

Rapid lyric lines now shorten their scroll and highlight transitions, and the
sidebar wakes at the next timestamp. A failed playlist-library page keeps its
loaded rows and offers Retry at the failed offset. The
[validation notes and native Windows comparison](bugfix-review/README.md)
record 960 passing library tests and the other passing targets with MilkDrop
disabled. Those initial checks omitted MilkDrop because vcpkg was missing. The 2.0.1
maintenance run resolved vcpkg and libclang and passed full-feature Windows
checks; shared CI supplies the launcher and docs checks. Live Spotify validation
remains outstanding. Native Linux rendering and macOS platform CI are recorded
in the October sync; interactive macOS account testing has not been performed.
These fixes are not included
in the published 2.0.0 downloads.

The [release decisions](RELEASE_DECISIONS.md) record the required package types and public checks. [PACKAGING.md](../../PACKAGING.md) gives the build and publication procedure. The [upstream sync guide](MAINTENANCE.md) keeps future lyric and theme changes separate from fork identity. The drift workflow reports upstream changes without merging or publishing them.
