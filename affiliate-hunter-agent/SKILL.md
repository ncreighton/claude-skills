---
name: affiliate-hunter-agent
description: Ultimate affiliate marketing opportunity locator and auto-application wizard for multi-site publishing networks. Use when user needs to find affiliate programs, discover partnership opportunities, evaluate commission structures, auto-apply to affiliate networks, track application status, or monetize content across multiple niches. Triggers include "find affiliates", "affiliate programs", "monetize", "commission", "partnership opportunities", "apply to affiliate", "Amazon Associates", "ShareASale", "Impact", "CJ Affiliate", "affiliate network", "product recommendations", or any revenue/monetization requests across website portfolios.
---

# Affiliate Hunter Agent

Automated affiliate program discovery, qualification, and application system for multi-site publishing empires.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   AFFILIATE HUNTER AGENT                     │
├─────────────────────────────────────────────────────────────┤
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐ │
│  │ Discovery │→ │Qualification│→ │Application│→ │ Tracking  │ │
│  │  Engine   │  │   Scorer   │  │   Agent   │  │  System   │ │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘ │
│        ↑              ↑              ↑              ↑        │
│  ┌─────────────────────────────────────────────────────────┐│
│  │              SITE PROFILE DATABASE                       ││
│  │   17 sites × niche data × traffic × application info    ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Discover Opportunities
```
"Find affiliate programs for [niche/site]"
"What affiliate networks work best for smart home content?"
"Discover high-commission programs for witchcraft products"
```

### 2. Qualify & Score
```
"Evaluate this affiliate program: [URL]"
"Compare commission rates for [product category]"
"Score these opportunities for [site name]"
```

### 3. Auto-Apply
```
"Apply to ShareASale for SmartHomeWizards.com"
"Fill out the Amazon Associates application"
"Submit affiliate applications for all my tech sites"
```

### 4. Track Status
```
"Check my pending affiliate applications"
"Update application status for [network]"
"Show approved programs across all sites"
```

## Discovery Engine

### Affiliate Network Categories

| Network Type | Examples | Best For |
|-------------|----------|----------|
| **Major Networks** | ShareASale, CJ, Impact, Awin | High-volume, diverse merchants |
| **Amazon Associates** | amazon.com/associates | Physical products, broad appeal |
| **Direct Programs** | Individual brand programs | Higher commissions, exclusivity |
| **Digital Products** | ClickBank, JVZoo, Warrior+ | Info products, courses |
| **SaaS/Software** | PartnerStack, FirstPromoter | Tech tools, subscriptions |
| **Hosting/Tech** | Bluehost, SiteGround | Web hosting, domains |

### Discovery Workflow

1. **Niche Analysis**
   - Load site profile from `references/site-profiles.json`
   - Identify primary content categories
   - Map content to product types

2. **Network Search Strategy**
   - Search major networks for niche keywords
   - Query "[niche] + affiliate program" variations
   - Check competitor backlinks for affiliate hints
   - Search for direct brand programs

3. **Opportunity Extraction**
   - Program name and merchant
   - Commission structure (% or flat)
   - Cookie duration
   - Payment threshold/terms
   - Application requirements

### Search Queries by Niche

**Witchcraft/Spirituality:**
- witchcraft supplies affiliate program
- tarot cards affiliate
- crystals wholesale affiliate
- spiritual products partnership
- occult supplies commission

**Smart Home:**
- smart home affiliate program
- home automation partnership
- IoT devices affiliate
- smart speaker affiliate
- Ring/Nest/Ecobee affiliate

**AI/Technology:**
- AI tools affiliate program
- SaaS affiliate partnership
- software affiliate high commission
- tech gadgets affiliate
- AI writing tools affiliate

**Mythology/Education:**
- book affiliate programs
- educational content partnership
- mythology merchandise affiliate
- collectibles affiliate program

**Family/Wellness:**
- family products affiliate
- parenting affiliate program
- wellness products partnership
- organic baby affiliate
- family health affiliate

**Productivity:**
- planner affiliate program
- stationery affiliate
- productivity tools affiliate
- bullet journal supplies affiliate

## Qualification Scoring

### Scoring Matrix (0-100)

| Factor | Weight | Criteria |
|--------|--------|----------|
| **Commission Rate** | 25% | >15%=25, 10-15%=20, 5-10%=15, <5%=10 |
| **Cookie Duration** | 20% | >30d=20, 15-30d=15, 7-14d=10, <7d=5 |
| **Product Fit** | 25% | Exact match=25, Related=15, Tangential=5 |
| **Brand Reputation** | 15% | Established=15, Growing=10, Unknown=5 |
| **Payment Terms** | 15% | <$25=15, $25-50=10, $50-100=5, >$100=3 |

