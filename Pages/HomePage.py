from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver import ActionChains


class HomePage(BasePage):
    CLOSE_POPUP = (By.XPATH, "//button[@id='dismissBtn']")
    SKINCARE = (By.XPATH, "//label[@aria-label='Skincare']")
    AGING = (By.XPATH, "(//a[contains(text(),'Anti-Aging')])[2]")
    QUICK_SHOP =(By.XPATH, "(//button[@aria-label='Quick Shop'])[4]")
    SHORT_DEC = (By.XPATH,"(//div[@class='elc-product-name-section js-product-name-section'])[4]")
    ADD_TO_BAG = (By.XPATH,'//button[@aria-label="Add To Bag"]')
    CHECK_OUT = (By.XPATH,"(//a[@class='button btn-primary'])[1]")
    CART_CHECK_OUT = (By.XPATH,"//a[@class='checkout-btns button']")

    #TODO page action for login page

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self, title):
        return self.get_title(title)

    # def close_popup(self, CLOSE_POPUP):
    #     self.do_click(self.CLOSE_POPUP)

    def skincare_hover(self):
        hover_action = self.mouse_hover(self.SKINCARE)
        hover_action.perform()

    def product_navigation(self):
        self.click(self.AGING)

    def scroll_to_skincare(self):
        self.scroll_to_element(self.SHORT_DEC)

    def quickview_hover(self):
        hover_action = self.mouse_hover(self.QUICK_SHOP)
        hover_action.perform()

    def click_quick_view(self):
        self.click(self.QUICK_SHOP)

    def add_to_bag(self):
        self.click(self.ADD_TO_BAG)

    def check_out(self):
        self.click(self.CHECK_OUT)

    def cart_check_out(self):
        self.click(self.CART_CHECK_OUT)

    def validate_title(self, ):
        if (self.get_title() == self.driver.get(TestData.PAGE_TITLE)):
            assert True




    # def do_login(self,username,password):
    #     self.do_send_keys(self.EMAIL)
    #     self.do_send_keys(self.PASSWORD)
    #     self.do_click(self.SIGN_IN)
    #
    # def do_signup(self,signup):
    #     self.do_click(self.SIGN_UP)
