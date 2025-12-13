# BUILD-GUIDE: WitchcraftForBeginners

## Complete Build Sequence for Claude Code

**Generated:** 2025-12-13  
**DNA Version:** 2.0.0  
**Site URL:** https://witchcraftforbeginners.com  
**Status:** FLAGSHIP SITE - New Build/Redesign

---

## How to Use This Guide

1. **Open Claude Code** with this project folder
2. **Read CLAUDE.md first** - it has all design tokens
3. **Copy each prompt** exactly as written
4. **Wait for completion** before moving to next prompt
5. **Run checkpoint** after each phase
6. **Never skip steps** - order matters

Each prompt is numbered: `P[Phase].[Step]`

---

## Phase 0: Verification

### P0.1 - Verify Connection
```
Read CLAUDE.md and confirm you understand the design system for WitchcraftForBeginners.

Confirm you see:
- Primary color: #4A1C6F (Deep Amethyst)
- Secondary color: #D4AF37 (Candle Gold)
- Background: #1A1A2E (Night Sky)
- Font heading: Cinzel
- Font body: Lora
- Voice: Wise but warm, patient teacher

Test the WordPress MCP connection by listing current plugins.
```

**Expected:** Claude confirms design understanding + plugin list appears

---

## Phase 1: Foundation

### P1.1 - Theme Check
```
Check if Blocksy theme is installed and active.
If not, guide me through installing Blocksy from the theme repository.
```

### P1.2 - Child Theme Creation
```
Create a Blocksy child theme for WitchcraftForBeginners.
The child theme should be named "witchcraft-for-beginners-child".
Include:
- style.css with theme header referencing parent
- functions.php that enqueues parent styles
- Empty /assets/css/ folder for custom styles
- Empty /assets/js/ folder for custom scripts
```

### P1.3 - Activate Child Theme
```
Activate the witchcraft-for-beginners-child theme.
Verify the parent Blocksy theme styles are loading correctly.
Check browser console for any errors.
```

### P1.4 - Install Core Plugins
```
Install and activate these plugins in order:
1. Wordfence Security
2. Limit Login Attempts Reloaded
3. LiteSpeed Cache
4. RankMath SEO
5. WPCode Pro (or WPCode Lite if no license)
6. Redirection
7. UpdraftPlus
8. Complianz GDPR

Do NOT configure yet - just install and activate.
Report which plugins were successfully installed.
```

### P1.5 - Install Site-Specific Plugins
```
Install and activate these site-specific plugins for WitchcraftForBeginners:

1. WP Recipe Maker - for spell and ritual "recipes" with structured data
2. WPForms Lite - for contact form
3. Grow Social Pro (or Grow by Mediavine) - for social sharing

Report installation status for each.
```

### P1.6 - Remove Default Content
```
Delete all default WordPress content:
- "Sample Page" page
- "Hello World" post
- All sample comments
- Any placeholder content

Confirm site is clean and ready for custom content.
```

### ✓ Phase 1 Checkpoint
```
Run Phase 1 checkpoint:
- Confirm "witchcraft-for-beginners-child" theme is active
- List all installed plugins (should be 11 total)
- Confirm no default content exists
- Check /wp-content/debug.log for any PHP errors
- Report status of each item
```

---

## Phase 2: Design System Implementation

### P2.1 - Implement CSS Variables
```
Create the CSS tokens file for WitchcraftForBeginners.
Path: /wp-content/themes/witchcraft-for-beginners-child/assets/css/tokens.css

Contents:
:root {
  /* Primary Palette */
  --color-primary: #4A1C6F;
  --color-secondary: #D4AF37;
  --color-accent: #8B4513;
  
  /* Backgrounds (Dark First) */
  --color-bg-primary: #1A1A2E;
  --color-bg-secondary: #16213E;
  --color-bg-tertiary: #0F0F1A;
  
  /* Text */
  --color-text-primary: #E8E4D9;
  --color-text-secondary: #B8B4A9;
  --color-text-muted: #6B6860;
  
  /* Semantic */
  --color-success: #4A7C59;
  --color-warning: #C9A227;
  --color-error: #8B3A3A;
  --color-info: #4A6F8B;
  
  /* Typography */
  --font-heading: 'Cinzel', Garamond, 'Times New Roman', serif;
  --font-body: 'Lora', Georgia, 'Times New Roman', serif;
  --font-accent: 'Cormorant Garamond', Georgia, serif;
  
  /* Font Sizes (1.333 scale) */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.333rem;
  --text-xl: 1.777rem;
  --text-2xl: 2.369rem;
  --text-3xl: 3.157rem;
  --text-4xl: 4.209rem;
  
  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 1rem;
  --space-4: 1.5rem;
  --space-5: 2rem;
  --space-6: 3rem;
  --space-7: 4rem;
  --space-8: 6rem;
  
  /* Effects */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --shadow-glow: 0 0 40px rgba(212, 175, 55, 0.15);
  --transition-normal: 0.5s ease-out;
  --transition-slow: 0.8s ease-out;
  --transition-reveal: 1.2s ease-out;
}

Then add this to functions.php to enqueue:
function witchcraft_enqueue_tokens() {
    wp_enqueue_style('witchcraft-tokens', get_stylesheet_directory_uri() . '/assets/css/tokens.css');
}
add_action('wp_enqueue_scripts', 'witchcraft_enqueue_tokens');
```

