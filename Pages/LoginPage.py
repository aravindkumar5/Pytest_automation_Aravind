from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.NAME,"EMAIL_ADDRESS")
    PASSWORD = (By.NAME,"PASSWORD")
    SIGN_IN = (By.XPATH,"//input[@value='Sign in']")
    SIGN_UP = (By.ID,"new-account-link")

#TODO page action for login page

    def __init__(self,driver):
        super().__init__(driver)

    def get_title(self,title):
        return self.get_title(title)

    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL)
        self.do_send_keys(self.PASSWORD)
        self.do_click(self.SIGN_IN)

    def do_signup(self,signup):
        self.do_click(self.SIGN_UP)


