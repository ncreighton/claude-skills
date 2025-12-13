# Visual-to-Code Pipeline

## The Missing Link: How Claude Actually SEES and IMPLEMENTS Designs

This skill solves the core problem: Claude can't see images, but it CAN generate designs through v0.app and Figma, then implement them precisely.

---

## The Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         VISUAL-TO-CODE PIPELINE                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  STEP 1: DNA FILE                                                                │
│  └── Colors, typography, voice, anti-patterns (JSON)                             │
│                                                                                  │
│  STEP 2: DESIGN TOKENS                                                           │
│  └── CSS Variables + Tailwind Config + Figma Variables                           │
│      (Claude generates these from DNA)                                           │
│                                                                                  │
│  STEP 3: v0.app PROMPTS                                                          │
│  └── Claude generates detailed prompts for each component                        │
│      → User pastes into v0.dev → v0 generates visual component                   │
│      → Export code OR screenshot for reference                                   │
│                                                                                  │
│  STEP 4: FIGMA SYNC (Optional but recommended)                                   │
│  └── Push tokens to Figma via MCP                                                │
│      → Create component library in Figma                                         │
│      → Use Figma MCP to extract specs during implementation                      │
│                                                                                  │
│  STEP 5: CLAUDE CODE IMPLEMENTATION                                              │
│  └── Claude Code receives:                                                       │
│      - CLAUDE.md (design tokens)                                                 │
│      - v0 exported code (component reference)                                    │
│      - Figma specs via MCP (exact measurements)                                  │
│      → Implements EXACTLY what was designed                                      │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Step 1: Design Token Generator

From any DNA file, generate these three token formats:

### CSS Custom Properties
```css
:root {
  /* Colors */
  --color-primary: #4A1C6F;
  --color-secondary: #D4AF37;
  --color-bg-primary: #1A1A2E;
  --color-bg-secondary: #0F0F1A;
  --color-text-primary: #E8E4D9;
  --color-text-secondary: #B8B0A0;
  --color-accent: #7B2D8E;
  
  /* Typography */
  --font-heading: 'Cinzel', serif;
  --font-body: 'Lora', serif;
  --font-accent: 'Cormorant Garamond', serif;
  
  /* Type Scale */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  --text-hero: 4.209rem;
  
  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;
  --space-section: 6rem;
  
  /* Effects */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-full: 9999px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.4);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.5);
  --shadow-glow: 0 0 40px rgba(212, 175, 55, 0.15);
  
  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.5s ease-out;
  --transition-reveal: 1.2s ease-out;
}
```

### Tailwind Config
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#4A1C6F',
        secondary: '#D4AF37',
        'bg-primary': '#1A1A2E',
        'bg-secondary': '#0F0F1A',
        'text-primary': '#E8E4D9',
        'text-secondary': '#B8B0A0',
        accent: '#7B2D8E',
      },
      fontFamily: {
        heading: ['Cinzel', 'serif'],
        body: ['Lora', 'serif'],
        accent: ['Cormorant Garamond', 'serif'],
      },
      fontSize: {
        'hero': '4.209rem',
      },
      spacing: {
        'section': '6rem',
      },
      boxShadow: {
        'glow': '0 0 40px rgba(212, 175, 55, 0.15)',
      },
      transitionDuration: {
        'slow': '500ms',
        'reveal': '1200ms',
      },
    },
  },
}
```

### Figma Variables Format
```json
{
  "colors": {
    "primary": { "value": "#4A1C6F", "type": "color" },
    "secondary": { "value": "#D4AF37", "type": "color" },
    "bg-primary": { "value": "#1A1A2E", "type": "color" },
    "bg-secondary": { "value": "#0F0F1A", "type": "color" },
    "text-primary": { "value": "#E8E4D9", "type": "color" },
    "text-secondary": { "value": "#B8B0A0", "type": "color" }
  },
  "typography": {
    "heading-font": { "value": "Cinzel", "type": "font" },
    "body-font": { "value": "Lora", "type": "font" },
    "hero-size": { "value": "67.34px", "type": "dimension" }
  },
  "spacing": {
    "section-gap": { "value": "96px", "type": "dimension" }
  }
}
```

---

## Step 2: v0.app Prompt Generator

Claude generates detailed prompts for v0.dev. User pastes these into v0 to generate visual components.

### v0 Prompt Template
```
Create a [COMPONENT_TYPE] with these EXACT specifications:

