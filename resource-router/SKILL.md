# RESOURCE ROUTER SKILL
## Meta-Skill for Automatic Prompt-to-Resource Routing
### Version 1.0

---

## Overview

This skill ensures Claude **ALWAYS** uses the right tools for every task. It automatically routes prompts to the appropriate:
- Skills
- MCPs (Model Context Protocol servers)
- APIs
- Research tools
- File operations

**AUTO-ACTIVATE**: This skill should run on EVERY message to determine optimal resource usage.

---

## Skill Triggers

### Document Creation
```yaml
docx/word/document:
  - /mnt/skills/public/docx/SKILL.md

xlsx/spreadsheet/excel:
  - /mnt/skills/public/xlsx/SKILL.md

pptx/presentation/slides:
  - /mnt/skills/public/pptx/SKILL.md

pdf:
  - /mnt/skills/public/pdf/SKILL.md
```

### WordPress Operations
```yaml
wordpress/plugin/theme:
  - /mnt/skills/user/wordpress-empire-system/SKILL.md
  - /mnt/skills/user/wordpress-core/SKILL.md

gutenberg/block:
  - /mnt/skills/user/wordpress-blocks/SKILL.md

security/hardening:
  - /mnt/skills/user/wordpress-security-patterns/SKILL.md

accessibility/a11y:
  - /mnt/skills/user/wordpress-accessibility-patterns/SKILL.md
```

### Automation
```yaml
n8n/workflow/automation:
  - /mnt/skills/user/n8n-master-architect/SKILL.md

zimmwriter/bulk/csv:
  - /mnt/skills/user/zimmwriter-control/SKILL.md

parallel/batch/all sites:
  - /mnt/skills/user/multi-task-orchestrator/SKILL.md
```

### Browser Automation
```yaml
browse/scrape/navigate:
  - /mnt/skills/user/browser-automation-superagent/SKILL.md

steel/fallback/when MCP fails:
  - /mnt/skills/user/steel-browser-automation/SKILL.md

ai browser/browseruse:
  - /mnt/skills/user/browseruse-ai-agent/SKILL.md

systeme.io/email sequence/funnel:
  - /mnt/skills/user/systeme-io-browser-automation/SKILL.md
```

### Design & Development
```yaml
design tokens/v0 prompt/visual:
  - /mnt/skills/user/visual-to-code-pipeline/SKILL.md

figma.com URL:
  - Figma MCP: get_design_context

frontend/ui/component:
  - /mnt/skills/public/frontend-design/SKILL.md
```

### Content & SEO
```yaml
witchcraft/substack/coven:
  - /mnt/skills/user/witchcraft-substack-voice/SKILL.md
  - /mnt/skills/user/coven-keeper-agent/SKILL.md

affiliate/amazon/product:
  - /mnt/skills/user/affiliate-hunter-agent/SKILL.md

seo/llm optimizer:
  - /mnt/skills/user/seo-llm-optimizer-tests/SKILL.md
```

### Meta Operations
```yaml
create skill:
  - /mnt/skills/examples/skill-creator/SKILL.md
  - /mnt/skills/user/auto-skill-generator/SKILL.md

find mcp:
  - Search Composio for available MCPs

credentials/api keys:
  - /mnt/skills/user/credential-vault-manager/SKILL.md

site audit/design check:
  - /mnt/skills/user/site-design-auditor/SKILL.md

code standards/linting:
  - /mnt/skills/user/code-standards-checker/SKILL.md
```

---

## MCP Routing

### Available MCPs
```yaml
Figma:
  Trigger: figma.com URLs, design context
  Tool: get_design_context
  Use: Extract design information from Figma files

Canva:
  Trigger: canva.com URLs, design assets
  Tool: Canva MCP tools
  Use: Access Canva designs

Browserbase:
  Trigger: Browser automation, screenshots
  Tools: navigate, act, extract, screenshot
  Use: Browser-based automation

Composio:
  Trigger: Third-party integrations
  Tools: COMPOSIO_SEARCH_TOOLS, COMPOSIO_EXECUTE_TOOL
  Use: Connect to 500+ apps

Context7:
  Trigger: Library documentation
  Tools: resolve-library-id, get-library-docs
  Use: Get up-to-date docs

Exa:
  Trigger: Research, web search
  Tools: web_search_exa, get_code_context_exa
  Use: AI-powered search

Memory:
  Trigger: Remember, recall, knowledge graph
  Tools: create_entities, search_nodes
  Use: Persistent memory storage
```

---

## Research Tools

### When to Use What

```yaml
General Research:
  Tool: Exa web_search_exa
  Best For: Broad topics, trends, news

Code Documentation:
  Tool: Context7 get-library-docs
  Best For: API docs, library reference

Competitor Analysis:
  Tool: Exa + Browserbase
  Best For: Site analysis, feature comparison

Product Research:
  Tool: Amazon PAAPI + Exa
  Best For: Product data, reviews
```

---

## API Priority

When multiple options exist, use this priority:

```
1. MCP (fastest, most integrated)
2. Direct API (reliable, documented)
3. Steel.dev Browser (simple automation)
4. BrowserUse AI (complex/unknown tasks)
```

