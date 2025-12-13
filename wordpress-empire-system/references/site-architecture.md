# Site Architecture Reference

Complete guide to WordPress site structure, category organization, navigation patterns, and information architecture for SEO dominance and user experience excellence.

## Architecture Philosophy

**"Structure enables scale."** Every architectural decision should:
1. Make content discoverable by users AND search engines
2. Distribute link equity intelligently
3. Scale without reorganization
4. Support autonomous content creation
5. Create topical authority clusters

## Category Architecture

### The 5-7 Rule
Every site should have **5-7 parent categories** maximum. This:
- Keeps navigation manageable
- Forces topical focus
- Creates clear content clusters
- Improves SEO authority

### Category Structure Template
```
SITE
├── Category 1 (Parent)
│   ├── Subcategory 1.1
│   ├── Subcategory 1.2
│   └── Subcategory 1.3
├── Category 2 (Parent)
│   ├── Subcategory 2.1
│   └── Subcategory 2.2
├── Category 3 (Parent)
│   └── (May have no subcategories)
├── Category 4 (Parent)
│   ├── Subcategory 4.1
│   ├── Subcategory 4.2
│   └── Subcategory 4.3
└── Category 5-7 (Parent)
    └── Subcategories as needed
```

### Category Naming Rules
- **SEO-friendly**: Include target keywords
- **User-friendly**: Clear and intuitive
- **Consistent**: Parallel structure across categories
- **Scalable**: Room for growth without renaming

### Example: WitchcraftForBeginners.com
```
WITCHCRAFT FOR BEGINNERS
├── Getting Started (for absolute beginners)
│   ├── What is Witchcraft
│   ├── First Steps
│   └── Essential Tools
├── Spellwork (practical magic)
│   ├── Protection Spells
│   ├── Love & Relationships
│   ├── Money & Abundance
│   └── Healing Spells
├── Divination (seeing & knowing)
│   ├── Tarot
│   ├── Pendulums
│   └── Scrying
├── Rituals & Sabbats (celebrations)
│   ├── Wheel of the Year
│   ├── Moon Rituals
│   └── Daily Practices
├── Herbalism & Crystals (natural tools)
│   ├── Herbs
│   ├── Crystals
│   └── Essential Oils
├── Deities & Spirits (spiritual relationships)
│   ├── Working with Deities
│   └── Ancestors & Spirits
└── Ethics & Growth (philosophical)
    ├── Magical Ethics
    └── Advanced Practice
```

### Example: SmartHomeWizards.com
```
SMART HOME WIZARDS
├── Smart Home Basics
│   ├── Getting Started
│   ├── Choosing an Ecosystem
│   └── Smart Home Planning
├── Voice Assistants (hubs)
│   ├── Alexa
│   ├── Google Assistant
│   └── Siri & HomeKit
├── Smart Lighting
│   ├── Smart Bulbs
│   ├── Smart Switches
│   └── Lighting Scenes
├── Security & Cameras
│   ├── Smart Cameras
│   ├── Video Doorbells
│   └── Smart Locks
├── Climate Control
│   ├── Smart Thermostats
│   ├── Smart Fans
│   └── Air Quality
├── Entertainment
│   ├── Smart TVs
│   ├── Streaming Devices
│   └── Smart Speakers
└── Automation
    ├── Routines & Scenes
    ├── Advanced Automations
    └── Troubleshooting
```

## Page Hierarchy

### Essential Pages
Every site needs these pages (NOT in categories):

| Page | URL | Purpose |
|------|-----|---------|
| Homepage | / | Convert, establish authority |
| About | /about/ | Build trust, tell story |
| Contact | /contact/ | Support, business inquiries |
| Privacy Policy | /privacy-policy/ | Legal requirement |
| Terms | /terms/ | Legal requirement |
| Start Here | /start-here/ | Guide new visitors |
| Resources | /resources/ | Tools, recommendations |

### Content Page Types
```
PAGE TYPES
├── Pillar Content (Cornerstone)
│   ├── Ultimate guides (3000+ words)
│   ├── Comprehensive how-tos
│   └── Resource hubs
├── Cluster Content (Supporting)
│   ├── Specific topics (1500-2500 words)
│   ├── How-to articles
│   └── List posts
├── News/Updates
│   ├── Industry news
│   ├── Product announcements
│   └── Site updates
└── Landing Pages
    ├── Lead magnets
    ├── Product/service pages
    └── Campaign pages
```

