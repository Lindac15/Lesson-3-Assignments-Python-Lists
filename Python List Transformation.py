# Task 1: Given the list of grades:
# Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)

# Task 2: Calculate the average grade and display it.

average = sum(grades) / len(grades)
print(average)

# Task 3: Replace any grade below 80 with the value Failed.

grades = ['Failed' if grade < 80 else grade for grade in grades]
print(grades)

