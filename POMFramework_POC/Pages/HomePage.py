from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Utilities.utils import Utils
from Pages.PaymentPage import PaymentPage


class HomePage(BasePage):
    log = Utils.log_to_file_output()

    INSURANCE_LINK = (By.LINK_TEXT, "Insurance")
    MAKE_A_PAYMENT_BUTTON = (By.XPATH, "//p[@class='mobile']//a[contains(text(),'Make A Payment')]")
    CONTINUE_TO_MAKE_A_PAYMENT_BUTTON = (By.ID, "site-leave-continue-link")  #//a[@id="site-leave-continue-link"]


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_make_a_payment_button_exist(self):
        return self.is_visible(self.MAKE_A_PAYMENT_BUTTON)

    def get_home_page_title(self, title):
        self.log.info("title of the Home page: "+self.get_title(title))
        return self.get_title(title)

    def check_insurance_link_exist(self):
        self.log.info("The Insurance link should be visible: "+self.is_visible(self.INSURANCE_LINK))
        return self.is_visible(self.INSURANCE_LINK)

    def do_make_a_payment(self):
        self.do_click(self.MAKE_A_PAYMENT_BUTTON)
        self.log.info("Make A Payment button should be clicked.")
        self.do_click(self.CONTINUE_TO_MAKE_A_PAYMENT_BUTTON)
        self.log.info("Clicked on Continue to move to make a payment.")
        return PaymentPage(self.driver)