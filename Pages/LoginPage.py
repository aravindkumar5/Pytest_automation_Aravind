from selenium.webdriver.common.by import By

from selenium import webdriver

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    email_field = (By.NAME, "EMAIL_ADDRESS")
    password_field = (By.NAME, "PASSWORD")
    sign_in = (By.XPATH, "//input[@value='Sign in']")
    Sign_up = (By.ID, "new-account-link")
    log_out = ""
    home_signin = (By.XPATH, "//a[@aria-label='Sign in']")

    #TODO page action for login page

    def __init__(self, driver):
        self.driver = driver

    def homepage_signin(self):
        self.driver.find_element_by_xpath(self.home_signin).click()

    def username(self, username):
        self.driver.find_element_by_name(self.email_field).send_keys(username)

    def password(self, password):
        self.driver.find_element_by_name(self.password_field).send_keys(password)

    def click_signin(self):
        self.driver.find_element_by_xpath(self.sign_in).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.log_out).click()

