"""Tests for CSS generator."""
import sys
from pathlib import Path
import json

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.generate_css import generate_css
from generators.generate_tkinter import generate_tkinter


def test_css_generation():
    """Test that CSS is generated correctly."""
    repo_root = Path(__file__).parent.parent
    themes_dir = repo_root / 'themes'
    output_file = repo_root / 'output' / 'css' / 'colors.css'
    
    print("Generating CSS...")
    generate_css(themes_dir, output_file)
    
    # Verify output file exists
    if not output_file.exists():
        print("❌ CSS file was not generated")
        return False
    
    # Read and validate content
    with open(output_file, 'r') as f:
        content = f.read()
    
    # Check that all expected themes are present
    expected_themes = []
    themes_root = repo_root / 'themes'
    for subdir in ['base', 'crazy']:
        subdir_path = themes_root / subdir
        if not subdir_path.exists():
            continue
        for json_file in sorted(subdir_path.glob('*.json')):
            theme_id = json.loads(json_file.read_text())['id']
            expected_themes.append(f'{theme_id}-theme')
    
    missing_themes = []
    for theme in expected_themes:
        if f'body.{theme}' not in content:
            missing_themes.append(theme)
    
    if missing_themes:
        print(f"❌ Missing themes in CSS: {', '.join(missing_themes)}")
        return False
    
    # Check that common CSS rules are present
    required_rules = [
        'body {', '#top-bar {', 'button {', 'button:hover {'
    ]
    
    missing_rules = []
    for rule in required_rules:
        if rule not in content:
            missing_rules.append(rule)
    
    if missing_rules:
        print(f"❌ Missing CSS rules: {', '.join(missing_rules)}")
        return False
    
    print(f"✅ CSS generation successful!")
    print(f"   - Generated {len(expected_themes)} themes")
    print(f"   - Output: {output_file}")
    print(f"   - Size: {len(content)} bytes")
    
    return True


def test_tkinter_generation():
    """Test that Tkinter theme output is generated correctly."""
    repo_root = Path(__file__).parent.parent
    themes_dir = repo_root / 'themes'
    output_dir = repo_root / 'output' / 'tkinter'
    output_file = output_dir / 'themes.json'

    print("Generating Tkinter themes...")
    generate_tkinter(themes_dir, output_dir)

    if not output_file.exists():
        print("❌ Tkinter themes.json was not generated")
        return False

    payload = json.loads(output_file.read_text())
    if 'themes' not in payload:
        print("❌ Tkinter themes.json missing 'themes' key")
        return False

    theme_count = len(payload['themes'])
    if theme_count == 0:
        print("❌ Tkinter themes.json has no themes")
        return False

    required_keys = [
        'background', 'foreground', 'buttonBackground', 'buttonHover',
        'accentGreen', 'accentRed', 'accentBlue', 'tkinterId'
    ]
    first_theme = next(iter(payload['themes'].values()))
    missing_keys = [k for k in required_keys if k not in first_theme]
    if missing_keys:
        print(f"❌ Tkinter theme entries missing keys: {', '.join(missing_keys)}")
        return False

    print("✅ Tkinter generation successful!")
    print(f"   - Generated {theme_count} themes")
    print(f"   - Output: {output_file}")
    return True


if __name__ == '__main__':
    print("=" * 50)
    print("Testing CSS Generator")
    print("=" * 50)
    
    css_ok = test_css_generation()
    tkinter_ok = test_tkinter_generation()
    if not css_ok or not tkinter_ok:
        sys.exit(1)
