#!/usr/bin/env python3
"""
Batch Site Auditor
Run comprehensive design audits across multiple sites.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Import local audit modules
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from css_auditor import CSSAuditor
from a11y_auditor import A11yAuditor


# Default site configuration for Nick's 17-site network
DEFAULT_SITES = [
    {
        "name": "Smart Home Wizards",
        "url": "https://smarthomewizards.com",
        "brand": "smarthome",
        "vertical": "tech"
    },
    {
        "name": "Witchcraft For Beginners",
        "url": "https://witchcraftforbeginners.com",
        "brand": "witchcraft",
        "vertical": "spirituality"
    },
    {
        "name": "Mythical Archives",
        "url": "https://mythicalarchives.com",
        "brand": "mythology",
        "vertical": "mythology"
    },
    {
        "name": "AI in Action Hub",
        "url": "https://aiinactionhub.com",
        "brand": "ai",
        "vertical": "tech"
    },
    {
        "name": "Family Flourish",
        "url": "https://family-flourish.com",
        "brand": "family",
        "vertical": "family"
    },
    {
        "name": "Bullet Journals",
        "url": "https://bulletjournals.net",
        "brand": "productivity",
        "vertical": "productivity"
    }
]


class BatchAuditor:
    """Run audits across multiple sites."""
    
    def __init__(self, sites, output_dir='./audit-reports'):
        self.sites = sites
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.results = []
        
    def run_full_audit(self, css_depth=2, a11y_level='AA', parallel=False):
        """Run all audits on all sites."""
        print("\n" + "=" * 70)
        print("🔍 BATCH SITE AUDITOR")
        print(f"   Sites: {len(self.sites)}")
        print(f"   CSS Depth: {css_depth}")
        print(f"   A11y Level: WCAG 2.1 {a11y_level}")
        print("=" * 70)
        
        if parallel:
            self._run_parallel(css_depth, a11y_level)
        else:
            self._run_sequential(css_depth, a11y_level)
        
        # Generate summary report
        summary = self._generate_summary()
        self._save_summary(summary)
        self._print_summary(summary)
        
        return summary
    
    def _run_sequential(self, css_depth, a11y_level):
        """Run audits one site at a time."""
        for i, site in enumerate(self.sites, 1):
            print(f"\n[{i}/{len(self.sites)}] {site['name']}")
            print("-" * 50)
            
            result = self._audit_site(site, css_depth, a11y_level)
            self.results.append(result)
    
    def _run_parallel(self, css_depth, a11y_level):
        """Run audits in parallel."""
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(
                    self._audit_site, site, css_depth, a11y_level
                ): site for site in self.sites
            }
            
            for future in as_completed(futures):
                site = futures[future]
                try:
                    result = future.result()
                    self.results.append(result)
                    status = "✅" if result['status'] == 'success' else "❌"
                    print(f"{status} {site['name']}: {result['total_issues']} issues")
                except Exception as e:
                    print(f"❌ {site['name']}: {e}")
    
    def _audit_site(self, site, css_depth, a11y_level):
        """Run all audits on a single site."""
        result = {
            'site': site['name'],
            'url': site['url'],
            'brand': site.get('brand', 'unknown'),
            'vertical': site.get('vertical', 'unknown'),
            'timestamp': datetime.now().isoformat(),
            'status': 'success',
            'audits': {}
        }
        
        try:
            # CSS Audit
            print(f"  📋 Running CSS audit...")
            css_auditor = CSSAuditor(
                site['url'], 
                site.get('tokens'),
                css_depth
            )
            css_report = css_auditor.audit()
            result['audits']['css'] = css_report
            
            # Save individual CSS report
            css_file = self.output_dir / f"{site['brand']}-css-{self.timestamp}.json"
            with open(css_file, 'w') as f:
                json.dump(css_report, f, indent=2)
            
            # Accessibility Audit
            print(f"  ♿ Running accessibility audit...")
            a11y_auditor = A11yAuditor(a11y_level)
            a11y_auditor.audit_url(site['url'])
            a11y_report = a11y_auditor.generate_report(site['url'])
            result['audits']['accessibility'] = a11y_report
            
            # Save individual a11y report
            a11y_file = self.output_dir / f"{site['brand']}-a11y-{self.timestamp}.json"
            with open(a11y_file, 'w') as f:
                json.dump(a11y_report, f, indent=2)
            
            # Calculate totals
            result['total_issues'] = (
                css_report['summary']['total_issues'] +
                a11y_report['summary']['total']
            )
            result['high_priority'] = (
                css_report['summary']['high'] +
                a11y_report['summary']['high']
            )
            
        except Exception as e:
            result['status'] = 'error'
            result['error'] = str(e)
            result['total_issues'] = 0
            result['high_priority'] = 0
        
        return result
    
    def _generate_summary(self):
        """Generate cross-site summary."""
        summary = {
            'timestamp': self.timestamp,
            'total_sites': len(self.results),
            'successful_audits': sum(1 for r in self.results if r['status'] == 'success'),
            'failed_audits': sum(1 for r in self.results if r['status'] == 'error'),
            'total_issues': sum(r.get('total_issues', 0) for r in self.results),
            'high_priority': sum(r.get('high_priority', 0) for r in self.results),
            'by_site': [],
            'by_vertical': {},
            'common_issues': {}
        }
        
        # Per-site breakdown
        for result in self.results:
            summary['by_site'].append({
                'name': result['site'],
                'url': result['url'],
                'brand': result['brand'],
                'total_issues': result.get('total_issues', 0),
                'high_priority': result.get('high_priority', 0),
                'status': result['status']
            })
        
        # By vertical
        verticals = {}
        for result in self.results:
            vertical = result.get('vertical', 'unknown')
            if vertical not in verticals:
                verticals[vertical] = {'sites': 0, 'issues': 0}
            verticals[vertical]['sites'] += 1
            verticals[vertical]['issues'] += result.get('total_issues', 0)
        summary['by_vertical'] = verticals
        
        # Find common issues
        issue_types = {}
        for result in self.results:
            if result['status'] != 'success':
                continue
            
            for audit_name, audit_data in result.get('audits', {}).items():
                for issue in audit_data.get('issues', []):
                    issue_type = issue.get('type', 'unknown')
                    if issue_type not in issue_types:
                        issue_types[issue_type] = 0
                    issue_types[issue_type] += 1
        
        # Sort by frequency
        summary['common_issues'] = dict(
            sorted(issue_types.items(), key=lambda x: x[1], reverse=True)[:10]
        )
        
        return summary
    
    def _save_summary(self, summary):
        """Save summary to files."""
        # JSON summary
        summary_file = self.output_dir / f"summary-{self.timestamp}.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # HTML report
        html_file = self.output_dir / f"summary-{self.timestamp}.html"
        html = self._generate_html_report(summary)
        with open(html_file, 'w') as f:
            f.write(html)
        
        print(f"\n📄 Reports saved to {self.output_dir}/")
    
    def _generate_html_report(self, summary):
        """Generate HTML summary report."""
        sites_html = ""
        for site in sorted(summary['by_site'], 
                          key=lambda x: x['high_priority'], reverse=True):
            status_class = 'success' if site['status'] == 'success' else 'error'
            priority_class = 'danger' if site['high_priority'] > 5 else 'warning' if site['high_priority'] > 0 else 'good'
            
            sites_html += f"""
            <tr class="{status_class}">
                <td><a href="{site['url']}" target="_blank">{site['name']}</a></td>
                <td>{site['brand']}</td>
                <td>{site['total_issues']}</td>
                <td class="{priority_class}">{site['high_priority']}</td>
                <td>{site['status']}</td>
            </tr>
            """
        
        common_issues_html = ""
        for issue_type, count in summary['common_issues'].items():
            common_issues_html += f"<li><strong>{issue_type}</strong>: {count} occurrences</li>"
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Batch Site Audit Report</title>
    <style>
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1200px; margin: 0 auto; padding: 20px;
            background: #f5f5f5;
        }}
        h1 {{ color: #333; }}
        .summary-cards {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 20px 0; }}
        .card {{ background: white; padding: 20px; border-radius: 8px; text-align: center; }}
        .card h3 {{ margin: 0; color: #666; font-size: 14px; }}
        .card .number {{ font-size: 36px; font-weight: bold; margin: 10px 0; }}
        .card.danger .number {{ color: #e74c3c; }}
        .card.warning .number {{ color: #f39c12; }}
        .card.good .number {{ color: #27ae60; }}
        table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background: #333; color: white; }}
        tr:hover {{ background: #f9f9f9; }}
        .danger {{ color: #e74c3c; font-weight: bold; }}
        .warning {{ color: #f39c12; }}
        .good {{ color: #27ae60; }}
        .error {{ background: #fee; }}
        .common-issues {{ background: white; padding: 20px; border-radius: 8px; margin-top: 20px; }}
    </style>
</head>
<body>
    <h1>🔍 Batch Site Audit Report</h1>
    <p>Generated: {summary['timestamp']}</p>
    
    <div class="summary-cards">
        <div class="card">
            <h3>Sites Audited</h3>
            <div class="number">{summary['total_sites']}</div>
        </div>
        <div class="card">
            <h3>Total Issues</h3>
            <div class="number">{summary['total_issues']}</div>
        </div>
        <div class="card danger">
            <h3>High Priority</h3>
            <div class="number">{summary['high_priority']}</div>
        </div>
        <div class="card {'danger' if summary['failed_audits'] > 0 else 'good'}">
            <h3>Failed Audits</h3>
            <div class="number">{summary['failed_audits']}</div>
        </div>
    </div>
    
    <h2>Sites Overview</h2>
    <table>
        <thead>
            <tr>
                <th>Site</th>
                <th>Brand</th>
                <th>Total Issues</th>
                <th>High Priority</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {sites_html}
        </tbody>
    </table>
    
    <div class="common-issues">
        <h2>Most Common Issues</h2>
        <ol>
            {common_issues_html}
        </ol>
    </div>
</body>
</html>
"""
    
    def _print_summary(self, summary):
        """Print summary to console."""
        print("\n" + "=" * 70)
        print("📊 AUDIT SUMMARY")
        print("=" * 70)
        print(f"Sites Audited: {summary['total_sites']}")
        print(f"Successful: {summary['successful_audits']}")
        print(f"Failed: {summary['failed_audits']}")
        print(f"\nTotal Issues: {summary['total_issues']}")
        print(f"High Priority: {summary['high_priority']}")
        
        print("\n📈 By Vertical:")
        for vertical, data in summary['by_vertical'].items():
            print(f"  {vertical}: {data['sites']} sites, {data['issues']} issues")
        
        print("\n🔥 Most Common Issues:")
        for issue_type, count in list(summary['common_issues'].items())[:5]:
            print(f"  • {issue_type}: {count}")
        
        # Flag sites needing attention
        problem_sites = [s for s in summary['by_site'] if s['high_priority'] > 5]
        if problem_sites:
            print("\n⚠️  SITES NEEDING IMMEDIATE ATTENTION:")
            for site in problem_sites:
                print(f"  🔴 {site['name']}: {site['high_priority']} high-priority issues")


