# Prompt: Apply a Visual Assault theme to an app

This is the canonical, full version of the prompt used to apply one theme
from `themes/THEMES.md` to a target application. For the short copy-paste
version, see the Quick Start section in the root `README.md` — this file
exists for reference and for anyone who wants the reasoning spelled out.

## Prompt template

```
I want to apply the "<THEME NAME>" theme from the Visual Assault theme
library to this app. The theme's exact token values are here:

https://raw.githubusercontent.com/gerp93/VisualAssault/main/themes/THEMES.md

(If you can't fetch URLs, I'll paste the theme's block below instead.)

Please:
1. Look at this repo and figure out how it currently handles styling/theming
   (plain CSS, CSS custom properties, Tailwind, a JS theme object like MUI or
   styled-components, Tkinter ttk styles, a Qt stylesheet, or something
   else).
2. Produce ONE file, in whatever format is native to that styling mechanism,
   that defines this theme using it — e.g. a `.css` file with custom
   properties, a Tailwind config fragment, a theme object module, a ttk style
   dict, a `.qss` file, etc.
3. Transcribe every color value exactly as given in THEMES.md. Do not
   invent, round, or "improve" any value, and do not adjust contrast — the
   theme is already designed to keep text legible.
4. Map every token in the theme (topBarBg, topBarHover, text, bg, bgHover,
   primaryAction, primaryActionHover, primaryActionText, accentGreen,
   accentRed, accentBlue) to the equivalent concept in this app's styling
   system. If a token doesn't have an obvious home in this framework, ask me
   rather than guessing.
5. Do NOT modify existing components, add a theme switcher, or wire this
   file into the app's markup/JSX/templates. Just produce the theme file —
   I'll decide separately how and when to consume it.

Theme: <THEME NAME>
```

## Scope, explained

- **One artifact, not a refactor.** The point of this prompt is to get a
  single, framework-native theme file out the other end — not to have the
  assistant touch every component that renders color. That keeps the change
  small enough to review at a glance, and keeps "apply a theme" separate
  from "roll a theme out across my UI," which is a bigger, riskier ask you
  should do deliberately, not as a side effect.
- **No color substitution.** If a value looks wrong for the framework (e.g.
  a framework that wants hex instead of `rgb()`), converting format is fine;
  changing the actual color is not.
- **Reference examples exist, but aren't a template.** `examples/reference/`
  has illustrative CSS/Tkinter output from an earlier prototype. It's useful
  for naming-convention ideas, but it is not authoritative and may not match
  `themes/THEMES.md` going forward — always trust THEMES.md over anything in
  `examples/`.

## If you're updating an already-applied theme

See `prompts/update-theme.md` instead — updating is a smaller, more targeted
operation than a first-time apply.
