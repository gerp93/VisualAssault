# visual-assault-angular

Loud, deliberately eye-searing themes for Angular apps. No required
dependencies, no Angular build tooling of its own — just an SCSS partial
and a typed constant.

This works identically whether your Angular app runs in a browser tab or
is wrapped in Electron/Tauri as a desktop app — the theme is just CSS
custom properties on a class; the desktop shell around it doesn't matter.

Generated from [`themes/THEMES.md`](../../themes/THEMES.md) by
[`scripts/generate_packages.py`](../../scripts/generate_packages.py). Don't
edit `themes.scss` or `theme-names.ts` by hand — edit `THEMES.md` and
regenerate.

## Usage

In your global styles (e.g. `styles.scss`):

```scss
@import 'visual-assault-angular/themes';
```

Then apply a theme class to your root element, e.g. in `app.component.ts`:

```ts
import { THEME_NAMES, ThemeName } from 'visual-assault-angular/theme-names';

@HostBinding('class')
themeClass: string = `theme-${THEME_NAMES[0] as ThemeName}`;
```

Each theme applies via a `.theme-<theme-id>` class and sets these custom
properties: `--color-top-bar-bg`, `--color-top-bar-hover`, `--color-text`,
`--color-bg`, `--color-bg-hover`, `--color-primary-action`,
`--color-primary-action-hover`, `--color-primary-action-text` (only present
when a theme overrides it), `--color-accent-green`, `--color-accent-red`,
`--color-accent-blue`, `--color-surface`, `--color-border`,
`--color-text-muted`, `--color-accent-muted`.

See [`themes/THEMES.md`](../../themes/THEMES.md) for the full list of
themes and what each token means.
