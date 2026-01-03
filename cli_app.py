# cli_app.py

from grade_calculator import GradeCalculator

def run_cli():
    gc = GradeCalculator()
    
    name = input("Enter student name: ")
    marks_input = input("Enter marks (comma separated): ")
    try:
        marks = [int(m.strip()) for m in marks_input.split(",")]
        gc.validate_marks(marks)
        gpa = gc.calculate_gpa(marks)
        grade = gc.calculate_grade(marks)
        
        print(f"\nStudent: {name}")
        print(f"GPA: {gpa}")
        print(f"Grade: {grade}")
    except Exception as e:
        print(f"Error: {e}")
