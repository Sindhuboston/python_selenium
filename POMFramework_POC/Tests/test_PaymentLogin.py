import time
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Utilities.utils import Utils

class Test_Payment(BaseTest):
    log=Utils.log_to_file_output()

    def test_payment_alert(self):
        self.loginpage = LoginPage(self.driver)
        self.homepage=self.loginpage.do_pay_my_loan()
        self.paymentpage = self.homepage.do_make_a_payment()
        time.sleep(3)
        flag = self.paymentpage.do_signin_for_payment_alert()
        assert flag