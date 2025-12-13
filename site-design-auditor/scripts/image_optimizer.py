#!/usr/bin/env python3
"""
Image Optimizer
Batch compress, convert, and optimize images for web performance.
"""

import argparse
import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from PIL import Image
except ImportError:
    print("Installing dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "Pillow", "--break-system-packages", "-q"])
    from PIL import Image


class ImageOptimizer:
    """Batch image optimization for web."""
    
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff'}
    
    def __init__(self, quality=85, max_width=1920, generate_srcset=False):
        self.quality = quality
        self.max_width = max_width
        self.generate_srcset = generate_srcset
        self.srcset_widths = [320, 640, 768, 1024, 1280, 1920]
        self.stats = {
            'processed': 0,
            'skipped': 0,
            'errors': 0,
            'original_size': 0,
            'optimized_size': 0
        }
    
    def optimize_directory(self, input_dir, output_dir, output_format='webp'):
        """Process all images in a directory."""
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Find all images
        images = []
        for ext in self.SUPPORTED_FORMATS:
            images.extend(input_path.glob(f'**/*{ext}'))
            images.extend(input_path.glob(f'**/*{ext.upper()}'))
        
        print(f"Found {len(images)} images to process")
        
        results = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(
                    self.optimize_image, 
                    img, 
                    output_path, 
                    output_format
                ): img for img in images
            }
            
            for future in as_completed(futures):
                img_path = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                    
                    if result['status'] == 'success':
                        savings = result.get('savings_percent', 0)
                        print(f"  ✅ {img_path.name} → {result['output_name']} ({savings:.1f}% smaller)")
                    else:
                        print(f"  ⚠️ {img_path.name}: {result.get('message', 'Unknown error')}")
                        
                except Exception as e:
                    print(f"  ❌ {img_path.name}: {e}")
                    self.stats['errors'] += 1
        
        return results
    
    def optimize_image(self, input_path, output_dir, output_format='webp'):
        """Optimize a single image."""
        input_path = Path(input_path)
        original_size = input_path.stat().st_size
        self.stats['original_size'] += original_size
        
        try:
            img = Image.open(input_path)
            
            # Convert RGBA to RGB for JPEG/WebP (preserve for PNG)
            if img.mode == 'RGBA' and output_format.lower() in ['jpg', 'jpeg']:
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            elif img.mode == 'RGBA' and output_format.lower() == 'webp':
                pass  # WebP supports RGBA
            elif img.mode not in ['RGB', 'L']:
                img = img.convert('RGB')
            
            # Resize if too large
            if img.width > self.max_width:
                ratio = self.max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((self.max_width, new_height), Image.Resampling.LANCZOS)
            
            # Generate output filename
            stem = input_path.stem
            ext = f'.{output_format.lower()}'
            output_name = f"{stem}{ext}"
            output_path = output_dir / output_name
            
            # Save optimized image
            save_kwargs = {'optimize': True}
            
            if output_format.lower() in ['jpg', 'jpeg']:
                save_kwargs['quality'] = self.quality
                save_kwargs['progressive'] = True
            elif output_format.lower() == 'webp':
                save_kwargs['quality'] = self.quality
                save_kwargs['method'] = 4  # Balance speed/quality
            elif output_format.lower() == 'png':
                save_kwargs['compress_level'] = 9
            
            img.save(output_path, **save_kwargs)
            
            # Generate srcset variants if requested
            srcset_files = []
            if self.generate_srcset:
                srcset_files = self._generate_srcset(img, output_dir, stem, output_format)
            
            optimized_size = output_path.stat().st_size
            self.stats['optimized_size'] += optimized_size
            self.stats['processed'] += 1
            
            return {
                'status': 'success',
                'input': str(input_path),
                'output': str(output_path),
                'output_name': output_name,
                'original_size': original_size,
                'optimized_size': optimized_size,
                'savings_percent': ((original_size - optimized_size) / original_size) * 100,
                'dimensions': img.size,
                'srcset': srcset_files
            }
            
        except Exception as e:
            self.stats['errors'] += 1
            return {
                'status': 'error',
                'input': str(input_path),
                'message': str(e)
            }
    
    def _generate_srcset(self, img, output_dir, stem, output_format):
        """Generate responsive image variants."""
        srcset_files = []
        ext = f'.{output_format.lower()}'
        
        for width in self.srcset_widths:
            if width >= img.width:
                continue
                
            ratio = width / img.width
            new_height = int(img.height * ratio)
            
            resized = img.resize((width, new_height), Image.Resampling.LANCZOS)
            
            filename = f"{stem}-{width}w{ext}"
            filepath = output_dir / filename
            
            save_kwargs = {'optimize': True}
            if output_format.lower() in ['jpg', 'jpeg', 'webp']:
                save_kwargs['quality'] = self.quality
            
            resized.save(filepath, **save_kwargs)
            srcset_files.append({
                'width': width,
                'file': str(filepath),
                'size': filepath.stat().st_size
            })
        
        return srcset_files
    
    def generate_html_srcset(self, image_path, srcset_files, alt_text=''):
        """Generate HTML img tag with srcset."""
        if not srcset_files:
            return f'<img src="{image_path}" alt="{alt_text}" loading="lazy">'
        
        srcset_parts = [f"{f['file']} {f['width']}w" for f in srcset_files]
        srcset_parts.append(f"{image_path} {self.max_width}w")
        srcset_str = ', '.join(srcset_parts)
        
        sizes = "(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        
        return f'''<img 
    src="{image_path}" 
    srcset="{srcset_str}"
    sizes="{sizes}"
    alt="{alt_text}"
    loading="lazy"
    decoding="async"
>'''
    
    def print_stats(self):
        """Print optimization statistics."""
        print("\n" + "=" * 60)
        print("📊 OPTIMIZATION SUMMARY")
        print("=" * 60)
        print(f"Processed: {self.stats['processed']} images")
        print(f"Errors: {self.stats['errors']}")
        
        if self.stats['original_size'] > 0:
            original_mb = self.stats['original_size'] / (1024 * 1024)
            optimized_mb = self.stats['optimized_size'] / (1024 * 1024)
            savings = ((self.stats['original_size'] - self.stats['optimized_size']) 
                      / self.stats['original_size']) * 100
            
            print(f"\nOriginal size: {original_mb:.2f} MB")
            print(f"Optimized size: {optimized_mb:.2f} MB")
            print(f"Total savings: {savings:.1f}%")


