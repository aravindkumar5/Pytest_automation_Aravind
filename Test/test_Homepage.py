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

    def test_skincare(self):
        self.hp = HomePage()

