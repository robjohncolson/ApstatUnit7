import re
import os

def verify_conversion(file_path):
    """
    Verify that the HTML file has been properly converted from Unit 5 to Unit 6
    by checking for any remaining references to Unit 5.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define patterns to search for - refined to avoid false positives
    unit5_patterns = [
        r'Unit 5',
        r'unit 5',
        r'Unit5',
        r'unit5',
        r'Topic 5\.',
        r'topic 5\.',
        r'\b5-\d+\b',  # IDs like 5-1, 5-2, etc. with word boundaries
        r'/5_',        # PDF paths like /5_quiz.pdf with slash prefix
        r'/5\.pdf',    # With slash prefix
        r'apStatsUnit5',
        r'7-12%',      # Unit 5 exam weight
        r'pdfs/unit5'
    ]
    
    print(f"Verifying {file_path} for Unit 5 references...")
    
    # Search for patterns and collect results
    issues = []
    for pattern in unit5_patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            line_no = content[:match.start()].count('\n') + 1
            context_start = max(0, match.start() - 30)
            context_end = min(len(content), match.end() + 30)
            context = content[context_start:context_end].replace('\n', ' ')
            issues.append(f"Line {line_no}: Found '{match.group()}' in: ...{context}...")
    
    # Check if Unit 6 has correct exam weight
    if '12-15%' not in content:
        issues.append("Could not find the correct exam weight for Unit 6 (12-15%)")
    
    # Report results
    if issues:
        print(f"\n⚠️ Found {len(issues)} issues that need to be fixed:")
        for issue in issues:
            print(f"  • {issue}")
        return False
    else:
        print("\n✅ No Unit 5 references found! Conversion appears complete.")
        return True

def verify_pdf_files():
    """
    Verify that all PDF files for Unit 6 are properly referenced in the HTML
    """
    # List all PDF files in the Unit 6 directory
    pdf_dir = "pdfs/unit6"
    if not os.path.exists(pdf_dir):
        print(f"⚠️ Directory {pdf_dir} does not exist!")
        return False
    
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    
    # Read the HTML content
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check each PDF file
    missing_pdfs = []
    for pdf in pdf_files:
        if pdf not in content and 'original_files' not in pdf:
            missing_pdfs.append(pdf)
    
    if missing_pdfs:
        print(f"\n⚠️ Found {len(missing_pdfs)} PDF files not referenced in the HTML:")
        for pdf in missing_pdfs:
            print(f"  • {pdf}")
        return False
    else:
        print("\n✅ All PDF files are properly referenced in the HTML.")
        return True

if __name__ == "__main__":
    html_verified = verify_conversion('index.html')
    pdf_verified = verify_pdf_files()
    
    if html_verified and pdf_verified:
        print("\n🎉 Conversion verification completed successfully!")
    else:
        print("\n⚠️ Conversion verification failed. Please fix the issues listed above.") 