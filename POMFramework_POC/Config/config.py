class TestData:
    CHROME_EXECUTABLE_PATH = 'C:/Program Files/Drivers/chromedriver.exe'
    FIREFOX_EXECUTABLE_PATH = 'C:/Program Files/Drivers/geckodriver.exe'

    BASE_URL = "https://www.dcu.org/borrow/vehicle-loans/auto-loans.html"
    USER_NAME = "Admin"
    PASSWORD = "admin123"
    LOGIN_PAGE_TITLE = "Auto Loans | DCU"
    PAY_MY_LOAN_TITLE = "Loan Payments | DCU"
    MEMBER_NUMBER = "321"
    LOAN_NUMBER = "987"
    SSN_LAST_DIGITS = "3577"

    TD_DCU_Workbook = "C:\\Users\\sindh\\PycharmProjects\\POMFramework_POC\\TestData\\TDexcel.xlsx"
    TD_DCU_Sheet = "Sheet1"

    #SkillBoard locators:
    URL_SKILLBOARD = "https://skillboard.org/"
    FIRSTNAME = "Sindhu"
    LASTNAME = "Boston"
    USERNAME = "sindhuboston"
    TD_SkillBoard_Workbook = "C:\\Users\\sindh\\PycharmProjects\\POMFramework_POC\\TestData\\TDexcel.xlsx"
    TD_SkillBoard_Sheet = "Sheet1"


    EXCEL_FILE_PATH = None
    SHEET_NAME = None

    @classmethod
    def set_excel_file_path(cls, file_path):
        cls.EXCEL_FILE_PATH = file_path

    @classmethod
    def set_sheet_name(cls, sheet_name):
        cls.SHEET_NAME = sheet_name