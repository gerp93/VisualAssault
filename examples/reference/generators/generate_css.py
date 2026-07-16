"""Generate CSS themes from JSON theme definitions."""
from pathlib import Path
from typing import List
from src.theme import Theme


def generate_css(themes_dir: Path, output_file: Path) -> None:
    """
    Generate CSS file from all theme JSON files.
    
    Args:
        themes_dir: Directory containing theme JSON files
        output_file: Output CSS file path
    """
    themes = load_all_themes(themes_dir)
    
    css_content = []
    
    # Generate CSS for each theme
    for theme in themes:
        css_content.append(generate_theme_css(theme))
    
    # Add common CSS rules
    css_content.append(generate_common_css())
    
    # Write to file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w') as f:
        f.write('\n'.join(css_content))
    
    print(f"✓ Generated CSS for {len(themes)} themes -> {output_file}")


def load_all_themes(themes_dir: Path) -> List[Theme]:
    """
    Load all theme JSON files from the themes directory.
    
    Args:
        themes_dir: Directory containing theme subdirectories
        
    Returns:
        List of Theme objects
    """
    themes = []
    
    # Load from base/ and crazy/ subdirectories
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


def generate_theme_css(theme: Theme) -> str:
    """
    Generate CSS for a single theme.
    
    Args:
        theme: Theme object
        
    Returns:
        CSS string for the theme
    """
    css = f"body.{theme.id}-theme {{\n"
    
    colors = theme.colors
    css += f"    --color-top-bar-bg: {colors.topBarBg};\n"
    css += f"    --color-top-bar-hover: {colors.topBarHover};\n"
    css += f"    --color-text: {colors.text};\n"
    css += f"    --color-bg: {colors.bg};\n"
    css += f"    --color-bg-hover: {colors.bgHover};\n"
    css += f"    --color-primary-action: {colors.primaryAction};\n"
    css += f"    --color-primary-action-hover: {colors.primaryActionHover};\n"
    css += f"    --color-accent-green: {colors.accentGreen};\n"
    css += f"    --color-accent-red: {colors.accentRed};\n"
    css += f"    --color-accent-blue: {colors.accentBlue};\n"
    
    css += "}\n"
    
    return css


def generate_common_css() -> str:
    """
    Generate common CSS rules that apply to all themes.
    
    Returns:
        Common CSS string
    """
    return """body {
    color: var(--color-text);
    background: var(--color-bg);
}

#top-bar {
    background-color: var(--color-top-bar-bg);
}

#top-bar-menu {
    background-color: var(--color-top-bar-bg);
}

#top-bar-menu .top-bar-menu-link:hover {
    background-color: var(--color-top-bar-hover);
}

a {
    color: var(--color-accent-blue);
}

dialog {
    color: var(--color-text);
    background: var(--color-bg);
}

button {
    color: var(--color-text);
    background-color: var(--color-primary-action);
}

button:hover {
    color: var(--color-text);
    background-color: var(--color-primary-action-hover);
}

input {
    color: var(--color-text);
    background: var(--color-bg);
}

input[type="submit"] {
    color: var(--color-text);
    background-color: var(--color-primary-action);
}

input[type="submit"]:hover {
    color: var(--color-text);
    background-color: var(--color-primary-action-hover);
}

textarea {
    color: var(--color-text);
    background: var(--color-bg);
}

select {
    color: var(--color-text);
    background: var(--color-bg);
}

tbody>tr:hover {
    background-color: var(--color-bg-hover);
}

.lobby-chat-message-green {
    color: var(--color-accent-green);
}

.lobby-chat-message-red {
    color: var(--color-accent-red);
}

.lobby-chat-message-blue {
    color: var(--color-accent-blue);
}

progress {
    accent-color: var(--color-accent-red);
}

progress.progress-full {
    accent-color: var(--color-accent-green);
}

.danger-zone {
    border-color: var(--color-accent-red);
    background-color: var(--color-bg-hover);
}

.danger-zone-summary {
    color: var(--color-accent-red);
}

.htmx-result-good {
    color: var(--color-accent-green);
}

.htmx-result-bad {
    color: var(--color-accent-red);
}

#lobby-grid-container>div {
    background-color: var(--color-bg);
}"""


if __name__ == '__main__':
    # Run standalone
    from pathlib import Path
    
    repo_root = Path(__file__).parent.parent
    themes_dir = repo_root / 'themes'
    output_file = repo_root / 'output' / 'css' / 'colors.css'
    
    generate_css(themes_dir, output_file)
