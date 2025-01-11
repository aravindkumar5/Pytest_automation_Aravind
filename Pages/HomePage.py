from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver import ActionChains


class HomePage(BasePage):
    CLOSE_POPUP = (By.XPATH, "//button[@id='dismissBtn']")
    SKINCARE = (By.XPATH, "//label[@aria-label='Skincare']")
    AGING = (By.XPATH, "(//a[contains(text(),'Anti-Aging')])[1]")
    QUICK_SHOP = (By.XPATH, "(//button[@aria-label='Quick Shop'])[4]")
    PROD_IMG = (By.XPATH, "//img[@alt='1.7oz / 50ml | clinique smart clinical repair™ lifting face + neck cream']")
    SHORT_DEC = (By.XPATH, "(//div[@class='elc-product-name-section js-product-name-section'])[4]")
    ADD_TO_BAG = (By.XPATH, '//button[@aria-label="Add To Bag"]')
    CHECK_OUT = (By.XPATH, "(//a[@class='button btn-primary'])[1]")
    CART_CHECK_OUT = (By.XPATH, "//a[@class='checkout-btns button']")
    #TODO Checkout inputs
    FIRST_NAME = (By.XPATH, "// input[ @ id = 'shipping-first-name-input']")
    LAST_NAME = (By.XPATH, "// input[ @ id = 'shipping-last-name-input']")
    ADDRESS_1 = (By.XPATH, "// input[ @ id = 'shipping-address1-input']")
    ADDRESS_2 = (By.XPATH, "// input[ @ id = 'shipping-address2-input']")
    PINCODE = (By.XPATH, "// input[ @ id = 'shipping-zip-code-input']")
    CITY = (By.XPATH, "//input[@id='shipping-city-input']")
    PHONE_NO = (By.XPATH, "// input[ @ id = 'shipping-phone1-input']")
    STATE_LIST = (By.XPATH, "//ul[@role='listbox']")
    CHK_PWD_FLD = (By.XPATH, "//input[@id='form--checkout-_-checkout_signin--field--PASSWORD']")
    CHK_BTN = (By.XPATH, "//input[@data-test-id='form_signin_continue']")
    EMAIL_FIELD = (By.NAME, "EMAIL_ADDRESS")
    NEW_SHIPPING_ADD = (By.XPATH, "//div[contains(@class,'new-address-label')]")
    STATE_NAME = (By.XPATH, "//li[@id='downshift-0-item-2']")
    FOOTER_LINK = (By.XPATH, "//a[@class='text-link--style-2']")

    #TODO page action for login page

    def __init__(self, driver):
        super().__init__(driver)

    # def get_title(self):
    #     return self.driver.title

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
        hover_action = self.mouse_hover(self.PROD_IMG)
        hover_action.perform()

    def click_quick_view(self):
        self.click(self.QUICK_SHOP)

    def add_to_bag(self):
        self.click(self.ADD_TO_BAG)

    def check_out(self):
        self.click(self.CHECK_OUT)

    def cart_check_out(self):
        self.click(self.CART_CHECK_OUT)

    def checkout_address(self, firstname, lastname, address1, address2, pincode, city, phone_no):
        self.sendkeys(self.FIRST_NAME, firstname)
        self.sendkeys(self.LAST_NAME, lastname)
        self.sendkeys(self.ADDRESS_1, address1)
        self.sendkeys(self.ADDRESS_2, address2)
        self.sendkeys(self.CITY, city)
        self.sendkeys(self.PINCODE, pincode)
        self.sendkeys(self.PHONE_NO, phone_no)
        # self.click(self.STATE_LIST)
        # self.click(self.STATE_NAME)

    def scroll_to_footer(self):
        self.scroll_to_element(self.FOOTER_LINK)

    # def state_dropdown(self, value):
    #     self.select_from_dropdown(self.STATE_LIST, value)

    def checkout_login(self, username, password):
        self.sendkeys(self.EMAIL_FIELD, username)
        self.sendkeys(self.CHK_PWD_FLD, password)
        self.click(self.CHK_BTN)

    def new_shipping_add_click(self):
        self.click(self.NEW_SHIPPING_ADD)

    def footer_link_check(self):
        element = self.all_click(self.FOOTER_LINK)
        return element

    # def validate_title(self, ):
    #     if (self.get_title() == self.driver.get(TestData.PAGE_TITLE)):
    #         assert True

    # def do_login(self,username,password):
    #     self.do_send_keys(self.EMAIL)
    #     self.do_send_keys(self.PASSWORD)
    #     self.do_click(self.SIGN_IN)
    #
    # def do_signup(self,signup):
    #     self.do_click(self.SIGN_UP)
