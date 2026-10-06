---
title: Privacy
description: MagicSpot storage, network requests and optional services.
nav_order: 4
---

MagicSpot runs on your computer with no MagicSpot account, hosted backend, app telemetry or analytics. It retains the upstream Spotify connections and adds local lyrics appearance settings.

## Local storage

Spotify grants and optional proxy passwords use Credential Manager on Windows, Keychain on macOS or Secret Service on Linux, under `com.falleng101.magicspot2`. You authorize on Spotify's browser page; MagicSpot does not handle your Spotify password. A locked or unavailable store is reported, with no plaintext fallback for new grants.

Settings, skins and themes live in the configuration folder. Session data, window state, recent plays and logs live in the state folder. Audio, artwork, lyrics and library metadata live in the cache folder. See [Settings & Files](/settings-and-files/) for exact paths. The new profile does not import Spotifast or discontinued MagicSpot v3 files.

The app keeps `magicspot2.log` and, after a panic, `panic.log` locally. Credentials must not be logged. Logs may contain track or system details; review them before attaching them to an issue. **Sign out** removes saved Spotify grants; failed deletion leaves revocation markers to prevent restoring them.

## Network requests

| Service | Purpose |
| --- | --- |
| Spotify | Browser authorization, catalogue, account, library, playlist, audio and Connect requests. |
| LRCLIB | Lyrics fallback when Spotify has none; sends artist, title, album and duration, without an account identifier. |
| GitHub | Checks this fork's release feed, and downloads an update if requested. Automatic checks can be disabled in Settings. Replacing the standalone Windows executable is manual. |
| Local network | mDNS receiver discovery and communication with selected Spotify Connect receivers. |

MilkDrop downloads preset packs from GitHub when used. Links such as Spotify developer setup or the Winamp Skin Museum open in your browser. Each service has its own privacy terms; see [Spotify's policy](https://www.spotify.com/legal/privacy-policy/).

Artwork-derived lyrics backgrounds reuse the existing cover loader, blur and cache. Font, size, glow and theme settings require no new service.

## Documentation site

The fork removes the inherited Spotifast domain and analytics script. No MagicSpot hosted documentation site is configured. Reading the Markdown on GitHub uses GitHub's service; a local Jekyll preview includes no project analytics.

Questions and bug reports belong on [MagicSpot GitHub Issues](https://github.com/FallenG101/MagicSpot2/issues).
