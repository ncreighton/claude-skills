# Claude Code Workflows Reference

Complete guide to building WordPress sites using Claude Code projects - structured, autonomous, and production-ready.

## Project Philosophy

**"Structure enables perfection."**

Every WordPress project in Claude Code should:
1. Have organized file structure from day one
2. Contain all customizations in version-controllable files
3. Be deployable to any WordPress installation
4. Document decisions and configurations
5. Evolve autonomously as the site grows

## Project Initialization

### Create New Site Project
```bash
# Set project name
PROJECT="smarthomewizards"
SITE_NAME="Smart Home Wizards"

# Create full structure
mkdir -p $PROJECT/{theme/{blocksy-child/{templates,assets/{css,js,images}},customizations},plugins/{custom-functionality/includes,snippets},blocks/{custom-blocks,patterns},assets/{css,js,images,fonts},content/{pages,templates},config,docs,exports}

# Navigate to project
cd $PROJECT

# Initialize README
cat > README.md << EOF
# $SITE_NAME

WordPress site project for $SITE_NAME.

## Quick Start
1. Upload \`theme/blocksy-child/\` to \`wp-content/themes/\`
2. Upload \`plugins/custom-functionality/\` to \`wp-content/plugins/\`
3. Import \`config/\` settings via respective plugin interfaces
4. Activate child theme and plugins

## Structure
- \`theme/\` - Child theme and customizations
- \`plugins/\` - Custom plugins and WPCode snippets
- \`blocks/\` - Custom blocks and patterns
- \`assets/\` - Global assets (not theme-specific)
- \`content/\` - Page content and templates
- \`config/\` - Plugin configurations (exportable)
- \`docs/\` - Documentation
- \`exports/\` - Exported data (Customizer, etc.)

## Tech Stack
- Theme: Blocksy + Blocksy Companion Pro
- SEO: RankMath Pro
- Cache: LiteSpeed Cache
- MCP: AI Engine
- Code: WPCode

Generated: $(date)
EOF

echo "✅ Project $PROJECT initialized"
```

### Initialize Child Theme
```bash
# Create Blocksy child theme style.css
cat > theme/blocksy-child/style.css << EOF
/*
 Theme Name: $SITE_NAME Child
 Theme URI: https://$(echo $PROJECT | tr '[:upper:]' '[:lower:]').com
 Description: Custom child theme for $SITE_NAME
 Author: Nick
 Template: blocksy
 Version: 1.0.0
 Text Domain: ${PROJECT}-child
*/

/* Brand variables loaded via functions.php */
/* Custom styles below */
EOF

# Create functions.php
cat > theme/blocksy-child/functions.php << 'PHPEOF'
<?php
/**
 * Child Theme Functions
 */

// Prevent direct access
if (!defined('ABSPATH')) exit;

/**
 * Enqueue styles and scripts
 */
add_action('wp_enqueue_scripts', function() {
    $theme = wp_get_theme();
    $version = $theme->get('Version');
    
    // Parent theme
    wp_enqueue_style('blocksy-parent', get_template_directory_uri() . '/style.css');
    
    // Child theme
    wp_enqueue_style('child-style', get_stylesheet_uri(), ['blocksy-parent'], $version);
    
    // Brand CSS variables
    wp_enqueue_style('brand-variables', 
        get_stylesheet_directory_uri() . '/assets/css/brand-variables.css', 
        [], $version
    );
    
    // Custom CSS
    wp_enqueue_style('custom-styles', 
        get_stylesheet_directory_uri() . '/assets/css/custom.css', 
        ['brand-variables'], $version
    );
    
    // Custom JS
    wp_enqueue_script('custom-scripts', 
        get_stylesheet_directory_uri() . '/assets/js/custom.js', 
        ['jquery'], $version, true
    );
}, 20);

/**
 * Custom image sizes
 */
add_action('after_setup_theme', function() {
    add_image_size('hero', 1920, 1080, true);
    add_image_size('card', 600, 400, true);
    add_image_size('square', 400, 400, true);
    add_image_size('featured-lg', 1200, 628, true);
});

/**
 * Register block pattern category
 */
add_action('init', function() {
    register_block_pattern_category('sitename', [
        'label' => __('Site Patterns', 'sitename-child')
    ]);
});

/**
 * Excerpt customization
 */
add_filter('excerpt_length', function() { return 25; });
add_filter('excerpt_more', function() { return '...'; });

/**
 * Add theme support
 */
add_action('after_setup_theme', function() {
    add_theme_support('responsive-embeds');
    add_theme_support('align-wide');
});
PHPEOF

echo "✅ Child theme initialized"
```

