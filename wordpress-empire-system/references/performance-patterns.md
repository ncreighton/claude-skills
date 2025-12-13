# Performance Patterns Reference

Complete guide to WordPress performance optimization using LiteSpeed Cache for Core Web Vitals excellence.

## Performance Philosophy

**"Speed is a feature."**

Every millisecond matters:
- 1 second delay = 7% reduction in conversions
- 53% of mobile users abandon after 3 seconds
- Google uses page speed as a ranking factor
- Fast sites feel more professional and trustworthy

## Core Web Vitals Targets

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤2.5s | 2.5s - 4s | >4s |
| **FID** (First Input Delay) | ≤100ms | 100ms - 300ms | >300ms |
| **CLS** (Cumulative Layout Shift) | ≤0.1 | 0.1 - 0.25 | >0.25 |
| **INP** (Interaction to Next Paint) | ≤200ms | 200ms - 500ms | >500ms |

## LiteSpeed Cache Configuration

### General Settings
```
LiteSpeed Cache → General
├── Automatically Upgrade: ON
├── Guest Mode: ON
├── Guest Optimization: ON
├── Server IP: (Leave empty unless needed)
└── Notifications: ON
```

### Cache Settings
```
LiteSpeed Cache → Cache
├── Enable Cache: ON
├── Cache Logged-in Users: OFF
├── Cache Commenters: OFF
├── Cache REST API: ON
├── Cache Login Page: OFF
├── Cache favicon.ico: ON
├── Cache PHP Resources: ON
├── Cache Mobile: ON
├── List of Mobile User Agents: (default)
├── Private Cached URIs: (blank)
├── Force Public Cache URIs: (blank)
├── Drop Query String: utm_source, utm_medium, utm_campaign, fbclid, gclid
└── TTL
    ├── Default Public Cache TTL: 604800 (7 days)
    ├── Default Private Cache TTL: 1800
    ├── Default Front Page TTL: 604800
    ├── Default Feed TTL: 0 (disabled)
    └── Default 404 TTL: 3600
```

### Purge Settings
```
LiteSpeed Cache → Purge
├── Purge All On Upgrade: ON
├── Auto Purge Rules For Publish/Update
│   ├── All pages: OFF
│   ├── Front page: ON
│   ├── Home page: ON
│   ├── Pages: ON
│   ├── Posts: ON
│   ├── Author archive: ON
│   ├── Yearly archive: ON
│   ├── Monthly archive: ON
│   ├── Daily archive: ON
│   └── Category/Tag archives: ON
├── Serve Stale: ON
└── Scheduled Purge URLs: (blank)
```

### Excludes
```
LiteSpeed Cache → Excludes
├── Do Not Cache URIs:
│   /cart/
│   /checkout/
│   /my-account/
│   /wp-admin/
├── Do Not Cache Query Strings: (blank - handled in cache)
├── Do Not Cache Categories: (blank)
├── Do Not Cache Tags: (blank)
├── Do Not Cache Cookies:
│   woocommerce_cart_hash
│   woocommerce_items_in_cart
│   wp_woocommerce_session
├── Do Not Cache User Agents: (blank)
└── Do Not Cache Roles: Administrator
```

### Page Optimization - CSS
```
LiteSpeed Cache → Page Optimization → CSS Settings
├── CSS Minify: ON
├── CSS Combine: ON (test carefully)
├── Generate UCSS: ON (Remove unused CSS)
├── UCSS Inline: OFF
├── CSS Combine External and Inline: ON
├── Load CSS Asynchronously: ON
├── CCSS Per URL: ON
├── Inline CSS Async Lib: ON
├── Font Display Optimization: Swap
└── UCSS Whitelist: (add if needed)
```

### Page Optimization - JS
```
LiteSpeed Cache → Page Optimization → JS Settings
├── JS Minify: ON
├── JS Combine: OFF (often causes issues)
├── JS Combine External and Inline: OFF
├── Load JS Deferred: ON
├── Load Inline JS: Default
├── Exclude JQuery: OFF
└── JS Delayed
    ├── Enable: ON
    ├── Delay Inline JS: ON
    └── JS Delayed Includes:
        /gtag
        /analytics
        /ga.js
        /facebook
        /pixel
        /hotjar
        /intercom
        /crisp
        /drift
        /tracking
```