### P2.2 - Configure Blocksy Colors
```
Configure Blocksy Global Colors in Customizer:

Color 1 (Primary): #4A1C6F
Color 2 (Secondary): #D4AF37
Color 3 (Text Primary): #E8E4D9
Color 4 (Text Secondary): #B8B4A9
Color 5 (Background Primary): #1A1A2E
Color 6 (Background Secondary): #16213E
Color 7 (Accent): #8B4513
Color 8 (Border): #2A2A3E

Set Site Background to #1A1A2E (Night Sky).
```

### P2.3 - Configure Typography
```
Configure Blocksy typography settings in Customizer:

Body Font:
- Family: Lora
- Size: 18px (1rem base)
- Line Height: 1.7
- Weight: 400

Headings:
- Family: Cinzel
- H1: 4.209rem, weight 600
- H2: 3.157rem, weight 600
- H3: 2.369rem, weight 500
- H4: 1.777rem, weight 500
- H5: 1.333rem, weight 500
- H6: 1rem, weight 600
- Line Height: 1.2
- Letter Spacing: 0.02em
```

### P2.4 - Load Custom Fonts
```
Add Google Fonts to the child theme. Add to functions.php:

function witchcraft_enqueue_fonts() {
    wp_enqueue_style(
        'witchcraft-fonts',
        'https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Dancing+Script:wght@400;700&display=swap',
        array(),
        null
    );
}
add_action('wp_enqueue_scripts', 'witchcraft_enqueue_fonts');

Verify fonts appear correctly:
- Check Network tab shows fonts loading
- Check Inspector shows Cinzel on headings
- Check Lora on body text
```

### P2.5 - Button & Link Styles
```
Add custom button and link styles. Create /assets/css/components.css:

/* Links */
a {
    color: var(--color-secondary);
    text-decoration: none;
    transition: var(--transition-normal);
}
a:hover {
    color: var(--color-primary);
}

/* Primary Button - The Invitation Style */
.btn-primary,
.wp-block-button__link {
    background: var(--color-primary);
    color: var(--color-text-primary);
    border: 1px solid var(--color-secondary);
    border-radius: var(--radius-md);
    padding: 0.875rem 2rem;
    font-family: var(--font-heading);
    font-size: var(--text-sm);
    letter-spacing: 0.05em;
    transition: var(--transition-normal);
    text-transform: none;
}
.btn-primary:hover,
.wp-block-button__link:hover {
    background: var(--color-secondary);
    color: var(--color-bg-primary);
    box-shadow: var(--shadow-glow);
}

/* Secondary Button */
.btn-secondary {
    background: transparent;
    color: var(--color-secondary);
    border: 1px solid var(--color-secondary);
    border-radius: var(--radius-md);
    padding: 0.875rem 2rem;
}
.btn-secondary:hover {
    background: rgba(212, 175, 55, 0.1);
}

Enqueue this file in functions.php.
```

### P2.6 - Form Styles
```
Add form styling to components.css:

/* Form Elements */
input[type="text"],
input[type="email"],
input[type="search"],
textarea {
    background: var(--color-bg-secondary);
    border: 1px solid rgba(212, 175, 55, 0.2);
    border-radius: var(--radius-sm);
    color: var(--color-text-primary);
    padding: 0.75rem 1rem;
    font-family: var(--font-body);
    transition: var(--transition-normal);
}
input:focus,
textarea:focus {
    border-color: var(--color-secondary);
    outline: none;
    box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.1);
}
::placeholder {
    color: var(--color-text-muted);
}
```

