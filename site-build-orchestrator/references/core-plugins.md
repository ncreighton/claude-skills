# Core Plugins Reference

## Universal Plugins (ALL Sites)

These plugins are required on EVERY site in the empire. No exceptions.

### 1. Theme & Page Building

| Plugin | Purpose | Configuration Notes |
|--------|---------|---------------------|
| **Blocksy** | Theme framework | Install from theme repo, activate child theme |
| **Blocksy Companion** | Theme extensions | Enable: Header Builder, Footer Builder, Custom Fonts |

### 2. SEO & Structured Data

| Plugin | Purpose | Configuration Notes |
|--------|---------|---------------------|
| **RankMath SEO Pro** | Primary SEO | Setup wizard → Advanced mode → Enable all modules |
| **RankMath Schema Pro** | Advanced schema | Enable custom schema templates |

**RankMath Configuration:**
```
General Settings:
- Separator: – (en dash)
- OpenGraph enabled
- Twitter Cards enabled
- Local SEO (for applicable sites)

Titles & Meta:
- Homepage: Custom (site-specific from DNA)
- Posts: %title% %sep% %sitename%
- Categories: %term% %sep% %sitename%

Sitemap:
- Enable XML Sitemap
- Include posts, pages, categories
- Exclude tags (unless site uses them)
- Ping search engines: Yes

Schema:
- Default: Article
- Enable FAQ schema
- Enable HowTo schema
```

### 3. Performance & Caching

| Plugin | Purpose | Configuration Notes |
|--------|---------|---------------------|
| **LiteSpeed Cache** | Caching + optimization | For Hostinger (uses LSCWP) |
| **ShortPixel** | Image optimization | API key required, lossy compression |

**LiteSpeed Configuration:**
```
Cache:
- Enable Cache: Yes
- Cache Logged-in Users: No
- Cache Mobile: Yes (separate cache)
- TTL: 604800 (7 days)

Image Optimization:
- Auto Request Cron: Yes
- Optimization Level: Lossy
- Preserve EXIF: No
- WebP Replacement: Yes
- QUIC.cloud: Connect account

Page Optimization:
- CSS Minify: Yes
- CSS Combine: Yes (test first)
- JS Minify: Yes
- JS Combine: No (often breaks things)
- HTML Minify: Yes
- Lazy Load Images: Yes
- Responsive Placeholder: Yes
```

### 4. Security

| Plugin | Purpose | Configuration Notes |
|--------|---------|---------------------|
| **Wordfence Security** | Firewall + malware scan | Free tier sufficient |
| **Limit Login Attempts Reloaded** | Brute force protection | 3 attempts, 20 min lockout |

**Wordfence Configuration:**
```
Firewall:
- Web Application Firewall: Enabled
- Real-Time IP Blocklist: Enabled
- Brute Force Protection: Enabled
- Rate Limiting: Enabled

Scan:
- Schedule: Weekly
- Scan theme/plugin files: Yes
- Check core files: Yes
```

### 5. Backup & Recovery

| Plugin | Purpose | Configuration Notes |
|--------|---------|---------------------|
| **UpdraftPlus** | Automated backups | Cloud storage (Google Drive) |

**UpdraftPlus Configuration:**
```
Schedule:
- Files: Weekly
- Database: Daily

Remote Storage:
- Google Drive (authenticate)
- Retain: 4 backups

Include:
- Plugins, themes, uploads, other
- Database: All tables
```

### 6. Legal & Privacy

| Plugin | Purpose | Configuration Notes |
|--------|---------|---------------------|
| **Complianz GDPR/CCPA** | Cookie consent + privacy | Configure per region |

**Complianz Configuration:**
```
Wizard:
- Select regions: US, EU, UK
- Cookie categories: Functional, Analytics, Marketing
- Consent style: Opt-in for EU, Opt-out for US

Cookie Banner:
- Style: Match site design (from DNA colors)
- Position: Bottom
- Close on scroll: No (EU requirement)
```

### 7. Functionality & Utilities

| Plugin | Purpose | Configuration Notes |
|--------|---------|---------------------|
| **WPCode Pro** | Code snippets manager | Organize by function |
| **AI Engine** | AI integration | MCP connection |
| **Redirection** | 301 redirects | Monitor 404s |

**WPCode Organization:**
```
Snippet Categories:
- Design: CSS overrides, animations
- Functionality: Custom PHP
- Analytics: Tracking codes
- Performance: Optimization tweaks
- SEO: Schema additions
```

---

## Site-Specific Plugins

### Content-Type Plugins

| Site Type | Plugins Needed |
|-----------|----------------|
| **Affiliate/Review** | FLAVOR (for comparison tables), WP Recipe Maker |
| **eCommerce** | WooCommerce (if applicable) |
| **Directory** | GeoDirectory or custom post types |
| **Educational** | LearnDash or custom course structure |

### Feature Plugins

| Feature | Plugin | Sites That Need It |
|---------|--------|-------------------|
| **Recipe Cards** | WP Recipe Maker | Witchcraft, Kitchen, Family |
| **Comparison Tables** | TablePress or custom | SmartHome, Wearable, Pulse |
| **Galleries** | Envira Gallery | All with heavy imagery |
| **Forms** | WPForms Lite | All (contact forms) |
| **Social Sharing** | Grow Social | All |

---

## Plugin Installation Order

**CRITICAL: Install in this order to avoid conflicts:**

1. **Security first** - Wordfence, Limit Login
2. **Performance** - LiteSpeed Cache (before content)
3. **SEO** - RankMath (needs content structure)
4. **Theme extensions** - Blocksy Companion
5. **Utilities** - WPCode, Redirection
6. **Content plugins** - Site-specific
7. **Legal** - Complianz (after design finalized)
8. **Backup** - UpdraftPlus (after everything configured)

---

## Plugin Conflicts to Avoid

| Never Combine | Reason |
|---------------|--------|
| Multiple caching plugins | Conflicts, site breaks |
| Multiple SEO plugins | Duplicate meta, confusion |
| Multiple security plugins | Resource hog, false positives |
| Elementor + Gutenberg focus | Pick one page builder approach |

---

## Premium Plugin Licenses

**Plugins requiring license keys:**

| Plugin | License Location | Renewal |
|--------|------------------|---------|
| RankMath Pro | RankMath account | Annual |
| WPCode Pro | WPCode account | Annual |
| LiteSpeed (QUIC.cloud) | QUIC.cloud account | Usage-based |
| ShortPixel | ShortPixel account | Credit-based |

---

## Plugin Health Checks

**Monthly tasks:**

- [ ] Update all plugins (test on staging first)
- [ ] Check Wordfence scan results
- [ ] Verify backups are completing
- [ ] Review LiteSpeed cache hit rate
- [ ] Check for plugin conflicts after updates

---

## Emergency Plugin Procedures

### Site Down After Plugin Update

1. Access via FTP/File Manager
2. Rename `/wp-content/plugins/[problem-plugin]` to `/wp-content/plugins/[problem-plugin]-disabled`
3. Site should recover
4. Investigate and update properly

### Plugin Conflict Diagnosis

1. Deactivate all plugins
2. Activate one by one
3. Test after each activation
4. Identify conflicting pair
5. Find alternative or fix

---

## Plugin Documentation Links

- Blocksy: https://creativethemes.com/blocksy/docs/
- RankMath: https://rankmath.com/kb/
- LiteSpeed: https://docs.litespeedtech.com/lscache/lscwp/
- Wordfence: https://www.wordfence.com/help/
- UpdraftPlus: https://updraftplus.com/support/
- Complianz: https://complianz.io/docs/
