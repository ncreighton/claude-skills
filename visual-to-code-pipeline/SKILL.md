# VISUAL-TO-CODE PIPELINE SKILL
## DNA → Design Tokens → v0 Prompts → Code
### Version 1.0

---

## Overview

This skill enables Claude to "see" designs by converting:
1. **DNA Files** → Site personality, colors, fonts, style
2. **Design Tokens** → CSS variables, Tailwind config
3. **v0 Prompts** → Ready-to-paste prompts for v0.dev
4. **Implementation** → React/HTML code from v0 output

**THE KEY SKILL** for producing unique, non-generic designs.

**Trigger Keywords:** design tokens, v0 prompt, visual reference, generate components, design package, token export, Figma sync, component generation

---

## The Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    VISUAL-TO-CODE PIPELINE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  DNA FILE        →    DESIGN TOKENS    →    v0 PROMPT          │
│  (personality)        (CSS/Tailwind)        (component spec)   │
│                                                                 │
│       ↓                    ↓                    ↓               │
│                                                                 │
│  Site brain         variables.css      "Generate a hero with   │
│  Colors, fonts      tailwind.config    these exact colors..."  │
│  Voice, mood        spacing, shadows                           │
│                                                                 │
│                              ↓                                  │
│                                                                 │
│                    v0.dev GENERATES CODE                        │
│                              ↓                                  │
│                                                                 │
│                    USER EXPORTS CODE                            │
│                              ↓                                  │
│                                                                 │
│                    CLAUDE IMPLEMENTS                            │
│                    (as WordPress block/component)               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: DNA File Analysis

### DNA File Structure (from creative-command-center)

```yaml
# Example: witchcraftforbeginners-brain.md
Site: WitchcraftForBeginners
Domain: witchcraftforbeginners.com
Niche: Witchcraft & Spirituality

Personality:
  Voice: Mystical warmth, welcoming, grounded
  Tone: Like a wise friend sharing ancient knowledge
  Mood: Candles, moonlight, aged paper, sacred spaces

Colors:
  Primary: #4A1C6F (Deep Purple - mystical power)
  Secondary: #C9A962 (Gold - wisdom, prosperity)
  Background: #0D0D0D (Near-black - night sky)
  Accent: #2D1B4E (Dark purple - depth)
  Text: #E8E0D5 (Warm cream)

Typography:
  Display: Cinzel (mystical serif, uppercase titles)
  Body: Lora (elegant serif, readable)
  Accent: Cormorant Garamond (poetic emphasis)

Anti-Patterns (NEVER do):
  - Halloween imagery (skulls, orange+purple)
  - Centered text layouts  
  - Sans-serif fonts
  - "Learn More" generic CTAs
  - Purple-to-blue gradients
  - Stock photo witches
  - Pentagram overuse
```

---

## Phase 2: Design Token Generation

### CSS Variables Output

```css
/* variables.css - Generated from DNA */
:root {
  /* Colors */
  --color-primary: #4A1C6F;
  --color-secondary: #C9A962;
  --color-background: #0D0D0D;
  --color-accent: #2D1B4E;
  --color-text: #E8E0D5;
  --color-text-muted: #A89F94;
  --color-border: rgba(201, 169, 98, 0.3);
  
  /* Typography */
  --font-display: 'Cinzel', serif;
  --font-body: 'Lora', serif;
  --font-accent: 'Cormorant Garamond', serif;
  
  /* Font Sizes */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  
  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;
  
  /* Borders */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.5);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.5);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 20px rgba(201, 169, 98, 0.3);
}
```

### Tailwind Config Output

