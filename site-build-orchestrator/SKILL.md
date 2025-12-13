# Site Build Orchestrator v2.0

## The Complete Empire Building System

**Purpose:** Build, launch, maintain, and scale any site in Nick's publishing empire with zero guesswork, zero missed steps, and maximum efficiency.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         EMPIRE COMMAND CENTER                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌────────────────────┐    ┌────────────────────┐    ┌────────────────────┐    │
│  │   DNA LAYER        │    │   GENERATION LAYER │    │   EXECUTION LAYER  │    │
│  │                    │    │                    │    │                    │    │
│  │ creative-command-  │───▶│ claudemd-generator │───▶│ Claude Code        │    │
│  │ center             │    │ site-build-        │    │ Projects           │    │
│  │                    │    │ orchestrator       │    │                    │    │
│  │ • 16+ DNA files    │    │ • CLAUDE.md        │    │ • Phase execution  │    │
│  │ • Design specs     │    │ • BUILD-GUIDE.md   │    │ • MCP connection   │    │
│  │ • Voice rules      │    │ • All checklists   │    │ • Live deployment  │    │
│  └────────────────────┘    └────────────────────┘    └────────────────────┘    │
│           │                         │                         │                 │
│           ▼                         ▼                         ▼                 │
│  ┌────────────────────────────────────────────────────────────────────────┐    │
│  │                        AUTOMATION LAYER                                 │    │
│  │  n8n • ZimmWriter • GitHub Actions • Scheduled Tasks                    │    │
│  └────────────────────────────────────────────────────────────────────────┘    │
│           │                         │                         │                 │
│           ▼                         ▼                         ▼                 │
│  ┌────────────────────────────────────────────────────────────────────────┐    │
│  │                        MONITORING LAYER                                 │    │
│  │  Analytics • Performance • Health Checks • Revenue Tracking             │    │
│  └────────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## The 12-Phase Build Process

| Phase | Name | Duration | Key Deliverables |
|-------|------|----------|------------------|
| **0** | Preflight | 30 min | All systems verified, files ready |
| **1** | Foundation | 1 hour | Theme, child theme, core plugins |
| **2** | Design System | 2 hours | Tokens, colors, typography |
| **3** | Global Elements | 2 hours | Header, nav, footer |
| **4** | Homepage | 3-4 hours | Hero, sections, atmosphere |
| **5** | Templates | 2-3 hours | Category, post, page |
| **6** | Core Pages | 2 hours | About, contact, legal |
| **7** | SEO Setup | 1-2 hours | RankMath, schema, sitemaps |
| **8** | Performance | 1-2 hours | Caching, Core Web Vitals |
| **9** | Content Foundation | 2-4 hours | Pillar content, linking |
| **10** | Integration Setup | 1-2 hours | Analytics, email, automation |
| **11** | QA & Testing | 2-3 hours | Full testing suite |
| **12** | Launch & Monitor | 1 hour | Go live, monitoring |

**Total: ~20-25 hours per site**

---

## Site Type Profiles

### Affiliate/Review Sites
**Sites:** SmartHomeWizards, PulseGearReviews, KitchenTechInsider, WearableGearHub
- Revenue: Affiliate commissions (Amazon, direct)
- Content: Product reviews, comparisons, buying guides
- Special: Product schema, comparison tables, affiliate disclaimers
- See: `/site-types/affiliate-site.md`

### Authority/Educational Sites
**Sites:** WitchcraftForBeginners, MythicalArchives, AIinActionHub, BulletJournals
- Revenue: Ads + products + courses
- Content: In-depth guides, tutorials, reference
- Special: E-E-A-T signals, pillar content
- See: `/site-types/content-authority.md`

### Lifestyle/Niche Sites
**Sites:** FamilyFlourish, SproutAndSpruce, CelebrationSeason, ManifestAndAlign
- Revenue: Ads + printables + affiliate
- Content: Inspiration, how-tos, community
- Special: Pinterest SEO, visual content
- See: `/site-types/lifestyle-site.md`

### News/Updates Sites
**Sites:** ClearAINews, WealthFromAI, AIDiscovery
- Revenue: Ads + newsletter
- Content: Breaking news, analysis
- Special: Speed, freshness signals
- See: `/site-types/news-site.md`

---

## Directory Structure

```
site-build-orchestrator/
├── SKILL.md                      # Master orchestrator (this file)
├── generators/                   # Build package generators
├── templates/                    # Base templates for all files
├── site-types/                   # Site-type specific guides
├── content-strategy/             # Content planning system
├── automation/                   # n8n and workflow configs
├── integrations/                 # MCP, GitHub, tool setups
├── validation/                   # QA and testing procedures
├── troubleshooting/              # Problem resolution guides
├── post-launch/                  # Maintenance and growth
├── references/                   # Plugin and hosting docs
├── checklists/                   # Printable checklists
├── examples/                     # Complete working examples
└── scripts/                      # Automation scripts
```

---

## Quality Gates

Each phase has a quality gate that MUST pass before proceeding:

### Design Quality Gate (Phase 4)
```
□ Screenshot Test: Designer would save for inspiration
□ Swap Test: Could NOT work on generic site
□ Memory Test: Can name memorable element
□ Atmosphere Test: Matches DNA emotional targets
```

### Performance Quality Gate (Phase 8)
```
□ PageSpeed Mobile ≥ DNA target
□ PageSpeed Desktop ≥ DNA target
□ All Core Web Vitals green
□ Cache headers correct
```

### Launch Quality Gate (Phase 12)
```
□ All previous gates passed
□ Zero broken links
□ Forms functional
□ Analytics confirmed
□ Schema validates
□ Security scan clean
```

---

## Command Reference

### Generate Build Package
```
Generate complete build package for [SiteName]:
1. Read DNA from creative-command-center
2. Generate CLAUDE.md
3. Generate BUILD-GUIDE.md (site-type specific)
4. Generate all checklists
5. Save to outputs folder
```

### Batch Generate All Sites
```
Generate build packages for all 16 sites in batch.
```

### Validate Existing Site
```
Run full validation audit for [SiteName] against DNA.
```

### Generate Content Strategy
```
Create 90-day content strategy for [SiteName].
```

---

## Integration Points

| Tool | Purpose | Config Location |
|------|---------|-----------------|
| WordPress MCP | Site execution | `/integrations/mcp-wordpress-setup.md` |
| Figma MCP | Design reference | `/integrations/mcp-figma-setup.md` |
| n8n | Automation | `/automation/n8n-content-pipeline.md` |
| ZimmWriter | Content | `/automation/zimmwriter-integration.md` |
| GitHub | Version control | `/integrations/github-workflow.md` |

---

## Emergency Procedures

**Site Down:** Check hosting → Clear cache → Disable plugins → Restore backup
**Hacked:** Maintenance mode → Change passwords → Scan → Restore → Harden
**Data Loss:** Stop → Check backups → Restore → Verify

See: `/troubleshooting/` for detailed procedures.

---

## Post-Launch System

After launch, each site enters the maintenance cycle:

**Daily:** Health checks, backup verification
**Weekly:** Content review, performance check, security scan
**Monthly:** Full audit, analytics review, strategy adjustment
**Quarterly:** Competitor analysis, major updates

See: `/post-launch/` for complete system.

---

*Site Build Orchestrator v2.0*
*The Complete Empire Building System*
