# SYSTEME.IO BROWSER AUTOMATION SKILL
## Comprehensive Browser Automation for Email Marketing
### Version 1.0

---

## Overview

Systeme.io is a powerful all-in-one marketing platform, but its API has LIMITED functionality. This skill enables browser automation for operations the API **cannot** do:

### API Can Do ✅
- Manage contacts
- Add/remove tags
- Basic list operations

### API CANNOT Do (Requires Browser) ❌
- Create/edit blog posts
- Create/edit funnel pages
- Create/edit email sequences/campaigns
- Manage workflows & automation rules
- Upload media
- Create/edit products
- Build sales funnels
- Design email templates

**Trigger Keywords:** systeme.io, email sequence, funnel, automation rules, newsletter, campaign

---

## Credentials

```yaml
Systeme.io:
  API Key: 82tyjz6r3hzl5kq6qyl9ix9rusrkh3j7c8abj0fxaotfu4ruqftksnvuwxujhloc
  API Base: https://api.systeme.io/api/
  Login URL: https://systeme.io/dashboard/en/login
  Email: aiautomationblueprint@gmail.com
  Password: Ashlynn.09
```

---

## Dashboard URL Patterns

```yaml
Login: https://systeme.io/dashboard/en/login
Dashboard: https://systeme.io/dashboard
Contacts: https://systeme.io/dashboard/en/contacts
Tags: https://systeme.io/dashboard/en/tags
Emails: https://systeme.io/dashboard/en/emails
Campaigns: https://systeme.io/dashboard/en/campaigns
Funnels: https://systeme.io/dashboard/en/funnels
Blog: https://systeme.io/dashboard/en/blog
Products: https://systeme.io/dashboard/en/products
Automation: https://systeme.io/dashboard/en/automation-rules
```

---

## Element Selectors Reference

### Login Page
```css
Email Input: input[name="email"], input[type="email"]
Password Input: input[name="password"], input[type="password"]
Login Button: button[type="submit"], .login-button
```

### Dashboard Navigation
```css
Sidebar Menu: .sidebar-menu, .dashboard-nav
Email Section: a[href*="/emails"], .nav-emails
Funnels Section: a[href*="/funnels"], .nav-funnels
Blog Section: a[href*="/blog"], .nav-blog
Contacts Section: a[href*="/contacts"], .nav-contacts
```

### Email Editor
```css
Subject Field: input[name="subject"], .email-subject-input
Content Editor: .tiptap-editor, .ProseMirror, [contenteditable="true"]
Save Button: .save-button, button:contains("Save")
Send Test: .send-test-button
```

### Campaign Builder
```css
Create Button: .create-campaign, button:contains("Create")
Campaign Name: input[name="name"], .campaign-name-input
Email List: .email-list-dropdown, select[name="list"]
Schedule: .schedule-picker, input[type="datetime-local"]
```

---

## Complete Python Implementation

