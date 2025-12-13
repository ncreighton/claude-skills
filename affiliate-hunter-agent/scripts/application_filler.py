#!/usr/bin/env python3
"""
Affiliate Application Form Filler

Automates filling out affiliate program applications using browser automation.
Integrates with Browserbase, Playwright, or Skyvern MCPs.

Usage:
    python application_filler.py --site witchcraft-beginners --network shareasale
    python application_filler.py --url "https://example.com/affiliate-apply" --site smart-home-wizards
"""

import json
import argparse
import os
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Dict, List
import time


@dataclass
class FormField:
    """Represents a form field to fill"""
    name: str
    selector: str  # CSS selector or natural language description
    value: str
    field_type: str = "text"  # text, select, checkbox, radio, textarea


@dataclass
class ApplicationResult:
    """Result of an application submission"""
    network: str
    site_id: str
    url: str
    status: str  # submitted, failed, needs_review
    timestamp: str
    screenshot_path: str = ""
    confirmation_id: str = ""
    error_message: str = ""


class SiteProfileLoader:
    """Loads and manages site profile data for applications"""
    
    def __init__(self, profiles_path: str = None):
        if profiles_path is None:
            profiles_path = Path(__file__).parent.parent / "references" / "site-profiles.json"
        
        with open(profiles_path, 'r') as f:
            self.data = json.load(f)
    
    def get_site(self, site_id: str) -> Optional[dict]:
        """Get site profile by ID"""
        for site in self.data.get("sites", []):
            if site.get("site_id") == site_id:
                return site
        return None
    
    def get_owner_info(self) -> dict:
        """Get owner/applicant information"""
        return self.data.get("owner", {})
    
    def get_application_data(self, site_id: str) -> dict:
        """Get pre-filled application data for a site"""
        site = self.get_site(site_id)
        if not site:
            return {}
        
        owner = self.get_owner_info()
        app_data = site.get("application_data", {})
        
        # Merge owner and site data
        return {
            **owner,
            **app_data,
            "site_id": site_id,
            "domain": site.get("domain", ""),
            "niche": site.get("niche", "")
        }


class FormFieldMapper:
    """Maps application data to form fields"""
    
    # Common field label patterns
    FIELD_MAPPINGS = {
        "website_url": [
            "Website URL", "Site URL", "Your Website", "Blog URL", 
            "URL", "Web Address", "Website Address", "Your Site URL"
        ],
        "website_name": [
            "Website Name", "Site Name", "Blog Name", "Company Name",
            "Business Name", "Your Website Name", "Site Title"
        ],
        "description": [
            "Website Description", "Site Description", "About Your Site",
            "Description", "Tell us about your website", "About Your Website",
            "Describe your site", "How do you plan to promote"
        ],
        "category": [
            "Category", "Niche", "Primary Category", "Website Category",
            "Content Type", "Primary Topic", "Industry", "Vertical"
        ],
        "traffic": [
            "Monthly Traffic", "Monthly Visitors", "Page Views",
            "Unique Visitors", "Traffic Volume", "Monthly Pageviews",
            "Estimated Traffic"
        ],
        "promotion_methods": [
            "Promotion Methods", "How will you promote", "Marketing Channels",
            "Traffic Sources", "Promotional Methods", "How do you drive traffic"
        ],
        "email": [
            "Email", "Email Address", "Contact Email", "Your Email"
        ],
        "name": [
            "Name", "Full Name", "Your Name", "Contact Name"
        ],
        "phone": [
            "Phone", "Phone Number", "Contact Phone", "Telephone"
        ],
        "address": [
            "Address", "Street Address", "Mailing Address"
        ],
        "city": ["City"],
        "state": ["State", "State/Province", "Region"],
        "zip": ["Zip", "Zip Code", "Postal Code"],
        "country": ["Country"]
    }
    
    @classmethod
    def find_field_mapping(cls, field_label: str) -> Optional[str]:
        """Find which data key maps to a field label"""
        field_label_lower = field_label.lower()
        
        for data_key, patterns in cls.FIELD_MAPPINGS.items():
            for pattern in patterns:
                if pattern.lower() in field_label_lower or field_label_lower in pattern.lower():
                    return data_key
        
        return None
    
    @classmethod
    def map_data_to_field(cls, field_label: str, app_data: dict) -> Optional[str]:
        """Get the value for a field from application data"""
        mapping = cls.find_field_mapping(field_label)
        if not mapping:
            return None
        
        # Handle nested data (like address)
        if mapping == "address":
            addr = app_data.get("address", {})
            return addr.get("street", "")
        
        # Direct mappings
        if mapping == "website_url":
            return app_data.get("site_url", "")
        elif mapping == "website_name":
            return app_data.get("site_name", "")
        elif mapping == "description":
            return app_data.get("site_description", "")
        elif mapping == "category":
            return app_data.get("primary_category", "")
        elif mapping == "traffic":
            return app_data.get("estimated_monthly_traffic", "")
        elif mapping == "promotion_methods":
            methods = app_data.get("promotion_methods", [])
            return ", ".join(methods) if isinstance(methods, list) else methods
        
        # Check owner data
        return app_data.get(mapping, "")


