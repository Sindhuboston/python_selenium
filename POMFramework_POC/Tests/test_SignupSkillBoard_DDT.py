from Config.config import TestData
from Pages.LoginSkillBoardPage import LoginSkillBoardPage
from Tests.BaseTest import BaseTest
from Utilities.utils import Utils


class Test_SignSB_DDT(BaseTest):
    log = Utils.log_to_file_output()
    TestData.set_excel_file_path(TestData.TD_SkillBoard_Workbook)
    TestData.set_sheet_name(TestData.TD_SkillBoard_Sheet)

    def test_ddt_on_SB_signup(self):
        self.lgSBpg = LoginSkillBoardPage(self.driver)
        test_data = Utils.get_ddt()
        for data in test_data:
            test_case_name = data['TestCase']
            firstname = data['firstname']
            lastname = data['lastname']
            username = data['username']
            email = data['email']
            password = data['password']

            validation_results = self.lgSBpg.do_signup_on_skillboard(firstname, lastname, username, email, password)
            self.log.info(f"\n\n********** Password '{password}' validations start **********\n")
            # Use a list to store any assertion errors:
            assertion_errors = []

            try:
                assert validation_results["upper_case"] is True
                self.log.info("---------- Uppercase exists in new password")
            except AssertionError as e:
                self.log.error("---------- Uppercase validation failed: " + str(e))
                assertion_errors.append("Uppercase validation")
                self.driver.save_screenshot(".\\Reports\\" + "upper_case.png")

            try:
                assert validation_results["lower_case"] is True
                self.log.info("---------- Lowercase exists in new password")
            except AssertionError as e:
                self.log.error("---------- Lowercase validation failed: " + str(e))
                assertion_errors.append("Lowercase validation")
                self.driver.save_screenshot(".\\Reports\\" + "lower_case.png")

            try:
                assert validation_results["number"] is True
                self.log.info("---------- Number exists in new password")
            except AssertionError as e:
                self.log.error("---------- Number validation failed: " + str(e))
                self.driver.save_screenshot(".\\Reports\\" + "number.png")

            try:
                assert validation_results["special_char"] is True
                self.log.info("---------- Special character exists in new password")
            except AssertionError as e:
                self.driver.save_screenshot(".\\Reports\\" + "special_char.png")
                self.log.error("---------- Special character validation failed: " + str(e))

            try:
                assert validation_results["total_chars"] is True
                self.log.info("---------- expected # of characters exists in new password")
            except AssertionError as e:
                self.log.error("---------- Total characters validation failed: " + str(e))
                self.driver.save_screenshot(".\\Reports\\" + "total_chars.png")

            if assertion_errors:
                # Handle the assertion errors as needed, you can raise an exception here if necessary
                self.log.error("Some validation errors occurred.")
                raise AssertionError("Assertion errors: " + ", ".join(assertion_errors))
            