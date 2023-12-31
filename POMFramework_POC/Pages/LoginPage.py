import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Utilities.utils import Utils

class LoginPage(BasePage):
    log = Utils.log_to_file_output()

    USERNAME = (By.XPATH, "//input[@class='form-control memberNumber']")
    PASSWORD = (By.XPATH, "//input[@class='form-control' and @name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    PAY_MY_LOAN_LINK = (By.LINK_TEXT, "PAY MY LOAN")
    SIGNUP_LINK = (By.LINK_TEXT, "Forgot Username/Password?")

    """Get the driver instance whenever LoginPage is called."""
    """driver FROM: test_loginPage < BaseTest < fixtures(conftest.py) ."""
    """driver TO:  this class & also the super class(BasePage) """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        print("URL: "+TestData.BASE_URL)

    """This is used to get the page title"""
    def get_login_page_title(self, title):
        self.log.info("title = " + title)
        return self.get_title(title)


    """This is used to check SignUp link"""

    def check_signup_link_exist(self):
        is_visible = self.is_visible(self.SIGNUP_LINK)
        self.log.info("SignUp link is visible: " + str(is_visible))
        return self.is_visible(self.SIGNUP_LINK)

    """This is used to log into app"""
    def do_login(self, username, password):
        self.do_send_text(self.USERNAME, username)
        self.do_send_text(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.LOGIN_BUTTON)

    def do_pay_my_loan(self):
        self.do_click(self.PAY_MY_LOAN_LINK)
        self.log.info("button, Pay My Loan button should be clicked")
        self.log.info("Home Page should be opened.")
        return HomePage(self.driver)