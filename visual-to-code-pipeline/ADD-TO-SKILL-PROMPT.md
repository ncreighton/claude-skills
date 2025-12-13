# PROMPT TO ADD TO VISUAL DESIGN SYSTEM SKILL

## Copy This Section Into Your Skill

---

## Visual-to-Code Pipeline Integration

### The Core Workflow

Claude CANNOT see images directly. Instead, use this pipeline:

```
DNA File → Design Tokens → v0.app Prompts → User generates in v0 → Export code → Claude implements from code
```

### Step 1: Always Generate Design Tokens First

When starting any site design work, FIRST generate tokens in THREE formats:

1. **CSS Custom Properties** (for WordPress/vanilla CSS)
2. **Tailwind Config** (for React/Next.js/v0 components)
3. **Figma Variables JSON** (for Figma sync)

These tokens are the SOURCE OF TRUTH for all visual decisions.

### Step 2: Generate v0.app Prompts for Components

For each component the site needs, generate a detailed v0.dev prompt that includes:

```
Create a [COMPONENT] with these EXACT specifications:

DESIGN SYSTEM:
- Background: [exact hex from tokens]
- Primary color: [exact hex]
- Secondary color: [exact hex]
- Text color: [exact hex]
- Heading font: [exact font name]
- Body font: [exact font name]

COMPONENT SPECS:
[Detailed layout, spacing, sizing]

STYLE REQUIREMENTS:
[Mood, atmosphere, specific visual notes]

MUST INCLUDE:
[Required elements]

MUST NOT INCLUDE:
[Anti-patterns from DNA]

Output as: React component with Tailwind CSS
```

### Step 3: User Executes v0 Prompts

Instruct the user to:
1. Go to https://v0.dev
2. Paste the prompt
3. Generate the component
4. Export the code
5. Save to project folder

### Step 4: Claude Code Uses v0 Output as Reference

The v0 exported code becomes the VISUAL REFERENCE. Claude Code should:
- Read the v0 component code
- Understand the exact structure and styling
- Implement equivalent in WordPress/target platform
- Match the visual output exactly

### When to Use Figma MCP

If Figma MCP is available:
1. Push tokens to Figma as variables
2. Create component frames in Figma
3. Use `get_design_context` to extract specs during implementation
4. Compare implementation to Figma source

### Commands to Implement

```
GENERATE DESIGN PACKAGE:
"Generate complete design package for [Site] including:
1. CSS tokens
2. Tailwind config  
3. Figma variables JSON
4. v0.app prompts for: hero, navigation, cards, footer, newsletter
5. Updated CLAUDE.md with visual reference section"

GENERATE V0 PROMPT:
"Generate a v0.app prompt for [component] based on [Site] DNA.
Include exact colors, fonts, spacing, and anti-patterns."

IMPLEMENT FROM V0 REFERENCE:
"Implement the [component] in WordPress based on the v0 reference code at [path].
Match the structure and styling exactly, adapting for PHP/WordPress."
```

### File Structure for Projects

```
/project-folder/
├── CLAUDE.md                    # Tokens + rules + v0 references
├── design-reference/
│   ├── tokens/
│   │   ├── variables.css
│   │   ├── tailwind.config.js
│   │   └── figma-variables.json
│   └── v0-components/
│       ├── hero.tsx             # v0 export (reference)
│       ├── navigation.tsx
│       └── ...
└── BUILD-GUIDE.md               # Build prompts
```

### Critical Rule

**Never implement visual designs without either:**
1. v0 component code as reference, OR
2. Figma specs via MCP, OR  
3. Explicit token values from CLAUDE.md

This ensures Claude Code produces EXACTLY what was designed, not generic interpretations.

---

## Example: Generating a Hero Section

### 1. Claude Generates This v0 Prompt:

```
Create a full-viewport hero section:

DESIGN SYSTEM:
- Background: #0F0F1A
- Primary: #4A1C6F
- Accent: #D4AF37  
- Text: #E8E4D9
- Heading font: Cinzel (serif)
- Body font: Lora (serif)

SPECS:
- Height: 100vh
- Content: left of center
- Headline: "Where Ancient Wisdom Meets Modern Seekers" 
  - Cinzel, 4.2rem, #D4AF37
- Subhead: "Your trusted guide into authentic witchcraft practice"
  - Lora, 1.25rem, #E8E4D9
- CTA: "Begin Your Journey"
  - Transparent bg, gold border, gold text
  - Hover: subtle gold fill

STYLE:
- Candlelit atmosphere
- Content emerges from darkness (1.2s fade)
- Subtle radial gradient from center

AVOID:
- Halloween imagery
- Centered layout
- Sans-serif fonts
- "Learn More" button text

Output: React + Tailwind
```

### 2. User Pastes in v0.dev, Gets Component

### 3. User Exports Code to Project:
```
/v0-components/hero.tsx
```

### 4. Claude Code Implements:
```
"Implement the hero section in WordPress based on the v0 reference at 
/v0-components/hero.tsx. Use the same structure, convert Tailwind to 
CSS custom properties, and output as Blocksy-compatible PHP/HTML."
```

---

## Add This to CLAUDE.md Template

```markdown
## Visual Implementation References

### Design Tokens Location
- CSS: `/design-reference/tokens/variables.css`
- Tailwind: `/design-reference/tokens/tailwind.config.js`
- Figma: `/design-reference/tokens/figma-variables.json`

### v0 Component References
Components generated via v0.dev as visual targets:

| Component | Reference File | Status |
|-----------|---------------|--------|
| Hero | `/v0-components/hero.tsx` | Ready |
| Navigation | `/v0-components/nav.tsx` | Ready |
| Cards | `/v0-components/cards.tsx` | Ready |
| Footer | `/v0-components/footer.tsx` | Ready |

### Implementation Rule
Match v0 reference components EXACTLY in visual output.
Adapt code for WordPress but maintain visual fidelity.
```

---

*This prompt section should be added to any Visual Design System skill to enable the visual-to-code pipeline.*
