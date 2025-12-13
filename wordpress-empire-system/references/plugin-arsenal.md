# Plugin Arsenal Reference

Complete plugin guide for Nick's WordPress Empire - default stack plus WorldPressIt's 8,000+ premium plugins.

## Default Stack (Every Site)

These plugins are installed on ALL 17 sites:

### Core Essential Plugins
| Plugin | Purpose | Config Reference |
|--------|---------|------------------|
| **Blocksy Companion Pro** | Theme extensions | `theme-systems.md` |
| **RankMath SEO Pro** | SEO management | `seo-structure.md` |
| **LiteSpeed Cache** | Performance | `performance-patterns.md` |
| **AI Engine** | WordPress MCP | `claude-code-workflows.md` |
| **WPCode** | Code snippets | SKILL.md |
| **Complianz** | GDPR/Privacy | Below |
| **Content Egg** | Affiliate/comparison | Below |
| **Easy Table of Contents** | Post navigation | Below |
| **Wordfence** | Security | Below |
| **UpdraftPlus** | Backups | Below |

### Default Stack Configuration

#### Complianz (Privacy/GDPR)
```
Complianz → Wizard
├── Region: Select applicable (US/EU/UK)
├── Website Statistics: Google Analytics
├── Marketing: Configure third-party
├── Cookie Policy: Generate
├── Privacy Policy: Generate or link
└── Cookie Banner: Configure style

Cookie Banner Settings:
├── Position: Bottom
├── Style: Match brand colors
├── Accept/Decline: Both buttons
└── Consent: Category-based
```

#### Content Egg
```
Content Egg → Settings
├── Amazon
│   ├── Access Key: [From memory]
│   ├── Secret Key: [From memory]
│   ├── Associate Tag: [Per site]
│   └── Locale: US
├── Auto-Update: ON
├── Price Update: Every 12 hours
└── Templates: Comparison, Grid, List
```

#### Easy Table of Contents
```
Easy Table of Contents → Settings
├── General
│   ├── Enable Support: Posts
│   ├── Auto Insert: Posts
│   └── Position: Before first heading
├── Appearance
│   ├── Width: 100%
│   ├── Title: In This Article
│   ├── Show Title: ON
│   └── Style: Match theme
├── Advanced
│   ├── Headings: H2, H3
│   ├── Smooth Scroll: ON
│   └── Smooth Scroll Offset: 50px
└── Per-Post Override: Available in editor
```

#### Wordfence
```
Wordfence → All Options
├── Firewall
│   ├── Web Application Firewall: Enabled
│   ├── Brute Force Protection: ON
│   ├── Rate Limiting: Enabled
│   └── Blocking: Country blocking (if needed)
├── Scan
│   ├── Schedule: Daily
│   ├── Low Resource Mode: OFF
│   └── Email Alerts: ON
├── Login Security
│   ├── 2FA: Enable for admins
│   ├── reCAPTCHA: Optional
│   └── Login Attempts: 5
└── Tools
    └── Live Traffic: Monitor
```

#### UpdraftPlus
```
UpdraftPlus → Settings
├── Files Backup Schedule: Weekly
├── Database Backup Schedule: Daily
├── Remote Storage: Choose (Google Drive, Dropbox, etc.)
├── Include Files
│   ├── Plugins: ON
│   ├── Themes: ON
│   ├── Uploads: ON
│   └── Others: ON
├── Email: Receive backup reports
└── Retention: Keep 4 backups
```

## Theme & Page Builder Plugins

### Blocksy Ecosystem (PRIMARY)
| Plugin | Purpose |
|--------|---------|
| **Blocksy Companion Pro** | Header/footer builder, hooks, content blocks |
| **Stackable** | Additional blocks |
| **GenerateBlocks** | Lightweight blocks |

### Astra Ecosystem (SECONDARY)
| Plugin | Purpose |
|--------|---------|
| **Astra Pro** | Theme extensions |
| **Starter Templates Pro** | Import designs |
| **Spectra** | Gutenberg blocks |

