# Task 1: Given the two lists:
# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
new_list = [student for student in submitted if student in attended]
print(new_list)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]    
attended = ["Charlie", "Eve", "Alice", "Frank"] 
result = submitted == attended  
print(result)

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
merged_list = submitted + attended
for student in merged_list:
    if student not in submitted:
        attended.remove(student)    
print(attended)
