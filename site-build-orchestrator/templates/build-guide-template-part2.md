## Phase 5: Templates

### P5.1 - Category Template
```
Create/configure the category archive template:

{{CATEGORY_TEMPLATE}}

Layout: {{CATEGORY_LAYOUT}}
Posts Per Page: {{CATEGORY_POSTS_PER_PAGE}}
Pagination: {{CATEGORY_PAGINATION}}

Featured Treatment: {{CATEGORY_FEATURED}}
Card Style: {{CATEGORY_CARD_STYLE}}

Ensure category description displays at top.
```

### P5.2 - Single Post Template
```
Create/configure the single post template:

{{SINGLE_POST_TEMPLATE}}

Layout: {{SINGLE_POST_LAYOUT}}
Max Width: {{SINGLE_POST_MAX_WIDTH}}
Sidebar: {{SINGLE_POST_SIDEBAR}}

Typography for long-form reading:
- Paragraph spacing: {{PARAGRAPH_SPACING}}
- Line height: {{LINE_HEIGHT_BODY}}
- Font size: {{TYPE_BASE}} (consider {{TYPE_LG}} for this site)

Include:
- Featured image: {{FEATURED_IMAGE_STYLE}}
- Author box: {{AUTHOR_BOX}}
- Related posts: {{RELATED_POSTS}}
- Social sharing: {{SOCIAL_SHARING}}
- Comments: {{COMMENTS_STYLE}}
```

### P5.3 - Post Meta Styling
```
Style post meta information:
- Date format: {{DATE_FORMAT}}
- Author display: {{AUTHOR_DISPLAY}}
- Category links: {{CATEGORY_LINKS}}
- Reading time: {{READING_TIME}}
- Last updated: {{LAST_UPDATED}}

Position: {{META_POSITION}}
Style: {{META_STYLE}}
```

### P5.4 - Page Template
```
Create/configure the standard page template:

{{PAGE_TEMPLATE}}

Layout: {{PAGE_LAYOUT}}
Header: {{PAGE_HEADER_STYLE}}
Content Width: {{PAGE_CONTENT_WIDTH}}
```

### P5.5 - Search Results Template
```
Configure search results page:

Layout: Similar to category archive
Results format: {{SEARCH_RESULTS_FORMAT}}
No results message: "{{NO_RESULTS_MESSAGE}}"
```

### P5.6 - 404 Page Template
```
Create custom 404 page:

Message style: {{404_MESSAGE_STYLE}}
Include:
- Branded illustration or image
- Helpful message (matches voice)
- Search box
- Popular content links
- Return home button

Example copy for {{SITE_NAME}}:
"{{404_COPY}}"
```

### ✓ Phase 5 Checkpoint
```
Run Phase 5 checkpoint:
1. Create a test post, view single post template
2. View a category archive
3. View a page
4. Test search with results
5. Test search with no results
6. Force a 404 and check page
7. Verify typography matches DNA on long content
8. Check all templates on mobile
```

---

## Phase 6: Core Pages

### P6.1 - About Page
```
Create the About page for {{SITE_NAME}}:

URL: /about/ (or {{ABOUT_URL}})
Title: "{{ABOUT_TITLE}}"

Content structure:
{{ABOUT_CONTENT_STRUCTURE}}

Voice: {{ABOUT_VOICE}}
Include: {{ABOUT_INCLUDES}}
```

### P6.2 - Contact Page
```
Create the Contact page:

URL: /contact/
Title: "{{CONTACT_TITLE}}"

Include:
- Contact form (WPForms)
- Email: {{CONTACT_EMAIL}}
- Social links: {{SOCIAL_LINKS}}
- Response time expectation

Form fields:
{{CONTACT_FORM_FIELDS}}
```

### P6.3 - Privacy Policy
```
Create Privacy Policy page:

URL: /privacy-policy/
Use Complianz generated policy as base.
Customize with site-specific data practices.

Sections required:
- Information collection
- Cookie usage
- Third-party services (affiliates, analytics)
- User rights
- Contact information
```

### P6.4 - Terms of Service
```
Create Terms of Service page:

URL: /terms/
Include standard terms for:
- Content usage
- Affiliate disclosure
- Liability limitations
- User conduct
- Copyright
```

