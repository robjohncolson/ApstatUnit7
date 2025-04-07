#!/usr/bin/env python3
import re
import os
import sys
from pathlib import Path

def extract_pdf_paths(html_file_path):
    """Extract all PDF paths from the index.html file."""
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regular expression to find all PDF paths in the file
    pattern = r'(questionPdf|answersPdf):\s*\"(pdfs/unit7/.*?\.pdf)\"'
    matches = re.findall(pattern, content)
    
    # Create a dictionary of path types and their paths
    pdf_paths = {}
    for match_type, path in matches:
        if path not in pdf_paths:
            pdf_paths[path] = []
        pdf_paths[path].append(match_type)
    
    return pdf_paths

def get_actual_pdf_files(base_dir):
    """Get all PDF files in the pdfs/unit7 directory."""
    unit7_dir = os.path.join(base_dir, 'pdfs', 'unit7')
    if not os.path.exists(unit7_dir):
        print(f"Error: Directory {unit7_dir} not found!")
        return []
    
    pdf_files = []
    for root, _, files in os.walk(unit7_dir):
        for file in files:
            if file.endswith('.pdf'):
                # Get the relative path from the base directory
                rel_path = os.path.join('pdfs', 'unit7', file)
                rel_path = rel_path.replace('\\', '/')  # Normalize path separators
                pdf_files.append(rel_path)
    
    return pdf_files

def check_pdf_paths(base_dir):
    """Check if all PDF paths in index.html exist and if any files are not referenced."""
    html_file_path = os.path.join(base_dir, 'index.html')
    if not os.path.exists(html_file_path):
        print(f"Error: HTML file {html_file_path} not found!")
        return
    
    # Extract PDF paths from index.html
    referenced_paths = extract_pdf_paths(html_file_path)
    
    # Get actual PDF files
    actual_files = get_actual_pdf_files(base_dir)
    
    # Check if referenced paths exist
    missing_files = []
    for path in referenced_paths:
        if path not in actual_files:
            missing_files.append((path, referenced_paths[path]))
    
    # Check if any actual files are not referenced
    unreferenced_files = []
    for file in actual_files:
        # Skip files in original_files directory, and files with SG_ or TB_ prefixes
        if (file not in referenced_paths and 
            'original_files' not in file and 
            not os.path.basename(file).startswith(('SG_', 'TB_'))):
            unreferenced_files.append(file)
    
    # Count special files for the report
    sg_tb_files = []
    for file in actual_files:
        if os.path.basename(file).startswith(('SG_', 'TB_')):
            sg_tb_files.append(file)
    
    # Print results
    print("PDF Path Verification Results:")
    print("-" * 50)
    
    if missing_files:
        print("\nMissing files (referenced in index.html but not found):")
        for path, types in missing_files:
            type_str = ", ".join(types)
            print(f"  - {path} (referenced as {type_str})")
    else:
        print("\nAll referenced PDF files exist! ✓")
    
    if unreferenced_files:
        print("\nUnreferenced files (exist but not referenced in index.html):")
        for file in unreferenced_files:
            print(f"  - {file}")
    else:
        print("\nAll PDF files are properly referenced! ✓")
    
    # Print a summary
    print("\nSummary:")
    print(f"  - Total referenced PDF paths: {len(referenced_paths)}")
    print(f"  - Total actual PDF files: {len(actual_files)}")
    print(f"  - Missing files: {len(missing_files)}")
    print(f"  - Unreferenced files: {len(unreferenced_files)}")
    print(f"  - SG_/TB_ prefixed files (excluded from unreferenced count): {len(sg_tb_files)}")

if __name__ == "__main__":
    base_dir = os.getcwd()
    
    # If a directory is provided as a command-line argument, use it
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    
    check_pdf_paths(base_dir) 