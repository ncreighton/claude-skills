---
name: site-design-auditor
description: Comprehensive design system auditor for multi-site WordPress networks. Crawls sites for CSS inconsistencies, validates brand colors/fonts against Figma specs, flags accessibility issues, generates visual regression screenshots, optimizes images, subsets fonts, and syncs design tokens. Works in Claude.ai and Claude Code terminal. Use when user needs to audit site design, check CSS consistency, validate brand compliance, run visual QA, optimize images, subset fonts, sync design tokens, detect CSS regressions, or fix styling issues. Triggers include "audit design", "check CSS", "brand compliance", "visual regression", "design tokens", "font subset", "image optimize", "CSS inconsistency", "accessibility audit", "design system sync", "Figma tokens", or any design quality requests across websites.
---

# Site Design Auditor

Complete design system audit, validation, and optimization toolkit for multi-site networks.

## Core Capabilities

1. **CSS Consistency Auditor** - Detect inconsistencies across sites
2. **Brand Compliance Checker** - Validate against Figma specs
3. **Accessibility Auditor** - WCAG contrast, font sizes, focus states
4. **Visual Regression Testing** - Screenshot comparisons
5. **Design Token Pipeline** - Figma → CSS Variables → All Sites
6. **Image Optimizer** - Batch compress and convert
7. **Font Subsetter** - Reduce web font file sizes

## Quick Start

### Audit Single Site
```bash
python scripts/css_auditor.py https://smarthomewizards.com
```

### Audit All 17 Sites
```bash
python scripts/batch_auditor.py --config sites.json
```

### Full Design System Sync
```bash
python scripts/design_token_pipeline.py --figma-file YOUR_FILE_KEY --output ./tokens
```

## Workflow: Complete Site Audit

1. **Extract Design Tokens** → Pull from Figma
2. **Generate CSS Variables** → Create site-specific CSS
3. **Crawl Sites** → Detect CSS inconsistencies
4. **Check Brand Compliance** → Compare to Figma specs
5. **Run Accessibility Audit** → WCAG validation
6. **Capture Screenshots** → Visual baseline
7. **Optimize Assets** → Images and fonts
8. **Generate Report** → Actionable fixes per site

## Tool Selection Guide

| Task | Script | MCP Alternative |
|------|--------|-----------------|
| CSS audit | `css_auditor.py` | - |
| Visual regression | `visual_qa.py` | Playwright MCP |
| Brand check | `brand_compliance.py` | Figma MCP |
| Token sync | `design_token_pipeline.py` | Figma MCP |
| Image optimize | `image_optimizer.py` | - |
| Font subset | `font_subsetter.py` | - |
| Accessibility | `a11y_auditor.py` | - |

## Scripts Reference

### css_auditor.py
Crawls site and reports CSS inconsistencies.
```bash
python scripts/css_auditor.py URL [--output report.json] [--depth 3]
```

**Detects:**
- Inline styles that override brand CSS
- !important abuse
- Unused CSS variables
- Inconsistent font stacks
- Color values not matching tokens
- Breakpoint inconsistencies

### brand_compliance.py
Validates site against Figma design tokens.
```bash
python scripts/brand_compliance.py URL --tokens tokens.json
```

**Validates:**
- Primary/secondary colors match
- Typography scale compliance
- Spacing system adherence
- Component consistency

### a11y_auditor.py
WCAG 2.1 AA compliance checker.
```bash
python scripts/a11y_auditor.py URL [--level AA|AAA]
```

**Checks:**
- Color contrast ratios (4.5:1 text, 3:1 large)
- Focus indicators
- Font size minimums (16px body)
- Touch target sizes (44x44px)
- Alt text presence
- Heading hierarchy

### visual_qa.py
Screenshot comparison for regression detection.
```bash
python scripts/visual_qa.py URL --baseline ./baselines --output ./diffs
```

**Features:**
- Full page screenshots
- Viewport breakpoint testing
- Pixel-diff comparison
- Change highlighting
- Threshold configuration

### design_token_pipeline.py
Figma → CSS Variables → WordPress Sites
```bash
python scripts/design_token_pipeline.py \
  --figma-file FILE_KEY \
  --figma-token FIGMA_TOKEN \
  --output ./tokens
```

