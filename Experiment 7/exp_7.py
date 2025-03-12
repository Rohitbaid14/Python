students = {}

# Function to add a student
def add_student(roll, name, grade, attendance):
    students[roll] = {"name": name, "grade": grade, "attendance": attendance}
    print(" student is added:", name)

# Function to update grades
def update_grade(roll, new_grade):
    if roll in students:
        students[roll]["grade"] = new_grade
        print("Grade updated for roll number:", roll)
    else:
        print("Student is not found")

# Function to update attendance
def update_attendance(roll, new_attendance):
    if roll in students:
        students[roll]["attendance"] = new_attendance
        print("Attendance updated for roll number:", roll)
    else:
        print("Student is not found")

# Function to show all student records
def show_students():
    if not students:
        print("No student records is available")
    else:
        for roll, info in students.items():
            print("Roll:", roll, "Name:", info["name"], "Grade:", info["grade"], "Attendance:", info["attendance"])

# Adding some students
add_student(101, "Amit", "A", 90)
add_student(102, "Priya", "B", 85)

# Show all students
show_students()

# Update grade for roll 101
update_grade(101, "A+")

# Update attendance for roll 102
update_attendance(102, 92)

# Show all students again
show_students()

