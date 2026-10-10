# Maintaining the focused fork

Keep MagicSpot's lyrics and theme changes small and keep the Spotify engine close to upstream. [UPSTREAM.md](../../UPSTREAM.md) records the integrated base, dependency pins and patch inventory. The report-only drift workflow identifies upstream movement and changed-file overlap; it does not integrate or publish changes.

## Sync procedure

1. Start with a clean checkout of `main`. Fetch `origin` and `upstream`; use fast-forward-only pulls for published MagicSpot work. Review upstream release notes and `git log --oneline RECORDED_BASE..upstream/main`, using the base from UPSTREAM.md.
2. Review the entire upstream diff and overlaps with the UI, identity and packaging patches. Check dependency moves as a set, especially egui/winit and fastframe. Do not substitute discontinued v3 dependencies.
3. Integrate a bounded upstream batch with focused cherry-picks or a reviewed application of the diff onto main. Keep published history linear; do not merge upstream main or rebase already published MagicSpot commits. Preserve contributor credit and record the integrated upstream commit IDs, including any deliberately deferred commits.
4. Resolve UI conflicts against the approved behavior: fonts, saved 18–48 point size/Auto, active glow, cover background, growing cover, smooth follow/seek and OLED. Preserve upstream playback, authorization, queue and API contracts.
5. Recheck MagicSpot command/profile/credential/bundle/IPC/media/update identities. Review dependencies, Cargo.lock and the Nix vendor hash. Run the checks in [CONTRIBUTING.md](../../CONTRIBUTING.md); inspect native UI evidence when appearance changes. Use account-backed tests when authentication/playback changes require them, and state platform coverage honestly.
6. Update UPSTREAM.md, STATUS.md and the affected user/reference docs with the new base, deferred commits, conflicts and actual validation. Commit each compiling topic, check that unpublished commits contain no merges, then push. Syncing source does not by itself authorize a new release or public upstream message.

## Patch boundaries

Keep generally useful lyrics/theme changes independent of MagicSpot branding, profile and release changes. That makes future upstream proposals reviewable without asking Spotifast to adopt the fork's identity. The maintainer wants these UI improvements upstream eventually, but submitting a proposal, PR or message requires a direct request.

Internal library and catalogue names such as `spotifast`, `spotifast:liked-songs`, `assets/i18n/spotifast.pot` and legacy Omarchy assets remain where renaming adds churn without a user benefit. They are not instructions to use Spotifast's profile or publishers.

## Documentation and release upkeep

Use [docs/README.md](../README.md) as the documentation index. Update active guides, references, root policies, issue forms and site metadata together when app behavior or supported downloads change. Preserve and label historical baseline, upstream review evidence and `v0.*` notes rather than rewriting their history.

Only GitHub Releases establishes download availability. The 2.0.0 publisher is restricted to that version and requires successful current-main CI; see [PACKAGING.md](../../PACKAGING.md). New pushes replace the CI candidate. Future releases require their own scoped publication change. Version selectors and package-manager claims must follow files and channels that actually exist.
