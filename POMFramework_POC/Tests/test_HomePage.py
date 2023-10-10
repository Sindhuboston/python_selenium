import time

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Utilities.utils import Utils


class Test_HomePage(BaseTest):
    log = Utils.log_to_file_output()

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_pay_my_loan()
        title = homePage.get_home_page_title(TestData.PAY_MY_LOAN_TITLE)
        self.log.info(title)
        assert title == TestData.PAY_MY_LOAN_TITLE

    def test_make_a_payment_isvisible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_pay_my_loan()
        flag = homePage.check_make_a_payment_button_exist()
        self.log.info(flag)
        #homePage.take_screenshot("make_a_payment_screenshot")
        print("screenshot should be displayed here")
        assert flag

    def test_make_a_payment(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_pay_my_loan()
        print("This should click the Make a Payment button")
        time.sleep(2)
        homePage.do_make_a_payment()
        time.sleep(2)

