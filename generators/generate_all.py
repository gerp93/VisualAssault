"""Master generator orchestrator for all theme outputs."""
import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from generators.generate_css import generate_css
from generators.generate_tkinter import generate_tkinter


def generate_all():
    """Generate all theme outputs."""
    repo_root = Path(__file__).parent.parent
    themes_dir = repo_root / 'themes'
    
    print("🎨 Visual Assault Theme Generator")
    print("=" * 50)
    
    # Generate CSS
    print("\n📝 Generating CSS themes...")
    css_output = repo_root / 'output' / 'css' / 'colors.css'
    generate_css(themes_dir, css_output)
    
    print("\n🐍 Generating Tkinter themes...")
    generate_tkinter(themes_dir, repo_root / 'output' / 'tkinter')
    
    # print("\n✈️ Generating Flet themes...")
    # generate_flet(themes_dir, repo_root / 'output' / 'flet')
    
    # print("\n🌶️ Generating Flask themes...")
    # generate_flask(themes_dir, repo_root / 'output' / 'flask')
    
    print("\n" + "=" * 50)
    print("✅ All theme outputs generated successfully!")


if __name__ == '__main__':
    generate_all()
