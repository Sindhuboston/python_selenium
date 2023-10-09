from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Utilities.logs import Logs


class BT_LoginPage(BasePage):
    log = Logs.log_to_file_output()

    BT_LOGIN_BUTTON = (By.XPATH, '//span[@class="login"]')
    BT_SIGNIN_BUTTON = (By.XPATH, '//a[contains(text(),"Sign In") and @class="bt-nav-sign-link"]')
    USERNAME = (By.XPATH, "//input[@name='username' and @placeholder='Username']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get(TestData.BT_URL)
        self.driver.maximize_window()
        print("URL: " + TestData.BT_URL)
        self.log.info("URL: "+TestData.BT_URL)

    def do_on_login_button(self):
        self.do_click(self.BT_LOGIN_BUTTON)

    def do_signin_options(self):
        self.loginPg = BT_LoginPage(self.driver)
        self.loginPg.do_hover_on_element(self.BT_LOGIN_BUTTON)
        self.loginPg.do_click(self.BT_SIGNIN_BUTTON)