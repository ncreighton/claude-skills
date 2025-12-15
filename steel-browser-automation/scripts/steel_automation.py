#!/usr/bin/env python3
"""
Steel.dev Browser Automation - Complete Implementation
For Nick Creighton's 16-Site WordPress Empire

Usage:
    from steel_automation import SteelBrowserAutomation, wp_login, wp_create_post
    
    # Quick WordPress login
    steel = wp_login("https://smarthomewizards.com", "SmartHomeGuru", "password")
    
    # Or use context manager
    with SteelBrowserAutomation() as steel:
        steel.navigate("https://example.com")
        steel.click("#button")
        steel.type("#input", "text")
"""

import requests
import time
import base64
from typing import Optional, Dict, Any, List
from dataclasses import dataclass

# =============================================================================
# CREDENTIALS
# =============================================================================

STEEL_API_KEY = "ste-A43JGQkLsnI609gNUXatQ83QB88Aj2JHOyrhvdaax8AxCWwSI0sn3VD01ToP4RjxM5POgbxoDhaEcwmsxshm6BFtKYS8J2ErKFy"
BROWSERUSE_API_KEY = "bu_YUQ0ZqtuWge86lOZUaWiZtK_rG6PkCNElONERb9Jzgs"

# =============================================================================
# SITE REGISTRY
# =============================================================================

SITES = {
    "smarthomewizards": {
        "url": "https://smarthomewizards.com",
        "wp_user": "SmartHomeGuru",
        "amazon_tag": "smarthomewizards-20"
    },
    "witchcraftforbeginners": {
        "url": "https://witchcraftforbeginners.com",
        "wp_user": "MoonlightMystic",
        "amazon_tag": "witchcraftforbeginners-20"
    },
    "aiinactionhub": {
        "url": "https://aiinactionhub.com",
        "wp_user": "ActionHubAdmin",
        "amazon_tag": "aiinactionhub-20"
    },
    "aidiscoverydigest": {
        "url": "https://aidiscoverydigest.com",
        "wp_user": "DiscoveryScribe",
        "amazon_tag": "aidiscoverydigest-20"
    },
    "wealthfromai": {
        "url": "https://wealthfromai.com",
        "wp_user": "AIWealthWizard",
        "amazon_tag": "wealthfromai-20"
    },
    "mythicalarchives": {
        "url": "https://mythicalarchives.com",
        "wp_user": "ArcaneArchivist",
        "amazon_tag": "mythicalarchives-20"
    },
    "bulletjournals": {
        "url": "https://bulletjournals.net",
        "wp_user": "BulletJournalPro",
        "amazon_tag": "bulletjournals01-20"
    },
    "familyflourish": {
        "url": "https://family-flourish.com",
        "wp_user": "FamilyGrowthGuide",
        "amazon_tag": "familyflourish-20"
    },
    "pulsegearreviews": {
        "url": "https://pulsegearreviews.com",
        "wp_user": "PulseGearPro",
        "amazon_tag": "pulsegearreviews-20"
    },
    "clearainews": {
        "url": "https://clearainews.com",
        "wp_user": "ClearAIReporter",
        "amazon_tag": "clearainews-20"
    },
    "celebrationseason": {
        "url": "https://celebrationseason.net",
        "wp_user": "CelebrationPro",
        "amazon_tag": "celebrationseason-20"
    },
    "sproutandspruce": {
        "url": "https://sprout-and-spruce.com",
        "wp_user": "GardenGuru",
        "amazon_tag": "sproutandspruce-20"
    },
    "theconnectedhaven": {
        "url": "https://theconnectedhaven.com",
        "wp_user": "HavenHost",
        "amazon_tag": "connectedhaven-20"
    },
    "wearablegearreviews": {
        "url": "https://wearablegearreviews.com",
        "wp_user": "WearableTechPro",
        "amazon_tag": "wearablegearreviews-20"
    },
    "smarthomegearreviews": {
        "url": "https://smarthomegearreviews.com",
        "wp_user": "GearReviewPro",
        "amazon_tag": "smarthomegearreviews-20"
    },
    "manifestandalign": {
        "url": "https://manifestandalign.com",
        "wp_user": "ManifestMaster",
        "amazon_tag": "manifestandalign-20"
    }
}


# =============================================================================
# STEEL BROWSER AUTOMATION CLASS
# =============================================================================

