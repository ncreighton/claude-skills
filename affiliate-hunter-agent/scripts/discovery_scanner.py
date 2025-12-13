#!/usr/bin/env python3
"""
Affiliate Opportunity Discovery Scanner

Searches for affiliate programs across niches and scores them for relevance.
Can be run standalone or integrated with n8n workflows.

Usage:
    python discovery_scanner.py --niche "witchcraft" --site "witchcraft-beginners"
    python discovery_scanner.py --all-sites --output results.json
"""

import json
import argparse
import os
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional
import re

# Optional imports - will use mocks if not available
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


@dataclass
class AffiliateOpportunity:
    """Represents a discovered affiliate opportunity"""
    program_name: str
    network: str
    merchant: str
    url: str
    commission_rate: str
    cookie_duration: str
    score: int
    niche: str
    site_id: str
    status: str = "discovered"
    discovered_date: str = ""
    notes: str = ""
    
    def __post_init__(self):
        if not self.discovered_date:
            self.discovered_date = datetime.now().strftime("%Y-%m-%d")


class AffiliateScoringEngine:
    """Scores affiliate opportunities based on multiple factors"""
    
    COMMISSION_SCORES = {
        "high": 25,      # >15%
        "medium": 20,    # 10-15%
        "low": 15,       # 5-10%
        "minimal": 10    # <5%
    }
    
    COOKIE_SCORES = {
        "excellent": 20,  # >30 days
        "good": 15,       # 15-30 days
        "fair": 10,       # 7-14 days
        "poor": 5         # <7 days
    }
    
    @classmethod
    def score_commission(cls, rate_str: str) -> int:
        """Score commission rate (0-25)"""
        try:
            # Extract number from strings like "10%", "10-15%", "$10 per sale"
            numbers = re.findall(r'(\d+(?:\.\d+)?)', rate_str)
            if numbers:
                rate = float(numbers[0])
                if '%' in rate_str:
                    if rate >= 15:
                        return cls.COMMISSION_SCORES["high"]
                    elif rate >= 10:
                        return cls.COMMISSION_SCORES["medium"]
                    elif rate >= 5:
                        return cls.COMMISSION_SCORES["low"]
                    else:
                        return cls.COMMISSION_SCORES["minimal"]
                else:  # Flat rate
                    if rate >= 50:
                        return cls.COMMISSION_SCORES["high"]
                    elif rate >= 20:
                        return cls.COMMISSION_SCORES["medium"]
                    else:
                        return cls.COMMISSION_SCORES["low"]
        except:
            pass
        return 10  # Default score
    
    @classmethod
    def score_cookie(cls, duration_str: str) -> int:
        """Score cookie duration (0-20)"""
        try:
            numbers = re.findall(r'(\d+)', duration_str)
            if numbers:
                days = int(numbers[0])
                if 'hour' in duration_str.lower():
                    days = 1
                elif 'week' in duration_str.lower():
                    days *= 7
                elif 'month' in duration_str.lower():
                    days *= 30
                
                if days > 30:
                    return cls.COOKIE_SCORES["excellent"]
                elif days >= 15:
                    return cls.COOKIE_SCORES["good"]
                elif days >= 7:
                    return cls.COOKIE_SCORES["fair"]
                else:
                    return cls.COOKIE_SCORES["poor"]
        except:
            pass
        return 10  # Default score
    
    @classmethod
    def score_niche_fit(cls, program_niche: str, target_niche: str) -> int:
        """Score niche fit (0-25)"""
        # Simple keyword matching - could be enhanced with embeddings
        program_niche = program_niche.lower()
        target_niche = target_niche.lower()
        
        if program_niche == target_niche:
            return 25
        
        # Check for keyword overlap
        program_words = set(program_niche.split())
        target_words = set(target_niche.split())
        overlap = program_words & target_words
        
        if len(overlap) > 0:
            return 15
        
        # Related niches mapping
        related = {
            "witchcraft": ["spiritual", "occult", "pagan", "metaphysical", "crystals"],
            "smart-home": ["technology", "iot", "home automation", "electronics", "security"],
            "ai-tech": ["software", "saas", "technology", "automation", "productivity"],
            "mythology": ["education", "books", "history", "culture", "entertainment"],
            "family": ["parenting", "kids", "baby", "home", "wellness"],
            "productivity": ["office", "planning", "organization", "stationery", "business"]
        }
        
        for niche, relations in related.items():
            if target_niche in niche or niche in target_niche:
                if any(r in program_niche for r in relations):
                    return 15
        
        return 5  # Tangential fit
    
    @classmethod
    def score_reputation(cls, network: str, merchant: str) -> int:
        """Score brand/network reputation (0-15)"""
        known_networks = ["amazon", "shareasale", "cj", "impact", "awin", "rakuten"]
        
        if any(n in network.lower() for n in known_networks):
            return 15
        
        # Could be enhanced with reputation API or database
        return 10
    
    @classmethod
    def score_payment(cls, threshold_str: str) -> int:
        """Score payment threshold (0-15)"""
        try:
            numbers = re.findall(r'\$?(\d+(?:\.\d+)?)', threshold_str)
            if numbers:
                threshold = float(numbers[0])
                if threshold <= 25:
                    return 15
                elif threshold <= 50:
                    return 10
                elif threshold <= 100:
                    return 5
                else:
                    return 3
        except:
            pass
        return 10
    
    @classmethod
    def calculate_total_score(cls, opportunity: dict, target_niche: str) -> int:
        """Calculate total score (0-100)"""
        score = 0
        score += cls.score_commission(opportunity.get("commission_rate", ""))
        score += cls.score_cookie(opportunity.get("cookie_duration", ""))
        score += cls.score_niche_fit(opportunity.get("niche", ""), target_niche)
        score += cls.score_reputation(
            opportunity.get("network", ""),
            opportunity.get("merchant", "")
        )
        score += cls.score_payment(opportunity.get("payment_threshold", "$50"))
        return min(100, score)


