# TODO

This repo's own backlog, not a KVG_Standards compliance checklist (see
[KVG_Standards](https://github.com/gerp93/KVG_Standards)). Just what's not built yet.

## Features

-

## Fixes

- `scripts/generate_packages.py` reads and writes files with the platform default encoding, so on Windows it
  turns the em dash in the generated Flet docstring into a garbage character. Pass `encoding="utf-8"` (CI on
  Linux is unaffected).
