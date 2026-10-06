# MagicSpot 2.0 status

MagicSpot 2 is the new development line at https://github.com/FallenG101/MagicSpot2. The discontinued https://github.com/FallenG101/MagicSpot repository remains separate.

The October 5 kickoff documents are planning references. Their embedded prompt is not an additional request. The maintainer subsequently requested the improved lyrics sidebar, OLED Blue, a usable GitHub release and a macOS DMG. Those direct requests set the current scope.

## Release check, October 5, 2026

There is no public MagicSpot release at this check. [CI run 37391265335](https://github.com/FallenG101/MagicSpot2/actions/runs/37391265335), on `4e3da02`, completed with eight passing jobs and two failures. Normal release/demo builds passed on all three operating systems; quality, docs, Nix, Windows tests and macOS tests passed. The Windows ZIP was produced. Both Mac architectures compiled, but the DMG was not produced.

Linux's unavailable-display regression failed because the renamed command's startup INFO log was excluded by the old default filter. The universal DMG packager passed its binary path after `lipo -verify_arch`, where lipo treated it as another architecture. Commit `83b289f` corrects the log filters and both lipo calls. The existing regression and package verification remain in place; these platform-specific fixes still require the replacement CI run.

The Windows release/demo test suite passed again locally after the log fix. Documentation checks validated nine YAML files, 17 page front matters, 82 local links, settings names and issue-form identities. The Jekyll site build runs in CI; no local Ruby build is claimed. Active guides, policy, issue forms, site metadata and in-app help links now describe the fork; historical upstream evidence remains labeled.

The fixes and docs are pushed as a new current-main candidate. GitHub will run the required builds and publish Preview 1 automatically only after they all pass. At the maintainer's request, those builds are left running without waiting for completion. Check [Actions](https://github.com/FallenG101/MagicSpot2/actions) and [Releases](https://github.com/FallenG101/MagicSpot2/releases) for the live state; this is a dated snapshot, not an assertion that later CI passed.

## Direction

Maintain the small lyrics/theme improvements and keep current with Spotifast. Aim to contribute suitable UI improvements upstream, with the maintainer's explicit instruction before submitting. Keep runtime and Spotify behavior close to upstream, and isolate UI work from MagicSpot identity and packaging changes. No discontinued-v3 dependencies, telemetry or alternative audio sources are added.

## Completed development work

- Forked latest Spotifast main, preserved history and recorded the stable reference, compiler and fastframe/egui/winit/librespot revisions.
- Built and tested the untouched Windows baseline; captured native UI evidence.
- Retained upstream CI, added normal release/demo builds on all three targets, and restricted inherited publishing/packaging/triage to its original owner.
- Added report-only upstream drift reporting, including changed-file overlap.
- Implemented the lyrics/OLED pass in its own commit, `e252ee0`.
- Added the requested font options, subtle active-line glow, larger song card and
  artwork-derived sidebar background as a separate UI adjustment.
- Added a saved 18–48 point lyric size with Auto mode, and a cover that grows as
  the sidebar is widened.
- Separated executable, profile, secure-store, window state, IPC, tray, media, Connect name and updater identities. See `IDENTITY.md`.
- Prepared `2.0.0-preview.1`: normal Windows x64 ZIP and universal macOS DMG, both without demo data or MilkDrop. Retained all license notices.

## Validation

The Windows release/demo suite passed 974 tests with one ignored native-store round trip; that exact dummy-grant native-store test passed separately. Strict clippy passed. Packaging regression suites passed four tests each. Native Windows captures cover light, dark and OLED Blue, normal/narrow windows, lyrics states and appearance options. See `UI_NOTES.md` and the historical `BASELINE.md`.

The normal release build and release-commit CI/package verification are the final publication checks. At the maintainer's request, GitHub is left to complete those builds. The Preview 1 publication workflow requires successful CI on the current main commit, verifies both CI download checksums, and publishes that commit with the written notes. It authorizes only `2.0.0-preview.1`, not future releases. macOS runs on GitHub's native runner; the DMG check mounts the image and verifies bundle identity, version, signature and both architectures. No local macOS or Linux interactive session is claimed.

Live Spotify sign-in, local playback, Connect and relaunch have not been exercised with an account in this session. The inherited flows are enabled and unchanged; demo coverage does not establish live-account behavior. The Windows binary has no publisher signature; macOS uses ad-hoc signing without notarization.

## Future validation and maintenance

Native account-backed checks, measured performance budgets, Linux install packaging, Apple notarization and upstream sync exercises remain follow-up work. The kickoff's proposed two-sync/cross-platform-preview roadmap is not represented as completed. No speed or memory improvement is claimed. The report-only drift workflow does not merge, publish or submit upstream changes automatically.