### Initialize Custom Plugin
```bash
# Create custom functionality plugin
PLUGIN_DIR="plugins/custom-functionality"

cat > $PLUGIN_DIR/custom-functionality.php << 'PHPEOF'
<?php
/**
 * Plugin Name: Site Custom Functionality
 * Description: Custom functionality for this site
 * Version: 1.0.0
 * Author: Nick
 */

// Prevent direct access
if (!defined('ABSPATH')) exit;

// Define constants
define('SCF_VERSION', '1.0.0');
define('SCF_PATH', plugin_dir_path(__FILE__));
define('SCF_URL', plugin_dir_url(__FILE__));

// Include files
require_once SCF_PATH . 'includes/security.php';
require_once SCF_PATH . 'includes/performance.php';
require_once SCF_PATH . 'includes/customizations.php';

// Activation hook
register_activation_hook(__FILE__, function() {
    flush_rewrite_rules();
});

// Deactivation hook
register_deactivation_hook(__FILE__, function() {
    flush_rewrite_rules();
});
PHPEOF

# Create includes files
cat > $PLUGIN_DIR/includes/security.php << 'PHPEOF'
<?php
/**
 * Security Enhancements
 */

// Disable XML-RPC
add_filter('xmlrpc_enabled', '__return_false');

// Remove WordPress version
remove_action('wp_head', 'wp_generator');

// Disable REST API for non-logged users (selective)
add_filter('rest_authentication_errors', function($result) {
    if (empty($result) && !is_user_logged_in()) {
        // Allow specific endpoints
        $allowed = ['/wp-json/wp/v2/posts', '/wp-json/wp/v2/pages', '/wp-json/rankmath/'];
        $request_uri = $_SERVER['REQUEST_URI'] ?? '';
        
        foreach ($allowed as $endpoint) {
            if (strpos($request_uri, $endpoint) !== false) {
                return $result;
            }
        }
    }
    return $result;
});
PHPEOF

cat > $PLUGIN_DIR/includes/performance.php << 'PHPEOF'
<?php
/**
 * Performance Enhancements
 */

// Remove query strings from static resources
add_filter('script_loader_src', 'scf_remove_query_strings', 15);
add_filter('style_loader_src', 'scf_remove_query_strings', 15);
function scf_remove_query_strings($src) {
    if (strpos($src, '?ver=')) {
        $src = remove_query_arg('ver', $src);
    }
    return $src;
}

// Limit post revisions
if (!defined('WP_POST_REVISIONS')) {
    define('WP_POST_REVISIONS', 5);
}

// Disable emojis
add_action('init', function() {
    remove_action('wp_head', 'print_emoji_detection_script', 7);
    remove_action('admin_print_scripts', 'print_emoji_detection_script');
    remove_action('wp_print_styles', 'print_emoji_styles');
    remove_action('admin_print_styles', 'print_emoji_styles');
    remove_filter('the_content_feed', 'wp_staticize_emoji');
    remove_filter('comment_text_rss', 'wp_staticize_emoji');
    remove_filter('wp_mail', 'wp_staticize_emoji_for_email');
});
PHPEOF

cat > $PLUGIN_DIR/includes/customizations.php << 'PHPEOF'
<?php
/**
 * Site Customizations
 */

// Add smooth scrolling
add_action('wp_footer', function() {
    echo '<style>html{scroll-behavior:smooth}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}</style>';
});

// Add last modified to singular pages
add_action('wp_head', function() {
    if (is_singular()) {
        echo '<meta property="article:modified_time" content="' . esc_attr(get_the_modified_time('c')) . '">' . "\n";
    }
});
PHPEOF

echo "✅ Custom functionality plugin initialized"
```

## File Structure Deep Dive

