# student_manager.py
import json
from grade_calculator import GradeCalculator

class StudentManager:

    def __init__(self):
        self.gc = GradeCalculator()

    def load_student(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return data

    def calculate_student_result(self, filename):
        data = self.load_student(filename)
        marks = data["marks"]
        gpa = self.gc.calculate_gpa(marks)
        grade = self.gc.calculate_grade(marks)

        return {
            "name": data["student"],
            "marks": marks,
            "gpa": gpa,
            "grade": grade
        }
