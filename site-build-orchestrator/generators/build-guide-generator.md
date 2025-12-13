# Build Guide Generator

## Purpose

Transforms a DNA file from Creative Command Center into a complete build package:
- BUILD-GUIDE.md (step-by-step prompts)
- PREFLIGHT-CHECKLIST.md (pre-build verification)
- PHASE-CHECKPOINTS.md (QA between phases)
- PLUGIN-MANIFEST.md (all plugins with configs)

---

## Input Required

1. **DNA File** - The site's DNA from Creative Command Center
2. **Site Status** - New build, redesign, or upgrade
3. **Current State** - What exists already (if anything)

---

## Generation Process

### Step 1: Parse DNA

Extract from DNA file:

```javascript
// Core Identity
site_id           → {{SITE_SLUG}}
site_name         → {{SITE_NAME}}
url               → {{SITE_URL}}
archetype         → Informs hero/voice
soul              → Informs all messaging

// Colors
colors.palette.primary.hex     → {{COLOR_PRIMARY}}
colors.palette.secondary.hex   → {{COLOR_SECONDARY}}
colors.palette.accent.hex      → {{COLOR_ACCENT}}
colors.palette.background_*.hex → {{COLOR_BG_*}}
colors.palette.text_*.hex      → {{COLOR_TEXT_*}}
colors.mode                    → {{COLOR_MODE}}

// Typography
typography.headings.primary_font  → {{FONT_HEADING}}
typography.body.primary_font      → {{FONT_BODY}}
typography.type_scale.*           → {{TYPE_*}}
typography.body.line_height       → {{LINE_HEIGHT_BODY}}

// Visual Philosophy
visual_philosophy.density.content_to_whitespace_ratio → {{DENSITY_RATIO}}
visual_philosophy.motion.speed    → {{TRANSITION_*}}
visual_philosophy.shape_language.border_radius_philosophy → {{RADIUS_*}}

// Layout
layout_constitution.homepage.*     → Homepage build specs
layout_constitution.category_pages.* → Category specs
layout_constitution.single_posts.* → Post specs
layout_constitution.spacing_rhythm.* → {{SPACING_*}}

// Navigation
navigation.primary_nav.*  → {{PRIMARY_NAV_*}}
navigation.mobile_nav.*   → {{MOBILE_NAV_*}}

// Signature Elements
signature_elements.must_include → {{SIGNATURE_ELEMENTS}}

// Voice
voice.* → Content voice specs
voice.cta_voice.* → {{CTA_*}}

// Technical
technical.performance_targets.* → {{PERF_*}}

// SEO
seo.primary_keywords → {{SEO_PRIMARY_KEYWORDS}}
seo.content_pillars → {{PILLAR_PAGES}}
```

### Step 2: Generate CSS Tokens

Transform color and typography values into CSS custom properties:

```css
:root {
  /* Colors from DNA */
  --color-primary: [colors.palette.primary.hex];
  --color-secondary: [colors.palette.secondary.hex];
  /* ... etc */
  
  /* Typography from DNA */
  --font-heading: [typography.headings.primary_font];
  --font-body: [typography.body.primary_font];
  /* ... etc */
}
```

### Step 3: Generate Site-Specific Sections

Based on DNA characteristics, generate appropriate:

**Hero Section:**
- If archetype is "Magician" → emergence/reveal animation
- If archetype is "Sage" → scholarly, calm intro
- If archetype is "Caregiver" → warm, welcoming embrace
- If archetype is "Hero" → bold, action-oriented
- etc.

**Homepage Sections:**
- Based on content_categories in DNA
- Based on audience personas

**Signature Elements:**
- Extract from signature_elements.must_include
- Include placement and frequency rules

### Step 4: Determine Site-Specific Plugins

Based on DNA site_id and niche:

```
witchcraft-for-beginners:
  - WP Recipe Maker (for spell/ritual "recipes")
  - Custom moon phase widget
  - Dark mode forced

smart-home-wizards:
  - Comparison table plugin
  - Product schema extension
  - Affiliate link manager

family-flourish:
  - Age-gating for some content
  - Pinterest optimizations
  - Recipe card schema

ai-in-action-hub:
  - Code syntax highlighting
  - Tool embed support
  - Dark mode toggle
```

### Step 5: Generate Anti-Pattern Warnings

From DNA anti_patterns section, create specific warnings:

```
NEVER DO (from DNA):
[List each item from anti_patterns.layout_forbidden]
[List each item from anti_patterns.visual_forbidden]
[List each item from anti_patterns.typography_forbidden]
...
```

### Step 6: Generate Quality Tests

From DNA quality_benchmarks section:

```
Before considering complete:
- [List what_perfect_looks_like items as questions]
- Run: [tests.screenshot_test]
- Run: [tests.swap_test]
- etc.
```

---

## Template Variable Mapping