### P6.5 - Affiliate Disclosure
```
Create Affiliate Disclosure page:

URL: /affiliate-disclosure/ (or {{DISCLOSURE_URL}})
Required by FTC.

Content:
- Clear statement of affiliate relationships
- How recommendations are made
- Commission structure mention
- Promise of honest reviews
```

### P6.6 - Start Here / Pillar Page
```
Create the main entry point page:

URL: {{START_HERE_URL}}
Title: "{{START_HERE_TITLE}}"

This is the key pillar page for {{SITE_NAME}}.

Structure:
{{START_HERE_STRUCTURE}}

Internal links to: {{START_HERE_LINKS}}
```

### P6.7 - Category Landing Pages
```
Create landing pages for main categories:

{{CATEGORY_LANDING_PAGES}}

Each category landing should have:
- Custom introduction
- Featured/best content
- Subcategory navigation
- Clear content hierarchy
```

### ✓ Phase 6 Checkpoint
```
Run Phase 6 checkpoint:
1. Visit each core page - all accessible?
2. Contact form submits correctly?
3. Privacy and Terms are complete?
4. Affiliate disclosure present?
5. Start Here page has clear navigation?
6. All pages match site design?
7. No broken links?
```

---

## Phase 7: SEO Setup

### P7.1 - RankMath General Setup
```
Configure RankMath SEO:

Run setup wizard:
- Mode: Advanced
- Enable modules: SEO Analysis, Sitemap, Schema, Redirections, 404 Monitor, Analytics

General Settings:
- Separator: {{SEO_SEPARATOR}}
- OpenGraph: Enabled
- Twitter Cards: Enabled
```

### P7.2 - Title & Meta Templates
```
Configure title templates:

Homepage: {{SEO_HOMEPAGE_TITLE}}
Posts: %title% {{SEO_SEPARATOR}} %sitename%
Pages: %title% {{SEO_SEPARATOR}} %sitename%
Categories: %term% {{SEO_SEPARATOR}} %sitename%

Meta descriptions: Leave to individual page optimization
```

### P7.3 - Schema Markup
```
Configure default schema:

Site Type: {{SCHEMA_SITE_TYPE}}
Organization/Person: {{SCHEMA_ENTITY_TYPE}}
Logo: Upload site logo

Default post schema: Article
Enable FAQ schema: Yes
Enable HowTo schema: Yes (for applicable content)

Site-specific schema:
{{SITE_SPECIFIC_SCHEMA}}
```

### P7.4 - XML Sitemap
```
Configure sitemap settings:

Include:
- Posts: Yes
- Pages: Yes
- Categories: Yes
- Tags: {{SITEMAP_TAGS}}

Exclude:
- Author archives
- Date archives
- {{SITEMAP_EXCLUDES}}

Submit to:
- Google Search Console
- Bing Webmaster Tools
```

### P7.5 - Search Console Verification
```
Add site to Google Search Console:

1. Use HTML tag method or DNS verification
2. Submit sitemap: {{SITE_URL}}/sitemap_index.xml
3. Request indexing for homepage
4. Set up performance tracking
```

### P7.6 - Robots.txt Configuration
```
Configure robots.txt:

Allow: All public content
Disallow:
- /wp-admin/
- /wp-includes/
- /wp-content/plugins/
- /trackback/
- /feed/
- /?s=

Sitemap: {{SITE_URL}}/sitemap_index.xml
```

### P7.7 - Internal Linking Strategy Setup
```
Plan internal linking structure:

Strategy: {{INTERNAL_LINKING_STRATEGY}}

Pillar pages: {{PILLAR_PAGES}}
Hub structure: {{HUB_STRUCTURE}}

Create a linking map document for content team.
```

### P7.8 - Redirections Setup
```
Configure Redirections plugin:

Monitor 404s: Enabled
Auto-redirect: Disabled (manual control)

Create initial redirects:
{{INITIAL_REDIRECTS}}
```

### ✓ Phase 7 Checkpoint
```
Run Phase 7 checkpoint:
1. RankMath shows green checkmarks for setup
2. Schema validation: Use Google Rich Results Test
3. Sitemap accessible and complete
4. Site verified in Search Console
5. robots.txt correct
6. No critical SEO issues flagged
```

