# Affiliate/Review Site Build Profile

## Site Type: Affiliate & Product Review

**Sites in this category:**
- SmartHomeWizards
- PulseGearReviews  
- KitchenTechInsider
- WearableGearHub
- TheConnectedHaven

---

## Revenue Model

```
Primary: Affiliate Commissions (60-80% of revenue)
├── Amazon Associates (main)
├── Direct brand partnerships
├── ShareASale/CJ Affiliate networks
└── Individual product affiliate programs

Secondary: Display Advertising (20-40%)
├── Mediavine/AdThrive (when qualified)
└── Google AdSense (starting out)

Tertiary: Lead Generation
└── Newsletter sponsorships
```

---

## Content Architecture

### Content Pillars

1. **Product Reviews** (40% of content)
   - Individual product deep-dives
   - 2,000-3,500 words
   - Schema: Product, Review
   - Affiliate links: 3-5 per review

2. **Comparison Posts** (25% of content)
   - "X vs Y" and "Best X for Y"
   - Comparison tables required
   - 2,500-4,000 words
   - Schema: ItemList, Product
   - Affiliate links: 5-10

3. **Buying Guides** (20% of content)
   - "How to Choose..." 
   - Criteria explanation
   - 3,000-5,000 words
   - Schema: HowTo, ItemList
   - Internal links to reviews

4. **How-To/Tutorial** (15% of content)
   - Setup guides, troubleshooting
   - Supports product recommendations naturally
   - 1,500-2,500 words
   - Schema: HowTo

---

## Required Plugins (Beyond Core)

| Plugin | Purpose | Configuration |
|--------|---------|---------------|
| **FLAVOR** or **TablePress** | Comparison tables | Style to match DNA |
| **ThirstyAffiliates** or **Pretty Links** | Link management | Cloaking, tracking |
| **FLAVOR Amazon** | Product blocks | If using FLAVOR suite |
| **WP Review Starter** | Review schema | Star ratings, pros/cons |

### Plugin Configuration: ThirstyAffiliates
```
Settings:
- Link Prefix: /recommends/ or /go/
- No-follow: Yes (all affiliate links)
- Open in new tab: Yes
- Link categories: By product type
- Geotargeting: Enable if international audience

Disclosure:
- Auto-insert disclosure: Yes
- Disclosure text: Site-specific from DNA
- Position: Top of content
```

---

## Homepage Structure

### Hero Section
```
Purpose: Establish authority, not hard-sell
Content:
- Headline: "Expert [Niche] Reviews & Guides"
- Subhead: What makes reviews trustworthy
- Trust signals: Years of experience, products tested
- NO: "Buy now" or aggressive affiliate pushes

Example for SmartHomeWizards:
"Independent Smart Home Reviews Since 2023
We test every device. We recommend only what works."
```

### Section 1: Featured Reviews
```
Layout: 3-4 "Editor's Choice" products
Content:
- Best-in-category highlights
- Quick specs
- Rating badge
- "Read Full Review" CTA

NOT: Direct buy links on homepage (too aggressive)
```

### Section 2: Category Navigation
```
Layout: Visual category cards
Categories for SmartHomeWizards:
- Smart Speakers
- Smart Lighting
- Security Cameras
- Smart Thermostats
- Robot Vacuums
```

### Section 3: Latest Reviews
```
Layout: Blog-style with thumbnails
Content: Most recent reviews
Purpose: Show freshness/activity
```

### Section 4: How We Test
```
Purpose: E-E-A-T signal
Content:
- Testing methodology
- Review criteria
- Editorial independence statement
- Meet the team (optional)
```

---

## Single Review Template

### Above the Fold
```
[Breadcrumbs]
[H1: Product Name Review: Verdict in Title]
[Quick Verdict Box]
├── Overall Rating: X/10 stars
├── Best For: [use case]
├── Price: $XXX (with affiliate link)
└── Our Take: 1-2 sentence summary
[Featured Image: Product hero shot]
[Table of Contents]
```

### Review Body Structure
```
1. Executive Summary (for skimmers)
   - What it is
   - Who it's for
   - Key findings
   - Verdict

2. Specifications Table
   - Key specs in scannable format
   - Comparison to competitors

3. Design & Build (with images)
4. Features & Performance
5. Pros & Cons (structured data)
6. Real-World Testing Results
7. Value Assessment
8. Verdict & Recommendations
9. FAQ Section
10. Related Products (internal links)
```

### Affiliate Link Placement
```
Strategic positions:
1. Quick verdict box (above fold) - 1 link
2. After specifications - 1 link
3. Mid-content "Check Price" button - 1 link
4. After verdict - 1-2 links
5. Comparison to alternatives - links to each

Total: 5-7 affiliate links per review
Too many = spam, too few = lost revenue
```

### Required Schema
```json
{
  "@type": "Product",
  "name": "Product Name",
  "image": "product-image.jpg",
  "description": "...",
  "brand": { "@type": "Brand", "name": "..." },
  "review": {
    "@type": "Review",
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": "8.5",
      "bestRating": "10"
    },
    "author": { "@type": "Person", "name": "..." }
  },
  "aggregateRating": {...},
  "offers": {
    "@type": "Offer",
    "price": "299.99",
    "priceCurrency": "USD",
    "availability": "InStock",
    "url": "affiliate-link"
  }
}
```

