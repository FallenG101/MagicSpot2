---
title: Packaging
description: How MagicSpot 2.0.1 downloads are built and published.
nav_order: 7
---

MagicSpot 2.0.1 produces a standalone Windows x64 EXE with a license-notice sidecar and a universal macOS DMG, plus SHA-256 checksums. Both contain the normal app with upstream's default MilkDrop feature and without demo data. Windows is unsigned; macOS is ad-hoc signed without notarization. MagicSpot supports Windows and macOS; inherited Linux source and packaging are best effort without maintained builds or release support.

See the repository's [Packaging and release procedure](https://github.com/FallenG101/MagicSpot2/blob/main/PACKAGING.md) for commands, artifact names, verification and the successful-current-main CI publication gate. [Download](/download/) covers installation and manual updates.

The inherited Spotifast native packaging, Flatpak manifests and release tools remain as source/history references. Their publishing workflows are disabled for this fork; they do not indicate that MagicSpot packages exist in those channels.
