# Task 1: Given the lists:
# Filter out students who have grades below 80. Print the name, grade and activiy.

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
merged_list = list(zip(students, grades, activities))
filtered_list = [student for student in merged_list if student[1] >= 80]
print(filtered_list)

# Task 2: For the remaining students, add students name in a new list named

students_approved = [student[0] for student in filtered_list]

# Task 3: Print the students_approved list.
print(students_approved)
