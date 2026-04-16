"""Visual Assault Theme data structures and parsing."""
from dataclasses import dataclass, field
from typing import Optional
import json
from pathlib import Path


@dataclass
class Colors:
    """Theme color definitions."""
    topBarBg: str
    topBarHover: str
    text: str
    bg: str
    bgHover: str
    primaryAction: str
    primaryActionHover: str
    primaryActionText: Optional[str] = None
    accentGreen: str = ""
    accentRed: str = ""
    accentBlue: str = ""


@dataclass
class Typography:
    """Typography settings for the theme."""
    fontFamily: str = "'Arial', 'Helvetica', sans-serif"
    fontFamilyMono: str = "'Consolas', 'Courier New', monospace"
    fontSizeBase: str = "16px"
    fontWeightNormal: int = 400
    fontWeightBold: int = 700


@dataclass
class Metadata:
    """Theme metadata."""
    inspiration: str = ""
    author: str = ""
    createdAt: str = ""
    wcagAACompliant: bool = False


@dataclass
class Theme:
    """Complete theme definition."""
    id: str
    name: str
    displayName: str
    category: str
    colors: Colors
    description: str = ""
    typography: Optional[Typography] = None
    metadata: Optional[Metadata] = None

    @classmethod
    def from_json(cls, json_path: Path) -> "Theme":
        """Load theme from JSON file."""
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        colors = Colors(**data['colors'])
        typography = Typography(**data.get('typography', {})) if 'typography' in data else None
        metadata = Metadata(**data.get('metadata', {})) if 'metadata' in data else None
        
        return cls(
            id=data['id'],
            name=data['name'],
            displayName=data['displayName'],
            category=data['category'],
            colors=colors,
            description=data.get('description', ''),
            typography=typography,
            metadata=metadata
        )

    def to_dict(self) -> dict:
        """Convert theme to dictionary."""
        result = {
            'id': self.id,
            'name': self.name,
            'displayName': self.displayName,
            'category': self.category,
            'colors': {
                'topBarBg': self.colors.topBarBg,
                'topBarHover': self.colors.topBarHover,
                'text': self.colors.text,
                'bg': self.colors.bg,
                'bgHover': self.colors.bgHover,
                'primaryAction': self.colors.primaryAction,
                'primaryActionHover': self.colors.primaryActionHover,
                'primaryActionText': self.colors.primaryActionText,
                'accentGreen': self.colors.accentGreen,
                'accentRed': self.colors.accentRed,
                'accentBlue': self.colors.accentBlue,
            }
        }
        
        if self.description:
            result['description'] = self.description
        
        if self.typography:
            result['typography'] = {
                'fontFamily': self.typography.fontFamily,
                'fontFamilyMono': self.typography.fontFamilyMono,
                'fontSizeBase': self.typography.fontSizeBase,
                'fontWeightNormal': self.typography.fontWeightNormal,
                'fontWeightBold': self.typography.fontWeightBold,
            }
        
        if self.metadata:
            result['metadata'] = {
                'inspiration': self.metadata.inspiration,
                'author': self.metadata.author,
                'createdAt': self.metadata.createdAt,
                'wcagAACompliant': self.metadata.wcagAACompliant,
            }
        
        return result
