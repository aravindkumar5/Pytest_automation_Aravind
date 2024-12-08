import pytest
from selenium import webdriver

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

from Config.config import TestData
from Pages.BasePage import BasePage

from Test.test_base import BaseTest


class Test_Login(BaseTest):

    @pytest.mark.first
    def test_signup_link_visible(self):
        self.lp = LoginPage(self.driver)
        flag = self.lp.is_signup_link_exist()
        assert flag

    @pytest.mark.second
    def test_click_login_link(self):
        self.lp = LoginPage(self.driver)
        self.lp.click_signin_link()

    @pytest.mark.third
    def test_logged_in(self):
        self.lp = LoginPage(self.driver)
        self.lp.use_login(TestData.USER_NAME, TestData.PASSWORD)

    @pytest.mark.last
    def test_login_page_title(self):
        self.lp = LoginPage(self.driver)
        title = self.lp.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE



