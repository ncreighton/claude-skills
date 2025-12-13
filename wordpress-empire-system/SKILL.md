---
name: wordpress-empire-system
description: "Ultimate WordPress design/dev system for 17-site publishing empire. Triggers: design site, build page, customize theme, homepage, fix CSS, structure site, hero section, Blocksy, Astra, Elementor, blocks, Gutenberg, RankMath, LiteSpeed, AI Engine MCP, category structure, navigation, responsive, conversion, SEO, schema, typography, animations, CTAs, templates. Uses WorldPressIt 8000+ premium plugins. Creates human-feeling, SEO-optimized WordPress masterpieces. Works in Claude Code projects."
---

# WordPress Empire System

Ultimate WordPress design, development, structure building, and optimization system for Nick's 17-site publishing empire. Creates masterpiece-level sites that are beautiful, human-feeling, engaging, SEO-optimized, and conversion-focused.

**Works in both Claude.ai AND Claude Code terminal for project-based development.**

## Core Tech Stack

### Primary Theme Stack
| Tool | Purpose | Priority |
|------|---------|----------|
| **Blocksy Theme** | Primary theme | DEFAULT |
| **Blocksy Companion Pro** | Theme extensions | DEFAULT |
| **Astra Theme** | Secondary option | ALTERNATIVE |
| **Astra Pro** | Theme extensions | ALTERNATIVE |

### Page Building
| Tool | Purpose |
|------|---------|
| **Gutenberg/Blocks** | Content editing, block patterns |
| **Elementor Pro** | Advanced page building |

### Essential Plugins (Default Stack)
| Plugin | Purpose |
|--------|---------|
| **RankMath SEO Pro** | SEO (NOT Yoast) |
| **LiteSpeed Cache** | Performance (NOT WP Rocket) |
| **AI Engine** | WordPress MCP connection |
| **WPCode** | Custom code snippets |
| **Complianz** | GDPR/Privacy compliance |
| **Content Egg** | Affiliate/comparison content |
| **Easy Table of Contents** | Navigation |
| **Wordfence** | Security |
| **UpdraftPlus** | Backups |

## Quick Start

### Before ANY WordPress Work
1. **Identify the target site** and load its brand from `references/brand-systems.md`
2. **Read relevant reference files** based on task:
   - Design → `references/design-mastery.md`
   - Plugins → `references/plugin-arsenal.md`
   - Structure → `references/site-architecture.md`
   - Performance → `references/performance-patterns.md`
   - SEO → `references/seo-structure.md`
   - Conversion → `references/engagement-patterns.md`
   - Blocksy/Astra → `references/theme-systems.md`
   - Claude Code → `references/claude-code-workflows.md`

3. **Execute with confidence** - be bold, decisive, visionary

## Claude Code Project Workflow

When working in Claude Code terminal on WordPress projects:

### Project Structure
```
site-name-project/
├── README.md                 # Project overview, goals
├── theme/
│   ├── blocksy-child/       # Child theme files
│   │   ├── style.css
│   │   ├── functions.php
│   │   └── templates/
│   └── customizations/      # Theme customizations
├── plugins/
│   ├── custom-functionality/
│   │   ├── custom-functionality.php
│   │   └── includes/
│   └── snippets/            # WPCode snippets
├── blocks/
│   ├── custom-blocks/       # Custom Gutenberg blocks
│   └── block-patterns/      # Reusable patterns
├── assets/
│   ├── css/                 # Custom CSS
│   ├── js/                  # Custom JavaScript
│   ├── images/              # Optimized images
│   └── fonts/               # Custom fonts
├── content/
│   ├── pages/               # Page content/structure
│   └── templates/           # Content templates
├── config/
│   ├── blocksy-settings.json
│   ├── rankmath-settings.json
│   ├── litespeed-settings.json
│   └── elementor-settings.json
└── docs/
    ├── brand-guide.md
    ├── structure-plan.md
    └── seo-strategy.md
```

### Claude Code Commands
```bash
# Initialize new site project
mkdir -p site-name/{theme/blocksy-child,plugins/custom-functionality,blocks,assets/{css,js,images},content,config,docs}

# Create child theme
cat > site-name/theme/blocksy-child/style.css << 'EOF'
/*
 Theme Name: Site Name Child
 Template: blocksy
 Version: 1.0.0
*/
EOF

# Generate brand CSS variables
python /mnt/skills/user/wordpress-empire-system/scripts/generate_brand_css.py witchcraft > site-name/assets/css/brand-variables.css

# Generate pre-launch checklist
python /mnt/skills/user/wordpress-empire-system/scripts/design_checklist.py "Site Name" full > site-name/docs/launch-checklist.md
```