---

## Phase 8: Performance Optimization

### P8.1 - LiteSpeed Cache Configuration
```
Configure LiteSpeed Cache:

Cache Settings:
- Enable Cache: Yes
- Cache Logged-in Users: No
- Cache Mobile: Yes
- Private Cache: No

TTL Settings:
- Default: 604800 (7 days)
- Front Page: 604800
- Feed: 0 (disabled)

Object Cache:
- Enable if Redis/Memcached available
```

### P8.2 - Page Optimization
```
Configure page optimization:

CSS:
- Minify: Yes
- Combine: Test first, may break
- Inline: Async
- Font display: swap

JavaScript:
- Minify: Yes
- Combine: No (often breaks)
- Defer: Yes
- Inline: No

HTML:
- Minify: Yes
- DNS Prefetch: {{DNS_PREFETCH}}
- Preload: {{PRELOAD_ASSETS}}
```

### P8.3 - Image Optimization Setup
```
Configure image optimization:

LiteSpeed Image Optimization:
- Auto Request: Yes
- Optimization Level: Lossy
- WebP: Yes
- QUIC.cloud: Connect account

Or ShortPixel (alternative):
- API Key: [Configure]
- Compression: Lossy
- WebP: Yes
- Resize large: Yes (max 2048px)
```

### P8.4 - Lazy Loading
```
Configure lazy loading:

LiteSpeed:
- Lazy Load Images: Yes
- Lazy Load iframes: Yes
- Placeholder: Responsive

Exclude from lazy loading:
- Logo
- Above-fold hero images
- LCP image
```

### P8.5 - Critical CSS
```
Generate critical CSS:

Use LiteSpeed UCSS (Unique CSS):
- Enable UCSS: Yes
- Inline: Yes
- Async load: Yes

This removes unused CSS from each page.
```

### P8.6 - Database Optimization
```
Optimize database:

LiteSpeed:
- Clean Revisions: Keep last 5
- Auto Drafts: Clean
- Trash: Clean
- Spam Comments: Clean
- Optimize Tables: Yes
- Schedule: Weekly
```

### P8.7 - CDN Setup (Optional)
```
Configure QUIC.cloud CDN:

1. Connect QUIC.cloud account
2. Enable CDN in LiteSpeed
3. Configure:
   - Cache Static Files: Yes
   - HTML Cache: Optional (test first)
   
Or Cloudflare:
- Point DNS to Cloudflare
- SSL: Full (Strict)
- Cache: Standard
- Page Rules for WP Admin
```

### P8.8 - Performance Testing
```
Run performance tests:

Test URLs:
- Homepage: {{SITE_URL}}
- Single post: {{TEST_POST_URL}}
- Category: {{TEST_CATEGORY_URL}}

Targets:
- PageSpeed Mobile: >{{PERF_MOBILE}}
- PageSpeed Desktop: >{{PERF_DESKTOP}}
- LCP: <{{PERF_LCP}}
- FID/INP: <{{PERF_FID}}
- CLS: <{{PERF_CLS}}

If targets not met, iterate on:
1. Image optimization
2. Render-blocking resources
3. Server response time
4. JavaScript execution
```

### ✓ Phase 8 Checkpoint
```
Run Phase 8 checkpoint:
1. PageSpeed Insights score meets targets
2. Core Web Vitals all green
3. No console errors
4. Cache working (check headers)
5. WebP images serving
6. Lazy loading working
7. No visible layout shift
```

---

## Phase 9: Initial Content

### P9.1 - Create Content Categories
```
Create the main content categories:

{{CONTENT_CATEGORIES}}

For each category:
- Name and slug
- Description (SEO optimized)
- Parent/child relationships
```

### P9.2 - Pillar Content Creation
```
Create pillar/cornerstone content:

{{PILLAR_CONTENT_LIST}}

Each pillar should:
- Target primary keyword
- Be comprehensive ({{PILLAR_WORD_COUNT}} words)
- Include internal links to related content
- Have optimized schema
```

### P9.3 - Supporting Content
```
Create initial supporting content:

{{SUPPORTING_CONTENT_LIST}}

Each post should:
- Link back to pillar page
- Target secondary keyword
- Include related post links
```

