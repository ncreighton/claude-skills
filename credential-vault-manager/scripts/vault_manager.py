#!/usr/bin/env python3
"""
Credential Vault Manager.
Secure storage and retrieval of browser cookies and sessions.
"""

import os
import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, asdict
import base64

# Optional encryption support
try:
    from cryptography.fernet import Fernet
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False


@dataclass
class SessionInfo:
    domain: str
    cookies: List[Dict]
    last_updated: str
    expires_at: Optional[str]
    source: str
    profile: Optional[str]
    is_valid: bool = True


class VaultManager:
    """Manage credential vault operations."""
    
    def __init__(self, vault_path: str = "~/.credential_vault", encrypt: bool = False):
        self.vault_path = Path(vault_path).expanduser()
        self.vault_file = self.vault_path / "vault.json"
        self.key_file = self.vault_path / ".vault_key"
        self.encrypt = encrypt and HAS_CRYPTO
        
        # Initialize vault directory
        self.vault_path.mkdir(parents=True, exist_ok=True)
        os.chmod(self.vault_path, 0o700)  # Secure permissions
        
        # Initialize encryption if enabled
        self.cipher = None
        if self.encrypt:
            self._init_encryption()
        
        # Load or create vault
        self.vault = self._load_vault()
    
    def _init_encryption(self):
        """Initialize Fernet encryption."""
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            os.chmod(self.key_file, 0o600)
        
        self.cipher = Fernet(key)
    
    def _encrypt_data(self, data: str) -> str:
        """Encrypt data string."""
        if self.cipher:
            encrypted = self.cipher.encrypt(data.encode())
            return base64.b64encode(encrypted).decode()
        return data
    
    def _decrypt_data(self, data: str) -> str:
        """Decrypt data string."""
        if self.cipher:
            decrypted = self.cipher.decrypt(base64.b64decode(data))
            return decrypted.decode()
        return data
    
    def _load_vault(self) -> Dict:
        """Load vault from disk."""
        if not self.vault_file.exists():
            return {
                "version": "1.0",
                "created_at": datetime.now().isoformat(),
                "sites": {},
                "profiles": {}
            }
        
        with open(self.vault_file, 'r') as f:
            data = f.read()
        
        if self.encrypt and data.startswith('"') and data.endswith('"'):
            data = self._decrypt_data(json.loads(data))
        
        return json.loads(data)
    
    def _save_vault(self):
        """Save vault to disk."""
        data = json.dumps(self.vault, indent=2, default=str)
        
        if self.encrypt:
            data = json.dumps(self._encrypt_data(data))
        
        with open(self.vault_file, 'w') as f:
            f.write(data)
        
        os.chmod(self.vault_file, 0o600)
    
    def save_session(self, domain: str, cookies: List[Dict], 
                     source: str = "manual", profile: Optional[str] = None,
                     expires_hours: int = 720):
        """Save session cookies for a domain."""
        now = datetime.now()
        expires_at = now + timedelta(hours=expires_hours)
        
        session = SessionInfo(
            domain=domain,
            cookies=cookies,
            last_updated=now.isoformat(),
            expires_at=expires_at.isoformat(),
            source=source,
            profile=profile,
            is_valid=True
        )
        
        self.vault["sites"][domain] = asdict(session)
        self._save_vault()
        
        print(f"Saved {len(cookies)} cookies for {domain}")
        return session
    
    def load_session(self, domain: str) -> Optional[SessionInfo]:
        """Load session cookies for a domain."""
        if domain not in self.vault["sites"]:
            # Try to find partial match
            for site_domain in self.vault["sites"]:
                if domain in site_domain or site_domain in domain:
                    domain = site_domain
                    break
            else:
                return None
        
        data = self.vault["sites"][domain]
        session = SessionInfo(**data)
        
        # Check expiry
        if session.expires_at:
            expires = datetime.fromisoformat(session.expires_at)
            if datetime.now() > expires:
                session.is_valid = False
                print(f"Warning: Session for {domain} has expired")
        
        return session
    
    def get_cookies(self, domain: str) -> List[Dict]:
        """Get just the cookies for a domain."""
        session = self.load_session(domain)
        if session and session.cookies:
            return session.cookies
        return []
    
    def list_sites(self) -> List[str]:
        """List all sites with stored sessions."""
        return list(self.vault["sites"].keys())
    
    def delete_session(self, domain: str):
        """Delete session for a domain."""
        if domain in self.vault["sites"]:
            del self.vault["sites"][domain]
            self._save_vault()
            print(f"Deleted session for {domain}")
    
    def check_session_health(self, domain: str) -> Dict[str, Any]:
        """Check if a session is still valid."""
        session = self.load_session(domain)
        if not session:
            return {"status": "not_found", "domain": domain}
        
        result = {
            "status": "ok" if session.is_valid else "expired",
            "domain": domain,
            "cookie_count": len(session.cookies),
            "last_updated": session.last_updated,
            "expires_at": session.expires_at,
            "source": session.source
        }
        
        # Check for session cookies (might expire sooner)
        session_cookies = [c for c in session.cookies if not c.get('expires')]
        if session_cookies:
            result["has_session_cookies"] = True
            result["warning"] = "Contains session cookies that may expire on browser close"
        
        return result
    
    def import_from_extractor(self, cookies_file: str):
        """Import cookies from cookie_extractor.py output."""
        with open(cookies_file, 'r') as f:
            data = json.load(f)
        
        imported = 0
        for browser, cookies in data.items():
            if not isinstance(cookies, list):
                continue
            
            # Group by domain
            by_domain = {}
            for cookie in cookies:
                domain = cookie.get('domain', '').lstrip('.')
                if domain:
                    if domain not in by_domain:
                        by_domain[domain] = []
                    by_domain[domain].append(cookie)
            
            # Save each domain
            for domain, domain_cookies in by_domain.items():
                self.save_session(
                    domain=domain,
                    cookies=domain_cookies,
                    source=browser,
                    profile=cookies[0].get('profile') if domain_cookies else None
                )
                imported += len(domain_cookies)
        
        print(f"Imported {imported} cookies from {cookies_file}")
    
    def export_for_playwright(self, domain: str) -> List[Dict]:
        """Export cookies in Playwright-compatible format."""
        cookies = self.get_cookies(domain)
        
        playwright_cookies = []
        for c in cookies:
            playwright_cookie = {
                "name": c["name"],
                "value": c["value"],
                "domain": c.get("domain", domain),
                "path": c.get("path", "/"),
            }
            
            if c.get("expires"):
                playwright_cookie["expires"] = c["expires"]
            if c.get("secure"):
                playwright_cookie["secure"] = True
            if c.get("httpOnly"):
                playwright_cookie["httpOnly"] = True
            if c.get("sameSite"):
                playwright_cookie["sameSite"] = c["sameSite"]
            
            playwright_cookies.append(playwright_cookie)
        
        return playwright_cookies
    
    def export_for_requests(self, domain: str) -> Dict[str, str]:
        """Export cookies as simple dict for requests library."""
        cookies = self.get_cookies(domain)
        return {c["name"]: c["value"] for c in cookies}
    
    def get_summary(self) -> Dict:
        """Get vault summary."""
        sites = self.vault["sites"]
        
        summary = {
            "total_sites": len(sites),
            "total_cookies": sum(len(s.get("cookies", [])) for s in sites.values()),
            "sites": []
        }
        
        for domain, session in sites.items():
            summary["sites"].append({
                "domain": domain,
                "cookies": len(session.get("cookies", [])),
                "source": session.get("source"),
                "last_updated": session.get("last_updated"),
                "is_valid": session.get("is_valid", True)
            })
        
        return summary


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Credential Vault Manager")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List stored sites")
    
    # Get command
    get_parser = subparsers.add_parser("get", help="Get cookies for domain")
    get_parser.add_argument("domain", help="Domain to get cookies for")
    get_parser.add_argument("--format", choices=["json", "playwright", "requests"],
                          default="json", help="Output format")
    
    # Import command
    import_parser = subparsers.add_parser("import", help="Import cookies from file")
    import_parser.add_argument("file", help="Cookies file to import")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete session")
    delete_parser.add_argument("domain", help="Domain to delete")
    
    # Health command
    health_parser = subparsers.add_parser("health", help="Check session health")
    health_parser.add_argument("domain", help="Domain to check")
    
    # Summary command
    summary_parser = subparsers.add_parser("summary", help="Show vault summary")
    
    args = parser.parse_args()
    vault = VaultManager()
    
    if args.command == "list":
        sites = vault.list_sites()
        print(f"Stored sites ({len(sites)}):")
        for site in sites:
            print(f"  - {site}")
    
    elif args.command == "get":
        if args.format == "playwright":
            cookies = vault.export_for_playwright(args.domain)
        elif args.format == "requests":
            cookies = vault.export_for_requests(args.domain)
        else:
            cookies = vault.get_cookies(args.domain)
        print(json.dumps(cookies, indent=2))
    
    elif args.command == "import":
        vault.import_from_extractor(args.file)
    
    elif args.command == "delete":
        vault.delete_session(args.domain)
    
    elif args.command == "health":
        health = vault.check_session_health(args.domain)
        print(json.dumps(health, indent=2))
    
    elif args.command == "summary":
        summary = vault.get_summary()
        print(json.dumps(summary, indent=2))
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
