# WitchcraftForBeginners - Claude Code Project

> **Generated:** 2025-12-13  
> **DNA Version:** 2.0.0  
> **Site URL:** https://witchcraftforbeginners.com  
> **Status:** FLAGSHIP SITE - Highest Priority

---

## 🎯 IDENTITY

### Who This Site Is
The wise witch who remembers what it was like to be new. Transforms curiosity into practice through patient guidance. Never condescending, always empowering. Treats the craft with reverence but makes it accessible.

**Archetype:** Magician + Sage

### Soul Statement
> An ancient grimoire reimagined for the digital age, where every scroll reveals a secret.

This is the candlelit sanctuary where seekers become practitioners. We honor the old ways while speaking in modern tongues. Every visitor is treated as a future member of the craft, deserving of respect and real knowledge—not watered-down spirituality or dangerous misinformation.

### What We ARE
- The trusted guide into authentic witchcraft practice
- A bridge between ancient wisdom and modern seekers
- A community that takes the craft seriously while remaining warm and welcoming

### What We Are NOT
- Not a trendy aesthetic
- Not 'witch-lite' for Instagram
- Not appropriative of closed practices
- Not fear-mongering or dark for darkness's sake
- Not a marketplace first

### Emotional Tone
- **Primary:** Warm mysticism
- **Secondary:** Empowering reverence
- **Tertiary:** Grounded wonder
- **Range:** curiosity, wonder, belonging, empowerment, reverence, comfort, excitement, peace
- **NEVER:** fear, anxiety, shame, confusion, overwhelm, skepticism, judgment, rushed urgency

---

## 🎨 DESIGN TOKENS

### Colors

```css
/* CSS Custom Properties - PRODUCTION READY */
:root {
  /* Primary Palette */
  --color-primary: #4A1C6F;          /* Deep Amethyst - accents, links, important UI */
  --color-secondary: #D4AF37;        /* Candle Gold - highlights, warmth accents */
  --color-accent: #8B4513;           /* Aged Leather - tertiary, grounding */
  
  /* Backgrounds (Dark First) */
  --color-bg-primary: #1A1A2E;       /* Night Sky */
  --color-bg-secondary: #16213E;     /* Midnight Blue */
  --color-bg-tertiary: #0F0F1A;      /* Deep Void */
  
  /* Text */
  --color-text-primary: #E8E4D9;     /* Aged Parchment (12.5:1 contrast) */
  --color-text-secondary: #B8B4A9;   /* Faded Ink */
  --color-text-muted: #6B6860;       /* Shadow Text */
  
  /* Semantic */
  --color-success: #4A7C59;          /* Forest Green */
  --color-warning: #C9A227;          /* Amber Caution */
  --color-error: #8B3A3A;            /* Deep Crimson */
  --color-info: #4A6F8B;             /* Twilight Blue */
}
```

```javascript
// tailwind.config.js - COPY THIS EXACTLY
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#4A1C6F',
        secondary: '#D4AF37',
        accent: '#8B4513',
        background: {
          DEFAULT: '#1A1A2E',
          secondary: '#16213E',
          tertiary: '#0F0F1A',
        },
        foreground: {
          DEFAULT: '#E8E4D9',
          secondary: '#B8B4A9',
          muted: '#6B6860',
        },
        success: '#4A7C59',
        warning: '#C9A227',
        error: '#8B3A3A',
        info: '#4A6F8B',
      },
    },
  },
}
```

### Typography

