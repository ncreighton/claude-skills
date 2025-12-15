# BROWSERUSE AI AGENT SKILL
## AI-Powered Browser Automation for Complex Tasks
### Version 1.0

---

## Overview

BrowserUse is an AI-powered browser agent that can:
- Navigate websites autonomously
- Figure out complex multi-step tasks
- Handle dynamic/JavaScript-heavy pages
- Complete tasks when you don't know exact selectors
- Research and explore websites intelligently

**Use When:** You need AI to figure out how to complete a task

**Trigger Keywords:** ai browser, browseruse, ai agent, complex task, figure it out

---

## Credentials

```yaml
BrowserUse:
  API Key: bu_YUQ0ZqtuWge86lOZUaWiZtK_rG6PkCNElONERb9Jzgs
  Base URL: https://api.browseruse.com
```

---

## When to Use BrowserUse vs Steel.dev

| Use Steel.dev | Use BrowserUse |
|---------------|----------------|
| Simple, repeatable tasks | Complex multi-step workflows |
| Known selectors | Unknown page structure |
| Form filling | AI-guided navigation |
| Data extraction | Research and exploration |
| Fast execution | When you need AI judgment |

---

## API Usage

### Execute Task with AI

```python
import requests

BROWSERUSE_API_KEY = "bu_YUQ0ZqtuWge86lOZUaWiZtK_rG6PkCNElONERb9Jzgs"

def ai_browser_task(task: str, start_url: str = None) -> dict:
    """
    Execute a task using AI browser agent
    
    Args:
        task: Natural language description of what to do
        start_url: Optional starting URL
    
    Returns:
        Result of the AI agent's execution
    """
    response = requests.post(
        "https://api.browseruse.com/v1/tasks",
        headers={
            "Authorization": f"Bearer {BROWSERUSE_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "task": task,
            "start_url": start_url,
            "max_steps": 20,
            "timeout": 300  # 5 minutes
        }
    )
    return response.json()
```

### Example Tasks

```python
# Research task
result = ai_browser_task(
    task="Go to Google and find the top 5 smart home trends for 2025, summarize each one",
    start_url="https://google.com"
)

# Form completion
result = ai_browser_task(
    task="Navigate to WordPress admin, create a new page called 'About Us' with placeholder content",
    start_url="https://mysite.com/wp-admin"
)

# Data extraction
result = ai_browser_task(
    task="Find all product prices on this page and create a list",
    start_url="https://amazon.com/s?k=smart+home+devices"
)
```

---

## Complete Class Implementation

