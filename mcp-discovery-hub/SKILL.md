---
name: mcp-discovery-hub
description: Automated discovery, evaluation, and recommendation of MCP servers to expand AI agent capabilities. Maintains a curated database of MCP servers, tracks ecosystem updates, evaluates compatibility, and provides installation guidance. Use when user needs to find new MCPs, evaluate MCP options, install MCP servers, or when capability gaps are detected. Triggers include "find MCP", "new MCP", "MCP for", "install MCP", "what MCPs", "recommend MCP", "MCP servers", or when any tool limitation is detected.
---

# MCP Discovery Hub

Automated MCP ecosystem monitoring, evaluation, and integration.

## Core Functions

### 1. Discovery
- Monitor MCP repositories and registries
- Track new server releases
- Identify trending/popular servers
- Detect ecosystem changes

### 2. Evaluation
- Assess server quality and maturity
- Check compatibility with existing setup
- Evaluate security and maintenance
- Compare alternatives

### 3. Recommendation
- Match MCPs to capability gaps
- Prioritize by user needs
- Provide integration guidance
- Track adoption success

## MCP Registry Sources

### Primary Sources
```yaml
official:
  - https://github.com/modelcontextprotocol/servers
  - https://mcp.so/
  - https://smithery.ai/

community:
  - https://github.com/punkpeye/awesome-mcp-servers
  - https://mcpmarket.com/
  - https://glama.ai/mcp/servers

enterprise:
  - AWS Bedrock AgentCore
  - Cloudflare MCP
  - Google Cloud MCP
```

### Discovery Commands
```bash
# Search official registry
web_search "site:github.com/modelcontextprotocol {keyword} MCP"

# Search community
web_search "site:mcp.so {category}"

# Find new releases
web_search "new MCP server {month} {year}"
```

## Curated MCP Database

### Tier 1: Essential (Install First)
| MCP | Category | Purpose | Install |
|-----|----------|---------|---------|
| filesystem | Core | File operations | `npx @anthropic/filesystem-mcp` |
| github | Code | Repo management | `npx @modelcontextprotocol/server-github` |
| brave-search | Search | Web search | `npx @anthropic/brave-search-mcp` |
| browserbase | Browser | Cloud automation | `npx @browserbasehq/mcp-server-browserbase` |
| browser-mcp | Browser | Local automation | `npx @anthropic/browser-mcp` |

### Tier 2: Productivity Boosters
| MCP | Category | Purpose | Install |
|-----|----------|---------|---------|
| notion | Docs | Note management | `npx notion-mcp` |
| google-drive | Storage | Cloud files | `npx @anthropic/google-drive-mcp` |
| slack | Comms | Team messaging | `npx @anthropic/slack-mcp` |
| gmail | Comms | Email | `npx @anthropic/gmail-mcp` |
| calendar | Schedule | Events | `npx @anthropic/google-calendar-mcp` |

### Tier 3: Development
| MCP | Category | Purpose | Install |
|-----|----------|---------|---------|
| docker | Containers | Container control | `npx docker-mcp` |
| kubernetes | Infra | K8s management | `npx @stackloklabs/mkp` |
| postgres | Database | SQL queries | `npx @anthropic/postgres-mcp` |
| supabase | Backend | Full backend | `npx supabase-mcp` |
| vercel | Deploy | Hosting | `npx vercel-mcp` |

### Tier 4: AI Enhancement
| MCP | Category | Purpose | Install |
|-----|----------|---------|---------|
| qdrant | Vector | Semantic memory | `npx qdrant-mcp` |
| pinecone | Vector | Vector search | `npx pinecone-mcp` |
| openai | AI | Model access | `npx openai-mcp` |
| langchain | AI | Chain tools | `npx langchain-mcp` |
| firecrawl | Scraping | Web extraction | `npx @anthropic/firecrawl-mcp` |

### Tier 5: Automation
| MCP | Category | Purpose | Install |
|-----|----------|---------|---------|
| n8n | Workflow | Automation | `npx n8n-mcp` |
| zapier | Workflow | Integrations | `npx zapier-mcp` |
| make | Workflow | Scenarios | `npx make-mcp` |
| cron | Scheduling | Timed tasks | `npx cron-mcp` |

### Tier 6: Content & Media
| MCP | Category | Purpose | Install |
|-----|----------|---------|---------|
| youtube | Video | Video management | `npx youtube-mcp` |
| spotify | Audio | Music/podcasts | `npx spotify-mcp` |
| minimax | Media | TTS/Image gen | `npx minimax-mcp` |
| cloudinary | Media | Asset management | `npx cloudinary-mcp` |

## Nick's Recommended Stack

### For 17-Site Publishing Empire
```json
{
  "mcpServers": {
    "wordpress": {
      "command": "npx",
      "args": ["wordpress-mcp"],
      "env": {"WP_SITES_CONFIG": "/path/to/sites.json"},
      "priority": "CRITICAL",
      "reason": "Direct control of all 17 sites"
    },
    "google-drive": {
      "command": "npx",
      "args": ["@anthropic/google-drive-mcp"],
      "priority": "HIGH",
      "reason": "Asset and content storage"
    },
    "notion": {
      "command": "npx",
      "args": ["notion-mcp"],
      "priority": "HIGH",
      "reason": "Content calendar and planning"
    },
    "browserbase": {
      "command": "npx",
      "args": ["@browserbasehq/mcp-server-browserbase"],
      "env": {
        "BROWSERBASE_API_KEY": "${BROWSERBASE_API_KEY}",
        "BROWSERBASE_PROJECT_ID": "${BROWSERBASE_PROJECT_ID}"
      },
      "priority": "HIGH",
      "reason": "Web automation with stealth"
    },
    "firecrawl": {
      "command": "npx",
      "args": ["@anthropic/firecrawl-mcp"],
      "priority": "MEDIUM",
      "reason": "Advanced content scraping"
    }
  }
}
```

