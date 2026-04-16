"""Tests for theme completeness and validation."""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.theme import Theme
from src.validators import validate_theme_completeness, check_contrast_compliance


def test_theme_completeness():
    """Test that all themes have required fields."""
    themes_dir = Path(__file__).parent.parent / 'themes'
    errors = []
    
    for subdir in ['base', 'crazy']:
        subdir_path = themes_dir / subdir
        if not subdir_path.exists():
            continue
            
        for json_file in sorted(subdir_path.glob('*.json')):
            try:
                theme = Theme.from_json(json_file)
                is_valid, validation_errors = validate_theme_completeness(theme)
                
                if not is_valid:
                    errors.append(f"\n{json_file.name}:")
                    for error in validation_errors:
                        errors.append(f"  - {error}")
                else:
                    print(f"✓ {theme.id}: Complete")
                    
            except Exception as e:
                errors.append(f"\n{json_file.name}: Failed to load - {e}")
    
    if errors:
        print("\n❌ Theme completeness errors:")
        for error in errors:
            print(error)
        return False
    else:
        print("\n✅ All themes are complete!")
        return True


def test_contrast():
    """Test contrast ratios for all themes."""
    themes_dir = Path(__file__).parent.parent / 'themes'
    warnings = []
    
    for subdir in ['base', 'crazy']:
        subdir_path = themes_dir / subdir
        if not subdir_path.exists():
            continue
            
        for json_file in sorted(subdir_path.glob('*.json')):
            try:
                theme = Theme.from_json(json_file)
                is_compliant, contrast_warnings = check_contrast_compliance(theme)
                
                if not is_compliant:
                    warnings.append(f"\n{theme.id}:")
                    for warning in contrast_warnings:
                        warnings.append(f"  ⚠️  {warning}")
                else:
                    print(f"✓ {theme.id}: WCAG AA compliant")
                    
            except Exception as e:
                warnings.append(f"\n{json_file.name}: Failed to check - {e}")
    
    if warnings:
        print("\n⚠️  Contrast warnings:")
        for warning in warnings:
            print(warning)
    else:
        print("\n✅ All themes meet WCAG AA standards!")
    
    return True


if __name__ == '__main__':
    print("=" * 50)
    print("Testing Theme Completeness")
    print("=" * 50)
    completeness_passed = test_theme_completeness()
    
    print("\n" + "=" * 50)
    print("Testing Contrast Ratios")
    print("=" * 50)
    contrast_passed = test_contrast()
    
    if not completeness_passed:
        sys.exit(1)