```css
:root {
  /* Font Families */
  --font-heading: 'Cinzel', Garamond, 'Times New Roman', serif;
  --font-body: 'Lora', Georgia, 'Times New Roman', serif;
  --font-accent: 'Cormorant Garamond', Georgia, serif;
  --font-handwritten: 'Dancing Script', cursive;
  
  /* Font Sizes (1.333 Perfect Fourth Scale) */
  --text-xs: 0.75rem;      /* 13.5px */
  --text-sm: 0.875rem;     /* 15.75px */
  --text-base: 1rem;       /* 18px */
  --text-lg: 1.333rem;     /* 24px */
  --text-xl: 1.777rem;     /* 32px */
  --text-2xl: 2.369rem;    /* 42.6px */
  --text-3xl: 3.157rem;    /* 56.8px */
  --text-4xl: 4.209rem;    /* 75.8px */
  
  /* Line Heights */
  --leading-body: 1.7;
  --leading-heading: 1.2;
  
  /* Letter Spacing */
  --tracking-heading: 0.02em;
}
```

```javascript
// tailwind.config.js typography
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        heading: ['Cinzel', 'Garamond', 'Times New Roman', 'serif'],
        body: ['Lora', 'Georgia', 'Times New Roman', 'serif'],
        accent: ['Cormorant Garamond', 'Georgia', 'serif'],
        handwritten: ['Dancing Script', 'cursive'],
      },
      fontSize: {
        'xs': '0.75rem',
        'sm': '0.875rem',
        'base': '1rem',
        'lg': '1.333rem',
        'xl': '1.777rem',
        '2xl': '2.369rem',
        '3xl': '3.157rem',
        '4xl': '4.209rem',
      },
      lineHeight: {
        'body': '1.7',
        'heading': '1.2',
      },
      letterSpacing: {
        'heading': '0.02em',
      },
    },
  },
}
```