### Identity Variables
| Variable | DNA Path |
|----------|----------|
| {{SITE_NAME}} | Top-level or derived from site_id |
| {{SITE_SLUG}} | site_id |
| {{SITE_URL}} | url |
| {{DNA_VERSION}} | evolution.version |

### Color Variables
| Variable | DNA Path |
|----------|----------|
| {{COLOR_PRIMARY}} | colors.palette.primary.hex |
| {{COLOR_SECONDARY}} | colors.palette.secondary.hex |
| {{COLOR_ACCENT}} | colors.palette.accent.hex |
| {{COLOR_BG_PRIMARY}} | colors.palette.background_primary.hex |
| {{COLOR_BG_SECONDARY}} | colors.palette.background_secondary.hex |
| {{COLOR_BG_TERTIARY}} | colors.palette.background_tertiary.hex |
| {{COLOR_TEXT_PRIMARY}} | colors.palette.text_primary.hex |
| {{COLOR_TEXT_SECONDARY}} | colors.palette.text_secondary.hex |
| {{COLOR_TEXT_MUTED}} | colors.palette.text_muted.hex |
| {{COLOR_MODE}} | colors.mode |

### Typography Variables
| Variable | DNA Path |
|----------|----------|
| {{FONT_HEADING}} | typography.headings.primary_font |
| {{FONT_HEADING_WEIGHT}} | typography.headings.weight_range (max) |
| {{FONT_BODY}} | typography.body.primary_font |
| {{FONT_BODY_WEIGHT}} | typography.body.weight |
| {{FONT_ACCENT}} | typography.accent.font |
| {{TYPE_BASE}} | typography.type_scale.base_size |
| {{TYPE_*}} | typography.type_scale.scale_values.* |
| {{LINE_HEIGHT_BODY}} | typography.body.line_height |
| {{LINE_HEIGHT_HEADING}} | typography.headings... (derive) |
| {{LETTER_SPACING_HEADING}} | typography.headings.letter_spacing |

### Layout Variables
| Variable | DNA Path |
|----------|----------|
| {{SECTION_GAP}} | layout_constitution.spacing_rhythm.section_gap_range |
| {{DENSITY_RATIO}} | visual_philosophy.density.content_to_whitespace_ratio |
| {{CONTAINER_MAX_WIDTH}} | Derive from layout or use 1440px default |
| {{CONTENT_MAX_WIDTH}} | layout_constitution.single_posts.max_width |

### Effect Variables
| Variable | DNA Path |
|----------|----------|
| {{RADIUS_SM}} | Derive from visual_philosophy.shape_language |
| {{RADIUS_MD}} | Derive from visual_philosophy.shape_language |
| {{RADIUS_LG}} | Derive from visual_philosophy.shape_language |
| {{TRANSITION_FAST}} | Derive from visual_philosophy.motion.speed |
| {{TRANSITION_NORMAL}} | Derive from visual_philosophy.motion.speed |
| {{TRANSITION_SLOW}} | Derive from visual_philosophy.motion.speed |

### Navigation Variables
| Variable | DNA Path |
|----------|----------|
| {{PRIMARY_NAV_ITEMS}} | navigation.primary_nav.required_items |
| {{NAV_MAX_ITEMS}} | navigation.primary_nav.max_items |
| {{MOBILE_NAV_TYPE}} | navigation.mobile_nav.style |
| {{NAV_PHILOSOPHY}} | navigation.philosophy |

### Performance Variables
| Variable | DNA Path |
|----------|----------|
| {{PERF_MOBILE}} | technical.performance_targets.pagespeed_mobile |
| {{PERF_DESKTOP}} | technical.performance_targets.pagespeed_desktop |
| {{PERF_LCP}} | technical.performance_targets.lcp |
| {{PERF_FID}} | technical.performance_targets.fid |
| {{PERF_CLS}} | technical.performance_targets.cls |

---

## Usage

### In Claude.ai:

```
Generate a complete build package for [SiteName] using the Site Build Orchestrator.

Read the DNA file from Creative Command Center:
/mnt/skills/user/creative-command-center/brains/[site-slug].json

Generate:
1. BUILD-GUIDE.md
2. PREFLIGHT-CHECKLIST.md
3. PHASE-CHECKPOINTS.md
4. PLUGIN-MANIFEST.md

Save all files to /mnt/user-data/outputs/[site-slug]/
```

### Batch Generation:

```
Generate build packages for all 16 sites in Creative Command Center.
Use Site Build Orchestrator to create complete packages for each.
Save to /mnt/user-data/outputs/[site-slug]/ for each site.
```

---

## Quality Requirements

Generated files must:
1. Have NO generic placeholders remaining
2. Be completely site-specific
3. Match DNA exactly
4. Include all anti-patterns as warnings
5. Include all quality tests
6. Be ready to use immediately in Claude Code