---

## Comparison Post Template

### Structure
```
[H1: X vs Y: Which Should You Buy in 2025?]
[Quick Answer Box]
├── Winner for [use case 1]: Product X
├── Winner for [use case 2]: Product Y
└── Best Overall: [winner]

[Comparison Table - REQUIRED]
| Feature | Product X | Product Y |
|---------|-----------|-----------|
| Price   | $X        | $Y        |
| ...     | ...       | ...       |

[Detailed Comparison Sections]
[Final Verdict with recommendations by use case]
[FAQ]
```

### Comparison Table Requirements
```
Must include:
- Price (with affiliate links)
- Key differentiating features
- Our rating for each
- "Best For" use case
- Visual indicators (✓/✗ or color coding)

Style:
- Sticky header on scroll
- Mobile responsive (cards or horizontal scroll)
- DNA-compliant colors
```

---

## Buying Guide Template

### Structure
```
[H1: How to Choose the Best [Product Category] in 2025]
[Who This Guide is For]
[Quick Recommendations Table]
├── Best Overall: [link]
├── Best Budget: [link]
├── Best Premium: [link]
└── Best for [specific need]: [link]

[What to Look For Section]
- Feature 1 explanation
- Feature 2 explanation
- etc.

[Our Top Picks - Detailed]
- Each recommendation with mini-review
- Links to full reviews

[FAQ]
```

---

## Legal Requirements

### FTC Compliance
```
Required elements:
1. Affiliate Disclosure page (/affiliate-disclosure/)
2. Per-post disclosure (top of content)
3. Clear labeling of affiliate links

Disclosure text example:
"This post contains affiliate links. If you purchase through these links, 
we earn a commission at no extra cost to you. This helps support our 
independent testing. See our full disclosure."
```

### Amazon-Specific
```
Required:
- "As an Amazon Associate I earn from qualifying purchases"
- Prices must include "at time of posting" disclaimer
- No price guarantees
- No screenshots of Amazon pages (use own photos)
```

---

## SEO Priorities

### Target Keywords
```
Primary patterns:
- "[product name] review"
- "best [product category]"
- "[product X] vs [product Y]"
- "is [product] worth it"
- "[product category] buying guide"

Long-tail patterns:
- "best [product] for [specific use]"
- "[product] review [year]"
- "[product] pros and cons"
```

### Internal Linking Strategy
```
From reviews → buying guides (hub)
From buying guides → individual reviews
From comparisons → both products reviewed
Cross-link related product categories

Example link flow:
Smart Speaker Buying Guide (pillar)
├── Echo Dot Review
├── Google Nest Mini Review
├── HomePod Mini Review
└── Echo Dot vs Google Nest (comparison)
    ├── Links back to guide
    └── Links to each review
```

---

## Performance Considerations

### Image Optimization
```
Product images:
- Hero: 1200x800 max, WebP
- Thumbnails: 400x300
- Comparison tables: 200x200 product shots
- Lazy load all below fold

Sources:
- Take own photos when possible (E-E-A-T)
- Press kit images (with permission)
- Amazon product images (check TOS)
```

### Page Speed
```
Review pages tend to be heavy:
- Multiple product images
- Comparison tables
- Affiliate widgets

Mitigations:
- Aggressive lazy loading
- Defer non-critical JS
- Minimize affiliate plugin scripts
- Use native lazy loading for images
```

---

## Monetization Tracking

### Track These Metrics
```
Per post:
- Click-through rate to affiliate links
- Conversion rate (if available)
- Revenue per post
- Revenue per 1000 visitors

Overall:
- Total affiliate revenue
- Revenue by product category
- Revenue by affiliate program
- Best performing posts
```

### Analytics Setup
```
Google Analytics 4:
- Track outbound link clicks
- Create affiliate link click event
- Tag links with categories

ThirstyAffiliates:
- Enable click tracking
- Review click reports weekly
```

---

## Anti-Patterns for Affiliate Sites

```
NEVER:
✗ Fake reviews (never tested product)
✗ Excessive affiliate links (>10 per post)
✗ Auto-generated comparison tables
✗ Prices without "at time of posting"
✗ Missing FTC disclosure
✗ Aggressive pop-ups for affiliate products
✗ Thin content just to place links
✗ Hiding affiliate relationship
✗ Keyword stuffing in reviews

ALWAYS:
✓ Honest pros AND cons
✓ Test products when possible
✓ Clear disclosure
✓ Helpful, complete information
✓ Update reviews when products change
✓ Recommend alternatives (even non-affiliate)
```

---

## Checklist: Affiliate Site Launch

```
□ Affiliate disclosure page live
□ ThirstyAffiliates/link manager configured
□ Comparison table plugin styled to DNA
□ Review schema implemented and validated
□ At least 3 pillar buying guides published
□ At least 10 product reviews published
□ Internal linking structure complete
□ Amazon Associates approved (or applied)
□ Analytics tracking affiliate clicks
□ FTC disclosures on all affiliate content
```

---

*Affiliate Site Profile - Site Build Orchestrator v2.0*
