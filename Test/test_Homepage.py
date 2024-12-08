import time

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Test.test_base import BaseTest
from Config.config import TestData
from selenium import webdriver


class Test_Homepage(BaseTest):

    # def test_homepage_title(self):
    #     # self.driver = webdriver.Chrome()
    #     # self.driver.get(TestData.BASE_URL)
    #     expected_title = self.driver.title
    #     if expected_title == TestData.LOGIN_PAGE_TITLE:
    #         assert True
    #     else:
    #         assert False

    def test_hover_skincare(self):
        self.hp = HomePage(self.driver)
        title = self.hp.get_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE
        self.hp.skincare_hover()
        self.hp.product_navigation()  #2nd case
        self.hp.scroll_to_skincare()
        self.hp.quickview_hover()
        self.hp.click_quick_view()
        self.hp.add_to_bag()
        self.hp.check_out()
        self.hp.cart_check_out()
        self.hp.checkout_login(TestData.USER_NAME, TestData.PASSWORD)
        self.hp.cart_check_out()
        time.sleep(5)
        self.hp.new_shipping_add_click()
        self.hp.checkout_address(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.ADDRESS_1, TestData.ADDRESS_2,
                                 TestData.PINCODE, TestData.CITY, TestData.PHONE_NO)
