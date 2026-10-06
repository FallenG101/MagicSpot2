---
title: What is MagicSpot?
description: A native Spotify client with improved lyrics and OLED Blue.
nav_order: 0
---

MagicSpot 2 is a native Spotify desktop app with an Apple Music-inspired lyrics sidebar and an OLED Blue theme. It is a focused fork of [Spotifast](https://github.com/crmne/spotifast) by Carmine Paolino and contributors.

The October 5 foundation is upstream main commit `7048219`, five commits newer than stable `v0.12.0`. It includes that release and the subsequent upstream fixes and additions. It is not built from discontinued MagicSpot v3.

## What changes

The sidebar uses spacious bold lyrics, smooth following, a subtle active-line glow and blurred cover colors. Choose Inter, System or Monospace, use Auto size or 18–48 points, and widen the sidebar to grow the cover. **OLED Blue** adds black main surfaces and blue accents. See [Lyrics & Themes](/lyrics-and-themes/).

Spotify sign-in, local playback, library, search, playlists, queue, Connect, the Winamp mini player, full-screen lyrics and MilkDrop retain the upstream foundation. MilkDrop is included in the 2.0.0 downloads.

## Requirements and limits

Local playback requires Spotify Premium. Spotify and librespot determine which account and playback features are available; see [What Spotify Allows](/what-spotify-allows/). MagicSpot is independent and not affiliated with Spotify.

Version 2.0.0 targets Windows x64 and a universal Mac app. Linux remains a source/CI target. Windows is unsigned and macOS is ad-hoc signed without notarization. Live account-backed validation is still a follow-up; no MagicSpot startup-time or memory improvement is claimed.

The project aims to maintain a small upstream-compatible patch set and eventually offer suitable UI improvements to Spotifast. Release availability, provenance and validation are recorded in the [project documentation](https://github.com/FallenG101/MagicSpot2/blob/main/docs/README.md).
