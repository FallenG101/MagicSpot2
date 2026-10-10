"""Capture matching native demo windows. No real Spotify profile is opened."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

CASES = [
    ("default", "#648: default title bar off", "playlist:pl1", "lyrics", False, ":minimize,maximize,close"),
    ("right", "#648: right buttons and lyrics", "playlist:pl1", "lyrics", True, ":minimize,maximize,close"),
    ("left", "#648: left buttons and queue", "playlist:pl1", "queue", True, "close,minimize,maximize:"),
    ("appearance", "#648: Appearance setting", "settings", "appearance", False, ":close"),
    ("playlist", "#722/#744/#745: playlist contributors and shuffle", "playlist:pl1", "", False, ":close"),
    ("radio", "#659: song radio", "radio:spotify:track:trk0", "", False, ":close"),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", required=True, type=Path)
    parser.add_argument("--after", required=True, type=Path)
    parser.add_argument("--before-sha", default="8491cf3")
    parser.add_argument("--after-sha", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    host = "Windows" if sys.platform == "win32" else "Linux"
    cases = CASES if host == "Linux" else CASES[4:]
    args.output.mkdir(parents=True, exist_ok=False)
    scratch = Path(".cache/upstream-visual-profiles").resolve()
    env = os.environ.copy()
    for phase, binary in (("before", args.before), ("after", args.after)):
        for name, label, page, flags, titlebar, layout in cases:
            for theme in ("dark", "light"):
                for size, pixels in (("normal", "1280x800"), ("narrow", "1024x768")):
                    key = f"{phase}-{theme}-{size}-{name}"
                    profile = scratch / key
                    config = profile / "config"
                    config.mkdir(parents=True, exist_ok=True)
                    (config / "settings.json").write_text(json.dumps({"custom_titlebar": titlebar}), encoding="utf8")
                    if host == "Linux":
                        env.update(XDG_CURRENT_DESKTOP="GNOME", GSETTINGS_BACKEND="keyfile", XDG_CONFIG_HOME=str(config))
                        subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.preferences", "button-layout", f"'{layout}'"], env=env, check=True)
                    shot = (args.output / f"{key}.png").resolve()
                    command = [str(binary.resolve()), "--demo", "--demo-data", str(profile),
                               "--demo-page", page, "--demo-show", ",".join(filter(None, [flags, theme])),
                               "--demo-size", pixels, "--demo-shot", str(shot), "--demo-shot-delay", "5000"]
                    kwargs = {}
                    if host == "Windows":
                        startup = subprocess.STARTUPINFO()
                        startup.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        startup.wShowWindow = 0
                        kwargs["startupinfo"] = startup
                    subprocess.run(command, env=env, check=True, timeout=45, stdout=subprocess.DEVNULL, **kwargs)
                    if not shot.is_file():
                        raise RuntimeError(f"Missing capture: {shot}")
                    print(f"Captured {key}", flush=True)
    metadata = dict(host=host, before=args.before_sha, after=args.after_sha, settle_ms=5000,
                    cases=[dict(key=c[0], label=c[1]) for c in cases])
    (args.output / "capture.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf8")
    template = Path(__file__).with_name("upstream-review.html").read_text(encoding="utf8")
    (args.output / "index.html").write_text(template.replace("/*CAPTURE_METADATA*/", json.dumps(metadata)), encoding="utf8")


if __name__ == "__main__":
    main()
