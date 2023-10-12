import time

from Config.config import TestData
from Tests.BaseTest import BaseTest
from Utilities.utils import Utils
from Pages.LoginSkillBoardPage import LoginSkillBoardPage


class Test_LoginSkillBoard(BaseTest):
    log = Utils.log_to_file_output()
    TestData.set_excel_file_path(TestData.TD_SkillBoard_Workbook)
    TestData.set_sheet_name(TestData.TD_SkillBoard_Sheet)

    def test_signup_on_skillboard(self):

        self.pgSBLogin = LoginSkillBoardPage(self.driver)
        firstname = Utils.get_data("firstname")
        lastname = Utils.get_data("lastname")
        username = Utils.get_data("username")
        user_email = Utils.get_data("email")
        password = Utils.get_data("password")

        validation_results = self.pgSBLogin.do_signup_on_skillboard(firstname, lastname, username, user_email, password)

        # Use a list to store any assertion errors:
        assertion_errors = []

        try:
            assert validation_results["upper_case"] is True
        except AssertionError as e:
            self.log.error("Uppercase validation failed: " + str(e))
            assertion_errors.append("Uppercase validation")

        try:
            assert validation_results["lower_case"] is True
        except AssertionError as e:
            self.log.error("Lowercase validation failed: " + str(e))
            assertion_errors.append("Lowercase validation")

        try:
            assert validation_results["number"] is True
        except AssertionError as e:
            self.log.error("Number validation failed: " + str(e))

        try:
            assert validation_results["special_char"] is True
        except AssertionError as e:
            self.log.info("Special character validation failed: " + str(e))

        try:
            assert validation_results["total_chars"] is True
        except AssertionError as e:
            self.log.error("Total characters validation failed: " + str(e))

        if assertion_errors:
                #Handle the assertion errors as needed, you can raise an exception here if necessary
            self.log.error("Some validation errors occurred.")
            raise AssertionError("Assertion errors: " + ", ".join(assertion_errors))

    def test_verify_verification_code_display(self):
        self.pgSBLogin = LoginSkillBoardPage()
        self.pgSBLogin.verify_verification_code_display()