### Complete Project Tree
```
site-project/
├── README.md                           # Project documentation
├── .gitignore                          # Git ignore rules
│
├── theme/
│   ├── blocksy-child/                  # Child theme
│   │   ├── style.css                   # Theme header
│   │   ├── functions.php               # Theme functions
│   │   ├── screenshot.png              # Theme screenshot
│   │   ├── templates/                  # Custom templates
│   │   │   ├── template-landing.php    # Landing page template
│   │   │   └── template-full-width.php # Full width template
│   │   └── assets/
│   │       ├── css/
│   │       │   ├── brand-variables.css # CSS variables
│   │       │   └── custom.css          # Custom styles
│   │       ├── js/
│   │       │   └── custom.js           # Custom scripts
│   │       └── images/                 # Theme images
│   └── customizations/
│       ├── customizer.json             # Exported customizer
│       └── hooks.md                    # Hook documentation
│
├── plugins/
│   ├── custom-functionality/           # Main custom plugin
│   │   ├── custom-functionality.php
│   │   └── includes/
│   │       ├── security.php
│   │       ├── performance.php
│   │       └── customizations.php
│   └── snippets/                       # WPCode snippets
│       ├── analytics.php
│       ├── schema.php
│       └── shortcodes.php
│
├── blocks/
│   ├── custom-blocks/                  # Custom Gutenberg blocks
│   │   └── hero-block/
│   │       ├── block.json
│   │       ├── edit.js
│   │       ├── save.js
│   │       └── style.css
│   └── patterns/                       # Block patterns
│       ├── hero-section.php
│       ├── feature-grid.php
│       ├── testimonial-section.php
│       └── cta-section.php
│
├── assets/
│   ├── css/                            # Global CSS (not theme)
│   ├── js/                             # Global JS
│   ├── images/                         # Site images
│   │   ├── logo.svg
│   │   ├── favicon.png
│   │   └── og-image.jpg
│   └── fonts/                          # Custom fonts
│       └── local-fonts/
│
├── content/
│   ├── pages/                          # Page content
│   │   ├── homepage.md                 # Homepage content
│   │   ├── about.md                    # About page
│   │   └── contact.md                  # Contact page
│   └── templates/                      # Content templates
│       ├── post-template.md
│       └── review-template.md
│
├── config/
│   ├── blocksy-settings.json           # Blocksy config
│   ├── rankmath-settings.json          # RankMath config
│   ├── litespeed-settings.json         # LiteSpeed config
│   └── ai-engine-settings.json         # AI Engine config
│
├── docs/
│   ├── brand-guide.md                  # Brand guidelines
│   ├── structure-plan.md               # Site structure
│   ├── seo-strategy.md                 # SEO strategy
│   ├── content-calendar.md             # Content planning
│   └── launch-checklist.md             # Pre-launch checklist
│
└── exports/
    ├── customizer-export.json          # Customizer settings
    ├── widgets-export.json             # Widget settings
    └── menus-export.json               # Menu structure
```

### .gitignore Template
```bash
cat > .gitignore << 'EOF'
# WordPress
wp-content/uploads/
wp-content/cache/
wp-content/upgrade/
wp-content/backup-db/
wp-content/backups/

# Sensitive
*.log
*.sql
wp-config.php
.htaccess
.env

# System
.DS_Store
Thumbs.db
*.swp
*.swo

# IDE
.idea/
.vscode/
*.sublime-project
*.sublime-workspace

# Dependencies
node_modules/
vendor/

# Build
dist/
build/
EOF
```

## Workflow Commands

### Generate Brand CSS
```bash
# Using the skill's script
python /mnt/skills/user/wordpress-empire-system/scripts/generate_brand_css.py witchcraft > theme/blocksy-child/assets/css/brand-variables.css
```

### Generate Checklist
```bash
# Generate pre-launch checklist
python /mnt/skills/user/wordpress-empire-system/scripts/design_checklist.py "Site Name" full > docs/launch-checklist.md
```

### Create Block Pattern
```bash
cat > blocks/patterns/hero-section.php << 'EOF'
<?php
/**
 * Title: Hero Section
 * Slug: sitename/hero-section
 * Categories: sitename
 */
?>
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|80","bottom":"var:preset|spacing|80"}}}} -->
<div class="wp-block-group alignfull" style="padding-top:var(--wp--preset--spacing--80);padding-bottom:var(--wp--preset--spacing--80)">

<!-- wp:heading {"textAlign":"center","level":1} -->
<h1 class="wp-block-heading has-text-align-center">Headline</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center">Subheadline text here.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons">
<!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button">CTA Button</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->

</div>
<!-- /wp:group -->
EOF
```

