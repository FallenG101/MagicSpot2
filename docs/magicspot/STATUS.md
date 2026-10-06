# MagicSpot 2.0 status

The regular [MagicSpot 2.0 release](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.0) is public and marked **Latest** on the repository home page. It offers a standalone Windows x64 EXE, a universal Apple Silicon and Intel DMG, third-party license notices and SHA-256 checksums. There is no ZIP or preview release. Windows is unsigned; the Mac app is ad-hoc signed without notarization. Linux remains a source and CI target.

## Source and scope

MagicSpot starts from Spotifast main `7048219`, which was still upstream's main commit at the [functional parity audit](../../UPSTREAM.md#functional-parity-audit). The changes are the lyrics sidebar, saved font/size and glow controls, artwork-derived background and growing cover, OLED Blue, and the fork's separate identity and packaging. The playback engine and Spotify backend source are unchanged. Both downloads include upstream's default MilkDrop feature and exclude demo data.

## Validation

[CI run 37405687141](https://github.com/FallenG101/MagicSpot2/actions/runs/37405687141) passed all ten jobs on release commit `84de29c97ddf366c29813608674bfad3f4758bd4`: normal and demo builds, platform tests, quality, docs, Nix and Mac DMG packaging. The Windows EXE reports `magicspot2 2.0.0`; its x64 PE header, license sidecar and package SHA-256 values were checked. The Mac workflow verified both architectures, version, mounted DMG and app signature. GitHub's public API reports `draft: false`, `prerelease: false` and `v2.0.0` as Latest; the repository's visible Releases panel shows MagicSpot 2.0, and anonymous requests to the release page and both downloads returned HTTP 200.

The automatic publisher initially rejected a nonexistent `v2.0.0` tag because its 404 handling read GitHub's JSON error body as a tag SHA. After all CI jobs passed, the same CI artifacts were independently verified and published at that tested commit. The tag check and checksum-order comparison were fixed in the publication code afterward. The superseded preview release and tag were removed only after the regular release was verified.

Live Spotify account sign-in, playback and Connect have **not** been exercised in this development session. Their inherited flows remain enabled; automated tests and source comparison do not replace an account-backed test. No startup or memory improvement is claimed.

## Maintenance

The [release decisions](RELEASE_DECISIONS.md) record the required package types and public checks. [PACKAGING.md](../../PACKAGING.md) gives the build and publication procedure. The [upstream sync guide](MAINTENANCE.md) keeps future lyric and theme changes separate from fork identity. The drift workflow reports upstream changes without merging or publishing them.
