import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from Utilities.utils import Utils

# The 'LoginSkillBoardPage' class defines the Page Object for the SkillBoard login and signup page.
# It encapsulates the page elements and provides methods for interacting with these elements.
# Page elements, identified by locators, are defined as class attributes for reuse in methods.
# The class includes a constructor to initialize the page and navigate to the SkillBoard URL.
# Logging is used to record actions and errors during page interactions for debugging and reporting.

class LoginSkillBoardPage(BasePage):

    SIGN_UP = (By.XPATH, "//button[contains(text(),'Sign up')]")
    FIRSTNAME = (By.ID, "firstName")
    LASTNAME = (By.ID, "lastName")
    USERNAME = (By.ID, "username")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    T_AND_C_AGREE_MSG = (By.XPATH, "//P[contains(text(),'you agree')]")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    CANCEL_SIGNUP = (By.XPATH, "//button[text()='Cancel']")

    SB_LOGO = (By.XPATH, "(//img[@src='/SkillBoardBadge.png'])[last()]")
    VERIFICATION_CODE_MSG = (By.XPATH, "//p[contains(text(),'enter the verification code received on your email.')]")
    CONFIRM_CODE_BUTTON = (By.XPATH, "//button[text()='Confirm Code']")

    PSW_UPPER_CASE = (By.XPATH, "//p[contains(text(),'upper case') and contains(@class,'green')]")
    PSW_LOWER_CASE = (By.XPATH, "//p[contains(text(),'lower case') and contains(@class,'green')]")
    PSW_NUMBER = (By.XPATH, "//p[contains(text(),'number') and contains(@class,'green')]")
    PSW_SPECIAL_CHAR = (By.XPATH, "//p[contains(text(),'special') and contains(@class,'green')]")
    PSW_TOTAL_CHARS = (By.XPATH, "//p[contains(text(),'8 char') and contains(@class,'green')]")

    SIGN_IN = (By.XPATH, "//button[text()='Sign in']")

    log = Utils().log_to_file_output()

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.driver.get(TestData.URL_SKILLBOARD)
        self.log.info(f"---------- URL: {TestData.URL_SKILLBOARD}")

    def do_check_signup_sblogo(self):
        try:
            self.do_click(self.SIGN_UP)
            self.is_visible(self.SB_LOGO)
        except Exception as e:
            print(f"some errors occurred in do_check_signup_sbLogo")

    def do_signup_on_skillboard(self, firstname, lastname, username, user_email, password):
        try:
            self.do_click(self.SIGN_UP)
            self.log.info("---------- Sign Up button is clicked on the website.")

            self.do_clear(self.FIRSTNAME)
            self.do_send_text(self.FIRSTNAME, firstname)
            self.do_clear(self.LASTNAME)
            self.do_send_text(self.LASTNAME, lastname)
            self.do_clear(self.USERNAME)
            self.do_send_text(self.USERNAME, username)
            self.do_clear(self.EMAIL)
            self.do_send_text(self.EMAIL, user_email)
            self.do_clear(self.PASSWORD)
            self.do_send_text(self.PASSWORD, password)
            self.log.info("---------- Signup details are entered.")

            # Perform multiple validations and log the results
            is_upper_case_visible = self.is_visible(self.PSW_UPPER_CASE)
            is_lower_case_visible = self.is_visible(self.PSW_LOWER_CASE)
            is_number_visible = self.is_visible(self.PSW_NUMBER)
            is_special_char_visible = self.is_visible(self.PSW_SPECIAL_CHAR)
            is_total_chars_visible = self.is_visible(self.PSW_TOTAL_CHARS)

            self.do_click(self.CANCEL_SIGNUP)
            self.log.info("---------- Cancel button in the pop-up window is clicked.")


            # You can return the validation results as needed, e.g., a dictionary or list.
            return {
                "upper_case": is_upper_case_visible,
                "lower_case": is_lower_case_visible,
                "number": is_number_visible,
                "special_char": is_special_char_visible,
                "total_chars": is_total_chars_visible
            }
        except Exception as e:
            self.log.error(f"---------- An error occurred in the do_signup_on_skillboard: {str(e)}")


    def do_login_into_skillboard(self, username, password):
        try:
            self.do_click(self.SIGN_IN)
            self.log.info("---------- Sign in button is clicked on the website.")
            self.do_clear(self.USERNAME)
            self.do_send_text(self.USERNAME, username)
            self.log.info(f"---------- username '{username}' is entered.")
            self.do_clear(self.PASSWORD)
            self.do_send_text(self.PASSWORD, password)
            self.log.info(f"---------- password '{password}' is entered.")
            self.do_click(self.SUBMIT)
            self.log.info(f"---------- Sign in button is clicked.")
            time.sleep(2)
            self.driver.save_screenshot(".\\Reports\\" + "Sign in.png")


        except Exception as e:
            self.log.error(f"---------- An error occurred in the do_login_into_skillboard(): {str(e)}")

    def get_home_page_title(self, title):
        self.log.info(f"---------- title of the Home page: " + self.get_title(title))
        return self.get_title(title)