def main():
    parser = argparse.ArgumentParser(description='Batch Site Auditor')
    parser.add_argument('--config', '-c', help='Sites config JSON file')
    parser.add_argument('--output', '-o', default='./audit-reports',
                        help='Output directory')
    parser.add_argument('--depth', '-d', type=int, default=2,
                        help='CSS crawl depth')
    parser.add_argument('--level', '-l', choices=['A', 'AA', 'AAA'],
                        default='AA', help='WCAG conformance level')
    parser.add_argument('--parallel', '-p', action='store_true',
                        help='Run audits in parallel')
    parser.add_argument('--sites', '-s', nargs='+',
                        help='Specific site URLs to audit')
    
    args = parser.parse_args()
    
    # Load sites config
    if args.config:
        with open(args.config) as f:
            config = json.load(f)
            sites = config.get('sites', [])
    elif args.sites:
        sites = [{'name': url, 'url': url, 'brand': 'custom'} for url in args.sites]
    else:
        print("Using default site configuration...")
        sites = DEFAULT_SITES
    
    auditor = BatchAuditor(sites, args.output)
    summary = auditor.run_full_audit(
        css_depth=args.depth,
        a11y_level=args.level,
        parallel=args.parallel
    )
    
    # Return exit code based on high priority issues
    return 1 if summary['high_priority'] > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