class BrowserbaseIntegration:
    """Integration with Browserbase MCP for form filling"""
    
    def __init__(self, api_key: str = None, project_id: str = None):
        self.api_key = api_key or os.getenv("BROWSERBASE_API_KEY")
        self.project_id = project_id or os.getenv("BROWSERBASE_PROJECT_ID")
        self.session_id = None
    
    def create_session(self) -> str:
        """Create a new browser session"""
        # This would call Browserbase API
        # For now, return placeholder
        print("Creating Browserbase session...")
        self.session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        return self.session_id
    
    def navigate(self, url: str):
        """Navigate to URL"""
        print(f"Navigating to: {url}")
        # browserbase_navigate(url=url)
    
    def fill_field(self, selector: str, value: str):
        """Fill a form field"""
        print(f"Filling '{selector}' with: {value[:50]}...")
        # browserbase_fill(selector=selector, value=value)
    
    def select_option(self, selector: str, value: str):
        """Select dropdown option"""
        print(f"Selecting '{value}' in '{selector}'")
        # browserbase_select(selector=selector, value=value)
    
    def click(self, selector: str):
        """Click element"""
        print(f"Clicking: {selector}")
        # browserbase_click(selector=selector)
    
    def screenshot(self, filename: str) -> str:
        """Take screenshot"""
        print(f"Taking screenshot: {filename}")
        # browserbase_screenshot(filename=filename)
        return f"/screenshots/{filename}"
    
    def wait(self, seconds: float = 2):
        """Wait for page load"""
        time.sleep(seconds)
    
    def close_session(self):
        """Close browser session"""
        print("Closing session...")
        self.session_id = None


