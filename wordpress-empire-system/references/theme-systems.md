# Theme Systems Reference

Complete guide to Blocksy and Astra theme customization for the WordPress Empire.

## Theme Selection

### When to Use Blocksy (Default)
- Most sites in the empire
- Blog-focused content
- Performance-critical sites
- Sites needing advanced header/footer builders
- Sites requiring Gutenberg/blocks focus

### When to Use Astra
- E-commerce heavy sites
- Sites needing extensive Elementor integration
- Family-Flourish (established)
- Sites with complex WooCommerce needs

## Blocksy Theme Mastery

### Installation
```bash
# Via WP-CLI
wp theme install blocksy --activate
wp plugin install blocksy-companion --activate

# Blocksy Pro (from WorldPressIt)
# Upload blocksy-companion-pro.zip via admin
```

### Blocksy Customizer Deep Dive

#### General Options
```
Customize → General Options
├── Site Identity
│   ├── Logo (Upload SVG preferred)
│   ├── Site Title & Tagline
│   └── Site Icon (512x512 favicon)
├── Layout
│   ├── Container Width: 1200px (content), 1400px (wide)
│   ├── Content/Sidebar: Choose layout
│   └── Vertical Spacing: Comfortable (40px)
├── Colors
│   ├── Color Palette: Define 8 colors
│   │   ├── Color 1: Primary
│   │   ├── Color 2: Primary Hover
│   │   ├── Color 3: Secondary
│   │   ├── Color 4: Secondary Hover
│   │   ├── Color 5: Text Primary
│   │   ├── Color 6: Text Secondary
│   │   ├── Color 7: Accent
│   │   └── Color 8: Accent Hover
│   └── Use CSS variables throughout
├── Typography
│   ├── Base Font: Body font family
│   ├── Headings: Display font family
│   └── Links: Underline style
└── Performance
    ├── Local Fonts: ON (download Google Fonts)
    ├── Lazy Load: ON
    └── Content Width: Match container
```

#### Header Builder (Blocksy Pro)
```
Customize → Header
├── Header Builder
│   ├── Top Row (optional)
│   │   ├── Social Icons
│   │   ├── Contact Info
│   │   └── Top Menu
│   ├── Middle Row (main)
│   │   ├── Logo
│   │   ├── Menu
│   │   ├── Search
│   │   └── Button
│   └── Bottom Row (optional)
│       └── Secondary Menu
├── Global Header
│   ├── Height: 80-100px
│   ├── Background: Transparent or solid
│   └── Shadow: Subtle on scroll
├── Transparent Header
│   ├── Enable: Per-page control
│   ├── Text Color: White/Dark
│   └── Logo: Alternative for dark BG
└── Sticky Header
    ├── Enable: ON
    ├── Behavior: Scroll up to reveal
    └── Height: Shrink to 60-70px
```

#### Footer Builder (Blocksy Pro)
```
Customize → Footer
├── Footer Builder
│   ├── Widget Areas (Top Section)
│   │   ├── 3-4 columns
│   │   ├── About, Categories, Resources, Newsletter
│   │   └── Equal or custom widths
│   ├── Bottom Bar
│   │   ├── Copyright
│   │   ├── Menu
│   │   └── Social Icons
│   └── Reveal Effect: ON
├── Global Footer
│   ├── Background: Dark or brand color
│   ├── Text Color: Light
│   └── Spacing: Generous
└── Footer Widgets
    └── Configure in Appearance → Widgets
```

#### Blog Settings
```
Customize → Blog Posts
├── Archive Layout
│   ├── Layout: Grid or Simple
│   ├── Columns: 2 or 3
│   ├── Card Style: Boxed or Simple
│   └── Featured Image: Ratio 16:9 or 4:3
├── Card Elements
│   ├── Featured Image: Show
│   ├── Title: Show
│   ├── Excerpt: Show (max 20 words)
│   ├── Read More: Show
│   ├── Meta: Author, Date, Category
│   └── Dividers: Subtle
├── Single Post
│   ├── Structure: Title on top or below image
│   ├── Featured Image: Full width or contained
│   ├── Author Box: Enable
│   ├── Related Posts: Enable
│   ├── Share Buttons: Enable
│   └── Post Navigation: Previous/Next
└── Categories
    ├── Hero: Category description
    ├── Layout: Match archive
    └── Sidebar: Optional
```

### Blocksy Pro Hooks

Insert content at specific locations:
```
Blocksy Pro → Hooks
├── Before Header
├── After Header
├── Before Content
├── After Content
├── Before Footer
├── After Footer
├── Before Post Content
├── After Post Content
└── Custom Locations
```

#### Example Hook Usage
```php
// Add notification bar before header
// In Hooks → Before Header:
<div class="notification-bar">
    Free shipping on orders over $50! <a href="/shop">Shop Now</a>
</div>
```

### Blocksy Content Blocks (Pro)

