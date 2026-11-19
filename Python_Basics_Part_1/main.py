
# ==========================================
# Python Basics Part-1
# ==========================================


# Question 1: Basic Print
# Python program that prints the following text exactly:
# Welcome to Python Programming!
# I am learning the basics.

print("Question 1: Basic Print")
print("Welcome to Python Programming!")
print("I am learning the basics.")


# ==========================================
# Question 2: Print with Variables
# Create two variables:
# name → your name
# age → your age
# Print the output like this:
# My name is Tahmid and I am 25 years old.


print("\nQuestion 2: Print with Variables")

name = "Tahmid"
age = 25

print(f"My name is {name} and I am {age} years old.")


# ==========================================
# Question 3: User Input
# Take user input for:
# Name
# Favorite programming language
# Print a message:
# Hello , your favorite language is.


print("\nQuestion 3: User Input")

user_name = input("Enter your name: ")
language = input("Enter your favorite programming language: ")

print(f"Hello {user_name}, your favorite language is {language}.")


# ==========================================
# Question 4: Type Casting (String to Integer)
# 1. Take two numbers from the user using input()
# 2. Convert them to integer
# 3. Print their sum
# Example output:
# The sum is: 30

print("\nQuestion 4: Type Casting")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

print("The sum is:", total)


# ==========================================
# Question 5: Simple Calculator
# Take two numbers from the user and:
# - Convert them to integers
# - Print Addition
# - Print Subtraction
# - Print Multiplication
# Example:
# Addition: 20
# Subtraction: 10
# Multiplication: 75

print("\nQuestion 5: Simple Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("-" * 25)
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print("-" * 25)
