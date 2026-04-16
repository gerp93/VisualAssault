"""Visual Assault Theme System - Core Library."""

__version__ = "1.0.0"
__author__ = "Grantford Barnes"

from src.theme import Theme, Colors, Typography, Metadata
from src.validators import (
    validate_theme_completeness,
    check_contrast_compliance,
    calculate_contrast_ratio
)

__all__ = [
    'Theme',
    'Colors',
    'Typography',
    'Metadata',
    'validate_theme_completeness',
    'check_contrast_compliance',
    'calculate_contrast_ratio',
]
