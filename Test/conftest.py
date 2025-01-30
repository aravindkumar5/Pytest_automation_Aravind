import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # chrome_options = Options()
        # chrome_options.add_argument("--headless=new")
        # web_driver = webdriver.Chrome(options=chrome_options)
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()
        # service_obj = Service(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        # web_driver = webdriver.Chrome(service=service_obj)
    if request.param == "firefox":
        service = Service(executable_path="firefox.geckodriver")
        web_driver = webdriver.Firefox(service=service)
    request.cls.driver = web_driver
    yield
    web_driver.close()

