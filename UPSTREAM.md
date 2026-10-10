# Upstream provenance

- Source: https://github.com/crmne/spotifast
- Fork: https://github.com/FallenG101/MagicSpot2
- Integrated on: October 10, 2026
- Selected branch: `main`
- Base commit: `dd2d5e34e66d4e01e31e595a3022a1de808b449a`
- Base commit date: October 10, 2026
- Latest stable release at bootstrap: `v0.12.0`
- Stable release commit: `ed9cb550d1514b5e7edfcf44d58d04406a3d5c5b`
- License: MIT. Preserve `LICENSE` and upstream copyright notices.

MagicSpot bootstrapped from `7048219` on October 5, then integrated all 23
subsequent commits through the recorded snapshot using reviewed cherry-picks
and one credited README adaptation. No upstream commits are deferred. Published
history and tags remain intact, with no merge commits. The recorded snapshot
need not be an ancestor of MagicSpot HEAD. `origin` is MagicSpot2; `upstream`
is Spotifast. See the [October sync record](docs/magicspot/upstream-sync-2026-10.md).

## Foundation

- Compiler: Rust 1.98.0, pinned by `rust-toolchain.toml`.
- fastframe: all runtime and build crates pinned together to
  `dennisgr7/fastframe` revision `f7dc6fbe938e8a953509d110cdba036f537e5b7e`.
- projectm-sys: `dennisgr7/projectm-rs` revision
  `1ef6df1c20247a3a5800c625e46262330f93bbd6`.
- egui: `ba6790fe7cf46e58e8d27ce1524cbfdee745e938`.
- winit: `ed7caa9023f10b397f5b6ec8284a840cbd8a6f65`.
- librespot: `23fc42cff37848e51f0d8eaefad1a93941b71e59`.
- Supported upstream platforms: Windows, macOS, Linux.
- Maintained MagicSpot products: Windows and macOS. The maintainer removed
  Linux platform/Nix/screenshot CI gates for 2.0.1 on October 10, 2026;
  inherited Linux source and packaging are best effort.
- Local validation host: Windows; other platforms require CI/native hardware.

No dependency changes or code from discontinued MagicSpot v3 have been imported.

## Historical 2.0.0 functional parity audit

On October 5, 2026, `git ls-remote upstream refs/heads/main` still returned
`7048219716fb8bbf2f1af0934f545801f52cb29b`, which was the
upstream main commit at that time. The source diff adds the requested lyrics and
OLED theme behavior, plus MagicSpot naming, separate profile/credentials,
desktop integration names and update repository. The playback engine and
Spotify backend (`src/player.rs` and `src/backend.rs`) are unchanged. In
`src/auth.rs`, only sign-in page wording changes; in `src/http.rs`, only the
application name in the User-Agent changes. The release build uses upstream's
default feature set, including MilkDrop. Live account-backed playback and
Connect still need direct validation; this code audit does not replace it.
The regular 2.0.0 packages and platform checks passed on [CI run 37405687141](https://github.com/FallenG101/MagicSpot2/actions/runs/37405687141).

## MagicSpot patch inventory

| Patch | Files | Purpose |
| --- | --- | --- |
| Bootstrap documentation | `README.md`, `UPSTREAM.md`, `docs/magicspot/` | Record project direction, provenance, acceptance checks and actual validation |
| Publishing and triage guards | `.github/workflows/` except `ci.yml` and `upstream-drift.yml` | Keep inherited deployment, release, packaging and external triage jobs restricted to their upstream repository |
| Build validation | `.github/workflows/ci.yml` | Retain upstream checks and add release/demo compilation on each supported OS |
| Upstream drift reporting | `.github/workflows/upstream-drift.yml`, `.github/scripts/upstream-drift.py` | Report upstream movement and overlapping changes without merging, publishing or posting comments |
| Lyrics sidebar | `src/ui/lyrics.rs`, `src/model.rs`, `src/app.rs`, `src/demo.rs` | Larger stable text, song header, soft edges and action-based follow/seek behavior |
| Lyrics appearance options | `src/ui/lyrics.rs`, `src/ui/settings.rs`, `src/settings.rs`, `src/theme.rs`, `src/model.rs`, `src/app.rs`, `src/demo.rs` | Persisted font choices, subtle active-line glow, larger cover card and cached artwork background |
| Rapid lyric following | `src/lyrics.rs`, `src/ui/lyrics.rs` | Schedule both views at the next timestamp and finish transitions before rapid line changes |
| Playlist-library recovery | `src/app.rs`, `src/model.rs`, `src/ui/sidebar.rs`, `src/demo.rs`, `src/entrypoint.rs` | Retain failed page offsets and loaded rows, with a persistent manual retry and deterministic UI coverage |
| OLED | `src/theme.rs`, `src/settings.rs`, `src/app.rs`, `src/demo.rs`, `src/entrypoint.rs` | Persisted built-in black/white/gray palette and deterministic demo coverage; keeps the legacy `oled_blue` settings key |
| App identity and release | `src/identity.rs`, profile/credential/IPC/update and shell modules, Cargo metadata, macOS/Nix metadata, `packaging/magicspot/` | Separate MagicSpot 2 from both previous apps and package normal Windows/macOS downloads |
| MagicSpot publication | `.github/workflows/magicspot-release.yml`, `packaging/magicspot/prepare-release.py` | Publish authorized version 2.0.1 only after every named current-main CI job passes and both downloads verify |

The untouched application baseline is commit `225a65c`. The lyrics/OLED patch is
isolated in `e252ee0`; fonts/glow/artwork follow in `ef38ed2`, size/growing cover in `748b804`, and identity/packaging in `f140497`. Publication gates are in `4e3da02`. The first release
uses its own application/profile/secure-store/update identity. The inherited
Spotifast installer and external publishers remain unused.

## Maintainer direction

The maintainer's October 5 direction is to keep this a small lyrics/theme fork
and stay current with Spotifast. The intended destination for generally useful
UI improvements is upstream Spotifast, subject to its maintainer's acceptance.
Keep UI patches independent of MagicSpot branding, packaging and release files.
Do not expand into feature parity with discontinued v3 or fork shared runtime
dependencies without a demonstrated blocker. No upstream proposal or PR has
been submitted in this session.

## Sync procedure

Fetch `upstream` and review its release notes and diff from the recorded base.
Integrate small batches on `main` without rewriting published history. Follow
the linear-history policy in `AGENTS.md`. Update this file's base and patch
inventory with each integration, run the upstream checks, and record elapsed
effort, conflicts and regressions in `docs/magicspot/STATUS.md`.

The drift workflow measures pending commits from the reviewed upstream snapshot
to upstream/main and compares changed paths. It does not use fork graph
ahead/behind counts or require the snapshot to be an ancestor of HEAD.
Temporary-repository regressions cover cherry-picked history, new upstream
changes and rewritten upstream history. The drift workflow is report-only. A report is not permission to merge, tag,
publish, migrate a profile or send public messages.

See [MAINTENANCE.md](docs/magicspot/MAINTENANCE.md) for the bounded sync procedure and documentation/release boundaries. Active fork docs are indexed in [docs/README.md](docs/README.md); retained v0.x notes and old review captures are historical upstream records.