```python
import requests
import time
from typing import Optional, Dict, Any

class BrowserUseAgent:
    """
    BrowserUse AI Agent for Complex Browser Tasks
    When you need AI to figure it out
    """
    
    def __init__(self):
        self.api_key = "bu_YUQ0ZqtuWge86lOZUaWiZtK_rG6PkCNElONERb9Jzgs"
        self.base_url = "https://api.browseruse.com/v1"
    
    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def execute_task(
        self,
        task: str,
        start_url: Optional[str] = None,
        max_steps: int = 20,
        timeout: int = 300
    ) -> Dict[str, Any]:
        """
        Execute a task using AI browser agent
        
        Args:
            task: Natural language task description
            start_url: Optional starting URL
            max_steps: Maximum AI actions (default 20)
            timeout: Timeout in seconds (default 300)
        
        Returns:
            Task execution result
        """
        payload = {
            "task": task,
            "max_steps": max_steps,
            "timeout": timeout
        }
        
        if start_url:
            payload["start_url"] = start_url
        
        response = requests.post(
            f"{self.base_url}/tasks",
            headers=self._headers(),
            json=payload
        )
        
        return response.json()
    
    def get_task_status(self, task_id: str) -> Dict[str, Any]:
        """Check status of a running task"""
        response = requests.get(
            f"{self.base_url}/tasks/{task_id}",
            headers=self._headers()
        )
        return response.json()
    
    def wait_for_completion(self, task_id: str, poll_interval: int = 5) -> Dict[str, Any]:
        """Wait for task to complete, polling status"""
        while True:
            status = self.get_task_status(task_id)
            if status.get("status") in ["completed", "failed", "timeout"]:
                return status
            time.sleep(poll_interval)
    
    def research(self, topic: str, depth: str = "medium") -> Dict[str, Any]:
        """
        Research a topic using AI browser
        
        Args:
            topic: What to research
            depth: "shallow" (quick), "medium" (balanced), "deep" (thorough)
        """
        max_steps = {"shallow": 10, "medium": 20, "deep": 40}.get(depth, 20)
        
        return self.execute_task(
            task=f"Research the following topic and provide a comprehensive summary: {topic}",
            start_url="https://google.com",
            max_steps=max_steps
        )
    
    def fill_form(self, url: str, form_data: Dict[str, str]) -> Dict[str, Any]:
        """
        Fill out a form using AI
        
        Args:
            url: Form URL
            form_data: Dictionary of field names to values
        """
        field_instructions = "\n".join([
            f"- {field}: {value}" 
            for field, value in form_data.items()
        ])
        
        return self.execute_task(
            task=f"Fill out the form with these values:\n{field_instructions}\nThen submit the form.",
            start_url=url
        )
    
    def extract_data(self, url: str, what_to_extract: str) -> Dict[str, Any]:
        """
        Extract specific data from a page
        
        Args:
            url: Page URL
            what_to_extract: Description of data to extract
        """
        return self.execute_task(
            task=f"Extract the following from this page: {what_to_extract}. Return as structured data.",
            start_url=url
        )


# Convenience functions
def ai_research(topic: str) -> Dict[str, Any]:
    """Quick research on any topic"""
    agent = BrowserUseAgent()
    return agent.research(topic)

def ai_browser_task(task: str, start_url: str = None) -> Dict[str, Any]:
    """Execute any browser task with AI"""
    agent = BrowserUseAgent()
    return agent.execute_task(task, start_url)
```

---

## Fallback Integration

BrowserUse is the LAST fallback in the chain:

```
MCP → API → Steel.dev → BrowserUse (AI)
```

Use in fallback handler:

```python
async def execute_with_fallback(task: str, site_config: dict):
    """Execute task with automatic fallback chain"""
    
    # 1. Try MCP
    try:
        return await mcp_execute(task, site_config)
    except:
        pass
    
    # 2. Try API
    try:
        return await api_execute(task, site_config)
    except:
        pass
    
    # 3. Try Steel.dev (simple browser)
    try:
        return await steel_execute(task, site_config)
    except:
        pass
    
    # 4. Final fallback: AI Agent
    return await browseruse_execute(task, site_config)

async def browseruse_execute(task: str, site_config: dict):
    """Let AI figure it out"""
    agent = BrowserUseAgent()
    
    # Convert task to natural language
    task_description = f"""
    Site: {site_config['url']}
    Task: {task}
    
    Complete this task on the website. Login credentials:
    Username: {site_config['wp_user']}
    Password: {site_config['wp_pass']}
    """
    
    result = agent.execute_task(
        task=task_description,
        start_url=f"{site_config['url']}/wp-admin"
    )
    
    return {
        "success": result.get("status") == "completed",
        "method": "browseruse_ai",
        "result": result
    }
```

---

## Quick Commands

```yaml
# Research anything
ai_research("best smart home devices 2025")

# Execute any task
ai_browser_task("Create a blog post about AI trends", "https://mysite.com/wp-admin")

# Extract data
agent = BrowserUseAgent()
agent.extract_data("https://amazon.com/product", "product name, price, and rating")
```

---

*BrowserUse AI Agent Skill*
*Version 1.0 | Recovered 2025-12-15*
*When you need AI to figure it out*
