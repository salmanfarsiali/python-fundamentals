
# ==========================================
# Python Basics Assignment Part - 2
# ==========================================


# Question 1: Loop Basics (for loop)
# Write a Python program that uses a for loop to print numbers from 1 to 10.

print("Question 1: Loop Basics")

for number in range(1, 11):
    print(number)


# ==========================================
# Question 2: Loop with Condition
# Using a for loop, print only the even numbers between 1 and 20.

print("\nQuestion 2: Even Numbers")

for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# ==========================================
# Question 3: String Manipulation
# Take a string input from the user and:
# 1. Print the string in uppercase
# 2. Print the length of the string
# 3. Print the string reversed

print("\nQuestion 3: String Manipulation")

text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Length:", len(text))
print("Reversed:", text[::-1])


# ==========================================
# Question 4: String Processing with Loop
# Take a string from the user and count how many vowels (a, e, i, o, u) are in the string.

print("\nQuestion 4: Count Vowels")

text = input("Enter a string: ")

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
