# task1_student_marks.py

# Step 1: Create a dictionary
student_marks = {
    "Karthik": 85,
    "Ram": 90,
    "Jai": 78,
    "Ayush": 92
}


name = input("Enter the student name: ")

# Step 3 & 4: Retrieve marks or show message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the record.")