class DiscoveryScanner:
    """Main scanner class for finding affiliate opportunities"""
    
    def __init__(self, site_profiles_path: str = None):
        self.site_profiles = self._load_site_profiles(site_profiles_path)
        self.scorer = AffiliateScoringEngine()
        self.results = []
        
        if ANTHROPIC_AVAILABLE:
            self.client = anthropic.Anthropic()
        else:
            self.client = None
    
    def _load_site_profiles(self, path: str = None) -> dict:
        """Load site profiles from JSON"""
        if path is None:
            # Default path relative to skill
            path = Path(__file__).parent.parent / "references" / "site-profiles.json"
        
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Site profiles not found at {path}")
            return {"sites": []}
    
    def get_site_by_id(self, site_id: str) -> Optional[dict]:
        """Get site profile by ID"""
        for site in self.site_profiles.get("sites", []):
            if site.get("site_id") == site_id:
                return site
        return None
    
    def generate_search_queries(self, niche: str, keywords: list = None) -> list:
        """Generate search queries for affiliate discovery"""
        queries = [
            f"{niche} affiliate program",
            f"best {niche} affiliate programs 2025",
            f"{niche} partner program high commission",
            f"{niche} products affiliate",
            f"top {niche} affiliate offers"
        ]
        
        if keywords:
            for kw in keywords[:3]:  # Limit to top 3 keywords
                queries.append(f"{kw} affiliate program")
        
        return queries
    
    def discover_with_claude(self, niche: str, site_id: str) -> list:
        """Use Claude to discover and analyze affiliate programs"""
        if not self.client:
            print("Anthropic client not available. Using mock data.")
            return self._mock_discovery(niche)
        
        prompt = f"""You are an affiliate marketing expert. Find affiliate programs suitable for a {niche} content website.

For each program, provide:
1. Program name
2. Network (Amazon, ShareASale, CJ, Impact, Direct, etc.)
3. Merchant/Brand name
4. Application URL (if known)
5. Commission rate
6. Cookie duration
7. Why it's a good fit

Return as JSON array with these exact fields:
[
  {{
    "program_name": "Example Affiliate Program",
    "network": "ShareASale",
    "merchant": "Example Brand",
    "url": "https://example.com/affiliates",
    "commission_rate": "10%",
    "cookie_duration": "30 days",
    "fit_reason": "Great product match for audience"
  }}
]

Find 10-15 relevant programs. Focus on:
- High commission rates (10%+)
- Long cookie durations (30+ days)
- Reputable brands
- Products that match the {niche} audience

Return ONLY the JSON array, no other text."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Parse JSON from response
            content = response.content[0].text
            # Clean up potential markdown code blocks
            content = re.sub(r'^```json\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            
            programs = json.loads(content)
            
            # Score each program
            opportunities = []
            for p in programs:
                score = self.scorer.calculate_total_score(p, niche)
                opp = AffiliateOpportunity(
                    program_name=p.get("program_name", "Unknown"),
                    network=p.get("network", "Unknown"),
                    merchant=p.get("merchant", "Unknown"),
                    url=p.get("url", ""),
                    commission_rate=p.get("commission_rate", "Varies"),
                    cookie_duration=p.get("cookie_duration", "Unknown"),
                    score=score,
                    niche=niche,
                    site_id=site_id,
                    notes=p.get("fit_reason", "")
                )
                opportunities.append(opp)
            
            return opportunities
            
        except Exception as e:
            print(f"Error in Claude discovery: {e}")
            return []
    
    def _mock_discovery(self, niche: str) -> list:
        """Return mock data for testing without API"""
        mock_programs = [
            {
                "program_name": f"{niche.title()} Shop Affiliate",
                "network": "ShareASale",
                "merchant": f"Top {niche.title()} Store",
                "url": "https://shareasale.com/example",
                "commission_rate": "12%",
                "cookie_duration": "30 days",
                "niche": niche
            },
            {
                "program_name": "Amazon Associates",
                "network": "Amazon",
                "merchant": "Amazon",
                "url": "https://affiliate-program.amazon.com",
                "commission_rate": "4-10%",
                "cookie_duration": "24 hours",
                "niche": "general"
            }
        ]
        
        opportunities = []
        for p in mock_programs:
            score = self.scorer.calculate_total_score(p, niche)
            opp = AffiliateOpportunity(
                program_name=p["program_name"],
                network=p["network"],
                merchant=p["merchant"],
                url=p["url"],
                commission_rate=p["commission_rate"],
                cookie_duration=p["cookie_duration"],
                score=score,
                niche=niche,
                site_id="test-site"
            )
            opportunities.append(opp)
        
        return opportunities
    
    def scan_site(self, site_id: str) -> list:
        """Scan for opportunities for a specific site"""
        site = self.get_site_by_id(site_id)
        if not site:
            print(f"Site not found: {site_id}")
            return []
        
        niche = site.get("niche", "general")
        keywords = site.get("niche_keywords", [])
        
        print(f"Scanning opportunities for {site_id} ({niche})...")
        opportunities = self.discover_with_claude(niche, site_id)
        
        # Sort by score
        opportunities.sort(key=lambda x: x.score, reverse=True)
        
        return opportunities
    
    def scan_all_sites(self) -> dict:
        """Scan all sites in profile database"""
        all_results = {}
        
        for site in self.site_profiles.get("sites", []):
            site_id = site.get("site_id")
            if site_id and not site_id.startswith("site-"):  # Skip placeholder sites
                opportunities = self.scan_site(site_id)
                all_results[site_id] = [asdict(o) for o in opportunities]
        
        return all_results
    
    def export_results(self, results: list, output_path: str):
        """Export results to JSON file"""
        with open(output_path, 'w') as f:
            json.dump([asdict(r) if hasattr(r, '__dataclass_fields__') else r for r in results], f, indent=2)
        print(f"Results exported to {output_path}")
    
    def get_recommendations(self, opportunities: list, min_score: int = 70) -> dict:
        """Get action recommendations based on scores"""
        auto_apply = [o for o in opportunities if o.score >= min_score]
        review = [o for o in opportunities if 50 <= o.score < min_score]
        skip = [o for o in opportunities if o.score < 50]
        
        return {
            "auto_apply": auto_apply,
            "review_needed": review,
            "skip": skip,
            "summary": {
                "total": len(opportunities),
                "high_priority": len(auto_apply),
                "review": len(review),
                "skipped": len(skip)
            }
        }


def main():
    parser = argparse.ArgumentParser(description="Affiliate Opportunity Discovery Scanner")
    parser.add_argument("--niche", help="Niche to search for")
    parser.add_argument("--site", help="Site ID to scan for")
    parser.add_argument("--all-sites", action="store_true", help="Scan all sites")
    parser.add_argument("--output", help="Output file path", default="affiliate_opportunities.json")
    parser.add_argument("--profiles", help="Path to site-profiles.json")
    parser.add_argument("--min-score", type=int, default=70, help="Minimum score for auto-apply")
    
    args = parser.parse_args()
    
    scanner = DiscoveryScanner(args.profiles)
    
    if args.all_sites:
        results = scanner.scan_all_sites()
        scanner.export_results(results, args.output)
    elif args.site:
        opportunities = scanner.scan_site(args.site)
        recommendations = scanner.get_recommendations(opportunities, args.min_score)
        
        print(f"\n=== Discovery Results for {args.site} ===")
        print(f"Total found: {recommendations['summary']['total']}")
        print(f"High priority (auto-apply): {recommendations['summary']['high_priority']}")
        print(f"Review needed: {recommendations['summary']['review']}")
        print(f"Skipped: {recommendations['summary']['skipped']}")
        
        if recommendations['auto_apply']:
            print("\n🎯 TOP OPPORTUNITIES (Auto-Apply Recommended):")
            for opp in recommendations['auto_apply'][:5]:
                print(f"  • {opp.program_name} ({opp.network}) - Score: {opp.score}")
                print(f"    Commission: {opp.commission_rate}, Cookie: {opp.cookie_duration}")
        
        scanner.export_results([asdict(o) for o in opportunities], args.output)
    elif args.niche:
        opportunities = scanner.discover_with_claude(args.niche, "manual-search")
        scanner.export_results(opportunities, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
