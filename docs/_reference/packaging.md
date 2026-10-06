---
title: Packaging
description: How MagicSpot Preview 1 downloads are built and published.
nav_order: 7
---

Preview 1 produces a Windows x64 ZIP and a universal macOS DMG, plus SHA-256 checksums. Both contain the normal app without demo data or MilkDrop. Windows is unsigned; macOS is ad-hoc signed without notarization. Linux remains a source/CI target.

See the repository's [Packaging and release procedure](https://github.com/FallenG101/MagicSpot2/blob/main/PACKAGING.md) for commands, artifact names, verification and the successful-current-main CI publication gate. [Download](/download/) covers installation and manual preview updates.

The inherited Spotifast native packaging, Flatpak manifests and release tools remain as source/history references. Their publishing workflows are disabled for this fork; they do not indicate that MagicSpot packages exist in those channels.
