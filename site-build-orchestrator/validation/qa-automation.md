# Validation & QA Automation

## Automated Quality Assurance System

This system provides automated checks to validate sites against their DNA specifications, catch issues early, and maintain quality standards across all 17 sites.

---

## Validation Categories

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        VALIDATION PYRAMID                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│                    ┌─────────────────┐                                   │
│                    │   DNA MATCH     │  ← Does site match specs?         │
│                    └─────────────────┘                                   │
│              ┌───────────────────────────┐                               │
│              │    TECHNICAL HEALTH       │  ← Is site working?           │
│              └───────────────────────────┘                               │
│        ┌─────────────────────────────────────┐                           │
│        │       PERFORMANCE METRICS           │  ← Is site fast?          │
│        └─────────────────────────────────────┘                           │
│  ┌───────────────────────────────────────────────┐                       │
│  │           SEO COMPLIANCE                       │  ← Is site optimized?│
│  └───────────────────────────────────────────────┘                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 1. DNA Compliance Validation

### Color Validation

```yaml
test: color_compliance
description: Verify site colors match DNA specification

checks:
  - name: primary_color
    expected: "{{DNA.colors.palette.primary.hex}}"
    locations:
      - "css: --color-primary"
      - "blocksy: global_colors.color_1"
      - "headers/buttons visible elements"
    tolerance: "exact match"

  - name: secondary_color
    expected: "{{DNA.colors.palette.secondary.hex}}"
    locations:
      - "css: --color-secondary"
      - "blocksy: global_colors.color_2"
    tolerance: "exact match"

  - name: background_primary
    expected: "{{DNA.colors.palette.background_primary.hex}}"
    locations:
      - "css: --color-bg-primary"
      - "body background-color"
    tolerance: "exact match"

  - name: text_primary
    expected: "{{DNA.colors.palette.text_primary.hex}}"
    locations:
      - "css: --color-text-primary"
      - "body color"
    tolerance: "exact match"

  - name: no_forbidden_colors
    forbidden:
      - "#FFFFFF" (if dark mode site)
      - Generic grays not in palette
    check: "Scan all CSS for non-palette colors"
```

### Typography Validation

```yaml
test: typography_compliance
description: Verify fonts match DNA specification

checks:
  - name: heading_font
    expected: "{{DNA.typography.headings.primary_font}}"
    locations:
      - "h1, h2, h3, h4, h5, h6 font-family"
      - "@font-face declarations"
      - "Google Fonts import"
    
  - name: body_font
    expected: "{{DNA.typography.body.primary_font}}"
    locations:
      - "body font-family"
      - "p font-family"
    
  - name: font_loading
    check: "Verify fonts in Network tab"
    expect: "All specified fonts loading"
    
  - name: no_sans_serif_headings
    if: DNA.anti_patterns.typography_forbidden includes "sans-serif headings"
    check: "h1-h6 font-family"
    expect: "No sans-serif fonts"
```

### Voice Validation (Content Check)

```yaml
test: voice_compliance
description: Sample content matches DNA voice

checks:
  - name: forbidden_phrases
    forbidden: "{{DNA.voice.forbidden_phrases}}"
    scan: "All published content"
    alert_if: "Any match found"
    
  - name: cta_style
    check: "Button text across site"
    forbidden: 
      - "Learn More"
      - "Click Here"
      - "Submit"
    expected_style: "{{DNA.voice.cta_voice}}"
    
  - name: tone_consistency
    sample: "Random 5 posts"
    check: "Against DNA voice guidelines"
    method: "Manual or AI review"
```

---

## 2. Technical Health Validation

### Core Functionality

```yaml
test: core_functionality
description: Essential site functions work

checks:
  - name: homepage_loads
    url: "{{site_url}}"
    expect: "HTTP 200"
    timeout: "10s"
    
  - name: ssl_valid
    check: "SSL certificate"
    expect: 
      - "Valid"
      - "Not expiring within 30 days"
      - "Correct domain"
      
  - name: no_mixed_content
    check: "HTTPS page loading HTTP resources"
    expect: "No mixed content warnings"
    
  - name: admin_accessible
    url: "{{site_url}}/wp-admin/"
    expect: "Login page loads"
    
  - name: forms_functional
    test: "Submit contact form"
    expect: "Success message, email received"
```

### Plugin Health