## Internal Linking Architecture

### Link Equity Flow
```
                    HOMEPAGE
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     CATEGORY 1   CATEGORY 2   CATEGORY 3
          │            │            │
    ┌─────┼─────┐    ┌─┴─┐     ┌────┼────┐
    ▼     ▼     ▼    ▼   ▼     ▼    ▼    ▼
  PILLAR POSTS    CLUSTER CONTENT
    │     │          │     │
    └──►──┼──◄──────┘     │
          │               │
     Cross-linking for topical authority
```

### Linking Rules

**From Homepage**:
- Link to ALL parent categories
- Link to 3-5 most important pillar posts
- Featured/recent content section

**From Category Pages**:
- Link to subcategories
- Link to pillar content in category
- Display recent posts in category

**From Posts**:
- Link to parent category
- Link to related posts (same category)
- Link to pillar content (contextually)
- Cross-link between clusters (sparingly)

### Contextual Linking
```
LINKING DENSITY:
├── Introduction (1-2 links)
├── Body Content
│   ├── Link every 200-300 words
│   ├── Use descriptive anchor text
│   └── Link to related content
├── Conclusion (1-2 links)
└── Related Posts Section (3-5 links)
```

### Anchor Text Strategy
- **Branded**: "SmartHomeWizards guide" (for homepage)
- **Exact Match**: "smart thermostat reviews" (use sparingly)
- **Partial Match**: "our guide to smart thermostats"
- **Generic**: "read more", "learn more" (avoid overuse)
- **Natural**: "we've written about this before"

## Navigation Structure

### Primary Navigation
```
HEADER NAVIGATION
├── Logo (links to homepage)
├── Main Menu (5-7 items max)
│   ├── Category 1 (dropdown optional)
│   ├── Category 2
│   ├── Category 3
│   ├── Resources
│   └── About
├── Search Icon
└── CTA Button ("Subscribe", "Start Here")
```

### Mega Menu Structure
For sites with complex hierarchies:
```
┌─────────────────────────────────────────────────────────┐
│  CATEGORY NAME                                          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ SUBCATEGORY  │  │ SUBCATEGORY  │  │ FEATURED     │  │
│  │ • Link 1     │  │ • Link 1     │  │ [Image]      │  │
│  │ • Link 2     │  │ • Link 2     │  │ Title        │  │
│  │ • Link 3     │  │ • Link 3     │  │ [Read →]     │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Footer Navigation
```
FOOTER
├── Column 1: About/Company
│   ├── About
│   ├── Contact
│   ├── Write for Us
│   └── Advertise
├── Column 2: Categories
│   ├── Category 1
│   ├── Category 2
│   └── Category 3
├── Column 3: Resources
│   ├── Start Here
│   ├── Tools
│   └── Newsletter
├── Column 4: Legal
│   ├── Privacy Policy
│   ├── Terms
│   └── Affiliate Disclosure
└── Bottom Bar
    ├── Copyright
    └── Social Icons
```

### Mobile Navigation
- Hamburger menu (right side)
- Full-screen overlay OR slide-in drawer
- Accordion for subcategories
- Search prominently placed
- CTA button visible

### Breadcrumbs
Always include breadcrumbs:
```
Home > Category > Subcategory > Post Title
```

Schema markup:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://site.com/"},
    {"@type": "ListItem", "position": 2, "name": "Category", "item": "https://site.com/category/"},
    {"@type": "ListItem", "position": 3, "name": "Post Title", "item": "https://site.com/category/post/"}
  ]
}
```

## Template Structure

### Homepage Template
```
HOMEPAGE STRUCTURE
├── Hero Section
│   ├── Headline (value prop)
│   ├── Subhead (clarify benefit)
│   ├── Primary CTA
│   └── Secondary CTA (optional)
├── Trust Signals
│   ├── Logos/mentions
│   ├── Numbers (subscribers, posts, etc.)
│   └── Star rating (if applicable)
├── Category Showcase
│   ├── Featured category 1
│   ├── Featured category 2
│   └── Featured category 3
├── Featured Content
│   ├── Pillar post 1
│   ├── Pillar post 2
│   └── Pillar post 3
├── Recent Posts
│   └── Latest 3-6 posts
├── Lead Capture
│   ├── Value proposition
│   └── Email signup form
├── About Section
│   ├── Brief story
│   └── Author introduction
├── Testimonials/Social Proof
│   └── Reader feedback
└── Final CTA
    └── Primary conversion goal
```

