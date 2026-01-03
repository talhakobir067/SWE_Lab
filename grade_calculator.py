# grade_calculator.py

class GradeCalculator:

    def validate_marks(self, marks):
        if not isinstance(marks, list):
            raise TypeError("Marks must be a list")

        for m in marks:
            if m < 0 or m > 100:
                raise ValueError("Each mark must be between 0 and 100")

        return True

    def calculate_average(self, marks):
        self.validate_marks(marks)
        return sum(marks) / len(marks)

    def calculate_gpa(self, marks):
        avg = self.calculate_average(marks)

        if avg >= 80: return 4.0
        if avg >= 70: return 3.5
        if avg >= 60: return 3.0
        if avg >= 50: return 2.5
        return 2.0

    def calculate_grade(self, marks):
        avg = self.calculate_average(marks)

        if avg >= 80: return "A+"
        if avg >= 70: return "A"
        if avg >= 60: return "B"
        if avg >= 50: return "C"
        if avg >= 40: return "D"
        return "F"
