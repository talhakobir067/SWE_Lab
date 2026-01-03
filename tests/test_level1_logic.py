# tests/test_level1_logic.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from grade_calculator import GradeCalculator

class TestLevel1Logic(unittest.TestCase):

    def setUp(self):
        self.gc = GradeCalculator()

    def test_validate_marks(self):
        self.assertTrue(self.gc.validate_marks([80, 90, 70]))
        with self.assertRaises(ValueError):
            self.gc.validate_marks([-10, 90])

    def test_average(self):
        self.assertEqual(self.gc.calculate_average([80, 90]), 85)

    def test_gpa(self):
        self.assertEqual(self.gc.calculate_gpa([85, 90]), 4.0)
        self.assertEqual(self.gc.calculate_gpa([75, 70]), 3.5)

    def test_grade(self):
        self.assertEqual(self.gc.calculate_grade([90, 80]), "A+")
        self.assertEqual(self.gc.calculate_grade([72, 70]), "A")

if __name__ == "__main__":
    unittest.main()
