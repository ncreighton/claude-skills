---
name: zimmwriter-control
description: Complete control system for ZimmWriter v10.846+ content generation software. Use when user requests bulk content generation, ZimmWriter configuration, CSV creation for article batches, site-specific content workflows, or managing multi-site content operations across their 17-website publishing network. Triggers include phrases like "generate articles with ZimmWriter", "create bulk content for [site]", "set up ZimmWriter for [niche]", "make CSV for ZimmWriter", or any content automation requests.
---

# ZimmWriter Control System

Complete command and configuration system for ZimmWriter desktop application (v10.846+).

## Quick Start Commands

When user says: "Generate 50 smart home articles" → Generate CSV with titles, load site config, provide ZimmWriter settings
When user says: "Create mythology content batch" → Pull mythicalarchives.com config, generate appropriate outlines
When user says: "Set up ZimmWriter for witchcraft site" → Load witchcraftforbeginners.com settings, explain configuration

## Workflow Overview

1. **Understand request** - Identify site, quantity, topic focus
2. **Load site config** - Read from references/site-configs.json
3. **Generate content plan** - Create titles, outlines, keywords
4. **Create CSV file** - Use scripts/generate_bulk_csv.py
5. **Provide ZimmWriter settings** - Specify exact UI configuration
6. **Deliver instructions** - Step-by-step loading process

## ZimmWriter Interface Structure

###

 Bulk Blog Writer (Main Interface)

**Title Input Area:**
- List of Blog Post Titles (large text box, top of screen)
- Format: Semi-colon separated OR one per line (up to 1,000 titles, 70,000 chars max)
- Alternative: Load SEO CSV (overrides manual titles)

**Left Column Settings:**
- # of H2: Automatic (dropdown) or specific number (1-20)
- H2 Auto Limit: Number dropdown (default 10)
- Section Length: Short/Medium/Long dropdown
- Voice: First Person/Second Person/Third Person
- Enable Literary Devices checkbox
- Enable Lists checkbox
- Enable Tables checkbox
- Enable Blockquotes checkbox
- Nuke AI Words checkbox
- Bold to Help Readability checkbox
- Enable Key Takeaways checkbox
- Disable Skinny Paragraphs checkbox
- Enable H3 checkbox
- Disable Active Voice checkbox
- Disable Conclusion checkbox

**Middle Column Settings:**
- Intro: Standard Intro/No Intro dropdown
- FAQ: No FAQ/FAQ dropdown
- Audience Personality: None dropdown
- AI Model for Writing: Claude-4.5 Sonnet (ANT) / GPT-4o Mini (OA) / etc.
- Write in the Style of ___ (text input)
- Use Auto Style checkbox
- Automatic Keywords checkbox
- Show Image Prompt for Each H2 checkbox
- Enable Progress Indicator checkbox
- Overwrite URL Merge Cache checkbox

**Right Column Settings:**
- Featured Image: None dropdown
- Subheading Image Quantity: None dropdown
- Subheading Images Model: None dropdown
- AI Model for Image Prompts: None dropdown
- Output in Non-English: (text input)
- AI Model for Translation: None dropdown

**Right Side Buttons (Enable/Disable Features):**
- WordPress Disabled
- Link Pack Disabled
- SERP Scraping Disabled
- Deep Research Disabled
- Style Mimic Disabled
- Custom Outline Disabled
- Custom Prompt Disabled
- YouTube Videos Disabled
- Webhook Disabled
- Alt Images Disabled
- SEO CSV Disabled (**turns GREEN when CSV loaded**)

**Bottom Buttons:**
- Start Bulk Writer
- Exit Bulk Writer
- Clear All Data

**Profile Management:**
- Load Profile: None dropdown (top left)
- Profile Name: (text input)
- Save Profile / Update Profile / Delete Profile buttons

## Site Configurations

Reference references/site-configs.json for complete details. Key sites:

1. **aiinactionhub.com** - AI & Technology (2000-2500 words, professional tone)
2. **smarthomewizards.com** - Smart Home Automation (1800-2200 words, friendly/helpful)
3. **witchcraftforbeginners.com** - Witchcraft & Spirituality (1500-2000 words, mystical/supportive)
4. **family-flourish.com** - Family & Parenting (1500-2000 words, warm/practical)
5. **mythicalarchives.com** - Mythology & Folklore (2000-2500 words, scholarly/engaging)

