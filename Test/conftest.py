import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox import options

from Config.config import TestData

web_driver = None
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        service_obj = Service(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=service_obj)
    if request.param == "firefox":
        service = Service(executable_path="firefox.geckodriver")
        web_driver = webdriver.Firefox(service=service)
    request.cls.driver = web_driver
    yield
    web_driver.close()