Create reusable sections:
```
Blocksy → Content Blocks
├── Create Block
│   ├── Name: Hero Section
│   ├── Content: Design in Gutenberg
│   └── Display: Choose locations
├── Display Conditions
│   ├── Entire Website
│   ├── Specific Pages
│   ├── Post Types
│   ├── Categories
│   └── Custom rules
└── Position
    ├── Before Header
    ├── After Header
    ├── Replace Header
    └── etc.
```

### Blocksy Custom CSS

Add in Customize → Additional CSS:
```css
/* Brand CSS Variables */
:root {
    --theme-palette-color-1: #4A1C6F;
    --theme-palette-color-2: #6B3FA0;
    --theme-palette-color-3: #C9A962;
    --theme-palette-color-4: #E5D4A1;
    --theme-palette-color-5: #E8E8E8;
    --theme-palette-color-6: #A0A0A0;
    --theme-palette-color-7: #1E3A5F;
    --theme-palette-color-8: #0D0D0D;
    
    /* Custom additions */
    --brand-gradient: linear-gradient(135deg, var(--theme-palette-color-1), var(--theme-palette-color-3));
    --brand-shadow: 0 4px 20px rgba(74, 28, 111, 0.15);
}

/* Custom button styles */
.wp-block-button__link {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.wp-block-button__link:hover {
    transform: translateY(-2px);
    box-shadow: var(--brand-shadow);
}

/* Hero enhancement */
.hero-section {
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--brand-gradient);
    opacity: 0.9;
    z-index: 1;
}
```

## Astra Theme Mastery

### Installation
```bash
# Via WP-CLI
wp theme install astra --activate
wp plugin install astra-sites --activate

# Astra Pro (from WorldPressIt)
# Upload astra-addon-plugin.zip via admin
```

### Astra Customizer Deep Dive

#### Global Settings
```
Customize → Global
├── Typography
│   ├── Body: Font, size, line-height
│   ├── Headings: Font, sizes (H1-H6)
│   └── Content Width: 1200px
├── Colors
│   ├── Base Colors
│   │   ├── Text Color
│   │   ├── Theme Color (Primary)
│   │   ├── Link Color
│   │   └── Link Hover Color
│   └── Background Color
├── Container
│   ├── Width: 1200px
│   ├── Layout: Full Width/Boxed/Padded
│   └── Content Width: 60%
└── Buttons
    ├── Border Radius: 4px-8px
    ├── Padding: 12px 24px
    └── Hover Effects
```

#### Header Builder (Astra Pro)
```
Customize → Header Builder
├── Primary Header
│   ├── Logo
│   ├── Primary Menu
│   ├── Search
│   └── Button
├── Above Header (optional)
│   ├── Contact info
│   └── Social icons
├── Below Header (optional)
│   └── Secondary menu
└── Mobile Header
    ├── Logo
    ├── Toggle Button
    └── Off-Canvas Menu
```

#### Blog Settings
```
Customize → Blog
├── Archive
│   ├── Layout: Grid/List
│   ├── Columns: 2-3
│   ├── Post Structure: Title, Meta, Image
│   └── Pagination: Infinite/Numbers
├── Single Post
│   ├── Featured Image: Above/Below title
│   ├── Post Structure: Title, Meta, Content
│   ├── Author Info: Show
│   ├── Related Posts: Show
│   └── Comments: Show
└── Sidebar
    ├── Default: Right/Left/None
    └── Per-post override
```

### Astra Pro Modules

Enable in Appearance → Astra Options:
```
☑ Colors & Background
☑ Typography
☑ Spacing
☑ Blog Pro
☑ Mobile Header
☑ Header Sections
☑ Nav Menu
☑ Sticky Header
☑ Page Headers
☑ Custom Layouts
☑ Site Layouts
☑ Scroll To Top
☑ WooCommerce (if needed)
```

### Astra Custom Layouts (Pro)

Create custom headers, footers, hooks:
```
Appearance → Astra → Custom Layouts
├── Header
│   ├── Build with Elementor
│   └── Display Rules: All pages
├── Footer
│   ├── Build with Elementor
│   └── Display Rules: All pages
├── 404 Page
│   └── Custom design
├── Hooks
│   ├── After Header
│   ├── Before Content
│   ├── After Content
│   └── etc.
└── Content
    └── Custom templates
```

## Child Theme Setup

### Blocksy Child Theme
```css
/* style.css */
/*
 Theme Name: Site Name Child
 Theme URI: https://sitename.com
 Description: Child theme for Site Name
 Author: Nick
 Author URI: https://sitename.com
 Template: blocksy
 Version: 1.0.0
 Text Domain: sitename-child
*/

/* Import brand variables */
@import url('assets/css/brand-variables.css');
```