### Elementor Ecosystem
| Plugin | Purpose |
|--------|---------|
| **Elementor Pro** | Page builder |
| **Premium Addons Pro** | 90+ widgets |
| **Essential Addons** | 100+ widgets |
| **Ultimate Addons** | Advanced widgets |
| **PowerPack** | Extended elements |
| **JetElements** | Dynamic content |

## SEO & Content Plugins

### SEO Stack
| Plugin | Purpose | Notes |
|--------|---------|-------|
| **RankMath SEO Pro** | Primary SEO | DEFAULT |
| **RankMath Schema Markup** | Rich results | Built into Pro |
| **WP Search Console** | Alternative analytics | If needed |
| **Schema Pro** | Additional schema | If RankMath insufficient |

### Content Enhancement
| Plugin | Purpose |
|--------|---------|
| **Easy Table of Contents** | Post navigation |
| **TablePress Pro** | Data tables |
| **Content Egg** | Affiliate/comparison |
| **Ultimate FAQ** | FAQ sections |
| **Jenga Accordion** | Collapsible content |

### Related Posts
| Plugin | Purpose |
|--------|---------|
| **Jetwoo Related** | Related products |
| **Contextual Related Posts** | Smart recommendations |
| **JETRP** | Related posts grid |

## Performance Plugins

### Caching (LiteSpeed Primary)
| Plugin | Purpose | Notes |
|--------|---------|-------|
| **LiteSpeed Cache** | Full optimization | DEFAULT |
| **Redis Object Cache** | Object caching | If server supports |
| **Perfmatters** | Additional optimization | Optional complement |
| **Asset CleanUp Pro** | Script management | Optional |

### Image Optimization
| Plugin | Purpose |
|--------|---------|
| **LiteSpeed (built-in)** | WebP, optimization |
| **Smush Pro** | Backup optimizer |
| **ShortPixel** | Alternative |
| **Imagify** | Alternative |

## Forms & Lead Capture

### Form Builders
| Plugin | Purpose |
|--------|---------|
| **WPForms Pro** | User-friendly forms |
| **Gravity Forms** | Advanced forms |
| **Fluent Forms Pro** | Modern, fast |
| **Ninja Forms Pro** | Flexible |

### Lead Capture
| Plugin | Purpose |
|--------|---------|
| **OptinMonster** | Popups, slide-ins |
| **Convert Pro** | Advanced opt-ins |
| **Thrive Leads** | List building |
| **Jetwoo Popup** | Elementor popups |

## E-commerce (WooCommerce Sites)

### Core WooCommerce
| Plugin | Purpose |
|--------|---------|
| **WooCommerce** | Core commerce |
| **WooCommerce Subscriptions** | Recurring |
| **WooCommerce Memberships** | Member areas |
| **WooCommerce Bookings** | Appointments |

### WooCommerce Enhancement
| Plugin | Purpose |
|--------|---------|
| **YITH Plugins** | Various extensions |
| **CartFlows Pro** | Sales funnels |
| **Jetwoo Builder** | Product templates |
| **ShopEngine Pro** | Elementor WooCommerce |

## Security & Backup

### Security
| Plugin | Purpose | Notes |
|--------|---------|-------|
| **Wordfence** | Firewall, scanning | DEFAULT |
| **iThemes Security Pro** | Hardening | Alternative |
| **Sucuri Security** | Cloud firewall | Enterprise |
| **MalCare** | Malware removal | If infected |

### Backup
| Plugin | Purpose | Notes |
|--------|---------|-------|
| **UpdraftPlus Premium** | Backup & restore | DEFAULT |
| **BackupBuddy** | Complete backup | Alternative |
| **WP Migrate DB Pro** | Database migration | For moves |

## Analytics & Tracking

| Plugin | Purpose |
|--------|---------|
| **MonsterInsights Pro** | Google Analytics |
| **ExactMetrics Pro** | Analytics dashboard |
| **RankMath Analytics** | Built into RankMath |
| **WP Statistics** | Privacy-focused |

## Social & Engagement

### Social Proof
| Plugin | Purpose |
|--------|---------|
| **TrustPulse** | FOMO notifications |
| **NotificationX Pro** | Social proof |
| **ProveSource** | Conversion proof |

