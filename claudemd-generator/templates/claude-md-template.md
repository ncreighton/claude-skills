# {{SITE_NAME}} - Claude Code Project

> **Generated:** {{GENERATED_DATE}}  
> **DNA Version:** {{DNA_VERSION}}  
> **Site URL:** {{SITE_URL}}

---

## 🎯 IDENTITY

### Who This Site Is
{{ARCHETYPE_EXPRESSION}}

### Soul Statement
> {{SOUL_ONE_SENTENCE}}

{{SOUL_EXPANDED}}

### Emotional Tone
- **Primary:** {{EMOTIONAL_PRIMARY}}
- **Secondary:** {{EMOTIONAL_SECONDARY}}
- **Range:** {{EMOTIONAL_RANGE}}
- **NEVER:** {{EMOTIONAL_FORBIDDEN}}

---

## 🎨 DESIGN TOKENS

### Colors

```css
/* CSS Custom Properties - paste into your stylesheet */
:root {
  /* Primary Palette */
  --color-primary: {{COLOR_PRIMARY_HEX}};
  --color-secondary: {{COLOR_SECONDARY_HEX}};
  --color-accent: {{COLOR_ACCENT_HEX}};
  
  /* Backgrounds */
  --color-bg-primary: {{COLOR_BG_PRIMARY}};
  --color-bg-secondary: {{COLOR_BG_SECONDARY}};
  --color-bg-tertiary: {{COLOR_BG_TERTIARY}};
  
  /* Text */
  --color-text-primary: {{COLOR_TEXT_PRIMARY}};
  --color-text-secondary: {{COLOR_TEXT_SECONDARY}};
  --color-text-muted: {{COLOR_TEXT_MUTED}};
  
  /* Semantic */
  --color-success: {{COLOR_SUCCESS}};
  --color-warning: {{COLOR_WARNING}};
  --color-error: {{COLOR_ERROR}};
  --color-info: {{COLOR_INFO}};
}

/* Dark mode (if applicable) */
{{DARK_MODE_VARIABLES}}
```

```javascript
// tailwind.config.js colors
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '{{COLOR_PRIMARY_HEX}}',
        secondary: '{{COLOR_SECONDARY_HEX}}',
        accent: '{{COLOR_ACCENT_HEX}}',
        background: {
          DEFAULT: '{{COLOR_BG_PRIMARY}}',
          secondary: '{{COLOR_BG_SECONDARY}}',
          tertiary: '{{COLOR_BG_TERTIARY}}',
        },
        foreground: {
          DEFAULT: '{{COLOR_TEXT_PRIMARY}}',
          secondary: '{{COLOR_TEXT_SECONDARY}}',
          muted: '{{COLOR_TEXT_MUTED}}',
        },
      },
    },
  },
}
```

### Typography

```css
:root {
  /* Font Families */
  --font-heading: {{FONT_HEADING}};
  --font-body: {{FONT_BODY}};
  --font-accent: {{FONT_ACCENT}};
  
  /* Font Sizes (using {{TYPE_SCALE_RATIO}} scale) */
  --text-xs: {{TYPE_XS}};
  --text-sm: {{TYPE_SM}};
  --text-base: {{TYPE_BASE}};
  --text-lg: {{TYPE_LG}};
  --text-xl: {{TYPE_XL}};
  --text-2xl: {{TYPE_2XL}};
  --text-3xl: {{TYPE_3XL}};
  --text-4xl: {{TYPE_4XL}};
  
  /* Line Heights */
  --leading-body: {{LINE_HEIGHT_BODY}};
  --leading-heading: {{LINE_HEIGHT_HEADING}};
  
  /* Letter Spacing */
  --tracking-heading: {{LETTER_SPACING_HEADING}};
}
```

