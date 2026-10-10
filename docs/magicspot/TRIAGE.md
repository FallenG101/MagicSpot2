# Visual scope ledger

Visual approval is separate from implementation, automated tests and release gates.

| Upstream PR | Scope | Maintainer decision | Evidence and remaining gates |
| --- | --- | --- | --- |
| #648 | Optional Linux custom title bar, desktop-configured left/right buttons and space above navigation/side panels; off by default | October 10, 2026: “Include the optional Linux title bar”, subject to inspecting matching Linux light/dark and narrow/normal captures | [Native Linux comparison](upstream-review/linux/index.html) inspected October 10: default off, left/right controls, lyrics/queue space and setting fit in both themes at both sizes. No adjustment required. All twelve exact-main CI jobs, Nix and verified packages remain publication gates. |

The requested OLED, rapid-lyrics and playlist-retry scope remains approved.
The October upstream sync does not authorize any further shell redesign.
