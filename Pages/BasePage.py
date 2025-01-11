#TODO This class is the parent of all the Pages
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from Config.config import TestData

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.get_title(title)

    def click(self, by_locator):
        try:
            # Wait for the element to be visible and clickable
            WebDriverWait(self.driver, timeout=15).until(
                EC.visibility_of_element_located(by_locator)
            ).click()
            logger.info(f"Successfully clicked the element: {by_locator}")
            return True  # Explicitly return success
        except Exception as e:
            # Log the error and return failure
            logger.error(f"An error occurred while clicking the element {by_locator}: {str(e)}")
            return False  # Explicitly return failure

    def all_click(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located(by_locator))
        # element = self.driver.find_elements(by_locator)
        return  element

    def sendkeys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
        assert element, "element not displayed"

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def mouse_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        hover = ActionChains(self.driver).move_to_element(element)
        return hover

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def select_from_dropdown(self, by_locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        select = Select(element)
        select.select_by_visible_text(value)
