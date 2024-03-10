import os
import pytest
import allure
from allure_commons.types import AttachmentType
from fixture.application import Application# Adjust the import as necessary for your project structure
import subprocess

# Define the base directory for reports relative to this file's location
base_dir = os.path.abspath(os.path.dirname(__file__))
results_dir = os.path.join(base_dir, "allure-results")
report_dir = os.path.join(base_dir, "allure-report")

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")
    parser.addoption("--allure-report", action="store_true", help="Generate Allure report after tests")

@pytest.fixture(scope="function")
def app(request):
    headless = request.config.getoption("--headless")
    fixture = Application(headless=headless)  # Ensure your Application class supports headless mode
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to take screenshots on test failure."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "app" in item.fixturenames:
            app = item.funcargs["app"]
            take_screenshot(app, report.nodeid)

def take_screenshot(app, nodeid):
    """Take a screenshot using the app's WebDriver and attach it to the Allure report."""
    screenshot_directory = os.path.join(base_dir, "allure-results", "screenshots")
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)
    # Normalize nodeid to create a valid filename
    filename = nodeid.replace("::", "_").replace("/", "_") + ".png"
    screenshot_file_path = os.path.join(screenshot_directory, filename)
    app.wd.save_screenshot(screenshot_file_path)
    if os.path.exists(screenshot_file_path):
        allure.attach.file(screenshot_file_path, name="Screenshot on failure", attachment_type=AttachmentType.PNG)
    else:
        print(f"Failed to capture screenshot: {screenshot_file_path}")

def pytest_sessionfinish(session, exitstatus):
    """Generate Allure report at the end of the test session if --allure-report was specified."""
    if session.config.getoption("--allure-report"):
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        subprocess.call(['allure', 'generate', results_dir, '-o', report_dir, '--clean'])
