# # CONCEPTS COVERED IN THIS PROGRAM
# Advanced Looping Techniques
# Functions and Scope
# Lambda, map, filter, reduce
# List, Set, and Dictionary Comprehensions
# Advanced Data Structures
# Modules and Packages
# File Handling
# Sophisticated Exception Handling
# Decorators
# Generators

# Create a Python program that simulates a "Student Grades Management System" for a class.
# Decorator to log when the report is generated
def log_report(func):
    def wrapper(*args, **kwargs):
        print("Report generated.")
        func(*args, **kwargs)
    return wrapper

# Function to validate and get grade input
def get_grade_input():
    while True:
        try:
            grade = float(input("Enter grade (0-100): "))
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            return grade
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Function to get student details and store them
def get_student_data():
    students = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        grade = get_grade_input()
        students[name] = grade
    return students

# Function to calculate average grade using lambda and map
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

# Function to generate the student report
@log_report
def generate_report(students):
    # Dictionary comprehension for average calculation
    student_avg = {name: calculate_average([grade]) for name, grade in students.items()}

    # List comprehension to create the report sorted by average grade
    report = sorted([(name, student_avg[name]) for name in student_avg], key=lambda x: x[1], reverse=True)
    
    # File Handling: Save the report to a file
    with open("student_report.txt", "w") as file:
        file.write("Student Grades Report\n")
        file.write("====================================\n")
        for name, avg in report:
            file.write(f"{name}: {avg:.2f}\n")
    
    # Print the report
    print("\nStudent Grades Report (Sorted by Average Grade):")
    for name, avg in report:
        print(f"{name}: {avg:.2f}")
    
    return report

# Main program execution
if __name__ == "__main__":
    students = get_student_data()
    generate_report(students)
