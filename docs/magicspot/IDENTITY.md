# MagicSpot 2 identity and first release

The maintainer requested a usable GitHub release on October 5, 2026, including
normal Spotify sign-in and playback. Version `2.0.0-preview.1` is the new line,
separate from Spotifast 0.12 and discontinued MagicSpot v3.

| Surface | Identity |
| --- | --- |
| Product and default Connect device | MagicSpot |
| Cargo package and desktop command | `magicspot2` |
| Internal Rust library | `spotifast`, retained for upstream integration |
| Secure-store service and macOS bundle | `com.falleng101.magicspot2` |
| Single-instance channel and window persistence | `magicspot2` |
| Conventional profile directories | `ProjectDirs::from("com", "FallenG101", "magicspot2")` |
| Log | `magicspot2.log`, inside the separate state directory |
| GitHub updates | `FallenG101/MagicSpot2` |
| Windows download | `magicspot2-vVERSION-x86_64-pc-windows-msvc.zip` |
| macOS download | `magicspot2-vVERSION-macos-universal.dmg` |

No previous settings, cache, credential or window-state files are imported.
The profile-directory regression compares both previous app namespaces without
writing either. The native credential regression uses disposable dummy grants.

The Windows ZIP needs extraction and a launch of `magicspot2.exe`; it does not
register URL handlers, install shortcuts, change default apps or create an
uninstaller. Delete the extracted folder to remove the executable. Preferences
remain in its separate profile. The inherited Spotifast installer and packaging
publishers are not used. Their original files remain for upstream provenance.
Source macOS bundle metadata and Nix desktop packaging use the new identity.
The macOS DMG contains a universal MagicSpot.app with its own bundle identity.
It is ad-hoc signed, with a verified signature and both architectures, but has
no Apple notarization. The DMG is mounted and its app/version checked in CI.
Nix and Linux remain source/CI targets without install downloads in this release.

## Spotify and privacy

Web API and librespot client IDs, OAuth loopback redirects, permissions, token
verification, playback, Connect and API routing retain upstream behavior. The
public shared Web API app is shared with other clients and subject to Spotify's
quota; the optional personal-app flow remains available. New grants are stored
in the operating system's secure store under MagicSpot 2's service and profile
key. No Spotify password is handled by MagicSpot.

The app uses Spotify for catalogue, account and audio requests. Artwork and audio
are cached within the configured budget. Lyrics may use LRCLIB, including artist,
title, album and duration. Automatic update checks use this fork's GitHub releases
and can be disabled in Settings. Downloads use the matching asset and SHA-256
from `checksums.txt`; unsigned downloads are not publisher-authenticated. No
telemetry or hosted MagicSpot backend is added.

## Release scope

The Windows x64 and universal macOS executables are release builds without the demo feature or
MilkDrop. It supports normal sign-in and playback; local playback requires
Spotify Premium. The inherited engine is not changed by this release. A live
account sign-in/playback/Connect session and install packages on other operating
systems have not been validated locally. macOS packaging is built and verified
on GitHub's macOS runner. No performance improvement is claimed.

The kickoff documents remain a roadmap. Their proposed cross-platform packaging,
performance and sync-exercise milestones are recorded as future work, rather
than represented as completed checks for this first preview.
