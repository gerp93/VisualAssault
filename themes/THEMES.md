# Visual Assault Themes

This file is the **single source of truth** for every Visual Assault theme.
There is no JSON schema, generator, or build step behind it — an AI
assistant reads this file directly and transcribes a theme's values into
whatever styling mechanism a target app uses (CSS custom properties, a
Tailwind config, a JS theme object, Tkinter ttk styles, a Qt stylesheet,
etc.).

If you're applying a theme to an app, see `prompts/apply-theme.md` (or the
Quick Start block in the root `README.md`) rather than doing it by hand.

## Rules for anyone (human or AI) using this file

- **Transcribe values exactly.** Every color below is authoritative. Never
  substitute a "close enough" color, round a value, or invent one that isn't
  present in a theme's block.
- **Don't "fix" contrast.** These themes are already designed to keep text
  legible against its background. If a token pairing looks unusual, that's
  intentional — leave it alone.
- **Don't add tokens that aren't there.** If a theme doesn't define an
  optional field, don't invent a value for it.

## Design philosophy

Visual Assault themes are **not** meant to be unreadable, low-contrast, or
broken. Every theme keeps text legible against its background — that's a
hard requirement, not a nice-to-have.

What makes a theme "visual assault" is the *nature and combination* of the
colors themselves: bright neons, harsh or clashing hues, jarring pairings
that are perfectly readable but hard to stare at for long. Think "loud,"
not "broken."

Not every theme in this set has to be abrasive, either. A handful lean more
"striking and cohesive" than "harsh," and that's expected — this is a
library of bold, opinionated palettes, not a mandate that everything has to
be ugly on purpose.

## Color format

All colors are expressed as `rgb(r, g, b)` — consistent, unambiguous, and
trivially convertible to hex or any other format a target framework needs.

## Token reference

| Token | Drives |
|---|---|
| `topBarBg` | Background of the app's top navigation/header bar |
| `topBarHover` | Hover state for elements in the top bar |
| `text` | Primary body text color |
| `bg` | Main page/app background |
| `bgHover` | Background for hover states (e.g. table rows, list items) |
| `primaryAction` | Background of primary action buttons |
| `primaryActionHover` | Hover state for primary action buttons |
| `primaryActionText` | Text color on primary action buttons; `null` means reuse `text` |
| `accentGreen` | Success/positive states |
| `accentRed` | Error/danger states |
| `accentBlue` | Informational/link states |

## Themes

### Blue Oval

Deep blue, high-contrast palette.

```
topBarBg:            rgb(13, 71, 161)
topBarHover:          rgb(25, 100, 200)
text:                 rgb(255, 255, 255)
bg:                   rgb(13, 71, 161)
bgHover:              rgb(10, 55, 130)
primaryAction:        rgb(70, 80, 90)
primaryActionHover:   rgb(90, 100, 110)
primaryActionText:    null
accentGreen:          rgb(200, 210, 220)
accentRed:            rgb(255, 150, 150)
accentBlue:           rgb(150, 200, 255)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Bubblegum

Hot pink explosion.

```
topBarBg:            rgb(204, 0, 102)
topBarHover:          rgb(170, 40, 170)
text:                 rgb(255, 255, 255)
bg:                   rgb(255, 105, 180)
bgHover:              rgb(255, 182, 193)
primaryAction:        rgb(153, 50, 204)
primaryActionHover:   rgb(187, 51, 187)
primaryActionText:    null
accentGreen:          rgb(255, 255, 0)
accentRed:            rgb(204, 0, 102)
accentBlue:           rgb(135, 206, 235)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Commander Keen

Retro DOS EGA/VGA palette.

```
topBarBg:            rgb(85, 85, 255)
topBarHover:          rgb(85, 255, 255)
text:                 rgb(255, 255, 85)
bg:                   rgb(0, 0, 170)
bgHover:              rgb(0, 0, 0)
primaryAction:        rgb(85, 85, 255)
primaryActionHover:   rgb(0, 170, 170)
primaryActionText:    null
accentGreen:          rgb(85, 255, 85)
accentRed:            rgb(170, 0, 170)
accentBlue:           rgb(85, 255, 255)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Electric Lime

Bright green-yellow blast.

```
topBarBg:            rgb(136, 170, 0)
topBarHover:          rgb(74, 0, 128)
text:                 rgb(10, 10, 10)
bg:                   rgb(204, 255, 0)
bgHover:              rgb(238, 255, 170)
primaryAction:        rgb(74, 0, 128)
primaryActionHover:   rgb(119, 0, 255)
primaryActionText:    null
accentGreen:          rgb(136, 170, 0)
accentRed:            rgb(255, 0, 170)
accentBlue:           rgb(0, 102, 255)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Flambeau

Warm orange and ember tones.

