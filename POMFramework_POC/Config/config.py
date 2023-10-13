
# The 'TestData' class serves as a configuration and data storage class for test-related constants and paths.
# It centralizes various parameters, including browser driver paths, URLs, and excel file paths for test data.

class TestData:
    CHROME_EXECUTABLE_PATH = 'C:/Program Files/Drivers/chromedriver.exe'
    FIREFOX_EXECUTABLE_PATH = 'C:/Program Files/Drivers/geckodriver.exe'

    LOGIN_PAGE_TITLE = "Auto Loans | DCU"
    PAY_MY_LOAN_TITLE = "Loan Payments | DCU"


    # Paths for test data files are provided:

    BASE_URL = "https://www.dcu.org/borrow/vehicle-loans/auto-loans.html"
    TD_DCU_Workbook = "C:\\Users\\sindh\\PycharmProjects\\POMFramework_POC\\TestData\\TDexcel.xlsx"
    TD_DCU_Sheet = "Sheet1"

    URL_SKILLBOARD = "https://skillboard.org/"
    TD_SkillBoard_Workbook = "C:\\Users\\sindh\\PycharmProjects\\POMFramework_POC\\TestData\\TDexcel_SkillBoard.xlsx"
    TD_SkillBoard_Sheet = "Sheet1"


    # The class also includes class methods for setting the Excel file path and sheet name dynamically.
    EXCEL_FILE_PATH = None
    SHEET_NAME = None

    @classmethod
    def set_excel_file_path(cls, file_path):
        cls.EXCEL_FILE_PATH = file_path

    @classmethod
    def set_sheet_name(cls, sheet_name):
        cls.SHEET_NAME = sheet_name