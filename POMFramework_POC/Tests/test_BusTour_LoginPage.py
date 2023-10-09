import time

from selenium.webdriver import ActionChains

from Pages.BusTour_LoginPage import BT_LoginPage
from Tests.BaseTest import BaseTest
from Utilities.logs import Logs


class Test_BT_LoginPage(BaseTest):
    log = Logs.log_to_file_output()

    def test_signin(self):
        self.loginPg = BT_LoginPage(self.driver)
        self.loginPg.do_signin_options
        time.sleep(5)

    """
     def test_do_login(self):
        self.loginPg = BT_LoginPage(self.driver)
        self.loginPg.click_on_login_button()
        self.log.info("Click on Login button to open login pop-up window.")
    """