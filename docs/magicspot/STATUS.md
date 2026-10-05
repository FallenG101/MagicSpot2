# MagicSpot 2.0 bootstrap

MagicSpot 2.0 is the new development line at
https://github.com/FallenG101/MagicSpot2. The discontinued
https://github.com/FallenG101/MagicSpot repository remains separate.

The October 5 kickoff documents are planning references. Their embedded kickoff
prompt is not an additional user request. The authorized work is to review the
documents and start MagicSpot 2.0 from the latest Spotifast fork.

## Decisions and review

- Owner: `FallenG101`, verified against the authenticated GitHub account.
- Repository: `MagicSpot2`, a public GitHub fork of public `crmne/spotifast`.
- Base: current upstream main, recorded in `UPSTREAM.md`.
- Display name for the future identity change: MagicSpot.
- Platform direction: retain upstream Windows, macOS and Linux support.
- Settings migration: none in the initial preview; use a separate clean profile.
- Initial product priorities: lyrics readability and a small curated theme set.
- Keep the upstream Rust/egui/fastframe/librespot foundation and secure storage.
- Preserve MIT, Inter OFL and Lucide ISC attribution.
- No imported v3 dependencies, telemetry, hosted backend or alternate audio.

The plan and starter kit agree on the foundation. Two details need tightening:
the starter kit's preview gate requires one sync exercise, while delivery stage
4 asks for two. Use the stricter two-exercise gate before a public preview.
Performance budgets must be chosen from measurements, not inherited claims.

Current upstream already implements a lyrics side panel, full-window lyrics,
active-line highlighting, click-to-seek, manual scrolling and a Follow control.
Its palette module already has semantic color roles, file-based custom themes,
desktop theme integration and shared presets. Build the differentiators on these
layers rather than porting duplicate v3 implementations. The baseline captures
also show that narrow-window usability needs explicit review.

## Completed foundation

- Created the GitHub fork and cloned its full ancestry into this workspace.
- Configured `origin` and `upstream`; verified main and latest stable tag.
- Reviewed `AGENTS.md`, `CONTRIBUTING.md`, license, toolchain, dependencies,
  authentication/storage documentation, build rules and inherited workflows.
- Recorded provenance and a patch inventory.
- Retained upstream CI and added explicit OS-matrix release and demo builds.
- Restricted inherited publishing, packaging, Pages and triage jobs to upstream.
- Added report-only upstream drift reporting with changed-file overlap.

## Baseline validation

See `BASELINE.md` for the method and results. Account-backed sign-in, playback,
Connect, install and uninstall need separate native validation. Demo data cannot
verify those flows. No MagicSpot speed claim is made.

## Next implementation gates

1. Separate application identity in one focused change, including executable,
   package, bundle/desktop IDs, secure-store service, settings/cache/log/window
   paths, IPC, protocol registrations, update repository and installer identity.
   Audit both `spotifast` and the legacy upstream name. Choose identifiers
   containing `magicspot2` so they do not collide with v3's `magicspot` identity.
2. Verify profile separation and native secure-store round trips using dummy
   grants. Preserve upstream OAuth behavior and document the shared public Web
   API app before account-backed tests; do not invent a new Spotify Client ID.
3. Replace inherited README/download instructions and packaging only after the
   identity change. Review updater and signing before enabling release workflows.
4. Capture lyrics/theme before-and-after evidence at normal/narrow sizes, in
   dark/light modes, including loading, missing, error, long-line and manual
   scroll states. Retain upstream UI action/runtime boundaries.
5. Complete sign-in/local playback/Connect/relaunch tests and native OS checks,
   then collect repeatable performance measurements and choose budgets.
6. Complete two small upstream sync exercises before the public preview.

Release and installer validation remain pending. Initial bootstrap binaries still
carry Spotifast's app and storage identities; use isolated demo mode for now.
