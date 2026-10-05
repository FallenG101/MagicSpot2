# Upstream provenance

- Source: https://github.com/crmne/spotifast
- Fork: https://github.com/FallenG101/MagicSpot2
- Integrated on: October 5, 2026
- Selected branch: `main`
- Base commit: `7048219716fb8bbf2f1af0934f545801f52cb29b`
- Base commit date: October 4, 2026
- Latest stable release at bootstrap: `v0.12.0`
- Stable release commit: `ed9cb550d1514b5e7edfcf44d58d04406a3d5c5b`
- License: MIT. Preserve `LICENSE` and upstream copyright notices.

Current main was selected because the requested starting point is the latest
Spotifast. The stable release remains a comparison reference. Git ancestry and
tags are preserved. `origin` is MagicSpot2; `upstream` is Spotifast.

## Foundation

- Compiler: Rust 1.98.0, pinned by `rust-toolchain.toml`.
- fastframe: tag `v0.4.1`, locked at
  `23d87e048185ef317f272e2a67416f516b2f2b04`.
- egui: `ba6790fe7cf46e58e8d27ce1524cbfdee745e938`.
- winit: `ed7caa9023f10b397f5b6ec8284a840cbd8a6f65`.
- librespot: `23fc42cff37848e51f0d8eaefad1a93941b71e59`.
- Supported upstream platforms: Windows, macOS, Linux.
- Local validation host: Windows; other platforms require CI/native hardware.

No dependency changes or code from discontinued MagicSpot v3 have been imported.

## MagicSpot patch inventory

| Patch | Files | Purpose |
| --- | --- | --- |
| Bootstrap documentation | `README.md`, `UPSTREAM.md`, `docs/magicspot/` | Record project direction, provenance, acceptance checks and actual validation |
| Publishing and triage guards | `.github/workflows/` except `ci.yml` and `upstream-drift.yml` | Keep inherited deployment, release, packaging and external triage jobs restricted to their upstream repository |
| Build validation | `.github/workflows/ci.yml` | Retain upstream checks and add release/demo compilation on each supported OS |
| Upstream drift reporting | `.github/workflows/upstream-drift.yml`, `.github/scripts/upstream-drift.py` | Report upstream movement and overlapping changes without merging, publishing or posting comments |
| Lyrics sidebar | `src/ui/lyrics.rs`, `src/model.rs`, `src/app.rs`, `src/demo.rs` | Larger stable text, song header, soft edges and action-based follow/seek behavior |
| OLED Blue | `src/theme.rs`, `src/settings.rs`, `src/app.rs`, `src/demo.rs`, `src/entrypoint.rs` | Persisted built-in black/blue palette and deterministic demo coverage |

The untouched application baseline is commit `225a65c`. UI work follows that
baseline; application identities remain inherited. Do not install development
builds alongside Spotifast or v3 using
the inherited packaging. See `docs/magicspot/STATUS.md` for the identity gate.

## Sync procedure

Fetch `upstream` and review its release notes and diff from the recorded base.
Integrate small batches on `main` without rewriting published history. Follow
the linear-history policy in `AGENTS.md`. Update this file's base and patch
inventory with each integration, run the upstream checks, and record elapsed
effort, conflicts and regressions in `docs/magicspot/STATUS.md`.

The drift workflow is report-only. A report is not permission to merge, tag,
publish, migrate a profile or send public messages.