```javascript
// tailwind.config.js - Generated from DNA
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#4A1C6F',
        secondary: '#C9A962',
        background: '#0D0D0D',
        accent: '#2D1B4E',
        cream: '#E8E0D5',
        muted: '#A89F94',
      },
      fontFamily: {
        display: ['Cinzel', 'serif'],
        body: ['Lora', 'serif'],
        accent: ['Cormorant Garamond', 'serif'],
      },
      boxShadow: {
        'glow': '0 0 20px rgba(201, 169, 98, 0.3)',
        'glow-lg': '0 0 40px rgba(201, 169, 98, 0.4)',
      },
      backgroundImage: {
        'gradient-mystical': 'linear-gradient(to bottom, #0D0D0D, #2D1B4E)',
      },
    },
  },
}
```

---

## Phase 3: v0 Prompt Generation

### Prompt Template

```markdown
# v0 Component Generation Prompt

## Component: [COMPONENT_NAME]
## Site: [SITE_NAME]

### Design System (USE THESE EXACT VALUES)

**Colors:**
- Primary: [HEX] - [description]
- Secondary: [HEX] - [description]
- Background: [HEX]
- Text: [HEX]

**Typography:**
- Headings: [FONT_NAME] (Google Font)
- Body: [FONT_NAME] (Google Font)

**Style Rules:**
- [Specific style requirement]
- [Specific style requirement]

### ANTI-PATTERNS (NEVER DO)
❌ [Anti-pattern 1]
❌ [Anti-pattern 2]
❌ [Anti-pattern 3]

### Component Specification

[Detailed description of what to build]

### Output Requirements
- React + Tailwind CSS
- Mobile-first responsive
- Include Google Fonts import
- Use exact hex values from design system
- Include hover/focus states
```

### Example: Hero Section Prompt

```markdown
# v0 Component Generation Prompt

## Component: Hero Section
## Site: WitchcraftForBeginners

### Design System (USE THESE EXACT VALUES)

**Colors:**
- Primary: #4A1C6F (deep purple - mystical power)
- Secondary: #C9A962 (gold - wisdom accents)
- Background: #0D0D0D (near-black)
- Text: #E8E0D5 (warm cream)

**Typography:**
- Headings: Cinzel (Google Font) - uppercase, letter-spacing: 0.1em
- Body: Lora (Google Font) - elegant, 1.7 line-height

**Style Rules:**
- Left-aligned text (NOT centered)
- Subtle gold glow effects on hover
- Dark atmospheric backgrounds
- Mystical but sophisticated aesthetic
- Moon phases, candles, herbs as imagery motifs

### ANTI-PATTERNS (NEVER DO)
❌ Halloween imagery (skulls, orange+purple combinations)
❌ Centered text layouts
❌ Sans-serif fonts
❌ Generic "Learn More" CTAs
❌ Purple-to-blue gradients
❌ Stock photo witches with cauldrons
❌ Overuse of pentagrams

### Component Specification

Create a full-width hero section for a modern witchcraft education website.

Layout:
- Full viewport height (100vh)
- Content left-aligned, 60% width on desktop
- Image/visual element on right side
- Responsive: stack on mobile

Content:
- Pre-headline: Small caps text "Begin Your Magical Journey"
- Main headline: Large, powerful, mystical
- Subheadline: Welcoming, warm invitation
- CTA button: Gold with hover glow effect

Visual Elements:
- Subtle animated stars or moon particles (optional)
- Gradient overlay on background
- Gold accent line or decorative element

### Output Requirements
- React + Tailwind CSS
- Mobile-first responsive
- Include Google Fonts: Cinzel, Lora
- Use exact hex values: #4A1C6F, #C9A962, #0D0D0D, #E8E0D5
- Include hover/focus states with gold glow
```

---

## Phase 4: Implementation

### From v0 Output to WordPress

After user exports code from v0.dev:

