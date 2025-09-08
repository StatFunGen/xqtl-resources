#!/usr/bin/env python3
"""
Hugo site generator for xQTL Resources
Handles content transformation and organization for Hugo
Uses Hugo Book theme's automatic navigation generation
"""

import os
import re
import sys
import argparse
import subprocess
import shutil
import urllib.request
import zipfile
import tempfile
from pathlib import Path
from collections import defaultdict

# Configuration defaults
DEFAULT_CONTENT_DIR = 'content'
DEFAULT_WEBSITE_DIR = 'website'
DEFAULT_BASE_URL = 'https://statfungen.github.io/xqtl-resources/'
DEFAULT_GITHUB_URL = 'https://github.com/StatFunGen/xqtl-resources/tree/main/'
HUGO_BOOK_THEME_URL = 'https://github.com/alex-shpak/hugo-book/archive/refs/heads/master.zip'

class HugoSiteGenerator:
    """Hugo site generator with content transformation"""
    
    def __init__(self, content_dir=DEFAULT_CONTENT_DIR, website_dir=DEFAULT_WEBSITE_DIR, 
                 base_url=DEFAULT_BASE_URL, github_url=DEFAULT_GITHUB_URL, verbose=True):
        self.source_content_dir = content_dir
        self.data_dir = os.path.join(content_dir, 'xqtl-data')
        self.website_dir = website_dir
        self.website_content_dir = os.path.join(website_dir, 'content')
        self.themes_dir = os.path.join(website_dir, 'themes')
        self.base_url = base_url
        self.github_url = github_url
        self.verbose = verbose
        self.problematic_files = []
        
    def log(self, message, level='info'):
        """Simple logging function"""
        if self.verbose:
            prefix = {
                'info': '→',
                'success': '✔',
                'warning': '⚠',
                'error': '✗'
            }.get(level, '→')
            print(f"{prefix} {message}")
    
    def setup_directories(self):
        """Create necessary directory structure"""
        dirs = [
            self.website_dir,
            self.website_content_dir,
            self.themes_dir
        ]
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
        self.log(f"Created directory structure in {self.website_dir}", 'success')
    
    def download_theme(self, force=False):
        """Download Hugo Book theme with proper error handling"""
        theme_path = os.path.join(self.themes_dir, 'hugo-book')
        
        if os.path.exists(theme_path) and not force:
            self.log("Theme already exists, skipping download", 'info')
            return True
        
        self.log("Downloading Hugo Book theme...", 'info')
        
        # Use temporary file for safer download
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp_file:
            tmp_path = tmp_file.name
        
        try:
            # Download theme
            urllib.request.urlretrieve(HUGO_BOOK_THEME_URL, tmp_path)
            
            # Extract theme
            with zipfile.ZipFile(tmp_path, 'r') as zip_ref:
                zip_ref.extractall(self.themes_dir)
            
            # Find and rename extracted directory
            for item in os.listdir(self.themes_dir):
                if item.startswith('hugo-book') and item != 'hugo-book':
                    old_path = os.path.join(self.themes_dir, item)
                    if os.path.exists(theme_path):
                        shutil.rmtree(theme_path)
                    os.rename(old_path, theme_path)
                    break
            
            self.log("Theme downloaded successfully", 'success')
            return True
            
        except Exception as e:
            self.log(f"Failed to download theme: {e}", 'error')
            self.log(f"You can manually clone: git clone https://github.com/alex-shpak/hugo-book.git {theme_path}", 'info')
            return False
        finally:
            # Clean up temp file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def create_hugo_config(self):
        """Copy Hugo configuration file from source repository"""
        source_config = 'hugo.toml'
        dest_config = os.path.join(self.website_dir, 'hugo.toml')
    
        if not os.path.exists(source_config):
            self.log(f"Error: hugo.toml not found in repository root", 'error')
            self.log(f"Expected location: {os.path.abspath(source_config)}", 'error')
            return False
    
        try:
            shutil.copy2(source_config, dest_config)
            self.log(f"Copied hugo.toml to {dest_config}", 'success')
            return True
        except Exception as e:
            self.log(f"Failed to copy hugo.toml: {e}", 'error')
            return False
    
    def sanitize_markdown_content(self, content):
        """Sanitize markdown content to avoid Hugo parsing errors"""
        if not content:
            return content
        
        # Fix unquoted attributes in links/images
        content = re.sub(r'\{([^}]+)=([^}"]+)\}', r'{$1="$2"}', content)
        
        # Escape {{ and }} in code blocks and inline code
        def escape_braces(match, is_block=False):
            code = match.group(1)
            code = code.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')
            return f'```{code}```' if is_block else f'`{code}`'
        
        content = re.sub(r'```(.*?)```', lambda m: escape_braces(m, True), content, flags=re.DOTALL)
        content = re.sub(r'`([^`]+)`', lambda m: escape_braces(m, False), content)
        
        # Remove Pandoc-style attributes
        content = re.sub(r'\{\.[\w\s-]+\}', '', content)
        
        return content
    
    def extract_title_from_content(self, content, filepath):
        """Extract title from markdown content or generate from filepath"""
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        return Path(filepath).stem.replace('-', ' ').replace('_', ' ').title()
    
    def calculate_weight(self, filepath, is_index=False):
        """Calculate weight for ordering in navigation"""
        if is_index:
            return 1
        
        # Special files get priority
        filename = os.path.basename(filepath).lower()
        if 'overview' in filename or 'introduction' in filename:
            return 5
        if 'readme' in filename:
            return 10
        
        # Default weight for regular files
        return 50
    
    def add_frontmatter(self, content, title, filepath, depth_level=1):
        """Add Hugo frontmatter to markdown content
        
        Hugo Book theme automatically generates navigation based on:
        - Directory structure (hierarchy)
        - _index.md files (create sections) 
        - Weight values (control ordering)
        - bookHidden (hide from nav but keep accessible)
        - bookCollapseSection (collapse sections for cleaner nav)
        """
        safe_title = title.replace('"', '\\"')
        
        # Determine if this is an index file
        filename = os.path.basename(filepath)
        is_index = filename == 'README.md' or filename == '_index.md'
        
        # Calculate weight
        weight = self.calculate_weight(filepath, is_index)
        
        # Only hide deep non-index files from navigation
        book_hidden = "bookHidden: true\n" if depth_level > 2 and not is_index else ""
        
        # Collapse sections at level 2 for cleaner navigation
        book_collapse = "bookCollapseSection: true\n" if depth_level == 2 and is_index else ""
        
        frontmatter = f"""---
title: "{safe_title}"
weight: {weight}
bookToc: true
{book_collapse}{book_hidden}---

"""
        return frontmatter + content
    
    def process_markdown_file(self, source_file, dest_file, depth_level=1):
        """Process a single markdown file with all transformations"""
        try:
            # Read content
            with open(source_file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            
            # Extract title and sanitize content
            title = self.extract_title_from_content(content, source_file)
            content = self.sanitize_markdown_content(content)
            
            # Add frontmatter
            content = self.add_frontmatter(content, title, source_file, depth_level)
            
            # Ensure destination directory exists
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            
            # Write to destination
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
            
        except Exception as e:
            self.log(f"Error processing {source_file}: {e}", 'error')
            self.problematic_files.append(source_file)
            return False
    
    def copy_static_files(self):
        """Copy static files (images, PDFs, etc.) that might be referenced in markdown"""
        static_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf', '.csv', '.json'}
        copied_count = 0
        
        for root, dirs, files in os.walk(self.source_content_dir):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                ext = Path(filename).suffix.lower()
                if ext in static_extensions:
                    source_file = os.path.join(root, filename)
                    rel_path = os.path.relpath(source_file, self.source_content_dir)
                    dest_file = os.path.join(self.website_content_dir, rel_path)
                    
                    try:
                        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                        shutil.copy2(source_file, dest_file)
                        copied_count += 1
                    except Exception as e:
                        self.log(f"Failed to copy static file {rel_path}: {e}", 'warning')
        
        if copied_count > 0:
            self.log(f"Copied {copied_count} static files", 'success')
        
        return copied_count
    
    def copy_content_files(self):
        """Copy and transform all content files"""
        self.log("Copying and transforming content files...", 'info')
        
        processed_count = 0
        
        # Process all markdown files recursively
        for root, dirs, files in os.walk(self.source_content_dir):
            # Skip hidden directories and the website directory
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'website']
            
            for filename in files:
                if not filename.endswith('.md'):
                    continue
                
                source_file = os.path.join(root, filename)
                
                # Calculate relative path and depth
                rel_dir = os.path.relpath(root, self.source_content_dir)
                if rel_dir == '.':
                    rel_dir = ''
                    depth_level = 1
                else:
                    depth_level = len(rel_dir.split(os.sep)) + 1
                
                # Determine destination filename and path
                dest_filename = '_index.md' if filename == 'README.md' else filename
                
                # Build destination path
                if rel_dir:
                    dest_dir = os.path.join(self.website_content_dir, rel_dir)
                    dest_file = os.path.join(dest_dir, dest_filename)
                    log_path = os.path.join(rel_dir, filename)
                else:
                    dest_file = os.path.join(self.website_content_dir, dest_filename)
                    log_path = filename
                
                # Process the file
                if self.process_markdown_file(source_file, dest_file, depth_level):
                    dest_log_path = os.path.relpath(dest_file, self.website_content_dir)
                    self.log(f"  Transformed: {log_path} → {dest_log_path}", 'success')
                    processed_count += 1
        
        # Copy static files
        static_count = self.copy_static_files()
        
        self.log(f"Processed {processed_count} markdown files", 'success')
        return processed_count
    
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
            
            # Extract title
            metadata['title'] = self.extract_title_from_content(content, filepath)
            
            lines = content.split('\n')
            
            # Get description (first non-heading line after title)
            in_description = False
            for line in lines:
                if metadata['title'] and line.strip().startswith('# ' + metadata['title']):
                    in_description = True
                    continue
                if in_description and line.strip() and not line.startswith('#'):
                    desc = line.strip().rstrip('.')
                    if desc:
                        metadata['description'] = desc + '.'
                    break
            
            # Extract lead analysts
            lead_match = re.search(
                r'(?:Lead analysts?|Contact|Contributors?):\s*(.+?)(?:\n|$)', 
                content, 
                re.IGNORECASE | re.MULTILINE
            )
            if lead_match:
                lead = lead_match.group(1).strip()
                # Clean up the lead analyst text
                lead = re.sub(r'\([^)]+\)', '', lead)  # Remove parentheses
                lead = re.sub(r'<[^>]+>', '', lead)     # Remove emails
                lead = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', lead)  # Remove markdown links
                lead = re.sub(r'\s+', ' ', lead).strip('. ')
                if lead:
                    metadata['lead_analysts'] = lead
            
            return metadata
            
        except Exception as e:
            self.log(f"Error reading metadata from {filepath}: {e}", 'warning')
            return metadata
    
    def collect_xqtl_metadata(self):
        """Collect metadata from xqtl-data files for README generation"""
        if not os.path.exists(self.data_dir):
            self.log(f"xqtl-data directory not found at {self.data_dir}", 'warning')
            return []
        
        # Find all markdown files in xqtl-data (excluding README files)
        all_files = []
        for root, dirs, files in os.walk(self.data_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for f in files:
                if f.endswith('.md') and f.lower() != 'readme.md':
                    all_files.append(os.path.join(root, f))
        
        if not all_files:
            self.log(f"No markdown files found in {self.data_dir}", 'warning')
            return []
        
        self.log(f"Found {len(all_files)} markdown files in xqtl-data", 'info')
        
        # Extract metadata from files
        all_items = []
        for filepath in all_files:
            metadata = self.get_metadata_from_file(filepath)
            if metadata and metadata.get('title'):
                all_items.append(metadata)
        
        if all_items:
            self.log(f"Collected metadata from {len(all_items)} xqtl-data items", 'success')
        
        return all_items
    
    def generate_readme(self, all_items):
        """Generate README.md for the repository"""
        if not all_items:
            self.log("No items to include in README", 'warning')
            return False
        
        readme_path = 'README.md'
        
        content = f"""# `README` automatically generated by `scripts/hugo_generator.py`

This repository contains {len(all_items)} datasets developed by the ADSP Functional Genomics Consortium.

Published at: {self.base_url}

## Dataset Categories

"""
        
        # Group by category
        by_category = defaultdict(list)
        for item in all_items:
            by_category[item['category']].append(item)
        
        # Category configuration
        category_order = ['study_info', 'gwas', 'omics', 'qtl', 'reference_data']
        category_names = {
            'study_info': 'Study Information',
            'gwas': 'GWAS Summary Statistics',
            'omics': 'Omics Data',
            'qtl': 'QTL Results',
            'reference_data': 'Reference Data'
        }
        
        # Write each category
        for cat in category_order:
            if cat in by_category:
                cat_title = category_names.get(cat, cat.replace('_', ' ').title())
                items = sorted(by_category[cat], key=lambda x: x['title'].lower())
                
                content += f"### {cat_title} ({len(items)} datasets)\n\n"
                
                for item in items:
                    rel_path = os.path.relpath(item['filepath'], '.')
                    github_link = f"{self.github_url}{rel_path}"
                    
                    entry = f"- [{item['title']}]({github_link})"
                    if item.get('description'):
                        entry += f": {item['description']}"
                    if item.get('lead_analysts'):
                        entry += f" (Lead: {item['lead_analysts']})"
                    content += entry + "\n"
                
                content += "\n"
        
        # Add repository structure and contributing sections
        content += """## Repository Structure

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
2. Run `make` or `python scripts/hugo_generator.py --serve` to preview locally
3. Submit a pull request

The `website/` directory is automatically generated and should not be edited directly.

## Building the Site

```bash
# Install Hugo (https://gohugo.io/getting-started/installing/)
# Then run:

# Generate and serve locally
python scripts/hugo_generator.py --serve

# Build for production
python scripts/hugo_generator.py --build --minify
```
"""
        
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.log(f"Generated {readme_path}", 'success')
            return True
        except Exception as e:
            self.log(f"Failed to generate README: {e}", 'error')
            return False
    
    def check_hugo_installed(self):
        """Check if Hugo is installed and get version"""
        try:
            result = subprocess.run(['hugo', 'version'], capture_output=True, text=True)
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                self.log(f"Hugo found: {version_line}", 'info')
                
                # Check for minimum version (optional)
                version_match = re.search(r'v(\d+)\.(\d+)', version_line)
                if version_match:
                    major, minor = map(int, version_match.groups())
                    if major == 0 and minor < 80:
                        self.log("Warning: Hugo version < 0.80, some features may not work", 'warning')
                
                return True
        except FileNotFoundError:
            pass
        
        self.log("Hugo not found. Install from https://gohugo.io/getting-started/installing/", 'error')
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
                public_dir = os.path.join(self.website_dir, 'public')
                if os.path.exists(public_dir):
                    file_count = sum(len(files) for _, _, files in os.walk(public_dir))
                    self.log(f"Site built successfully: {file_count} files in {public_dir}", 'success')
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
            
            cmd = ['hugo', 'server']
            if port != 1313:
                cmd.extend(['--port', str(port)])
            
            self.log(f"Starting Hugo server on port {port}...", 'info')
            self.log("Press Ctrl+C to stop", 'info')
            
            subprocess.run(cmd)
            
        except KeyboardInterrupt:
            self.log("\nServer stopped", 'info')
        finally:
            os.chdir(original_dir)
    
    def run_full_pipeline(self, download_theme=True, generate_readme=True, 
                         build=False, serve=False, minify=False):
        """Run the complete processing pipeline"""
        self.log("=== Hugo Site Generator ===\n", 'info')
        
        # Track overall success
        success = True
        
        # Step 1: Setup
        self.log("Step 1: Setting up directories...", 'info')
        self.setup_directories()
        
        # Step 2: Theme
        if download_theme:
            self.log("\nStep 2: Downloading theme...", 'info')
            if not self.download_theme():
                success = False
                self.log("Theme download failed but continuing...", 'warning')
        else:
            self.log("\nStep 2: Skipping theme download", 'info')
        
        # Step 3: Content
        self.log("\nStep 3: Processing content files...", 'info')
        file_count = self.copy_content_files()
        if file_count == 0:
            self.log("Warning: No content files were processed", 'warning')
            success = False
        
        # Step 4: Metadata
        self.log("\nStep 4: Collecting metadata for README...", 'info')
        all_items = self.collect_xqtl_metadata()
        
        # Step 5: Config
        self.log("\nStep 5: Creating Hugo configuration...", 'info')
        if not self.create_hugo_config():
            self.log("Failed to create Hugo config", 'error')
            success = False
        
        # Step 6: README
        if generate_readme:
            self.log("\nStep 6: Generating README...", 'info')
            self.generate_readme(all_items)
        
        # Step 7: Build
        if build or serve:
            self.log("\nStep 7: Building site...", 'info')
            if not serve:  # Only build without serving
                if not self.build_site(minify=minify):
                    success = False
        
        # Step 8: Serve
        if serve:
            self.log("\nStep 8: Starting server...", 'info')
            self.serve_site()
        
        # Final report
        self.log("\n=== Processing complete! ===", 'success')
        
        if not serve and not build:
            self.log("\nNext steps:", 'info')
            self.log(f"  cd {self.website_dir} && hugo server", 'info')
            self.log(f"  cd {self.website_dir} && hugo --minify", 'info')
        
        if self.problematic_files:
            self.log(f"\nWarning: {len(self.problematic_files)} files had issues:", 'warning')
            for f in self.problematic_files[:5]:
                rel_path = os.path.relpath(f, '.')
                self.log(f"  - {rel_path}", 'warning')
            if len(self.problematic_files) > 5:
                self.log(f"  ... and {len(self.problematic_files) - 5} more", 'warning')
        
        return success


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
  %(prog)s --content-dir custom/content --website-dir custom/website
  
  # Skip theme download (if already installed)
  %(prog)s --no-theme-download --serve
  
  # For GitHub Actions
  %(prog)s --base-url https://statfungen.github.io/xqtl-resources/ --build --minify

Notes:
  - Hugo must be installed: https://gohugo.io/getting-started/installing/
  - The website/ directory is auto-generated (should be in .gitignore)
  - Edit content in content/ directory, not in website/
"""
    )
    
    # Path arguments
    parser.add_argument('--content-dir', default=DEFAULT_CONTENT_DIR,
                       help=f'Source content directory (default: {DEFAULT_CONTENT_DIR})')
    parser.add_argument('--website-dir', default=DEFAULT_WEBSITE_DIR,
                       help=f'Output website directory (default: {DEFAULT_WEBSITE_DIR})')
    parser.add_argument('--base-url', default=DEFAULT_BASE_URL,
                       help=f'Base URL for the site (default: {DEFAULT_BASE_URL})')
    parser.add_argument('--github-url', default=DEFAULT_GITHUB_URL,
                       help=f'GitHub repository URL (default: {DEFAULT_GITHUB_URL})')
    
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
    
    # Validate arguments
    if args.minify and not args.build and not args.serve:
        parser.error("--minify requires --build or --serve")
    
    # Create generator instance
    generator = HugoSiteGenerator(
        content_dir=args.content_dir,
        website_dir=args.website_dir,
        base_url=args.base_url,
        github_url=args.github_url,
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
