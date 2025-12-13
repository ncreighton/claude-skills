---
name: enhancement-scout
description: Proactive discovery system for finding new tools, apps, programs, techniques, and capabilities that would enhance the AI agent ecosystem. Continuously scans for innovations, evaluates relevance, and recommends adoptions. Use when user asks about new tools, when capability gaps are detected, or proactively during any task where better tools might exist. Triggers include "find better", "new tools", "alternatives", "what's new", "trending", "innovations", or automatically when detecting potential for improvement.
---

# Enhancement Scout

Proactive discovery of tools, techniques, and innovations.

## Core Mission

Never settle for current capabilities. Continuously:
- Scout for new tools and technologies
- Evaluate innovations for relevance
- Recommend adoptions and upgrades
- Stay ahead of the curve
- Bring the best to the workflow

## Discovery Domains

### 1. AI & Automation Tools
```yaml
categories:
  content_generation:
    - AI writing tools
    - Image generators
    - Video creation
    - Voice synthesis
    
  automation:
    - Workflow platforms (n8n, Make, Zapier)
    - Browser automation
    - API orchestration
    - Task scheduling
    
  ai_agents:
    - Agent frameworks
    - MCP servers
    - AI coding tools
    - Autonomous systems
```

### 2. Publishing & Content
```yaml
categories:
  cms_platforms:
    - WordPress enhancements
    - Headless CMS options
    - Publishing automation
    
  seo_tools:
    - Keyword research
    - Content optimization
    - Rank tracking
    - Link building
    
  content_tools:
    - Writing assistants
    - Grammar/style checkers
    - Plagiarism detection
    - AI detection bypass
```

### 3. Development & DevOps
```yaml
categories:
  coding:
    - AI coding assistants
    - IDE plugins
    - Code review tools
    - Testing frameworks
    
  infrastructure:
    - Hosting solutions
    - CDN options
    - Database services
    - Container platforms
    
  security:
    - Vulnerability scanners
    - Auth solutions
    - Encryption tools
```

### 4. Business & Productivity
```yaml
categories:
  project_management:
    - Task trackers
    - Time management
    - Team collaboration
    
  finance:
    - Invoicing
    - Payment processing
    - Accounting automation
    
  marketing:
    - Email platforms
    - Social schedulers
    - Analytics tools
```

## Scouting Protocols

### Daily Quick Scan
```python
async def daily_scan():
    """Quick scan of priority areas."""
    
    priority_searches = [
        "new AI tools {today}",
        "MCP server releases",
        "automation tools trending",
        "WordPress plugin releases",
    ]
    
    for query in priority_searches:
        results = await web_search(query)
        evaluate_and_store(results)
```

### Weekly Deep Dive
```python
async def weekly_deep_dive():
    """Comprehensive scan of all domains."""
    
    # Product Hunt new launches
    ph_results = await scan_product_hunt("ai", "automation", "publishing")
    
    # GitHub trending
    gh_results = await scan_github_trending(
        topics=["mcp", "ai-agent", "automation", "wordpress"]
    )
    
    # Tech news
    news = await scan_tech_news([
        "TechCrunch", "Hacker News", "AI News"
    ])
    
    # Synthesize findings
    return synthesize_discoveries(ph_results, gh_results, news)
```

### Trigger-Based Scouting
```python
def scout_on_trigger(trigger):
    """Scout when specific need detected."""
    
    triggers = {
        "task_failed": scout_alternatives,
        "user_complained": scout_better_tools,
        "manual_workaround": scout_automation,
        "slow_performance": scout_optimizations,
        "missing_feature": scout_solutions,
    }
    
    if trigger in triggers:
        triggers[trigger]()
```

## Relevance Scoring

### For Nick's Ecosystem
```python
def score_relevance(tool, nick_context):
    """Score tool relevance to Nick's needs."""
    
    score = 0
    
    # Publishing relevance
    if tool.category in ["cms", "content", "seo"]:
        score += 30  # Core business
    
    # Automation relevance
    if tool.enables_automation:
        score += 25  # Critical need
    
    # Scale relevance
    if tool.supports_multi_site:
        score += 20  # 17 sites need
    
    # AI integration
    if tool.has_api or tool.has_mcp:
        score += 15  # Agent compatibility
    
    # Time savings
    score += estimate_time_savings(tool) * 10
    
    return score
```

### Priority Matrix
```
                    HIGH IMPACT
                         │
    ┌────────────────────┼────────────────────┐
    │                    │                    │
    │   CONSIDER         │   ADOPT NOW        │
    │   (Monitor)        │   (Prioritize)     │
    │                    │                    │
LOW ├────────────────────┼────────────────────┤ HIGH
EFFORT                   │                    EFFORT
    │                    │                    │
    │   SKIP             │   EVALUATE         │
    │   (Ignore)         │   (Test first)     │
    │                    │                    │
    └────────────────────┼────────────────────┘
                         │
                    LOW IMPACT
```

## Current Recommendations

