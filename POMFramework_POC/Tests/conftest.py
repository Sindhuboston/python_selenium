from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Utilities.utils import Utils


# This file contains configuration settings and fixtures for a Pytest-based automated testing framework.
# It is responsible for initializing web drivers, configuring report generation, and defining test-related configurations.

@pytest.fixture(params=["chrome", "edge"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")  # Adjust the size as needed
        web_driver = webdriver.Chrome()
        Utils.log_to_file_output().info("---------- Launching Chrome browser ---------- ")
    elif request.param == "edge":
        web_driver = webdriver.Edge()
        Utils.log_to_file_output().info("---------- Launching Edge browser ---------- ")
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
        Utils.log_to_file_output().info("---------- Launching Firefox browser ---------- ")
    request.cls.driver = web_driver
    yield
    web_driver.quit()


def pytest_configure(config):
    # Get today's date
    today = datetime.now()

    # Define the location for the reports
    timestamp = today.strftime('%m-%d-%Y %I-%M-%S %p')
    report_dir = Path("Reports", f"Report_On_{timestamp}")
    report_dir.mkdir(parents=True, exist_ok=True)

    # Create an HTML file:
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

    # # Add custom metadata to the report
    # config._metadata['Product Name'] = 'Skill Board'
    # config._metadata['Module'] = 'Smoke Test'

    # Get the Python version and add it to metadata
    # python_version = sys.version.split('\n')[0]
    # config._metadata['Python'] = python_version


def pytest_html_report_title(report):
    report.title = "POC Test Report"

# def pytest_html_results_table_row(report, cells):
#     if 'failed' in cells[-1]:
#         if 'validation_error' in cells[-2]:
#             cells[0] = '<b>Validation Error</b>'
#         else:
#             cells[0] = '<b>Failed</b>'
