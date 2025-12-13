#!/usr/bin/env python3
"""
Visual QA & Regression Testing
Captures screenshots and compares against baselines to detect visual regressions.
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw
except ImportError:
    print("Installing dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "Pillow", "--break-system-packages", "-q"])
    from PIL import Image, ImageChops, ImageDraw

# Try playwright, fall back to selenium
BROWSER_ENGINE = None
try:
    from playwright.sync_api import sync_playwright
    BROWSER_ENGINE = 'playwright'
except ImportError:
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        BROWSER_ENGINE = 'selenium'
    except ImportError:
        pass


class VisualQA:
    """Screenshot capture and comparison tool."""
    
    VIEWPORTS = {
        'mobile': (375, 812),
        'tablet': (768, 1024),
        'desktop': (1440, 900),
        'wide': (1920, 1080)
    }
    
    def __init__(self, baseline_dir='./baselines', output_dir='./visual-qa-output'):
        self.baseline_dir = Path(baseline_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.baseline_dir.mkdir(parents=True, exist_ok=True)
        self.results = []
        
    def capture_screenshots(self, url, viewports=None):
        """Capture screenshots at different viewports."""
        viewports = viewports or list(self.VIEWPORTS.keys())
        screenshots = {}
        
        if BROWSER_ENGINE == 'playwright':
            screenshots = self._capture_playwright(url, viewports)
        elif BROWSER_ENGINE == 'selenium':
            screenshots = self._capture_selenium(url, viewports)
        else:
            print("Error: No browser engine available.")
            print("Install with: pip install playwright && playwright install")
            print("Or: pip install selenium webdriver-manager")
            return {}
            
        return screenshots
    
    def _capture_playwright(self, url, viewports):
        """Capture using Playwright."""
        screenshots = {}
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            
            for viewport_name in viewports:
                width, height = self.VIEWPORTS[viewport_name]
                
                context = browser.new_context(
                    viewport={'width': width, 'height': height},
                    device_scale_factor=2
                )
                page = context.new_page()
                
                try:
                    page.goto(url, wait_until='networkidle', timeout=30000)
                    page.wait_for_timeout(2000)  # Wait for animations
                    
                    # Full page screenshot
                    filename = self._get_filename(url, viewport_name)
                    filepath = self.output_dir / filename
                    
                    page.screenshot(path=str(filepath), full_page=True)
                    screenshots[viewport_name] = filepath
                    print(f"  📸 Captured {viewport_name}: {filename}")
                    
                except Exception as e:
                    print(f"  ❌ Failed {viewport_name}: {e}")
                finally:
                    context.close()
                    
            browser.close()
            
        return screenshots
    
    def _capture_selenium(self, url, viewports):
        """Capture using Selenium."""
        screenshots = {}
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        for viewport_name in viewports:
            width, height = self.VIEWPORTS[viewport_name]
            
            try:
                driver = webdriver.Chrome(options=options)
                driver.set_window_size(width, height)
                driver.get(url)
                
                # Wait for page load
                import time
                time.sleep(3)
                
                filename = self._get_filename(url, viewport_name)
                filepath = self.output_dir / filename
                
                driver.save_screenshot(str(filepath))
                screenshots[viewport_name] = filepath
                print(f"  📸 Captured {viewport_name}: {filename}")
                
            except Exception as e:
                print(f"  ❌ Failed {viewport_name}: {e}")
            finally:
                driver.quit()
                
        return screenshots
    
    def compare_to_baseline(self, screenshots, threshold=0.01):
        """Compare screenshots to baselines."""
        comparisons = []
        
        for viewport, screenshot_path in screenshots.items():
            baseline_path = self.baseline_dir / screenshot_path.name
            
            if not baseline_path.exists():
                comparisons.append({
                    'viewport': viewport,
                    'status': 'new',
                    'screenshot': str(screenshot_path),
                    'message': 'No baseline exists'
                })
                continue
            
            # Compare images
            diff_result = self._compare_images(
                baseline_path, 
                screenshot_path, 
                threshold
            )
            
            comparisons.append({
                'viewport': viewport,
                **diff_result
            })
            
        return comparisons
    
    def _compare_images(self, baseline_path, current_path, threshold):
        """Compare two images and generate diff."""
        baseline = Image.open(baseline_path).convert('RGB')
        current = Image.open(current_path).convert('RGB')
        
        # Handle size differences
        if baseline.size != current.size:
            return {
                'status': 'size_changed',
                'baseline_size': baseline.size,
                'current_size': current.size,
                'diff_percentage': 100,
                'message': f'Size changed from {baseline.size} to {current.size}'
            }
        
        # Calculate difference
        diff = ImageChops.difference(baseline, current)
        
        # Calculate percentage of changed pixels
        diff_data = list(diff.getdata())
        total_pixels = len(diff_data)
        changed_pixels = sum(1 for pixel in diff_data if sum(pixel) > 30)
        diff_percentage = (changed_pixels / total_pixels) * 100
        
        if diff_percentage > threshold:
            # Generate diff image
            diff_filename = f"diff-{current_path.name}"
            diff_path = self.output_dir / diff_filename
            
            # Create highlighted diff
            diff_highlight = self._create_diff_highlight(baseline, current, diff)
            diff_highlight.save(diff_path)
            
            return {
                'status': 'changed',
                'diff_percentage': round(diff_percentage, 2),
                'diff_image': str(diff_path),
                'baseline': str(baseline_path),
                'current': str(current_path),
                'message': f'{diff_percentage:.2f}% pixels changed'
            }
        
        return {
            'status': 'unchanged',
            'diff_percentage': round(diff_percentage, 2),
            'message': 'No significant changes detected'
        }
    
    def _create_diff_highlight(self, baseline, current, diff):
        """Create an image highlighting the differences."""
        # Use current as base and overlay red on changed areas
        highlight = current.copy()
        draw = ImageDraw.Draw(highlight)
        
        # Convert diff to binary mask
        diff_gray = diff.convert('L')
        threshold = 30
        
        # Create red overlay on changed pixels
        pixels = highlight.load()
        diff_pixels = diff_gray.load()
        
        width, height = highlight.size
        for y in range(height):
            for x in range(width):
                if diff_pixels[x, y] > threshold:
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (255, min(g, 100), min(b, 100))
        
        return highlight
    
    def update_baseline(self, screenshot_path):
        """Update baseline with current screenshot."""
        import shutil
        baseline_path = self.baseline_dir / Path(screenshot_path).name
        shutil.copy(screenshot_path, baseline_path)
        print(f"  ✅ Updated baseline: {baseline_path.name}")
    
    def _get_filename(self, url, viewport):
        """Generate consistent filename from URL."""
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.netloc.replace('.', '-')
        path = parsed.path.replace('/', '-').strip('-') or 'home'
        return f"{domain}_{path}_{viewport}.png"
    
    def generate_report(self, url, comparisons):
        """Generate HTML report."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = self.output_dir / f"visual-qa-report-{timestamp}.html"
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Visual QA Report - {url}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               max-width: 1400px; margin: 0 auto; padding: 20px; background: #f5f5f5; }}
        h1 {{ color: #333; }}
        .summary {{ background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
        .comparison {{ background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
        .status {{ display: inline-block; padding: 4px 12px; border-radius: 4px; font-weight: bold; }}
        .status.unchanged {{ background: #d4edda; color: #155724; }}
        .status.changed {{ background: #f8d7da; color: #721c24; }}
        .status.new {{ background: #cce5ff; color: #004085; }}
        .images {{ display: flex; gap: 20px; margin-top: 15px; }}
        .images img {{ max-width: 400px; border: 1px solid #ddd; border-radius: 4px; }}
        .image-container {{ text-align: center; }}
        .image-label {{ font-weight: bold; margin-bottom: 8px; color: #666; }}
        .diff-percentage {{ font-size: 24px; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>🔍 Visual QA Report</h1>
    <div class="summary">
        <p><strong>URL:</strong> {url}</p>
        <p><strong>Generated:</strong> {datetime.now().isoformat()}</p>
        <p><strong>Total Viewports:</strong> {len(comparisons)}</p>
    </div>
"""
        
        for comp in comparisons:
            status_class = comp['status']
            html += f"""
    <div class="comparison">
        <h3>{comp['viewport'].title()} Viewport</h3>
        <span class="status {status_class}">{comp['status'].upper()}</span>
        <p>{comp.get('message', '')}</p>
"""
            if comp['status'] == 'changed':
                html += f"""
        <p class="diff-percentage">{comp['diff_percentage']}% Changed</p>
        <div class="images">
            <div class="image-container">
                <div class="image-label">Baseline</div>
                <img src="{comp.get('baseline', '')}" alt="Baseline">
            </div>
            <div class="image-container">
                <div class="image-label">Current</div>
                <img src="{comp.get('current', '')}" alt="Current">
            </div>
            <div class="image-container">
                <div class="image-label">Diff</div>
                <img src="{comp.get('diff_image', '')}" alt="Diff">
            </div>
        </div>
"""
            html += "    </div>\n"
        
        html += """
</body>
</html>
"""
        
        with open(report_path, 'w') as f:
            f.write(html)
            
        return report_path


def main():
    parser = argparse.ArgumentParser(description='Visual QA & Regression Testing')
    parser.add_argument('url', help='URL to capture')
    parser.add_argument('--baseline', '-b', default='./baselines', 
                        help='Baseline directory')
    parser.add_argument('--output', '-o', default='./visual-qa-output',
                        help='Output directory')
    parser.add_argument('--viewports', '-v', nargs='+', 
                        choices=['mobile', 'tablet', 'desktop', 'wide'],
                        help='Viewports to capture')
    parser.add_argument('--threshold', '-t', type=float, default=0.5,
                        help='Diff threshold percentage')
    parser.add_argument('--update-baseline', '-u', action='store_true',
                        help='Update baselines with current screenshots')
    parser.add_argument('--capture-only', '-c', action='store_true',
                        help='Only capture, skip comparison')
    
    args = parser.parse_args()
    
    if not BROWSER_ENGINE:
        print("❌ No browser engine available!")
        print("Install Playwright: pip install playwright && playwright install chromium")
        print("Or Selenium: pip install selenium webdriver-manager")
        return 1
    
    print(f"\n🔍 Visual QA for {args.url}")
    print(f"   Using: {BROWSER_ENGINE}")
    print("=" * 60)
    
    qa = VisualQA(args.baseline, args.output)
    
    # Capture screenshots
    print("\n📸 Capturing screenshots...")
    screenshots = qa.capture_screenshots(args.url, args.viewports)
    
    if not screenshots:
        print("❌ No screenshots captured")
        return 1
    
    if args.capture_only:
        print(f"\n✅ Screenshots saved to {args.output}/")
        return 0
    
    if args.update_baseline:
        print("\n📝 Updating baselines...")
        for viewport, path in screenshots.items():
            qa.update_baseline(path)
        print(f"✅ Baselines updated in {args.baseline}/")
        return 0
    
    # Compare to baselines
    print("\n🔄 Comparing to baselines...")
    comparisons = qa.compare_to_baseline(screenshots, args.threshold)
    
    # Print results
    print("\n" + "=" * 60)
    print("📊 RESULTS")
    print("=" * 60)
    
    changes_found = False
    for comp in comparisons:
        status_emoji = {
            'unchanged': '✅',
            'changed': '❌',
            'new': '🆕',
            'size_changed': '⚠️'
        }.get(comp['status'], '❓')
        
        print(f"{status_emoji} {comp['viewport']}: {comp['message']}")
        
        if comp['status'] in ['changed', 'size_changed']:
            changes_found = True
    
    # Generate report
    report_path = qa.generate_report(args.url, comparisons)
    print(f"\n📄 Report saved: {report_path}")
    
    # Save JSON results
    results_path = qa.output_dir / 'results.json'
    with open(results_path, 'w') as f:
        json.dump({
            'url': args.url,
            'timestamp': datetime.now().isoformat(),
            'comparisons': comparisons
        }, f, indent=2, default=str)
    
    return 1 if changes_found else 0


if __name__ == '__main__':
    sys.exit(main())