```javascript
// tailwind.config.js typography
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        heading: [{{FONT_HEADING_ARRAY}}],
        body: [{{FONT_BODY_ARRAY}}],
        accent: [{{FONT_ACCENT_ARRAY}}],
      },
      fontSize: {
        'xs': '{{TYPE_XS}}',
        'sm': '{{TYPE_SM}}',
        'base': '{{TYPE_BASE}}',
        'lg': '{{TYPE_LG}}',
        'xl': '{{TYPE_XL}}',
        '2xl': '{{TYPE_2XL}}',
        '3xl': '{{TYPE_3XL}}',
        '4xl': '{{TYPE_4XL}}',
      },
    },
  },
}
```

**Google Fonts Import:**
```html
<link href="https://fonts.googleapis.com/css2?family={{GOOGLE_FONTS_STRING}}&display=swap" rel="stylesheet">
```

### Spacing

```css
:root {
  /* Spacing Scale */
  {{SPACING_VARIABLES}}
  
  /* Section Gaps */
  --section-gap-sm: {{SECTION_GAP_SM}};
  --section-gap-md: {{SECTION_GAP_MD}};
  --section-gap-lg: {{SECTION_GAP_LG}};
}
```

```javascript
// tailwind.config.js spacing (extends default)
module.exports = {
  theme: {
    extend: {
      spacing: {
        {{TAILWIND_SPACING}}
      },
    },
  },
}
```

### Effects

```css
:root {
  /* Border Radius */
  --radius-sm: {{RADIUS_SM}};
  --radius-md: {{RADIUS_MD}};
  --radius-lg: {{RADIUS_LG}};
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: {{SHADOW_SM}};
  --shadow-md: {{SHADOW_MD}};
  --shadow-lg: {{SHADOW_LG}};
  
  /* Transitions */
  --transition-fast: {{TRANSITION_FAST}};
  --transition-normal: {{TRANSITION_NORMAL}};
  --transition-slow: {{TRANSITION_SLOW}};
}
```

---

## ✍️ CONTENT RULES

### Voice Personality
{{VOICE_PERSONALITY_TRAITS}}

### Tone Spectrum
- **Formal ↔ Casual:** {{TONE_FORMAL_CASUAL}}/10
- **Serious ↔ Playful:** {{TONE_SERIOUS_PLAYFUL}}/10
- **Technical ↔ Accessible:** {{TONE_TECHNICAL_ACCESSIBLE}}/10

### Writing Style
- **Sentences:** {{WRITING_SENTENCE_LENGTH}}
- **Paragraphs:** {{WRITING_PARAGRAPH_LENGTH}}
- **Vocabulary:** {{WRITING_VOCABULARY}}
- **Perspective:** {{WRITING_PERSPECTIVE}}

### ✅ USE These Phrases
{{ENCOURAGED_PHRASES}}

### ❌ NEVER Use These Phrases
{{FORBIDDEN_PHRASES}}

### CTA Voice
**Style:** {{CTA_STYLE}}

**Good CTAs:**
{{CTA_EXAMPLES}}

**Bad CTAs (never use):**
{{CTA_FORBIDDEN}}

---

## 🚫 ANTI-PATTERNS

### Layout - NEVER Do
{{ANTI_LAYOUT}}

### Visual - NEVER Do
{{ANTI_VISUAL}}

### Typography - NEVER Do
{{ANTI_TYPOGRAPHY}}

### Content - NEVER Do
{{ANTI_CONTENT}}

### Imagery - NEVER Do
{{ANTI_IMAGERY}}

### Site-Specific Forbidden
{{ANTI_SITE_SPECIFIC}}

### Immediate Rejection Triggers
If you see ANY of these, stop and fix:
{{REJECTION_TRIGGERS}}

---

## 🔧 TECHNICAL STACK

### Platform
- **CMS:** {{PLATFORM_CMS}}
- **Theme:** {{PLATFORM_THEME}}
- **Page Builder:** {{PLATFORM_BUILDER}}

### Required Plugins
{{REQUIRED_PLUGINS}}

