#!/usr/bin/env python3
"""
Multi-browser cookie extraction utility.
Extracts cookies from Chrome, Firefox, Edge, Brave, and Opera.
"""

import os
import sys
import json
import sqlite3
import shutil
import tempfile
import platform
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

# Try to import browser_cookie3, fall back to manual extraction
try:
    import browser_cookie3
    HAS_BROWSER_COOKIE3 = True
except ImportError:
    HAS_BROWSER_COOKIE3 = False
    print("Warning: browser_cookie3 not installed. Using manual extraction.")
    print("Install with: pip install browser_cookie3 --break-system-packages")


def get_browser_paths() -> Dict[str, Dict[str, str]]:
    """Get browser profile paths for current OS."""
    system = platform.system()
    home = Path.home()
    
    paths = {
        "chrome": {},
        "firefox": {},
        "edge": {},
        "brave": {},
        "opera": {}
    }
    
    if system == "Linux":
        paths["chrome"]["cookies"] = home / ".config/google-chrome/Default/Cookies"
        paths["chrome"]["profile"] = home / ".config/google-chrome/Default"
        paths["firefox"]["profile"] = home / ".mozilla/firefox"
        paths["edge"]["cookies"] = home / ".config/microsoft-edge/Default/Cookies"
        paths["brave"]["cookies"] = home / ".config/BraveSoftware/Brave-Browser/Default/Cookies"
        paths["opera"]["cookies"] = home / ".config/opera/Cookies"
        
    elif system == "Darwin":  # macOS
        paths["chrome"]["cookies"] = home / "Library/Application Support/Google/Chrome/Default/Cookies"
        paths["chrome"]["profile"] = home / "Library/Application Support/Google/Chrome/Default"
        paths["firefox"]["profile"] = home / "Library/Application Support/Firefox/Profiles"
        paths["edge"]["cookies"] = home / "Library/Application Support/Microsoft Edge/Default/Cookies"
        paths["brave"]["cookies"] = home / "Library/Application Support/BraveSoftware/Brave-Browser/Default/Cookies"
        paths["opera"]["cookies"] = home / "Library/Application Support/com.operasoftware.Opera/Cookies"
        
    elif system == "Windows":
        local = Path(os.environ.get("LOCALAPPDATA", ""))
        roaming = Path(os.environ.get("APPDATA", ""))
        paths["chrome"]["cookies"] = local / "Google/Chrome/User Data/Default/Network/Cookies"
        paths["chrome"]["profile"] = local / "Google/Chrome/User Data/Default"
        paths["firefox"]["profile"] = roaming / "Mozilla/Firefox/Profiles"
        paths["edge"]["cookies"] = local / "Microsoft/Edge/User Data/Default/Network/Cookies"
        paths["brave"]["cookies"] = local / "BraveSoftware/Brave-Browser/User Data/Default/Network/Cookies"
        paths["opera"]["cookies"] = roaming / "Opera Software/Opera Stable/Cookies"
    
    return paths