**Google Fonts Import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet">
```

### Spacing

```css
:root {
  /* Spacing Scale */
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 1rem;      /* 16px */
  --space-4: 1.5rem;    /* 24px */
  --space-5: 2rem;      /* 32px */
  --space-6: 3rem;      /* 48px */
  --space-7: 4rem;      /* 64px */
  --space-8: 6rem;      /* 96px */
  --space-9: 8rem;      /* 128px */
  
  /* Section Gaps */
  --section-gap-sm: 5rem;    /* 80px */
  --section-gap-md: 7rem;    /* 112px */
  --section-gap-lg: 10rem;   /* 160px */
}
```

### Effects

```css
:root {
  /* Border Radius - soft but not bubbly */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-full: 9999px;
  
  /* Shadows - soft, atmospheric, NOT drop-shadow */
  --shadow-sm: 0 4px 20px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 8px 40px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 16px 60px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 40px rgba(212, 175, 55, 0.15);
  
  /* Transitions - SLOW and deliberate */
  --transition-fast: 0.3s ease-out;
  --transition-normal: 0.5s ease-out;
  --transition-slow: 0.8s ease-out;
  --transition-reveal: 1.2s ease-out;
}
```

---

## ✍️ CONTENT RULES

### Voice Personality
Wise but warm • Patient teacher • Respectful of tradition • Empowering not gatekeeping • Mystical but grounded

### Tone Spectrum
- **Formal ↔ Casual:** 6/10 - Respectful but approachable
- **Serious ↔ Playful:** 7/10 - Takes craft seriously, warm delivery
- **Technical ↔ Accessible:** 4/10 - Always accessible, never jargon-heavy

### Writing Style
- **Sentences:** Varied—short for emphasis, longer for explanation
- **Paragraphs:** 3-4 sentences typical, never walls of text
- **Vocabulary:** Accessible with craft-specific terms explained
- **Perspective:** Second person (you) for instructions, first person (we) for community

### ✅ USE These Phrases
- "Your practice"
- "The craft"
- "As you develop your skills"
- "Many practitioners find"
- "In traditional practice"
- "Consider your intention"
- "Trust your intuition"

### ❌ NEVER Use These Phrases
- "Transform your life"
- "Unlock your potential"
- "Ultimate guide to everything"
- "You won't believe"
- "Secret that experts don't want you to know"
- "Easy 5-minute spell"
- "This one weird trick"
- "As an AI language model"
- "It's important to note that"

### CTA Voice
**Style:** Invitation, not command

**Good CTAs:**
- "Begin Your Journey"
- "Enter the Circle"
- "Discover Your Path"
- "Light the Candle"
- "Explore the Grimoire"

**Bad CTAs (NEVER use):**
- "Learn More"
- "Get Started"
- "Click Here"
- "Submit"
- "Buy Now"
- "Sign Up"
- "Download Now"

---

## 🚫 ANTI-PATTERNS

### Layout - NEVER Do
- Hero → 3-column features → CTA (template trap)
- Centered-everything symmetry
- Generic blog grid as main content
- Sidebar on articles
- Mega menu navigation
- Sticky everything
- Footer with 5 identical columns

### Visual - NEVER Do
- Purple-to-blue gradients
- White backgrounds
- Pastel colors
- Neon accents
- Stock overlays
- Generic icon sets
- Material design shadows
- Perfectly rounded pill buttons

### Typography - NEVER Do
- Sans-serif headings
- Inter, Roboto, Arial ANYWHERE
- System font stack for headings
- All-caps body text
- Centered body paragraphs
- Justified text

### Content - NEVER Do
- Generic CTAs ("Learn More")
- "Welcome to our website"
- "Your one-stop shop"
- Clickbait headlines
- Excessive exclamation marks
- Emojis in body content

### Imagery - NEVER Do
- Stock witch costumes
- Halloween imagery
- Pentagram poses
- Black cat clichés
- Cauldron stereotypes
- AI-generated faces
- Harry Potter aesthetic

### Site-Specific Forbidden
- Appropriation of closed practices (Voodoo, Hoodoo without proper attribution)
- Trivializing the craft as aesthetic
- Fear-based content ("dangerous spells")
- Promising unrealistic results
- Gatekeeping or elitism
- Gendering witchcraft unnecessarily

### Immediate Rejection Triggers
If ANY of these are true, STOP and redesign:
- Looks like a WordPress theme demo
- Could work on any spiritual site
- Uses template layout patterns
- Hero could be anywhere
- Typography is generic sans-serif
- Colors are AI-generated purple/blue

---

## 🔧 TECHNICAL STACK

### Platform
- **CMS:** WordPress
- **Theme:** Blocksy with child theme
- **Page Builder:** Gutenberg blocks

### Required Plugins
- RankMath SEO Pro
- LiteSpeed Cache
- AI Engine
- WPCode Pro
- Complianz GDPR
- Wordfence Security
- UpdraftPlus Backup

### Performance Targets
| Metric | Target |
|--------|--------|
| PageSpeed Mobile | >80 |
| PageSpeed Desktop | >90 |
| LCP | <2.5s |
| FID | <100ms |
| CLS | <0.1 |
| TTFB | <600ms |

### Breakpoints
```css
/* Mobile First */
/* Base: < 768px (mobile) */
@media (min-width: 768px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1440px) { /* Wide */ }
```

---

## 🔍 SEO CONFIGURATION

### Primary Keywords
- witchcraft for beginners
- how to start witchcraft
- beginner witch
- learn witchcraft
- witchcraft basics

### Secondary Keywords
- spells for beginners
- moon magic
- witchcraft tools
- book of shadows
- wicca vs witchcraft

### Content Pillars
1. Beginner's Path
2. Spells & Rituals
3. Moon Magic
4. Tools & Supplies
5. Sabbats & Seasons

### Schema Types
- Article
- HowTo
- FAQPage
- WebSite
- Organization

### Internal Linking Strategy
Hub and spoke from pillar pages. Every post links to its pillar. Pillars link to each other.

### Content Depth Targets
- Pillar: 3000-5000 words
- Hub: 1500-2500 words
- Spoke: 1000-2000 words
- Support: 500-1000 words

---

## ✨ SIGNATURE ELEMENTS

### Must Include (Every Page)
1. **Moon Phase Indicator** - Current moon phase displayed subtly in header or footer
2. **Candle Glow Effect** - Subtle warm glow in hero sections (use `--shadow-glow`)
3. **Emergence Animation** - Content appearing from darkness (use `--transition-reveal`)

### Optional Flourishes
- Constellation patterns in spacious background areas
- Botanical border elements for special content
- Parchment texture overlay on cards
- Hand-drawn dividers between major sections

### Usage Rules
- Maximum 3 signature elements per page
- Place at entry points and section transitions
- These elements are special because they're rare—overuse makes them ordinary

---

## 📋 QUICK REFERENCE

### Most-Used Colors
| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| Deep Amethyst | `#4A1C6F` | `--color-primary` | Links, accents, UI |
| Candle Gold | `#D4AF37` | `--color-secondary` | Highlights, warmth |
| Night Sky | `#1A1A2E` | `--color-bg-primary` | Main background |
| Aged Parchment | `#E8E4D9` | `--color-text-primary` | Body text |

