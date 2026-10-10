# Lyric timing and playlist recovery (unreleased)

The sidebar now requests a frame at the next lyric timestamp, as the full-screen
view already did. Both views shorten scroll and highlight transitions when the
next line is near. A headless egui regression follows lines 120 ms apart at both
views' normal scroll positions. Timestamp tests cover duplicate times, exact
boundaries, backward seeks, the last line and plain lyrics.

A failed playlist continuation retains its offset and the rows already loaded.
The Library shows the error and Retry in both list and grid views. Retry resumes
that page, preserves the generation, and continues sequential paging on success.
The first-page Retry starts a fresh generation. Requests keep the existing Web
API routing, bounded retry policy and cooldown. There is no new polling loop.
State tests cover repeated failures, duplicate actions and stale first-page
responses; a UI test clicks Retry in initial, partial and grid failures.

[Open the native Windows comparison](index.html). It covers Dark and Light at
1280 × 800 and 1024 × 768, for first-page failure, later-page failure, a request
in progress and the unchanged lyric layout. Before compiles the sidebar source
from `3ddd309` with the same theme and new deterministic failure fixtures. After
compiles the updated sidebar. Static captures do not verify audio synchronization.

Windows validation:

- `cargo fmt --all --check` and `git diff --check` passed.
- `cargo clippy --locked --no-default-features --features demo --all-targets -- -D warnings` passed.
- `cargo test --locked --no-default-features --features demo --all-targets` passed:
  960 library tests, one ignored native credential round trip, and all binary,
  integration and example targets. The isolated child-process test also passed.
- `cargo test --locked --no-default-features --features demo --doc` passed
  (no doc tests are currently defined).
- Release-name, MagicSpot release-preparation and Flatpak metainfo Python checks
  passed (4, 1 and 4 tests respectively).
- Default/all-feature Clippy, test, doc-test and documentation checks were
  attempted. All stop in projectm-sys because `VCPKG_INSTALLATION_ROOT` is unset.
- The Linux launcher check cannot complete here: no working Bash/Unix tools or
  Ruby are available. Jekyll cannot run because Ruby/Bundler are absent.

No dependencies, version, release packages or publication settings changed.
Live Spotify validation and native macOS/Linux coverage remain outstanding.
Existing OLED edits in the working tree were preserved.
