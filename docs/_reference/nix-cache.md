---
title: Nix Source Builds (Best Effort)
description: Inherited Nix packaging outside MagicSpot's maintained release support.
---

MagicSpot maintains Windows and macOS downloads. Inherited Nix packaging is
best effort, without a maintained Linux build or public MagicSpot binary cache.
The maintainer removed the Linux/Nix jobs from release CI on October 10, 2026.
The earlier successful 2.0.1 Nix build remains in the
[October validation record](https://github.com/FallenG101/MagicSpot2/blob/main/docs/magicspot/upstream-sync-2026-10.md).

## Inherited source recipe

From a checkout, `nix build .#magicspot2` selects the inherited package;
`.#default` and `.#spotifast` are aliases. `nix develop` supplies a source-build
environment. Declared flake architectures do not establish validation.

Anyone updating this packaging should recalculate the vendor hash after a
lockfile or package-version change and verify it on a Nix host. That work is
separate from MagicSpot's Windows/macOS release gates.

There is no MagicSpot Nix publisher to enable with repository variables or
secrets. Actual supported downloads are listed on [GitHub Releases](https://github.com/FallenG101/MagicSpot2/releases/latest).
