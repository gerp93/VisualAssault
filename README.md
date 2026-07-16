# Visual Assault

A library of bold, loud, cross-framework theme palettes — defined once in
Markdown, applied to your app by your own AI coding assistant. No package to
install, no per-framework generator to maintain.

## Quick Start

Copy the block below into your AI coding assistant (Claude Code, Cursor,
Copilot Chat, etc.) from inside your app's repo, filling in a theme name from
the list below:

```
Fetch https://raw.githubusercontent.com/gerp93/VisualAssault/main/themes/THEMES.md
and apply the "<theme name>" theme to this app. Detect this app's styling
mechanism (CSS, Tailwind, a JS theme object, Tkinter, etc.) and produce one
native theme file using that mechanism, transcribing the theme's color
values exactly. Do not rewire existing components to use it unless I ask
separately.
```

If your assistant can't fetch URLs, open `themes/THEMES.md` yourself, copy
just the one theme's section, and paste it in after "apply the following
theme to this app:" instead.

That's it — there's nothing to `npm install` or `pip install`. For the fuller
version of this prompt (with more detail on scope/behavior), see
[`prompts/apply-theme.md`](prompts/apply-theme.md). Updating a theme you've
already applied is a separate, smaller ask — see
[`prompts/update-theme.md`](prompts/update-theme.md).

## How this works

- **`themes/THEMES.md`** is the single source of truth for every theme's
  exact color values — no JSON, no schema, no build step behind it.
- **`prompts/`** holds the instructions consumers give their AI assistant to
  apply or update a theme in their own app.
- **`examples/reference/`** holds illustrative (non-authoritative) example
  output from an earlier prototype — useful for naming-convention ideas, not
  a source of truth.

An AI assistant reads a theme's token values from `themes/THEMES.md` and
produces exactly one native artifact for whatever styling mechanism your app
already uses — a CSS file with custom properties, a Tailwind config
fragment, a JS theme object, a Tkinter style dict, a Qt stylesheet, and so
on. It doesn't rewire your components to consume that file — that's a
separate, explicit step you ask for if and when you want it.

## Design philosophy

These themes are **not** meant to be unreadable or low-contrast — text stays
legible against its background in every theme here. What makes a theme
"visual assault" is the *nature and combination* of the colors themselves:
bright neons, harsh or clashing hues, jarring pairings that are perfectly
readable but hard to stare at for long. Not every theme has to be abrasive,
either — a few lean more "striking" than "harsh," and that's expected.

See `themes/THEMES.md` for the full philosophy and every theme's exact
values.

## Available themes (14)

| Theme | Vibe |
|---|---|
| Blue Oval | Deep blue, high-contrast |
| Bubblegum | Hot pink explosion |
| Commander Keen | Retro DOS EGA/VGA palette |
| Electric Lime | Bright green-yellow blast |
| Flambeau | Warm orange and ember tones |
| Flambeau Inverse | Inverse of Flambeau |
| Green Acres | Farm-green and yellow |
| Hacker | Matrix-style green on black |
| Hawkeye | Black and old-gold |
| Lava | Fiery red-hot |
| Merica | Red/white/blue |
| Neon | High-contrast neon dark mode |
| Red Barn | Barn red with bright accents |
| Retrowave | 80s synthwave palette |

## Contributing a new theme

Add a new section to `themes/THEMES.md` following the existing format: a
name, a short description, and a fenced block with every token from the
[Token reference](themes/THEMES.md#token-reference) filled in as an exact
`rgb(r, g, b)` value.
