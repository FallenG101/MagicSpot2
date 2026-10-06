# MagicSpot documentation

MagicSpot 2 is a focused lyrics and theme fork of [Spotifast](https://github.com/crmne/spotifast). The first preview is `2.0.0-preview.1`. Get the [public Preview 1 downloads](https://github.com/FallenG101/MagicSpot2/releases/tag/v2.0.0-preview.1) from its direct release page; GitHub's repository home page omits prereleases from the Releases panel.

## User guides

- [What MagicSpot offers](_guide/what-is-spotifast.md)
- [Downloads and manual updates](_guide/download.md)
- [Install, sign in and build from source](_guide/getting-started.md)
- [Everyday use](_guide/using-spotifast.md)
- [Lyrics and OLED Blue](_guide/lyrics-and-themes.md)
- [Winamp mini player](_guide/winamp.md)
- [Optional source-build MilkDrop](_guide/milkdrop.md)
- [Personal Spotify app](_guide/make-it-even-faster.md)

## Reference

- [Settings, profile paths and commands](_reference/settings-and-files.md)
- [Spotify connections and credentials](_reference/how-it-connects.md)
- [Queue behavior](_reference/queue.md)
- [Spotify capabilities and limits](_reference/what-spotify-allows.md)
- [Privacy](_reference/privacy.md)
- [Translations](_reference/translating.md)
- [Packaging](_reference/packaging.md) and [Nix cache](_reference/nix-cache.md)

## Development and maintenance

- [Contributing](../CONTRIBUTING.md) and [agent instructions](../AGENTS.md)
- [Upstream provenance and patch inventory](../UPSTREAM.md)
- [Maintenance and sync procedure](magicspot/MAINTENANCE.md)
- [Identity](magicspot/IDENTITY.md), [validation status](magicspot/STATUS.md), [UI evidence](magicspot/UI_NOTES.md) and [historical baseline](magicspot/BASELINE.md)
- [Preview 1 notes](../packaging/release-notes/v2.0.0-preview.1.md) and [release procedure](../PACKAGING.md)
- [Release decisions and distribution contract](magicspot/RELEASE_DECISIONS.md)

The Jekyll site source is maintained here. With Ruby and Bundler installed, run `bundle install` and `bundle exec jekyll build` from `docs/`; `bundle exec jekyll serve` previews it locally. There is no configured MagicSpot domain or enabled Pages deployment. CI builds the site for validation. GitHub renders this index and the Markdown guides directly; site-root links inside guides refer to the Jekyll routes.

Guide filenames retain upstream names where that keeps links and future syncs simple. Version numbers beginning with `0.` in the retained technical reference describe Spotifast history, not MagicSpot releases. Old `packaging/release-notes/v0.*`, review assets under `docs/assets/`, and the untouched baseline are historical upstream material. Their screenshots, signatures, downloads and performance measurements are not claims about MagicSpot.
