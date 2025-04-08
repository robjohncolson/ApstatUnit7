import re

# Path to the file (read-only mode)
file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    lines = content.split('\n')

# Locations identified by the analysis script
fix_locations = [
    # Line ranges for first set of fixes (change 1-capstone_q to 3-capstone_q)
    (3176, 3178),  # First block
    (3264, 3266),  # Second block
    (3305, 3307),  # Third block
]

print("# RECOMMENDED FIXES")
print("# The following edits should be made to index.html:\n")

# 1. Generate fix for the 1-capstone_q references
for start_line, end_line in fix_locations:
    print(f"## Fix for lines {start_line}-{end_line}")
    
    # Extract the block of lines to modify
    block = lines[start_line-1:end_line]
    
    # Prepare the original and modified versions for comparison
    original = '\n'.join(block)
    modified = original.replace('quiz.quizId === "1-capstone_q1"', 'quiz.quizId === "3-capstone_q1"')
    modified = modified.replace('quiz.quizId === "1-capstone_q2"', 'quiz.quizId === "3-capstone_q2"')
    modified = modified.replace('quiz.quizId === "1-capstone_q3"', 'quiz.quizId === "3-capstone_q3"')
    
    print("Original:")
    print("```")
    print(original)
    print("```\n")
    
    print("Modified:")
    print("```")
    print(modified)
    print("```\n")

# 2. Generate fix for the MCQ Part B Answers default text issue in line 3308
mcq_part_b_line = 3307  # Line is 0-indexed in the array
print(f"## Fix for line {mcq_part_b_line+1}")

# Extract the line to modify
original_line = lines[mcq_part_b_line]
modified_line = original_line.replace('"MCQ Part B Answers") : "Answers PDF"', '"Answers PDF") : "Answers PDF"')

print("Original:")
print("```")
print(original_line)
print("```\n")

print("Modified:")
print("```")
print(modified_line)
print("```\n")

print("# COMPLETE EDIT INSTRUCTIONS")
print("\nTo update the file, you should make an edit_file call with the following parameters:")
print("- target_file: index.html")
print("- instructions: Update Unit 1 capstone references to Unit 3, and fix the default capstone answer text.")
print("- code_edit: Update each of the sections as shown above.") 