DESIGN SYSTEM:
- Background: [HEX] (dark/light)
- Primary color: [HEX]
- Secondary/accent: [HEX]
- Text color: [HEX]
- Heading font: [FONT_NAME] (serif/sans-serif)
- Body font: [FONT_NAME]

COMPONENT SPECS:
- [Detailed description of the component]
- [Layout requirements]
- [Spacing requirements]
- [Animation/interaction requirements]

STYLE REQUIREMENTS:
- [Specific visual style notes]
- [What to avoid]
- [Mood/atmosphere]

MUST INCLUDE:
- [Required elements]

MUST NOT INCLUDE:
- [Anti-patterns]

Output as: React component with Tailwind CSS
```

### Example: WitchcraftForBeginners Hero Section

```
Create a full-viewport hero section with these EXACT specifications:

DESIGN SYSTEM:
- Background: #0F0F1A (very dark navy, almost black)
- Primary color: #4A1C6F (deep amethyst purple)
- Secondary/accent: #D4AF37 (warm candlelight gold)
- Text color: #E8E4D9 (aged parchment cream)
- Heading font: Cinzel (elegant serif)
- Body font: Lora (readable serif)

COMPONENT SPECS:
- Full viewport height (100vh)
- Content positioned slightly left of center (not perfectly centered)
- Radial gradient from center: rgba(74, 28, 111, 0.1) to transparent
- Headline: "Where Ancient Wisdom Meets Modern Seekers"
  - Font: Cinzel
  - Size: ~4.2rem / 67px
  - Color: #D4AF37 (gold)
  - Letter-spacing: 0.02em
- Subheadline: "Your trusted guide into authentic witchcraft practice"
  - Font: Lora
  - Size: 1.25rem
  - Color: #E8E4D9
  - Max-width: 500px
- CTA Button: "Begin Your Journey"
  - Background: transparent
  - Border: 1px solid #D4AF37
  - Text: #D4AF37
  - Padding: 1rem 2.5rem
  - Hover: background fills with rgba(212, 175, 55, 0.1)
- Moon phase indicator in top-right: simple crescent moon icon, 32px, gold outline

STYLE REQUIREMENTS:
- Atmosphere: Candlelit study in an old cottage
- Feeling: Mysterious but welcoming, wise not spooky
- Animation: Content fades in slowly (1.2s) as if emerging from shadow
- Subtle particle effect: tiny gold specks floating slowly upward (optional)

MUST INCLUDE:
- Generous whitespace
- Slow, elegant transitions (0.5s minimum)
- The moon icon

MUST NOT INCLUDE:
- Stock witch imagery (no pointed hats, cauldrons, Halloween stuff)
- Sans-serif fonts
- White or light backgrounds
- Generic "Learn More" or "Get Started" button text
- Centered layout (should be slightly asymmetrical)
- Harsh shadows or bright colors

Output as: React component with Tailwind CSS, include the CSS for custom properties
```

---

## Step 3: v0 Workflow

### For Each Component:

1. **Generate v0 Prompt** (Claude does this)
   ```
   Generate a v0.app prompt for the [component] based on [site] DNA.
   ```

2. **User Executes in v0.dev**
   - Go to https://v0.dev
   - Paste the prompt
   - v0 generates the component
   - Iterate with follow-up prompts if needed

3. **Export from v0**
   - Copy the React/HTML code
   - Take a screenshot for visual reference
   - Save both to the project folder

4. **Add to Claude Code Project**
   ```
   /project-folder/
   ├── CLAUDE.md (design tokens)
   ├── BUILD-GUIDE.md (prompts)
   ├── v0-components/
   │   ├── hero-section.tsx (v0 export)
   │   ├── hero-section.png (screenshot)
   │   ├── navigation.tsx
   │   ├── navigation.png
   │   └── ...
   ```

5. **Claude Code Implements**
   - Reads CLAUDE.md for tokens
   - References v0 code for component structure
   - Implements in WordPress/target platform

---

## Step 4: Figma Integration

### Push Tokens to Figma

Using Figma MCP or Figma API:

```javascript
// Push design tokens to Figma variables
const figmaTokens = {
  "collections": [{
    "name": "WitchcraftForBeginners",
    "modes": [{ "name": "Default" }],
    "variables": [
      { "name": "color/primary", "value": "#4A1C6F" },
      { "name": "color/secondary", "value": "#D4AF37" },
      { "name": "color/bg-primary", "value": "#1A1A2E" },
      // ... all tokens
    ]
  }]
};

