"""Apply identical Blend sample data to throwaway before/after demo checkouts.

This only adds a fixture flag to the demo, leaving the product UI under review
unchanged. Never pass the working checkout used for ordinary builds.
"""

from pathlib import Path
import sys

ANCHOR = '            "queue" => app.show_queue_panel = true,\n'
FIXTURE = '''            "review-blend" => {
                if let Some(page) = app.playlist_pages.get_mut("pl1") {
                    if let Some(playlist) = page.playlist.get_mut() {
                        playlist.name = "Carmine + Sam Blend".into();
                        playlist.owner.id = Some("spotify".into());
                        playlist.owner.display_name = Some("Spotify".into());
                        playlist.collaborative = false;
                    }
                    page.contributors = ["demo".into(), "sam".into()].into_iter().collect();
                    for (index, item) in page.items.items.iter_mut().enumerate() {
                        if let Some(adder) = &mut item.added_by {
                            adder.id = Some(if index % 2 == 0 { "demo" } else { "sam" }.into());
                        }
                    }
                }
                app.user_names.insert("demo".into(), Some("Carmine".into()));
            }
'''

for directory in sys.argv[1:]:
    root = Path(directory).resolve()
    if root == Path.cwd().resolve() or ".cache" not in root.parts:
        raise SystemExit("Review fixtures require a throwaway .cache checkout")
    path = root / "src/demo.rs"
    source = path.read_text(encoding="utf8")
    if source.count(ANCHOR) != 1 or '"review-blend"' in source:
        raise SystemExit(f"Review fixture anchor changed: {path}")
    path.write_text(source.replace(ANCHOR, FIXTURE + ANCHOR), encoding="utf8")
    # Lyrics controls make the full Appearance group taller than a narrow
    # capture. Use the real settings search so the new switch is visible.
    entrypoint = root / "src/entrypoint.rs"
    source = entrypoint.read_text(encoding="utf8")
    needle = 'gettext(app.locale, "Appearance").into_owned()'
    if source.count(needle) != 1:
        raise SystemExit(f"Settings search fixture anchor changed: {entrypoint}")
    entrypoint.write_text(source.replace(needle, 'gettext(app.locale, "Custom title bar").into_owned()'), encoding="utf8")
