# STEEL.DEV BROWSER AUTOMATION SKILL
## Fallback System for When APIs Fail
### Version 1.0

---

## Overview

Steel.dev provides cloud browser automation that works when:
- MCP connections fail or timeout
- APIs don't support needed functionality
- Manual tasks need automation
- Complex multi-step workflows are required
- Authentication is needed that APIs can't handle

**Trigger Keywords:** steel fallback, browser automation, automate browser, click on, fill form, when MCP fails

---

## Credentials

```yaml
Steel.dev:
  API Key: ste-A43JGQkLsnI609gNUXatQ83QB88Aj2JHOyrhvdaax8AxCWwSI0sn3VD01ToP4RjxM5POgbxoDhaEcwmsxshm6BFtKYS8J2ErKFy
  Base URL: https://api.steel.dev
  
BrowserUse:
  API Key: bu_YUQ0ZqtuWge86lOZUaWiZtK_rG6PkCNElONERb9Jzgs
  Base URL: https://api.browseruse.com
```

---

## Core Concepts

### When to Use Steel.dev (Fallback Triggers)

```yaml
Automatic Fallback Triggers:
  - MCP connection timeout (>30 seconds)
  - MCP returns error 3 consecutive times
  - API endpoint returns 401/403/500
  - Rate limit exceeded
  - Feature not available via API
  
Manual Trigger Keywords:
  - "use browser to..."
  - "automate the browser..."
  - "steel fallback..."
  - "browser automation..."
  - "click on..."
  - "fill form..."
```

### Steel.dev vs BrowserUse

```yaml
Steel.dev:
  Best For:
    - Simple, repeatable tasks
    - Fast execution
    - Form filling
    - Data extraction
    - Screenshot capture
  
BrowserUse:
  Best For:
    - Complex multi-step workflows
    - AI-guided navigation
    - Dynamic page handling
    - When you don't know exact selectors
    - Research and exploration
```

---

## API Reference

### Create Browser Session

```python
import requests

STEEL_API_KEY = "ste-A43JGQkLsnI609gNUXatQ83QB88Aj2JHOyrhvdaax8AxCWwSI0sn3VD01ToP4RjxM5POgbxoDhaEcwmsxshm6BFtKYS8J2ErKFy"

def create_steel_session():
    """Create a new Steel.dev browser session"""
    response = requests.post(
        "https://api.steel.dev/v1/sessions",
        headers={
            "Authorization": f"Bearer {STEEL_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "browser": "chromium",
            "blockAds": True,
            "solveCaptcha": True,
            "proxy": "residential"  # Options: residential, datacenter, none
        }
    )
    return response.json()
```

### Navigate to URL

```python
def navigate(session_id: str, url: str):
    """Navigate browser to a URL"""
    response = requests.post(
        f"https://api.steel.dev/v1/sessions/{session_id}/navigate",
        headers={"Authorization": f"Bearer {STEEL_API_KEY}"},
        json={"url": url}
    )
    return response.json()
```

### Click Element

```python
def click(session_id: str, selector: str):
    """Click an element by CSS selector"""
    response = requests.post(
        f"https://api.steel.dev/v1/sessions/{session_id}/click",
        headers={"Authorization": f"Bearer {STEEL_API_KEY}"},
        json={"selector": selector}
    )
    return response.json()
```

### Type Text

```python
def type_text(session_id: str, selector: str, text: str):
    """Type text into an input field"""
    response = requests.post(
        f"https://api.steel.dev/v1/sessions/{session_id}/type",
        headers={"Authorization": f"Bearer {STEEL_API_KEY}"},
        json={
            "selector": selector,
            "text": text
        }
    )
    return response.json()
```

### Extract Data

```python
def extract(session_id: str, selector: str):
    """Extract text content from elements"""
    response = requests.post(
        f"https://api.steel.dev/v1/sessions/{session_id}/extract",
        headers={"Authorization": f"Bearer {STEEL_API_KEY}"},
        json={"selector": selector}
    )
    return response.json()
```

### Screenshot

```python
def screenshot(session_id: str):
    """Take a screenshot of the current page"""
    response = requests.post(
        f"https://api.steel.dev/v1/sessions/{session_id}/screenshot",
        headers={"Authorization": f"Bearer {STEEL_API_KEY}"}
    )
    return response.json()  # Returns base64 image
```

