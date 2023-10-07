from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):

    INSURANCE_LINK = (By.LINK_TEXT, "Insurance")
    MAKE_A_PAYMENT_BUTTON = (By.XPATH, "//p[@class='mobile']//a[contains(text(),'Make A Payment')]")


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_make_a_payment_button_exist(self):
        return self.is_visible(self.MAKE_A_PAYMENT_BUTTON)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def check_insurance_link_exist(self):
        return self.is_visible(self.INSURANCE_LINK)

    def do_make_a_payment(self):
        self.do_click(self.MAKE_A_PAYMENT_BUTTON)