// Via Figma REST API
POST /v1/files/{file_key}/variables
```

### Create Component Library in Figma

1. Create a new Figma file for the site
2. Set up the token variables
3. Build components using the tokens
4. Use as visual reference during implementation

### Extract Specs via Figma MCP

During Claude Code implementation:
```
Use Figma MCP to get the exact specifications for the hero section.
File: [figma_file_url]
Node: [hero_section_node_id]
```

---

## Step 5: Claude Code Project Setup

### Project Structure
```
C:\Claude Code Projects\witchcraft-for-beginners\
├── CLAUDE.md                    # Design tokens + rules
├── BUILD-GUIDE.md               # Step-by-step prompts
├── .mcp/
│   └── config.json              # MCP connections
├── design-reference/
│   ├── tokens/
│   │   ├── css-variables.css
│   │   ├── tailwind.config.js
│   │   └── figma-variables.json
│   ├── v0-components/
│   │   ├── hero.tsx
│   │   ├── hero.png
│   │   ├── navigation.tsx
│   │   └── ...
│   └── figma-link.md            # Link to Figma file
└── implementation/
    └── ... (WordPress files)
```

### CLAUDE.md Addition for v0 Reference
```markdown
## Visual References

### v0 Component Library
The following components were generated via v0.dev and represent the exact visual target:

- **Hero Section:** `/design-reference/v0-components/hero.tsx`
- **Navigation:** `/design-reference/v0-components/navigation.tsx`
- **Card Grid:** `/design-reference/v0-components/card-grid.tsx`

When implementing, match these components EXACTLY in structure and styling.
Adapt for WordPress/PHP as needed but maintain visual fidelity.

### Figma File
Design source: [Figma URL]
Use Figma MCP to extract exact measurements when needed.
```

---

## Command Reference

### Generate All Tokens
```
Generate design tokens for [SiteName] in all three formats:
1. CSS custom properties
2. Tailwind config
3. Figma variables JSON

Save to /design-reference/tokens/
```

### Generate v0 Prompts for All Components
```
Generate v0.app prompts for [SiteName] components:
1. Hero section
2. Navigation header
3. Card/article grid
4. Footer
5. Newsletter signup
6. [Site-specific components]

Output as markdown file with each prompt clearly separated.
```

### Create Figma Variables
```
Using Figma MCP, create a new variables collection for [SiteName] with all design tokens.
```

### Full Design Package
```
Generate complete design package for [SiteName]:
1. All design tokens (3 formats)
2. v0.app prompts for core components
3. CLAUDE.md with visual reference section
4. Instructions for user to execute v0 prompts

Save to /mnt/user-data/outputs/[site-slug]-design-package/
```

---

## The Key Insight

**Claude can't see images, but Claude CAN:**
1. Generate precise prompts that CREATE visuals (v0.dev)
2. Read code that REPRESENTS visuals (v0 exports)
3. Extract specs from design tools (Figma MCP)
4. Implement based on these references

**The workflow is:**
```
Claude generates → User executes in v0 → v0 creates visual → 
Export code → Claude Code implements from code reference
```

This gives Claude "vision" through a text-to-visual-to-text pipeline.

---

## Quick Start

For any new site:

1. **In Claude.ai:**
   ```
   Generate complete design package for [SiteName] using Visual-to-Code Pipeline.
   Include tokens, v0 prompts, and CLAUDE.md updates.
   ```

2. **User does:**
   - Takes each v0 prompt to v0.dev
   - Generates components
   - Exports code to project folder
   - Optionally creates Figma file with tokens

3. **In Claude Code:**
   - Has CLAUDE.md with tokens
   - Has v0 component code as reference
   - Implements WordPress version matching the reference

---

*Visual-to-Code Pipeline - Giving Claude "Vision" Through Design Tools*
