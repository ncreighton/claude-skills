# BUILD-GUIDE: {{SITE_NAME}}

## Complete Build Sequence for Claude Code

**Generated:** {{DATE}}  
**DNA Version:** {{DNA_VERSION}}  
**Site URL:** {{SITE_URL}}  
**Status:** {{BUILD_STATUS}}

---

## How to Use This Guide

1. **Open Claude Code** with this project folder
2. **Copy each prompt** exactly as written
3. **Wait for completion** before moving to next prompt
4. **Run checkpoint** after each phase
5. **Never skip steps** - order matters

Each prompt is numbered: `P[Phase].[Step]`

---

## Phase 0: Verification

### P0.1 - Verify Connection
```
Read CLAUDE.md and confirm you understand the design system for {{SITE_NAME}}.
List the primary colors, fonts, and voice guidelines.
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
Create a Blocksy child theme for {{SITE_NAME}}.
The child theme should be named "{{SITE_SLUG}}-child".
Include:
- style.css with theme header
- functions.php with parent style enqueue
- Empty customizations folder structure
```

### P1.3 - Activate Child Theme
```
Activate the {{SITE_SLUG}}-child theme.
Verify the parent Blocksy theme styles are loading correctly.
```

### P1.4 - Install Core Plugins
```
Install and activate these plugins in order:
1. Wordfence Security
2. Limit Login Attempts Reloaded
3. LiteSpeed Cache
4. RankMath SEO
5. WPCode Pro (if license available) or WPCode Lite
6. Redirection
7. UpdraftPlus
8. Complianz GDPR

Do NOT configure yet - just install and activate.
Report which plugins were successfully installed.
```

### P1.5 - Install Site-Specific Plugins
```
Install and activate these site-specific plugins for {{SITE_NAME}}:
{{SITE_SPECIFIC_PLUGINS}}

Report installation status for each.
```

### P1.6 - Remove Default Content
```
Delete all default WordPress content:
- Sample Page
- Hello World post
- Sample comments
- Any placeholder content

Confirm site is clean.
```

### ✓ Phase 1 Checkpoint
```
Run Phase 1 checkpoint:
- Confirm child theme is active
- List all installed plugins
- Confirm no default content exists
- Check for any PHP errors in debug log
```

---

## Phase 2: Design System Implementation

### P2.1 - Implement CSS Variables
```
Add these CSS custom properties to the child theme.
Create file: /wp-content/themes/{{SITE_SLUG}}-child/assets/css/tokens.css

{{CSS_TOKENS}}

Then enqueue this file in functions.php.
```

### P2.2 - Configure Blocksy Colors
```
Using the WordPress Customizer (or direct database if MCP allows):
Set Blocksy color palette:

Global Colors:
- Color 1 (Primary): {{COLOR_PRIMARY}}
- Color 2 (Secondary): {{COLOR_SECONDARY}}
- Color 3 (Text): {{COLOR_TEXT_PRIMARY}}
- Color 4 (Text Secondary): {{COLOR_TEXT_SECONDARY}}
- Color 5 (Background): {{COLOR_BG_PRIMARY}}
- Color 6 (Background Secondary): {{COLOR_BG_SECONDARY}}
- Color 7 (Accent): {{COLOR_ACCENT}}
- Color 8 (Border): {{COLOR_BORDER}}
```

### P2.3 - Configure Typography
```
Configure Blocksy typography settings:

Body Font:
- Family: {{FONT_BODY}}
- Size: {{TYPE_BASE}}
- Line Height: {{LINE_HEIGHT_BODY}}
- Weight: {{FONT_BODY_WEIGHT}}

Heading Font (H1-H6):
- Family: {{FONT_HEADING}}
- Weight: {{FONT_HEADING_WEIGHT}}
- Line Height: {{LINE_HEIGHT_HEADING}}
- Letter Spacing: {{LETTER_SPACING_HEADING}}

Font Sizes:
- H1: {{TYPE_4XL}}
- H2: {{TYPE_3XL}}
- H3: {{TYPE_2XL}}
- H4: {{TYPE_XL}}
- H5: {{TYPE_LG}}
- H6: {{TYPE_BASE}}
```

### P2.4 - Load Custom Fonts
```
Add Google Fonts to the child theme.
Create a function to properly enqueue:

{{GOOGLE_FONTS_URL}}

Ensure fonts load with display=swap for performance.
Verify fonts appear in browser inspector.
```

