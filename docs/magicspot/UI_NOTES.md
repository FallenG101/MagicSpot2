# Lyrics sidebar and OLED Blue

Requested October 5, 2026: an Apple Music-inspired lyrics sidebar and an OLED
theme with blue accents. This visual scope was requested directly by the
maintainer. No additional shell/navigation redesign is included.

## Sidebar

- A compact cover, song title and artist header above the words.
- Responsive 24–32 point bold lyrics, generous line spacing, a bright active
  line and quiet surrounding lines. Font metrics stay fixed when a line changes.
- Smooth following and gentle scroll-edge fades. Manual wheel/drag scrolling
  releases following; Follow and click-to-seek remain available.
- Loading, missing, instrumental, error/retry and untimed content retain their
  existing meanings. Plain lyrics use readable text without a false active line.
- Full-window lyrics retain their layout.

## OLED Blue

Choose **Settings > Appearance > Theme > OLED Blue**. Window, library/sidebar
and player surfaces are black, with blue selection, focus and hover accents.
Raised controls use very dark cool surfaces so they remain distinguishable.
The built-in choice is saved as `oled_blue` and needs no theme file. Existing
System, Light, Dark and custom choices remain available; no defaults are changed.

Demo preview:

```powershell
cargo run --locked --release --no-default-features --features demo -- --demo --demo-show lyrics,oled
```

## Review and validation

Before-and-after evidence is saved locally in `.cache/lyrics-review/index.html`,
with theme, size and state selectors. Before is commit `225a65c`, using the same
demo data, inner window size and six-second capture delay. OLED Blue is new and
is compared with the old Dark appearance. Native captures are Windows only.

The release/demo Windows test suite passed 971 tests, with one native-store test
ignored in the main suite. That dummy-grant native-store round trip passed
separately. Strict clippy passed. Regression coverage includes stable wrapped
line metrics, manual scroll and Follow, full-window transitions, theme persistence,
custom-palette switching, text contrast and rendering of pages/dialogs/states.
The autoscroll test now locates the actual panel instead of clicking the old
lyrics-header coordinate, which the new song header occupies.

No
startup, memory, CPU or playback-speed improvement is claimed. No dependencies,
network services, Spotify grants or profile paths are changed by this UI work.