def extract_firefox_cookies_manual(domain: Optional[str] = None) -> List[Dict]:
    """Extract Firefox cookies directly from SQLite database."""
    cookies = []
    firefox_path = get_browser_paths()["firefox"]["profile"]
    
    if not firefox_path.exists():
        return cookies
    
    # Find profile directories
    profile_dirs = list(firefox_path.glob("*.default*"))
    
    for profile_dir in profile_dirs:
        cookie_file = profile_dir / "cookies.sqlite"
        if not cookie_file.exists():
            continue
        
        # Copy to temp to avoid lock issues
        with tempfile.NamedTemporaryFile(delete=False, suffix=".sqlite") as tmp:
            tmp_path = tmp.name
        
        try:
            shutil.copy(cookie_file, tmp_path)
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            query = """
                SELECT name, value, host, path, expiry, isSecure, isHttpOnly, sameSite
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
                    "httpOnly": bool(row[6]),
                    "sameSite": row[7] if len(row) > 7 else "Lax",
                    "source": "firefox",
                    "profile": str(profile_dir)
                })
            
            conn.close()
        finally:
            os.unlink(tmp_path)
    
    return cookies


def extract_cookies_browser_cookie3(browser: str, domain: Optional[str] = None) -> List[Dict]:
    """Extract cookies using browser_cookie3 library."""
    if not HAS_BROWSER_COOKIE3:
        return []
    
    cookies = []
    browser_funcs = {
        "chrome": browser_cookie3.chrome,
        "firefox": browser_cookie3.firefox,
        "edge": browser_cookie3.edge,
        "brave": browser_cookie3.brave,
        "opera": browser_cookie3.opera,
    }
    
    if browser not in browser_funcs:
        return cookies
    
    try:
        cj = browser_funcs[browser](domain_name=domain)
        for cookie in cj:
            cookies.append({
                "name": cookie.name,
                "value": cookie.value,
                "domain": cookie.domain,
                "path": cookie.path,
                "expires": cookie.expires,
                "secure": cookie.secure,
                "httpOnly": getattr(cookie, 'httpOnly', False),
                "source": browser,
            })
    except Exception as e:
        print(f"Error extracting {browser} cookies: {e}")
    
    return cookies


def extract_all_cookies(domain: Optional[str] = None) -> Dict[str, List[Dict]]:
    """Extract cookies from all available browsers."""
    results = {
        "chrome": [],
        "firefox": [],
        "edge": [],
        "brave": [],
        "opera": [],
        "extracted_at": datetime.now().isoformat()
    }
    
    browsers = ["chrome", "firefox", "edge", "brave", "opera"]
    
    for browser in browsers:
        if HAS_BROWSER_COOKIE3:
            results[browser] = extract_cookies_browser_cookie3(browser, domain)
        elif browser == "firefox":
            results[browser] = extract_firefox_cookies_manual(domain)
    
    return results


def save_cookies_json(cookies: Dict, output_file: str):
    """Save cookies to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cookies, f, indent=2, default=str)
    print(f"Saved cookies to {output_file}")


def save_cookies_netscape(cookies: List[Dict], output_file: str):
    """Save cookies in Netscape format (for curl, wget, etc.)."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# Generated by cookie_extractor.py\n\n")
        
        for c in cookies:
            domain = c.get('domain', '')
            flag = 'TRUE' if domain.startswith('.') else 'FALSE'
            path = c.get('path', '/')
            secure = 'TRUE' if c.get('secure') else 'FALSE'
            expires = str(c.get('expires', 0) or 0)
            name = c['name']
            value = c['value']
            f.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n")
    
    print(f"Saved Netscape cookies to {output_file}")


def flatten_cookies(cookies_by_browser: Dict) -> List[Dict]:
    """Flatten browser-grouped cookies into single list."""
    flattened = []
    for browser, browser_cookies in cookies_by_browser.items():
        if isinstance(browser_cookies, list):
            flattened.extend(browser_cookies)
    return flattened


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract browser cookies")
    parser.add_argument("--domain", "-d", help="Filter by domain")
    parser.add_argument("--browser", "-b", choices=["chrome", "firefox", "edge", "brave", "opera", "all"],
                       default="all", help="Browser to extract from")
    parser.add_argument("--output", "-o", default="cookies.json", help="Output file")
    parser.add_argument("--format", "-f", choices=["json", "netscape"], default="json",
                       help="Output format")
    
    args = parser.parse_args()
    
    print(f"Extracting cookies...")
    if args.domain:
        print(f"  Domain filter: {args.domain}")
    
    if args.browser == "all":
        cookies = extract_all_cookies(args.domain)
    else:
        cookies = {args.browser: extract_cookies_browser_cookie3(args.browser, args.domain)}
    
    # Count cookies
    total = sum(len(v) for v in cookies.values() if isinstance(v, list))
    print(f"  Found {total} cookies")
    
    # Save
    if args.format == "json":
        save_cookies_json(cookies, args.output)
    else:
        flat_cookies = flatten_cookies(cookies)
        save_cookies_netscape(flat_cookies, args.output)
    
    return cookies


if __name__ == "__main__":
    main()