### Page Optimization - HTML
```
LiteSpeed Cache → Page Optimization → HTML Settings
├── HTML Minify: ON
├── DNS Prefetch:
    fonts.googleapis.com
    fonts.gstatic.com
    www.google-analytics.com
    www.googletagmanager.com
├── DNS Prefetch Control: ON
├── Remove Query Strings: ON
├── Load Google Fonts Asynchronously: ON
├── Remove Google Fonts: OFF
├── Remove WordPress Emoji: ON
├── Remove Noscript Tags: OFF
└── Async HTML API: Disabled
```

### Page Optimization - Media
```
LiteSpeed Cache → Page Optimization → Media Settings
├── Lazy Load Images: ON
├── Basic Image Placeholder: Grey background
├── Responsive Placeholder: ON
├── Responsive Placeholder SVG: (default)
├── Responsive Placeholder Color: #E8E8E8
├── LQIP Cloud Generator: ON
├── LQIP Quality: Low
├── Generate LQIP In Background: ON
├── Lazy Load Iframes: ON
├── Add Missing Sizes: ON
└── Inline Lazy Load Images Library: ON
```

### Page Optimization - VPI (Viewport Images)
```
LiteSpeed Cache → Page Optimization → VPI
├── Viewport Images: ON
├── Viewport Images Cron: ON
└── VPI Pages: (leave default)
```

### Image Optimization
```
LiteSpeed Cache → Image Optimization
├── Auto Request Cron: ON
├── Auto Pull Cron: ON
├── Optimize Original Images: ON
├── Remove Original Backups: OFF (keep first time)
├── Optimize Losslessly: OFF (lossy is better)
├── Preserve EXIF/XMP Data: OFF
├── Create WebP Versions: ON
├── Image WebP Replacement: ON
├── WebP For Extra srcset: ON
└── Optimize Images Setting
    └── WebP Lossless: OFF
```

### CDN Settings
```
LiteSpeed Cache → CDN
├── QUIC.cloud CDN: ON (if using)
├── CDN URL: https://cdn.yoursite.com
├── Original URLs: wp-content/
├── Included Directories: wp-content/themes, wp-content/plugins
├── Exclude Path: wp-content/cache
├── Load JQuery Remotely: OFF
├── Cloudflare API: (if using)
└── QUIC.cloud:
    ├── Enable: ON
    ├── CDN Mapping: ON
    └── Region: Auto
```

### Object Cache
```
LiteSpeed Cache → Object
├── Object Cache: ON (if server supports Redis/Memcached)
├── Method: Redis (preferred) or Memcached
├── Host: 127.0.0.1
├── Port: 6379
├── Default Object Lifetime: 360
├── Admin Bar: ON
├── Transients: ON
├── Persistent Connection: ON
├── Cache WP-Admin: OFF
├── Store Transients in DB: OFF
└── Global Groups: (default)
```

### Browser Cache
```
LiteSpeed Cache → Browser
├── Browser Cache: ON
└── Browser Cache TTL: 31557600 (1 year)
```

### Database Optimization
```
LiteSpeed Cache → Database
├── Clean All: (run monthly)
├── Post Revisions: ON
├── Auto Drafts: ON
├── Trashed Posts: ON
├── Spam Comments: ON
├── Trashed Comments: ON
├── Trackbacks/Pingbacks: ON
├── Expired Transients: ON
├── All Transients: OFF (be careful)
├── Optimize Tables: ON
└── DB Optimization Cron: Weekly
```

### Crawler Settings
```
LiteSpeed Cache → Crawler
├── Crawler: ON
├── Delay: 500 (ms between requests)
├── Run Duration: 400
├── Interval Between Runs: 600
├── Crawl Interval: 302400
├── Threads: 3
├── Server Load Limit: 1
├── Custom Sitemap: (leave blank, uses default)
└── Drop Domain from Sitemap: ON
```

## Additional Performance Plugins

### Perfmatters (Complement to LiteSpeed)
```
Perfmatters → Options
├── General
│   ├── Disable Emojis: ON
│   ├── Disable Dashicons: ON (if not logged in)
│   ├── Disable Embeds: OFF (need YouTube)
│   ├── Remove jQuery Migrate: ON (test first)
│   └── Disable XML-RPC: ON
├── Assets
│   ├── Script Manager: Enable
│   └── Disable per-page: Analytics on non-essential pages
└── Lazy Loading
    └── Defer to LiteSpeed
```

### Asset CleanUp Pro (Alternative)
```
Asset CleanUp → Settings
├── Strip Version Query Strings: ON
├── Disable Emojis: ON
├── Remove RSS Feed Links: OFF
└── Script/Style Manager:
    └── Disable unused per-page
```

## Image Optimization Strategy