### Close Session

```python
def close_session(session_id: str):
    """Close the browser session"""
    response = requests.delete(
        f"https://api.steel.dev/v1/sessions/{session_id}",
        headers={"Authorization": f"Bearer {STEEL_API_KEY}"}
    )
    return response.json()
```

---

## Complete Class Implementation

```python
import requests
import time
from typing import Optional, Dict, Any, List

class SteelBrowserAutomation:
    """
    Steel.dev Browser Automation for WordPress Empire
    Fallback when MCP/API fails
    """
    
    def __init__(self):
        self.api_key = "ste-A43JGQkLsnI609gNUXatQ83QB88Aj2JHOyrhvdaax8AxCWwSI0sn3VD01ToP4RjxM5POgbxoDhaEcwmsxshm6BFtKYS8J2ErKFy"
        self.base_url = "https://api.steel.dev/v1"
        self.session_id = None
        
    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def start_session(self, proxy: str = "residential") -> str:
        """Start a new browser session"""
        response = requests.post(
            f"{self.base_url}/sessions",
            headers=self._headers(),
            json={
                "browser": "chromium",
                "blockAds": True,
                "solveCaptcha": True,
                "proxy": proxy
            }
        )
        data = response.json()
        self.session_id = data.get("sessionId")
        return self.session_id
    
    def navigate(self, url: str) -> Dict[str, Any]:
        """Navigate to URL"""
        return requests.post(
            f"{self.base_url}/sessions/{self.session_id}/navigate",
            headers=self._headers(),
            json={"url": url}
        ).json()
    
    def click(self, selector: str) -> Dict[str, Any]:
        """Click element by CSS selector"""
        return requests.post(
            f"{self.base_url}/sessions/{self.session_id}/click",
            headers=self._headers(),
            json={"selector": selector}
        ).json()
    
    def type(self, selector: str, text: str) -> Dict[str, Any]:
        """Type text into input field"""
        return requests.post(
            f"{self.base_url}/sessions/{self.session_id}/type",
            headers=self._headers(),
            json={"selector": selector, "text": text}
        ).json()
    
    def extract(self, selector: str) -> List[str]:
        """Extract text from elements"""
        response = requests.post(
            f"{self.base_url}/sessions/{self.session_id}/extract",
            headers=self._headers(),
            json={"selector": selector}
        ).json()
        return response.get("data", [])
    
    def screenshot(self, save_path: Optional[str] = None) -> str:
        """Take screenshot, optionally save to file"""
        response = requests.post(
            f"{self.base_url}/sessions/{self.session_id}/screenshot",
            headers=self._headers()
        ).json()
        
        base64_data = response.get("data")
        if save_path and base64_data:
            import base64
            with open(save_path, 'wb') as f:
                f.write(base64.b64decode(base64_data))
        
        return base64_data
    
    def wait(self, seconds: float):
        """Wait for page to load"""
        time.sleep(seconds)
    
    def close(self):
        """Close the browser session"""
        if self.session_id:
            requests.delete(
                f"{self.base_url}/sessions/{self.session_id}",
                headers=self._headers()
            )
            self.session_id = None
    
    def __enter__(self):
        self.start_session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```

---

## WordPress Admin Automation Examples

### Login to WordPress Admin

```python
def wp_login(steel: SteelBrowserAutomation, site_url: str, username: str, password: str):
    """Login to WordPress admin"""
    steel.navigate(f"{site_url}/wp-login.php")
    steel.wait(2)
    
    steel.type("#user_login", username)
    steel.type("#user_pass", password)
    steel.click("#wp-submit")
    
    steel.wait(3)
    return steel.extract(".wrap h1")  # Should show "Dashboard"
```

### Create a New Post

```python
def wp_create_post(steel: SteelBrowserAutomation, title: str, content: str):
    """Create a new WordPress post via browser"""
    steel.navigate(f"{site_url}/wp-admin/post-new.php")
    steel.wait(3)
    
    # Enter title
    steel.type("#title", title)
    
    # Switch to text editor if needed
    steel.click("#content-html")  # Switch to text mode
    steel.wait(1)
    
    # Enter content
    steel.type("#content", content)
    
    # Publish
    steel.click("#publish")
    steel.wait(3)
    
    return "Post created"
```

