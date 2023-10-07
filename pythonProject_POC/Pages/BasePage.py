import os
import allure
import pytest
import pytest_html
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
"""It contains all generic methods & utilities for all the pages"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """===== modified youtube code with chatgpt suggestion: ====="""
    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, call):
        pytest_html = self.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extras = getattr(report, "extras", [])

        if report.when == "call" or report.when == "setup":
            xfail = hasattr(report, "wasxfail")

            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                self._capture_screenshot(file_name)

                if file_name:
                    # Corrected the HTML code to open the image in a new window
                    html = ('<div><a href="{0}" target="_blank">'
                            '<img src="{0}" alt="screenshot" style="width:304px;height:228px;" />'
                            '</a></div>').format(file_name)

                    extras.append(pytest_html.extras.html(html))
                    print(extras)
        #report.extras = extras

    def _capture_screenshot(self, image_name):
        self.driver.get_screenshot_as_file(image_name)

    def pytest_html_reprot_title(self, report):
        report.title = "Automation Report"

    """===== 1.  https://youtu.be/MM6axmqAKWM?si=dMGNCDthimlNJAkj code: ====="""
    """
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
                    html = '<div><img src=%s alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick-window.open(this.src)" align="right"/></div>' %file_name
                    extras.append(pytest_html.extras.html(html))
            report.extras = extras


            # always add url to report
            extras.append(pytest_html.extras.url("http://www.example.com/"))

                # only add additional html on failure
                extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            report.extras = extras

    # this method will take a screenshot:
    def _capture_screenshot(self, image_name):
        self.driver.get_screenshot_as_file(image_name)

    # this method will give report name:
    def pytest_html_report_title(report):
        report.title = "My very own title!"
    """

    """================ 2.  Below is chatGPT code: ======================="""

    def pytest_runtest_makereport(self, item, call):
        report = super().pytest_runtest_makereport(item, call)

        if report.when == "call" and report.failed:
            # Capture a screenshot when the test fails
            screenshot_name = item.name + ".png"
            screenshot_path = os.path.join("Reports", screenshot_name)
            self.driver.save_screenshot(screenshot_path)

    def take_screenshot(self, report_name):
        report_folder = "Reports/"  # Specify the relative report folder path

        try:
            screenshot_path = os.path.join(report_folder, report_name + ".png")
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            print(f"Error taking screenshot: {str(e)}")

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        """Gets the title of the current page."""   """return self.driver.title"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