*(12 additional sites to be configured as needed)*

## CSV Generation

### Quick Generation from Titles

```python
from scripts.generate_bulk_csv import generate_csv_from_titles

titles = ["Article Title 1", "Article Title 2", "Article Title 3"]

generate_csv_from_titles(
    titles=titles,
    output_path="/tmp/batch.csv",
    site_domain="smarthomewizards.com",
    wordpress_category="Guides"
)
```

### Detailed Articles with Custom Outlines

```python
from scripts.generate_bulk_csv import generate_bulk_csv

articles = [{
    'title': 'Best Smart Thermostats 2025',
    'outline': '''Best Thermostats
- Nest Learning{url=https://amazon.com/dp/XXX}{tpl}
- Ecobee Smart{url=https://amazon.com/dp/XXX}{tpl}
Buying Guide{list}''',
    'seo_keywords': ['smart thermostat', 'nest', 'ecobee'],
    'wordpress_category': 'Product Reviews'
}]

generate_bulk_csv(articles, "/tmp/detailed.csv", "smarthomewizards.com")
```

## Typical Workflows

### Bulk Generation (No Custom Outline)
1. Generate titles based on user request
2. Create CSV with titles only
3. Load site config for settings
4. Provide ZimmWriter configuration
5. User loads CSV, starts generation

### Product Roundups (Custom Outlines)
1. Generate roundup title
2. Create outline with {tpl} and {url=} variables
3. Populate OUTLINE column in CSV
4. ZimmWriter auto-enables Custom Outline
5. Product templates auto-generate

### SERP-Optimized Content
1. Generate titles + comprehensive keywords
2. Populate SEO KEYWORDS column (50-150 per article)
3. Enable SERP Scraping in ZimmWriter
4. Keywords auto-populate from CSV

## Common Settings by Site

### AI Technology (aiinactionhub.com)
- H2: Automatic, limit 10 | Section: Medium-Long | Voice: Second Person
- Enable: Lists, Tables, Blockquotes, H3, FAQ, Key Takeaways
- Model: Claude-4.5 Sonnet | SERP: Enabled

### Smart Home (smarthomewizards.com)
- H2: Automatic, limit 8-10 | Section: Medium | Voice: Second Person
- Enable: Lists, Tables, H3, FAQ, Key Takeaways
- Model: Claude-4.5 Sonnet | Link Pack: For affiliates

### Witchcraft (witchcraftforbeginners.com)
- H2: Automatic, limit 8 | Section: Medium | Voice: Second Person
- Enable: Lists, Blockquotes, Literary Devices, H3, FAQ
- Model: Claude-4.5 Sonnet | SERP: Disabled (preserve unique voice)

### Mythology (mythicalarchives.com)
- H2: Automatic, limit 10 | Section: Long | Voice: Third Person
- Enable: Lists, Tables, Blockquotes, Literary Devices, H3, FAQ
- Model: Claude-4.5 Sonnet | SERP: Enabled

## Custom Outline Variables

- **{list}** - Generate bulleted list
- **{table}** - Create comparison table
- **{yt}** - Embed YouTube video suggestion
- **{tpl}** - Product template (requires {url=})
- **{url=https://...}** - Scrape specific URL

Example:
```
Smart Lock Features{table}
- Security Ratings{list}
- Installation{url=https://example.com/guide}
```

## Quality Control Checklist

Before bulk generation:
1. ✓ CSV loaded (SEO CSV button GREEN)
2. ✓ AI Model: Claude-4.5 Sonnet
3. ✓ WordPress category configured
4. ✓ Link Pack loaded (if affiliates)
5. ✓ Section Length appropriate
6. ✓ Enable Progress Indicator
7. ✓ Test with 2-3 articles first

## Best Practices

1. **Start small** - Test 5-10 articles before large batches
2. **Use profiles** - Save configurations per site/niche
3. **CSV organization** - Separate CSVs per site
4. **Review outputs** - Check first articles for quality
5. **Keyword research** - Quality keyword lists matter
6. **Custom outlines** - Use for structured/product content
7. **Draft status** - Review before publishing
8. **Backup CSVs** - Save for regeneration

## Resources

- **scripts/generate_bulk_csv.py** - CSV generation utilities
- **references/site-configs.json** - All site configurations
- **references/outline-templates.md** - Common outline patterns (to be added)
- **references/keyword-strategies.md** - SEO keyword guidance (to be added)
