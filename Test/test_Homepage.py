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
# import requests

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


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
        title = cls.hp.driver.title
        if title == TestData.PAGE_TITLE:
            assert True
            logger.info("Verified the page title")
        else:
            logger.error("Page title is not matching with the expected title")
            assert False, "Page title verification failed"

    def test_prod_nav(self):
        self.hp.skincare_hover()
        if self.hp.product_navigation():  #2nd case
            assert True
            logger.info("Product link click, landed on multiple product page")
        else:
            logger.error("Not able to click the link")
            assert False, "Product navigation failed"

        # screenshot_data = self.hp.driver.get_screenshot_as_png()

    def test_add_qv(self):
        if self.hp.scroll_to_skincare():
            assert True
            logger.info("Scrolled to skincare")
            assert True
        if self.hp.quickview_hover():
            assert True
            logger.info("Hover check")
        if self.hp.click_quick_view():
            assert True
            logger.info("Clicked on quick view")
        if self.hp.add_to_bag():
            assert True
            logger.info("Product is added to cart")
        else:
            logger.error("Not able to add the product to cart")
            assert False, "Add to bag actions failed"

    def test_checkout(self):
        if self.hp.check_out():
            assert True
            logger.info("Able to click the check out button")
        if self.hp.cart_check_out():
            assert True
            logger.info("User is able to enter address in the shipping page")
        if self.hp.checkout_login(TestData.USER_NAME, TestData.PASSWORD):
            assert True
            logger.info("User is able to sign in checkout page")
        if self.hp.cart_check_out():
            assert True
            logger.info("User is able to click checkout button in checkout page")
            time.sleep(5)
        if self.hp.new_shipping_add_click():
            assert True
            logger.info("User is able to click add shipping address button")
        if self.hp.checkout_address(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.ADDRESS_1, TestData.ADDRESS_2,
                                      TestData.PINCODE, TestData.CITY, TestData.PHONE_NO):
            assert True
            logger.info("User is able to enter the address")
        else:
            logger.error("User is not able to add shipping address")
            assert False, "Entering address action failed"

    def test_footer_link(self):
        self.hp = HomePage(self.driver)
        self.hp.scroll_to_footer()
        footer_links = self.hp.footer_link_check()
        for link_name in footer_links:
            get_link = link_name.get_attribute("href")
            print(link_name.text, '-', get_link)
            ActionChains(self.hp.driver).key_down(Keys.CONTROL).click(link_name).key_up(Keys.CONTROL).perform()
            window_handles = self.hp.driver.window_handles
            parent_window = window_handles[0]
            if len(window_handles) > 1:
                child_window = window_handles[1]
                self.hp.driver.switch_to.window(child_window)
                time.sleep(1)
                # child_window_url = self.hp.driver.current_url
                # response = requests.get(child_window_url)
                # if response.status_code == 200:
                #     print(f"Success: The page {child_window_url} returned a 200 OK response.")
                # else:
                #     print(f"Error: The page {child_window_url} returned a {response.status_code} response.")
                self.hp.driver.close()
            self.hp.driver.switch_to.window(parent_window)

            # self.hp.driver.close()
            # self.hp.driver.switch_to.window(parent_window)
            # title = self.hp.driver.get_title
            # print(title)

            # if offer == self.hp.driver.title:
            # elif

            # time.sleep(5)
            # self.hp.driver.close()
