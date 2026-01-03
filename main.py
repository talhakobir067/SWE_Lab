# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cli_app import run_cli

def main():
    print("=== Welcome to the Student Grade Calculator ===\n")
    run_cli()  # This runs the CLI interface

if __name__ == "__main__":
    main()
