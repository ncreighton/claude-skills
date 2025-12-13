# SEO Structure Reference

Complete guide to SEO-optimized WordPress structure using RankMath Pro for search dominance.

## SEO Philosophy

**"Write for humans, structure for machines."**

Every SEO decision should:
1. Improve user experience first
2. Make content discoverable
3. Build topical authority
4. Support featured snippets
5. Enable rich results

## RankMath Pro Configuration

### Setup Wizard
Run the setup wizard first:
```
Rank Math → Dashboard → Setup Wizard
├── Your Site Type: Blog/Personal/Business
├── Site Name: Your Site Name
├── Logo: Upload site logo
├── Default Social Image: Upload OG image
├── Search Console: Connect Google
├── Analytics: Connect Google Analytics
└── SEO Tweaks: Apply recommended
```

### General Settings
```
Rank Math → General Settings
├── Links
│   ├── Strip Category Base: ON
│   ├── Redirect Attachments: ON
│   ├── Redirect Attachment URLs to Parent: ON
│   ├── Nofollow External Links: OFF
│   ├── Nofollow Image File Links: OFF
│   ├── Open External Links in New Tab: ON
│   └── Add rel="noreferrer": ON
├── Breadcrumbs
│   ├── Enable Breadcrumbs: ON
│   ├── Separator: » or >
│   ├── Home Label: Home
│   ├── Home Link: ON
│   ├── Prefix: (blank)
│   ├── Archive Format: Archives for %s
│   ├── Search Format: Results for %s
│   └── 404 Label: 404 Error: page not found
├── Webmaster Tools
│   ├── Google Search Console: Verify
│   ├── Bing Webmaster Tools: Verify
│   └── Others: As needed
├── Edit robots.txt: Configure
├── Edit .htaccess: (careful)
└── 404 Monitor: ON
```

### Titles & Meta Settings
```
Rank Math → Titles & Meta
├── Global Meta
│   ├── Separator: – (en-dash) or | (pipe)
│   ├── Capitalize Titles: ON
│   └── Noindex Empty Archives: ON
├── Local SEO
│   ├── Person or Company: Company
│   ├── Company Name: Site Name
│   ├── Logo: Upload
│   └── Social URLs: Add all profiles
├── Social Meta
│   ├── Add SEO Meta Box: ON
│   ├── Default Share Image: Upload
│   ├── Twitter Card Type: Summary Large Image
│   └── Facebook Admin ID: (if needed)
├── Homepage
│   ├── Title: %sitename% %sep% %tagline%
│   ├── Description: Compelling description (155 chars)
│   └── Robots: Index, Follow
├── Authors
│   ├── Author Archives: ON
│   ├── Title: %name% %sep% %sitename%
│   └── Description: Articles by %name%
├── Misc Pages
│   ├── Search Results: noindex
│   └── 404 Pages: noindex
└── Post Types (for each):
    ├── Posts
    │   ├── Title: %title% %sep% %sitename%
    │   ├── Description: %excerpt%
    │   ├── Schema Type: Article
    │   ├── Article Type: BlogPosting
    │   ├── Custom Robots: Index, Follow
    │   └── Add SEO Controls: ON
    ├── Pages
    │   ├── Title: %title% %sep% %sitename%
    │   ├── Description: %excerpt%
    │   ├── Schema Type: WebPage
    │   └── Custom Robots: Index, Follow
    └── Attachments
        └── Redirect to Parent: ON
```

### Taxonomies Settings
```
Rank Math → Titles & Meta → Taxonomies
├── Categories
│   ├── Title: %term% %sep% %sitename%
│   ├── Description: %term_description%
│   └── Robots: Index, Follow
├── Tags
│   ├── Title: %term% %sep% %sitename%
│   └── Robots: noindex (unless significant traffic)
└── Custom Taxonomies
    └── Configure as needed
```

### Sitemap Settings
```
Rank Math → Sitemap Settings
├── General
│   ├── Sitemap: ON
│   ├── Include Images: ON
│   ├── Include Featured Images: ON
│   ├── Ping Search Engines: ON
│   └── Links Per Sitemap: 200
├── Post Types
│   ├── Posts: Include
│   ├── Pages: Include
│   └── Attachments: Exclude
└── Taxonomies
    ├── Categories: Include
    └── Tags: Exclude (unless valuable)
```