```php
<?php
/**
 * Custom Hero Block
 * Generated from v0.dev → WitchcraftForBeginners DNA
 */

// Register the block
add_action('init', function() {
    register_block_type('wcfb/hero', [
        'render_callback' => 'wcfb_render_hero',
        'attributes' => [
            'preHeadline' => ['type' => 'string', 'default' => 'Begin Your Magical Journey'],
            'headline' => ['type' => 'string', 'default' => 'Discover Ancient Wisdom'],
            'subheadline' => ['type' => 'string'],
            'ctaText' => ['type' => 'string', 'default' => 'Start Your Practice'],
            'ctaUrl' => ['type' => 'string', 'default' => '/getting-started'],
        ]
    ]);
});

function wcfb_render_hero($attributes) {
    // v0-generated code adapted for WordPress
    ob_start();
    ?>
    <section class="wcfb-hero" style="
        min-height: 100vh;
        background: linear-gradient(to bottom, #0D0D0D, #2D1B4E);
        color: #E8E0D5;
        font-family: 'Lora', serif;
    ">
        <!-- v0 code inserted here -->
    </section>
    <?php
    return ob_get_clean();
}
```

---

## Complete Workflow

### Step 1: Read DNA File
```bash
# DNA files location
/mnt/skills/user/creative-command-center/brains/[site]-brain.md
```

### Step 2: Generate Tokens
```python
def generate_tokens_from_dna(dna_content: str) -> dict:
    """Parse DNA file and generate design tokens"""
    # Extract colors, fonts, spacing
    # Return CSS variables and Tailwind config
```

### Step 3: Generate v0 Prompts
```python
def generate_v0_prompt(component: str, dna: dict, tokens: dict) -> str:
    """Generate a v0.dev-ready prompt for a component"""
    # Include exact hex codes
    # Include font names
    # Include anti-patterns
    # Include detailed specification
```

### Step 4: User Action
1. Copy prompt to v0.dev
2. Generate component
3. Export code
4. Save to project folder

### Step 5: Claude Implements
```python
def implement_v0_code(v0_code: str, target: str) -> str:
    """Convert v0 code to WordPress block or plugin"""
    # Parse React code
    # Convert to WordPress-compatible
    # Add block registration
    # Return ready-to-use PHP
```

---

## Site DNA Files (from creative-command-center)

| Site | DNA File | Primary Color | Font |
|------|----------|---------------|------|
| WitchcraftForBeginners | witchcraftforbeginners-brain.md | #4A1C6F | Cinzel |
| SmartHomeWizards | smarthomewizards-brain.md | #00D4FF | Inter |
| AIinActionHub | aiinactionhub-brain.md | #7C3AED | Space Grotesk |
| MythicalArchives | mythicalarchives-brain.md | #8B4513 | Playfair Display |
| Family-Flourish | familyflourish-brain.md | #10B981 | Nunito |
| BulletJournals | bulletjournals-brain.md | #F59E0B | Caveat |

---

## v0 API Integration (Advanced)

v0.dev now has Platform API for programmatic access:

```python
import requests

V0_API_KEY = "v1:Gc9e6pCtq5X2AkIkYhEEBzDL:cEDxU9gxvibKpVjdqkkbEZN4"

def v0_generate_component(prompt: str) -> dict:
    """Generate component using v0 API"""
    response = requests.post(
        "https://v0.dev/api/generate",
        headers={
            "Authorization": f"Bearer {V0_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "model": "v0-1",
            "framework": "react",
            "styling": "tailwind"
        }
    )
    return response.json()
```

---

## Quick Commands

```yaml
# Generate tokens for a site
generate_tokens("witchcraftforbeginners")

# Generate v0 prompt for component
generate_v0_prompt("hero", "witchcraftforbeginners")
generate_v0_prompt("navigation", "smarthomewizards")
generate_v0_prompt("card-grid", "aiinactionhub")

# Full pipeline
run_visual_pipeline("witchcraftforbeginners", ["hero", "nav", "cards", "footer"])
```

---

## GitHub Repositories

- **creative-command-center**: DNA files for all 16 sites
- **site-design-packages**: Generated design packages
- **visual-to-code-pipeline**: This skill and templates

---

*Visual-to-Code Pipeline Skill*
*Version 1.0 | Recovered 2025-12-15*
*The key to producing unique, non-generic designs*
