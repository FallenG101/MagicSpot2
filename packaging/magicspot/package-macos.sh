#!/bin/bash
# Package the release executable as an ad-hoc signed universal MagicSpot DMG.
set -euo pipefail
binary="$1"
output="$2"
version=$(python3 -c 'import tomllib; print(tomllib.load(open("Cargo.toml", "rb"))["package"]["version"])')
name="magicspot2-v${version}-macos-universal.dmg"
input="$output/macos-input"
test ! -e "$input"
mkdir -p "$input/licenses"
lipo "$binary" -verify_arch arm64 x86_64
test "$("$binary" --version)" = "magicspot2 $version"
bash packaging/macos/bundle.sh "$binary" "$input/MagicSpot.app" "$version"
cp README.md LICENSE "$input/"
cp assets/fonts/Inter-LICENSE.txt assets/fonts/NotoEmoji-LICENSE.txt "$input/licenses/"
cp assets/icons/LICENSE.txt "$input/licenses/Lucide-LICENSE.txt"
ln -s /Applications "$input/Applications"
test "$(/usr/libexec/PlistBuddy -c 'Print :CFBundleIdentifier' "$input/MagicSpot.app/Contents/Info.plist")" = 'com.falleng101.magicspot2'
test "$(/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' "$input/MagicSpot.app/Contents/Info.plist")" = "$version"
codesign --verify --strict "$input/MagicSpot.app"
hdiutil create -volname 'MagicSpot' -srcfolder "$input" -ov -format UDZO "$output/$name"
hdiutil verify "$output/$name"
mount=$(mktemp -d)
trap 'hdiutil detach "$mount" >/dev/null 2>&1 || true; rmdir "$mount" 2>/dev/null || true' EXIT
hdiutil attach "$output/$name" -readonly -nobrowse -mountpoint "$mount"
test "$("$mount/MagicSpot.app/Contents/MacOS/MagicSpot" --version)" = "magicspot2 $version"
lipo "$mount/MagicSpot.app/Contents/MacOS/MagicSpot" -verify_arch arm64 x86_64
codesign --verify --strict "$mount/MagicSpot.app"
hdiutil detach "$mount"
rmdir "$mount"
trap - EXIT
(cd "$output" && shasum -a 256 "$name" > checksums.txt)
