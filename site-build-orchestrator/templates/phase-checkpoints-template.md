# Phase Checkpoints: {{SITE_NAME}}

## Quality Assurance Verification Points

**Generated:** {{DATE}}  
**Site:** {{SITE_URL}}

---

## How to Use

After completing each phase in BUILD-GUIDE.md:
1. Run the checkpoint for that phase
2. Mark each item ✅ or ❌
3. If ANY item is ❌, fix before proceeding
4. Only move to next phase when all items are ✅

---

## Phase 1 Checkpoint: Foundation

### Theme Verification
| Check | Status | Notes |
|-------|--------|-------|
| Blocksy parent theme installed | ⬜ | |
| Child theme active | ⬜ | Name: {{SITE_SLUG}}-child |
| Parent styles loading | ⬜ | Check in browser |
| No PHP errors | ⬜ | Check debug.log |

### Plugin Verification
| Plugin | Installed | Activated | Notes |
|--------|-----------|-----------|-------|
| Wordfence Security | ⬜ | ⬜ | |
| Limit Login Attempts | ⬜ | ⬜ | |
| LiteSpeed Cache | ⬜ | ⬜ | |
| RankMath SEO | ⬜ | ⬜ | |
| WPCode | ⬜ | ⬜ | |
| Redirection | ⬜ | ⬜ | |
| UpdraftPlus | ⬜ | ⬜ | |
| Complianz | ⬜ | ⬜ | |
{{SITE_SPECIFIC_PLUGINS_CHECK}}

### Clean State
| Check | Status |
|-------|--------|
| No default posts | ⬜ |
| No default pages | ⬜ |
| No default comments | ⬜ |
| No placeholder content | ⬜ |

**Phase 1 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 2 Checkpoint: Design System

### CSS Tokens
| Token Category | Implemented | Correct Values | Notes |
|----------------|-------------|----------------|-------|
| Colors - Primary | ⬜ | {{COLOR_PRIMARY}} | |
| Colors - Secondary | ⬜ | {{COLOR_SECONDARY}} | |
| Colors - Background | ⬜ | {{COLOR_BG_PRIMARY}} | |
| Colors - Text | ⬜ | {{COLOR_TEXT_PRIMARY}} | |
| Typography - Heading | ⬜ | {{FONT_HEADING}} | |
| Typography - Body | ⬜ | {{FONT_BODY}} | |
| Spacing Scale | ⬜ | 8px base | |
| Border Radius | ⬜ | {{RADIUS_MD}} | |
| Shadows | ⬜ | Match DNA | |
| Transitions | ⬜ | {{TRANSITION_NORMAL}} | |

### Visual Verification
| Check | Status | Notes |
|-------|--------|-------|
| Fonts loading (check Network tab) | ⬜ | |
| Colors match DNA exactly | ⬜ | |
| Background correct | ⬜ | |
| Links styled properly | ⬜ | |
| Buttons match specification | ⬜ | |
| Form elements styled | ⬜ | |

### Browser Check
| Browser | Renders Correctly |
|---------|-------------------|
| Chrome | ⬜ |
| Firefox | ⬜ |
| Safari | ⬜ |
| Edge | ⬜ |

**Phase 2 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 3 Checkpoint: Global Elements

### Header
| Check | Status | Notes |
|-------|--------|-------|
| Logo displays | ⬜ | |
| Logo links to home | ⬜ | |
| Navigation visible | ⬜ | |
| All nav items work | ⬜ | |
| Dropdowns function | ⬜ | |
| Search accessible | ⬜ | |
| Mobile menu works | ⬜ | |
| Sticky header (if enabled) | ⬜ | |

### Footer
| Check | Status | Notes |
|-------|--------|-------|
| Footer displays | ⬜ | |
| All footer links work | ⬜ | |
| Copyright text correct | ⬜ | |
| Social links work | ⬜ | |
| Widget areas populated | ⬜ | |

