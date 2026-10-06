---
title: Download
description: MagicSpot Windows executable, universal macOS DMG and source builds.
nav_order: 2
---

The [MagicSpot 2.0 release page](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.0) lists the verified downloads. GitHub also shows it as **Latest** under Releases on the repository home page.

| Platform | 2.0.0 asset | Installation |
| --- | --- | --- |
| Windows x64 (Intel/AMD) | `magicspot2-v2.0.0-x86_64-pc-windows-msvc.exe` | Download and open the executable directly. It runs without extracting an archive or installing an app. |
| macOS Apple Silicon and Intel | `magicspot2-v2.0.0-macos-universal.dmg` | Open the DMG and drag **MagicSpot** to **Applications**. Eject the DMG, then open the installed app. |
| Linux | Source build | See [Getting Started](/getting-started/#build-from-source). No Linux download is published for 2.0.0. |

These are normal applications with Spotify sign-in, playback, Connect and MilkDrop enabled. Local playback requires Spotify Premium. The downloads omit demo mode. Windows on ARM, a Windows installer, AppImage, Flatpak, AUR and Homebrew packages are not offered for this release.

Windows has no publisher signature. macOS uses ad-hoc signing, without Apple notarization; first launch may require approval in **System Settings > Privacy & Security**. Download only from the project's release page. `checksums.txt` provides SHA-256 integrity checks; it is not a separate publisher signature.

## Manual updates

Download newer versions manually from GitHub Releases. On Windows, replace the standalone `.exe`. On macOS, replace the MagicSpot app in Applications. Preferences and credentials remain in the separate MagicSpot profile.

The inherited automatic checker points at `FallenG101/MagicSpot2`, but the standalone `.exe` is replaced manually. Do not expect the green update indicator to replace it.

## Nix and Cargo

From a MagicSpot checkout, `nix build .#magicspot2` builds the app; `.#default` and the inherited `.#spotifast` alias select the same package. `nix develop` supplies the development environment. The CI Nix check targets x86_64 Linux. There is no configured public MagicSpot binary cache; other architectures are not validated merely because the flake declares them.

You can install from source with:

```sh
cargo install --git https://github.com/FallenG101/MagicSpot2 --locked
```

Source installs follow their own update/build path. See [Packaging](https://github.com/FallenG101/MagicSpot2/blob/main/PACKAGING.md) for how downloads are produced.