def main():
    parser = argparse.ArgumentParser(description='Image Optimizer')
    parser.add_argument('input', help='Input directory or file')
    parser.add_argument('--output', '-o', default='./optimized',
                        help='Output directory')
    parser.add_argument('--format', '-f', default='webp',
                        choices=['webp', 'jpg', 'jpeg', 'png'],
                        help='Output format')
    parser.add_argument('--quality', '-q', type=int, default=85,
                        help='Compression quality (1-100)')
    parser.add_argument('--max-width', '-w', type=int, default=1920,
                        help='Maximum width (larger images resized)')
    parser.add_argument('--srcset', '-s', action='store_true',
                        help='Generate responsive srcset variants')
    
    args = parser.parse_args()
    
    print(f"\n🖼️ Image Optimizer")
    print(f"   Format: {args.format.upper()}")
    print(f"   Quality: {args.quality}")
    print(f"   Max Width: {args.max_width}px")
    if args.srcset:
        print(f"   Generating srcset variants")
    print("=" * 60)
    
    optimizer = ImageOptimizer(
        quality=args.quality,
        max_width=args.max_width,
        generate_srcset=args.srcset
    )
    
    input_path = Path(args.input)
    
    if input_path.is_file():
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        result = optimizer.optimize_image(input_path, output_dir, args.format)
        if result['status'] == 'success':
            print(f"✅ Optimized: {result['output_name']}")
            print(f"   Savings: {result['savings_percent']:.1f}%")
    else:
        optimizer.optimize_directory(args.input, args.output, args.format)
    
    optimizer.print_stats()
    
    return 0 if optimizer.stats['errors'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
