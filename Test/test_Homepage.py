from Pages.BasePage import BasePage
from Test.test_base import BaseTest
from Config.config import TestData
from selenium import webdriver


class Homepage(BaseTest, BasePage):

    def homepage_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TestData.BASE_URL)
        expected_title = self.driver.title
        if expected_title == TestData.LOGIN_PAGE_TITLE:
            assert True
        else:
            assert False
