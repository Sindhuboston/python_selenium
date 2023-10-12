import time

from Config.config import TestData
from Tests.BaseTest import BaseTest
from Utilities.utils import Utils
from Pages.LoginSkillBoardPage import LoginSkillBoardPage


class Test_LoginSkillBoard(BaseTest):
    log = Utils.log_to_file_output()
    TestData.set_excel_file_path(TestData.TD_SkillBoard_Workbook)
    TestData.set_sheet_name(TestData.TD_SkillBoard_Sheet)

    def test_SignUp_skillboard(self):
        self.pgSBLogin = LoginSkillBoardPage(self.driver)
        firstname = Utils.get_data("firstname")
        lastname = Utils.get_data("lastname")
        username = Utils.get_data("username")
        self.pgSBLogin.do_login_skillboard(firstname, lastname, username)
        time.sleep(5)