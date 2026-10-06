---
title: Download
description: MagicSpot Windows ZIP, universal macOS DMG and source builds.
nav_order: 2
---

Download from [MagicSpot GitHub Releases](https://github.com/FallenG101/MagicSpot2/releases). Preview 1 is published only after every required CI job passes and both downloads are verified. A pending build does not mean the files are available yet.

| Platform | Preview 1 asset | Installation |
| --- | --- | --- |
| Windows x64 (Intel/AMD) | `magicspot2-v2.0.0-preview.1-x86_64-pc-windows-msvc.zip` | Extract the whole ZIP, then open `magicspot2.exe` in its folder. |
| macOS Apple Silicon and Intel | `magicspot2-v2.0.0-preview.1-macos-universal.dmg` | Open the DMG and drag **MagicSpot** to **Applications**. Eject the DMG, then open the installed app. |
| Linux | Source build | See [Getting Started](/getting-started/#build-from-source). No Linux download is published for Preview 1. |

These are normal applications with Spotify sign-in, playback and Connect enabled. Local playback requires Spotify Premium. The downloads omit demo mode and MilkDrop. Windows on ARM, installers, AppImage, Flatpak, AUR and Homebrew packages are not offered for this preview.

Windows has no publisher signature. macOS uses ad-hoc signing, without Apple notarization; first launch may require approval in **System Settings > Privacy & Security**. Download only from the project's release page. `checksums.txt` provides SHA-256 integrity checks; it is not a separate publisher signature.

## Manual preview updates

Download previews manually from GitHub Releases. Quit MagicSpot, extract the replacement Windows folder or replace the Mac app in Applications, then relaunch. Preferences and credentials remain in the separate MagicSpot profile.

The inherited automatic checker points at `FallenG101/MagicSpot2` and checks stable releases. It does not advertise prereleases. The Preview 1 Windows ZIP also lacks the portable-update marker required for automatic replacement. Do not expect the green update indicator to deliver this preview.

## Nix and Cargo

From a MagicSpot checkout, `nix build .#magicspot2` builds the app; `.#default` and the inherited `.#spotifast` alias select the same package. `nix develop` supplies the development environment. The CI Nix check targets x86_64 Linux. There is no configured public MagicSpot binary cache; other architectures are not validated merely because the flake declares them.

You can install from source with:

```sh
cargo install --git https://github.com/FallenG101/MagicSpot2 --locked --no-default-features
```

Source installs follow their own update/build path. See [Packaging](https://github.com/FallenG101/MagicSpot2/blob/main/PACKAGING.md) for how downloads are produced.
