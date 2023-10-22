import time
import pytest
from Config.config import TestData
from Tests.BaseTest import BaseTest
from Utilities.utils import Utils
from Pages.LoginSkillBoardPage import LoginSkillBoardPage

# This class, 'Test_LoginSkillBoard', is a test suite designed to verify the functionality of the SkillBoard signup process.
# It inherits setup and teardown methods from the 'BaseTest' class for test environment setup and cleanup.
# The class contains test cases for signing up on SkillBoard and verifying various validation criteria during the signup process.

# Test cases included in this class:
# 1. 'test_signup_on_skillboard': This test case performs a SkillBoard signup and verifies various password validation criteria,
#    such as uppercase, lowercase, numbers, special characters, and total character count.
# 2. 'test_verify_verification_code_display': (Currently commented out) This test case aims to verify the display of a verification code during signup.

# Note: Assertions and logging are used to capture and report the test results.

class Test_LoginSkillBoard(BaseTest):
    log = Utils.log_to_file_output()

    # Attempt to set the Excel file path and handle exceptions if the file is not found.
    try:
        TestData.set_excel_file_path(TestData.TD_SkillBoard_Workbook)
        TestData.set_sheet_name(TestData.TD_SkillBoard_Sheet)

    except FileNotFoundError:
        raise Exception("The specified Excel file cannot be located.")

    def test_signup_on_skillboard(self):
        #It will search for the test case name and return the data based on the specified column.
        TestData.set_testcase_name("test_signup_on_skillboard")


        self.pgSBLogin = LoginSkillBoardPage(self.driver)
        firstname = Utils.get_data("firstname")
        lastname = Utils.get_data("lastname")
        username = Utils.get_data("username")
        user_email = Utils.get_data("email")
        password = Utils.get_data("password")

        # Check for empty values and raise an exception if any of them are empty.
        if not firstname or not lastname or not username or not user_email or not password:
            raise ValueError("Some data fields are empty. Please check your test data source.")

        validation_results = self.pgSBLogin.do_signup_on_skillboard(firstname, lastname, username, user_email, password)
        self.log.info(f"\n\n********** Password '{password}' validations start **********\n")
        # Use a list to store any assertion errors:
        assertion_errors = []


        try:
            assert validation_results["upper_case"] is True
            self.log.info("---------- Uppercase exists in new password")
        except AssertionError as e:
            self.driver.save_screenshot(".\\Reports\\" + "upper_case.png")
            self.log.error("---------- Uppercase validation failed: " + str(e))
            assertion_errors.append("Uppercase validation")


        try:
            assert validation_results["lower_case"] is True
            self.log.info("---------- Lowercase exists in new password")
        except AssertionError as e:
            self.driver.save_screenshot(".\\Reports\\" + "lower_case.png")
            self.log.error("---------- Lowercase validation failed: " + str(e))
            assertion_errors.append("Lowercase validation")

        try:
            assert validation_results["number"] is True
            self.log.info("---------- Number exists in new password")
        except AssertionError as e:
            self.driver.save_screenshot(".\\Reports\\" + "number.png")
            self.log.error("---------- Number validation failed: " + str(e))

        try:
            assert validation_results["special_char"] is True
            self.log.info("---------- Special character exists in new password")
        except AssertionError as e:
            #self.driver.save_screenshot(".\\Reports\\" + "special_char.png")
            self.log.error("---------- Special character validation failed: " + str(e))

        try:
            assert validation_results["total_chars"] is True
            self.log.info("---------- expected # of characters exists in new password")
        except AssertionError as e:
            self.driver.save_screenshot(".\\Reports\\" + "total_chars.png")
            self.log.error("---------- Total characters validation failed: " + str(e))


        if assertion_errors:
                #Handle the assertion errors as needed, you can raise an exception here if necessary
            self.log.error("---------- Some validation errors occurred.")
            raise AssertionError("Assertion errors: " + ", ".join(assertion_errors))
        else:
            # If no assertion errors occurred, close the browser
            self.log.info("---------- No validation errors, closing the browser.")
            #self.driver.close()

    def test_successful_login_to_skillboard(self):
        TestData.set_testcase_name("test_successful_login_to_skillboard")
        self.pgSBLogin = LoginSkillBoardPage(self.driver)

        username = Utils.get_data("username")
        password = Utils.get_data("password")
        self.pgSBLogin.do_login_into_skillboard(username, password)