### Schema Settings
```
Rank Math → Schema Templates (Pro)
├── Article Schema (Default for Posts)
│   ├── Type: Article
│   ├── Headline: %title%
│   ├── Description: %excerpt%
│   ├── Author: Post Author
│   └── Publisher: Organization
├── HowTo Schema (Tutorial Posts)
│   ├── Use when: Post has steps
│   └── Trigger: Category or manual
├── FAQ Schema
│   ├── Use when: Has Q&A content
│   └── Add via block or shortcode
├── Product Schema (Reviews)
│   ├── Name: Product name
│   ├── Rating: Review score
│   └── Price: If applicable
└── Custom Schemas
    └── Build per content type
```

### Instant Indexing (Pro)
```
Rank Math → Instant Indexing
├── Enable: ON
├── Bing Indexing: ON
├── Google Indexing API: Configure
└── Auto-Submit:
    ├── Posts: ON
    ├── Pages: ON
    └── Products: ON (if WooCommerce)
```

### Analytics Integration
```
Rank Math → Analytics
├── Google Search Console: Connect
├── Google Analytics: Connect
├── Install Analytics Code: ON (or use separate)
└── Dashboard Widget: ON
```

### SEO Analysis
```
Rank Math → SEO Analysis
├── Run Analysis: Check site health
├── Fix Issues: Follow recommendations
└── Competitors: Track (Pro feature)
```

## On-Page SEO Structure

### Title Tag Formula
```
[Primary Keyword] - [Modifier/Benefit] | [Brand]

Examples:
"Best Smart Thermostats 2024 - Expert Reviews | Smart Home Wizards"
"Beginner Witchcraft Guide - Start Your Practice | Witchcraft For Beginners"
"AI Writing Tools Compared - Which is Best? | AI in Action Hub"
```

**Rules**:
- 50-60 characters (display limit)
- Primary keyword near start
- Compelling modifier (numbers, year, emotional words)
- Brand at end

### Meta Description Formula
```
[Hook/Question] + [Value Proposition] + [CTA]

Examples:
"Looking for the perfect smart thermostat? We tested 15+ models hands-on. See our honest reviews and find your match. Read our guide →"
"Ready to start witchcraft? Our beginner guide covers everything from first tools to first spells. Begin your magical journey today."
```

**Rules**:
- 150-155 characters
- Include target keyword naturally
- Compelling reason to click
- Action-oriented language

### Heading Hierarchy
```
H1: Main Topic (One per page, includes primary keyword)
├── H2: Major Section (Secondary keywords)
│   ├── H3: Subsection (Long-tail variations)
│   │   └── H4: Details (If needed)
│   └── H3: Another Subsection
├── H2: Another Major Section
│   └── H3: Subsection
└── H2: Conclusion/Summary
```

**Rules**:
- ONE H1 per page
- H2s for main sections
- H3s for subsections
- Never skip levels (H2 → H4)
- Include keywords naturally

### RankMath Focus Keyword
```
Post Editor → RankMath Meta Box
├── Focus Keyword: Primary keyword
├── Additional Keywords: 2-4 related terms
├── SEO Score: Aim for 80+
└── Readability: Aim for Good
```

**Best Practices**:
- Use focus keyword in:
  - Title tag
  - Meta description
  - H1 heading
  - First 100 words
  - Image alt text
  - URL slug
- Don't over-optimize (keyword stuffing)

## Schema Markup Patterns

### Article Schema (RankMath Default)
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "description": "Article description",
  "image": "https://site.com/image.jpg",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Site Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://site.com/logo.png"
    }
  },
  "datePublished": "2024-01-15",
  "dateModified": "2024-06-20"
}
```

### FAQ Schema (via RankMath Block)
```
<!-- In Gutenberg editor, add FAQ by Rank Math block -->

Or shortcode:
[rank_math_faq]
Question 1|Answer 1
Question 2|Answer 2
[/rank_math_faq]
```

### HowTo Schema (via RankMath Block)
```
<!-- In Gutenberg editor, add HowTo by Rank Math block -->

Includes:
- Total time
- Tools needed
- Materials
- Step-by-step instructions
```

### Product Review Schema
```
Post Editor → RankMath → Schema
├── Schema Type: Product
├── Product Name: [Product]
├── Description: Brief description
├── Brand: [Brand name]
├── SKU: (if applicable)
├── Price: $ amount
├── Rating: X/5
└── Review: Your review text
```

## Technical SEO

### XML Sitemap
RankMath auto-generates at: `yoursite.com/sitemap_index.xml`

Submit to:
- Google Search Console
- Bing Webmaster Tools

### robots.txt (via RankMath)
```
User-agent: *
Allow: /

