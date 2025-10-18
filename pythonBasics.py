# =====================================================
# Python Basics
# =====================================================

#Hello World and Comments
print("Hello, World!")

# Single-line comment
"""
Multi-line comment explaining:
- What this file does
- Learning Python basics in steps
"""

message = "Lets learn Python Basics"
print(message)

# -----------------------------------------------------

# Variables and Data Types
name = "Nasir"
age = 28
height = 5.7
is_active = True

print(f"My name is {name}, I am {age} years old, height: {height}, active: {is_active}")
print(type(name), type(age), type(height), type(is_active))

# Type casting
age_str = str(age)
print("After type casting:", age_str, type(age_str))

# -----------------------------------------------------

# Strings
course = "Python Programming"
print(course.lower())
print(course.upper())
print(course.title())
print(course.count("o"))
print(course.find("Pro"))

# Slicing
print(course[0:6]) 
print(course[-11:])    

# f-Strings
print(f"Welcome to {course} course!")

# -----------------------------------------------------

# Numbers (Integers and Floats)
num1 = 10
num2 = 3
print(num1 + num2, num1 - num2, num1 * num2, num1 / num2, num1 // num2, num1 ** num2)
print(abs(-7))
print(round(3.14159, 2))

# Comparisons
print(num1 > num2, num1 == 10, num1 != num2)

# -----------------------------------------------------

# Lists, Tuples, Sets
courses = ['Math', 'Physics', 'Chemistry', 'CS']
print(courses)
courses.append('AI')
courses.insert(1, 'English')
print(courses)

# Remove items
courses.remove('Physics')
print(courses)

# Tuples (immutable)
tup = ('Red', 'Green', 'Blue')
print(tup)

# Sets (no duplicates, unordered)
course_set = {'Math', 'CS', 'AI', 'Math'}
print(course_set)

# -----------------------------------------------------

# Dictionaries
student = {'name': 'Nasir', 'age': 30, 'courses': ['Math', 'CS']}
print(student['name'])
print(student.get('phone', 'Not Found'))

student['phone'] = '12345'
print(student)

for key, value in student.items():
    print(key, value)

# -----------------------------------------------------

# Conditionals
language = "Python"
if language == "Python":
    print("You are learning Python!")
elif language == "Java":
    print("You are learning Java!")
else:
    print("Unknown language")

# -----------------------------------------------------

# Loops
nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n)

for i in range(5):
    print("Iteration:", i)

count = 0
while count < 3:
    print("Count:", count)
    count += 1

# -----------------------------------------------------

# Functions
def greet(name="User"):
    return f"Hello, {name}!"

print(greet("Nasir"))

def add(x, y):
    return x + y

print("Sum:", add(10, 5))

# -----------------------------------------------------


print("All basics covered successfully!")
