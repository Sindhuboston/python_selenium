import os
import allure
import pytest
import pytest_html
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

"""This class is the parent of all pages"""
"""It contains all generic methods & utilities for all the pages"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def take_screenshot(self, report_name):
        report_folder = "Reports/"  # Specify the relative report folder path
        try:
            screenshot_path = os.path.join(report_folder, report_name + ".png")
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            print(f"Error taking screenshot: {str(e)}")
    def do_hover_on_element(self, by_locator):
        act_chains = ActionChains(self.driver)
        locator_strategy, locator_value = by_locator  # Unpack the tuple
        login_button_ele = self.driver.find_element(locator_strategy, locator_value)
        act_chains.move_to_element(login_button_ele).perform()
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    def do_send_text(self, by_locator, text):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
            element.send_keys(text)
        except Exception as e:
            print(f"Error sending text: '{text}' to element located by: {by_locator}\nError message: {str(e)}")
    def do_get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    def get_title(self, title):
        """Gets the title of the current page."""   """return self.driver.title"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