### ✓ Phase 2 Checkpoint
```
Run Phase 2 checkpoint:
1. Open site in browser, open Inspector
2. Verify CSS variables are loading (check :root)
3. Check font-family on body = Lora
4. Check font-family on h1/h2 = Cinzel
5. Verify background is #1A1A2E
6. Test a link hover state (should transition smoothly)
7. Check a button style
8. Take a screenshot for reference
```

---

## Phase 3: Global Elements

### P3.1 - Header Configuration
```
Configure the Blocksy header using Header Builder:

Desktop Header:
- Row 1: Top bar (optional - can add moon phase here later)
- Row 2: Main header
  - Left: Logo
  - Center: Primary Menu
  - Right: Search icon
- Background: Transparent (for hero overlap) OR #1A1A2E
- Height: 80px
- Sticky: Yes, shrink to 60px on scroll

Mobile Header:
- Logo left
- Hamburger right
- Background: #1A1A2E

Style:
- Text color: #E8E4D9
- Hover: #D4AF37
```

### P3.2 - Logo Implementation
```
For now, create a text-based logo until proper logo is ready:

In Customizer → Header → Logo:
- Type: Site Title & Tagline (or Text Logo)
- Font: Cinzel
- Size: 28px desktop, 22px mobile
- Color: #D4AF37 (Candle Gold)
- Weight: 600

When real logo SVG is ready:
- Upload to Media Library
- Desktop max height: 50px
- Mobile max height: 40px
- Alt text: "WitchcraftForBeginners Logo"
```

### P3.3 - Primary Navigation
```
Create the primary navigation menu:

Go to Appearance → Menus
Menu Name: Primary Menu
Location: Primary (Header)

Items (in this order):
1. Begin Here (link to /begin-here/)
2. Spells & Rituals (category archive)
3. Moon Magic (category archive)
4. Tools & Supplies (category archive)
5. About (link to /about/)

Style notes:
- Max 6 items
- No mega menus - keep mystery
- Dropdowns simple, dark background
- Item naming: Inviting, not clinical

DO NOT add generic items like "Blog" or "Home".
```

### P3.4 - Mobile Navigation
```
Configure mobile navigation:

Type: Full-screen overlay
Background: #0F0F1A (Deep Void)
Animation: Fade in 0.3s

Menu items:
- Color: #E8E4D9
- Hover: #D4AF37
- Font: Cinzel
- Size: 1.5rem
- Spacing: 2rem between items

Close button:
- Position: Top right
- Color: #D4AF37

"Navigation is a moment, not a utility" - it should feel like entering a new chamber.
```

### P3.5 - Footer Configuration
```
Configure Blocksy footer:

Structure:
- Row 1: 4 columns for widgets/links
- Row 2: Copyright bar

Background: #0F0F1A (Deep Void)
Text: #B8B4A9 (Faded Ink)
Links: #D4AF37 hover

Row 1 Content:
- Column 1: About text + social icons
- Column 2: Quick Links (Begin Here, Popular Posts)
- Column 3: Categories
- Column 4: Newsletter signup

Row 2:
- Left: © 2025 WitchcraftForBeginners. Blessed Be.
- Right: Privacy | Terms | Affiliate Disclosure
```

### P3.6 - Breadcrumbs
```
Configure breadcrumbs using RankMath:

Settings → General Settings → Breadcrumbs:
- Enable: Yes
- Separator: »
- Show on: Posts, Pages, Categories

Style in CSS:
.rank-math-breadcrumb {
    font-size: var(--text-sm);
    color: var(--color-text-muted);
    margin-bottom: var(--space-4);
}
.rank-math-breadcrumb a {
    color: var(--color-text-secondary);
}
.rank-math-breadcrumb a:hover {
    color: var(--color-secondary);
}

Position: Above content title on posts and category pages.
```

### ✓ Phase 3 Checkpoint
```
Run Phase 3 checkpoint:
1. Test header on desktop - logo, nav, search visible
2. Click through all 5 nav items - all work?
3. Test mobile hamburger menu - opens full screen?
4. Test sticky header - shrinks on scroll?
5. Check footer - all columns display?
6. Verify social icons work
7. Check breadcrumbs on a test page
8. All transitions smooth (0.5s)?
```