```
topBarBg:            rgb(195, 46, 11)
topBarHover:          rgb(220, 70, 30)
text:                 rgb(0, 0, 0)
bg:                   rgb(255, 189, 123)
bgHover:              rgb(195, 170, 140)
primaryAction:        rgb(195, 46, 11)
primaryActionHover:   rgb(220, 70, 30)
primaryActionText:    null
accentGreen:          rgb(0, 100, 0)
accentRed:            rgb(195, 46, 11)
accentBlue:           rgb(100, 60, 20)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Flambeau Inverse

Inverse of Flambeau — dark ember background, light text.

```
topBarBg:            rgb(160, 35, 8)
topBarHover:          rgb(130, 25, 5)
text:                 rgb(255, 255, 255)
bg:                   rgb(195, 46, 11)
bgHover:              rgb(160, 35, 8)
primaryAction:        rgb(120, 80, 40)
primaryActionHover:   rgb(160, 110, 60)
primaryActionText:    null
accentGreen:          rgb(255, 230, 180)
accentRed:            rgb(255, 255, 255)
accentBlue:           rgb(255, 189, 123)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Green Acres

Farm-green and yellow palette.

```
topBarBg:            rgb(54, 124, 43)
topBarHover:          rgb(70, 150, 55)
text:                 rgb(255, 222, 0)
bg:                   rgb(54, 124, 43)
bgHover:              rgb(40, 100, 30)
primaryAction:        rgb(30, 70, 25)
primaryActionHover:   rgb(40, 90, 32)
primaryActionText:    null
accentGreen:          rgb(255, 222, 0)
accentRed:            rgb(255, 180, 0)
accentBlue:           rgb(200, 255, 150)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Hacker

Matrix-style green on black.

```
topBarBg:            rgb(0, 26, 0)
topBarHover:          rgb(0, 51, 0)
text:                 rgb(0, 255, 0)
bg:                   rgb(13, 13, 13)
bgHover:              rgb(0, 17, 0)
primaryAction:        rgb(0, 26, 0)
primaryActionHover:   rgb(0, 51, 0)
primaryActionText:    null
accentGreen:          rgb(0, 255, 65)
accentRed:            rgb(255, 191, 0)
accentBlue:           rgb(50, 205, 50)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Hawkeye

Black and old-gold palette.

```
topBarBg:            rgb(0, 0, 0)
topBarHover:          rgb(40, 40, 0)
text:                 rgb(255, 205, 0)
bg:                   rgb(0, 0, 0)
bgHover:              rgb(30, 25, 0)
primaryAction:        rgb(40, 40, 40)
primaryActionHover:   rgb(60, 60, 60)
primaryActionText:    null
accentGreen:          rgb(255, 205, 0)
accentRed:            rgb(255, 150, 0)
accentBlue:           rgb(255, 230, 100)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Lava

Fiery red-hot palette.

```
topBarBg:            rgb(51, 0, 0)
topBarHover:          rgb(77, 0, 0)
text:                 rgb(255, 255, 255)
bg:                   rgb(204, 0, 0)
bgHover:              rgb(26, 0, 0)
primaryAction:        rgb(51, 0, 0)
primaryActionHover:   rgb(102, 0, 0)
primaryActionText:    null
accentGreen:          rgb(255, 204, 0)
accentRed:            rgb(255, 51, 0)
accentBlue:           rgb(255, 102, 0)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Merica

Red/white/blue palette.

```
topBarBg:            rgb(191, 10, 48)
topBarHover:          rgb(220, 40, 70)
text:                 rgb(255, 255, 255)
bg:                   rgb(0, 40, 104)
bgHover:              rgb(0, 30, 80)
primaryAction:        rgb(191, 10, 48)
primaryActionHover:   rgb(220, 40, 70)
primaryActionText:    null
accentGreen:          rgb(255, 255, 255)
accentRed:            rgb(191, 10, 48)
accentBlue:           rgb(100, 180, 255)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Neon

High-contrast neon dark mode.

```
topBarBg:            rgb(26, 0, 51)
topBarHover:          rgb(51, 0, 102)
text:                 rgb(0, 255, 255)
bg:                   rgb(10, 10, 10)
bgHover:              rgb(13, 13, 26)
primaryAction:        rgb(51, 0, 51)
primaryActionHover:   rgb(102, 0, 102)
primaryActionText:    null
accentGreen:          rgb(57, 255, 20)
accentRed:            rgb(255, 20, 147)
accentBlue:           rgb(125, 249, 255)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Red Barn

Barn red with bright accents.

```
topBarBg:            rgb(198, 12, 48)
topBarHover:          rgb(230, 40, 70)
text:                 rgb(255, 255, 255)
bg:                   rgb(198, 12, 48)
bgHover:              rgb(160, 10, 35)
primaryAction:        rgb(0, 0, 0)
primaryActionHover:   rgb(40, 40, 40)
primaryActionText:    null
accentGreen:          rgb(255, 220, 100)
accentRed:            rgb(255, 255, 255)
accentBlue:           rgb(255, 180, 180)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16

### Retrowave

80s synthwave palette.

```
topBarBg:            rgb(45, 27, 78)
topBarHover:          rgb(74, 44, 122)
text:                 rgb(255, 107, 157)
bg:                   rgb(26, 10, 46)
bgHover:              rgb(61, 31, 92)
primaryAction:        rgb(61, 31, 92)
primaryActionHover:   rgb(92, 45, 138)
primaryActionText:    null
accentGreen:          rgb(255, 217, 61)
accentRed:            rgb(224, 64, 251)
accentBlue:           rgb(199, 125, 255)
```
inspiration: card-judge theme set · author: Grantford Barnes · createdAt: 2026-04-16
