# Batch Build Package Generator

## Generate All 16 Sites at Once

This generator creates complete build packages for every site in the empire in a single operation.

---

## Sites Inventory

| # | Site ID | Status | Site Type |
|---|---------|--------|-----------|
| 1 | witchcraft-for-beginners | FLAGSHIP | Authority |
| 2 | smart-home-wizards | Priority | Affiliate |
| 3 | mythical-archives | Active | Authority |
| 4 | ai-in-action-hub | Active | Authority |
| 5 | family-flourish | Active | Lifestyle |
| 6 | bullet-journals | Active | Lifestyle |
| 7 | kitchen-tech-insider | Active | Affiliate |
| 8 | pulse-gear-reviews | Active | Affiliate |
| 9 | clear-ai-news | Active | News |
| 10 | wealth-from-ai | Active | News |
| 11 | ai-discovery | Active | News |
| 12 | wearable-gear-hub | Active | Affiliate |
| 13 | the-connected-haven | Active | Lifestyle |
| 14 | celebration-season | Planned | Lifestyle |
| 15 | sprout-and-spruce | Planned | Lifestyle |
| 16 | manifest-and-align | Planned | Authority |

---

## Batch Generation Command

```
Generate complete build packages for all 16 sites in the empire.

For each site:
1. Read DNA from /creative-command-center/brains/[slug].json
2. Determine site type (affiliate/authority/lifestyle/news)
3. Generate CLAUDE.md using claudemd-generator
4. Generate BUILD-GUIDE.md using site-type specific template
5. Generate PREFLIGHT-CHECKLIST.md
6. Generate PHASE-CHECKPOINTS.md
7. Generate PLUGIN-MANIFEST.md (site-type specific)
8. Save all files to /mnt/user-data/outputs/[slug]/

Output:
- 16 folders, each containing complete build package
- Summary report of what was generated
- Any errors or missing DNA files noted
```

---

## Site Type Mapping

```yaml
site_type_assignments:
  
  affiliate:
    sites:
      - smart-home-wizards
      - kitchen-tech-insider
      - pulse-gear-reviews
      - wearable-gear-hub
    template: affiliate-site.md
    plugins:
      - thirstyaffiliates
      - flavor-comparison-tables
      - product-schema
    
  authority:
    sites:
      - witchcraft-for-beginners
      - mythical-archives
      - ai-in-action-hub
      - bullet-journals
      - manifest-and-align
    template: content-authority.md
    plugins:
      - wp-recipe-maker (if applicable)
      - advanced-schema
    
  lifestyle:
    sites:
      - family-flourish
      - the-connected-haven
      - celebration-season
      - sprout-and-spruce
    template: lifestyle-site.md (to be created)
    plugins:
      - pinterest-optimization
      - printables-delivery
    
  news:
    sites:
      - clear-ai-news
      - wealth-from-ai
      - ai-discovery
    template: news-site.md (to be created)
    plugins:
      - news-schema
      - rapid-publishing
```

---

## Generated Package Contents

Each generated folder contains:

```
/[site-slug]/
├── CLAUDE.md                    (15-25 KB)
│   ├── Identity & Voice
│   ├── Design Tokens (CSS + Tailwind)
│   ├── Typography System
│   ├── Spacing & Effects
│   ├── Content Rules
│   ├── Anti-Patterns
│   ├── Technical Stack
│   ├── SEO Configuration
│   ├── Signature Elements
│   └── Quick Reference
│
├── BUILD-GUIDE.md               (20-35 KB)
│   ├── Phase 0-12 Prompts
│   ├── Site-Specific Customizations
│   ├── Site-Type Additions
│   └── Critical Reminders
│
├── PREFLIGHT-CHECKLIST.md       (5-8 KB)
│   ├── Infrastructure Checks
│   ├── Account Verification
│   ├── Asset Preparation
│   └── Go/No-Go Criteria
│
├── PHASE-CHECKPOINTS.md         (10-15 KB)
│   ├── Phase 1-12 Checkpoints
│   ├── Quality Gates
│   └── Design Tests
│
├── PLUGIN-MANIFEST.md           (8-12 KB)
│   ├── Core Plugins (universal)
│   ├── Site-Type Plugins
│   ├── Site-Specific Plugins
│   └── Configuration Details
│
└── .mcp/
    └── config-template.json     (MCP configuration template)
```

---

## Batch Progress Tracking

### Generation Log Template

```markdown
# Batch Generation Log
**Started:** {{timestamp}}
**Generator Version:** 2.0

## Progress

| Site | DNA | CLAUDE.md | BUILD-GUIDE | Checklists | Status |
|------|-----|-----------|-------------|------------|--------|
| witchcraft-for-beginners | ✓ | ✓ | ✓ | ✓ | ✅ Complete |
| smart-home-wizards | ✓ | ✓ | ... | ... | 🔄 In Progress |
| ... | | | | | |

## Errors
- Site X: Missing DNA file
- Site Y: Template variable not found

## Summary
- Sites processed: X/16
- Successful: X
- Errors: X
- Time elapsed: XX minutes

**Completed:** {{timestamp}}
```

---

## Post-Generation Steps

After batch generation completes:

### 1. Verify All Packages
```
For each generated package:
□ Open CLAUDE.md - check for {{VARIABLES}} remaining
□ Open BUILD-GUIDE.md - check site-specific content
□ Verify no placeholder text
□ Confirm site type additions present
```

### 2. Create Claude Code Projects
```
For each site:
□ Create folder: C:\Claude Code Projects\[site-slug]\
□ Copy all generated files
□ Add MCP configuration (site-specific)
□ Test Claude Code connection
```

### 3. Priority Queue
```
Build order recommendation:
1. witchcraft-for-beginners (FLAGSHIP - template/example)
2. smart-home-wizards (Priority affiliate)
3. [remaining based on revenue potential]
```

---

## Incremental Generation

If you need to regenerate specific sites:

```
Regenerate build packages for:
- smart-home-wizards (updated DNA)
- family-flourish (new site type assignment)

Keep existing packages for other sites.
Save to /mnt/user-data/outputs/incremental-[date]/
```

---

## Quality Validation Post-Generation

Run these checks after batch generation:

```yaml
validation_checks:
  
  completeness:
    - all_16_folders_exist
    - each_folder_has_5_required_files
    - no_empty_files
    
  variable_substitution:
    - no_double_brace_patterns: "{{.*}}"
    - no_placeholder_text: "[TO BE FILLED]"
    - site_names_correct
    
  site_specificity:
    - colors_match_dna
    - voice_section_unique
    - plugins_match_site_type
    
  cross_site_consistency:
    - core_plugins_same_across_all
    - phase_structure_consistent
    - checklist_format_consistent
```

---

## Command Quick Reference

### Generate All
```
Generate complete build packages for all 16 sites.
```

### Generate Specific Sites
```
Generate build packages for: witchcraft-for-beginners, smart-home-wizards
```

### Regenerate with Updates
```
Regenerate BUILD-GUIDE.md for all affiliate sites with updated comparison table section.
```

### Generate New Site
```
Generate build package for new site [site-name] using DNA file [path].
```

---

*Batch Build Package Generator - Site Build Orchestrator v2.0*