### Performance Targets
| Metric | Target |
|--------|--------|
| PageSpeed Mobile | {{PERF_MOBILE}} |
| PageSpeed Desktop | {{PERF_DESKTOP}} |
| LCP | {{PERF_LCP}} |
| FID | {{PERF_FID}} |
| CLS | {{PERF_CLS}} |

### Breakpoints
```css
/* Mobile First */
/* Base: < {{BP_MOBILE}} */
@media (min-width: {{BP_TABLET}}) { /* Tablet */ }
@media (min-width: {{BP_DESKTOP}}) { /* Desktop */ }
@media (min-width: {{BP_WIDE}}) { /* Wide */ }
```

---

## 🔍 SEO CONFIGURATION

### Primary Keywords
{{SEO_PRIMARY_KEYWORDS}}

### Content Pillars
{{SEO_CONTENT_PILLARS}}

### Schema Types
{{SEO_SCHEMA_TYPES}}

### Internal Linking Strategy
{{SEO_LINKING_STRATEGY}}

---

## 📋 QUICK REFERENCE

### Most-Used Colors
| Name | Hex | Usage |
|------|-----|-------|
| Primary | `{{COLOR_PRIMARY_HEX}}` | {{COLOR_PRIMARY_USAGE}} |
| Secondary | `{{COLOR_SECONDARY_HEX}}` | {{COLOR_SECONDARY_USAGE}} |
| Background | `{{COLOR_BG_PRIMARY}}` | Main background |
| Text | `{{COLOR_TEXT_PRIMARY}}` | Body text |

### Most-Used Typography
| Element | Font | Size | Weight |
|---------|------|------|--------|
| H1 | {{FONT_HEADING_NAME}} | {{TYPE_4XL}} | {{FONT_HEADING_WEIGHT_MAX}} |
| H2 | {{FONT_HEADING_NAME}} | {{TYPE_3XL}} | {{FONT_HEADING_WEIGHT_MAX}} |
| Body | {{FONT_BODY_NAME}} | {{TYPE_BASE}} | {{FONT_BODY_WEIGHT}} |
| Small | {{FONT_BODY_NAME}} | {{TYPE_SM}} | {{FONT_BODY_WEIGHT}} |

### Content Density
**Target:** {{DENSITY_RATIO}} (content to whitespace)

### Motion
**Default transition:** `{{TRANSITION_NORMAL}}`
**Animation style:** {{MOTION_STYLE}}

---

## 📁 PROJECT STRUCTURE

```
{{SITE_SLUG}}/
├── CLAUDE.md              ◄── This file
├── .mcp/
│   └── config.json        ◄── MCP server configs
├── tokens/
│   ├── variables.css      ◄── CSS custom properties
│   └── tailwind.config.js ◄── Tailwind configuration
├── src/                   ◄── Theme/plugin code
└── content/               ◄── Content drafts
```

---

## 🚀 COMMON TASKS

### Starting Work
1. Read this CLAUDE.md first
2. Check current site state via MCP
3. Verify tokens match this file

### Making Design Changes
1. Reference Design Tokens section
2. Use CSS variables or Tailwind classes
3. Verify against Anti-Patterns before committing

### Writing Content
1. Check Content Rules section
2. Use encouraged phrases
3. Match voice personality
4. Verify no forbidden phrases

### Deploying
1. Test against Performance Targets
2. Verify mobile responsiveness
3. Check PageSpeed score
4. Deploy to {{DEPLOYMENT_TARGET}}

---

## ⚠️ CRITICAL REMINDERS

1. **This file is the source of truth** - don't fetch external skills
2. **All values are ready to use** - copy/paste into code
3. **Check Anti-Patterns before every commit**
4. **Voice consistency matters** - {{VOICE_REMINDER}}
5. **When in doubt, refer to Identity section**

---

*Generated by CLAUDE.md Generator from {{SITE_NAME}} DNA v{{DNA_VERSION}}*
