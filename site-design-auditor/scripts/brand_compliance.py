#!/usr/bin/env python3
"""
Brand Compliance Checker
Validates website against design tokens and brand guidelines.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime

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


class BrandComplianceChecker:
    """Check website compliance with brand design tokens."""
    
    def __init__(self, tokens_file):
        self.tokens = self._load_tokens(tokens_file)
        self.issues = []
        self.stats = defaultdict(int)
        
    def _load_tokens(self, filepath):
        """Load design tokens from JSON."""
        with open(filepath) as f:
            return json.load(f)
    
    def check_url(self, url):
        """Check a URL against brand tokens."""
        print(f"  Checking: {url}")
        
        try:
            response = requests.get(url, timeout=15, headers={
                'User-Agent': 'BrandChecker/1.0'
            })
            response.raise_for_status()
        except Exception as e:
            return {'error': str(e)}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Run all checks
        self._check_colors(soup, url)
        self._check_typography(soup, url)
        self._check_spacing(soup, url)
        self._check_css_variables(soup, url)
        
        return self._generate_report(url)
    
    def _check_colors(self, soup, url):
        """Check color usage against brand tokens."""
        if 'colors' not in self.tokens:
            return
        
        brand_colors = self.tokens['colors']
        
        # Normalize brand colors to lowercase hex
        normalized_brand = {}
        for name, value in brand_colors.items():
            if value.startswith('#'):
                # Normalize to 6-digit hex
                hex_val = value.lower()
                if len(hex_val) == 4:  # #RGB -> #RRGGBB
                    hex_val = f"#{hex_val[1]*2}{hex_val[2]*2}{hex_val[3]*2}"
                normalized_brand[name] = hex_val
        
        brand_hex_values = set(normalized_brand.values())
        
        # Find all color declarations
        color_pattern = re.compile(r'#[0-9a-fA-F]{3,6}')
        
        # Check inline styles
        for elem in soup.find_all(style=True):
            style = elem.get('style', '')
            colors = color_pattern.findall(style)
            
            for color in colors:
                normalized = self._normalize_hex(color)
                if normalized not in brand_hex_values:
                    self.issues.append({
                        'type': 'off_brand_color',
                        'severity': 'medium',
                        'location': url,
                        'selector': self._get_selector(elem),
                        'found': color,
                        'brand_colors': list(brand_colors.keys()),
                        'message': f'Color {color} not in brand palette',
                        'fix': f'Replace with brand color variable'
                    })
                    self.stats['off_brand_colors'] += 1
        
        # Check style tags
        for style_tag in soup.find_all('style'):
            content = style_tag.string or ''
            colors = color_pattern.findall(content)
            
            for color in colors:
                normalized = self._normalize_hex(color)
                if normalized not in brand_hex_values:
                    self.stats['off_brand_colors'] += 1
    
    def _check_typography(self, soup, url):
        """Check typography against brand tokens."""
        if 'typography' not in self.tokens:
            return
        
        typo = self.tokens['typography']
        brand_fonts = set()
        
        # Collect brand font families
        if 'fontFamily' in typo:
            for font_stack in typo['fontFamily'].values():
                # Extract first font name
                first_font = font_stack.split(',')[0].strip().strip('"\'')
                brand_fonts.add(first_font.lower())
        
        # Find font-family declarations
        font_pattern = re.compile(r'font-family:\s*([^;]+)')
        
        for elem in soup.find_all(style=True):
            style = elem.get('style', '')
            matches = font_pattern.findall(style)
            
            for font_stack in matches:
                first_font = font_stack.split(',')[0].strip().strip('"\'').lower()
                
                if first_font not in brand_fonts and first_font not in ['inherit', 'sans-serif', 'serif', 'monospace']:
                    self.issues.append({
                        'type': 'off_brand_font',
                        'severity': 'medium',
                        'location': url,
                        'selector': self._get_selector(elem),
                        'found': font_stack.strip(),
                        'brand_fonts': list(typo.get('fontFamily', {}).values()),
                        'message': f'Font "{first_font}" not in brand typography',
                        'fix': 'Use brand font variable'
                    })
                    self.stats['off_brand_fonts'] += 1
        
        # Check font sizes
        if 'fontSize' in typo:
            brand_sizes = set(typo['fontSize'].values())
            size_pattern = re.compile(r'font-size:\s*([^;]+)')
            
            for style_tag in soup.find_all('style'):
                content = style_tag.string or ''
                sizes = size_pattern.findall(content)
                
                for size in sizes:
                    size = size.strip()
                    if size not in brand_sizes and not size.startswith('var('):
                        self.stats['non_standard_sizes'] += 1
    
    def _check_spacing(self, soup, url):
        """Check spacing values against brand tokens."""
        if 'spacing' not in self.tokens:
            return
        
        brand_spacing = set(self.tokens['spacing'].values())
        spacing_pattern = re.compile(r'(?:margin|padding)(?:-(?:top|right|bottom|left))?:\s*([^;]+)')
        
        # Check style tags for non-standard spacing
        for style_tag in soup.find_all('style'):
            content = style_tag.string or ''
            matches = spacing_pattern.findall(content)
            
            for value in matches:
                # Skip shorthand with multiple values for now
                if ' ' in value.strip():
                    continue
                
                value = value.strip()
                if value not in brand_spacing and not value.startswith('var(') and value != '0':
                    self.stats['non_standard_spacing'] += 1
    
    def _check_css_variables(self, soup, url):
        """Check for proper CSS variable usage."""
        # Look for style tags that should use variables
        for style_tag in soup.find_all('style'):
            content = style_tag.string or ''
            
            # Count hardcoded vs variable usage
            hardcoded_colors = len(re.findall(r'#[0-9a-fA-F]{3,6}', content))
            variable_colors = len(re.findall(r'var\(--color', content))
            
            if hardcoded_colors > 0 and variable_colors == 0:
                self.issues.append({
                    'type': 'no_css_variables',
                    'severity': 'medium',
                    'location': url,
                    'hardcoded_count': hardcoded_colors,
                    'message': f'{hardcoded_colors} hardcoded colors, 0 CSS variables used',
                    'fix': 'Convert hardcoded values to CSS variables'
                })
    
    def _normalize_hex(self, hex_color):
        """Normalize hex color to 6-digit lowercase."""
        hex_val = hex_color.lower()
        if len(hex_val) == 4:
            hex_val = f"#{hex_val[1]*2}{hex_val[2]*2}{hex_val[3]*2}"
        return hex_val
    
    def _get_selector(self, elem):
        """Generate CSS-like selector."""
        selector = elem.name
        if elem.get('id'):
            selector += f"#{elem['id']}"
        elif elem.get('class'):
            selector += '.' + '.'.join(elem['class'][:2])
        return selector
    
    def _generate_report(self, url):
        """Generate compliance report."""
        by_severity = defaultdict(list)
        for issue in self.issues:
            by_severity[issue['severity']].append(issue)
        
        # Calculate compliance score
        total_checks = (
            self.stats.get('off_brand_colors', 0) +
            self.stats.get('off_brand_fonts', 0) +
            self.stats.get('non_standard_sizes', 0) +
            self.stats.get('non_standard_spacing', 0) +
            10  # baseline
        )
        violations = (
            self.stats.get('off_brand_colors', 0) +
            self.stats.get('off_brand_fonts', 0)
        )
        compliance_score = max(0, 100 - (violations * 5))
        
        return {
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'compliance_score': compliance_score,
            'issues': self.issues,
            'summary': {
                'total_issues': len(self.issues),
                'high': len(by_severity['high']),
                'medium': len(by_severity['medium']),
                'low': len(by_severity['low'])
            },
            'stats': dict(self.stats),
            'tokens_checked': list(self.tokens.keys())
        }
    
    def print_summary(self, report):
        """Print human-readable summary."""
        score_emoji = "🟢" if report['compliance_score'] >= 80 else "🟡" if report['compliance_score'] >= 60 else "🔴"
        
        print("\n" + "=" * 60)
        print("🎨 BRAND COMPLIANCE REPORT")
        print("=" * 60)
        print(f"URL: {report['url']}")
        print(f"\n{score_emoji} Compliance Score: {report['compliance_score']}%")
        print(f"\nTokens Checked: {', '.join(report['tokens_checked'])}")
        print(f"\nIssues Found: {report['summary']['total_issues']}")
        print(f"  🔴 High: {report['summary']['high']}")
        print(f"  🟡 Medium: {report['summary']['medium']}")
        print(f"  🟢 Low: {report['summary']['low']}")
        
        print("\nStats:")
        for stat, count in report['stats'].items():
            print(f"  • {stat.replace('_', ' ').title()}: {count}")
        
        if report['issues']:
            print("\n📋 Issues:")
            for issue in report['issues'][:10]:
                print(f"  • [{issue['severity']}] {issue['type']}")
                print(f"    {issue['message']}")


def main():
    parser = argparse.ArgumentParser(description='Brand Compliance Checker')
    parser.add_argument('url', help='URL to check')
    parser.add_argument('--tokens', '-t', required=True,
                        help='Design tokens JSON file')
    parser.add_argument('--output', '-o', help='Output JSON file')
    
    args = parser.parse_args()
    
    print(f"\n🎨 Brand Compliance Checker")
    print("=" * 60)
    
    checker = BrandComplianceChecker(args.tokens)
    report = checker.check_url(args.url)
    
    if 'error' in report:
        print(f"❌ Error: {report['error']}")
        return 1
    
    checker.print_summary(report)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n📄 Report saved: {args.output}")
    
    return 0 if report['compliance_score'] >= 70 else 1


if __name__ == '__main__':
    sys.exit(main())