---

## Nick's Defaults

Apply these to EVERY response:

```yaml
Execution:
  - Bold, decisive, no permission asking
  - Full creative control
  - Modern tech Picasso design philosophy

Output:
  - Files over inline for substantial content
  - Professional quality, comprehensive scope
  - Download links for deliverables

Build:
  - 300-line chunks for large files
  - Stop before token limits
  - Push to GitHub at every opportunity

Research:
  - Search trending/viral before content
  - Reference past chats when relevant
  - Compound knowledge session over session
```

---

## Site Voice Reference

Apply correct voice based on site:

```yaml
witchcraftforbeginners.com:
  Voice: Mystical warmth
  Tone: Like a wise friend sharing ancient knowledge
  
smarthomewizards.com:
  Voice: Tech authority
  Tone: Expert but approachable

aiinactionhub.com:
  Voice: Forward analyst
  Tone: Insightful, trend-focused

mythicalarchives.com:
  Voice: Scholarly wonder
  Tone: Research-backed storytelling

family-flourish.com:
  Voice: Nurturing guide
  Tone: Supportive, practical

bulletjournals.net:
  Voice: Creative organizer
  Tone: Inspiring yet grounded
```

---

## Current Priorities

Always keep these in mind:

```yaml
P0 - Urgent:
  1. Automate all 16 sites (design + content)
  2. Scale KDP book publishing
  3. Launch agency services

P1 - High:
  - Content automation pipeline
  - n8n workflow optimization
  - Site design consistency

P2 - Standard:
  - SEO optimization
  - Content calendar execution
  - Maintenance tasks
```

---

## Auto-Routing Logic

```python
def route_prompt(prompt: str) -> List[str]:
    """
    Automatically determine which skills/tools to use
    
    Returns list of resources to load/use
    """
    resources = []
    prompt_lower = prompt.lower()
    
    # Document triggers
    if any(w in prompt_lower for w in ['docx', 'word', 'document']):
        resources.append('/mnt/skills/public/docx/SKILL.md')
    if any(w in prompt_lower for w in ['xlsx', 'spreadsheet', 'excel']):
        resources.append('/mnt/skills/public/xlsx/SKILL.md')
    if any(w in prompt_lower for w in ['pptx', 'presentation', 'slides']):
        resources.append('/mnt/skills/public/pptx/SKILL.md')
    if 'pdf' in prompt_lower:
        resources.append('/mnt/skills/public/pdf/SKILL.md')
    
    # WordPress triggers
    if any(w in prompt_lower for w in ['wordpress', 'plugin', 'theme', 'wp']):
        resources.append('/mnt/skills/user/wordpress-empire-system/SKILL.md')
    
    # Automation triggers
    if any(w in prompt_lower for w in ['n8n', 'workflow', 'automation']):
        resources.append('/mnt/skills/user/n8n-master-architect/SKILL.md')
    
    # Browser triggers
    if any(w in prompt_lower for w in ['browser', 'scrape', 'navigate']):
        resources.append('/mnt/skills/user/browser-automation-superagent/SKILL.md')
    
    # Systeme.io triggers
    if any(w in prompt_lower for w in ['systeme', 'email sequence', 'funnel']):
        resources.append('/mnt/skills/user/systeme-io-browser-automation/SKILL.md')
    
    # Design triggers
    if any(w in prompt_lower for w in ['design token', 'v0', 'visual']):
        resources.append('/mnt/skills/user/visual-to-code-pipeline/SKILL.md')
    
    # Figma URLs
    if 'figma.com' in prompt_lower:
        resources.append('MCP:Figma:get_design_context')
    
    return resources
```

---

## Quick Commands

```yaml
# View all skills
view /mnt/skills/user

# Read specific skill
view /mnt/skills/user/[skill-name]/SKILL.md

# Memory operations
memory_user_edits command="view"

# Search past chats
conversation_search query="[keywords]"

# Recent chats
recent_chats n=10
```

---

## Installation

To add to Claude Desktop `systemPrompt`:

```
<resource_router>
AUTO-ROUTE ON EVERY MESSAGE: Parse intent → Match skills → Pre-load → Execute fully

ALWAYS read /mnt/skills/user/resource-router/SKILL.md at conversation start.

SKILL TRIGGERS:
- docx/xlsx/pptx/pdf → /mnt/skills/public/[type]/SKILL.md
- wordpress/plugin/theme → /mnt/skills/user/wordpress-empire-system/SKILL.md
- n8n/workflow → /mnt/skills/user/n8n-master-architect/SKILL.md
- browser/scrape → /mnt/skills/user/browser-automation-superagent/SKILL.md
- figma.com → Figma MCP get_design_context
- create skill → /mnt/skills/examples/skill-creator/SKILL.md

NICK'S DEFAULTS:
- Bold execution, no permission asking
- Files over inline for substantial content
- Professional quality, comprehensive scope
</resource_router>
```

---

*Resource Router Skill*
*Version 1.0 | Recovered 2025-12-15*
*Meta-skill for automatic prompt-to-resource routing*