### Category Archive Template
```
CATEGORY ARCHIVE
├── Category Hero
│   ├── Category name
│   ├── Description
│   └── Subcategory links
├── Featured Post (if pillar exists)
│   └── Large card with pillar content
├── Subcategory Sections (optional)
│   ├── Subcategory 1 posts
│   ├── Subcategory 2 posts
│   └── etc.
├── All Posts Grid
│   └── Paginated post cards
├── Sidebar (optional)
│   ├── Search
│   ├── Related categories
│   ├── Popular posts
│   └── Newsletter signup
└── Category CTA
    └── Relevant lead magnet
```

### Single Post Template
```
SINGLE POST
├── Post Header
│   ├── Category badge
│   ├── Title (H1)
│   ├── Meta (author, date, read time)
│   └── Share buttons
├── Featured Image
│   └── Full-width hero image
├── Table of Contents (for long posts)
│   └── Jump links to H2s
├── Post Content
│   ├── Introduction
│   ├── Body sections (H2, H3)
│   └── Conclusion
├── In-Content CTA
│   └── Newsletter or lead magnet
├── Author Box
│   ├── Photo
│   ├── Bio
│   └── Social links
├── Related Posts
│   └── 3-6 related articles
├── Comments (if enabled)
│   └── Comment form
└── Post Footer
    ├── Tags
    ├── Share buttons
    └── Navigation (prev/next)
```

## URL Structure

### URL Rules
- Lowercase only
- Hyphens (not underscores)
- No stop words unless necessary
- Include target keyword
- Keep short (under 60 chars ideal)

### URL Patterns
| Content Type | Pattern | Example |
|--------------|---------|---------|
| Post | /category/post-title/ | /smart-lighting/best-smart-bulbs/ |
| Category | /category/ | /smart-lighting/ |
| Subcategory | /category/subcategory/ | /smart-lighting/smart-switches/ |
| Page | /page-name/ | /about/ |
| Tag | /tag/tag-name/ | /tag/alexa/ |
| Author | /author/name/ | /author/nick/ |

### Permalink Settings
WordPress Settings → Permalinks → Custom Structure:
```
/%category%/%postname%/
```

Or for simpler structure:
```
/%postname%/
```

## Taxonomy Strategy

### Categories vs Tags

**Categories** (Hierarchical):
- Main content organization
- 5-7 parent categories
- Appear in URLs
- Have dedicated archive pages
- SEO-focused

**Tags** (Flat):
- Cross-cutting topics
- Ecosystem/brand names (Alexa, Google, etc.)
- Product types (smart bulbs, thermostats)
- Use cases (automation, security)
- NOT in URLs

### Tag Rules
- Use sparingly (5-10 tags per post max)
- Consistent naming
- Combine synonyms
- Index popular tags only
- noindex sparse tag pages

## Scaling Considerations

### When to Add Categories
Only add new parent categories when:
1. You have 10+ posts for the topic
2. It doesn't fit existing categories
3. It represents a major pillar of your site
4. You can commit to ongoing content

### When to Add Subcategories
Add subcategories when:
1. A parent category has 20+ posts
2. Clear subtopics emerge
3. Users need easier navigation
4. SEO opportunity exists

### Migration Strategy
When restructuring:
1. Map old URLs to new URLs
2. Set up 301 redirects for ALL changed URLs
3. Update internal links
4. Submit updated sitemap
5. Monitor 404s in Search Console

## Architecture Checklist

Before launching or major changes:

### Structure Check
- [ ] 5-7 parent categories maximum
- [ ] Clear hierarchy (parent → sub → post)
- [ ] Logical URL structure
- [ ] Breadcrumbs implemented
- [ ] All orphan pages linked

### Navigation Check
- [ ] Main menu reflects primary categories
- [ ] Footer includes all important links
- [ ] Mobile navigation works smoothly
- [ ] Search functions correctly
- [ ] CTA visible in header

### Linking Check
- [ ] Homepage links to all categories
- [ ] Categories link to pillar content
- [ ] Posts link to related content
- [ ] No broken internal links
- [ ] Anchor text is descriptive

### Technical Check
- [ ] XML sitemap submitted
- [ ] robots.txt properly configured
- [ ] Canonical URLs set
- [ ] Pagination handled correctly
- [ ] Tag archives noindexed (if sparse)
