# MagicSpot 2.0 status

The maintainer requested a regular `v2.0.0` release with a standalone Windows x64 EXE and a universal Mac DMG. The application, release notes, packaging and publication workflow now target `2.0.0` without a preview suffix. The [release page](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.0) is the source of truth for availability; do not describe the downloads as public until GitHub publishes the verified assets.

## Source and scope

MagicSpot is a focused lyrics and theme fork of Spotifast main `7048219`, five commits beyond upstream stable `v0.12.0`. It adds the Apple Music inspired lyrics sidebar, saved font and size options, a subtle active-line glow, artwork-derived background, a larger cover in a wider sidebar, and OLED Blue. The app uses a separate MagicSpot profile and retains upstream Spotify sign-in, playback and Connect flows. Local playback requires Spotify Premium.

The Windows download is a versioned standalone `.exe` with separate license notices and checksums. The Mac download is a universal Apple Silicon and Intel `.dmg`. Both are normal builds without demo data or MilkDrop. Windows is unsigned; macOS is ad-hoc signed without notarization. Linux remains a source and CI target.

## Release verification

The earlier application code passed Windows and Mac package validation on successful CI run [37397093468](https://github.com/FallenG101/MagicSpot2/actions/runs/37397093468). Its Windows executable passed version, x64 PE, license and checksum checks; the DMG passed mount, architecture, version and signature checks on GitHub's Mac runner. Those binaries carry an earlier version and cannot be renamed into `2.0.0` assets. The regular release requires new Windows and Mac builds from its own current-main commit, along with quality, test, documentation and Nix gates. The publication workflow verifies both package checksum files and only then creates `v2.0.0` as GitHub's Latest release.

Live Spotify account sign-in, playback and Connect have not been exercised in this development session. The inherited flows remain enabled, but demo and automated coverage do not establish an account-backed session. No startup or memory improvement is claimed.

## Maintenance

The [release decisions](RELEASE_DECISIONS.md) require a full `2.0.0` version in the app, tag, title and asset names, a visible Latest release on the repository home page, and anonymous checks of all public downloads. [PACKAGING.md](../../PACKAGING.md) describes the release gate. The report-only upstream drift workflow does not merge, publish or submit upstream changes automatically.