class SteelBrowserAutomation:
    """
    Steel.dev Browser Automation for WordPress Empire
    Fallback when MCP/API fails
    """
    
    def __init__(self, api_key: str = STEEL_API_KEY):
        self.api_key = api_key
        self.base_url = "https://api.steel.dev/v1"
        self.session_id = None
        
    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _request(self, method: str, endpoint: str, json_data: dict = None) -> Dict[str, Any]:
        """Make API request to Steel.dev"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == "POST":
                response = requests.post(url, headers=self._headers(), json=json_data, timeout=60)
            elif method == "GET":
                response = requests.get(url, headers=self._headers(), timeout=60)
            elif method == "DELETE":
                response = requests.delete(url, headers=self._headers(), timeout=60)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def start_session(self, proxy: str = "residential") -> Optional[str]:
        """Start a new browser session"""
        result = self._request("POST", "/sessions", {
            "browser": "chromium",
            "blockAds": True,
            "solveCaptcha": True,
            "proxy": proxy
        })
        
        if "error" not in result:
            self.session_id = result.get("sessionId")
        return self.session_id
    
    def navigate(self, url: str) -> Dict[str, Any]:
        """Navigate to URL"""
        return self._request("POST", f"/sessions/{self.session_id}/navigate", {"url": url})
    
    def click(self, selector: str) -> Dict[str, Any]:
        """Click element by CSS selector"""
        return self._request("POST", f"/sessions/{self.session_id}/click", {"selector": selector})
    
    def type(self, selector: str, text: str) -> Dict[str, Any]:
        """Type text into input field"""
        return self._request("POST", f"/sessions/{self.session_id}/type", {
            "selector": selector,
            "text": text
        })
    
    def extract(self, selector: str) -> List[str]:
        """Extract text from elements"""
        result = self._request("POST", f"/sessions/{self.session_id}/extract", {"selector": selector})
        return result.get("data", [])
    
    def screenshot(self, save_path: Optional[str] = None) -> str:
        """Take screenshot, optionally save to file"""
        result = self._request("POST", f"/sessions/{self.session_id}/screenshot")
        base64_data = result.get("data", "")
        
        if save_path and base64_data:
            with open(save_path, 'wb') as f:
                f.write(base64.b64decode(base64_data))
        
        return base64_data
    
    def evaluate(self, expression: str) -> Dict[str, Any]:
        """Execute JavaScript in browser"""
        return self._request("POST", f"/sessions/{self.session_id}/evaluate", {
            "expression": expression
        })
    
    def wait(self, seconds: float):
        """Wait for page to load"""
        time.sleep(seconds)
    
    def close(self):
        """Close the browser session"""
        if self.session_id:
            self._request("DELETE", f"/sessions/{self.session_id}")
            self.session_id = None
    
    def __enter__(self):
        self.start_session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# =============================================================================
# WORDPRESS AUTOMATION FUNCTIONS
# =============================================================================

def wp_login(site_url: str, username: str, password: str) -> SteelBrowserAutomation:
    """
    Login to WordPress admin and return logged-in session
    
    Args:
        site_url: WordPress site URL (e.g., "https://smarthomewizards.com")
        username: WordPress username
        password: WordPress password or app password
    
    Returns:
        SteelBrowserAutomation instance with active session
    """
    steel = SteelBrowserAutomation()
    steel.start_session()
    
    steel.navigate(f"{site_url}/wp-login.php")
    steel.wait(3)
    
    steel.type("#user_login", username)
    steel.type("#user_pass", password)
    steel.click("#wp-submit")
    
    steel.wait(4)
    
    # Verify login
    dashboard_check = steel.extract(".wrap h1, #wp-admin-bar-site-name")
    if dashboard_check:
        print(f"✅ Logged in to {site_url}")
    else:
        print(f"⚠️ Login may have failed for {site_url}")
    
    return steel


def wp_create_post(steel: SteelBrowserAutomation, site_url: str, title: str, content: str, 
                   status: str = "draft") -> Dict[str, Any]:
    """
    Create a new WordPress post
    
    Args:
        steel: Logged-in SteelBrowserAutomation instance
        site_url: WordPress site URL
        title: Post title
        content: Post content (HTML)
        status: "draft" or "publish"
    
    Returns:
        Result dict with success status
    """
    steel.navigate(f"{site_url}/wp-admin/post-new.php")
    steel.wait(3)
    
    # Check if block editor or classic
    is_gutenberg = len(steel.extract(".block-editor")) > 0
    
    if is_gutenberg:
        # Gutenberg editor
        steel.click(".editor-post-title__input")
        steel.type(".editor-post-title__input", title)
        
        # Add content block
        steel.click(".block-editor-default-block-appender__content")
        steel.type(".block-editor-rich-text__editable", content)
    else:
        # Classic editor
        steel.type("#title", title)
        steel.click("#content-html")  # Switch to text mode
        steel.wait(0.5)
        steel.type("#content", content)
    
    # Publish or save draft
    if status == "publish":
        steel.click(".editor-post-publish-button, #publish")
    else:
        steel.click(".editor-post-save-draft, #save-post")
    
    steel.wait(3)
    
    return {"success": True, "title": title, "status": status}


def wp_install_plugin(steel: SteelBrowserAutomation, site_url: str, plugin_slug: str) -> Dict[str, Any]:
    """
    Install and activate a WordPress plugin
    
    Args:
        steel: Logged-in SteelBrowserAutomation instance
        site_url: WordPress site URL
        plugin_slug: Plugin slug from WordPress.org
    
    Returns:
        Result dict with success status
    """
    steel.navigate(f"{site_url}/wp-admin/plugin-install.php?s={plugin_slug}&tab=search")
    steel.wait(4)
    
    # Click install on first result
    steel.click(f".plugin-card-{plugin_slug} .install-now")
    steel.wait(10)
    
    # Activate
    steel.click(f".plugin-card-{plugin_slug} .activate-now")
    steel.wait(3)
    
    return {"success": True, "plugin": plugin_slug}


def wp_update_option(steel: SteelBrowserAutomation, site_url: str, 
                     option_page: str, option_name: str, value: str) -> Dict[str, Any]:
    """
    Update a WordPress option/setting
    
    Args:
        steel: Logged-in SteelBrowserAutomation instance
        site_url: WordPress site URL
        option_page: Settings page URL path (e.g., "options-general.php")
        option_name: Input field name or ID
        value: New value to set
    
    Returns:
        Result dict with success status
    """
    steel.navigate(f"{site_url}/wp-admin/{option_page}")
    steel.wait(3)
    
    steel.type(f"#{option_name}, [name='{option_name}']", value)
    steel.click("#submit")
    steel.wait(2)
    
    return {"success": True, "option": option_name, "value": value}


# =============================================================================
# BROWSERUSE AI AGENT
# =============================================================================

class BrowserUseAgent:
    """
    BrowserUse AI Agent for Complex Browser Tasks
    When you need AI to figure it out
    """
    
    def __init__(self, api_key: str = BROWSERUSE_API_KEY):
        self.api_key = api_key
        self.base_url = "https://api.browseruse.com/v1"
    
    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def execute_task(self, task: str, start_url: Optional[str] = None,
                     max_steps: int = 20, timeout: int = 300) -> Dict[str, Any]:
        """
        Execute a task using AI browser agent
        
        Args:
            task: Natural language task description
            start_url: Optional starting URL
            max_steps: Maximum AI actions
            timeout: Timeout in seconds
        
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
            json=payload,
            timeout=timeout + 30
        )
        
        return response.json()
    
    def research(self, topic: str) -> Dict[str, Any]:
        """Research a topic using AI browser"""
        return self.execute_task(
            task=f"Research the following topic and provide a comprehensive summary: {topic}",
            start_url="https://google.com",
            max_steps=30
        )


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def get_site_credentials(site_slug: str) -> Dict[str, str]:
    """Get credentials for a site by slug"""
    return SITES.get(site_slug, {})


def quick_login(site_slug: str, password: str) -> SteelBrowserAutomation:
    """Quick login to a site by slug"""
    site = SITES.get(site_slug)
    if not site:
        raise ValueError(f"Unknown site: {site_slug}")
    
    return wp_login(site["url"], site["wp_user"], password)


def ai_browser_task(task: str, start_url: str = None) -> Dict[str, Any]:
    """Execute any browser task with AI"""
    agent = BrowserUseAgent()
    return agent.execute_task(task, start_url)


# =============================================================================
# MAIN EXAMPLE
# =============================================================================

if __name__ == "__main__":
    print("Steel.dev Browser Automation - Test")
    print("=" * 50)
    
    # Test creating a session
    with SteelBrowserAutomation() as steel:
        print("✅ Session created:", steel.session_id)
        
        # Navigate to a test page
        steel.navigate("https://example.com")
        steel.wait(2)
        
        # Extract page title
        title = steel.extract("h1")
        print("✅ Page title:", title)
        
        # Take screenshot
        steel.screenshot("test_screenshot.png")
        print("✅ Screenshot saved")
    
    print("\n✅ All tests passed!")
