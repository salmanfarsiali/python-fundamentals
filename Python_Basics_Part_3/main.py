
# ==========================================
# Python Basics Part - 3
# Advanced Loops & Data Structures
# ==========================================


# Question 1: Enumerate with List
# Given the list:
# fruits = ["apple", "banana", "cherry", "mango"]
# Use enumerate() to print each fruit with its index number.
# Output format example:
# 0 apple  
# 1 banana  
# 2 cherry  
# 3 mango

print("Question 1: Enumerate with List")

fruits = ["apple", "banana", "cherry", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ==========================================
# Question 2: Zip with Two Lists
# Given two lists:
# students = ["Rahim", "Karim", "Ayesha"]
# scores = [85, 90, 78]
# Use zip() to print each student name along with their score.
# Example Output:
# Rahim scored 85
# Karim scored 90
# Ayesha scored 78

print("\nQuestion 2: Zip with Two Lists")

students = ["Rahim", "Karim", "Ayesha"]
scores = [85, 90, 78]

for student, score in zip(students, scores):
    print(f"{student} scored {score}")


# ==========================================
# Question 3: Tuple and Loop
##Question 3: Tuple and Loop
# Create a tuple of 5 subjects.
# Using a for loop, print each subject one by one.

print("\nQuestion 3: Tuple and Loop")

subjects = ("Math", "English", "Physics", "Chemistry", "Biology")

for subject in subjects:
    print(subject)


# ==========================================
# Question 4: Set Operations
# Given the sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7}
# Print the common elements using set operation
# Print the unique elements of set1

print("\nQuestion 4: Set Operations")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Common elements (Intersection)
print("Common elements:", set1 & set2)

# Unique elements of set1 (Difference)
print("Unique elements of set1:", set1 - set2)
