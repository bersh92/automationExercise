import subprocess
import sys
import os
import shutil

# Windows example: r'C:\Users\YOUR_USERNAME\allure-2.27.0\allure-2.27.0\bin\allure.bat'
ALLURE_COMMAND_PATH = 'allure'

def clear_directory(directory):
    """Clears the specified directory by removing it if it exists, then recreating it."""
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def open_allure_report():
    # Ensure the allure-report directory exists
    report_dir = "allure-report"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    # Serve the Allure report from the allure-results directory
    subprocess.call([ALLURE_COMMAND_PATH, 'serve', 'allure-results'])

def generate_allure_report():
    # Define the base directory for reports relative to this script's location
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    report_dir = os.path.join(base_dir, "allure-report")
    # Generate the Allure report from the allure-results directory
    subprocess.call([ALLURE_COMMAND_PATH, 'generate', results_dir, '-o', report_dir, '--clean'])

def run_tests_and_generate_report(headless=False):
    # Define the base directory for reports relative to this script's location
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    # Clear the allure-results directory to ensure fresh start
    clear_directory(results_dir)
    # Ensure the allure-report directory is cleared and ready for new report
    clear_directory(os.path.join(base_dir, "allure-report"))
    # Determine headless mode
    pytest_cmd = ['pytest', f'--alluredir={results_dir}']
    if headless:
        pytest_cmd.extend(['--headless'])
    # Run pytest with or without headless mode based on the headless argument
    subprocess.call(pytest_cmd)
    # Automatically generate the Allure report after tests have completed
    generate_allure_report()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'openReport':
            open_allure_report()
        elif command == 'testHeadless':
            run_tests_and_generate_report(headless=True)
        elif command == 'testNormal':
            run_tests_and_generate_report(headless=False)
        else:
            print(f"Unknown command: {command}")
    else:
        print("No command provided.")