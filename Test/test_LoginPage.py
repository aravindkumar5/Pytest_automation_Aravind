import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage

from Config.config import TestData
from Pages.BasePage import BasePage

from Test.test_base import BaseTest


class Test_Login_001():
    BASE_URL = "https://www.clinique.com"
    USER_NAME = "qatester123@gmail.com"
    PASSWORD = "Tester123"
    PAGE_TITLE = 'Clinique | Dermatology Skincare, Makeup, Fragrances & Gifts'
    LOGIN_PAGE_TITLE = "Clinique"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.BASE_URL)
        actual_title = self.driver.title
        if actual_title == "Clinique | Dermatology Skincare, Makeup, Fragrances & Gifts":
            assert True
        else:
            assert False
        self.driver.close()

    def test_signup_link(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.BASE_URL)
        self.lp = LoginPage(self.driver)
        # self.lp.close_popup()
        self.lp.homepage_signin()
        self.lp.username(self.USER_NAME)
        self.lp.password(self.PASSWORD)
        self.lp.click_signin()
        if self.lp.is_displayed():
            print("successfully logged")


    def test_login(self):
        pass