### P2.5 - Configure Spacing
```
Set Blocksy container and spacing settings:

Container:
- Max Width: {{CONTAINER_MAX_WIDTH}}
- Content Max Width: {{CONTENT_MAX_WIDTH}}

Spacing:
- Vertical Sections: {{SECTION_GAP}}
- Element Spacing: Use the 8px grid system

Add spacing utility classes to tokens.css if needed.
```

### P2.6 - Site Background
```
Configure the site background:
{{BACKGROUND_CONFIG}}

This should match the DNA visual philosophy:
- Mode: {{COLOR_MODE}}
- Feel: {{VISUAL_FEEL}}
```

### P2.7 - Link Styles
```
Configure link styles:
- Default: {{COLOR_PRIMARY}}
- Hover: {{LINK_HOVER_COLOR}}
- Visited: {{LINK_VISITED_COLOR}}
- Underline: {{LINK_UNDERLINE_STYLE}}
- Transition: {{TRANSITION_NORMAL}}
```

### P2.8 - Button Styles
```
Create custom button styles matching the DNA:

Primary Button:
- Background: {{BUTTON_PRIMARY_BG}}
- Text: {{BUTTON_PRIMARY_TEXT}}
- Border Radius: {{RADIUS_MD}}
- Padding: {{BUTTON_PADDING}}
- Hover: {{BUTTON_PRIMARY_HOVER}}
- Transition: {{TRANSITION_NORMAL}}

Secondary Button:
- Background: {{BUTTON_SECONDARY_BG}}
- Text: {{BUTTON_SECONDARY_TEXT}}
- Border: {{BUTTON_SECONDARY_BORDER}}
- Hover: {{BUTTON_SECONDARY_HOVER}}

Add these to tokens.css with .btn-primary and .btn-secondary classes.
```

### P2.9 - Form Styles
```
Configure form element styles:
- Input Background: {{INPUT_BG}}
- Input Border: {{INPUT_BORDER}}
- Input Focus: {{INPUT_FOCUS}}
- Input Border Radius: {{RADIUS_SM}}
- Input Padding: {{INPUT_PADDING}}
- Placeholder Color: {{INPUT_PLACEHOLDER}}
```

### ✓ Phase 2 Checkpoint
```
Run Phase 2 checkpoint:
1. Open the site in browser
2. Inspect and verify CSS variables are loading
3. Check font-family on body and headings
4. Verify colors match DNA specification
5. Test a link hover state
6. Check background is correct
7. Screenshot the current state for reference
```

---

## Phase 3: Global Elements

### P3.1 - Header Structure
```
Configure the Blocksy header using Header Builder:

{{HEADER_CONFIG}}

Structure:
- Desktop: {{HEADER_DESKTOP_LAYOUT}}
- Mobile: {{HEADER_MOBILE_LAYOUT}}
- Sticky: {{HEADER_STICKY}}

Remember: Navigation should feel like "{{NAV_PHILOSOPHY}}"
```

### P3.2 - Logo Implementation
```
Add the site logo:
- Upload logo file to Media Library
- Set in Customizer → Header → Logo
- Configure sizes:
  - Desktop: {{LOGO_DESKTOP_SIZE}}
  - Mobile: {{LOGO_MOBILE_SIZE}}
- Ensure retina version if available
- Add alt text: "{{SITE_NAME}} Logo"
```

### P3.3 - Primary Navigation
```
Create the primary navigation menu:

Menu Name: Primary Menu
Location: Header - Main Menu

Items (in order):
{{PRIMARY_NAV_ITEMS}}

Settings:
- Max items visible: {{NAV_MAX_ITEMS}}
- Dropdown behavior: {{NAV_DROPDOWN_BEHAVIOR}}
- Style dropdowns to match DNA
```

### P3.4 - Mobile Navigation
```
Configure mobile navigation:
{{MOBILE_NAV_CONFIG}}

Style:
- Type: {{MOBILE_NAV_TYPE}}
- Background: {{MOBILE_NAV_BG}}
- Text Color: {{MOBILE_NAV_TEXT}}
- Animation: {{MOBILE_NAV_ANIMATION}}
```

### P3.5 - Search Configuration
```
Configure site search:
- Style: {{SEARCH_STYLE}}
- Placeholder text: "{{SEARCH_PLACEHOLDER}}"
- Results page template: To be created in Phase 5
```

### P3.6 - Footer Structure
```
Configure the Blocksy footer using Footer Builder:

{{FOOTER_CONFIG}}

Structure:
- Rows: {{FOOTER_ROWS}}
- Columns: {{FOOTER_COLUMNS}}
- Background: {{FOOTER_BG}}
- Text: {{FOOTER_TEXT}}

Content:
{{FOOTER_CONTENT}}
```

