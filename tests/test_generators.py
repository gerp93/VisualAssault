"""Tests for CSS generator."""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.generate_css import generate_css


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
    expected_themes = [
        'dark-theme', 'light-theme', 'nord-polar-night-theme',
        'dracula-theme', 'purple-theme', 'tokyo-night-dark-theme',
        'gruvbox-dark-theme', 'gruvbox-light-theme'
    ]
    
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


if __name__ == '__main__':
    print("=" * 50)
    print("Testing CSS Generator")
    print("=" * 50)
    
    if not test_css_generation():
        sys.exit(1)