### P9.4 - Internal Link Implementation
```
Build internal link structure:

From pillars to clusters: 
- Each pillar links to 5-10 related posts
- Related posts link back to pillar
- Cross-link between related posts

Use RankMath link suggestions.
```

### P9.5 - Media Library Organization
```
Organize media library:

Create folders/tags for:
- Hero images
- Featured images
- Content images
- Icons/graphics
- Logos/branding

Naming convention: {{MEDIA_NAMING}}
Alt text: Always descriptive, keyword-aware
```

### ✓ Phase 9 Checkpoint
```
Run Phase 9 checkpoint:
1. All categories created
2. Pillar content published
3. Supporting content linked
4. Internal links working
5. No orphan pages
6. No broken links
7. All images optimized with alt text
```

---

## Phase 10: QA & Launch

### P10.1 - Cross-Browser Testing
```
Test in all major browsers:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

Check for:
- Layout consistency
- Font rendering
- Animation smoothness
- Form functionality
```

### P10.2 - Mobile Testing
```
Test on mobile devices:
- iPhone Safari
- Android Chrome
- Test touch interactions
- Verify responsive layouts
- Check font sizes (readable without zoom)
- Test navigation
```

### P10.3 - Accessibility Check
```
Run accessibility audit:

Check:
- Color contrast (WCAG AA minimum)
- Alt text on all images
- Keyboard navigation
- Focus states
- Screen reader compatibility
- Skip links
```

### P10.4 - Link Audit
```
Check all links:

Use Screaming Frog or similar:
- No 404 errors
- No redirect chains
- External links work
- Internal links correct
```

### P10.5 - Final SEO Audit
```
Final SEO checks:

- All pages have meta titles
- All pages have meta descriptions
- Schema validates
- Sitemap complete and submitted
- No noindex on public content
- Canonical tags correct
```

### P10.6 - Security Check
```
Final security audit:

- WordPress updated
- All plugins updated
- No vulnerabilities (Wordfence scan)
- File permissions correct
- SSL working sitewide
- Login protection active
```

### P10.7 - Backup & Documentation
```
Pre-launch backup:

- Full UpdraftPlus backup
- Download copy locally
- Document all configurations
- Save credentials securely
```

### P10.8 - Analytics Setup
```
Configure analytics:

Google Analytics 4:
- Property created
- Tracking code installed
- Goals/conversions set up
- Search Console connected

RankMath Analytics:
- Connect GA4
- Enable tracking
```

### P10.9 - Launch Checklist
```
Final launch checks:

[ ] All content proofread
[ ] Contact form tested
[ ] Thank you pages work
[ ] Email notifications work
[ ] 404 page works
[ ] Search works
[ ] All pages accessible
[ ] No test content visible
[ ] Remove "Coming Soon" if applicable
[ ] Remove staging URL references
```

### P10.10 - Go Live
```
Launch the site:

1. Clear all caches
2. Test homepage loads
3. Test key pages
4. Submit to Google for indexing
5. Announce launch (if applicable)
6. Monitor for 24 hours
```

### ✓ Phase 10 Final Checkpoint
```
Post-launch verification:

[ ] Site loads correctly
[ ] No console errors
[ ] Forms submitting
[ ] Analytics tracking
[ ] No broken links
[ ] Search engines can access
[ ] SSL working
[ ] Cache serving
[ ] All critical pages accessible

LAUNCH COMPLETE ✓
```

---

## Post-Launch Maintenance

### Weekly Tasks
- Check analytics
- Monitor Search Console
- Review 404 reports
- Content updates

### Monthly Tasks
- Plugin updates
- Security scan
- Performance check
- Backup verification

### Quarterly Tasks
- Content audit
- SEO review
- Speed optimization
- Competitive analysis

---

## Emergency Procedures

### Site Down
1. Check hosting status
2. Disable last plugin updated
3. Check error logs
4. Restore from backup if needed

### Hacked
1. Enable maintenance mode
2. Run Wordfence scan
3. Change all passwords
4. Restore from clean backup
5. Update everything
6. Request Google re-review if needed

---

*Generated by Site Build Orchestrator for {{SITE_NAME}}*
*Build Guide Version: 1.0*
*Last Updated: {{DATE}}*
