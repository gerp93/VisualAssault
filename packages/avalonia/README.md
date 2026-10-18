# visual-assault-avalonia

Loud, deliberately eye-searing themes for [Avalonia](https://avaloniaui.net/)
desktop apps (C#). Plain source files — no runtime dependency beyond Avalonia
itself, no build step, **not published to NuGet**. You copy the
`VisualAssault/` folder into your app, pinned to a release tag.

Generated from [`themes/THEMES.md`](../../themes/THEMES.md) by
[`scripts/generate_packages.py`](../../scripts/generate_packages.py). Don't
edit `Themes.cs` or `FluentMapping.cs` by hand — edit `THEMES.md` (or the
mapping table in the generator) and regenerate.

## What's in `VisualAssault/`

| File | |
|---|---|
| `Themes.cs` | Generated. `VisualAssaultThemes.All` / `Find(id)`; each `VaTheme` has the 15 tokens as Avalonia `Color`s via `theme[VaToken.Bg]`. |
| `FluentMapping.cs` | Generated. Which Avalonia Fluent resource keys each token overrides (about 200). |
| `ThemeManager.cs` | Hand-maintained (written once, never overwritten). `ThemeManager.Apply(id)` switches themes live. |

Theme ids are `snake_case` (`blue_oval`, `retrowave`), the same as the
Tkinter and Flet packages, so a saved theme preference means the same thing in
every stack. `primaryActionText: null` is resolved to the theme's `text`
color, as the token reference defines it.

## Usage

Add the Fluent theme as usual, then apply a VisualAssault theme once Avalonia
has initialized (and again whenever the user picks another):

```csharp
// App.axaml.cs
public override void OnFrameworkInitializationCompleted()
{
    ThemeManager.Apply("retrowave");   // or a saved preference
    base.OnFrameworkInitializationCompleted();
}
```

```xml
<!-- App.axaml -->
<Application.Styles>
  <FluentTheme />
</Application.Styles>
```

Stock controls (buttons, text boxes, combo boxes, check boxes, list and tree
items, tabs, scroll bars, sliders, toggle switches, tooltips, menus) pick the
theme up with no per-control styling. For your own XAML, every token is also
published as `Va<Token>Color` and `Va<Token>Brush`:

```xml
<Border Background="{DynamicResource VaSurfaceBrush}"
        BorderBrush="{DynamicResource VaBorderBrush}">
  <TextBlock Foreground="{DynamicResource VaTextMutedBrush}" Text="Hello" />
</Border>
```

Use `DynamicResource` (not `StaticResource`) so live theme switching updates
the control.

Things worth knowing:

- **Primary action button:** a plain `Button` uses `surface`/`border`/`text`;
  `<Button Classes="accent">` is the primary action (`primaryAction`,
  `primaryActionHover`, `primaryActionText`).
- **Dark vs light:** `ThemeManager` sets `RequestedThemeVariant` from the
  background's luminance, so any control this package doesn't map still gets
  legible Fluent defaults.
- **Unmapped controls:** DataGrid, Calendar/DatePicker/TimePicker, Expander and
  others are not themed yet. If you hit one, add its keys to
  `AVALONIA_FLUENT_MAP` in `scripts/generate_packages.py`, regenerate, run the
  verification below, and release — don't patch a vendored copy in your app.
- `ThemeManager.Apply` needs a running `Application` (it throws otherwise).

## Verifying

```bash
dotnet run --project packages/avalonia/verify
```

Headless (no display needed). It checks that every mapped key exists in the
real Fluent theme, in both the Dark and Light variants and with the kind we
emit (Color vs brush — you can't tell from a key's name), then renders real
controls under all 14 themes and compares pixels to the expected tokens, and
confirms live switching doesn't accumulate resources. Exit code 1 on any
failure. Run it after changing the generator or bumping the Avalonia version.

Verified against **Avalonia 12.1.4** on **.NET 10**.