### Navigation Test
| Item | Desktop | Mobile |
|------|---------|--------|
| Primary Nav | ⬜ | ⬜ |
| Dropdown Menus | ⬜ | ⬜ |
| Footer Nav | ⬜ | ⬜ |
| Breadcrumbs | ⬜ | ⬜ |

**Phase 3 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 4 Checkpoint: Homepage

### Hero Section
| Check | Status | Notes |
|-------|--------|-------|
| Hero displays correctly | ⬜ | |
| Hero matches DNA specification | ⬜ | |
| CTA button styled correctly | ⬜ | |
| CTA text is invitation (not command) | ⬜ | |
| Animation works (if applicable) | ⬜ | |
| Mobile hero works | ⬜ | |

### Content Sections
| Section | Present | Styled | Functional |
|---------|---------|--------|------------|
| Section 1 | ⬜ | ⬜ | ⬜ |
| Section 2 | ⬜ | ⬜ | ⬜ |
| Section 3 | ⬜ | ⬜ | ⬜ |
| Newsletter/CTA | ⬜ | ⬜ | ⬜ |

### Signature Elements
| Element | Implemented | Correct Placement |
|---------|-------------|-------------------|
{{SIGNATURE_ELEMENTS_CHECK}}

### Design Quality Tests
| Test | Result |
|------|--------|
| **Screenshot Test:** Would a designer save this for inspiration? | ⬜ Yes / ⬜ No |
| **Swap Test:** Could this homepage work on a generic site? | ⬜ Yes (FAIL) / ⬜ No (PASS) |
| **Memory Test:** What will visitors remember in a week? | Answer: ____________ |
| **Atmosphere Test:** Can you feel the {{EMOTIONAL_PRIMARY}}? | ⬜ Yes / ⬜ No |

### Mobile Homepage
| Check | Status |
|-------|--------|
| Loads correctly | ⬜ |
| Readable without zoom | ⬜ |
| Touch targets adequate (44px) | ⬜ |
| No horizontal scroll | ⬜ |

**Phase 4 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 5 Checkpoint: Templates

### Category Template
| Check | Status | Notes |
|-------|--------|-------|
| Category archive loads | ⬜ | |
| Posts display correctly | ⬜ | |
| Featured treatment works | ⬜ | |
| Pagination functions | ⬜ | |
| Category description shows | ⬜ | |

### Single Post Template
| Check | Status | Notes |
|-------|--------|-------|
| Post loads correctly | ⬜ | |
| Featured image displays | ⬜ | |
| Typography readable | ⬜ | |
| Related posts show | ⬜ | |
| Social sharing works | ⬜ | |
| Author box shows | ⬜ | |
| Comments functional | ⬜ | |

### Other Templates
| Template | Displays | Styled |
|----------|----------|--------|
| Standard Page | ⬜ | ⬜ |
| Search Results | ⬜ | ⬜ |
| 404 Page | ⬜ | ⬜ |
| Author Archive | ⬜ | ⬜ |

**Phase 5 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 6 Checkpoint: Core Pages

### Essential Pages
| Page | Created | URL Correct | Content Complete |
|------|---------|-------------|------------------|
| About | ⬜ | /about/ | ⬜ |
| Contact | ⬜ | /contact/ | ⬜ |
| Privacy Policy | ⬜ | /privacy-policy/ | ⬜ |
| Terms | ⬜ | /terms/ | ⬜ |
| Affiliate Disclosure | ⬜ | {{DISCLOSURE_URL}} | ⬜ |
| Start Here | ⬜ | {{START_HERE_URL}} | ⬜ |

### Functionality
| Check | Status |
|-------|--------|
| Contact form submits | ⬜ |
| Form sends notification | ⬜ |
| All page links work | ⬜ |
| Pages match design | ⬜ |

**Phase 6 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 7 Checkpoint: SEO

### RankMath Configuration
| Setting | Configured |
|---------|------------|
| Wizard completed | ⬜ |
| Titles & meta templates | ⬜ |
| Schema enabled | ⬜ |
| Sitemap enabled | ⬜ |
| OpenGraph enabled | ⬜ |

