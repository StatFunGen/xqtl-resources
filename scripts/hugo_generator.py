#!/usr/bin/env python3
"""
Hugo site generator for xQTL Resources
Handles content transformation and organization for Hugo
Modified to keep original structure only, no alphabetical organization
"""

import os
import re
import glob
import sys
import argparse
import subprocess
import shutil
import urllib.request
import zipfile
from pathlib import Path
from collections import OrderedDict, defaultdict

# Configuration defaults
DEFAULT_DATA_DIR = 'content/xqtl-data'
DEFAULT_CONTENT_DIR = 'content'
DEFAULT_WEBSITE_DIR = 'website'
DEFAULT_BASE_URL = 'https://statfungen.github.io/xqtl-resources/'
DEFAULT_GITHUB_URL = 'https://github.com/StatFunGen/xqtl-resources/tree/main/'
HUGO_BOOK_THEME_URL = 'https://github.com/alex-shpak/hugo-book/archive/refs/heads/master.zip'

class HugoSiteGenerator:
    """Hugo site generator with content transformation"""
    
    def __init__(self, content_dir=DEFAULT_CONTENT_DIR, website_dir=DEFAULT_WEBSITE_DIR, 
                 base_url=DEFAULT_BASE_URL, verbose=True):
        self.source_content_dir = content_dir
        self.data_dir = os.path.join(content_dir, 'xqtl-data')
        self.website_dir = website_dir
        self.website_content_dir = os.path.join(website_dir, 'content')
        self.themes_dir = os.path.join(website_dir, 'themes')
        self.base_url = base_url
        self.verbose = verbose
        self.problematic_files = []
        
    def log(self, message, level='info'):
        """Simple logging function"""
        if self.verbose:
            prefix = {
                'info': '→',
                'success': '✓',
                'warning': '⚠',
                'error': '✗'
            }.get(level, '→')
            print(f"{prefix} {message}")
    
    def setup_directories(self):
        """Create necessary directory structure"""
        dirs = [
            self.website_dir,
            self.website_content_dir,
            self.themes_dir,
            os.path.join(self.website_content_dir, 'menu')
        ]
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
        self.log(f"Created directory structure in {self.website_dir}", 'success')
    
    def download_theme(self, force=False):
        """Download Hugo Book theme"""
        theme_path = os.path.join(self.themes_dir, 'hugo-book')
        
        if os.path.exists(theme_path) and not force:
            self.log("Theme already exists, skipping download", 'info')
            return True
        
        self.log("Downloading Hugo Book theme...", 'info')
        
        try:
            # Download theme
            zip_path = os.path.join(self.themes_dir, 'hugo-book.zip')
            urllib.request.urlretrieve(HUGO_BOOK_THEME_URL, zip_path)
            
            # Extract theme
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.themes_dir)
            
            # Find extracted directory and rename to hugo-book
            for item in os.listdir(self.themes_dir):
                if item.startswith('hugo-book') and item != 'hugo-book':
                    old_path = os.path.join(self.themes_dir, item)
                    if os.path.exists(theme_path):
                        shutil.rmtree(theme_path)
                    os.rename(old_path, theme_path)
                    break
            
            # Clean up zip
            if os.path.exists(zip_path):
                os.remove(zip_path)
            
            self.log("Theme downloaded successfully", 'success')
            return True
            
        except Exception as e:
            self.log(f"Failed to download theme: {e}", 'error')
            self.log("You can manually clone: git clone https://github.com/alex-shpak/hugo-book.git " + theme_path, 'info')
            return False

    def create_hugo_config(self):
        """Copy Hugo configuration file from source repository"""
        source_config = 'hugo.toml'
        dest_config = os.path.join(self.website_dir, 'hugo.toml')
    
        # Check if source hugo.toml exists
        if not os.path.exists(source_config):
            self.log(f"Error: hugo.toml not found in repository root", 'error')
            self.log(f"Expected location: {os.path.abspath(source_config)}", 'error')
            sys.exit(1)
    
        # Copy the existing hugo.toml to website directory
        shutil.copy2(source_config, dest_config)
        self.log(f"Copied hugo.toml to {dest_config}", 'success')
    
    def sanitize_markdown_content(self, content):
        """Sanitize markdown content to avoid Hugo parsing errors"""
        if not content:
            return content
        
        # Fix unquoted attributes in links/images
        content = re.sub(r'\{([^}]+)=([^}"]+)\}', r'{$1="$2"}', content)
        
        # Escape {{ and }} in code blocks
        def escape_code_blocks(match):
            code = match.group(1)
            code = code.replace('{{', '&#123;&#123;')
            code = code.replace('}}', '&#125;&#125;')
            return f'```{code}```'
        
        content = re.sub(r'```(.*?)```', escape_code_blocks, content, flags=re.DOTALL)
        
        # Escape inline code
        def escape_inline_code(match):
            code = match.group(1)
            code = code.replace('{{', '&#123;&#123;')
            code = code.replace('}}', '&#125;&#125;')
            return f'`{code}`'
        
        content = re.sub(r'`([^`]+)`', escape_inline_code, content)
        
        # Remove Pandoc-style attributes
        content = re.sub(r'\{\.[\w\s-]+\}', '', content)
        
        return content
    
    def add_frontmatter(self, content, title, weight=10, depth_level=1):
        """Add Hugo frontmatter to markdown content"""
        # Escape quotes in title
        safe_title = title.replace('"', '\\"')
        
        # For depth limiting: hide items deeper than level 2
        # Level 1: root content
        # Level 2: xqtl-data/gwas, xqtl-data/omics, etc.
        # Level 3+: individual files within those directories
        
        # Don't hide index files or first two levels
        book_hidden = ""
        if depth_level > 2 and not content.startswith("# "):
            book_hidden = "bookHidden: true\n"
        
        # Collapse sections by default for cleaner navigation
        book_collapse = ""
        if depth_level == 2:
            book_collapse = "bookCollapseSection: true\n"
        
        frontmatter = f"""---
title: "{safe_title}"
weight: {weight}
bookToc: true
{book_collapse}{book_hidden}---

"""
        return frontmatter + content
    
    def copy_content_files(self):
        """Copy content/*.md files to website/content/ with proper transformation"""
        self.log("Copying and transforming content files...", 'info')
        
        # First, handle files in the root content directory
        root_files = glob.glob(os.path.join(self.source_content_dir, '*.md'))
        for source_file in root_files:
            filename = os.path.basename(source_file)
            
            # Transform README.md to _index.md
            if filename == 'README.md':
                dest_filename = '_index.md'
            else:
                dest_filename = filename
            
            dest_file = os.path.join(self.website_content_dir, dest_filename)
            
            # Read and process content
            with open(source_file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            
            # Extract title from first heading or filename
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
            else:
                title = Path(source_file).stem.replace('-', ' ').replace('_', ' ').title()
            
            # Sanitize and add frontmatter
            content = self.sanitize_markdown_content(content)
            content = self.add_frontmatter(content, title, weight=1, depth_level=1)
            
            # Write to destination
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.log(f"  Copied: {filename} → {dest_filename}", 'success')
        
        # Now handle subdirectories
        for subdir in os.listdir(self.source_content_dir):
            source_subdir = os.path.join(self.source_content_dir, subdir)
            if not os.path.isdir(source_subdir):
                continue
            
            dest_subdir = os.path.join(self.website_content_dir, subdir)
            os.makedirs(dest_subdir, exist_ok=True)
            
            # Copy all .md files in subdirectory
            md_files = glob.glob(os.path.join(source_subdir, '**/*.md'), recursive=True)
            for source_file in md_files:
                # Calculate relative path and depth
                rel_path = os.path.relpath(source_file, source_subdir)
                path_parts = rel_path.split(os.sep)
                depth_level = len(path_parts) + 1  # +1 for the subdir itself
                
                filename = os.path.basename(source_file)
                
                # Transform README.md to _index.md
                if filename == 'README.md':
                    dest_filename = '_index.md'
                    # Get the directory path for the index
                    dest_dir = os.path.dirname(os.path.join(dest_subdir, rel_path))
                    dest_file = os.path.join(dest_dir, dest_filename)
                else:
                    dest_file = os.path.join(dest_subdir, rel_path)
                
                # Ensure destination directory exists
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                
                # Read and process content
                with open(source_file, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                
                # Extract title
                title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1)
                else:
                    title = Path(source_file).stem.replace('-', ' ').replace('_', ' ').title()
                
                # Sanitize and add frontmatter
                content = self.sanitize_markdown_content(content)
                
                # Determine weight based on position
                weight = 10
                if filename == 'README.md' or dest_filename == '_index.md':
                    weight = 1
                
                content = self.add_frontmatter(content, title, weight=weight, depth_level=depth_level)
                
                # Write to destination
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.log(f"  Copied: {subdir}/{rel_path} → {os.path.relpath(dest_file, self.website_content_dir)}", 'success')
    
    def collect_xqtl_metadata(self):
        """Collect metadata from xqtl-data files for README generation"""
        if not os.path.exists(self.data_dir):
            self.log(f"xqtl-data directory not found at {self.data_dir}", 'warning')
            return None
        
        # Find all markdown files in xqtl-data
        patterns = [
            f'{self.data_dir}/gwas/*.md',
            f'{self.data_dir}/omics/*.md',
            f'{self.data_dir}/qtl/*.md',
            f'{self.data_dir}/study_info/*.md',
            f'{self.data_dir}/reference_data/*.md'
        ]
        
        all_files = []
        for pattern in patterns:
            files = glob.glob(pattern)
            all_files.extend(files)
        
        # Filter out README and index files
        all_files = [f for f in all_files if not f.endswith('README.md')]
        
        if not all_files:
            self.log(f"No markdown files found in {self.data_dir}", 'warning')
            return None
        
        self.log(f"Found {len(all_files)} markdown files in xqtl-data", 'info')
        
        # Extract metadata from files
        all_items = []
        for filepath in all_files:
            metadata = self.get_metadata_from_file(filepath)
            if metadata and metadata['title']:
                all_items.append(metadata)
        
        if all_items:
            self.log(f"Collected metadata from {len(all_items)} xqtl-data items", 'success')
        
        return all_items
    
    def get_metadata_from_file(self, filepath):
        """Extract metadata from a markdown file"""
        metadata = {
            'title': '',
            'description': '',
            'lead_analysts': '',
            'category': os.path.basename(os.path.dirname(filepath)),
            'filepath': filepath
        }
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Find the first heading
            for line in lines:
                line = line.strip()
                if line.startswith('# ') and not line.startswith('## '):
                    metadata['title'] = line[2:].strip()
                    break
            
            if not metadata['title']:
                # Use filename as title if no heading found
                metadata['title'] = Path(filepath).stem.replace('-', ' ').replace('_', ' ').title()
            
            # Get description
            in_description = False
            for i, line in enumerate(lines):
                if metadata['title'] and line.strip().startswith('# ' + metadata['title']):
                    in_description = True
                    continue
                if in_description and line.strip() and not line.startswith('#'):
                    metadata['description'] = line.strip().rstrip('.')
                    if metadata['description']:
                        metadata['description'] += '.'
                    break
            
            # Extract lead analysts
            full_content = '\n'.join(lines)
            lead_match = re.search(r'(?:Lead analysts?|Contact):\s*(.+?)(?:\n|$)', 
                                  full_content, re.IGNORECASE | re.MULTILINE)
            if lead_match:
                lead = lead_match.group(1).strip()
                lead = re.sub(r'\([^)]+\)', '', lead)  # Remove parentheses
                lead = re.sub(r'<[^>]+>', '', lead)     # Remove emails
                lead = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', lead)  # Remove markdown links
                lead = re.sub(r'\s+', ' ', lead)        # Normalize whitespace
                metadata['lead_analysts'] = lead.strip('. ')
            
            return metadata
            
        except Exception as e:
            self.log(f"Error reading {filepath}: {e}", 'error')
            self.problematic_files.append(filepath)
            return None
    
    def create_menu(self):
        """Create navigation menu for original structure"""
        menu_dir = os.path.join(self.website_content_dir, 'menu')
        os.makedirs(menu_dir, exist_ok=True)
        
        menu_content = """---
headless: true
---

- [**Home**]({{< relref "/" >}})
- [**xQTL Data Repository**]({{< relref "/xqtl-data" >}})
  - [Study Information]({{< relref "/xqtl-data/study_info" >}})
  - [GWAS Summary Statistics]({{< relref "/xqtl-data/gwas" >}})
  - [Omics Data]({{< relref "/xqtl-data/omics" >}})
  - [QTL Results]({{< relref "/xqtl-data/qtl" >}})
  - [Reference Data]({{< relref "/xqtl-data/reference_data" >}})
"""
        
        menu_path = os.path.join(menu_dir, 'index.md')
        with open(menu_path, 'w', encoding='utf-8') as f:
            f.write(menu_content)
        
        self.log("Created navigation menu", 'success')
    
    def generate_readme(self, all_items):
        """Generate README.md for the repository"""
        if not all_items:
            return
        
        readme_path = 'README.md'
        
        content = f"""# FunGen-xQTL Resources

This repository contains {len(all_items)} datasets developed by the ADSP Functional Genomics Consortium.

Published at: {self.base_url}

## Dataset Categories

"""
        
        # Group by category
        by_category = defaultdict(list)
        for item in all_items:
            by_category[item['category']].append(item)
        
        # Write each category
        category_order = ['study_info', 'gwas', 'omics', 'qtl', 'reference_data']
        category_names = {
            'study_info': 'Study Information',
            'gwas': 'GWAS Summary Statistics',
            'omics': 'Omics Data',
            'qtl': 'QTL Results',
            'reference_data': 'Reference Data'
        }
        
        for cat in category_order:
            if cat in by_category:
                cat_title = category_names.get(cat, cat.replace('_', ' ').title())
                items = sorted(by_category[cat], key=lambda x: x['title'].lower())
                
                content += f"### {cat_title} ({len(items)} datasets)\n\n"
                
                for item in items:
                    # Create GitHub link
                    rel_path = os.path.relpath(item['filepath'], '.')
                    github_link = f"{DEFAULT_GITHUB_URL}{rel_path}"
                    
                    entry = f"- [{item['title']}]({github_link})"
                    if item['description']:
                        entry += f": {item['description']}"
                    if item['lead_analysts']:
                        entry += f" (Lead: {item['lead_analysts']})"
                    content += entry + "\n"
                
                content += "\n"
        
        content += """

## Repository Structure

```
.
├── content/                  # Source markdown files
│   ├── xqtl-data/           # xQTL datasets
│   │   ├── study_info/      # Study descriptions
│   │   ├── gwas/            # GWAS summary statistics
│   │   ├── omics/           # Omics data
│   │   ├── qtl/             # QTL results
│   │   └── reference_data/  # Reference panels
│   └── *.md                 # Documentation pages
├── scripts/                  # Processing scripts
│   └── hugo_generator.py
└── website/                  # Generated Hugo site (git-ignored)
```

## Contributing

To add or update content:
1. Edit markdown files in `content/` directory
2. Run `make` and follow instructions to preview the website locally
3. Submit a pull request

The `website/` directory is automatically generated and should not be edited directly.
"""
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.log(f"Generated {readme_path}", 'success')
    
    def check_hugo_installed(self):
        """Check if Hugo is installed"""
        try:
            result = subprocess.run(['hugo', 'version'], capture_output=True, text=True)
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                self.log(f"Hugo found: {version_line}", 'info')
                return True
        except FileNotFoundError:
            pass
        
        self.log("Hugo not found. Install from https://gohugo.io", 'warning')
        return False
    
    def build_site(self, minify=False):
        """Build the Hugo site"""
        if not self.check_hugo_installed():
            return False
        
        original_dir = os.getcwd()
        try:
            os.chdir(self.website_dir)
            
            cmd = ['hugo']
            if minify:
                cmd.append('--minify')
            
            self.log("Building site with Hugo...", 'info')
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.log(f"Site built successfully in {self.website_dir}/public", 'success')
                return True
            else:
                self.log(f"Hugo build failed: {result.stderr}", 'error')
                return False
                
        finally:
            os.chdir(original_dir)


    def serve_site(self, port=1313):
        """Start Hugo development server"""
        if not self.check_hugo_installed():
            return False

        original_dir = os.getcwd()
        try:
            os.chdir(self.website_dir)
            if port == 1313:
                self.log(f"Starting Hugo server (Hugo will choose available port)", 'info')
                self.log("Press Ctrl+C to stop...", 'info')
                subprocess.run(['hugo', 'server'])
            else:
                self.log(f"Starting Hugo server at http://localhost:{port}", 'info')
                self.log("Press Ctrl+C to stop...", 'info')
                subprocess.run(['hugo', 'server', '--port', str(port)])
            
        except KeyboardInterrupt:
            self.log("\nServer stopped", 'info')
        finally:
            os.chdir(original_dir)
    
    def run_full_pipeline(self, download_theme=True, generate_readme=True, 
                         build=False, serve=False, minify=False):
        """Run the complete processing pipeline"""
        self.log("=== Hugo Site Generator ===\n", 'info')
        
        # Step 1: Setup directories
        self.log("Step 1: Setting up directories...", 'info')
        self.setup_directories()
        
        # Step 2: Download theme if requested
        if download_theme:
            self.log("\nStep 2: Downloading theme...", 'info')
            self.download_theme()
        else:
            self.log("\nStep 2: Skipping theme download", 'info')
        
        # Step 3: Copy content files with transformation (includes xqtl-data)
        self.log("\nStep 3: Copying content files with original structure...", 'info')
        self.copy_content_files()
        
        # Step 4: Collect metadata for README generation (but don't create alphabetical sections)
        self.log("\nStep 4: Collecting metadata for README...", 'info')
        all_items = self.collect_xqtl_metadata()
        
        # Step 5: Create navigation menu
        self.log("\nStep 5: Creating navigation menu...", 'info')
        self.create_menu()
        
        # Step 6: Create Hugo config
        self.log("\nStep 6: Creating Hugo configuration...", 'info')
        self.create_hugo_config()
        
        # Step 7: Generate README if requested
        if generate_readme and all_items:
            self.log("\nStep 7: Generating README...", 'info')
            self.generate_readme(all_items)
        
        # Step 8: Build if requested
        if build or serve:
            self.log("\nStep 8: Building site...", 'info')
            if not serve:  # Only build without serving
                self.build_site(minify=minify)
        
        # Step 9: Serve if requested
        if serve:
            self.log("\nStep 9: Starting server...", 'info')
            self.serve_site()
        
        self.log("\n=== Processing complete! ===", 'success')
        
        if not serve and not build:
            self.log("\nNext steps:", 'info')
            self.log(f"  cd {self.website_dir} && hugo server  # Preview locally", 'info')
            self.log(f"  cd {self.website_dir} && hugo --minify  # Build for production", 'info')
        
        if self.problematic_files:
            self.log(f"\nWarning: {len(self.problematic_files)} files had processing issues:", 'warning')
            for f in self.problematic_files[:5]:  # Show first 5
                self.log(f"  - {f}", 'warning')
            if len(self.problematic_files) > 5:
                self.log(f"  ... and {len(self.problematic_files) - 5} more", 'warning')
        
        return True


def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(
        description='Hugo Site Generator for xQTL Resources',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic processing and serve locally
  %(prog)s --serve
  
  # Build for production
  %(prog)s --build --minify
  
  # Custom paths
  %(prog)s --content-dir content --website-dir website --serve
  
  # For GitHub Actions
  %(prog)s --base-url https://statfungen.github.io/xqtl-resources/ --build --minify
"""
    )
    
    # Path arguments
    parser.add_argument('--content-dir', default=DEFAULT_CONTENT_DIR,
                       help=f'Source content directory (default: {DEFAULT_CONTENT_DIR})')
    parser.add_argument('--website-dir', default=DEFAULT_WEBSITE_DIR,
                       help=f'Output website directory (default: {DEFAULT_WEBSITE_DIR})')
    parser.add_argument('--base-url', default=DEFAULT_BASE_URL,
                       help=f'Base URL for Hugo (default: {DEFAULT_BASE_URL})')
    
    # Processing options
    parser.add_argument('--no-theme-download', action='store_true',
                       help='Skip downloading Hugo theme')
    parser.add_argument('--no-readme', action='store_true',
                       help='Skip generating README.md')
    
    # Build/serve options
    parser.add_argument('--build', action='store_true',
                       help='Build the site after processing')
    parser.add_argument('--minify', action='store_true',
                       help='Minify the built site (use with --build)')
    parser.add_argument('--serve', action='store_true',
                       help='Start Hugo server after processing')
    parser.add_argument('--port', type=int, default=1313,
                       help='Port for Hugo server (default: 1313)')
    
    # Other options
    parser.add_argument('--quiet', action='store_true',
                       help='Suppress output messages')
    
    args = parser.parse_args()
    
    # Create generator instance
    generator = HugoSiteGenerator(
        content_dir=args.content_dir,
        website_dir=args.website_dir,
        base_url=args.base_url,
        verbose=not args.quiet
    )
    
    # Run pipeline
    success = generator.run_full_pipeline(
        download_theme=not args.no_theme_download,
        generate_readme=not args.no_readme,
        build=args.build,
        serve=args.serve,
        minify=args.minify
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()