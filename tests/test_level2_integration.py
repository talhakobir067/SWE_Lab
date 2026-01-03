# tests/test_level2_integration.py
import unittest
from student_manager import StudentManager
import sys
import os
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestLevel2Integration(unittest.TestCase):

    def setUp(self):
        self.sm = StudentManager()
        # Create a temporary JSON file for testing
        self.temp_file = os.path.join(os.path.dirname(__file__), "temp_student.json")
        sample_student = {
            "student": "Talha",      # match student_manager expectation
            "marks": [95, 90, 92]
        }
        with open(self.temp_file, "w") as f:
            json.dump(sample_student, f)

    def test_load_student(self):
        data = self.sm.load_student(self.temp_file)
        self.assertIn("marks", data)
        self.assertEqual(data["student"], "Talha")
        self.assertEqual(data["marks"], [95, 90, 92])

    def test_full_result(self):
        result = self.sm.calculate_student_result(self.temp_file)
        self.assertEqual(result["name"], "Talha")   # output uses "name"
        self.assertAlmostEqual(result["gpa"], 4.0)
        self.assertEqual(result["grade"], "A+")

    def tearDown(self):
        # Delete temporary file after test
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

if __name__ == "__main__":
    unittest.main()
