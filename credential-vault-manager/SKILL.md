---
name: credential-vault-manager
description: Secure browser credential management system for extracting, storing, and injecting cookies, sessions, and passwords from Firefox and Chrome browsers. Enables AI agents to operate with existing user logins across all web services. Use when user needs to extract cookies from browsers, persist login sessions, manage saved passwords, import browser profiles, or enable authenticated automation. Triggers include "extract cookies", "browser cookies", "saved passwords", "login session", "import profile", "authenticated session", "use my logins", "browser profile", "session persistence", or any credential/session management requests.
---

# Credential Vault Manager

Secure browser credential extraction and management for AI agent authentication.

## Capabilities

### Cookie Extraction
- Extract from Chrome, Firefox, Edge, Brave, Opera
- Filter by domain
- Decrypt protected cookies
- Export to JSON/Netscape format

### Session Persistence
- Store sessions per-domain
- Auto-refresh expiring sessions
- Load into browser automation
- Track session health

### Profile Management
- Import entire browser profiles
- Merge profiles from multiple browsers
- Sync across automation sessions
- Backup and restore

## Cookie Extraction Methods

### Method 1: browser_cookie3 (Recommended)
```python
import browser_cookie3

# Chrome cookies
chrome_cookies = browser_cookie3.chrome(domain_name="example.com")

# Firefox cookies
firefox_cookies = browser_cookie3.firefox(domain_name="example.com")

# All browsers
all_cookies = browser_cookie3.load(domain_name="example.com")

# Specific profile
chrome_cookies = browser_cookie3.chrome(
    cookie_file="/path/to/Cookies",
    domain_name="example.com"
)
```

### Method 2: Direct SQLite Access
```python
import sqlite3
import os
import json

def extract_firefox_cookies(domain=None):
    """Extract cookies from Firefox profile."""
    # Find Firefox profile
    profiles_path = os.path.expanduser("~/.mozilla/firefox/")
    profile_dirs = [d for d in os.listdir(profiles_path) 
                    if d.endswith('.default') or d.endswith('.default-release')]
    
    cookies = []
    for profile in profile_dirs:
        cookie_file = os.path.join(profiles_path, profile, "cookies.sqlite")
        if os.path.exists(cookie_file):
            # Copy to avoid lock issues
            import shutil
            temp_file = "/tmp/firefox_cookies.sqlite"
            shutil.copy(cookie_file, temp_file)
            
            conn = sqlite3.connect(temp_file)
            cursor = conn.cursor()
            
            query = """
                SELECT name, value, host, path, expiry, isSecure, isHttpOnly
                FROM moz_cookies
            """
            if domain:
                query += f" WHERE host LIKE '%{domain}%'"
            
            cursor.execute(query)
            for row in cursor.fetchall():
                cookies.append({
                    "name": row[0],
                    "value": row[1],
                    "domain": row[2],
                    "path": row[3],
                    "expires": row[4],
                    "secure": bool(row[5]),
                    "httpOnly": bool(row[6])
                })
            conn.close()
    return cookies

def extract_chrome_cookies(domain=None):
    """Extract cookies from Chrome (requires decryption on some systems)."""
    import platform
    
    if platform.system() == "Linux":
        cookie_file = os.path.expanduser(
            "~/.config/google-chrome/Default/Cookies"
        )
    elif platform.system() == "Darwin":
        cookie_file = os.path.expanduser(
            "~/Library/Application Support/Google/Chrome/Default/Cookies"
        )
    elif platform.system() == "Windows":
        cookie_file = os.path.join(
            os.environ["LOCALAPPDATA"],
            r"Google\Chrome\User Data\Default\Network\Cookies"
        )
    
    # Chrome cookies require decryption - use browser_cookie3 instead
    return browser_cookie3.chrome(domain_name=domain)
```

### Method 3: Playwright Session Import
```python
from playwright.sync_api import sync_playwright
import json

def load_cookies_to_playwright(cookies_file):
    """Load cookies into Playwright session."""
    with open(cookies_file, 'r') as f:
        cookies = json.load(f)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Visit domain first (required for cookie injection)
        domains = set(c.get('domain', '').lstrip('.') for c in cookies)
        for domain in domains:
            try:
                page.goto(f"https://{domain}", timeout=5000)
            except:
                pass
        
        # Add cookies
        context.add_cookies(cookies)
        
        # Now navigating to any of these domains will be authenticated
        return browser, context, page
```

