---
name: browser-automation-superagent
description: Comprehensive browser automation system for AI agents with support for Browserbase MCP, Playwright MCP, Browser MCP, and Skyvern. Enables Claude to control browsers, navigate websites, fill forms, extract data, take screenshots, and perform complex multi-step web workflows. Use when user needs browser automation, web scraping, form filling, screenshot capture, web testing, authenticated browsing, or any task requiring browser control. Triggers include "browse", "navigate", "click", "fill form", "screenshot", "scrape", "extract from website", "login to", "automate browser", "web automation", "open page", or any web interaction requests.
---

# Browser Automation Superagent

Complete browser automation framework for superhuman web capabilities.

## MCP Server Options

### 1. Browserbase MCP (Cloud - Recommended)
Best for: Production automation, stealth mode, session persistence

```json
{
  "mcpServers": {
    "browserbase": {
      "command": "npx",
      "args": ["@browserbasehq/mcp-server-browserbase"],
      "env": {
        "BROWSERBASE_API_KEY": "${BROWSERBASE_API_KEY}",
        "BROWSERBASE_PROJECT_ID": "${BROWSERBASE_PROJECT_ID}"
      }
    }
  }
}
```

**Key Features:**
- Cloud-hosted browsers (no local resources)
- Built-in stealth mode for bot detection
- Session persistence via contexts
- Natural language commands via Stagehand
- Screenshot and video recording
- Proxy support

### 2. Browser MCP (Local - Uses Existing Profile)
Best for: Using existing logins/cookies, personal automation

```json
{
  "mcpServers": {
    "browser-mcp": {
      "command": "npx",
      "args": ["@anthropic/browser-mcp"]
    }
  }
}
```

**Key Features:**
- Uses YOUR existing Chrome profile
- All existing logins preserved
- Your real browser fingerprint
- No separate authentication needed
- Fast local execution

### 3. Playwright MCP (Local - Clean Sessions)
Best for: Testing, development, scripted automation

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-playwright"]
    }
  }
}
```

**Key Features:**
- Full Playwright API access
- Multiple browser engines (Chromium, Firefox, WebKit)
- Network interception
- Mobile emulation
- Parallel execution

### 4. Skyvern MCP (AI-Vision Based)
Best for: Complex sites, CAPTCHAs, changing layouts

```json
{
  "mcpServers": {
    "skyvern": {
      "command": "npx",
      "args": ["skyvern-mcp"]
    }
  }
}
```

**Key Features:**
- Computer vision + LLM understanding
- CAPTCHA solving
- Adaptive to layout changes
- No selectors needed
- 2FA support

## Core Operations

### Navigation
```
browserbase_navigate: Go to URL
browserbase_click: Click element by description
browserbase_fill: Fill input field
browserbase_select: Select dropdown option
browserbase_scroll: Scroll page
browserbase_wait: Wait for element/condition
```

### Data Extraction
```
browserbase_extract: Extract structured data (JSON schema)
browserbase_screenshot: Capture visual state
browserbase_get_text: Get page text content
browserbase_get_html: Get page HTML
```

### Session Management
```
browserbase_create_session: Start new session
browserbase_close_session: End session
browserbase_list_sessions: View active sessions
browserbase_set_context: Use persistent context
```

## Workflow Patterns

### Authenticated Browsing
```
1. Load credentials from vault (credential-vault-manager)
2. Create session with persistent context
3. Navigate to login page
4. Fill credentials using natural language
5. Verify login success
6. Proceed with authenticated actions
7. Save updated session cookies
```

### Data Scraping Pipeline
```
1. Navigate to target URL
2. Wait for dynamic content
3. Extract structured data with schema
4. Paginate through results
5. Aggregate and validate data
6. Export to desired format
```

### Form Automation
```
1. Navigate to form page
2. Map form fields
3. Fill each field with provided data
4. Handle dropdowns, checkboxes, radios
5. Upload files if needed
6. Submit and verify success
7. Screenshot confirmation
```

### Multi-Site Workflow
```
1. Plan site order for efficiency
2. Maintain separate sessions per site
3. Execute parallel where possible
4. Pass data between sites
5. Aggregate results
6. Handle failures gracefully
```

## Integration with Credential Vault

Use with `credential-vault-manager` skill:

```python
# Pseudo-workflow
1. vault.load_cookies("site.com")  # Get stored cookies
2. browser.create_session(cookies)  # Inject into browser
3. browser.navigate("https://site.com")
4. # Already logged in via cookies
5. # Perform authenticated actions
6. vault.save_cookies("site.com", browser.get_cookies())  # Update
```

## Error Handling

| Error | Recovery Strategy |
|-------|-------------------|
| Element not found | Wait longer, try alternative selector, use vision |
| CAPTCHA detected | Route to CAPTCHA service, try Skyvern |
| Login failed | Check credentials, try alternative auth |
| Rate limited | Backoff, rotate proxy, slow down |
| Session expired | Re-authenticate, refresh context |
| Page timeout | Retry with longer timeout, check connectivity |

## Best Practices

### Session Persistence
- Use Browserbase contexts for login persistence
- Store cookies after successful auth
- Check session validity before operations
- Refresh sessions proactively

### Stealth Mode
- Enable proxy rotation for scraping
- Randomize timing between actions
- Use residential proxies when needed
- Avoid patterns that trigger detection

### Performance
- Reuse sessions when possible
- Batch similar operations
- Use headless mode for speed
- Minimize screenshot frequency

### Reliability
- Always verify action success
- Implement retry logic
- Log all operations
- Screenshot on errors

## Quick Reference

| Task | Command Pattern |
|------|-----------------|
| Login | navigate → fill username → fill password → click submit |
| Extract table | navigate → wait for table → extract with schema |
| Fill form | navigate → fill each field → submit → screenshot |
| Screenshot | navigate → wait → screenshot |
| Download file | navigate → click download → wait for file |

## Environment Setup

Required environment variables:
```bash
# Browserbase
BROWSERBASE_API_KEY=your_key
BROWSERBASE_PROJECT_ID=your_project

# Optional: Custom model for Stagehand
ANTHROPIC_API_KEY=your_key  # For Claude-powered navigation
```

## Resources

- **references/mcp-configs.json** - Ready-to-use MCP configurations
- **references/selectors-guide.md** - Natural language selector tips
- **scripts/session_manager.py** - Session persistence utilities
- **scripts/cookie_injector.py** - Cookie loading helper
