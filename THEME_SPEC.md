# Visual Assault Theme Specification

This document defines the JSON format for Visual Assault theme definitions.

## Theme Structure

A theme is defined as a JSON object with the following structure:

```json
{
  "id": "theme-id",
  "name": "Theme Name",
  "displayName": "🎨 Display Name",
  "description": "Brief description",
  "category": "base",
  "colors": { /* color definitions */ },
  "typography": { /* optional typography settings */ },
  "metadata": { /* optional metadata */ }
}
```

## Required Fields

### `id` (string, required)
- Unique theme identifier in kebab-case format
- Must match pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`
- Example: `"dark"`, `"nord-polar-night"`, `"tokyo-night-dark"`
- This ID is used to generate CSS class names: `body.{id}-theme`

### `name` (string, required)
- Human-readable theme name
- Used for display in theme selectors
- Example: `"Dark"`, `"Nord Polar Night"`

### `displayName` (string, required)
- Display name with optional emoji or special characters
- Used for rich UI displays
- Example: `"🌙 Dark"`, `"❄️ Nord Polar Night"`

### `category` (string, required)
- Theme category: `"base"` or `"crazy"`
- **Base themes**: Production-ready, professional themes
- **Crazy themes**: Experimental, visually striking themes
- Example: `"base"`

### `colors` (object, required)
All color values must be in `rgb(r, g, b)` format where r, g, b are 0-255.

#### Required Color Properties:

##### `topBarBg` (string)
- Background color for the top navigation bar
- Example: `"rgb(50, 50, 50)"`

##### `topBarHover` (string)
- Hover state color for top bar elements
- Example: `"rgb(70, 70, 70)"`

##### `text` (string)
- Primary text color for body content
- Should have good contrast with `bg`
- Example: `"rgb(255, 255, 255)"`

##### `bg` (string)
- Main background color
- Example: `"rgb(34, 34, 34)"`

##### `bgHover` (string)
- Background color for hover states (e.g., table rows)
- Example: `"rgb(54, 54, 54)"`

##### `primaryAction` (string)
- Background color for primary action buttons
- Example: `"rgb(7, 72, 75)"`

##### `primaryActionHover` (string)
- Hover state for primary action buttons
- Example: `"rgb(8, 94, 99)"`

##### `primaryActionText` (string or null)
- Text color for primary action buttons
- If `null`, uses the theme's `text` color
- Example: `null` or `"rgb(255, 255, 255)"`

##### `accentGreen` (string)
- Success/positive accent color
- Used for success messages, valid states
- Example: `"rgb(120, 255, 99)"`

##### `accentRed` (string)
- Error/negative accent color
- Used for error messages, danger zones
- Example: `"rgb(255, 100, 100)"`

##### `accentBlue` (string)
- Info/link accent color
- Used for links, informational elements
- Example: `"rgb(130, 160, 255)"`

## Optional Fields

### `description` (string, optional)
- Detailed description of the theme
- Can include inspiration, use cases, etc.
- Example: `"Classic dark theme with teal accents"`

### `typography` (object, optional)
Typography settings for the theme. All fields are optional with defaults.

```json
"typography": {
  "fontFamily": "'Arial', 'Helvetica', sans-serif",
  "fontFamilyMono": "'Consolas', 'Courier New', monospace",
  "fontSizeBase": "16px",
  "fontWeightNormal": 400,
  "fontWeightBold": 700
}
```

- **fontFamily**: Primary font stack
- **fontFamilyMono**: Monospace font stack for code
- **fontSizeBase**: Base font size with unit
- **fontWeightNormal**: Normal text weight (100-900)
- **fontWeightBold**: Bold text weight (100-900)

### `metadata` (object, optional)
Additional metadata about the theme:

```json
"metadata": {
  "inspiration": "Nord color palette",
  "author": "Grantford Barnes",
  "createdAt": "2025-12-07",
  "wcagAACompliant": true
}
```

- **inspiration**: Source of inspiration for the theme
- **author**: Theme creator's name
- **createdAt**: Creation date in YYYY-MM-DD format
- **wcagAACompliant**: Whether theme meets WCAG AA contrast standards (boolean)

## Color Format Guidelines

### RGB Format
All colors must use the `rgb()` format:
```json
"bg": "rgb(34, 34, 34)"
```

### Why RGB?
- **Consistency**: Single format across all themes
- **Compatibility**: Works in CSS, can be converted to other formats
- **Clarity**: Explicit color values, no ambiguity
- **Validation**: Easy to validate with regex patterns

### Converting Colors

From Hex to RGB:
```
#222222 → rgb(34, 34, 34)
#FF0000 → rgb(255, 0, 0)
```

From color names (use explicit RGB values):
```
black → rgb(0, 0, 0)
white → rgb(255, 255, 255)
```

## Accessibility Guidelines

### WCAG AA Compliance
For professional themes, aim for WCAG AA compliance:
- **Normal text**: Minimum 4.5:1 contrast ratio
- **Large text** (18pt+): Minimum 3:1 contrast ratio

### Key Contrast Ratios to Check
1. **text** vs **bg**: Primary content readability
2. **text** vs **primaryAction**: Button text readability
3. **accentRed** vs **bg**: Error message visibility
4. **accentGreen** vs **bg**: Success message visibility

Use the validation tools to check:
```bash
python tests/test_theme_completeness.py
```

## Example Complete Theme

```json
{
  "id": "dark",
  "name": "Dark",
  "displayName": "🌙 Dark",
  "description": "Classic dark theme with teal accents",
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
  "typography": {
    "fontFamily": "'Arial', 'Helvetica', sans-serif",
    "fontFamilyMono": "'Consolas', 'Courier New', monospace",
    "fontSizeBase": "16px",
    "fontWeightNormal": 400,
    "fontWeightBold": 700
  },
  "metadata": {
    "inspiration": "Classic dark theme",
    "author": "Grantford Barnes",
    "createdAt": "2025-12-07",
    "wcagAACompliant": true
  }
}
```

## Validation

Themes are automatically validated against:
1. **JSON Schema**: `themes/schema.json`
2. **Completeness**: All required fields present
3. **Format**: Color values in correct RGB format
4. **Contrast**: WCAG compliance checks (warnings only)

Run validation:
```bash
python tests/test_theme_completeness.py
```

## CSS Output

Themes are converted to CSS custom properties:

```css
body.dark-theme {
    --color-top-bar-bg: rgb(50, 50, 50);
    --color-top-bar-hover: rgb(70, 70, 70);
    --color-text: rgb(255, 255, 255);
    --color-bg: rgb(34, 34, 34);
    --color-bg-hover: rgb(54, 54, 54);
    --color-primary-action: rgb(7, 72, 75);
    --color-primary-action-hover: rgb(8, 94, 99);
    --color-accent-green: rgb(120, 255, 99);
    --color-accent-red: rgb(255, 100, 100);
    --color-accent-blue: rgb(130, 160, 255);
}
```

## Future Format Extensions

Future versions may include:
- **Spacing tokens**: Margins, padding, gaps
- **Shadow definitions**: Box shadows, text shadows
- **Border definitions**: Border radius, widths
- **Animation timings**: Transition durations
- **Breakpoints**: Responsive design tokens

These will be added as optional fields to maintain backward compatibility.