## Vault Storage Format

### cookies_vault.json
```json
{
  "sites": {
    "example.com": {
      "cookies": [...],
      "last_updated": "2025-11-26T12:00:00Z",
      "expires_at": "2026-01-01T00:00:00Z",
      "source": "chrome",
      "profile": "Default"
    }
  },
  "profiles": {
    "chrome_default": {
      "path": "~/.config/google-chrome/Default",
      "imported_at": "2025-11-26T12:00:00Z"
    },
    "firefox_default": {
      "path": "~/.mozilla/firefox/*.default-release",
      "imported_at": "2025-11-26T12:00:00Z"
    }
  }
}
```

## Profile Locations

### Chrome
```
Linux:   ~/.config/google-chrome/Default/
macOS:   ~/Library/Application Support/Google/Chrome/Default/
Windows: %LOCALAPPDATA%\Google\Chrome\User Data\Default\
```

### Firefox
```
Linux:   ~/.mozilla/firefox/*.default-release/
macOS:   ~/Library/Application Support/Firefox/Profiles/*.default-release/
Windows: %APPDATA%\Mozilla\Firefox\Profiles\*.default-release\
```

### Edge
```
Linux:   ~/.config/microsoft-edge/Default/
macOS:   ~/Library/Application Support/Microsoft Edge/Default/
Windows: %LOCALAPPDATA%\Microsoft\Edge\User Data\Default\
```

### Brave
```
Linux:   ~/.config/BraveSoftware/Brave-Browser/Default/
macOS:   ~/Library/Application Support/BraveSoftware/Brave-Browser/Default/
Windows: %LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\
```

## Integration Workflow

### Full Authentication Pipeline
```
1. User specifies target sites
2. Extract cookies from all browsers
3. Filter to relevant domains
4. Store in vault with metadata
5. Browser automation loads from vault
6. Execute authenticated tasks
7. Save updated cookies back to vault
```

### Session Health Check
```python
def check_session_health(domain, cookies):
    """Verify session is still valid."""
    import requests
    
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(
            cookie['name'], 
            cookie['value'],
            domain=cookie.get('domain', domain)
        )
    
    # Try to access authenticated endpoint
    response = session.get(f"https://{domain}/api/user", timeout=10)
    return response.status_code == 200
```

## Security Considerations

### DO
- Store vault with appropriate file permissions (600)
- Encrypt vault at rest for sensitive environments
- Track session expiry and refresh proactively
- Audit which sessions are being used
- Delete sessions when no longer needed

### DON'T
- Commit vault to version control
- Share vault between users
- Store passwords in plain text
- Ignore session expiry warnings
- Use sessions after logout from browser

## Cookie Format Conversion

### Netscape to JSON
```python
def netscape_to_json(netscape_file):
    """Convert Netscape cookie file to JSON."""
    cookies = []
    with open(netscape_file, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 7:
                cookies.append({
                    "domain": parts[0],
                    "path": parts[2],
                    "secure": parts[3].lower() == 'true',
                    "expires": int(parts[4]) if parts[4] != '0' else None,
                    "name": parts[5],
                    "value": parts[6]
                })
    return cookies
```

### JSON to Netscape
```python
def json_to_netscape(cookies, output_file):
    """Convert JSON cookies to Netscape format."""
    with open(output_file, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        for c in cookies:
            domain = c.get('domain', '')
            flag = 'TRUE' if domain.startswith('.') else 'FALSE'
            path = c.get('path', '/')
            secure = 'TRUE' if c.get('secure') else 'FALSE'
            expires = str(c.get('expires', 0) or 0)
            name = c['name']
            value = c['value']
            f.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n")
```

## Quick Commands

| Task | Action |
|------|--------|
| Extract all cookies | `browser_cookie3.load()` |
| Extract for domain | `browser_cookie3.chrome(domain_name="x.com")` |
| Save to vault | `vault.save("domain", cookies)` |
| Load from vault | `vault.load("domain")` |
| Inject to browser | `context.add_cookies(cookies)` |
| Check validity | `check_session_health(domain, cookies)` |

## Resources

- **scripts/cookie_extractor.py** - Multi-browser cookie extraction
- **scripts/vault_manager.py** - Vault CRUD operations
- **scripts/session_refresher.py** - Auto-refresh expiring sessions
- **references/browser_paths.json** - All browser profile locations