```python
import time
import requests
from typing import Optional, Dict, Any, List
from dataclasses import dataclass

@dataclass
class SystemeConfig:
    api_key: str = "82tyjz6r3hzl5kq6qyl9ix9rusrkh3j7c8abj0fxaotfu4ruqftksnvuwxujhloc"
    email: str = "aiautomationblueprint@gmail.com"
    password: str = "Ashlynn.09"
    base_url: str = "https://api.systeme.io/api"
    dashboard_url: str = "https://systeme.io/dashboard"


class SystemeBrowserAutomation:
    """
    Complete Systeme.io automation via browser
    For operations the API cannot handle
    """
    
    def __init__(self, config: SystemeConfig = None):
        self.config = config or SystemeConfig()
        self.steel_api_key = "ste-A43JGQkLsnI609gNUXatQ83QB88Aj2JHOyrhvdaax8AxCWwSI0sn3VD01ToP4RjxM5POgbxoDhaEcwmsxshm6BFtKYS8J2ErKFy"
        self.session_id = None
        self.logged_in = False
    
    def _steel_request(self, endpoint: str, method: str = "POST", json_data: dict = None):
        """Make request to Steel.dev API"""
        url = f"https://api.steel.dev/v1{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.steel_api_key}",
            "Content-Type": "application/json"
        }
        
        if method == "POST":
            return requests.post(url, headers=headers, json=json_data).json()
        elif method == "DELETE":
            return requests.delete(url, headers=headers).json()
        elif method == "GET":
            return requests.get(url, headers=headers).json()
    
    def start_browser(self):
        """Start Steel.dev browser session"""
        result = self._steel_request("/sessions", json_data={
            "browser": "chromium",
            "blockAds": True,
            "solveCaptcha": True
        })
        self.session_id = result.get("sessionId")
        return self.session_id
    
    def navigate(self, url: str):
        """Navigate to URL"""
        return self._steel_request(
            f"/sessions/{self.session_id}/navigate",
            json_data={"url": url}
        )
    
    def click(self, selector: str):
        """Click element"""
        return self._steel_request(
            f"/sessions/{self.session_id}/click",
            json_data={"selector": selector}
        )
    
    def type_text(self, selector: str, text: str):
        """Type text into input"""
        return self._steel_request(
            f"/sessions/{self.session_id}/type",
            json_data={"selector": selector, "text": text}
        )
    
    def extract(self, selector: str) -> List[str]:
        """Extract text from elements"""
        result = self._steel_request(
            f"/sessions/{self.session_id}/extract",
            json_data={"selector": selector}
        )
        return result.get("data", [])
    
    def screenshot(self) -> str:
        """Take screenshot (returns base64)"""
        result = self._steel_request(f"/sessions/{self.session_id}/screenshot")
        return result.get("data")
    
    def wait(self, seconds: float):
        """Wait for page to load"""
        time.sleep(seconds)
    
    def close_browser(self):
        """Close browser session"""
        if self.session_id:
            self._steel_request(f"/sessions/{self.session_id}", method="DELETE")
            self.session_id = None
            self.logged_in = False
    
    # ==================== LOGIN ====================
    
    def login(self) -> bool:
        """Login to Systeme.io dashboard"""
        if not self.session_id:
            self.start_browser()
        
        self.navigate("https://systeme.io/dashboard/en/login")
        self.wait(3)
        
        # Enter credentials
        self.type_text("input[name='email']", self.config.email)
        self.type_text("input[name='password']", self.config.password)
        self.click("button[type='submit']")
        
        self.wait(5)
        
        # Verify login by checking for dashboard element
        dashboard_check = self.extract(".dashboard-title, .user-menu")
        self.logged_in = len(dashboard_check) > 0
        
        return self.logged_in
    
    # ==================== EMAIL OPERATIONS ====================
    
    def create_email(self, subject: str, content: str, from_name: str = None) -> Dict[str, Any]:
        """
        Create a new email (API cannot do this!)
        
        Args:
            subject: Email subject line
            content: Email body content (HTML or plain text)
            from_name: Sender name (optional)
        """
        if not self.logged_in:
            self.login()
        
        self.navigate(f"{self.config.dashboard_url}/en/emails")
        self.wait(2)
        
        # Click create new email
        self.click("button:contains('Create'), .create-email-btn")
        self.wait(2)
        
        # Fill in subject
        self.type_text("input[name='subject']", subject)
        
        # Fill in from name if provided
        if from_name:
            self.type_text("input[name='from_name']", from_name)
        
        # Click into content editor and fill
        self.click(".tiptap-editor, .ProseMirror")
        self.wait(0.5)
        
        # For rich text, we may need to use keyboard commands or paste
        self._steel_request(
            f"/sessions/{self.session_id}/evaluate",
            json_data={
                "expression": f"document.querySelector('.ProseMirror').innerHTML = `{content}`"
            }
        )
        
        # Save
        self.click("button:contains('Save'), .save-button")
        self.wait(2)
        
        return {"success": True, "subject": subject}
    
    def create_email_sequence(self, name: str, emails: List[Dict[str, str]], delays: List[int] = None) -> Dict[str, Any]:
        """
        Create an email sequence/campaign
        
        Args:
            name: Sequence name
            emails: List of {"subject": "", "content": ""} dicts
            delays: Days between emails (default: [0, 1, 3, 7, ...])
        """
        if not self.logged_in:
            self.login()
        
        if delays is None:
            delays = [0] + [i * 2 for i in range(1, len(emails))]  # 0, 2, 4, 6...
        
        self.navigate(f"{self.config.dashboard_url}/en/campaigns")
        self.wait(2)
        
        # Create campaign
        self.click("button:contains('Create'), .create-campaign-btn")
        self.wait(2)
        
        self.type_text("input[name='name']", name)
        self.click("button:contains('Create'), .confirm-create")
        self.wait(2)
        
        # Add each email
        for i, email in enumerate(emails):
            self.click("button:contains('Add Email'), .add-email-btn")
            self.wait(2)
            
            self.type_text("input[name='subject']", email["subject"])
            
            # Set delay
            if i > 0:
                delay_input = f"input[name='delay'], .delay-input"
                self.type_text(delay_input, str(delays[i]))
            
            # Fill content
            self.click(".tiptap-editor, .ProseMirror")
            self._steel_request(
                f"/sessions/{self.session_id}/evaluate",
                json_data={
                    "expression": f"document.querySelector('.ProseMirror').innerHTML = `{email['content']}`"
                }
            )
            
            self.click("button:contains('Save'), .save-email")
            self.wait(2)
        
        return {"success": True, "name": name, "email_count": len(emails)}
    
    # ==================== FUNNEL OPERATIONS ====================
    
    def create_funnel_page(self, funnel_id: str, page_name: str, page_type: str = "opt-in") -> Dict[str, Any]:
        """
        Create a new funnel page
        
        Args:
            funnel_id: ID of existing funnel
            page_name: Name for the new page
            page_type: "opt-in", "sales", "thank-you", etc.
        """
        if not self.logged_in:
            self.login()
        
        self.navigate(f"{self.config.dashboard_url}/en/funnels/{funnel_id}")
        self.wait(3)
        
        self.click("button:contains('Add Page'), .add-page-btn")
        self.wait(2)
        
        # Select page type
        self.click(f".page-type-{page_type}, [data-type='{page_type}']")
        self.wait(1)
        
        self.type_text("input[name='name']", page_name)
        self.click("button:contains('Create'), .create-page-btn")
        
        self.wait(3)
        
        return {"success": True, "page_name": page_name, "page_type": page_type}
    
    # ==================== BLOG OPERATIONS ====================
    
    def create_blog_post(self, title: str, content: str, category: str = None, publish: bool = False) -> Dict[str, Any]:
        """
        Create a blog post (API cannot do this!)
        
        Args:
            title: Post title
            content: Post content (HTML)
            category: Category name (optional)
            publish: Whether to publish immediately
        """
        if not self.logged_in:
            self.login()
        
        self.navigate(f"{self.config.dashboard_url}/en/blog/posts")
        self.wait(2)
        
        self.click("button:contains('Create'), .create-post-btn")
        self.wait(2)
        
        self.type_text("input[name='title']", title)
        
        if category:
            self.click(".category-dropdown, select[name='category']")
            self.click(f"option:contains('{category}')")
        
        # Fill content
        self.click(".tiptap-editor, .ProseMirror")
        self._steel_request(
            f"/sessions/{self.session_id}/evaluate",
            json_data={
                "expression": f"document.querySelector('.ProseMirror').innerHTML = `{content}`"
            }
        )
        
        if publish:
            self.click("button:contains('Publish'), .publish-btn")
        else:
            self.click("button:contains('Save'), .save-draft-btn")
        
        self.wait(2)
        
        return {"success": True, "title": title, "published": publish}
    
    # ==================== AUTOMATION RULES ====================
    
    def create_automation_rule(
        self,
        name: str,
        trigger: str,
        action: str,
        trigger_config: Dict = None,
        action_config: Dict = None
    ) -> Dict[str, Any]:
        """
        Create an automation rule
        
        Args:
            name: Rule name
            trigger: Trigger type ("tag_added", "form_submitted", "purchase", etc.)
            action: Action type ("add_tag", "send_email", "subscribe", etc.)
            trigger_config: Trigger-specific configuration
            action_config: Action-specific configuration
        """
        if not self.logged_in:
            self.login()
        
        self.navigate(f"{self.config.dashboard_url}/en/automation-rules")
        self.wait(2)
        
        self.click("button:contains('Create'), .create-rule-btn")
        self.wait(2)
        
        self.type_text("input[name='name']", name)
        
        # Select trigger
        self.click(".trigger-dropdown, select[name='trigger']")
        self.click(f"option[value='{trigger}'], option:contains('{trigger}')")
        self.wait(1)
        
        # Select action
        self.click(".action-dropdown, select[name='action']")
        self.click(f"option[value='{action}'], option:contains('{action}')")
        self.wait(1)
        
        # Save
        self.click("button:contains('Save'), .save-rule-btn")
        self.wait(2)
        
        return {"success": True, "name": name, "trigger": trigger, "action": action}
    
    # ==================== TAG OPERATIONS ====================
    
    def create_tag(self, tag_name: str) -> Dict[str, Any]:
        """Create a new tag"""
        if not self.logged_in:
            self.login()
        
        self.navigate(f"{self.config.dashboard_url}/en/tags")
        self.wait(2)
        
        self.click("button:contains('Create'), .create-tag-btn")
        self.wait(1)
        
        self.type_text("input[name='name']", tag_name)
        self.click("button:contains('Save'), .save-tag-btn")
        
        self.wait(2)
        
        return {"success": True, "tag_name": tag_name}
    
    # ==================== CONTEXT MANAGER ====================
    
    def __enter__(self):
        self.start_browser()
        self.login()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_browser()


# Convenience functions
def systeme_create_email_sequence(name: str, emails: List[Dict]) -> Dict:
    """Quick function to create email sequence"""
    with SystemeBrowserAutomation() as systeme:
        return systeme.create_email_sequence(name, emails)

def systeme_create_blog_post(title: str, content: str, publish: bool = False) -> Dict:
    """Quick function to create blog post"""
    with SystemeBrowserAutomation() as systeme:
        return systeme.create_blog_post(title, content, publish=publish)
```

