# tests/test_level3_cli.py
import unittest
from unittest.mock import patch
import io
from cli_app import run_cli
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestLevel3CLI(unittest.TestCase):

    @patch("builtins.input", side_effect=["Talha", "85,90,80"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cli_output(self, mock_stdout, mock_input):
        run_cli()
        output = mock_stdout.getvalue()
        self.assertIn("Talha", output)
        self.assertIn("GPA:", output)
        self.assertIn("Grade:", output)

if __name__ == "__main__":
    unittest.main()
