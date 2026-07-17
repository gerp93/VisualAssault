# visual-assault-tkinter

Loud, deliberately eye-searing themes as plain Python data for Tkinter/ttk
apps. No dependencies beyond the standard library.

Generated from [`themes/THEMES.md`](../../themes/THEMES.md) by
[`scripts/generate_packages.py`](../../scripts/generate_packages.py). Don't
edit `visual_assault_tkinter/themes.py` by hand — edit `THEMES.md` and
regenerate.

## Usage

```python
from visual_assault_tkinter import THEMES

theme = THEMES["retrowave"]

root.configure(background=theme["background"])
style = ttk.Style()
style.configure("TButton", background=theme["buttonBackground"], foreground=theme["foreground"])
style.map("TButton", background=[("active", theme["buttonHover"])])
```

Each theme is a dict keyed by a snake_case id (e.g. `"blue_oval"`,
`"retrowave"`) with hex color values: `name`, `background`,
`backgroundHover`, `foreground`, `topBarBackground`, `topBarHover`,
`buttonBackground`, `buttonHover`, `accentGreen`, `accentRed`,
`accentBlue`.

See [`themes/THEMES.md`](../../themes/THEMES.md) for the full list of
themes and what each token means.
