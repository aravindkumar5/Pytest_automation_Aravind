import time
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import get_attributes

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
    @classmethod
    def test_hover_skincare(cls):
        cls.hp = HomePage(cls.driver)
        title = cls.hp.get_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE
        cls.hp.skincare_hover()

    def test_prod_nav(self):
        self.hp.product_navigation()  #2nd case

    def test_add_qv(self):
        self.hp.scroll_to_skincare()
        self.hp.quickview_hover()
        self.hp.click_quick_view()
        self.hp.add_to_bag()

    def test_checkout(self):
        self.hp.check_out()
        self.hp.cart_check_out()
        self.hp.checkout_login(TestData.USER_NAME, TestData.PASSWORD)
        self.hp.cart_check_out()
        time.sleep(5)
        self.hp.new_shipping_add_click()
        self.hp.checkout_address(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.ADDRESS_1, TestData.ADDRESS_2,
                                 TestData.PINCODE, TestData.CITY, TestData.PHONE_NO)

    def test_footer_link(self):
        self.hp = HomePage(self.driver)
        self.hp.scroll_to_footer()
        footer_links = self.hp.footer_link_check()
        for link_name in footer_links:
            get_link = link_name.get_attribute("href")
            print(link_name.text,'-',get_link)
            ActionChains(self.hp.driver).key_down(Keys.CONTROL).click(link_name).key_up(Keys.CONTROL).perform()
            # time.sleep(5)
            # self.hp.driver.close()






