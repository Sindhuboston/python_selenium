import pytest
from selenium import webdriver
import pytest_html


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)

            if file_name:
                # Corrected the HTML code to open the image in a new window
                html = ('<div><a href="{0}" target="_blank">'
                        '<img src="{0}" alt="screenshot" style="width:304px;height:228px;" />'
                        '</a></div>').format(file_name)

                extras.append(pytest_html.extras.html(html))
    report.extras = extras

def _capture_screenshot(driver, image_name):
    driver.get_screenshot_as_file(image_name)

def pytest_html_report_title(report):
    report.title = "Automation Report"
