from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
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


def pytest_html_report_title(report):
    report.title = "POC Test Report"
