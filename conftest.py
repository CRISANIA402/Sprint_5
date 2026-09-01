
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data import URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()