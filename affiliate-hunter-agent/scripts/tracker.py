#!/usr/bin/env python3
"""
Affiliate Application & Opportunity Tracker

Track, update, and report on affiliate marketing activities.
Supports JSON file storage or Airtable integration.

Usage:
    python tracker.py add --program "Amazon Associates" --site "witchcraft-beginners" --status "applied"
    python tracker.py list --status pending
    python tracker.py update --id opp_123 --status approved --link "https://..."
    python tracker.py report --format summary
"""

import json
import argparse
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict
from dataclasses import dataclass, asdict, field
import uuid


@dataclass
class TrackedOpportunity:
    """A tracked affiliate opportunity"""
    id: str
    program_name: str
    network: str
    merchant: str
    site_id: str
    url: str
    commission_rate: str = ""
    cookie_duration: str = ""
    score: int = 0
    status: str = "discovered"
    discovered_date: str = ""
    applied_date: str = ""
    status_updated: str = ""
    affiliate_link: str = ""
    notes: str = ""
    screenshots: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.id:
            self.id = f"opp_{uuid.uuid4().hex[:8]}"
        if not self.discovered_date:
            self.discovered_date = datetime.now().strftime("%Y-%m-%d")


class AffiliateTracker:
    """Main tracker class for managing affiliate opportunities"""
    
    STATUS_FLOW = {
        "discovered": ["qualified", "skipped"],
        "qualified": ["applied", "skipped"],
        "applied": ["pending"],
        "pending": ["approved", "rejected"],
        "approved": ["active"],
        "rejected": ["applied"],  # Can re-apply
        "active": ["paused", "terminated"],
        "skipped": ["qualified"]  # Can reconsider
    }
    
    def __init__(self, storage_path: str = None):
        self.storage_path = storage_path or Path.home() / ".affiliate_tracker" / "opportunities.json"
        self.storage_path = Path(self.storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.opportunities = self._load_opportunities()
    
    def _load_opportunities(self) -> Dict[str, TrackedOpportunity]:
        """Load opportunities from storage"""
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                data = json.load(f)
                return {
                    opp_id: TrackedOpportunity(**opp_data)
                    for opp_id, opp_data in data.items()
                }
        return {}
    
    def _save_opportunities(self):
        """Save opportunities to storage"""
        data = {
            opp_id: asdict(opp)
            for opp_id, opp in self.opportunities.items()
        }
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_opportunity(self, **kwargs) -> TrackedOpportunity:
        """Add a new opportunity"""
        opp = TrackedOpportunity(**kwargs)
        self.opportunities[opp.id] = opp
        self._save_opportunities()
        return opp
    
    def get_opportunity(self, opp_id: str) -> Optional[TrackedOpportunity]:
        """Get opportunity by ID"""
        return self.opportunities.get(opp_id)
    
    def update_opportunity(self, opp_id: str, **updates) -> Optional[TrackedOpportunity]:
        """Update an existing opportunity"""
        opp = self.opportunities.get(opp_id)
        if not opp:
            return None
        
        for key, value in updates.items():
            if hasattr(opp, key):
                setattr(opp, key, value)
        
        opp.status_updated = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Auto-set applied_date when status changes to applied
        if updates.get("status") == "applied" and not opp.applied_date:
            opp.applied_date = datetime.now().strftime("%Y-%m-%d")
        
        self.opportunities[opp_id] = opp
        self._save_opportunities()
        return opp
    
    def update_status(self, opp_id: str, new_status: str) -> Optional[TrackedOpportunity]:
        """Update opportunity status with validation"""
        opp = self.opportunities.get(opp_id)
        if not opp:
            return None
        
        current_status = opp.status
        allowed_transitions = self.STATUS_FLOW.get(current_status, [])
        
        if new_status not in allowed_transitions and new_status != current_status:
            print(f"Warning: Unusual status transition from '{current_status}' to '{new_status}'")
        
        return self.update_opportunity(opp_id, status=new_status)
    
    def list_opportunities(
        self,
        status: str = None,
        site_id: str = None,
        network: str = None,
        min_score: int = None
    ) -> List[TrackedOpportunity]:
        """List opportunities with filters"""
        results = list(self.opportunities.values())
        
        if status:
            results = [o for o in results if o.status == status]
        if site_id:
            results = [o for o in results if o.site_id == site_id]
        if network:
            results = [o for o in results if o.network.lower() == network.lower()]
        if min_score:
            results = [o for o in results if o.score >= min_score]
        
        return sorted(results, key=lambda x: x.score, reverse=True)
    
    def get_pending_applications(self, days_old: int = 3) -> List[TrackedOpportunity]:
        """Get applications pending longer than X days"""
        cutoff = datetime.now() - timedelta(days=days_old)
        pending = self.list_opportunities(status="pending")
        
        return [
            o for o in pending
            if o.applied_date and datetime.strptime(o.applied_date, "%Y-%m-%d") < cutoff
        ]
    
    def import_from_discovery(self, discovery_results: List[dict], site_id: str):
        """Import opportunities from discovery scanner results"""
        for result in discovery_results:
            # Check if already tracked
            existing = [
                o for o in self.opportunities.values()
                if o.url == result.get("url") and o.site_id == site_id
            ]
            
            if not existing:
                self.add_opportunity(
                    program_name=result.get("program_name", "Unknown"),
                    network=result.get("network", "Unknown"),
                    merchant=result.get("merchant", "Unknown"),
                    site_id=site_id,
                    url=result.get("url", ""),
                    commission_rate=result.get("commission_rate", ""),
                    cookie_duration=result.get("cookie_duration", ""),
                    score=result.get("score", 0),
                    notes=result.get("notes", "")
                )
    
    def generate_report(self, report_type: str = "summary") -> dict:
        """Generate tracking report"""
        all_opps = list(self.opportunities.values())
        
        if report_type == "summary":
            by_status = {}
            for opp in all_opps:
                by_status[opp.status] = by_status.get(opp.status, 0) + 1
            
            by_site = {}
            for opp in all_opps:
                by_site[opp.site_id] = by_site.get(opp.site_id, 0) + 1
            
            by_network = {}
            for opp in all_opps:
                by_network[opp.network] = by_network.get(opp.network, 0) + 1
            
            active = [o for o in all_opps if o.status == "active"]
            
            return {
                "total_opportunities": len(all_opps),
                "by_status": by_status,
                "by_site": by_site,
                "by_network": by_network,
                "active_programs": len(active),
                "pending_applications": len([o for o in all_opps if o.status == "pending"]),
                "high_priority_discovered": len([o for o in all_opps if o.status == "discovered" and o.score >= 70])
            }
        
        elif report_type == "action_items":
            return {
                "ready_to_apply": self.list_opportunities(status="qualified"),
                "pending_follow_up": self.get_pending_applications(days_old=7),
                "high_value_discovered": [
                    o for o in self.list_opportunities(status="discovered")
                    if o.score >= 70
                ]
            }
        
        elif report_type == "revenue":
            active = self.list_opportunities(status="active")
            return {
                "active_programs": [
                    {
                        "program": o.program_name,
                        "site": o.site_id,
                        "commission": o.commission_rate,
                        "link": o.affiliate_link
                    }
                    for o in active
                ]
            }
        
        return {}
    
    def export_to_csv(self, output_path: str):
        """Export all opportunities to CSV"""
        import csv
        
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                "ID", "Program", "Network", "Merchant", "Site",
                "Commission", "Cookie", "Score", "Status",
                "Discovered", "Applied", "Link", "URL"
            ])
            
            for opp in self.opportunities.values():
                writer.writerow([
                    opp.id, opp.program_name, opp.network, opp.merchant,
                    opp.site_id, opp.commission_rate, opp.cookie_duration,
                    opp.score, opp.status, opp.discovered_date,
                    opp.applied_date, opp.affiliate_link, opp.url
                ])
        
        print(f"Exported {len(self.opportunities)} opportunities to {output_path}")


def format_opportunity(opp: TrackedOpportunity) -> str:
    """Format opportunity for display"""
    status_emoji = {
        "discovered": "🔍",
        "qualified": "⭐",
        "applied": "📤",
        "pending": "⏳",
        "approved": "✅",
        "rejected": "❌",
        "active": "💰",
        "skipped": "⏭️"
    }.get(opp.status, "❓")
    
    return (
        f"{status_emoji} [{opp.id}] {opp.program_name} ({opp.network})\n"
        f"   Site: {opp.site_id} | Score: {opp.score} | Status: {opp.status}\n"
        f"   Commission: {opp.commission_rate} | Cookie: {opp.cookie_duration}\n"
        f"   {opp.url}"
    )


def main():
    parser = argparse.ArgumentParser(description="Affiliate Opportunity Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add new opportunity")
    add_parser.add_argument("--program", required=True, help="Program name")
    add_parser.add_argument("--network", required=True, help="Affiliate network")
    add_parser.add_argument("--site", required=True, help="Site ID")
    add_parser.add_argument("--merchant", default="", help="Merchant name")
    add_parser.add_argument("--url", default="", help="Application URL")
    add_parser.add_argument("--commission", default="", help="Commission rate")
    add_parser.add_argument("--cookie", default="", help="Cookie duration")
    add_parser.add_argument("--score", type=int, default=0, help="Quality score")
    add_parser.add_argument("--status", default="discovered", help="Initial status")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List opportunities")
    list_parser.add_argument("--status", help="Filter by status")
    list_parser.add_argument("--site", help="Filter by site")
    list_parser.add_argument("--network", help="Filter by network")
    list_parser.add_argument("--min-score", type=int, help="Minimum score")
    
    # Update command
    update_parser = subparsers.add_parser("update", help="Update opportunity")
    update_parser.add_argument("--id", required=True, help="Opportunity ID")
    update_parser.add_argument("--status", help="New status")
    update_parser.add_argument("--link", help="Affiliate link (when approved)")
    update_parser.add_argument("--notes", help="Add notes")
    
    # Report command
    report_parser = subparsers.add_parser("report", help="Generate report")
    report_parser.add_argument("--format", default="summary", 
                               choices=["summary", "action_items", "revenue"])
    
    # Export command
    export_parser = subparsers.add_parser("export", help="Export to CSV")
    export_parser.add_argument("--output", default="affiliate_tracker_export.csv")
    
    # Import command
    import_parser = subparsers.add_parser("import", help="Import from discovery JSON")
    import_parser.add_argument("--file", required=True, help="JSON file path")
    import_parser.add_argument("--site", required=True, help="Site ID")
    
    args = parser.parse_args()
    tracker = AffiliateTracker()
    
    if args.command == "add":
        opp = tracker.add_opportunity(
            program_name=args.program,
            network=args.network,
            site_id=args.site,
            merchant=args.merchant,
            url=args.url,
            commission_rate=args.commission,
            cookie_duration=args.cookie,
            score=args.score,
            status=args.status
        )
        print(f"Added opportunity: {opp.id}")
        print(format_opportunity(opp))
    
    elif args.command == "list":
        opps = tracker.list_opportunities(
            status=args.status,
            site_id=args.site,
            network=args.network,
            min_score=args.min_score
        )
        print(f"\n{'='*60}")
        print(f"Found {len(opps)} opportunities")
        print('='*60)
        for opp in opps:
            print(format_opportunity(opp))
            print()
    
    elif args.command == "update":
        updates = {}
        if args.status:
            updates["status"] = args.status
        if args.link:
            updates["affiliate_link"] = args.link
        if args.notes:
            updates["notes"] = args.notes
        
        opp = tracker.update_opportunity(args.id, **updates)
        if opp:
            print("Updated opportunity:")
            print(format_opportunity(opp))
        else:
            print(f"Opportunity not found: {args.id}")
    
    elif args.command == "report":
        report = tracker.generate_report(args.format)
        print(f"\n{'='*60}")
        print(f"AFFILIATE TRACKING REPORT ({args.format.upper()})")
        print('='*60)
        print(json.dumps(report, indent=2, default=str))
    
    elif args.command == "export":
        tracker.export_to_csv(args.output)
    
    elif args.command == "import":
        with open(args.file, 'r') as f:
            results = json.load(f)
        tracker.import_from_discovery(results, args.site)
        print(f"Imported opportunities for {args.site}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