### For KDP Publishing
```json
{
  "mcpServers": {
    "google-drive": {
      "reason": "Manuscript storage"
    },
    "amazon-kdp": {
      "reason": "Direct KDP API access (if available)"
    },
    "canva": {
      "reason": "Cover design automation"
    },
    "browserbase": {
      "reason": "KDP dashboard automation"
    }
  }
}
```

### For Agency Services
```json
{
  "mcpServers": {
    "stripe": {
      "reason": "Payment processing"
    },
    "calendly": {
      "reason": "Booking management"
    },
    "slack": {
      "reason": "Client communication"
    },
    "notion": {
      "reason": "Project management"
    },
    "gmail": {
      "reason": "Email automation"
    }
  }
}
```

## Gap-to-MCP Mapping

When Claude detects → Recommend MCP:
```yaml
gaps:
  "can't access user's files":
    recommend: ["google-drive-mcp", "dropbox-mcp", "filesystem-mcp"]
    priority: HIGH
    
  "can't send notifications":
    recommend: ["slack-mcp", "telegram-mcp", "email-mcp"]
    priority: MEDIUM
    
  "can't remember between sessions":
    recommend: ["qdrant-mcp", "supabase-mcp", "redis-mcp"]
    priority: HIGH
    
  "can't automate workflows":
    recommend: ["n8n-mcp", "zapier-mcp", "make-mcp"]
    priority: CRITICAL
    
  "can't handle CAPTCHAs":
    recommend: ["skyvern-mcp", "browserbase-stealth"]
    priority: MEDIUM
    
  "can't manage containers":
    recommend: ["docker-mcp", "kubernetes-mcp"]
    priority: LOW
    
  "can't query databases":
    recommend: ["postgres-mcp", "mysql-mcp", "mongodb-mcp"]
    priority: MEDIUM
```

## Evaluation Criteria

### Quality Score (0-100)
```python
def evaluate_mcp(server):
    score = 0
    
    # Maintenance (25 pts)
    if updated_within_30_days: score += 25
    elif updated_within_90_days: score += 15
    elif updated_within_year: score += 5
    
    # Documentation (20 pts)
    if has_readme: score += 10
    if has_examples: score += 10
    
    # Community (20 pts)
    score += min(github_stars / 100, 20)
    
    # Security (20 pts)
    if no_known_vulnerabilities: score += 15
    if follows_security_best_practices: score += 5
    
    # Compatibility (15 pts)
    if works_with_claude_desktop: score += 10
    if works_with_claude_code: score += 5
    
    return score
```

### Red Flags
```
⚠️ AVOID if:
- No updates in 6+ months
- No documentation
- Requires excessive permissions
- Known security issues
- Single maintainer, no activity
- Hardcoded credentials in examples
```

## Installation Workflows

### Claude Desktop
```json
// Add to ~/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["package-name"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

### Claude Code
```bash
# Add MCP server
claude mcp add server-name --command "npx package-name"

# With environment variables
claude mcp add server-name --command "npx package-name" \
  --env API_KEY=your-key

# List installed
claude mcp list

# Remove
claude mcp remove server-name
```

### Verification
```bash
# Test connection
claude mcp test server-name

# Check logs
claude mcp logs server-name
```

## Auto-Discovery Protocol

### Weekly Scan
```python
async def weekly_mcp_scan():
    """Scan for new and updated MCPs."""
    
    # Check official registry
    official = await fetch_github_releases("modelcontextprotocol/servers")
    
    # Check community sources
    community = await search_awesome_mcp()
    
    # Check trending
    trending = await search_github_trending("mcp-server")
    
    # Evaluate new servers
    for server in new_servers:
        score = evaluate_mcp(server)
        if score > 70:
            add_to_recommendations(server)
    
    # Generate report
    return generate_discovery_report()
```

### Recommendation Triggers
```yaml
triggers:
  - task_failure_due_to_missing_capability
  - user_mentions_external_tool
  - pattern_detected_needing_automation
  - new_high_quality_mcp_released
  - existing_mcp_deprecated
```

## Quick Commands

| Command | Action |
|---------|--------|
| "Find MCP for X" | Search and recommend |
| "Install X MCP" | Provide installation steps |
| "Compare MCPs for X" | Side-by-side comparison |
| "Update MCP list" | Refresh recommendations |
| "What MCPs do I have?" | List current setup |
| "Best MCPs for my workflow" | Personalized recommendations |

## Resources

- **references/mcp-database.json** - Full curated database
- **references/installation-guides.md** - Detailed setup instructions
- **scripts/mcp_scanner.py** - Auto-discovery tool
- **scripts/mcp_evaluator.py** - Quality assessment
