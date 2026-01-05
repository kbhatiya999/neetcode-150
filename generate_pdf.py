#!/usr/bin/env python3
import os
import subprocess
import re

# --- A4 Standard Dimensions (inches) ---
A4_WIDTH = 8.27
A4_HEIGHT = 11.69

def get_files(directory):
    files = []
    for f in os.listdir(directory):
        if f.endswith('.md') or f.endswith('.py'):
            files.append(f)
    
    # Sort files numerically by prefix
    def sort_key(filename):
        match = re.match(r'(\d+)', filename)
        if match:
            return (int(match.group(1)), filename)
        return (float('inf'), filename)
    
    files.sort(key=sort_key)
    return files

def generate_unified_markdown(directory, files, output_md, width, height):
    with open(output_md, 'w', encoding='utf-8') as outfile:
        # Optimized typography for extreme compact printing
        outfile.write("<style>\n")
        outfile.write(f"  @page {{ size: {width}in {height}in; margin: 0.1in; }}\n")
        outfile.write("  body { font-size: 8pt; line-height: 1.1; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }\n")
        outfile.write("  h1 { font-size: 1.25em; } h2 { font-size: 1.15em; } h3 { font-size: 1.05em; }\n")
        outfile.write("  h1, h2, h3 { margin-top: 0.3em; margin-bottom: 0.1em; }\n")
        outfile.write("  pre { background-color: #f6f8fa; padding: 4px; border-radius: 2px; border: 1px solid #ddd; margin: 0.3em 0; font-size: 7pt; overflow-x: hidden; }\n")
        outfile.write("  hr { margin: 0.5em 0; border: 0; border-top: 1px solid #eee; }\n")
        outfile.write("  .file-header { font-weight: bold; color: #444; background: #eef; padding: 1px 4px; border-radius: 2px; font-size: 0.75em; margin: 0; }\n")
        outfile.write("  p, ul, ol { margin: 0.2em 0; }\n")
        outfile.write("</style>\n\n")

        for i, filename in enumerate(files):
            filepath = os.path.join(directory, filename)
            outfile.write(f'<p class="file-header">{filename}</p>\n\n')
            
            if filename.endswith('.md'):
                with open(filepath, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
            elif filename.endswith('.py'):
                outfile.write("```python\n")
                with open(filepath, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                outfile.write("\n```")
            
            outfile.write("\n\n---\n\n")

def get_available_folders(root_dir="."):
    """Find directories that look like user folders (contain .md and .py files)."""
    folders = []
    # Primary user folders usually contain subdirs or are subdirs of known users
    for item in sorted(os.listdir(root_dir)):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            # Check for immediate subdirs like Python3 or Solution
            sub_found = False
            for sub in sorted(os.listdir(item_path)):
                sub_path = os.path.join(item_path, sub)
                if os.path.isdir(sub_path) and not sub.startswith('.'):
                    folders.append(os.path.join(item, sub))
                    sub_found = True
            if not sub_found:
                folders.append(item)
    return sorted(folders)

def main():
    temp_md = 'unified.md'
    
    import sys
    target_dir = None
    orientation = None
    w_div = None
    h_div = None
    
    # Check for CLI arguments: [target_dir] [orientation] [width_divisor] [height_divisor]
    if len(sys.argv) >= 5:
        target_dir = sys.argv[1]
        orientation = sys.argv[2].lower()
        w_div = float(sys.argv[3])
        h_div = float(sys.argv[4])
    else:
        print("\n--- NeetCode 150 PDF Generator (A4 Scale) ---")
        
        # Folder selection
        available = get_available_folders()
        print("\nAvailable User Folders:")
        for idx, folder in enumerate(available, 1):
            print(f"{idx}. {folder}")
        
        try:
            folder_choice = input(f"\nSelect a folder (1-{len(available)}) [default: 1]: ").strip()
            if not folder_choice:
                target_dir = available[0]
            elif folder_choice.isdigit() and 1 <= int(folder_choice) <= len(available):
                target_dir = available[int(folder_choice)-1]
            else:
                target_dir = folder_choice if os.path.isdir(folder_choice) else available[0]
        except (ValueError, IndexError):
            target_dir = available[0]

        print(f"\nTarget Folder: {target_dir}")
        orient_input = input("Select Orientation (p: Portrait, l: Landscape) [default: p]: ").strip().lower()
        orientation = 'l' if orient_input == 'l' else 'p'
        
        try:
            w_div_input = input("Enter Width Divisor (e.g., 2 for half width) [default: 2]: ").strip()
            w_div = float(w_div_input) if w_div_input else 2.0
            h_div_input = input("Enter Height Divisor (e.g., 2 for half height) [default: 2]: ").strip()
            h_div = float(h_div_input) if h_div_input else 2.0
        except ValueError:
            print("Invalid input, using 2x2 scale.")
            w_div, h_div = 2.0, 2.0

    if not target_dir or not os.path.isdir(target_dir):
        print(f"Error: Target directory '{target_dir}' not found.")
        return

    # Physical A4 dimensions based on orientation
    if orientation == 'l':
        phys_w, phys_h = A4_HEIGHT, A4_WIDTH
        orient_name = "Landscape"
    else:
        phys_w, phys_h = A4_WIDTH, A4_HEIGHT
        orient_name = "Portrait"
    
    # Logical page size = Page size / Divisor
    log_w = phys_w / w_div
    log_h = phys_h / h_div
    
    # Format divisor strings for filename
    w_str = str(w_div).replace('.', 'p') if w_div != int(w_div) else str(int(w_div))
    h_str = str(h_div).replace('.', 'p') if h_div != int(h_div) else str(int(h_div))
    
    # Use only the basename of the target_dir for the filename
    folder_basename = target_dir.replace('/', '_').replace('\\', '_')
    layout_name = f"{folder_basename}_{orient_name}_W{w_str}_H{h_str}"
    output_pdf = f"NeetCode150_{layout_name}.pdf"
    
    print(f"\nActive Layout: {layout_name}")
    print(f"Physical Page: A4 {orient_name} ({phys_w}\" x {phys_h}\")")
    print(f"Logical Page: 1/{w_div} width x 1/{h_div} height => {log_w:.2f}\" x {log_h:.2f}\"")
    
    print(f"\nScanning directory: {target_dir}")
    files = get_files(target_dir)
    if not files:
        print(f"No .md or .py files found in {target_dir}")
        return
    print(f"Found {len(files)} files.")
    
    print(f"Generating temporary Markdown: {temp_md}")
    generate_unified_markdown(target_dir, files, temp_md, log_w, log_h)
    
    print(f"Converting to PDF using npx md-to-pdf...")
    try:
        # Explicit PDF options for the calculated layout
        pdf_options = f'{{"width": "{log_w:.2f}in", "height": "{log_h:.2f}in", "printBackground": true, "preferCSSPageSize": true}}'
        result = subprocess.run([
            'npx', '--yes', 'md-to-pdf', temp_md, 
            '--pdf-options', pdf_options
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully generated {output_pdf}")
            if os.path.exists('unified.pdf'):
                if os.path.exists(output_pdf):
                    os.remove(output_pdf)
                os.rename('unified.pdf', output_pdf)
                print(f"Saved as: {output_pdf}")
        else:
            print(f"Error during PDF generation: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists(temp_md):
            os.remove(temp_md)
            print(f"Cleaned up {temp_md}")

if __name__ == "__main__":
    main()