### Immediate Adoptions
```yaml
adopt_now:
  make_automation:
    tool: Make.com
    reason: "Zero scenarios built - biggest bottleneck"
    impact: "Unlocks entire automation stack"
    effort: "Medium - learning curve"
    
  wordpress_mcp:
    tool: WordPress REST API MCP
    reason: "Direct control of all 17 sites"
    impact: "Eliminates manual WordPress tasks"
    effort: "Low - straightforward setup"
    
  qdrant_memory:
    tool: Qdrant MCP
    reason: "Persistent vector memory across sessions"
    impact: "Claude remembers everything semantically"
    effort: "Medium - requires hosting"
```

### Evaluate These
```yaml
evaluate:
  skyvern:
    tool: Skyvern AI
    reason: "AI-vision browser automation"
    benefit: "Handles CAPTCHAs, adapts to changes"
    cost: "Paid service"
    
  n8n_self_hosted:
    tool: n8n (self-hosted)
    reason: "Alternative to Make.com"
    benefit: "No per-execution costs, full control"
    cost: "Server hosting required"
    
  cursor_ide:
    tool: Cursor AI IDE
    reason: "AI-native code editor"
    benefit: "Better than VS Code for AI coding"
    cost: "Subscription"
```

### Monitor for Future
```yaml
monitor:
  anthropic_computer_use:
    tool: Claude Computer Use API
    reason: "Full computer control"
    status: "Beta - watching for GA"
    
  openai_agents:
    tool: OpenAI Agents SDK
    reason: "Alternative agent framework"
    status: "Evaluating capabilities"
    
  browser_use:
    tool: browser-use
    reason: "Open source browser automation"
    status: "Gaining popularity"
```

## Discovery Search Patterns

### Find Alternatives
```bash
# When current tool has limitations
web_search "{current_tool} alternatives 2025"
web_search "better than {current_tool}"
web_search "{current_tool} vs"
```

### Find New Releases
```bash
# Stay current with releases
web_search "new {category} tools {month} 2025"
web_search "{category} Product Hunt launch"
web_search "GitHub trending {language} {topic}"
```

### Find Solutions
```bash
# When problem encountered
web_search "how to {problem} automation"
web_search "{problem} MCP server"
web_search "AI agent {problem} solution"
```

### Find Best Practices
```bash
# Optimization opportunities
web_search "{workflow} best practices 2025"
web_search "{tool} advanced techniques"
web_search "{domain} automation workflow"
```

## Tool Evaluation Checklist

### Before Recommending
```
☐ Actively maintained (commits in last 30 days)
☐ Good documentation
☐ Community support (issues answered)
☐ Security track record
☐ Reasonable pricing/open source
☐ API or MCP available
☐ Integrates with existing stack
☐ Solves real problem
☐ Time savings justify effort
☐ Scales to needs (17 sites)
```

### Red Flags
```
⚠️ AVOID:
- Abandoned projects (no updates 6+ months)
- No documentation
- Security vulnerabilities
- Vendor lock-in without escape
- Pricing that scales badly
- No API/integration options
- Single point of failure
```

## Innovation Alerts

### Subscribe To
```yaml
sources:
  newsletters:
    - The AI Report
    - TLDR Web Dev
    - Console.dev
    - WordPress Weekly
    
  feeds:
    - Product Hunt AI category
    - GitHub Explore
    - Hacker News frontpage
    - Reddit r/artificial
    
  accounts:
    - @anthropic
    - @OpenAI
    - @veraborisov (AI tools curator)
    - @levelsio (indie hacker tools)
```

### Alert Triggers
```python
alert_on = [
    "new MCP server",
    "browser automation",
    "content automation",
    "WordPress AI",
    "publishing workflow",
    "Make.com alternative",
    "n8n update",
    "AI agent framework",
]
```

## Quick Commands

| Command | Action |
|---------|--------|
| "Find alternatives to X" | Search and compare |
| "What's new in X?" | Scan recent developments |
| "Better tool for X" | Find improvements |
| "Trending in X" | Current hot tools |
| "Should I use X?" | Evaluate specific tool |
| "What am I missing?" | Gap analysis + recommendations |

## Continuous Improvement Loop

```
┌─────────────────────────────────────────────────┐
│                 SCOUT LOOP                      │
├─────────────────────────────────────────────────┤
│                                                 │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐   │
│   │ DISCOVER│ →  │EVALUATE │ →  │RECOMMEND│   │
│   └────┬────┘    └────┬────┘    └────┬────┘   │
│        │              │              │         │
│        └──────────────┼──────────────┘         │
│                       │                        │
│                  ┌────┴────┐                   │
│                  │  ADOPT  │                   │
│                  └────┬────┘                   │
│                       │                        │
│                  ┌────┴────┐                   │
│                  │ MEASURE │                   │
│                  └────┬────┘                   │
│                       │                        │
│                       ▼                        │
│              [Back to DISCOVER]                │
└─────────────────────────────────────────────────┘
```

The scout never stops looking for ways to make the system better.
