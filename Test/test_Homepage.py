from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Test.test_base import BaseTest
from Config.config import TestData
from selenium import webdriver


class Test_Homepage(BaseTest):

    def test_homepage_title(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get(TestData.BASE_URL)
        expected_title = self.driver.title
        if expected_title == TestData.LOGIN_PAGE_TITLE:
            assert True
        else:
            assert False

    def test_hover_skincare(self):
        self.hp = HomePage(self.driver)
        self.hp.skincare_hover()
        self.hp.product_navigation() #2nd case
        self.hp.scroll_to_skincare()
        self.hp.quickview_hover()
        self.hp.click_quick_view()
        self.hp.add_to_bag()
        self.hp.check_out()
        self.hp.cart_check_out()