**Pipeline:**
1. Extract variables from Figma
2. Transform to CSS custom properties
3. Generate per-site theme files
4. Push to WordPress via REST API

### image_optimizer.py
Batch image optimization.
```bash
python scripts/image_optimizer.py ./images --output ./optimized [--format webp]
```

**Optimizations:**
- WebP conversion
- JPEG quality optimization
- PNG compression
- Responsive srcset generation
- Lazy loading attributes

### font_subsetter.py
Reduce font file sizes by subsetting.
```bash
python scripts/font_subsetter.py ./fonts --output ./subsets [--chars latin]
```

**Options:**
- Latin, Latin-Extended, custom ranges
- WOFF2 output
- Usage analysis mode

## Configuration

### sites.json (Multi-Site Config)
```json
{
  "sites": [
    {
      "name": "Smart Home Wizards",
      "url": "https://smarthomewizards.com",
      "brand": "smarthome",
      "tokens": "tokens/smarthome.json"
    },
    {
      "name": "Witchcraft For Beginners",
      "url": "https://witchcraftforbeginners.com",
      "brand": "witchcraft",
      "tokens": "tokens/witchcraft.json"
    }
  ]
}
```

### tokens.json (Design Token Format)
```json
{
  "colors": {
    "primary": "#4A90D9",
    "secondary": "#2C3E50",
    "accent": "#E74C3C",
    "background": "#FFFFFF",
    "text": "#333333"
  },
  "typography": {
    "fontFamily": {
      "heading": "Montserrat, sans-serif",
      "body": "Open Sans, sans-serif"
    },
    "fontSize": {
      "h1": "2.5rem",
      "h2": "2rem",
      "h3": "1.75rem",
      "body": "1rem",
      "small": "0.875rem"
    }
  },
  "spacing": {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "2rem",
    "xl": "4rem"
  }
}
```

## n8n Integration

### Visual QA Automation Workflow
```
Trigger (Daily 2am) 
  → Run visual_qa.py on all sites
  → Compare to baselines
  → If diff > threshold
    → Send Slack alert
    → Create GitHub issue
  → Update baselines weekly
```

### Token Sync Workflow
```
Trigger (Figma webhook)
  → Extract updated tokens
  → Generate CSS files
  → Push to all 17 sites
  → Clear CDN cache
  → Notify completion
```

## Output Formats

### Audit Report (JSON)
```json
{
  "site": "smarthomewizards.com",
  "timestamp": "2024-01-15T10:30:00Z",
  "issues": [
    {
      "type": "css_inconsistency",
      "severity": "high",
      "location": "/",
      "selector": ".hero-title",
      "expected": "var(--color-primary)",
      "actual": "#random-color",
      "fix": "Replace inline color with CSS variable"
    }
  ],
  "summary": {
    "total_issues": 12,
    "high": 3,
    "medium": 6,
    "low": 3
  }
}
```

### Visual Diff Report (HTML)
Generated at `./reports/visual-diff-{date}.html` with:
- Side-by-side screenshots
- Highlighted differences
- Direct links to affected pages

## Claude Code Usage

In Claude Code terminal:
```bash
# Quick audit
cd /path/to/skill && python scripts/css_auditor.py https://yoursite.com

# Full pipeline
python scripts/design_token_pipeline.py --figma-file abc123 && \
python scripts/batch_auditor.py --config sites.json && \
python scripts/visual_qa.py https://yoursite.com
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Figma API rate limit | Add delay between requests, batch queries |
| Large site timeout | Increase depth limit, use sitemap |
| Screenshot differences | Check viewport size, wait for fonts |
| Token sync failed | Verify WordPress REST API credentials |

## Dependencies

```bash
pip install requests beautifulsoup4 Pillow fonttools brotli cssutils selenium playwright aiohttp
```

For Claude Code, ensure these are in your environment.

## Resources

- **references/brand-tokens/** - Token files per site vertical
- **references/wcag-checklist.md** - WCAG 2.1 requirements
- **assets/report-template.html** - HTML report template
- **scripts/** - All executable audit scripts
