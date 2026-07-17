# visual-assault-css

Loud, deliberately eye-searing themes as plain CSS custom properties. No
runtime dependencies, no build step — just a stylesheet.

Generated from [`themes/THEMES.md`](../../themes/THEMES.md) by
[`scripts/generate_packages.py`](../../scripts/generate_packages.py). Don't
edit `themes.css` by hand — edit `THEMES.md` and regenerate.

## Usage

```html
<link rel="stylesheet" href="node_modules/visual-assault-css/themes.css">
<body class="retrowave-theme">
```

Each theme applies via a `body.<theme-id>-theme` class and sets these
custom properties: `--color-top-bar-bg`, `--color-top-bar-hover`,
`--color-text`, `--color-bg`, `--color-bg-hover`, `--color-primary-action`,
`--color-primary-action-hover`, `--color-primary-action-text` (only present
when a theme overrides it), `--color-accent-green`, `--color-accent-red`,
`--color-accent-blue`. Wire your own CSS to them:

```css
body {
  color: var(--color-text);
  background: var(--color-bg);
}
```

See [`themes/THEMES.md`](../../themes/THEMES.md) for the full list of
themes and what each token means.