class ApplicationFiller:
    """Main class for filling affiliate applications"""
    
    NETWORK_APPLICATION_URLS = {
        "amazon": "https://affiliate-program.amazon.com/signup",
        "shareasale": "https://www.shareasale.com/info/affiliate-sign-up/",
        "cj": "https://signup.cj.com/member/signup/publisher/",
        "impact": "https://app.impact.com/signup",
        "awin": "https://ui.awin.com/awin/affiliate/",
        "rakuten": "https://rakutenadvertising.com/affiliate/",
        "clickbank": "https://accounts.clickbank.com/signup/"
    }
    
    def __init__(self, profiles_path: str = None):
        self.profile_loader = SiteProfileLoader(profiles_path)
        self.field_mapper = FormFieldMapper()
        self.browser = BrowserbaseIntegration()
        self.results: List[ApplicationResult] = []
    
    def get_application_url(self, network: str, custom_url: str = None) -> str:
        """Get application URL for a network"""
        if custom_url:
            return custom_url
        return self.NETWORK_APPLICATION_URLS.get(network.lower(), "")
    
    def prepare_form_data(self, site_id: str) -> Dict[str, str]:
        """Prepare all form data for a site"""
        return self.profile_loader.get_application_data(site_id)
    
    def fill_application(
        self,
        site_id: str,
        network: str,
        custom_url: str = None,
        dry_run: bool = False
    ) -> ApplicationResult:
        """Fill out an affiliate application"""
        
        url = self.get_application_url(network, custom_url)
        if not url:
            return ApplicationResult(
                network=network,
                site_id=site_id,
                url="",
                status="failed",
                timestamp=datetime.now().isoformat(),
                error_message=f"Unknown network: {network}"
            )
        
        app_data = self.prepare_form_data(site_id)
        if not app_data:
            return ApplicationResult(
                network=network,
                site_id=site_id,
                url=url,
                status="failed",
                timestamp=datetime.now().isoformat(),
                error_message=f"Site not found: {site_id}"
            )
        
        print(f"\n{'='*60}")
        print(f"FILLING APPLICATION: {network.upper()}")
        print(f"Site: {site_id}")
        print(f"URL: {url}")
        print(f"{'='*60}")
        
        if dry_run:
            print("\n[DRY RUN] Would fill the following fields:")
            for key, value in app_data.items():
                if value and key not in ['address', 'social_profiles']:
                    print(f"  {key}: {str(value)[:50]}...")
            
            return ApplicationResult(
                network=network,
                site_id=site_id,
                url=url,
                status="dry_run",
                timestamp=datetime.now().isoformat()
            )
        
        try:
            # Create browser session
            self.browser.create_session()
            
            # Navigate to application page
            self.browser.navigate(url)
            self.browser.wait(3)
            
            # Fill common fields
            field_sequence = self._get_fill_sequence(network)
            
            for field in field_sequence:
                value = self.field_mapper.map_data_to_field(field, app_data)
                if value:
                    if self._is_select_field(field):
                        self.browser.select_option(field, value)
                    else:
                        self.browser.fill_field(field, value)
                    self.browser.wait(0.5)
            
            # Screenshot before submit
            screenshot_pre = self.browser.screenshot(f"{site_id}_{network}_pre_submit.png")
            
            # Submit (commented out for safety)
            # self.browser.click("Submit")
            # self.browser.wait(3)
            
            # Screenshot confirmation
            # screenshot_post = self.browser.screenshot(f"{site_id}_{network}_confirmation.png")
            
            result = ApplicationResult(
                network=network,
                site_id=site_id,
                url=url,
                status="needs_review",  # Change to "submitted" when auto-submit enabled
                timestamp=datetime.now().isoformat(),
                screenshot_path=screenshot_pre
            )
            
        except Exception as e:
            result = ApplicationResult(
                network=network,
                site_id=site_id,
                url=url,
                status="failed",
                timestamp=datetime.now().isoformat(),
                error_message=str(e)
            )
        
        finally:
            self.browser.close_session()
        
        self.results.append(result)
        return result
    
    def _get_fill_sequence(self, network: str) -> List[str]:
        """Get the field fill sequence for a network"""
        # Generic sequence - would be customized per network
        return [
            "Website URL",
            "Website Name",
            "Website Description",
            "Category",
            "Email",
            "Name",
            "Phone",
            "Country"
        ]
    
    def _is_select_field(self, field_name: str) -> bool:
        """Check if field is a dropdown select"""
        select_fields = ["Category", "Country", "State", "Traffic"]
        return any(sf.lower() in field_name.lower() for sf in select_fields)
    
    def batch_apply(
        self,
        site_id: str,
        networks: List[str],
        dry_run: bool = False
    ) -> List[ApplicationResult]:
        """Apply to multiple networks for a single site"""
        results = []
        for network in networks:
            print(f"\nProcessing {network}...")
            result = self.fill_application(site_id, network, dry_run=dry_run)
            results.append(result)
            time.sleep(2)  # Pause between applications
        return results
    
    def export_results(self, output_path: str):
        """Export application results to JSON"""
        results_data = [
            {
                "network": r.network,
                "site_id": r.site_id,
                "url": r.url,
                "status": r.status,
                "timestamp": r.timestamp,
                "screenshot": r.screenshot_path,
                "confirmation_id": r.confirmation_id,
                "error": r.error_message
            }
            for r in self.results
        ]
        
        with open(output_path, 'w') as f:
            json.dump(results_data, f, indent=2)
        
        print(f"\nResults exported to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Affiliate Application Form Filler")
    parser.add_argument("--site", required=True, help="Site ID to apply for")
    parser.add_argument("--network", help="Network to apply to (amazon, shareasale, cj, etc.)")
    parser.add_argument("--networks", help="Comma-separated list of networks")
    parser.add_argument("--url", help="Custom application URL")
    parser.add_argument("--dry-run", action="store_true", help="Preview without submitting")
    parser.add_argument("--output", help="Output results file", default="application_results.json")
    parser.add_argument("--profiles", help="Path to site-profiles.json")
    
    args = parser.parse_args()
    
    filler = ApplicationFiller(args.profiles)
    
    if args.networks:
        networks = [n.strip() for n in args.networks.split(",")]
        results = filler.batch_apply(args.site, networks, dry_run=args.dry_run)
    elif args.network:
        result = filler.fill_application(
            args.site,
            args.network,
            custom_url=args.url,
            dry_run=args.dry_run
        )
        results = [result]
    else:
        print("Please specify --network or --networks")
        return
    
    # Print summary
    print("\n" + "="*60)
    print("APPLICATION SUMMARY")
    print("="*60)
    
    for r in results:
        status_emoji = {
            "submitted": "✅",
            "needs_review": "⚠️",
            "failed": "❌",
            "dry_run": "🔍"
        }.get(r.status, "❓")
        
        print(f"{status_emoji} {r.network}: {r.status}")
        if r.error_message:
            print(f"   Error: {r.error_message}")
    
    filler.export_results(args.output)


if __name__ == "__main__":
    main()