---

## Usage Examples

### Create Welcome Email Sequence

```python
# Define emails
welcome_sequence = [
    {
        "subject": "Welcome to Smart Home Wizards! 🏠",
        "content": "<h1>Welcome!</h1><p>Thanks for subscribing...</p>"
    },
    {
        "subject": "Your First Smart Home Tip",
        "content": "<p>Here's a quick tip to get started...</p>"
    },
    {
        "subject": "Ready for More? Check This Out",
        "content": "<p>Now that you've got the basics...</p>"
    }
]

# Create the sequence
with SystemeBrowserAutomation() as systeme:
    result = systeme.create_email_sequence(
        name="Welcome Sequence - Smart Home Wizards",
        emails=welcome_sequence,
        delays=[0, 2, 5]  # Send immediately, then 2 days, then 5 days
    )
    print(result)
```

### Create Automation Rule

```python
with SystemeBrowserAutomation() as systeme:
    # When someone gets tagged "buyer", add them to buyers list
    result = systeme.create_automation_rule(
        name="Buyer Tag → Buyers List",
        trigger="tag_added",
        action="subscribe_to_campaign",
        trigger_config={"tag": "buyer"},
        action_config={"campaign": "Buyers Nurture Sequence"}
    )
```

---

## n8n Integration

```json
{
  "name": "Systeme.io Email Sequence Creator",
  "nodes": [
    {
      "name": "Start Session",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.steel.dev/v1/sessions",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer ste-A43JGQkLsnI609gNUXatQ83QB88Aj2JHOyrhvdaax8AxCWwSI0sn3VD01ToP4RjxM5POgbxoDhaEcwmsxshm6BFtKYS8J2ErKFy"
        },
        "body": {"browser": "chromium", "blockAds": true}
      }
    },
    {
      "name": "Login to Systeme",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.steel.dev/v1/sessions/{{ $json.sessionId }}/navigate",
        "method": "POST",
        "body": {"url": "https://systeme.io/dashboard/en/login"}
      }
    }
  ]
}
```

---

## Stagehand AI Integration (Alternative)

For complex or dynamic operations, use BrowserUse AI agent:

```python
from browseruse_agent import ai_browser_task

# Let AI figure out the complex task
result = ai_browser_task(
    task="""
    Login to Systeme.io with these credentials:
    Email: aiautomationblueprint@gmail.com
    Password: Ashlynn.09
    
    Then create a new email campaign called "AI Discovery Weekly"
    with 5 emails about AI trends, each sent 3 days apart.
    """,
    start_url="https://systeme.io/dashboard/en/login"
)
```

---

## Quick Reference

| Operation | Method | API Support |
|-----------|--------|-------------|
| Create Contact | API | ✅ |
| Add Tag | API | ✅ |
| Create Email | Browser | ❌ |
| Create Sequence | Browser | ❌ |
| Create Blog Post | Browser | ❌ |
| Create Funnel | Browser | ❌ |
| Create Automation | Browser | ❌ |
| Upload Media | Browser | ❌ |

---

*Systeme.io Browser Automation Skill*
*Version 1.0 | Recovered 2025-12-15*
*Complete email marketing automation when API isn't enough*
