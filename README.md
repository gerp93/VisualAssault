# Visual Assault Theme System

**A unified, cross-platform design token system for managing themes across CSS, Tkinter, Flet, and Flask applications.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Visual Assault is a centralized theme management system designed to keep design tokens (colors, typography, spacing) synchronized across multiple frameworks and platforms. Instead of maintaining themes separately in each project, Visual Assault provides a single source of truth that generates theme outputs for any framework.

## Features

✅ **Single source of truth** — Edit once, deploy everywhere  
✅ **Consistency** — No more out-of-sync themes  
✅ **Scalability** — Add new frameworks without duplicating effort  
✅ **Validation** — Automated quality & completeness checks  
✅ **Collaboration** — Clear theme spec for contributors  
✅ **WCAG Compliance** — Contrast checking built-in

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/gerp93/VisualAssault.git
cd VisualAssault

# Install Python dependencies (Python 3.7+)
pip install -r requirements.txt
```

### Generate Themes

```bash
# Generate all theme outputs
python generators/generate_all.py

# Or generate CSS only
python generators/generate_css.py
```

### Validate Themes

```bash
# Run all validation tests
python tests/test_theme_completeness.py
python tests/test_generators.py
```

## Project Structure

```
visual-assault-themes/
├── themes/              # Theme definitions (JSON)
│   ├── base/           # Reserved for future shared/base themes
│   ├── crazy/          # Visually assaulting themes (current set)
│   │   ├── bubblegum.json
│   │   ├── neon.json
│   │   └── ...
│   └── schema.json     # JSON Schema validation
├── generators/         # Theme generators
│   ├── generate_css.py
│   ├── generate_tkinter.py
│   ├── generate_all.py
│   └── (future: flet, flask)
├── src/                # Core library
│   ├── theme.py       # Theme dataclass
│   └── validators.py  # Validation utilities
├── output/             # Generated outputs
│   ├── css/
│   │   └── colors.css
│   ├── tkinter/
│   │   └── themes.json
│   └── (future: flet, flask)
├── tests/              # Test suite
│   ├── test_theme_completeness.py
│   └── test_generators.py
└── .github/workflows/  # CI/CD (future)
```

## Available Themes

### Current Themes (14)

| Theme | Description | WCAG AA |
|-------|-------------|---------|
| Bubblegum | Hot pink explosion | ⚠️ |
| Electric Lime | Bright green-yellow blast | ⚠️ |
| Neon | High-contrast neon dark mode | ⚠️ |
| Commander Keen | Retro DOS palette | ⚠️ |
| Lava | Fiery red-hot palette | ⚠️ |
| Hacker | Matrix-style green on black | ⚠️ |
| Hawkeye | Black and old-gold palette | ⚠️ |
| Green Acres | Farm-green and yellow palette | ⚠️ |
| Red Barn | Barn red with bright accents | ⚠️ |
| Flambeau | Warm orange and ember tones | ⚠️ |
| Flambeau Inverse | Inverse Flambeau palette | ⚠️ |
| Blue Oval | Deep blue high-contrast palette | ⚠️ |
| Merica | Red/white/blue palette | ⚠️ |
| Retrowave | 80s synthwave palette | ⚠️ |

## Usage

### Using Generated CSS

```html
<!-- Include the generated CSS -->
<link rel="stylesheet" href="output/css/colors.css">

<!-- Apply a theme to the body -->
<body class="neon-theme">
    <div id="top-bar">My App</div>
    <button>Primary Action</button>
</body>
```

### Creating a New Theme

1. Create a new JSON file in `themes/base/` or `themes/crazy/`
2. Follow the [Theme Specification](THEME_SPEC.md)
3. Run validation: `python tests/test_theme_completeness.py`
4. Generate outputs: `python generators/generate_all.py`

Example theme JSON:

```json
{
  "id": "my-theme",
  "name": "My Theme",
  "displayName": "🎨 My Theme",
  "description": "A custom theme",
  "category": "base",
  "colors": {
    "topBarBg": "rgb(50, 50, 50)",
    "topBarHover": "rgb(70, 70, 70)",
    "text": "rgb(255, 255, 255)",
    "bg": "rgb(34, 34, 34)",
    "bgHover": "rgb(54, 54, 54)",
    "primaryAction": "rgb(7, 72, 75)",
    "primaryActionHover": "rgb(8, 94, 99)",
    "primaryActionText": null,
    "accentGreen": "rgb(120, 255, 99)",
    "accentRed": "rgb(255, 100, 100)",
    "accentBlue": "rgb(130, 160, 255)"
  }
}
```

## Development

### Running Tests

```bash
# Test theme completeness
python tests/test_theme_completeness.py

# Test CSS generation
python tests/test_generators.py
```

### Adding a New Generator

1. Create `generators/generate_<framework>.py`
2. Implement generation logic following existing patterns
3. Add to `generators/generate_all.py`
4. Add tests in `tests/`

## Roadmap

### Phase 1 (MVP) - ✅ Complete
- [x] Repository structure
- [x] Extract 8 themes from CSS to JSON
- [x] JSON schema validation
- [x] Theme dataclass (theme.py)
- [x] CSS generator
- [x] Master orchestrator
- [x] Validation tests
- [x] Documentation

### Phase 2 (In Progress)
- [x] Tkinter generator
- [ ] Flet generator
- [ ] Flask generator
- [x] Add "crazy" theme collection
- [x] Consolidate Tkinter mapping from KVG_Themes

### Phase 3 (Future)
- [ ] CI/CD validation & generation
- [ ] Automated sync to dependent repos
- [ ] Theme preview UI
- [ ] NPM/PyPI packages

## Contributing

See [CONTRIBUTOR_GUIDE.md](CONTRIBUTOR_GUIDE.md) for detailed contribution guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details

## Related Projects

- **CSS Themes**: [card-judge](https://github.com/gerp93/card-judge) — Web app themes
- **Tkinter Themes**: [KVG_Themes](https://github.com/gerp93/KVG_Themes) — Desktop app themes
- **Flet Themes**: [KVG_Themes_Flet](https://github.com/gerp93/KVG_Themes_Flet) — Flutter-based themes

## Credits

Created by Grantford Barnes as part of the Visual Assault design system initiative.
