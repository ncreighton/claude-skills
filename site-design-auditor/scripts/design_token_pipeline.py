#!/usr/bin/env python3
"""
Design Token Pipeline
Extracts design tokens from Figma and generates CSS variables for WordPress sites.
Figma → JSON Tokens → CSS Variables → WordPress Theme Files
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    print("Installing dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "requests", "--break-system-packages", "-q"])
    import requests


class FigmaTokenExtractor:
    """Extract design tokens from Figma file."""
    
    def __init__(self, file_key, access_token):
        self.file_key = file_key
        self.access_token = access_token
        self.base_url = "https://api.figma.com/v1"
        self.headers = {"X-Figma-Token": access_token}
        
    def extract_variables(self):
        """Get all variables from Figma file."""
        url = f"{self.base_url}/files/{self.file_key}/variables/local"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print(f"Warning: Could not fetch Figma variables: {e}")
            print("Using fallback method via styles...")
            return self._extract_from_styles()
            
        return self._process_variables(data)
    
    def _extract_from_styles(self):
        """Fallback: Extract from Figma styles."""
        url = f"{self.base_url}/files/{self.file_key}/styles"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            styles = response.json().get('meta', {}).get('styles', {})
        except Exception as e:
            print(f"Error fetching styles: {e}")
            return {}
            
        tokens = {
            'colors': {},
            'typography': {},
            'effects': {}
        }
        
        for style_id, style_info in styles.items():
            style_type = style_info.get('style_type', '')
            name = style_info.get('name', '').replace('/', '-').replace(' ', '-').lower()
            
            if style_type == 'FILL':
                tokens['colors'][name] = style_id
            elif style_type == 'TEXT':
                tokens['typography'][name] = style_id
            elif style_type == 'EFFECT':
                tokens['effects'][name] = style_id
                
        return tokens
    
    def _process_variables(self, data):
        """Process Figma variables API response."""
        tokens = {
            'colors': {},
            'typography': {},
            'spacing': {},
            'sizing': {},
            'radius': {},
            'effects': {}
        }
        
        variables = data.get('meta', {}).get('variables', {})
        collections = data.get('meta', {}).get('variableCollections', {})
        
        for var_id, var_data in variables.items():
            name = var_data.get('name', '').replace('/', '-').replace(' ', '-').lower()
            resolved_type = var_data.get('resolvedType', '')
            values = var_data.get('valuesByMode', {})
            
            # Get first mode value
            value = list(values.values())[0] if values else None
            
            if resolved_type == 'COLOR' and value:
                r = int(value.get('r', 0) * 255)
                g = int(value.get('g', 0) * 255)
                b = int(value.get('b', 0) * 255)
                a = value.get('a', 1)
                
                if a < 1:
                    tokens['colors'][name] = f"rgba({r}, {g}, {b}, {a})"
                else:
                    tokens['colors'][name] = f"#{r:02x}{g:02x}{b:02x}"
                    
            elif resolved_type == 'FLOAT' and value:
                # Categorize numeric tokens by name pattern
                if any(x in name for x in ['space', 'gap', 'margin', 'padding']):
                    tokens['spacing'][name] = f"{value}px"
                elif any(x in name for x in ['size', 'width', 'height']):
                    tokens['sizing'][name] = f"{value}px"
                elif 'radius' in name:
                    tokens['radius'][name] = f"{value}px"
                    
        return tokens


class CSSGenerator:
    """Generate CSS from design tokens."""
    
    def __init__(self, tokens, config=None):
        self.tokens = tokens
        self.config = config or {}
        
    def generate_css_variables(self):
        """Generate CSS custom properties."""
        lines = [
            "/* Design Tokens - Auto-generated */",
            f"/* Generated: {datetime.now().isoformat()} */",
            "",
            ":root {"
        ]
        
        # Colors
        if self.tokens.get('colors'):
            lines.append("  /* Colors */")
            for name, value in self.tokens['colors'].items():
                css_name = self._to_css_var_name(name, 'color')
                lines.append(f"  --{css_name}: {value};")
            lines.append("")
        
        # Typography
        if self.tokens.get('typography'):
            lines.append("  /* Typography */")
            typo = self.tokens['typography']
            
            if 'fontFamily' in typo:
                for name, value in typo['fontFamily'].items():
                    lines.append(f"  --font-family-{name}: {value};")
                    
            if 'fontSize' in typo:
                for name, value in typo['fontSize'].items():
                    lines.append(f"  --font-size-{name}: {value};")
                    
            if 'fontWeight' in typo:
                for name, value in typo['fontWeight'].items():
                    lines.append(f"  --font-weight-{name}: {value};")
                    
            if 'lineHeight' in typo:
                for name, value in typo['lineHeight'].items():
                    lines.append(f"  --line-height-{name}: {value};")
            lines.append("")
        
        # Spacing
        if self.tokens.get('spacing'):
            lines.append("  /* Spacing */")
            for name, value in self.tokens['spacing'].items():
                css_name = self._to_css_var_name(name, 'space')
                lines.append(f"  --{css_name}: {value};")
            lines.append("")
        
        # Sizing
        if self.tokens.get('sizing'):
            lines.append("  /* Sizing */")
            for name, value in self.tokens['sizing'].items():
                css_name = self._to_css_var_name(name, 'size')
                lines.append(f"  --{css_name}: {value};")
            lines.append("")
        
        # Border Radius
        if self.tokens.get('radius'):
            lines.append("  /* Border Radius */")
            for name, value in self.tokens['radius'].items():
                css_name = self._to_css_var_name(name, 'radius')
                lines.append(f"  --{css_name}: {value};")
            lines.append("")
        
        # Effects/Shadows
        if self.tokens.get('effects'):
            lines.append("  /* Effects */")
            for name, value in self.tokens['effects'].items():
                css_name = self._to_css_var_name(name, 'shadow')
                lines.append(f"  --{css_name}: {value};")
            lines.append("")
        
        lines.append("}")
        
        return "\n".join(lines)
    
    def generate_tailwind_config(self):
        """Generate Tailwind CSS config extension."""
        config = {
            "theme": {
                "extend": {}
            }
        }
        
        if self.tokens.get('colors'):
            config['theme']['extend']['colors'] = {
                self._to_js_name(k): f"var(--color-{self._to_css_var_name(k, '')})"
                for k, v in self.tokens['colors'].items()
            }
            
        if self.tokens.get('spacing'):
            config['theme']['extend']['spacing'] = {
                self._to_js_name(k): f"var(--space-{self._to_css_var_name(k, '')})"
                for k, v in self.tokens['spacing'].items()
            }
            
        return json.dumps(config, indent=2)
    
    def generate_scss_variables(self):
        """Generate SCSS variables."""
        lines = [
            "// Design Tokens - Auto-generated",
            f"// Generated: {datetime.now().isoformat()}",
            ""
        ]
        
        if self.tokens.get('colors'):
            lines.append("// Colors")
            for name, value in self.tokens['colors'].items():
                scss_name = self._to_scss_var_name(name, 'color')
                lines.append(f"${scss_name}: {value};")
            lines.append("")
            
        if self.tokens.get('spacing'):
            lines.append("// Spacing")
            for name, value in self.tokens['spacing'].items():
                scss_name = self._to_scss_var_name(name, 'space')
                lines.append(f"${scss_name}: {value};")
            lines.append("")
            
        return "\n".join(lines)
    
    def _to_css_var_name(self, name, prefix=''):
        """Convert token name to CSS variable name."""
        # Remove any existing prefix
        clean = re.sub(r'^(color|font|space|size|radius)[-_]?', '', name.lower())
        clean = re.sub(r'[^a-z0-9]+', '-', clean).strip('-')
        
        if prefix:
            return f"{prefix}-{clean}"
        return clean
    
    def _to_scss_var_name(self, name, prefix=''):
        """Convert token name to SCSS variable name."""
        clean = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
        if prefix:
            return f"{prefix}-{clean}"
        return clean
    
    def _to_js_name(self, name):
        """Convert to JavaScript-friendly name."""
        return re.sub(r'[^a-zA-Z0-9]+', '', name.title())


class WordPressPusher:
    """Push CSS to WordPress sites."""
    
    def __init__(self, site_url, username, app_password):
        self.site_url = site_url.rstrip('/')
        self.auth = (username, app_password)
        
    def push_css(self, css_content, filename='design-tokens.css'):
        """Push CSS file to WordPress media library or theme."""
        # Option 1: Use REST API to update customizer CSS
        url = f"{self.site_url}/wp-json/wp/v2/settings"
        
        # This requires the site to have custom CSS support
        # Alternative: Use theme file editing API
        
        print(f"Note: Direct CSS push requires theme-specific integration")
        print(f"Save CSS to: {filename}")
        
        return True


def load_tokens_from_file(filepath):
    """Load tokens from local JSON file."""
    with open(filepath) as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description='Design Token Pipeline')
    parser.add_argument('--figma-file', '-f', help='Figma file key')
    parser.add_argument('--figma-token', '-t', help='Figma access token')
    parser.add_argument('--input', '-i', help='Input tokens JSON file (alternative to Figma)')
    parser.add_argument('--output', '-o', default='./tokens', help='Output directory')
    parser.add_argument('--format', choices=['css', 'scss', 'tailwind', 'all'], 
                        default='all', help='Output format')
    parser.add_argument('--site-name', '-s', help='Site name for file prefix')
    
    args = parser.parse_args()
    
    # Get tokens from Figma or file
    if args.input:
        print(f"📂 Loading tokens from {args.input}")
        tokens = load_tokens_from_file(args.input)
    elif args.figma_file and args.figma_token:
        print(f"🎨 Extracting tokens from Figma file {args.figma_file}")
        extractor = FigmaTokenExtractor(args.figma_file, args.figma_token)
        tokens = extractor.extract_variables()
    else:
        print("Error: Provide either --input or --figma-file with --figma-token")
        return 1
    
    if not tokens:
        print("Error: No tokens extracted")
        return 1
    
    # Create output directory
    os.makedirs(args.output, exist_ok=True)
    
    # Generate CSS
    generator = CSSGenerator(tokens)
    prefix = f"{args.site_name}-" if args.site_name else ""
    
    if args.format in ['css', 'all']:
        css_content = generator.generate_css_variables()
        css_file = os.path.join(args.output, f"{prefix}design-tokens.css")
        with open(css_file, 'w') as f:
            f.write(css_content)
        print(f"✅ Generated: {css_file}")
    
    if args.format in ['scss', 'all']:
        scss_content = generator.generate_scss_variables()
        scss_file = os.path.join(args.output, f"{prefix}design-tokens.scss")
        with open(scss_file, 'w') as f:
            f.write(scss_content)
        print(f"✅ Generated: {scss_file}")
    
    if args.format in ['tailwind', 'all']:
        tw_content = generator.generate_tailwind_config()
        tw_file = os.path.join(args.output, f"{prefix}tailwind-tokens.json")
        with open(tw_file, 'w') as f:
            f.write(tw_content)
        print(f"✅ Generated: {tw_file}")
    
    # Save raw tokens
    tokens_file = os.path.join(args.output, f"{prefix}tokens.json")
    with open(tokens_file, 'w') as f:
        json.dump(tokens, f, indent=2)
    print(f"✅ Generated: {tokens_file}")
    
    print(f"\n🎉 Design tokens generated in {args.output}/")
    return 0


if __name__ == '__main__':
    sys.exit(main())