### Schema Validation
| Test | Result |
|------|--------|
| Homepage schema valid | ⬜ |
| Post schema valid | ⬜ |
| Page schema valid | ⬜ |

Test URL: https://search.google.com/test/rich-results

### Technical SEO
| Check | Status |
|-------|--------|
| Sitemap accessible | ⬜ |
| Sitemap submitted to GSC | ⬜ |
| robots.txt correct | ⬜ |
| Canonical tags present | ⬜ |
| No noindex errors | ⬜ |

**Phase 7 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 8 Checkpoint: Performance

### Core Web Vitals
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| LCP | <{{PERF_LCP}} | _____ | ⬜ |
| FID/INP | <{{PERF_FID}} | _____ | ⬜ |
| CLS | <{{PERF_CLS}} | _____ | ⬜ |

### PageSpeed Scores
| Page | Mobile Target | Mobile Actual | Desktop Target | Desktop Actual |
|------|---------------|---------------|----------------|----------------|
| Homepage | >{{PERF_MOBILE}} | _____ | >{{PERF_DESKTOP}} | _____ |
| Post | >{{PERF_MOBILE}} | _____ | >{{PERF_DESKTOP}} | _____ |
| Category | >{{PERF_MOBILE}} | _____ | >{{PERF_DESKTOP}} | _____ |

### Optimization Features
| Feature | Enabled | Working |
|---------|---------|---------|
| Caching | ⬜ | ⬜ |
| CSS minification | ⬜ | ⬜ |
| JS minification | ⬜ | ⬜ |
| Image optimization | ⬜ | ⬜ |
| WebP serving | ⬜ | ⬜ |
| Lazy loading | ⬜ | ⬜ |

**Phase 8 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 9 Checkpoint: Content

### Content Structure
| Category | Created | Has Content |
|----------|---------|-------------|
{{CONTENT_CATEGORIES_CHECK}}

### Pillar Content
| Pillar | Published | Word Count | Internal Links |
|--------|-----------|------------|----------------|
{{PILLAR_CONTENT_CHECK}}

### Internal Linking
| Check | Status |
|-------|--------|
| Pillars link to clusters | ⬜ |
| Clusters link to pillars | ⬜ |
| No orphan pages | ⬜ |
| No broken links | ⬜ |

**Phase 9 Result:** ⬜ PASS / ⬜ FAIL

---

## Phase 10 Checkpoint: Launch

### Browser Compatibility
| Browser | Desktop | Mobile |
|---------|---------|--------|
| Chrome | ⬜ | ⬜ |
| Firefox | ⬜ | ⬜ |
| Safari | ⬜ | ⬜ |
| Edge | ⬜ | ⬜ |

### Final Checks
| Item | Status |
|------|--------|
| All content proofread | ⬜ |
| No test content visible | ⬜ |
| Contact form works | ⬜ |
| Analytics tracking | ⬜ |
| SSL working | ⬜ |
| No console errors | ⬜ |
| Backup taken | ⬜ |
| Documentation complete | ⬜ |

### Launch Verification
| Check | Status |
|-------|--------|
| Site accessible | ⬜ |
| All pages load | ⬜ |
| Forms work | ⬜ |
| No errors in logs | ⬜ |

**Phase 10 Result:** ⬜ PASS / ⬜ FAIL

---

## Overall Build Status

| Phase | Status |
|-------|--------|
| 1. Foundation | ⬜ |
| 2. Design System | ⬜ |
| 3. Global Elements | ⬜ |
| 4. Homepage | ⬜ |
| 5. Templates | ⬜ |
| 6. Core Pages | ⬜ |
| 7. SEO | ⬜ |
| 8. Performance | ⬜ |
| 9. Content | ⬜ |
| 10. Launch | ⬜ |

**BUILD COMPLETE:** ⬜ YES / ⬜ NO

---

*Generated by Site Build Orchestrator*
