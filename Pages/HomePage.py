from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver import ActionChains


class LoginPage(BasePage):
    CLOSE_POPUP = "//button[@id='dismissBtn']"
    SKINCARE = "//label[@aria-label='Skincare']"
    AGING = "//a[contains(text(),'Anti-Aging')]"

    #TODO page action for login page

    def __init__(self, driver):
        self.driver = driver

    def get_title(self, title):
        return self.get_title(title)

    def close_popup(self, CLOSE_POPUP):
        self.do_click(self.CLOSE_POPUP)

    def validate_title(self, ):
        if (self.get_title() == self.driver.get(TestData.PAGE_TITLE)):
            assert True

    def product_navigation(self):
        self.do_send_keys(self.SKINCARE)
        self.do_click(self.AGING)

    # def do_login(self,username,password):
    #     self.do_send_keys(self.EMAIL)
    #     self.do_send_keys(self.PASSWORD)
    #     self.do_click(self.SIGN_IN)
    #
    # def do_signup(self,signup):
    #     self.do_click(self.SIGN_UP)
