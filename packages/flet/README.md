# visual-assault-flet

Loud, deliberately eye-searing themes as plain Python data for Flet apps.
This package has no dependency on `flet` itself — just color data — so it
stays correct regardless of which Flet version your app uses.

Generated from [`themes/THEMES.md`](../../themes/THEMES.md) by
[`scripts/generate_packages.py`](../../scripts/generate_packages.py). Don't
edit `visual_assault_flet/themes.py` by hand — edit `THEMES.md` and
regenerate.

## Usage

```python
import flet as ft
from visual_assault_flet import THEMES

theme = THEMES["retrowave"]

page.theme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=theme["primary"],
        background=theme["background"],
        surface=theme["background"],
        on_surface=theme["foreground"],
        error=theme["accentRed"],
    )
)
page.bgcolor = theme["background"]
```

Adjust the exact `ft.ColorScheme` fields you populate to whatever your Flet
version and app actually use — the dict just gives you the hex values,
it doesn't assume a particular Flet API shape.

Each theme is a dict keyed by a snake_case id (e.g. `"blue_oval"`,
`"retrowave"`) with hex color values: `name`, `background`,
`backgroundHover`, `foreground`, `topBarBackground`, `topBarHover`,
`primary`, `primaryHover`, `accentGreen`, `accentRed`, `accentBlue`.

See [`themes/THEMES.md`](../../themes/THEMES.md) for the full list of
themes and what each token means.