### Image Formats
| Format | Use Case | Compression |
|--------|----------|-------------|
| WebP | All images (primary) | LiteSpeed auto-converts |
| JPEG | Photos, complex images | 80% quality |
| PNG | Graphics with transparency | Lossless |
| SVG | Icons, logos | Vector |

### Image Sizes
```
Hero images: 1920px wide max
Content images: 1200px wide max
Thumbnails: 400px wide
Featured images: 1200x628px (social ratio)
```

### Responsive Images
LiteSpeed handles responsive images automatically with:
- Add Missing Sizes: ON
- Responsive Placeholder: ON
- WebP Replacement: ON

## Font Optimization

### Font Loading Strategy
```css
@font-face {
    font-family: 'CustomFont';
    src: url('font.woff2') format('woff2');
    font-display: swap;
    font-weight: 400;
    font-style: normal;
}
```

### LiteSpeed Font Display
Set in Page Optimization → CSS Settings:
```
Font Display Optimization: Swap
Load Google Fonts Asynchronously: ON
```

### Preload Critical Fonts
Add in functions.php or WPCode:
```php
add_action('wp_head', function() {
    echo '<link rel="preload" href="/wp-content/themes/blocksy-child/assets/fonts/font.woff2" as="font" type="font/woff2" crossorigin>';
}, 1);
```

## Database Optimization

### Automated Cleanup
LiteSpeed's Database Optimization handles:
- Post revisions (keep last 5)
- Auto drafts
- Trashed content
- Spam comments
- Expired transients
- Table optimization

### Manual wp-config.php Additions
```php
// Limit post revisions
define('WP_POST_REVISIONS', 5);

// Increase autosave interval
define('AUTOSAVE_INTERVAL', 300);

// Increase memory
define('WP_MEMORY_LIMIT', '256M');
define('WP_MAX_MEMORY_LIMIT', '512M');
```

## Hosting Requirements

### Server Configuration
- PHP 8.1+ (preferably 8.2)
- LiteSpeed Web Server (for full LSCACHE)
- MySQL 8.0+ or MariaDB 10.4+
- Redis or Memcached (for object cache)
- HTTP/2 or HTTP/3 support
- SSD storage

### PHP Configuration
```ini
memory_limit = 256M
max_execution_time = 300
upload_max_filesize = 64M
post_max_size = 64M
max_input_vars = 5000
opcache.enable = 1
opcache.memory_consumption = 256
```

## Performance Testing

### Testing Tools
| Tool | Purpose | Target |
|------|---------|--------|
| PageSpeed Insights | Core Web Vitals | 90+ |
| GTmetrix | Detailed waterfall | A grade |
| WebPageTest | Advanced analysis | - |
| Chrome DevTools | Real-time debugging | - |

### Testing Protocol
1. Test in incognito mode
2. Test multiple page types (home, post, category)
3. Test mobile and desktop separately
4. Run 3 tests, take average
5. Test after each major change

### Quick PageSpeed Test
```bash
# Using PageSpeed Insights API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://yoursite.com&strategy=mobile"
```

## Performance Checklist

### Immediate Impact
- [ ] Enable LiteSpeed Cache
- [ ] Enable CSS/JS minification
- [ ] Enable lazy loading
- [ ] Enable WebP conversion
- [ ] Remove unused CSS (UCSS)
- [ ] Delay non-critical JavaScript

### Medium Term
- [ ] Enable object cache (Redis)
- [ ] Configure CDN (QUIC.cloud)
- [ ] Optimize database
- [ ] Enable crawler preload
- [ ] Font display: swap

### Ongoing
- [ ] Weekly database cleanup
- [ ] Monthly plugin audit
- [ ] Regular performance testing
- [ ] Core Web Vitals monitoring
- [ ] Cache clearing after updates

## Troubleshooting

### Common Issues

**Page not caching:**
- Check exclude rules
- Verify no cache-blocking cookies
- Check for PHP errors

**CSS/JS broken after optimization:**
- Disable CSS combine, keep minify
- Disable JS combine
- Add problematic scripts to exclude

**Lazy load not working:**
- Verify no conflicting plugins
- Check if images have dimensions
- Test with Viewport Images ON

**Slow TTFB:**
- Enable object cache
- Check server load
- Optimize database
- Contact hosting support

### Clear All Caches
```bash
# Via WP-CLI
wp litespeed-purge all

# Via Dashboard
LiteSpeed Cache → Toolbox → Purge All
```

### Debug Mode
Add to wp-config.php:
```php
define('LSCWP_LOG', true);
define('LSCWP_LOG_MORE', true);
```

Check logs at: wp-content/debug.log
