"""Theme validation utilities."""
import re
from typing import List, Tuple
from src.theme import Theme


def validate_color_format(color: str) -> bool:
    """
    Validate that a color is in rgb() format.
    
    Args:
        color: Color string to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not color or color == "null":
        return True  # Allow null/empty for optional colors
    
    # Match rgb(r, g, b) format
    pattern = r'^rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)$'
    return bool(re.match(pattern, color))


def validate_theme_completeness(theme: Theme) -> Tuple[bool, List[str]]:
    """
    Validate that a theme has all required color properties.
    
    Args:
        theme: Theme object to validate
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    # Check required fields
    required_fields = [
        'topBarBg', 'topBarHover', 'text', 'bg', 'bgHover',
        'primaryAction', 'primaryActionHover', 'accentGreen',
        'accentRed', 'accentBlue'
    ]
    
    for field in required_fields:
        value = getattr(theme.colors, field, None)
        if not value:
            errors.append(f"Missing required color: {field}")
        elif not validate_color_format(value):
            errors.append(f"Invalid color format for {field}: {value}")
    
    # Validate optional primaryActionText
    if theme.colors.primaryActionText and not validate_color_format(theme.colors.primaryActionText):
        errors.append(f"Invalid color format for primaryActionText: {theme.colors.primaryActionText}")
    
    # Check ID format (kebab-case)
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', theme.id):
        errors.append(f"Invalid theme ID format: {theme.id} (must be kebab-case)")
    
    # Check category
    if theme.category not in ['base', 'crazy']:
        errors.append(f"Invalid category: {theme.category} (must be 'base' or 'crazy')")
    
    return len(errors) == 0, errors


def parse_rgb(color: str) -> Tuple[int, int, int]:
    """
    Parse an RGB color string into components.
    
    Args:
        color: Color string in format 'rgb(r, g, b)'
        
    Returns:
        Tuple of (r, g, b) values
    """
    match = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color)
    if match:
        return int(match.group(1)), int(match.group(2)), int(match.group(3))
    return 0, 0, 0


def calculate_relative_luminance(r: int, g: int, b: int) -> float:
    """
    Calculate relative luminance for contrast ratio.
    
    Args:
        r, g, b: RGB color components (0-255)
        
    Returns:
        Relative luminance value
    """
    def adjust(channel):
        channel = channel / 255.0
        if channel <= 0.03928:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4
    
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)


def calculate_contrast_ratio(color1: str, color2: str) -> float:
    """
    Calculate WCAG contrast ratio between two colors.
    
    Args:
        color1: First color in rgb() format
        color2: Second color in rgb() format
        
    Returns:
        Contrast ratio (1-21)
    """
    r1, g1, b1 = parse_rgb(color1)
    r2, g2, b2 = parse_rgb(color2)
    
    l1 = calculate_relative_luminance(r1, g1, b1)
    l2 = calculate_relative_luminance(r2, g2, b2)
    
    lighter = max(l1, l2)
    darker = min(l1, l2)
    
    return (lighter + 0.05) / (darker + 0.05)


def check_contrast_compliance(theme: Theme) -> Tuple[bool, List[str]]:
    """
    Check if theme meets WCAG AA contrast requirements.
    
    Args:
        theme: Theme to check
        
    Returns:
        Tuple of (is_compliant, list_of_warnings)
    """
    warnings = []
    
    # Check text/background contrast (should be >= 4.5:1 for normal text)
    text_bg_ratio = calculate_contrast_ratio(theme.colors.text, theme.colors.bg)
    if text_bg_ratio < 4.5:
        warnings.append(
            f"Text/background contrast ratio {text_bg_ratio:.2f}:1 is below WCAG AA minimum (4.5:1)"
        )
    
    # Check primary action button contrast
    action_ratio = calculate_contrast_ratio(theme.colors.text, theme.colors.primaryAction)
    if action_ratio < 4.5:
        warnings.append(
            f"Primary action contrast ratio {action_ratio:.2f}:1 is below WCAG AA minimum (4.5:1)"
        )
    
    return len(warnings) == 0, warnings