```yaml
test: plugin_health
description: All plugins functioning

checks:
  - name: no_php_errors
    check: "/wp-content/debug.log"
    expect: "No fatal errors, minimal warnings"
    
  - name: plugin_updates
    check: "Plugins needing updates"
    warn_if: ">3 plugins outdated"
    alert_if: "Security vulnerability reported"
    
  - name: plugin_conflicts
    check: "Console errors on page load"
    expect: "No plugin-related JS errors"
    
  - name: required_plugins_active
    required:
      - "wordfence/wordfence.php"
      - "litespeed-cache/litespeed-cache.php"
      - "seo-by-rank-math/rank-math.php"
      - "updraftplus/updraftplus.php"
    expect: "All required plugins active"
```

### Database Health

```yaml
test: database_health
description: Database performing well

checks:
  - name: database_size
    check: "Total database size"
    warn_if: ">500MB"
    suggest: "Run optimization"
    
  - name: table_overhead
    check: "Table fragmentation"
    warn_if: ">50MB overhead"
    suggest: "Optimize tables"
    
  - name: orphaned_data
    check:
      - "Orphaned post meta"
      - "Orphaned comment meta"
      - "Spam comments"
      - "Trashed items"
    suggest: "Clean if significant"
```

---

## 3. Performance Validation

### Page Speed

```yaml
test: pagespeed_validation
description: Site meets performance targets

checks:
  - name: homepage_mobile
    api: "PageSpeed Insights"
    url: "{{site_url}}"
    device: "mobile"
    target: "{{DNA.technical.performance_targets.pagespeed_mobile}}"
    
  - name: homepage_desktop
    api: "PageSpeed Insights"
    url: "{{site_url}}"
    device: "desktop"
    target: "{{DNA.technical.performance_targets.pagespeed_desktop}}"
    
  - name: sample_post
    api: "PageSpeed Insights"
    url: "{{site_url}}/sample-post/"
    targets: "Same as homepage"
```

### Core Web Vitals

```yaml
test: core_web_vitals
description: CWV meet thresholds

checks:
  - name: LCP
    target: "{{DNA.technical.performance_targets.lcp}}"
    threshold: "<2.5s good, <4s needs improvement"
    
  - name: FID_INP
    target: "{{DNA.technical.performance_targets.fid}}"
    threshold: "<100ms good, <300ms needs improvement"
    
  - name: CLS
    target: "{{DNA.technical.performance_targets.cls}}"
    threshold: "<0.1 good, <0.25 needs improvement"
```

### Asset Optimization

```yaml
test: asset_optimization
description: Images and assets optimized

checks:
  - name: image_optimization
    check: "Images on homepage"
    expect:
      - "WebP format or compressed"
      - "Proper sizing (not oversized)"
      - "Lazy loading below fold"
      
  - name: css_optimization
    check: "CSS delivery"
    expect:
      - "Minified"
      - "Critical CSS inlined (if configured)"
      - "Non-critical deferred"
      
  - name: js_optimization
    check: "JavaScript delivery"
    expect:
      - "Minified"
      - "Deferred or async"
      - "No render-blocking"
```

---

## 4. SEO Validation

### On-Page SEO

```yaml
test: onpage_seo
description: SEO fundamentals in place

checks:
  - name: meta_titles
    sample: "10 random pages"
    expect:
      - "Title present"
      - "Under 60 characters"
      - "Keyword included"
      - "Unique per page"
      
  - name: meta_descriptions
    sample: "10 random pages"
    expect:
      - "Description present"
      - "Under 160 characters"
      - "Compelling"
      - "Unique per page"
      
  - name: heading_structure
    sample: "10 random pages"
    expect:
      - "Single H1 per page"
      - "Logical hierarchy (H1→H2→H3)"
      - "Keywords in headings"
      
  - name: image_alt_text
    sample: "10 random pages"
    expect:
      - "All images have alt text"
      - "Alt text is descriptive"
```

### Technical SEO

```yaml
test: technical_seo
description: Technical SEO properly configured

checks:
  - name: sitemap
    url: "{{site_url}}/sitemap_index.xml"
    expect:
      - "Accessible"
      - "Valid XML"
      - "Contains all public content"
      
  - name: robots_txt
    url: "{{site_url}}/robots.txt"
    expect:
      - "Exists"
      - "Not blocking important content"
      - "Sitemap reference included"
      
  - name: canonical_tags
    sample: "10 random pages"
    expect:
      - "Canonical tag present"
      - "Self-referencing on most pages"
      
  - name: schema_markup
    sample: "Homepage + 3 posts"
    tool: "Google Rich Results Test"
    expect:
      - "Valid schema"
      - "No errors"
      - "Appropriate type for content"
```

### Internal Linking