### P3.7 - Footer Widgets
```
Add footer widgets:
{{FOOTER_WIDGETS}}

Style to match DNA - ensure consistent spacing and typography.
```

### P3.8 - Breadcrumbs
```
Configure breadcrumbs:
- Enable: {{BREADCRUMBS_ENABLED}}
- Style: {{BREADCRUMBS_STYLE}}
- Separator: {{BREADCRUMBS_SEPARATOR}}
- Position: {{BREADCRUMBS_POSITION}}

Use RankMath breadcrumbs for SEO benefits.
```

### ✓ Phase 3 Checkpoint
```
Run Phase 3 checkpoint:
1. Test header on desktop - logo, nav, search visible
2. Test header on mobile - hamburger menu works
3. Click through all nav items
4. Verify footer displays correctly
5. Check breadcrumbs appear on a test page
6. Test sticky header behavior
7. Verify all transitions are smooth ({{TRANSITION_NORMAL}})
```

---

## Phase 4: Homepage

### P4.1 - Create Homepage
```
Create a new page titled "Home" (or "{{HOMEPAGE_TITLE}}").
Set as static front page in Settings → Reading.
Use Gutenberg blocks for layout.
```

### P4.2 - Hero Section
```
Create the homepage hero section:

{{HERO_SPECIFICATION}}

Requirements from DNA:
- Type: {{HERO_TYPE}}
- Height: {{HERO_HEIGHT}}
- Content Placement: {{HERO_CONTENT_PLACEMENT}}
- Animation: {{HERO_ANIMATION}}
- CTA: "{{HERO_CTA_TEXT}}" - styled as invitation, not command

Visual:
- Background: {{HERO_BACKGROUND}}
- Overlay: {{HERO_OVERLAY}}
- Text Alignment: {{HERO_TEXT_ALIGN}}

IMPORTANT: {{HERO_CRITICAL_NOTES}}
```

### P4.3 - Signature Elements
```
Implement the signature elements for {{SITE_NAME}}:

{{SIGNATURE_ELEMENTS}}

Placement: {{SIGNATURE_PLACEMENT}}
Frequency: {{SIGNATURE_FREQUENCY}}

Remember: "These elements are special because they're rare. Overuse makes them ordinary."
```

### P4.4 - Homepage Section 1
```
Create homepage section 1:

{{HOMEPAGE_SECTION_1}}

Purpose: {{SECTION_1_PURPOSE}}
Layout: {{SECTION_1_LAYOUT}}
Content: {{SECTION_1_CONTENT}}
```

### P4.5 - Homepage Section 2
```
Create homepage section 2:

{{HOMEPAGE_SECTION_2}}

Purpose: {{SECTION_2_PURPOSE}}
Layout: {{SECTION_2_LAYOUT}}
Content: {{SECTION_2_CONTENT}}
```

### P4.6 - Homepage Section 3
```
Create homepage section 3:

{{HOMEPAGE_SECTION_3}}

Purpose: {{SECTION_3_PURPOSE}}
Layout: {{SECTION_3_LAYOUT}}
Content: {{SECTION_3_CONTENT}}
```

### P4.7 - Newsletter/CTA Section
```
Create the newsletter or primary CTA section:

{{NEWSLETTER_SECTION}}

CTA Voice: {{CTA_VOICE}}
Button Text: "{{NEWSLETTER_CTA_TEXT}}"
Style: Invitation, not demand
```

### P4.8 - Homepage Final Polish
```
Review and polish the homepage:

1. Check spacing between all sections ({{SECTION_GAP}})
2. Verify content-to-whitespace ratio ({{DENSITY_RATIO}})
3. Test all interactive elements
4. Check mobile responsiveness
5. Verify load performance
6. Add any final decorative elements per DNA
```

### ✓ Phase 4 Checkpoint
```
Run Phase 4 checkpoint:
1. Load homepage - does atmosphere match DNA?
2. Hero creates the right emotional response?
3. All sections visible and properly spaced?
4. CTAs styled correctly (invitation, not command)?
5. Mobile layout works?
6. No console errors?
7. Would you screenshot this for inspiration? If no, iterate.

Run the DNA tests:
- Screenshot test: Would a designer save this?
- Swap test: Could this work on a generic site? (Should fail)
- Memory test: What will visitors remember?
```
