import time

from selenium.webdriver.common.by import By
from Config.config import TestData
from Utilities.utils import Utils
from Pages.BasePage import BasePage


class PaymentPage(BasePage):
    log = Utils.log_to_file_output()
    """
    MEMBER_NUMBER_TEXTBOX = (By.ID, "membernumber")
    LOAN_NUMBER_TEXTBOX = (By.ID, "customernumber")
    SSN_LAST_DIGITS_TEXTBOX = (By.ID, "sp_lastfour")
    PROFILE_SETUP_RADIOBT = (By.ID, "quickCreateProfile")
    PROFILE_LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-primary login')]")
    ALERT_DISPLAY = (By.CSS_SELECTOR, "div.alert.alert-danger")  # //div[@class='alert alert-danger']
    """
    MEMBER_NUMBER_TEXTBOX = (By.XPATH, "//input[@id='membernumber']")
    LOAN_NUMBER_TEXTBOX = (By.XPATH, "//input[@id='customernumber']")
    SSN_LAST_DIGITS_TEXTBOX = (By.XPATH, "//input[@id='sp_lastfour']")
    PROFILE_SETUP_RADIOBT = (By.XPATH, "//input[@id='quickCreateProfile']")
    PROFILE_LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-primary login')]")
    ALERT_DISPLAY = (By.XPATH, "//div[@class='alert alert-danger']")


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def do_signin_for_payment_alert(self):
       # self.take_screenshot("landing_pg_for_Payment_SigIn")
        time.sleep(2)
        self.do_send_text(self.MEMBER_NUMBER_TEXTBOX, TestData.MEMBER_NUMBER)
        self.do_send_text(self.LOAN_NUMBER_TEXTBOX, TestData.LOAN_NUMBER)
        self.do_send_text(self.SSN_LAST_DIGITS_TEXTBOX, TestData.SSN_LAST_DIGITS)
        self.do_click(self.PROFILE_SETUP_RADIOBT)
        self.log.info("Member number entered: "+TestData.MEMBER_NUMBER)
        self.log.info("Loan number entered: " + TestData.LOAN_NUMBER)
        self.log.info("SSN last digits entered: " + TestData.SSN_LAST_DIGITS)
        return self.is_visible(self.ALERT_DISPLAY)
