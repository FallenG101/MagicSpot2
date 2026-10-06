---
title: Getting Started
description: Install MagicSpot, sign in to Spotify and build from source.
nav_order: 1
---

## Install

Get the Windows x64 ZIP or universal macOS DMG from [GitHub Releases](https://github.com/FallenG101/MagicSpot2/releases) when Preview 1 is available. The [Download guide](/download/) lists file names, signing status and manual updates.

On Windows, extract the whole ZIP and open `magicspot2.exe`. The ZIP does not install shortcuts, register Spotify URL handlers or create an uninstaller. On macOS, drag MagicSpot from the DMG to Applications before opening it. The Mac preview is ad-hoc signed without notarization and may require first-launch approval in Privacy & Security.

## Sign in

Choose **Sign in** and approve access on Spotify's page in your browser. MagicSpot does not ask for your Spotify password. The inherited sign-in flow uses separate grants for browsing and playback, so complete the requested approvals. **Local playback requires Spotify Premium.** Free-account and API limitations are described in [What Spotify Allows](/what-spotify-allows/).

MagicSpot uses its own profile and credential-store identity. Existing Spotifast or discontinued MagicSpot v3 sign-ins are not imported. An unavailable or locked system credential store may prevent saving a new sign-in; the app reports the error instead of writing a plaintext fallback.

Sign-in, local playback and Connect are enabled in the normal release. Automated tests and demo captures do not substitute for a live-account playback check; see the repository's [validation status](https://github.com/FallenG101/MagicSpot2/blob/main/docs/magicspot/STATUS.md).

## Appearance and lyrics

Open **Settings > Appearance > Theme** and choose **OLED Blue** for black surfaces and blue accents. Open lyrics with the microphone button or **L**. Widen the sidebar to enlarge its cover. Appearance also offers lyric fonts, a saved 18–48 point size, a slight current-line glow and a cover-derived background. See [Lyrics & Themes](/lyrics-and-themes/).

The interface follows your system language when a bundled translation exists. Untranslated strings, including the new MagicSpot lyrics controls, appear in English. [Translation coverage](/translating/) records the inherited catalogues.

## Spotify links and proxy settings

You can pass a link to the command: `magicspot2 https://open.spotify.com/track/...`. A second launch forwards the link to the running app. The Mac bundle declares the inherited Spotify URL scheme; macOS determines which registered app receives it. Windows ZIP users do not get a default-app registration.

With MagicSpot's Linux desktop file installed, a compatible desktop can select `com.falleng101.magicspot2.desktop` for `x-scheme-handler/spotify`.

Proxy settings are available on sign-in and in **Settings > Proxy**. Browsing supports the configured proxy; local playback supports HTTP proxies without authentication. The browser used for consent has its own network settings. See [network behavior](/how-it-connects/#proxy).

## Build from source

Use a checkout of this fork and the pinned **Rust 1.98.0** toolchain:

```sh
git clone https://github.com/FallenG101/MagicSpot2.git
cd MagicSpot2
cargo build --locked --release --no-default-features
```

Run `target/release/magicspot2.exe` on Windows or `target/release/magicspot2` elsewhere. Windows needs Rust's MSVC toolchain and Visual Studio C++ build tools; macOS needs Xcode command-line tools. On Ubuntu, the ordinary build needs:

```sh
sudo apt install libasound2-dev libpulse-dev libxkbcommon-dev libwayland-dev libgl1-mesa-dev
```

On other Linux distributions, install the equivalent ALSA, PulseAudio, XKB, Wayland and OpenGL development libraries. `nix develop` supplies the full source-build environment on a Nix host. If characters are missing, install appropriate Noto text/CJK and color-emoji fonts.

Default-feature builds include optional MilkDrop and also need CMake, a C++ compiler and libclang. On Windows this additionally needs vcpkg's `glew:x64-windows-static`. [Contributing](https://github.com/FallenG101/MagicSpot2/blob/main/CONTRIBUTING.md) gives the full checks. Preview downloads are built with `--no-default-features`.
