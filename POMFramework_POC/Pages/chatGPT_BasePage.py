from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """This class is the parent of all pages.
    It contains all generic methods & utilities for all the pages.
    """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        """Clicks an element located by the provided locator."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_text(self, by_locator, text):
        """Enters text into an element located by the provided locator."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_get_element_text(self, by_locator):
        """Gets the text of an element located by the provided locator."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        """Checks if an element located by the provided locator is visible.
        Returns the element itself if visible, None otherwise.
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator), None)

    def get_title(self):
        """Gets the title of the current page."""
        return self.driver.title
