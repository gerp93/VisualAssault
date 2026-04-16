"""Generate Tkinter theme output from JSON theme definitions."""
import json
import re
from pathlib import Path
from typing import Dict

from generators.generate_css import load_all_themes


def _rgb_to_hex(rgb: str) -> str:
    """Convert rgb(r, g, b) to #rrggbb."""
    match = re.match(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", rgb)
    if not match:
        raise ValueError(f"Invalid RGB value: {rgb}")
    r, g, b = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return f"#{r:02x}{g:02x}{b:02x}"


def _theme_to_tkinter_config(theme) -> Dict[str, str]:
    """Map VisualAssault theme colors to Tkinter-friendly tokens."""
    colors = theme.colors
    return {
        "tkinterId": theme.id.replace("-", "_"),
        "name": theme.name,
        "background": _rgb_to_hex(colors.bg),
        "backgroundHover": _rgb_to_hex(colors.bgHover),
        "foreground": _rgb_to_hex(colors.text),
        "topBarBackground": _rgb_to_hex(colors.topBarBg),
        "topBarHover": _rgb_to_hex(colors.topBarHover),
        "buttonBackground": _rgb_to_hex(colors.primaryAction),
        "buttonHover": _rgb_to_hex(colors.primaryActionHover),
        "accentGreen": _rgb_to_hex(colors.accentGreen),
        "accentRed": _rgb_to_hex(colors.accentRed),
        "accentBlue": _rgb_to_hex(colors.accentBlue),
    }


def generate_tkinter(themes_dir: Path, output_dir: Path) -> None:
    """Generate Tkinter JSON output file."""
    themes = load_all_themes(themes_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "themes.json"
    payload = {
        "formatVersion": 1,
        "source": "VisualAssault",
        "themes": {theme.id: _theme_to_tkinter_config(theme) for theme in themes},
    }

    output_file.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"✓ Generated Tkinter themes for {len(themes)} themes -> {output_file}")


if __name__ == "__main__":
    repo_root = Path(__file__).parent.parent
    generate_tkinter(repo_root / "themes", repo_root / "output" / "tkinter")
