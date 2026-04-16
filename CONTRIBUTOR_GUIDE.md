# Contributor Guide

Welcome to Visual Assault! This guide will help you contribute themes, generators, or improvements to the project.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Adding a New Theme](#adding-a-new-theme)
3. [Testing Your Theme](#testing-your-theme)
4. [Adding a Generator](#adding-a-generator)
5. [Code Style](#code-style)
6. [Submitting Changes](#submitting-changes)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- A text editor or IDE

### Setup

1. Fork the repository on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/VisualAssault.git
   cd VisualAssault
   ```

3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt  # when available
   ```

4. Create a feature branch:
   ```bash
   git checkout -b feature/my-new-theme
   ```

## Adding a New Theme

### Step 1: Choose Category

Decide whether your theme belongs in:
- **`themes/base/`**: Professional, production-ready themes
- **`themes/crazy/`**: Experimental, visually striking themes

### Step 2: Create Theme JSON

Create a new JSON file in the appropriate directory:

```bash
# For a base theme
touch themes/base/my-theme.json

# For a crazy theme
touch themes/crazy/my-theme.json
```

### Step 3: Define Your Theme

Follow the [Theme Specification](THEME_SPEC.md) to create your theme. Here's a template:

```json
{
  "id": "my-theme",
  "name": "My Theme",
  "displayName": "🎨 My Theme",
  "description": "A brief description of your theme",
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
  },
  "metadata": {
    "inspiration": "What inspired this theme?",
    "author": "Your Name",
    "createdAt": "2025-12-09",
    "wcagAACompliant": false
  }
}
```

### Step 4: Pick Good Colors

**Tips for choosing colors:**

1. **Start with a base color palette**
   - Pick 2-3 main colors that work well together
   - Use tools like [Coolors](https://coolors.co/) or [Adobe Color](https://color.adobe.com/)

2. **Ensure readability**
   - Text should be clearly visible on backgrounds
   - Aim for at least 4.5:1 contrast ratio (WCAG AA)
   - Test with contrast checkers

3. **Create visual hierarchy**
   - `topBarBg` should stand out from `bg`
   - Hover states should be noticeably different
   - Accents should pop without being overwhelming

4. **Test in context**
   - Generate the CSS and view it in a real application
   - Check all UI states (hover, active, disabled)

### Step 5: Color Conversion

If you have colors in other formats, convert them to RGB:

**Hex to RGB:**
```python
# Example: #FF5733 to rgb()
r = int('FF', 16)  # 255
g = int('57', 16)  # 87
b = int('33', 16)  # 51
# Result: rgb(255, 87, 51)
```

**Online tools:**
- [RapidTables RGB Converter](https://www.rapidtables.com/convert/color/hex-to-rgb.html)

## Testing Your Theme

### 1. Validate Theme Format

Run the completeness test to check for errors:

```bash
python tests/test_theme_completeness.py
```

Expected output:
```
✓ my-theme: Complete
✅ All themes are complete!
```

### 2. Check Contrast Ratios

```bash
python tests/test_theme_completeness.py
```

This will show warnings if your theme has poor contrast:
```
⚠️  Contrast warnings:
my-theme:
  ⚠️  Text/background contrast ratio 2.8:1 is below WCAG AA minimum (4.5:1)
```

**If you get warnings:**
- For professional themes: Fix the contrast issues
- For "crazy" themes: Acceptable to have warnings (set `wcagAACompliant: false`)

### 3. Generate CSS

```bash
python generators/generate_all.py
```

Expected output:
```
🎨 Visual Assault Theme Generator
==================================================
📝 Generating CSS themes...
✓ Generated CSS for 9 themes -> output/css/colors.css
==================================================
✅ All theme outputs generated successfully!
```

### 4. Test CSS Output

```bash
python tests/test_generators.py
```

### 5. Visual Testing

Create a simple HTML file to preview your theme:

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="output/css/colors.css">
    <style>
        body { padding: 20px; font-family: Arial, sans-serif; }
        #top-bar { padding: 10px; margin-bottom: 20px; }
        button { padding: 10px 20px; margin: 5px; border: none; cursor: pointer; }
        input, textarea { padding: 8px; margin: 5px; border: 1px solid #ccc; }
    </style>
</head>
<body class="my-theme-theme">
    <div id="top-bar">Top Bar</div>
    <h1>Theme Preview</h1>
    <p>This is regular text on the background.</p>
    <button>Primary Action</button>
    <input type="text" placeholder="Input field">
    <p style="color: var(--color-accent-green);">Success message</p>
    <p style="color: var(--color-accent-red);">Error message</p>
    <p><a href="#">Link color (accent blue)</a></p>
</body>
</html>
```

## Adding a Generator

Want to add support for a new framework (Tkinter, Flet, Flask)?

### 1. Create Generator File

```bash
touch generators/generate_<framework>.py
```

### 2. Implement Generator

Follow this template:

```python
"""Generate <framework> themes from JSON theme definitions."""
from pathlib import Path
from typing import List
from src.theme import Theme


def generate_<framework>(themes_dir: Path, output_dir: Path) -> None:
    """
    Generate <framework> theme files.
    
    Args:
        themes_dir: Directory containing theme JSON files
        output_dir: Output directory for generated files
    """
    themes = load_all_themes(themes_dir)
    
    # Your generation logic here
    
    print(f"✓ Generated <framework> for {len(themes)} themes -> {output_dir}")


def load_all_themes(themes_dir: Path) -> List[Theme]:
    """Load all themes from JSON files."""
    themes = []
    for subdir in ['base', 'crazy']:
        subdir_path = themes_dir / subdir
        if subdir_path.exists():
            for json_file in sorted(subdir_path.glob('*.json')):
                try:
                    theme = Theme.from_json(json_file)
                    themes.append(theme)
                except Exception as e:
                    print(f"Warning: Failed to load {json_file}: {e}")
    return themes


if __name__ == '__main__':
    # Run standalone
    repo_root = Path(__file__).parent.parent
    themes_dir = repo_root / 'themes'
    output_dir = repo_root / 'output' / '<framework>'
    generate_<framework>(themes_dir, output_dir)
```

### 3. Add to Master Generator

Edit `generators/generate_all.py`:

```python
from generators.generate_<framework> import generate_<framework>

# In generate_all() function:
print("\n🎯 Generating <framework> themes...")
generate_<framework>(themes_dir, repo_root / 'output' / '<framework>')
```

### 4. Add Tests

Create `tests/test_<framework>_generator.py`:

```python
"""Tests for <framework> generator."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.generate_<framework> import generate_<framework>


def test_<framework>_generation():
    """Test that <framework> files are generated correctly."""
    repo_root = Path(__file__).parent.parent
    themes_dir = repo_root / 'themes'
    output_dir = repo_root / 'output' / '<framework>'
    
    generate_<framework>(themes_dir, output_dir)
    
    # Add your validation checks here
    assert output_dir.exists()
    print("✅ <framework> generation successful!")
    return True


if __name__ == '__main__':
    if not test_<framework>_generation():
        sys.exit(1)
```

## Code Style

### Python
- Follow PEP 8 style guide
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

### JSON
- Use 2-space indentation
- Keep consistent field ordering
- Use lowercase for IDs (kebab-case)

### Comments
- Explain "why", not "what"
- Keep comments concise and relevant
- Update comments when code changes

## Submitting Changes

### 1. Test Everything

Before submitting, run all tests:

```bash
python tests/test_theme_completeness.py
python tests/test_generators.py
```

### 2. Commit Your Changes

```bash
git add .
git commit -m "Add my-theme theme"
```

**Good commit messages:**
- `Add hawkeye theme to crazy category`
- `Fix contrast ratio in purple theme`
- `Add Tkinter generator`
- `Update theme spec with spacing tokens`

### 3. Push to Your Fork

```bash
git push origin feature/my-new-theme
```

### 4. Create Pull Request

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill in the PR template:
   - **What**: What does this PR do?
   - **Why**: Why is this change needed?
   - **How**: How did you implement it?
   - **Testing**: How did you test it?

### 5. Respond to Feedback

- Be open to suggestions
- Make requested changes promptly
- Ask questions if something is unclear

## Getting Help

- **Questions?** Open a GitHub Discussion
- **Bugs?** Open a GitHub Issue
- **Ideas?** Open a GitHub Issue with "Enhancement" label

## Recognition

All contributors will be:
- Listed in the project README
- Credited in theme metadata (if you create themes)
- Part of the Visual Assault community!

Thank you for contributing! 🎨