## Blocksy Theme System

### Blocksy Customizer Structure
```
Appearance → Customize
├── General Options
│   ├── Colors → Use brand CSS variables
│   ├── Typography → Set font families
│   ├── Background → Site background
│   └── Container → Max-width (1200px default)
├── Header
│   ├── Header Builder → Drag-drop header elements
│   ├── Transparent Header → For hero sections
│   └── Sticky Header → Scroll behavior
├── Footer
│   ├── Footer Builder → Drag-drop footer elements
│   └── Footer Widgets → Widget areas
├── Blog
│   ├── Blog Posts → Archive layout
│   ├── Single Post → Post template
│   └── Categories → Archive styling
├── Pages
│   ├── Single Page → Default page template
│   └── 404 Page → Error page
└── WooCommerce (if active)
    ├── Shop → Product archive
    └── Single Product → Product page
```

### Blocksy Pro Features to Use
- **Custom Headers** - Per-page header variations
- **Custom Footers** - Per-page footer variations
- **Hooks System** - Insert content anywhere
- **Local Google Fonts** - Performance
- **Custom Post Types** - Extended content
- **Content Blocks** - Reusable sections
- **Mega Menu** - Advanced navigation

### Blocksy Child Theme functions.php
```php
<?php
/**
 * Site Name Child Theme
 */

// Enqueue parent and child styles
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style('blocksy-parent', get_template_directory_uri() . '/style.css');
    wp_enqueue_style('child-style', get_stylesheet_uri(), ['blocksy-parent']);
    
    // Brand CSS variables
    wp_enqueue_style('brand-variables', get_stylesheet_directory_uri() . '/assets/css/brand-variables.css');
});

// Add custom image sizes
add_action('after_setup_theme', function() {
    add_image_size('hero-image', 1920, 1080, true);
    add_image_size('card-image', 600, 400, true);
    add_image_size('thumbnail-square', 300, 300, true);
});

// Register block patterns
add_action('init', function() {
    register_block_pattern_category('site-name', [
        'label' => __('Site Name Patterns', 'site-name')
    ]);
});
```

## Block Patterns Library

### Hero Section Pattern
```php
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|80","bottom":"var:preset|spacing|80"}}},"backgroundColor":"primary","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-primary-background-color has-background" style="padding-top:var(--wp--preset--spacing--80);padding-bottom:var(--wp--preset--spacing--80)">

<!-- wp:heading {"textAlign":"center","level":1,"style":{"typography":{"fontSize":"clamp(2.5rem, 5vw, 4rem)"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="font-size:clamp(2.5rem, 5vw, 4rem)">Your Compelling Headline Here</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"1.25rem"}}} -->
<p class="has-text-align-center" style="font-size:1.25rem">Supporting subheadline that explains the value proposition clearly.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons">
<!-- wp:button {"className":"is-style-fill"} -->
<div class="wp-block-button is-style-fill"><a class="wp-block-button__link wp-element-button">Primary CTA</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button">Secondary CTA</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->

</div>
<!-- /wp:group -->
```

### Feature Grid Pattern
```php
<!-- wp:group {"align":"wide","layout":{"type":"constrained"}} -->
<div class="wp-block-group alignwide">
<!-- wp:columns {"align":"wide"} -->
<div class="wp-block-columns alignwide">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Feature One</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Description of this feature and its benefit to the user.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Feature Two</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Description of this feature and its benefit to the user.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Feature Three</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Description of this feature and its benefit to the user.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->
```

## RankMath SEO Configuration

### General Settings
```
Dashboard → Rank Math → General Settings
├── Links
│   ├── Strip Category Base: ON
│   ├── Redirect Attachments: ON
│   ├── Nofollow External Links: OFF (manual control)
│   └── Open External Links in New Tab: ON
├── Images
│   ├── Add Missing ALT: ON
│   └── Add Missing Title: ON
└── Breadcrumbs
    └── Enable: ON
```

### Titles & Meta
```
Rank Math → Titles & Meta
├── Global Meta
│   ├── Separator: –
│   └── Capitalize Titles: ON
├── Homepage
│   ├── Title: %sitename% %sep% %tagline%
│   └── Description: [Compelling 155-char description]
├── Posts
│   ├── Title: %title% %sep% %sitename%
│   └── Description: %excerpt%
└── Categories
    ├── Title: %term% %sep% %sitename%
    └── Description: %term_description%
```