### Create WPCode Snippet
```bash
cat > plugins/snippets/analytics.php << 'EOF'
<?php
/**
 * Snippet: Google Analytics 4
 * Location: Header
 */
?>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
EOF
```

## Config Export/Import

### Export Blocksy Settings
```bash
# Via Customizer Export/Import plugin
# Export from: Appearance → Customize → Export/Import
# Save to: config/blocksy-settings.json
```

### Export RankMath Settings
```bash
# Via RankMath
# Export from: Rank Math → Status & Tools → Import & Export
# Save to: config/rankmath-settings.json
```

### Export LiteSpeed Settings
```bash
# Via LiteSpeed Cache
# Export from: LiteSpeed Cache → Toolbox → Export
# Save to: config/litespeed-settings.json
```

## Development Workflow

### Daily Development
```bash
# 1. Pull latest changes (if using git)
git pull

# 2. Make changes in appropriate directories
# - Theme changes → theme/blocksy-child/
# - New functionality → plugins/custom-functionality/
# - Block patterns → blocks/patterns/
# - Documentation → docs/

# 3. Test locally or on staging

# 4. Commit changes
git add .
git commit -m "Description of changes"
git push
```

### Deployment
```bash
# Option 1: Manual upload
# Upload theme/blocksy-child/ to wp-content/themes/
# Upload plugins/custom-functionality/ to wp-content/plugins/

# Option 2: Git deployment (if server supports)
# SSH to server and git pull

# Option 3: WP-CLI (if available)
wp theme install theme/blocksy-child.zip --activate
wp plugin install plugins/custom-functionality.zip --activate
```

### Content Sync
```bash
# Export content structure
wp export --dir=exports/ --post_type=post,page

# Import on new site
wp import exports/*.xml --authors=create
```

## AI Engine MCP Integration

### MCP Config for Claude Desktop
```json
{
  "mcpServers": {
    "wordpress-sitename": {
      "command": "npx",
      "args": ["-y", "@anthropic/wordpress-mcp"],
      "env": {
        "WORDPRESS_URL": "https://sitename.com",
        "WORDPRESS_TOKEN": "your-ai-engine-token"
      }
    }
  }
}
```

### AI Engine REST API Endpoints
```
GET  /wp-json/mwai/v1/posts      # Get posts
POST /wp-json/mwai/v1/posts      # Create post
GET  /wp-json/mwai/v1/pages      # Get pages
POST /wp-json/mwai/v1/pages      # Create page
POST /wp-json/mwai/v1/chat       # Chat completion
```

### Testing MCP Connection
```bash
curl -X GET "https://sitename.com/wp-json/mwai/v1/posts" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Troubleshooting

### Common Issues

**Child theme not appearing:**
- Check style.css header format
- Ensure `Template: blocksy` matches parent exactly
- Verify parent theme is installed

**CSS not loading:**
- Check enqueue priority (use 20+)
- Verify file paths are correct
- Clear LiteSpeed cache

**Block patterns not showing:**
- Verify pattern file has correct header
- Check category registration
- Clear all caches

**MCP connection failing:**
- Verify AI Engine REST API is enabled
- Check token permissions
- Ensure CORS is configured

### Debug Mode
```php
// Add to wp-config.php for debugging
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', false);
define('SCRIPT_DEBUG', true);
```

### Cache Clearing
```bash
# Clear LiteSpeed cache via WP-CLI
wp litespeed-purge all

# Clear all caches
wp cache flush
```

## Best Practices

### Version Control
- Commit frequently with descriptive messages
- Use branches for major features
- Tag releases (v1.0.0, v1.1.0)
- Never commit sensitive data

### Documentation
- Update README.md with every change
- Document all custom hooks
- Keep brand guide current
- Maintain changelog

### Performance
- Minimize custom CSS/JS
- Use native WordPress functions
- Leverage LiteSpeed features
- Test Core Web Vitals regularly

### Security
- Never hardcode credentials
- Use environment variables
- Keep plugins updated
- Regular security audits