### Install Plugin

```python
def wp_install_plugin(steel: SteelBrowserAutomation, plugin_slug: str):
    """Install a WordPress plugin via browser"""
    steel.navigate(f"{site_url}/wp-admin/plugin-install.php?s={plugin_slug}&tab=search")
    steel.wait(3)
    
    # Click install on first result
    steel.click(f".plugin-card-{plugin_slug} .install-now")
    steel.wait(10)
    
    # Activate
    steel.click(f".plugin-card-{plugin_slug} .activate-now")
    steel.wait(3)
    
    return "Plugin installed and activated"
```

---

## Systeme.io Browser Automation

### Login to Systeme.io

```python
def systeme_login(steel: SteelBrowserAutomation, email: str, password: str):
    """Login to Systeme.io dashboard"""
    steel.navigate("https://systeme.io/dashboard/en/login")
    steel.wait(2)
    
    steel.type("input[name='email']", email)
    steel.type("input[name='password']", password)
    steel.click("button[type='submit']")
    
    steel.wait(5)
    return steel.extract(".dashboard-title")
```

### Create Email Sequence (API Can't Do This!)

```python
def systeme_create_email(steel: SteelBrowserAutomation, subject: str, content: str):
    """Create email in Systeme.io (requires browser automation)"""
    steel.navigate("https://systeme.io/dashboard/en/emails")
    steel.wait(3)
    
    # Click create new
    steel.click("[data-action='create-email']")
    steel.wait(2)
    
    # Fill in details
    steel.type("input[name='subject']", subject)
    
    # Switch to text editor
    steel.click(".editor-switch-text")
    steel.type(".email-content-editor", content)
    
    # Save
    steel.click(".save-email")
    steel.wait(3)
    
    return "Email created"
```

---

## n8n Integration

```json
{
  "name": "WordPress Browser Fallback",
  "nodes": [
    {
      "name": "Check Method",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.useBrowser }}",
              "operation": "equals",
              "value2": "true"
            }
          ]
        }
      }
    },
    {
      "name": "Steel Start Session",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.steel.dev/v1/sessions",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer ste-A43JGQkLsnI609gNUXatQ83QB88Aj2JHOyrhvdaax8AxCWwSI0sn3VD01ToP4RjxM5POgbxoDhaEcwmsxshm6BFtKYS8J2ErKFy"
        },
        "body": {
          "browser": "chromium",
          "blockAds": true
        }
      }
    }
  ]
}
```

---

## Fallback Decision Tree

```
Task Received
    │
    ▼
Try MCP Connection
    │
    ├── Success → Execute via MCP
    │
    └── Fail (3x) → Try Direct API
                        │
                        ├── Success → Execute via API
                        │
                        └── Fail (3x) → Use Steel.dev Browser
                                            │
                                            ├── Success → Task Complete
                                            │
                                            └── Fail → Use BrowserUse AI Agent
                                                          │
                                                          └── AI figures it out
```

---

## Site-Specific WordPress Credentials

Reference the site registry for WordPress admin logins:

| Site | WP User | Login URL |
|------|---------|-----------|
| SmartHomeWizards | SmartHomeGuru | smarthomewizards.com/wp-admin |
| MythicalArchives | ArcaneArchivist | mythicalarchives.com/wp-admin |
| WitchcraftForBeginners | MoonlightMystic | witchcraftforbeginners.com/wp-admin |
| ... | ... | ... |

---

## Quick Commands

```yaml
# Start automation
steel = SteelBrowserAutomation()
steel.start_session()

# WordPress login
steel.navigate("https://yoursite.com/wp-login.php")
steel.type("#user_login", "username")
steel.type("#user_pass", "password")
steel.click("#wp-submit")

# Take screenshot
steel.screenshot("current_page.png")

# Close when done
steel.close()
```

---

*Steel.dev Browser Automation Skill*
*Version 1.0 | Recovered 2025-12-15*
*Use when APIs fail - never do manual tasks again*