### Social Integration
| Plugin | Purpose |
|--------|---------|
| **Social Warfare Pro** | Share buttons |
| **Jenga Social** | Social feeds |
| **Custom Facebook Feed Pro** | FB integration |
| **Instagram Feed Pro** | IG integration |

## Advanced Functionality

### Custom Fields & Content
| Plugin | Purpose |
|--------|---------|
| **ACF Pro** | Custom fields |
| **JetEngine** | Dynamic content |
| **Toolset Types** | Custom content |
| **Meta Box Pro** | Custom meta |

### Search & Filtering
| Plugin | Purpose |
|--------|---------|
| **SearchWP** | Enhanced search |
| **FacetWP** | Advanced filtering |
| **JetSmartFilters** | Dynamic filters |

### Navigation
| Plugin | Purpose |
|--------|---------|
| **Max Mega Menu Pro** | Mega menus |
| **Jetwoo Menu** | Elementor menus |
| **UberMenu** | Advanced menus |

## MCP & Automation

### AI Engine (WordPress MCP)
```
AI Engine → Settings
├── REST API
│   ├── Enable: ON
│   ├── Authentication: Bearer Token
│   └── Token: [Generate secure]
├── ChatGPT
│   ├── API Key: [Your key]
│   └── Model: gpt-4 or gpt-3.5-turbo
├── Features
│   ├── AI Forms: ON
│   ├── Content Generation: ON
│   └── Embeddings: ON
└── Statistics: ON
```

### WPCode Pro (Code Snippets)
```
WPCode → Settings
├── Header & Footer: Global scripts
├── Code Snippets: PHP, JS, CSS
├── Conditional Logic: Where to run
├── Auto Insert: Locations
├── Library: Save and reuse
└── Safe Mode: Recovery option
```

## Plugin Selection Guide

### "I need to..."

| Task | Plugin |
|------|--------|
| Build a page | Gutenberg blocks + Blocksy |
| Build complex page | Elementor Pro |
| Create a popup | OptinMonster or Blocksy hooks |
| Add a slider | Slider Revolution |
| Make tables | TablePress Pro |
| Optimize speed | LiteSpeed Cache |
| Capture leads | WPForms Pro + OptinMonster |
| Improve SEO | RankMath Pro |
| Add custom fields | ACF Pro |
| Build mega menu | Max Mega Menu or Blocksy Pro |
| Create membership | MemberPress |
| Make courses | LearnDash |
| Add social proof | TrustPulse |
| Send newsletters | MailPoet Premium |
| Build sales funnel | CartFlows Pro |
| Filter content | FacetWP or JetSmartFilters |
| Connect to Claude | AI Engine |
| Add code snippets | WPCode |

## Plugin Conflict Prevention

### Common Conflicts & Solutions

**Multiple caching plugins:**
→ Use only LiteSpeed Cache

**Multiple SEO plugins:**
→ Use only RankMath Pro

**Lazy loading conflicts:**
→ Disable in all except LiteSpeed

**Elementor vs Blocks:**
→ Choose per page, don't mix on same page

**jQuery conflicts:**
→ LiteSpeed: Don't exclude jQuery

### Performance Considerations

**Keep active plugins minimal:**
- Audit quarterly
- Remove unused plugins (delete, don't deactivate)
- Prefer plugins that do multiple things

**Heavy plugins to monitor:**
- Visual page builders (use sparingly)
- Social sharing plugins
- Analytics plugins
- Backup plugins (schedule off-peak)

## WorldPressIt Quick Access

Nick has UNLIMITED access to 8,000+ premium plugins via WorldPressIt membership.

**How to find plugins:**
1. Go to worldpressit.com
2. Search plugin name
3. Download latest version
4. Install via WordPress admin

**Most-used from WorldPressIt:**
- Elementor Pro
- ACF Pro
- WPForms Pro
- OptinMonster
- TablePress Pro
- Slider Revolution
- SearchWP
- CartFlows Pro
- All JetPlugins
- All YITH plugins

**Remember:** Always check WorldPressIt first before buying directly!
