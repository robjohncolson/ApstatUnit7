import re

# Path to the file (read-only mode)
file_path = 'index.html'

try:
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all occurrences of quiz.quizId with capstone references
    unit1_references = re.findall(r'quiz\.quizId === \"1-capstone_q\d\"', content)
    unit3_references = re.findall(r'quiz\.quizId === \"3-capstone_q\d\"', content)
    unit7_references = re.findall(r'quiz\.quizId === \"7-capstone_q\d\"', content)
    
    print('Analysis of capstone button references:')
    print(f'Unit 1 capstone references: {len(unit1_references)}')
    print(f'Unit 3 capstone references: {len(unit3_references)}')
    print(f'Unit 7 capstone references: {len(unit7_references)}')
    print('\nAll Unit 1 references (these need to be updated):')
    for i, ref in enumerate(unit1_references):
        line_number = content[:content.find(ref)].count('\n') + 1
        print(f'{i+1}. Line {line_number}: {ref}')
    
    # Also find section where MCQ Part B Answers appears as default
    mcq_part_b_default = re.findall(r'\"MCQ Part B Answers\"\) : \"Answers PDF\"', content)
    print(f'\nDefault MCQ Part B Answer patterns to fix: {len(mcq_part_b_default)}')
    for i, ref in enumerate(mcq_part_b_default):
        line_number = content[:content.find(ref)].count('\n') + 1
        print(f'{i+1}. Line {line_number}: {ref}')
        
    # Extract the relevant sections for code editing
    relevant_sections = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'quiz.quizId === \"1-capstone_q' in line:
            section_start = max(0, i-5)
            section_end = min(len(lines), i+10)
            section = '\n'.join(lines[section_start:section_end])
            relevant_sections.append((i+1, section))
    
    print('\nRelevant code sections for editing:')
    for line_num, section in relevant_sections:
        print(f'\nAround line {line_num}:')
        print('-' * 50)
        print(section)
        print('-' * 50)
    
except Exception as e:
    print(f'Error analyzing file: {e}') 