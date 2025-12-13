#!/usr/bin/env python3
"""
Accessibility Auditor
WCAG 2.1 compliance checker for websites.
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


class A11yAuditor:
    """WCAG 2.1 accessibility auditor."""
    
    # WCAG contrast ratios
    CONTRAST_NORMAL = 4.5  # Normal text
    CONTRAST_LARGE = 3.0   # Large text (18px+ or 14px+ bold)
    CONTRAST_UI = 3.0      # UI components
    
    # Touch target size (WCAG 2.5.5)
    MIN_TOUCH_TARGET = 44
    
    def __init__(self, level='AA'):
        self.level = level
        self.issues = []
        self.stats = defaultdict(int)
        
    def audit_url(self, url):
        """Audit a single URL."""
        print(f"  Auditing: {url}")
        
        try:
            response = requests.get(url, timeout=15, headers={
                'User-Agent': 'A11yAuditor/1.0'
            })
            response.raise_for_status()
        except Exception as e:
            self.issues.append({
                'type': 'crawl_error',
                'wcag': 'N/A',
                'severity': 'error',
                'location': url,
                'message': str(e)
            })
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Run all audits
        self._audit_images(soup, url)
        self._audit_headings(soup, url)
        self._audit_links(soup, url)
        self._audit_forms(soup, url)
        self._audit_landmarks(soup, url)
        self._audit_language(soup, url)
        self._audit_focus_indicators(soup, url)
        self._audit_color_contrast(soup, url)
        self._audit_touch_targets(soup, url)
        self._audit_skip_links(soup, url)
        self._audit_tables(soup, url)
        
    def _audit_images(self, soup, url):
        """Check images have alt text (WCAG 1.1.1)."""
        for img in soup.find_all('img'):
            src = img.get('src', 'unknown')
            
            if not img.has_attr('alt'):
                self.issues.append({
                    'type': 'missing_alt',
                    'wcag': '1.1.1',
                    'severity': 'high',
                    'location': url,
                    'element': f'img[src="{src[:50]}"]',
                    'message': 'Image missing alt attribute',
                    'fix': 'Add alt="" for decorative images or descriptive alt text for informative images'
                })
                self.stats['missing_alt'] += 1
            elif img.get('alt', '').strip() == '' and not img.get('role') == 'presentation':
                # Empty alt on non-decorative image
                if not any(cls in (img.get('class') or []) 
                          for cls in ['icon', 'decoration', 'bg']):
                    self.issues.append({
                        'type': 'empty_alt',
                        'wcag': '1.1.1',
                        'severity': 'medium',
                        'location': url,
                        'element': f'img[src="{src[:50]}"]',
                        'message': 'Image has empty alt text - verify if decorative',
                        'fix': 'Add role="presentation" for decorative images or add descriptive alt text'
                    })
                    self.stats['empty_alt'] += 1
    
    def _audit_headings(self, soup, url):
        """Check heading hierarchy (WCAG 1.3.1)."""
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        # Check for single h1
        h1_count = len(soup.find_all('h1'))
        if h1_count == 0:
            self.issues.append({
                'type': 'missing_h1',
                'wcag': '1.3.1',
                'severity': 'high',
                'location': url,
                'message': 'Page missing h1 element',
                'fix': 'Add a single h1 element as the main page heading'
            })
        elif h1_count > 1:
            self.issues.append({
                'type': 'multiple_h1',
                'wcag': '1.3.1',
                'severity': 'medium',
                'location': url,
                'message': f'Page has {h1_count} h1 elements (should be 1)',
                'fix': 'Use only one h1 per page'
            })
        
        # Check hierarchy
        prev_level = 0
        for heading in headings:
            level = int(heading.name[1])
            
            if prev_level > 0 and level > prev_level + 1:
                self.issues.append({
                    'type': 'heading_skip',
                    'wcag': '1.3.1',
                    'severity': 'medium',
                    'location': url,
                    'element': heading.name,
                    'text': heading.get_text()[:50],
                    'message': f'Heading skips from h{prev_level} to h{level}',
                    'fix': f'Use h{prev_level + 1} instead of h{level}'
                })
                self.stats['heading_skip'] += 1
            
            prev_level = level
    
    def _audit_links(self, soup, url):
        """Check link accessibility (WCAG 2.4.4)."""
        for link in soup.find_all('a', href=True):
            text = link.get_text(strip=True)
            aria_label = link.get('aria-label', '')
            title = link.get('title', '')
            
            # Check for meaningful link text
            accessible_name = text or aria_label or title
            
            if not accessible_name:
                self.issues.append({
                    'type': 'empty_link',
                    'wcag': '2.4.4',
                    'severity': 'high',
                    'location': url,
                    'element': str(link)[:100],
                    'message': 'Link has no accessible name',
                    'fix': 'Add link text or aria-label'
                })
                self.stats['empty_link'] += 1
            elif accessible_name.lower() in ['click here', 'here', 'read more', 
                                             'learn more', 'more', 'link']:
                self.issues.append({
                    'type': 'generic_link_text',
                    'wcag': '2.4.4',
                    'severity': 'medium',
                    'location': url,
                    'text': accessible_name,
                    'message': f'Link text "{accessible_name}" is not descriptive',
                    'fix': 'Use descriptive link text that makes sense out of context'
                })
                self.stats['generic_link'] += 1
    
    def _audit_forms(self, soup, url):
        """Check form accessibility (WCAG 1.3.1, 3.3.2)."""
        inputs = soup.find_all(['input', 'select', 'textarea'])
        
        for input_elem in inputs:
            input_type = input_elem.get('type', 'text')
            
            # Skip hidden and submit inputs
            if input_type in ['hidden', 'submit', 'button', 'reset']:
                continue
            
            input_id = input_elem.get('id', '')
            aria_label = input_elem.get('aria-label', '')
            aria_labelledby = input_elem.get('aria-labelledby', '')
            placeholder = input_elem.get('placeholder', '')
            
            # Check for label
            has_label = False
            if input_id:
                label = soup.find('label', attrs={'for': input_id})
                has_label = label is not None
            
            if not (has_label or aria_label or aria_labelledby):
                self.issues.append({
                    'type': 'missing_label',
                    'wcag': '1.3.1',
                    'severity': 'high',
                    'location': url,
                    'element': f'{input_elem.name}[type="{input_type}"]',
                    'message': 'Form input missing associated label',
                    'fix': 'Add <label for="inputId"> or aria-label'
                })
                self.stats['missing_label'] += 1
            
            # Check placeholder isn't the only label
            if placeholder and not (has_label or aria_label or aria_labelledby):
                self.issues.append({
                    'type': 'placeholder_only_label',
                    'wcag': '3.3.2',
                    'severity': 'medium',
                    'location': url,
                    'element': f'{input_elem.name}[placeholder="{placeholder}"]',
                    'message': 'Placeholder used as only label (disappears on input)',
                    'fix': 'Add persistent label element'
                })
    
    def _audit_landmarks(self, soup, url):
        """Check landmark regions (WCAG 1.3.1)."""
        # Check for main landmark
        main = soup.find('main') or soup.find(role='main')
        if not main:
            self.issues.append({
                'type': 'missing_main',
                'wcag': '1.3.1',
                'severity': 'medium',
                'location': url,
                'message': 'Page missing <main> landmark',
                'fix': 'Add <main> element to wrap primary content'
            })
        
        # Check for navigation
        nav = soup.find('nav') or soup.find(role='navigation')
        if not nav:
            self.issues.append({
                'type': 'missing_nav',
                'wcag': '1.3.1',
                'severity': 'low',
                'location': url,
                'message': 'Page missing <nav> landmark',
                'fix': 'Add <nav> element for main navigation'
            })
    
    def _audit_language(self, soup, url):
        """Check language attributes (WCAG 3.1.1)."""
        html = soup.find('html')
        if html and not html.get('lang'):
            self.issues.append({
                'type': 'missing_lang',
                'wcag': '3.1.1',
                'severity': 'high',
                'location': url,
                'message': 'HTML element missing lang attribute',
                'fix': 'Add lang="en" (or appropriate language code) to <html>'
            })
    
    def _audit_focus_indicators(self, soup, url):
        """Check for focus indicator removal (WCAG 2.4.7)."""
        # Check inline styles and style tags
        for style in soup.find_all('style'):
            content = style.string or ''
            if 'outline: none' in content or 'outline:none' in content:
                if ':focus' in content:
                    self.issues.append({
                        'type': 'focus_removed',
                        'wcag': '2.4.7',
                        'severity': 'high',
                        'location': url,
                        'message': 'Focus outline removed without replacement',
                        'fix': 'Provide visible focus indicator (custom outline or box-shadow)'
                    })
                    self.stats['focus_removed'] += 1
                    break
    
    def _audit_color_contrast(self, soup, url):
        """Check for potential contrast issues (WCAG 1.4.3)."""
        # Check inline styles for light colors on potentially light backgrounds
        light_colors = ['#fff', '#ffffff', '#f', '#ff', '#eee', '#ddd', '#ccc']
        
        for elem in soup.find_all(style=True):
            style = elem.get('style', '').lower()
            
            for color in light_colors:
                if f'color:{color}' in style or f'color: {color}' in style:
                    self.issues.append({
                        'type': 'potential_contrast',
                        'wcag': '1.4.3',
                        'severity': 'medium',
                        'location': url,
                        'element': self._get_selector(elem),
                        'message': f'Light text color ({color}) may have contrast issues',
                        'fix': 'Verify contrast ratio meets 4.5:1 for normal text'
                    })
                    self.stats['contrast_warning'] += 1
    
    def _audit_touch_targets(self, soup, url):
        """Check touch target sizes (WCAG 2.5.5)."""
        # Check inline styles for small buttons/links
        for elem in soup.find_all(['a', 'button', 'input'], style=True):
            style = elem.get('style', '')
            
            # Look for pixel sizes
            size_match = re.search(r'(?:width|height):\s*(\d+)px', style)
            if size_match:
                size = int(size_match.group(1))
                if size < self.MIN_TOUCH_TARGET:
                    self.issues.append({
                        'type': 'small_touch_target',
                        'wcag': '2.5.5',
                        'severity': 'medium',
                        'location': url,
                        'element': self._get_selector(elem),
                        'size': size,
                        'message': f'Touch target {size}px is below {self.MIN_TOUCH_TARGET}px minimum',
                        'fix': f'Increase clickable area to at least {self.MIN_TOUCH_TARGET}x{self.MIN_TOUCH_TARGET}px'
                    })
    
    def _audit_skip_links(self, soup, url):
        """Check for skip navigation link (WCAG 2.4.1)."""
        # Look for skip link in first few elements
        first_links = soup.find_all('a')[:5]
        has_skip = False
        
        for link in first_links:
            href = link.get('href', '')
            text = link.get_text(strip=True).lower()
            
            if href.startswith('#') and ('skip' in text or 'main' in text):
                has_skip = True
                break
        
        if not has_skip:
            self.issues.append({
                'type': 'missing_skip_link',
                'wcag': '2.4.1',
                'severity': 'medium',
                'location': url,
                'message': 'Page missing skip navigation link',
                'fix': 'Add "Skip to main content" link as first focusable element'
            })
    
    def _audit_tables(self, soup, url):
        """Check table accessibility (WCAG 1.3.1)."""
        for table in soup.find_all('table'):
            # Check for headers
            headers = table.find_all('th')
            if not headers:
                # Check if it's a data table (has multiple rows/cols)
                rows = table.find_all('tr')
                if len(rows) > 1:
                    cells_per_row = [len(row.find_all(['td', 'th'])) for row in rows]
                    if any(c > 1 for c in cells_per_row):
                        self.issues.append({
                            'type': 'table_missing_headers',
                            'wcag': '1.3.1',
                            'severity': 'medium',
                            'location': url,
                            'message': 'Data table missing header cells',
                            'fix': 'Use <th> elements for header cells with scope attribute'
                        })
            
            # Check for caption
            if not table.find('caption') and not table.get('aria-label'):
                self.issues.append({
                    'type': 'table_missing_caption',
                    'wcag': '1.3.1',
                    'severity': 'low',
                    'location': url,
                    'message': 'Table missing caption or aria-label',
                    'fix': 'Add <caption> or aria-label to describe table purpose'
                })
    
    def _get_selector(self, elem):
        """Generate CSS-like selector."""
        selector = elem.name
        if elem.get('id'):
            selector += f"#{elem['id']}"
        elif elem.get('class'):
            selector += '.' + '.'.join(elem['class'][:2])
        return selector
    
    def generate_report(self, url):
        """Generate audit report."""
        by_severity = defaultdict(list)
        by_wcag = defaultdict(list)
        
        for issue in self.issues:
            by_severity[issue['severity']].append(issue)
            by_wcag[issue.get('wcag', 'N/A')].append(issue)
        
        return {
            'url': url,
            'level': self.level,
            'timestamp': datetime.now().isoformat(),
            'issues': self.issues,
            'summary': {
                'total': len(self.issues),
                'high': len(by_severity['high']),
                'medium': len(by_severity['medium']),
                'low': len(by_severity['low'])
            },
            'by_wcag': {k: len(v) for k, v in by_wcag.items()},
            'stats': dict(self.stats)
        }
    
    def print_summary(self, report):
        """Print human-readable summary."""
        print("\n" + "=" * 60)
        print(f"♿ ACCESSIBILITY AUDIT - WCAG 2.1 {self.level}")
        print("=" * 60)
        print(f"URL: {report['url']}")
        print(f"Total Issues: {report['summary']['total']}")
        print(f"  🔴 High: {report['summary']['high']}")
        print(f"  🟡 Medium: {report['summary']['medium']}")
        print(f"  🟢 Low: {report['summary']['low']}")
        
        print("\nBy WCAG Criterion:")
        for wcag, count in sorted(report['by_wcag'].items()):
            print(f"  {wcag}: {count} issues")
        
        if report['summary']['high'] > 0:
            print("\n⚠️  HIGH PRIORITY FIXES:")
            for issue in report['issues']:
                if issue['severity'] == 'high':
                    print(f"  • [{issue.get('wcag', 'N/A')}] {issue['type']}")
                    print(f"    {issue['message']}")
                    if 'fix' in issue:
                        print(f"    Fix: {issue['fix']}")


def main():
    parser = argparse.ArgumentParser(description='Accessibility Auditor')
    parser.add_argument('url', help='URL to audit')
    parser.add_argument('--level', '-l', choices=['A', 'AA', 'AAA'], 
                        default='AA', help='WCAG conformance level')
    parser.add_argument('--output', '-o', help='Output JSON file')
    
    args = parser.parse_args()
    
    print(f"\n♿ Accessibility Auditor - WCAG 2.1 {args.level}")
    print("=" * 60)
    
    auditor = A11yAuditor(args.level)
    auditor.audit_url(args.url)
    report = auditor.generate_report(args.url)
    auditor.print_summary(report)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n📄 Report saved: {args.output}")
    
    return 1 if report['summary']['high'] > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
