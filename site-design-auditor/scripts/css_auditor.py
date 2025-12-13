#!/usr/bin/env python3
"""
CSS Consistency Auditor
Crawls websites and detects CSS inconsistencies, inline style abuse,
!important overuse, and design token violations.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "requests", "beautifulsoup4", "--break-system-packages", "-q"])
    import requests
    from bs4 import BeautifulSoup


class CSSAuditor:
    def __init__(self, base_url, tokens_file=None, max_depth=3):
        self.base_url = base_url.rstrip('/')
        self.domain = urlparse(base_url).netloc
        self.max_depth = max_depth
        self.visited = set()
        self.issues = []
        self.tokens = self._load_tokens(tokens_file) if tokens_file else {}
        self.css_stats = defaultdict(int)
        
    def _load_tokens(self, filepath):
        """Load design tokens from JSON file."""
        try:
            with open(filepath) as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load tokens file: {e}")
            return {}
    
    def audit(self):
        """Run full site audit."""
        print(f"\n🔍 Auditing {self.base_url}")
        print("=" * 60)
        
        self._crawl(self.base_url, 0)
        
        return self._generate_report()
    
    def _crawl(self, url, depth):
        """Recursively crawl site pages."""
        if depth > self.max_depth or url in self.visited:
            return
            
        # Normalize URL
        if not url.startswith('http'):
            url = urljoin(self.base_url, url)
            
        # Stay on same domain
        if urlparse(url).netloc != self.domain:
            return
            
        self.visited.add(url)
        print(f"  Scanning: {url}")
        
        try:
            response = requests.get(url, timeout=10, headers={
                'User-Agent': 'SiteDesignAuditor/1.0'
            })
            response.raise_for_status()
        except Exception as e:
            self.issues.append({
                'type': 'crawl_error',
                'severity': 'low',
                'location': url,
                'message': str(e)
            })
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Run audits on this page
        self._audit_inline_styles(soup, url)
        self._audit_important_abuse(soup, url)
        self._audit_color_consistency(soup, url)
        self._audit_typography(soup, url)
        self._audit_css_variables(soup, url)
        
        # Find more links
        for link in soup.find_all('a', href=True):
            href = link['href']
            if not href.startswith(('#', 'mailto:', 'tel:', 'javascript:')):
                self._crawl(href, depth + 1)
    
    def _audit_inline_styles(self, soup, url):
        """Detect inline styles that should be in CSS."""
        elements_with_style = soup.find_all(style=True)
        
        for elem in elements_with_style:
            style = elem.get('style', '')
            
            # Flag concerning inline styles
            concerns = []
            if 'color:' in style.lower():
                concerns.append('color')
            if 'font-' in style.lower():
                concerns.append('font')
            if 'background' in style.lower():
                concerns.append('background')
            if 'margin' in style.lower() or 'padding' in style.lower():
                concerns.append('spacing')
                
            if concerns:
                self.issues.append({
                    'type': 'inline_style',
                    'severity': 'medium',
                    'location': url,
                    'element': elem.name,
                    'selector': self._get_selector(elem),
                    'style': style[:100],
                    'concerns': concerns,
                    'fix': f"Move {', '.join(concerns)} to CSS class using design tokens"
                })
                self.css_stats['inline_styles'] += 1
    
    def _audit_important_abuse(self, soup, url):
        """Detect !important overuse in style tags and inline styles."""
        # Check inline styles
        for elem in soup.find_all(style=True):
            style = elem.get('style', '')
            important_count = style.lower().count('!important')
            if important_count > 0:
                self.issues.append({
                    'type': 'important_abuse',
                    'severity': 'high',
                    'location': url,
                    'selector': self._get_selector(elem),
                    'count': important_count,
                    'fix': "Remove !important and fix CSS specificity instead"
                })
                self.css_stats['important_count'] += important_count
        
        # Check style tags
        for style_tag in soup.find_all('style'):
            content = style_tag.string or ''
            important_count = content.lower().count('!important')
            if important_count > 3:  # Threshold for concern
                self.issues.append({
                    'type': 'important_abuse',
                    'severity': 'high',
                    'location': url,
                    'selector': 'style tag',
                    'count': important_count,
                    'fix': "Refactor CSS to avoid !important dependency"
                })
                self.css_stats['important_count'] += important_count
    
    def _audit_color_consistency(self, soup, url):
        """Check colors against design tokens."""
        if not self.tokens.get('colors'):
            return
            
        token_colors = set(v.lower() for v in self.tokens['colors'].values())
        
        # Find all color declarations
        color_pattern = re.compile(r'#[0-9a-fA-F]{3,6}|rgb\([^)]+\)|rgba\([^)]+\)')
        
        for elem in soup.find_all(style=True):
            style = elem.get('style', '')
            colors = color_pattern.findall(style)
            
            for color in colors:
                color_lower = color.lower()
                if color_lower not in token_colors and not color_lower.startswith('rgba'):
                    self.issues.append({
                        'type': 'color_inconsistency',
                        'severity': 'medium',
                        'location': url,
                        'selector': self._get_selector(elem),
                        'found_color': color,
                        'expected': 'Use CSS variable from design tokens',
                        'fix': f"Replace {color} with var(--color-*)"
                    })
                    self.css_stats['color_violations'] += 1
    
    def _audit_typography(self, soup, url):
        """Check typography consistency."""
        # Check for font declarations in inline styles
        font_pattern = re.compile(r'font-family:\s*([^;]+)')
        
        for elem in soup.find_all(style=True):
            style = elem.get('style', '')
            fonts = font_pattern.findall(style)
            
            for font in fonts:
                self.issues.append({
                    'type': 'inline_typography',
                    'severity': 'medium',
                    'location': url,
                    'selector': self._get_selector(elem),
                    'font': font.strip(),
                    'fix': "Use CSS class with var(--font-family-*)"
                })
                self.css_stats['typography_violations'] += 1
    
    def _audit_css_variables(self, soup, url):
        """Check for proper CSS variable usage."""
        # Look for hardcoded values that should be variables
        style_content = ''
        for style_tag in soup.find_all('style'):
            style_content += style_tag.string or ''
        
        # Check for hardcoded spacing values
        spacing_pattern = re.compile(r':\s*([\d.]+)(px|rem|em)\s*[;}]')
        matches = spacing_pattern.findall(style_content)
        
        common_values = defaultdict(int)
        for value, unit in matches:
            common_values[f"{value}{unit}"] += 1
        
        # Report frequently repeated values
        for value, count in common_values.items():
            if count > 5:
                self.issues.append({
                    'type': 'missing_variable',
                    'severity': 'low',
                    'location': url,
                    'value': value,
                    'occurrences': count,
                    'fix': f"Create CSS variable for repeated value {value}"
                })
    
    def _get_selector(self, elem):
        """Generate a CSS-like selector for an element."""
        selector = elem.name
        if elem.get('id'):
            selector += f"#{elem['id']}"
        if elem.get('class'):
            selector += '.' + '.'.join(elem['class'][:2])
        return selector
    
    def _generate_report(self):
        """Generate audit report."""
        # Categorize issues
        by_severity = defaultdict(list)
        by_type = defaultdict(list)
        
        for issue in self.issues:
            by_severity[issue['severity']].append(issue)
            by_type[issue['type']].append(issue)
        
        report = {
            'site': self.base_url,
            'timestamp': datetime.now().isoformat(),
            'pages_scanned': len(self.visited),
            'issues': self.issues,
            'summary': {
                'total_issues': len(self.issues),
                'high': len(by_severity['high']),
                'medium': len(by_severity['medium']),
                'low': len(by_severity['low'])
            },
            'by_type': {k: len(v) for k, v in by_type.items()},
            'stats': dict(self.css_stats)
        }
        
        return report
    
    def print_summary(self, report):
        """Print human-readable summary."""
        print("\n" + "=" * 60)
        print("📊 AUDIT SUMMARY")
        print("=" * 60)
        print(f"Site: {report['site']}")
        print(f"Pages Scanned: {report['pages_scanned']}")
        print(f"Total Issues: {report['summary']['total_issues']}")
        print(f"  🔴 High: {report['summary']['high']}")
        print(f"  🟡 Medium: {report['summary']['medium']}")
        print(f"  🟢 Low: {report['summary']['low']}")
        
        print("\nIssues by Type:")
        for issue_type, count in report['by_type'].items():
            print(f"  • {issue_type}: {count}")
        
        if report['summary']['high'] > 0:
            print("\n⚠️  HIGH PRIORITY FIXES:")
            for issue in report['issues']:
                if issue['severity'] == 'high':
                    print(f"  → {issue['type']} at {issue['location']}")
                    if 'fix' in issue:
                        print(f"    Fix: {issue['fix']}")


def main():
    parser = argparse.ArgumentParser(description='CSS Consistency Auditor')
    parser.add_argument('url', help='URL to audit')
    parser.add_argument('--tokens', '-t', help='Design tokens JSON file')
    parser.add_argument('--output', '-o', help='Output JSON file')
    parser.add_argument('--depth', '-d', type=int, default=3, help='Max crawl depth')
    
    args = parser.parse_args()
    
    auditor = CSSAuditor(args.url, args.tokens, args.depth)
    report = auditor.audit()
    auditor.print_summary(report)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n📄 Full report saved to: {args.output}")
    
    # Return exit code based on high severity issues
    return 1 if report['summary']['high'] > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