### Schema Settings
```
Rank Math → Titles & Meta → Posts
├── Schema Type: Article
├── Article Type: BlogPosting
└── Default: ON

For Reviews: Product schema
For How-To: HowTo schema
For FAQ: FAQPage schema
```

## LiteSpeed Cache Configuration

### General Settings
```
LiteSpeed Cache → General
├── Automatically Upgrade: ON
├── Guest Mode: ON
└── Guest Optimization: ON
```

### Cache Settings
```
LiteSpeed Cache → Cache
├── Enable Cache: ON
├── Cache Logged-in Users: OFF
├── Cache REST API: ON
├── Cache Mobile: ON (separate cache)
└── Cache favicon.ico: ON
```

### Page Optimization
```
LiteSpeed Cache → Page Optimization
├── CSS Settings
│   ├── Minify CSS: ON
│   ├── Combine CSS: ON (test first)
│   ├── UCSS: ON
│   └── CSS Async Load: ON
├── JS Settings
│   ├── Minify JS: ON
│   ├── Combine JS: OFF
│   ├── JS Defer: ON
│   └── JS Delay: ON
└── Image Optimization
    ├── Auto Request Cron: ON
    ├── WebP Replacement: ON
    └── Lazy Load Images: ON
```

## AI Engine MCP Configuration

### WordPress MCP Connection
```
AI Engine → Settings → REST API
├── Enable REST API: ON
├── Authentication: Bearer Token
└── Token: [Generate secure token]
```

## WPCode Snippet Library

### Performance Snippet
```php
// Remove Query Strings
add_filter('script_loader_src', 'remove_query_strings', 15, 1);
add_filter('style_loader_src', 'remove_query_strings', 15, 1);
function remove_query_strings($src) {
    if (strpos($src, '?ver=')) {
        $src = remove_query_arg('ver', $src);
    }
    return $src;
}
```

### Security Snippet
```php
// Disable XML-RPC
add_filter('xmlrpc_enabled', '__return_false');
remove_action('wp_head', 'wp_generator');
```

### UX Enhancement Snippet
```php
// Smooth Scroll
add_action('wp_footer', function() {
    echo '<style>html{scroll-behavior:smooth}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}</style>';
});
```

## Design Principles

### "Modern Tech Picasso" Philosophy
1. **Unexpected but intentional** - Every surprising choice has purpose
2. **Bold without chaos** - Push boundaries while maintaining usability
3. **Human craftsmanship** - Every element feels hand-designed
4. **Memorable moments** - Create at least one "wow" per page
5. **Functional art** - Beauty serves purpose

### Anti-Patterns (NEVER Do These)
- Generic stock photos with filters
- Gradient backgrounds on white (AI look)
- Predictable card layouts
- Template-obvious designs
- Purple-to-blue gradients (screams AI)
- Roboto/Inter/Arial as body font

## Site-Specific Brand Quick Reference

| Site | Theme | Primary Color | Voice |
|------|-------|---------------|-------|
| WitchcraftForBeginners | Blocksy | #4A1C6F | Mystical warmth |
| SmartHomeWizards | Blocksy | #0066CC | Tech authority |
| AIinActionHub | Blocksy | #00F0FF | Future analyst |
| MythicalArchives | Blocksy | #8B4513 | Scholarly wonder |
| Family-Flourish | Astra | #E8887C | Nurturing guide |
| BulletJournals | Blocksy | #1A1A1A | Creative organizer |

See `references/brand-systems.md` for complete guidelines.

## Reference Files

| File | Purpose |
|------|---------|
| `references/design-mastery.md` | Complete design philosophy & patterns |
| `references/plugin-arsenal.md` | WorldPressIt plugin guide |
| `references/brand-systems.md` | All 17 site brand guidelines |
| `references/site-architecture.md` | Categories, navigation, structure |
| `references/seo-structure.md` | RankMath config, schema patterns |
| `references/performance-patterns.md` | LiteSpeed config, Core Web Vitals |
| `references/engagement-patterns.md` | Conversion, CTAs, lead capture |
| `references/theme-systems.md` | Blocksy & Astra customization |
| `references/claude-code-workflows.md` | Project-based development |

## Critical Reminders

- **Blocksy is primary theme** - Master it completely
- **RankMath for SEO** - Not Yoast
- **LiteSpeed for caching** - Not WP Rocket
- **AI Engine for MCP** - WordPress API connection
- **Blocks/Gutenberg native** - Use block patterns
- **WorldPressIt access** - 8,000+ plugins available
- **Brand consistency sacred** - Never cross brand voices
- **Human feeling paramount** - If it looks AI-generated, redo it
- **Claude Code projects** - Structure for terminal development
