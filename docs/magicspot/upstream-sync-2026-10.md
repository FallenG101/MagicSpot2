# October 10, 2026 upstream sync and 2.0.1 candidate

The initial working tree was reviewed and saved byte-for-byte before editing.
OLED is preserved in `05581ad`, rapid lyric following in `484f2fb`, and playlist
page retry in `8491cf3`. Their existing native Windows evidence is retained.
All 23 upstream changes from `7048219` through `dd2d5e3` are integrated. None
are deferred. Cherry-picks carry original authors and upstream SHA trailers;
the README adaptation retains its author's credit and an Upstream-commit trailer.
No published commit was rewritten and no merge commit was created.

## Reviewed integration

| Upstream commit | MagicSpot commit | Change |
| --- | --- | --- |
| `4ba8d98e31fb73516fd702da3dd36a3cb8fa9126` | `83b2b14` | Spin the transport button while the next track loads (#654) |
| `6d970aca749086b96edf81376c2820eff6fb9bf8` | `9090b66` | Name a song radio opened from a list after its song (#659) |
| `2590e338096579b5dd7b374d41e180a72e1e09a3` | `5e3a4cd` | docs: improve README navigation and showcase existing visuals (#677) |
| `5d77caf1cf7ae53b68c9f339d23886a633a2d573` | `288324b` | Bring the Windows on ARM build level with x64 (#682) |
| `a3e95f89b92d03352c720a9e4394e564fc6f80dc` | `d5ec5cc` | Stop a multi-song drag within its playlist from adding copies (#684) |
| `995c768dcba4da7f93302bf2107af6b7ec3df02b` | `d307929` | Fix playback artifacts and respond to held slider presses (#686) |
| `12deee472ee87e2c9ed0e0f13730cbdd9a6cfa45` | `31c836c` | Let dual-GPU Macs keep the integrated GPU for Spotifast (#736) |
| `eff77cd340dc5312a2f76b59c7a2ee73d0011867` | `005085a` | fix(i18n): refine Turkish translations for consistency and natural phrasing (#668) |
| `031e8c565c29bd72763bf29f0cfbe17c3446bc58` | `3f50d82` | Let the stereo resampler use vector registers on every target (#681) |
| `9d74afe8ad5196eb67942f449d6ed57988d58697` | `96dece0` | Reduce library sorting work during scrolling (#717) |
| `88d5831f0d63e797579b4cdccfdc94d19efd85cb` | `c4bb44d` | feat(i18n): add Ukrainian language support (#718) |
| `277a4fabcd2ca11ced4adb45b274f29084fde7eb` | `90125cb` | Wait for room in the audio queue instead of polling it (#726) |
| `17f3a0db3547aee20b24c432a7b8fb5fe1709592` | `6144d09` | Hide a minimised window to the tray when it is closed (#725) |
| `f5a946c6bb1b332a1147153821172cf08eb84d30` | `6740151` | Keep the resume point and history safe when a session ends abruptly (#727) |
| `9dd23c9b27a0ad6d43d4569a36547f9806945451` | `783edde` | Keep an adder's name once it is found (#744) |
| `d692a2276e11a597b579ef033e09f0c14dfbe018` | `a3e2384` | Keep the playlist shuffle button green while hovered (#722) |
| `cbe817610546c8d1b023ab3977dd89ede65d372e` | `641a8af` | Show Added By in Blends (#745) |
| `5b7a5dfe8c15542ee82fd7560c1e36496306b6c9` | `1288646` | Keep each album's songs in track order when sorting by album (#701) |
| `14db97c82263400d180100135d631c9885245ce2` | `fd1be8f` | Add Linux custom title bar (#648) |
| `595ddc4e6ff4241f9c46e3b994ff48bd1cdd3c8a` | `a0d736b` | Follow the system's power and session state (#728) |
| `fea496e4a2c51fa89899e3e07a39e6f9fd02114f` | `80574cd` | Sleep in the tray until something is due (#730) |
| `13876a8e81c7abd90266a2c20d030c3e5958213b` | `51f919b` | Keep playing when the audio output changes (#731) |
| `dd2d5e34e66d4e01e31e595a3022a1de808b449a` | `16c603f` | Poll other devices less often when nobody can see the app (#733) |

## Adaptations and patch boundaries

- Kept MagicSpot's application/profile/update identities, lyrics controls,
  neutral OLED palette, standalone EXE/DMG packaging and GitHub download routes.
- Adapted README navigation and getting-started text to this fork. Preserved
  original copyright and license notices and internal library/catalogue names.
- Kept every inherited external publisher guarded to crmne/spotifast.
- Combined Windows ARM CI improvements with the fork's own jobs and names.
  Windows ARM remains a compile/test target without a published ARM download.
- Preserved appearance demo filtering during upstream event-loop replacement.
- Corrected the Ukrainian title-bar string missed by upstream #648 in `abd5d21`.
- Optional Linux title-bar scope was explicitly approved on October 10. Native
  Linux evidence must cover default off, desktop-configured left/right buttons,
  sidebar/queue space and Appearance settings in both themes at both sizes.
- Kept the old MagicSpot vendor hash temporarily to derive the final hash from
  Nix CI after the final dependency and package-version changes. Spotifast's
  hash was not copied.

## Dependency review

All fastframe runtime/build crates move together from crmne's v0.4.1 to
dennisgr7/fastframe `f7dc6fbe938e8a953509d110cdba036f537e5b7e`.
The reviewed commits add Windows MMCSS audio priority and condition-variable
headless waits/wakes. projectm-sys moves to dennisgr7/projectm-rs
`1ef6df1c20247a3a5800c625e46262330f93bbd6`, fixing target-architecture vcpkg
triplets while respecting CMAKE_GENERATOR. Cargo.toml and Cargo.lock agree.
egui remains `ba6790fe7cf46e58e8d27ce1524cbfdee745e938`, with all its crates
together; winit remains `ed7caa9023f10b397f5b6ec8284a840cbd8a6f65`.
librespot remains `23fc42cff37848e51f0d8eaefad1a93941b71e59`.

## Validation record

The preserved local fixes passed formatting, Clippy and all no-MilkDrop/demo
targets, including 960 library tests (one ignored). After upstream integration,
1,002 library tests passed (two ignored) and thirteen binary tests passed.
The wider suite found the stale Ukrainian title-bar message. Its correction
passed the targeted localization suite. Three temporary-repository drift tests
pass, including a cherry-picked base that is not an ancestor of MagicSpot HEAD.

Windows full-feature prerequisites were resolved with a local vcpkg GLEW build,
MSVC/Ninja and libclang. On the 2.0.1 source, all-feature tests passed with
1,011 library tests (two ignored), thirteen binary tests and every other target.
Default-feature tests passed with 986 library tests (two ignored), twelve binary
tests and every other target. Clippy passed for both configurations; all-feature
doctests and warning-free Rustdoc passed. Formatting, four release-name tests,
four Flatpak metadata tests, five package-verifier tests, six exact-commit CI
gate tests and three drift tests also passed.

The first candidate CI run, [38083199342](https://github.com/FallenG101/MagicSpot2/actions/runs/38083199342),
derived the final MagicSpot 2.0.1 vendor hash:
`sha256-wCKC9aLQqXYCxuzhO+MtqSW98cGZwqdq9a1qz7T/HzE=`.
This came from MagicSpot's version and lockfile, not Spotifast's hash. The same
run exposed a short-SHA checkout error in the new visual job and Ubuntu's old
gettext lacking Rust extraction. Both prerequisites were corrected. Gettext
now comes from the locked Nix input. The second run regenerated the catalogues;
semantic review confirmed all 649 messages and every translation unchanged.
Only references, headers and wrapping changed. The localization test passed
after applying the reviewed hunks. Neither failed run could publish.

[Native Windows evidence](upstream-review/windows/index.html) has sixteen
matching light/dark, narrow/normal playlist and radio captures, all inspected.
[Native Linux evidence](upstream-review/linux/index.html) has 56 matching
captures from `97d955fc168a4f05504b834e9eec954264deb572`, all inspected on
October 10. Default-off layout, both window-button placements, lyrics/queue
space, the setting, playlist/radio and Blend contributors fit in both themes
at both sizes. The [combined comparison](upstream-review/index.html) links each
case and platform. The matching application source tree is recorded in
`upstream-review/linux/REVIEW.json`.

[CI 38083468357](https://github.com/FallenG101/MagicSpot2/actions/runs/38083468357)
passed all ten platform/build/docs/Nix jobs on `5c4928f`, including native ARM
tests, credential-store round trips, standalone Windows runtime checks and
universal DMG verification. Its two new checks exposed stale translation
references and a missing Linux capture runtime library, both corrected in
subsequent focused commits. The current
[CI 38085687912](https://github.com/FallenG101/MagicSpot2/actions/runs/38085687912)
has passed quality, docs, Linux/macOS tests, Linux/macOS release/demo builds,
universal DMG verification and the complete Nix package build with MagicSpot's
recalculated hash. Its Windows and cache-finalization jobs are still finishing
at the time of this record. The downloaded Windows EXE and universal DMG also
pass the combined package verifier. They are candidate artifacts, not published
downloads.

After this review, the maintainer explicitly chose “Yes, make 2.0.1
Windows/macOS only” on October 10. Linux release/demo builds, platform tests,
Nix packages and Linux screenshot jobs were removed from the final candidate
CI and publication requirements, including the Linux-only inspection guard.
The six-test guard suite became five tests because that Linux-specific
requirement no longer applies; exact-main, job-set, missing/skipped/failed-job
and wrong-SHA checks remain enforced. Shared quality/docs jobs remain on Ubuntu;
Windows x64/ARM and macOS tests and both supported download builds remain
required. Linux source and packaging are retained as best effort. The completed
Linux visual review and successful Nix build above are preserved, not claimed
as final-candidate gates.

The final candidate must pass all eight jobs on current main before publication.
No live Spotify account sign-in, playback or Connect
validation has been performed; automated and deterministic demo checks do not
establish it.
