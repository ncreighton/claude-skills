#!/usr/bin/env python3
"""
Font Subsetter
Reduce web font file sizes by creating subsets with only needed characters.
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from fontTools.ttLib import TTFont
    from fontTools.subset import Subsetter, Options
except ImportError:
    print("Installing dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "fonttools", "brotli", "--break-system-packages", "-q"])
    from fontTools.ttLib import TTFont
    from fontTools.subset import Subsetter, Options


class FontSubsetter:
    """Font subsetting for web optimization."""
    
    # Common character sets
    CHARSETS = {
        'latin': (
            'U+0000-00FF',  # Basic Latin + Latin-1 Supplement
        ),
        'latin-ext': (
            'U+0000-00FF',  # Basic Latin + Latin-1 Supplement
            'U+0100-017F',  # Latin Extended-A
            'U+0180-024F',  # Latin Extended-B
            'U+1E00-1EFF',  # Latin Extended Additional
        ),
        'latin-full': (
            'U+0000-00FF',
            'U+0100-017F',
            'U+0180-024F',
            'U+0250-02AF',  # IPA Extensions
            'U+1D00-1D7F',  # Phonetic Extensions
            'U+1E00-1EFF',
            'U+2000-206F',  # General Punctuation
            'U+2070-209F',  # Superscripts and Subscripts
            'U+20A0-20CF',  # Currency Symbols
            'U+2100-214F',  # Letterlike Symbols
        ),
        'numbers': (
            'U+0030-0039',  # 0-9
            'U+002C',       # ,
            'U+002E',       # .
            'U+0024',       # $
            'U+00A3',       # £
            'U+20AC',       # €
            'U+00A5',       # ¥
        ),
        'icons': (
            'U+E000-F8FF',  # Private Use Area (icons)
        ),
        'essential': (
            # Just ASCII printable
            'U+0020-007E',
        ),
    }
    
    # Common glyphs that should always be included
    COMMON_TEXT = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        " \n\t"
        "–—''""…•·×÷±≠≤≥"
        "áàâäãåæçéèêëíìîïñóòôöõøœúùûüýÿ"
        "ÁÀÂÄÃÅÆÇÉÈÊËÍÌÎÏÑÓÒÔÖÕØŒÚÙÛÜÝŸ"
    )
    
    def __init__(self, output_dir='./font-subsets'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.stats = {
            'processed': 0,
            'errors': 0,
            'original_size': 0,
            'subset_size': 0
        }
    
    def subset_font(self, font_path, charset='latin', custom_text=None, 
                    output_formats=None):
        """Create a subset of a font file."""
        font_path = Path(font_path)
        
        if not font_path.exists():
            return {'status': 'error', 'message': f'Font not found: {font_path}'}
        
        original_size = font_path.stat().st_size
        self.stats['original_size'] += original_size
        
        try:
            # Load font
            font = TTFont(font_path)
            
            # Build character set
            unicodes = set()
            
            # Add charset ranges
            if charset in self.CHARSETS:
                for range_str in self.CHARSETS[charset]:
                    unicodes.update(self._parse_unicode_range(range_str))
            
            # Add common text characters
            for char in self.COMMON_TEXT:
                unicodes.add(ord(char))
            
            # Add custom text characters
            if custom_text:
                for char in custom_text:
                    unicodes.add(ord(char))
            
            # Create subsetter
            options = Options()
            options.flavor = 'woff2'  # Output as WOFF2
            options.desubroutinize = True
            options.layout_features = ['*']  # Keep all OpenType features
            
            subsetter = Subsetter(options=options)
            subsetter.populate(unicodes=unicodes)
            subsetter.subset(font)
            
            # Determine output formats
            output_formats = output_formats or ['woff2']
            results = []
            
            for fmt in output_formats:
                output_name = f"{font_path.stem}.subset.{fmt}"
                output_path = self.output_dir / output_name
                
                if fmt == 'woff2':
                    font.flavor = 'woff2'
                elif fmt == 'woff':
                    font.flavor = 'woff'
                else:
                    font.flavor = None
                
                font.save(output_path)
                
                subset_size = output_path.stat().st_size
                self.stats['subset_size'] += subset_size
                
                results.append({
                    'format': fmt,
                    'path': str(output_path),
                    'size': subset_size
                })
            
            self.stats['processed'] += 1
            
            # Calculate savings
            best_size = min(r['size'] for r in results)
            savings = ((original_size - best_size) / original_size) * 100
            
            return {
                'status': 'success',
                'input': str(font_path),
                'original_size': original_size,
                'charset': charset,
                'glyph_count': len(unicodes),
                'outputs': results,
                'savings_percent': savings
            }
            
        except Exception as e:
            self.stats['errors'] += 1
            return {
                'status': 'error',
                'input': str(font_path),
                'message': str(e)
            }
    
    def _parse_unicode_range(self, range_str):
        """Parse a Unicode range like 'U+0000-00FF' into a set of codepoints."""
        unicodes = set()
        
        # Handle single codepoint
        if '-' not in range_str or range_str.count('-') == 0:
            codepoint = int(range_str.replace('U+', ''), 16)
            unicodes.add(codepoint)
            return unicodes
        
        # Handle range
        parts = range_str.replace('U+', '').split('-')
        if len(parts) == 2:
            start = int(parts[0], 16)
            end = int(parts[1], 16)
            for cp in range(start, end + 1):
                unicodes.add(cp)
        
        return unicodes
    
    def analyze_usage(self, html_dir):
        """Analyze HTML files to find actually used characters."""
        html_path = Path(html_dir)
        used_chars = set()
        
        for html_file in html_path.glob('**/*.html'):
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for char in content:
                        if ord(char) > 31:  # Skip control characters
                            used_chars.add(char)
            except Exception as e:
                print(f"Warning: Could not read {html_file}: {e}")
        
        return ''.join(sorted(used_chars))
    
    def subset_directory(self, font_dir, charset='latin', output_formats=None):
        """Process all fonts in a directory."""
        font_path = Path(font_dir)
        font_extensions = {'.ttf', '.otf', '.woff', '.woff2'}
        
        fonts = [f for f in font_path.iterdir() 
                 if f.suffix.lower() in font_extensions]
        
        results = []
        for font_file in fonts:
            print(f"  Processing: {font_file.name}")
            result = self.subset_font(font_file, charset, 
                                     output_formats=output_formats)
            results.append(result)
            
            if result['status'] == 'success':
                print(f"    ✅ {result['savings_percent']:.1f}% smaller")
            else:
                print(f"    ❌ {result.get('message', 'Unknown error')}")
        
        return results
    
    def generate_css(self, font_family, results):
        """Generate @font-face CSS declarations."""
        css_lines = [
            f"/* {font_family} - Subset Font CSS */",
            f"/* Generated by Font Subsetter */",
            ""
        ]
        
        for result in results:
            if result['status'] != 'success':
                continue
            
            for output in result['outputs']:
                if output['format'] != 'woff2':
                    continue
                
                # Extract weight and style from filename
                filename = Path(output['path']).stem
                weight = '400'
                style = 'normal'
                
                if 'bold' in filename.lower():
                    weight = '700'
                elif 'light' in filename.lower():
                    weight = '300'
                elif 'medium' in filename.lower():
                    weight = '500'
                elif 'semibold' in filename.lower():
                    weight = '600'
                elif 'black' in filename.lower():
                    weight = '900'
                
                if 'italic' in filename.lower():
                    style = 'italic'
                
                css_lines.extend([
                    "@font-face {",
                    f"  font-family: '{font_family}';",
                    f"  font-style: {style};",
                    f"  font-weight: {weight};",
                    "  font-display: swap;",
                    f"  src: url('{Path(output['path']).name}') format('woff2');",
                    "}",
                    ""
                ])
        
        return '\n'.join(css_lines)
    
    def print_stats(self):
        """Print subsetting statistics."""
        print("\n" + "=" * 60)
        print("📊 FONT SUBSETTING SUMMARY")
        print("=" * 60)
        print(f"Processed: {self.stats['processed']} fonts")
        print(f"Errors: {self.stats['errors']}")
        
        if self.stats['original_size'] > 0:
            original_kb = self.stats['original_size'] / 1024
            subset_kb = self.stats['subset_size'] / 1024
            savings = ((self.stats['original_size'] - self.stats['subset_size']) 
                      / self.stats['original_size']) * 100
            
            print(f"\nOriginal size: {original_kb:.1f} KB")
            print(f"Subset size: {subset_kb:.1f} KB")
            print(f"Total savings: {savings:.1f}%")


def main():
    parser = argparse.ArgumentParser(description='Font Subsetter')
    parser.add_argument('input', help='Input font file or directory')
    parser.add_argument('--output', '-o', default='./font-subsets',
                        help='Output directory')
    parser.add_argument('--charset', '-c', default='latin',
                        choices=['latin', 'latin-ext', 'latin-full', 
                                'numbers', 'icons', 'essential'],
                        help='Character set to include')
    parser.add_argument('--custom-text', '-t',
                        help='Additional text to include characters from')
    parser.add_argument('--analyze', '-a',
                        help='Analyze HTML directory for used characters')
    parser.add_argument('--formats', '-f', nargs='+', default=['woff2'],
                        choices=['woff2', 'woff', 'ttf'],
                        help='Output formats')
    parser.add_argument('--css', action='store_true',
                        help='Generate @font-face CSS')
    parser.add_argument('--font-family',
                        help='Font family name for CSS generation')
    
    args = parser.parse_args()
    
    print(f"\n🔤 Font Subsetter")
    print(f"   Charset: {args.charset}")
    print(f"   Formats: {', '.join(args.formats)}")
    print("=" * 60)
    
    subsetter = FontSubsetter(args.output)
    
    # Analyze usage if requested
    custom_text = args.custom_text or ''
    if args.analyze:
        print(f"\n📄 Analyzing HTML in {args.analyze}...")
        custom_text += subsetter.analyze_usage(args.analyze)
        print(f"   Found {len(set(custom_text))} unique characters")
    
    input_path = Path(args.input)
    
    if input_path.is_file():
        print(f"\n📦 Processing {input_path.name}...")
        result = subsetter.subset_font(
            input_path, 
            args.charset, 
            custom_text,
            args.formats
        )
        results = [result]
        
        if result['status'] == 'success':
            print(f"✅ Created subset with {result['glyph_count']} glyphs")
            print(f"   Savings: {result['savings_percent']:.1f}%")
            for output in result['outputs']:
                print(f"   → {output['path']}")
    else:
        print(f"\n📦 Processing fonts in {input_path}...")
        results = subsetter.subset_directory(
            input_path, 
            args.charset, 
            args.formats
        )
    
    # Generate CSS if requested
    if args.css:
        font_family = args.font_family or input_path.stem
        css = subsetter.generate_css(font_family, results)
        css_path = subsetter.output_dir / 'fonts.css'
        with open(css_path, 'w') as f:
            f.write(css)
        print(f"\n📝 Generated CSS: {css_path}")
    
    subsetter.print_stats()
    
    return 0 if subsetter.stats['errors'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
