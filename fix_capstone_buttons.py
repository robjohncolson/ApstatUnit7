import re

# Path to the file
input_file = 'index.html'
output_file = 'index_updated.html'

# Read the original file
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# 1. Replace "1-capstone_q" with "3-capstone_q"
modified_content = content.replace('quiz.quizId === "1-capstone_q1"', 'quiz.quizId === "3-capstone_q1"')
modified_content = modified_content.replace('quiz.quizId === "1-capstone_q2"', 'quiz.quizId === "3-capstone_q2"')
modified_content = modified_content.replace('quiz.quizId === "1-capstone_q3"', 'quiz.quizId === "3-capstone_q3"')

# 2. Replace "MCQ Part B Answers") : "Answers PDF" with "Answers PDF") : "Answers PDF"
modified_content = modified_content.replace('"MCQ Part B Answers") : "Answers PDF"', '"Answers PDF") : "Answers PDF"')

# 3. Replace empty string fallback with "Questions PDF" in linkText
modified_content = modified_content.replace('quiz.quizId === "3-capstone_q3" ? "MCQ Part B Questions" :\n                               ""', 
                                           'quiz.quizId === "3-capstone_q3" ? "MCQ Part B Questions" :\n                               "Questions PDF"')

# Write the updated content to a new file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(modified_content)

print(f"Updated content written to {output_file}")
print("Please verify the changes and then rename the file to replace the original.") 