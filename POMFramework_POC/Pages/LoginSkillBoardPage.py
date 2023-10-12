from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from Utilities.utils import Utils


class LoginSkillBoardPage(BasePage):

    SIGN_UP = (By.XPATH, "//button[contains(text(),'Sign up')]")
    FIRSTNAME = (By.ID, "firstName")
    LASTNAME = (By.ID, "lastName")
    USERNAME = (By.ID, "username")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    T_AND_C_AGREE_MSG = (By.XPATH, "//P[contains(text(),'you agree')]")
    SUBMIT_SIGNUP = (By.XPATH, "//button[@type='submit']")
    SB_LOGO = (By.XPATH, "(//img[@src='/SkillBoardBadge.png'])[last()]")

    log = Utils().log_to_file_output()

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get(TestData.URL_SKILLBOARD)
        self.log.info("URL: "+ TestData.URL_SKILLBOARD)

    def do_check_signup_sblogo(self):
        self.do_click(self.SIGN_UP)
        self.is_visible(self.SB_LOGO)


    def do_login_skillboard(self, firstname, lastname, username):
        self.do_click(self.SIGN_UP)
        self.log.info("\n Sign Up button is clicked.")
        self.do_send_text(self.FIRSTNAME, firstname)
        self.do_send_text(self.LASTNAME, lastname)
        self.do_send_text(self.USERNAME, username)


    def do_check_message(self):
        self.is_visible(self.T_AND_C_AGREE_MSG)


