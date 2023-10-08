import time

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest

"""calls the BaseTest (parent) to get the web_driver"""


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.check_signup_link_exist()
        print(flag)
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        print(title)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_PayMyLoan_Button(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_pay_my_loan()
        print("Pay My Loan button should be clicked.")
        time.sleep(2)

    """
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(2)
    """