Disallow: /wp-admin/
Disallow: /wp-login.php
Disallow: /?s=
Disallow: /search/

Sitemap: https://yoursite.com/sitemap_index.xml
```

### Canonical URLs
RankMath auto-adds canonicals. Override in post editor if needed.

### Redirections (RankMath Pro)
```
Rank Math → Redirections
├── Add New:
│   ├── Source URL: /old-page/
│   ├── Destination URL: /new-page/
│   └── Type: 301 (Permanent)
├── Import Redirections: CSV upload
└── Settings:
    ├── Redirect Attachments: ON
    ├── Monitor 404: ON
    └── Auto-redirect: ON
```

## Content Optimization

### RankMath Content Analysis
When editing a post, RankMath analyzes:

**Basic SEO** (Green checks needed):
- Focus keyword in title
- Focus keyword in meta description
- Focus keyword in URL
- Focus keyword in content
- Content length (minimum 600 words)
- Focus keyword in H2/H3

**Additional SEO**:
- External links (add 1-2)
- Internal links (add 2-4)
- Image with alt text
- Keyword density (1-2%)
- Table of contents (for long content)

**Readability**:
- Sentence length
- Paragraph length
- Transition words
- Passive voice (minimize)

### Content Structure for Featured Snippets

**Lists** (for "best of" queries):
```markdown
## Best [Things] for [Use Case]

Here are the top options:

1. **[Option 1]**: Description
2. **[Option 2]**: Description
3. **[Option 3]**: Description
```

**Tables** (for comparisons):
```markdown
| Feature | Product A | Product B | Product C |
|---------|-----------|-----------|-----------|
| Price | $50 | $75 | $100 |
| Rating | 4.5 | 4.8 | 4.2 |
```

**Definitions** (for "what is" queries):
```markdown
## What is [Term]?

[Term] is [clear, concise definition in 40-60 words].
```

**Steps** (for "how to" queries):
```markdown
## How to [Do Something]

Follow these steps:

1. **Step One**: Description
2. **Step Two**: Description
3. **Step Three**: Description
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
          ▼            ▼            ▼
    PILLAR POSTS ←→ CLUSTER CONTENT
```

### RankMath Link Suggestions
In post editor:
```
RankMath → Link Suggestions
├── Suggested Posts: Auto-suggested internal links
├── Link Count: Shows existing links
└── Orphan Content: Posts with no links
```

### Anchor Text Strategy
- **Branded**: "Smart Home Wizards guide"
- **Exact Match**: "smart thermostat reviews" (use sparingly)
- **Partial Match**: "our guide to smart thermostats"
- **Natural**: "we've written about this before"

## E-E-A-T Signals

### Experience
- First-person testing: "I tested..."
- Original photos
- Video demonstrations
- Real results and data

### Expertise
- Author bios with credentials
- Detailed explanations
- Industry knowledge
- Comprehensive coverage

### Authoritativeness
- Consistent author bylines
- Author archive pages
- Social proof
- External citations

### Trustworthiness
- Accurate information
- Updated content
- Contact information
- Affiliate disclosures

## RankMath SEO Checklist

### Before Publishing
- [ ] Focus keyword set
- [ ] Title tag optimized (50-60 chars)
- [ ] Meta description written (150-155 chars)
- [ ] URL is short and keyword-focused
- [ ] H1 includes focus keyword
- [ ] Focus keyword in first 100 words
- [ ] Content length adequate (600+ words)
- [ ] Images have alt text
- [ ] Internal links added (2-4)
- [ ] External links added (1-2)
- [ ] RankMath SEO score 80+
- [ ] Schema type selected
- [ ] Social images set

### After Publishing
- [ ] Submit to Google Search Console
- [ ] Share on social media
- [ ] Link from related posts
- [ ] Monitor rankings

### Monthly Tasks
- [ ] Review Search Console performance
- [ ] Update underperforming content
- [ ] Fix 404 errors (RankMath monitor)
- [ ] Add new schema opportunities
- [ ] Audit internal links
- [ ] Check keyword rankings

## RankMath Shortcuts

### Keyboard Shortcuts (in editor)
- `Ctrl + Shift + S`: Open RankMath sidebar
- Content Analysis: Auto-updates as you type

### Quick Access
- Dashboard: Rank Math → Dashboard
- Analytics: Rank Math → Analytics
- Schema: Per-post in editor sidebar
- Redirects: Rank Math → Redirections
- 404 Monitor: Rank Math → 404 Monitor
- Settings: Rank Math → General Settings
