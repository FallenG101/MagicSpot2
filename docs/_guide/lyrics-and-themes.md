---
title: Lyrics & Themes
description: Choose lyric fonts and sizes, artwork backgrounds and OLED.
nav_order: 4
---

## Open and resize the sidebar

Choose the microphone button in the player bar, or press **L**. Drag the sidebar's left edge to widen it. The rounded album cover grows with the available width, up to 240 points; a narrow window limits how far the sidebar can expand.

Synced lyrics highlight the current line and follow playback smoothly. Scroll or drag to read ahead; **Follow** returns to the current line. Click a timed line to seek. Plain lyrics have no timing, so they do not highlight a current line or support seeking. Missing lyrics and load errors keep their normal empty or retry controls.

## Fonts, size and glow

Open **Settings > Appearance**:

| Control | Choices and behavior |
| --- | --- |
| Lyrics font | **Inter** (default), **System**, or **Monospace**. System uses the platform font when available, with Inter as fallback. |
| Lyrics font size | **Auto** (default) sizes text for the sidebar. Click Auto to switch to a manual size, then adjust the slider from **18 to 48 points**. Click Auto again to restore automatic sizing. |
| Current lyric glow | Enabled by default. Adds a slight glow behind the sharp current line in synced lyrics. |
| Lyrics artwork background | Enabled by default. Uses a blurred version of the current cover with a dark overlay for readable text. Without artwork, the theme supplies a solid surface. |

These choices are saved between launches. Changing size or font reflows the sidebar without changing playback. The artwork background is independent of the app's general album-art accent setting. Even with a light app theme, the artwork-backed lyrics use a dark readable surface.

The expand button opens the inherited full-screen lyrics view. Its layout remains separate from the new sidebar typography controls. Press **Esc** or choose the shrink button to return.

## OLED

Choose **Settings > Appearance > Theme > OLED**. Main surfaces are black, with neutral gray controls and white accents. Turn **Lyrics artwork background** off for a pure-black lyrics surface. With it on, the sidebar keeps the song's artwork colors. Existing saved OLED selections remain compatible. This source update is not yet included in the published 2.0.0 downloads, which call the theme OLED Blue.

![Native Windows demo capture of the MagicSpot sidebar](/magicspot/lyrics-oled.png)

The image uses sample data for visual review. Release downloads use normal Spotify sign-in and playback.
