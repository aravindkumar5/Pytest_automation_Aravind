import pytest

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Test.test_base import BaseTest


class TestLogin(BaseTest,BasePage):


    def page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE


    def signup_link(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.home_signup()

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)