```php
<?php
// functions.php

/**
 * Enqueue child theme styles
 */
add_action('wp_enqueue_scripts', function() {
    // Parent theme
    wp_enqueue_style('blocksy-parent', get_template_directory_uri() . '/style.css');
    
    // Child theme
    wp_enqueue_style('child-style', get_stylesheet_uri(), ['blocksy-parent'], '1.0.0');
    
    // Brand variables
    wp_enqueue_style('brand-vars', get_stylesheet_directory_uri() . '/assets/css/brand-variables.css', [], '1.0.0');
    
    // Custom JS
    wp_enqueue_script('child-scripts', get_stylesheet_directory_uri() . '/assets/js/scripts.js', ['jquery'], '1.0.0', true);
}, 20);

/**
 * Add custom image sizes
 */
add_action('after_setup_theme', function() {
    add_image_size('hero', 1920, 1080, true);
    add_image_size('card', 600, 400, true);
    add_image_size('square', 400, 400, true);
});

/**
 * Register custom block patterns
 */
add_action('init', function() {
    register_block_pattern_category('sitename', [
        'label' => __('Site Name', 'sitename-child')
    ]);
});

/**
 * Customize excerpt length
 */
add_filter('excerpt_length', function() {
    return 25;
});

/**
 * Custom excerpt more
 */
add_filter('excerpt_more', function() {
    return '...';
});
```

### Astra Child Theme
```css
/* style.css */
/*
 Theme Name: Site Name Astra Child
 Theme URI: https://sitename.com
 Description: Astra child theme for Site Name
 Author: Nick
 Author URI: https://sitename.com
 Template: astra
 Version: 1.0.0
 Text Domain: sitename-astra-child
*/
```

```php
<?php
// functions.php

add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style('astra-parent', get_template_directory_uri() . '/style.css');
    wp_enqueue_style('child-style', get_stylesheet_uri(), ['astra-parent'], '1.0.0');
    wp_enqueue_style('brand-vars', get_stylesheet_directory_uri() . '/assets/css/brand-variables.css', [], '1.0.0');
}, 15);
```

## Theme Performance Optimization

### Blocksy Performance Settings
```
Customize → General Options → Performance
├── Preload Local Fonts: ON
├── Lazy Load Images: ON (or use LiteSpeed)
├── Disable Emojis: ON
├── Disable Embeds: OFF (YouTube needed)
└── Content Width: 1200px
```

### Astra Performance Settings
```
Appearance → Astra Options → Performance
├── Load Google Fonts Locally: ON
├── Preload Local Fonts: ON
├── Self-Host Google Fonts: ON
└── Font Display: Swap
```

### Additional Performance CSS
```css
/* Optimize font loading */
@font-face {
    font-display: swap;
}

/* Optimize images */
img {
    height: auto;
    max-width: 100%;
}

/* Reduce layout shift */
img, video, iframe {
    aspect-ratio: attr(width) / attr(height);
}
```

## Global Styles (theme.json)

For Blocksy with full site editing capabilities:
```json
{
    "$schema": "https://schemas.wp.org/trunk/theme.json",
    "version": 2,
    "settings": {
        "color": {
            "palette": [
                {"slug": "primary", "color": "#4A1C6F", "name": "Primary"},
                {"slug": "secondary", "color": "#C9A962", "name": "Secondary"},
                {"slug": "accent", "color": "#1E3A5F", "name": "Accent"},
                {"slug": "background", "color": "#0D0D0D", "name": "Background"},
                {"slug": "text", "color": "#E8E8E8", "name": "Text"}
            ]
        },
        "typography": {
            "fontFamilies": [
                {
                    "fontFamily": "\"Cinzel\", serif",
                    "slug": "heading",
                    "name": "Heading"
                },
                {
                    "fontFamily": "\"Lora\", serif",
                    "slug": "body",
                    "name": "Body"
                }
            ],
            "fontSizes": [
                {"slug": "small", "size": "0.875rem", "name": "Small"},
                {"slug": "medium", "size": "1rem", "name": "Medium"},
                {"slug": "large", "size": "1.25rem", "name": "Large"},
                {"slug": "x-large", "size": "1.5rem", "name": "Extra Large"},
                {"slug": "xx-large", "size": "2.25rem", "name": "Huge"}
            ]
        },
        "spacing": {
            "units": ["px", "em", "rem", "%", "vw", "vh"],
            "spacingSizes": [
                {"slug": "10", "size": "0.5rem", "name": "Tiny"},
                {"slug": "20", "size": "1rem", "name": "Small"},
                {"slug": "30", "size": "1.5rem", "name": "Medium"},
                {"slug": "40", "size": "2rem", "name": "Large"},
                {"slug": "50", "size": "3rem", "name": "X-Large"},
                {"slug": "60", "size": "4rem", "name": "XX-Large"}
            ]
        }
    }
}
```

## Theme Checklist

### Before Launch
- [ ] Logo uploaded (SVG preferred)
- [ ] Favicon set (512x512)
- [ ] Colors match brand guide
- [ ] Typography set correctly
- [ ] Header configured
- [ ] Footer configured
- [ ] Blog archive styled
- [ ] Single post styled
- [ ] 404 page designed
- [ ] Mobile menu works
- [ ] Sticky header works
- [ ] Performance settings enabled
- [ ] Child theme activated
- [ ] Custom CSS added
