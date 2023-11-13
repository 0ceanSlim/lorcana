import os
import subprocess
import sys

def check_python_installation():
    try:
        python_version = subprocess.check_output(
            ["python", "--version"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print(f"{python_version}")
        return True
    except FileNotFoundError:
        return False

def install_python():
    print("Python is not installed. Please download and install it from:")
    print("https://www.python.org/downloads/")
    input("Press Enter to continue after installing Python...")
    sys.exit(1)

def run_scripts_in_folder(folder_path):
    if not check_python_installation():
        install_python()

    # Get a list of all files in the folder
    script_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    if not script_files:
        print(f"No Python scripts found in {folder_path}")
        return

    for script_file in script_files:
        script_path = os.path.join(folder_path, script_file)

        # Run the script using subprocess
        try:
            subprocess.run(['python', script_path], check=True)
            print(f"Script {script_file} executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing script {script_file}: {e}")

if __name__ == "__main__":
    # Specify the folder containing the scripts
    scripts_folder = "src"

    run_scripts_in_folder(scripts_folder)

    print("Done.")
