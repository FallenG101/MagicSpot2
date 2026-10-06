# Lyrics sidebar and OLED Blue

Requested October 5, 2026: an Apple Music-inspired lyrics sidebar and an OLED
theme with blue accents. This visual scope was requested directly by the
maintainer. No additional shell/navigation redesign is included.

## Sidebar

- A larger rounded cover, song title, artist and album card above the words.
  The cover scales with the sidebar width, up to 240 points in an expanded panel.
- Responsive 24–32 point bold lyrics, generous line spacing, a bright active
  line and quiet surrounding lines. Font metrics stay fixed when a line changes.
- Inter, System and Monospace font choices in Settings > Appearance. System uses
  the platform font when available and falls back to bundled Inter. Font choices
  change only the lyrics sidebar and preserve fallback support for other scripts.
- Font size can be set from 18 to 48 points. Auto (the default) keeps the
  responsive 24–32 point sizing. Turn Auto off to use the size slider; it is saved.
- A subtle optional glow behind the current timed line, without changing wrapping.
  Untimed lyrics never receive a false current-line glow.
- The current song's blurred cover provides the sidebar background. Artwork is
  fetched and blurred through the existing asynchronous cache; the previous cover
  stays until the next is ready. Glow and artwork are enabled by default and can
  be turned off in Appearance. Without artwork, the selected theme supplies the
  background, including pure black for OLED Blue.
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

The release/demo Windows test suite passed 974 tests, with one native-store test
ignored in the main suite. That dummy-grant native-store round trip passed
separately. Strict clippy passed. Regression coverage includes stable wrapped
line metrics, manual scroll and Follow, full-window transitions, theme persistence,
custom-palette switching, text contrast and rendering of pages/dialogs/states.
Font persistence and old settings defaults, glow on/off layout, untimed lyrics,
and changing appearance while manually reading are covered by focused tests.
The final width/size adjustment also has native captures of the expanded cover,
40-point lyrics and the Appearance controls. Its demo flags are `lyrics-wide`
and `lyrics-large`; final cross-platform compilation remains a CI gate.
The autoscroll test now locates the actual panel instead of clicking the old
lyrics-header coordinate, which the new song header occupies.

No startup, memory, CPU or playback-speed improvement is claimed. No dependencies,
network services, Spotify grants or profile paths are changed by this UI work.


User controls are documented in [Lyrics & Themes](../_guide/lyrics-and-themes.md). The documentation index and maintenance guide distinguish inherited review captures from MagicSpot evidence.
