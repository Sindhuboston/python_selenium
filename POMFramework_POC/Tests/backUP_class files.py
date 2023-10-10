from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver



"""
--------------- test_PaymentLogin.py file ---------------
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


"""
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.quit()

def pytest_configure(config):
    # Get today's date
    today = datetime.now()
    # Define the location for the reports
    #report_dir = Path("Reports", today.strftime("%Y%m%d"))
   # report_dir = Path("Reports", f"Report_On_{today.strftime('%Y%m%d%H%M')}")
    timestamp=today.strftime(('%m-%d-%Y %I-%M-%S %p'))
    report_dir = Path("Reports", f"Report_On_{timestamp}")
    report_dir.mkdir(parents=True, exist_ok=True)
    # Create an HTML file:
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "POC Test Report"