### Minimum Thresholds

- Score ≥70: **Auto-apply** recommended
- Score 50-69: **Review** before applying
- Score <50: **Skip** unless strategic

### Red Flags to Avoid

- Payment threshold >$100
- Cookie duration <24 hours
- Negative merchant reviews
- Complex approval requirements
- Exclusive content mandates
- High refund rates

## Application Agent

### Site Profile Requirements

Each site profile in `references/site-profiles.json` contains:

```json
{
  "site_id": "witchcraft-beginners",
  "domain": "witchcraftforbeginners.com",
  "niche": "witchcraft/spirituality",
  "monthly_traffic": "estimated range",
  "primary_topics": ["spells", "tarot", "crystals"],
  "application_data": {
    "site_name": "Witchcraft For Beginners",
    "site_url": "https://witchcraftforbeginners.com",
    "site_description": "Educational resource for beginner witches...",
    "primary_category": "Spirituality/Religion",
    "secondary_category": "Lifestyle",
    "promotion_methods": ["Content/Blog", "Social Media", "Email"],
    "traffic_sources": ["Organic Search", "Pinterest", "Direct"]
  }
}
```

### Application Workflow

1. **Pre-Application Check**
   - Verify site meets network minimums
   - Check for existing applications
   - Confirm niche alignment

2. **Form Navigation** (via browser-automation-superagent)
   - Navigate to application URL
   - Detect form fields
   - Map to site profile data

3. **Field Mapping**
   ```
   Website URL → site_url
   Website Name → site_name
   Description → site_description
   Category → primary_category
   Traffic → monthly_traffic
   Promotion Methods → promotion_methods
   ```

4. **Submission & Capture**
   - Complete all required fields
   - Screenshot before submission
   - Submit application
   - Screenshot confirmation
   - Log to tracking system

### Browser Automation Commands

```python
# Using Browserbase MCP
browserbase_navigate(url=application_url)
browserbase_fill(selector="Website URL", value=site_url)
browserbase_fill(selector="Website Name", value=site_name)
browserbase_fill(selector="Description", value=site_description)
browserbase_select(selector="Category", value=category)
browserbase_click(selector="Submit Application")
browserbase_screenshot(filename="application_confirmation.png")
```

## n8n Automation Workflows

### Workflow 1: Opportunity Scanner
Scheduled daily scan for new opportunities.

See `references/n8n-workflows.json` for importable workflow.

### Workflow 2: Application Submitter
Triggered when opportunity score ≥70.

### Workflow 3: Status Checker
Weekly check of pending applications.

### Workflow 4: Approval Notifier
Alert when applications approved.

## Tracking System

### Status Categories

| Status | Description |
|--------|-------------|
| `discovered` | Found but not evaluated |
| `qualified` | Scored and ready for application |
| `applied` | Application submitted |
| `pending` | Awaiting network review |
| `approved` | Accepted into program |
| `rejected` | Application declined |
| `active` | Generating revenue |

### Tracking Database Schema

```json
{
  "opportunity_id": "uuid",
  "network": "ShareASale",
  "merchant": "Crystal Shop",
  "program_url": "https://...",
  "commission_rate": "15%",
  "cookie_duration": "30 days",
  "score": 82,
  "site_applied": "witchcraftforbeginners.com",
  "status": "pending",
  "applied_date": "2025-12-07",
  "notes": "",
  "affiliate_link": null
}
```

## Integration Points

### Required Tools
- **Web Search**: Discovery queries
- **Browser Automation**: Form filling (see browser-automation-superagent)
- **Credential Vault**: Network login storage (see credential-vault-manager)
- **n8n**: Workflow orchestration (see n8n-master-architect)

### Data Storage Options
- **Airtable**: Visual tracking dashboard
- **Notion**: Integrated with content planning
- **JSON Files**: Simple local storage
- **Google Sheets**: Collaborative access

## Execution Modes

### Interactive Mode
Claude assists step-by-step, requesting confirmation before actions.

### Autonomous Mode
Full automation with pre-approved criteria:
- Auto-apply when score ≥70
- Auto-reject when score <50
- Log all actions for review

### Batch Mode
Process multiple sites/networks in sequence:
```
"Apply to all witchcraft affiliate programs for WitchcraftForBeginners"
"Submit applications across all 17 sites for Amazon Associates"
```

## Files Reference

- `references/site-profiles.json` - Complete site database with application data
- `references/network-database.json` - Affiliate network details and requirements
- `references/n8n-workflows.json` - Importable automation workflows
- `scripts/discovery_scanner.py` - Automated opportunity finder
- `scripts/application_filler.py` - Form automation helper
- `scripts/tracker.py` - Status tracking utilities
- `assets/email-templates/` - Outreach templates for direct partnerships