```yaml
test: internal_linking
description: Internal link structure healthy

checks:
  - name: orphan_pages
    check: "Pages with no internal links pointing to them"
    expect: "Zero orphan pages"
    
  - name: broken_links
    tool: "Broken Link Checker or Screaming Frog"
    expect: "Zero broken internal links"
    
  - name: link_depth
    check: "Clicks from homepage to deepest content"
    expect: "<4 clicks to any page"
    
  - name: pillar_linking
    check: "Pillar pages have links from clusters"
    expect: "All clusters link to their pillar"
```

---

## 5. Security Validation

```yaml
test: security_validation
description: Security measures in place

checks:
  - name: wordfence_status
    check: "Wordfence firewall enabled"
    expect: "Active and optimized"
    
  - name: login_protection
    check: "Brute force protection"
    expect: "Limit Login Attempts or Wordfence protecting"
    
  - name: recent_scan
    check: "Last security scan"
    expect: "Within last 7 days"
    alert_if: "Issues found"
    
  - name: file_permissions
    check: "wp-config.php permissions"
    expect: "644 or more restrictive"
    
  - name: user_audit
    check: "Admin users"
    expect:
      - "No unknown users"
      - "Strong passwords"
      - "2FA if possible"
```

---

## Automated Validation Script

### Bash Script: validate-site.sh

```bash
#!/bin/bash
# Site Validation Script
# Usage: ./validate-site.sh <site-url> <dna-file>

SITE_URL=$1
DNA_FILE=$2
RESULTS_DIR="./validation-results/$(date +%Y%m%d)"

mkdir -p $RESULTS_DIR

echo "🔍 Validating: $SITE_URL"
echo "📄 DNA File: $DNA_FILE"
echo "=========================="

# 1. Basic connectivity
echo "Checking connectivity..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" $SITE_URL)
if [ "$HTTP_CODE" == "200" ]; then
    echo "✓ Site accessible (HTTP $HTTP_CODE)"
else
    echo "✗ Site issue (HTTP $HTTP_CODE)"
fi

# 2. SSL Check
echo "Checking SSL..."
SSL_EXPIRY=$(echo | openssl s_client -servername ${SITE_URL#https://} -connect ${SITE_URL#https://}:443 2>/dev/null | openssl x509 -noout -dates | grep notAfter)
echo "SSL Expiry: $SSL_EXPIRY"

# 3. PageSpeed (requires API key)
echo "Checking PageSpeed..."
# Add PageSpeed API call here

# 4. Check robots.txt
echo "Checking robots.txt..."
ROBOTS=$(curl -s "$SITE_URL/robots.txt")
if [[ $ROBOTS == *"Sitemap"* ]]; then
    echo "✓ robots.txt has sitemap"
else
    echo "⚠ robots.txt missing sitemap"
fi

# 5. Check sitemap
echo "Checking sitemap..."
SITEMAP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$SITE_URL/sitemap_index.xml")
if [ "$SITEMAP_CODE" == "200" ]; then
    echo "✓ Sitemap accessible"
else
    echo "✗ Sitemap issue (HTTP $SITEMAP_CODE)"
fi

# Generate report
echo ""
echo "Validation complete. Results saved to $RESULTS_DIR"
```

---

## Validation Report Template

```markdown
# Site Validation Report

**Site:** {{site_name}}
**URL:** {{site_url}}
**Date:** {{date}}
**DNA Version:** {{dna_version}}

## Summary

| Category | Status | Score |
|----------|--------|-------|
| DNA Compliance | ✓/⚠/✗ | X/10 |
| Technical Health | ✓/⚠/✗ | X/10 |
| Performance | ✓/⚠/✗ | X/10 |
| SEO | ✓/⚠/✗ | X/10 |
| Security | ✓/⚠/✗ | X/10 |

**Overall Score:** X/50

## Critical Issues (Fix Immediately)
1. ...
2. ...

## Warnings (Fix Soon)
1. ...
2. ...

## Recommendations (Improve)
1. ...
2. ...

## Passed Checks
- ✓ ...
- ✓ ...

## Detailed Results

### DNA Compliance
...

### Technical Health
...

### Performance
...

### SEO
...

### Security
...
```

---

## Scheduled Validation

```yaml
schedule:
  daily:
    - uptime_check
    - ssl_check
    - backup_verification
    
  weekly:
    - full_validation_suite
    - broken_link_check
    - performance_snapshot
    
  monthly:
    - comprehensive_audit
    - dna_compliance_review
    - security_deep_scan
    
  quarterly:
    - full_seo_audit
    - competitor_comparison
    - strategy_review
```

---

*Validation & QA Automation - Site Build Orchestrator v2.0*
