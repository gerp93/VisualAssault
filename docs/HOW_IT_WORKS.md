# How this works

This is the technical/background doc — the stuff a consumer doesn't need to
read to apply a theme, but that an AI assistant (or a contributor) benefits
from knowing. If you just want to apply a theme, the root
[`README.md`](../README.md) Quick Start is all you need.

## Architecture

- **`themes/THEMES.md`** is the single source of truth for every theme's
  exact color values — no JSON, no schema, no build step behind it.
- **`prompts/`** holds the instructions consumers give their AI assistant to
  apply ([`apply-theme.md`](../prompts/apply-theme.md)) or update
  ([`update-theme.md`](../prompts/update-theme.md)) a theme in their own
  app. The root README's Quick Start is a trimmed copy of `apply-theme.md`
  for the common case.
- **`examples/reference/`** holds illustrative (non-authoritative) example
  output from an earlier JSON+generator prototype — useful for
  naming-convention ideas, never a source of truth.

An AI assistant reads a theme's token values from `themes/THEMES.md` and
produces exactly one native artifact for whatever styling mechanism the
target app already uses — a CSS file with custom properties, a Tailwind
config fragment, a JS theme object, a Tkinter style dict, a Qt stylesheet,
and so on. It doesn't rewire the app's components to consume that file —
that's a separate, explicit step requested on its own.

## Why markdown instead of a generator pipeline

An earlier prototype (see the `copilot/setup-visual-assault-theme` branch
history) defined themes as JSON validated against a schema, with a
hand-written Python generator per output framework. That doesn't scale to
"support any framework" — every new target needs its own generator to
write and maintain. Putting an AI assistant in that role instead means new
frameworks are supported for free, at the cost of per-application review
instead of a guaranteed-correct deterministic generator. For a library of
decorative themes, that trade is worth it.

## Design philosophy (full version)

These themes are **not** meant to be unreadable or low-contrast. Every theme
keeps text legible against its background — that's a hard requirement, not
a nice-to-have.

What makes a theme "visual assault" is the *nature and combination* of the
colors themselves: bright neons, harsh or clashing hues, jarring pairings
that are perfectly readable but hard to stare at for long. Think "loud," not
"broken."

Not every theme in this set has to be abrasive, either. A handful lean more
"striking and cohesive" than "harsh," and that's expected — this is a
library of bold, opinionated palettes, not a mandate that everything has to
be ugly on purpose.

The full rules for transcribing values (never invent/round/"fix" a color)
live at the top of `themes/THEMES.md` — anyone or anything applying a theme
should follow them exactly.

## Updating an already-applied theme

See [`prompts/update-theme.md`](../prompts/update-theme.md). Short version:
if a theme's definition changes upstream after you've already applied it,
diff the old and new token blocks (or the git refs, if you tracked one) and
patch only what changed — don't blindly regenerate and stomp any local
customization.

## Contributing a new theme

Add a new section to `themes/THEMES.md` following the existing format: a
name, a short description, and a fenced block with every token from its
[Token reference](../themes/THEMES.md#token-reference) filled in as an exact
`rgb(r, g, b)` value.