### Most-Used Typography
| Element | Font | Size | Weight |
|---------|------|------|--------|
| H1 | Cinzel | 4.209rem | 600-700 |
| H2 | Cinzel | 3.157rem | 600 |
| H3 | Cinzel | 2.369rem | 500 |
| Body | Lora | 1rem (18px) | 400 |
| Small | Lora | 0.875rem | 400 |

### Content Density
**Target:** 40% content / 60% whitespace
**Philosophy:** Content breathes like the pauses between incantations

### Motion
**Default transition:** `0.5s ease-out`
**Animation style:** Slow, deliberate, organic—like candle flames and turning pages
**Reveal animations:** `0.8s-1.2s` for meaningful content emergence

---

## 📁 PROJECT STRUCTURE

```
witchcraft-for-beginners/
├── CLAUDE.md              ◄── This file (source of truth)
├── .mcp/
│   └── config.json        ◄── WordPress MCP config
├── tokens/
│   ├── variables.css      ◄── CSS custom properties (copy from above)
│   └── tailwind.config.js ◄── Tailwind configuration
├── src/
│   └── blocksy-child/     ◄── Child theme customizations
└── content/
    └── drafts/            ◄── Content drafts
```

---

## 🚀 COMMON TASKS

### Starting Work
1. Read this CLAUDE.md (you're doing it now!)
2. Check current site state via WordPress MCP
3. Verify tokens match this file

### Making Design Changes
1. Reference Design Tokens section above
2. Use CSS variables: `var(--color-primary)`
3. Verify against Anti-Patterns before committing
4. Test on mobile—simplified but still atmospheric

### Writing Content
1. Check Content Rules section
2. Use encouraged phrases, avoid forbidden ones
3. Match the wise-but-warm voice
4. Include internal links to pillar content

### Adding New Sections
1. Use Emergence Animation for reveals
2. Maintain 40/60 content-to-whitespace ratio
3. Include at least one signature element
4. Break grid every 6-8 cards with featured content

---

## ⚠️ CRITICAL REMINDERS

1. **This file is the source of truth** - Don't fetch external skills
2. **All values are ready to use** - Copy/paste directly into code
3. **Check Anti-Patterns before every commit** - If it could work on any spiritual site, it's wrong
4. **DARK MODE FIRST** - Light background = instant rejection
5. **NO SANS-SERIF HEADINGS** - Cinzel or nothing
6. **Slow animations** - 0.5s minimum, nothing bouncy
7. **Voice consistency** - Wise but warm, invitation not command

---

## 🌙 THE VIBE CHECK

Before deploying anything, ask yourself:

> *Can you FEEL the candle warmth through the screen?*
> 
> *Would a visitor pause on arrival—is the atmosphere tangible?*
> 
> *Does the typography feel like reading an ancient book?*
> 
> *Would a professional designer screenshot this for inspiration?*

If no to any of these, iterate until yes.

---

*Generated by CLAUDE.md Generator from WitchcraftForBeginners DNA v2.0.0*
