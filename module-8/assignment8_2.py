'''
Marco Rodriguez Gomez
04/30/2026
CSD 325 Module 8 Assignment 2
This program reads a .json file containing a list of students, prints the list, appends a new student to the list, and then saves the updated list back to the .json file.
'''
# import the json module to work with JSON data
import json

# Define the filename of the JSON file to read and write
filename = 'Student.json'

# Define a function to print the list of students in a formatted way
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the file into a Python list
with open(filename, 'r') as f:
    students = json.load(f)

# Print the original list to the console
print("This is the original Student list:")
print_students(students)

# Append new data to the list
new_student = {
    "F_Name": "Marco",
    "L_Name": "Rodriguez",
    "Student_ID": 12345,
    "Email": "mrodriguez@example.com"
}
students.append(new_student)

# Print the updated list to the console
print("\nThis is the updated Student list:")
print_students(students)

# Use dump() to save the updated data back to the file
with open(filename, 'w') as f:
    json.dump(students, f, indent=4)

print("\nThe .json file was updated.")