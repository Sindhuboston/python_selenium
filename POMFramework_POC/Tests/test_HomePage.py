import time

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Utilities.logs import Logs


class Test_HomePage(BaseTest):
    log = Logs.log_to_file_output()
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_pay_my_loan()
        title = homePage.get_home_page_title(TestData.PAY_MY_LOAN_TITLE)
        self.log.info(title)
        assert title == TestData.PAY_MY_LOAN_TITLE

    def test_make_a_payment_isvisible(self):
        #self.loginPage = LoginPage(self.driver)
        #homePage = self.loginPage.do_pay_my_loan()
        self.homePage = HomePage(self.driver)
        flag = self.homePage.check_make_a_payment_button_exist()
        self.log.info(flag)
        self.homePage.take_screenshot("make_a_payment_screenshot")
        self.log.info("take screenshot here")
        print("take screenshot here")
        assert flag

    def test_make_a_payment(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_pay_my_loan()
        print("This should click the Make a Payment button")
        homePage.do_make_a_payment()
        time.sleep(2)

    """
    def attach_screenshot(self, driver, screenshot_name):
        screenshot_name += ".png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)



    def test_insurance_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_pay_my_loan()
        flag = homePage.check_insurance_link_exist()
        assert flag
"""
