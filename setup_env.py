import os
import subprocess
import sys

def run_command(command, shell=True):
    """Run system command and handle errors."""
    result = subprocess.run(command, shell=shell)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

def main():
    # Step 1: Create a virtual environment
    print("Creating virtual environment...")
    run_command([sys.executable, "-m", "venv", "venv"])

    # Step 2: Install dependencies
    print("Installing pandas and openpyxl...")
    if os.name == 'nt':
        # Windows
        pip_install_command = "venv\\Scripts\\python.exe -m pip install --upgrade pip && venv\\Scripts\\python.exe -m pip install pandas openpyxl"
    else:
        # MacOS/Linux
        pip_install_command = "venv/bin/python -m pip install --upgrade pip && venv/bin/python -m pip install pandas openpyxl"
    
    run_command(pip_install_command, shell=True)

    print("Virtual environment set up and dependencies installed.")

if __name__ == "__main__":
    main()
