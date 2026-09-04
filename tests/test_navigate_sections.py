from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestNavigateSections:

    def test_navigate_to_sauces(self, driver):
        driver.find_element(*SECTION_SAUCES).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(TAB_HEADER_SAUCES)
        )

        element = driver.find_element(*TAB_HEADER_SAUCES)
        assert element.text == "Соусы"

    def test_navigate_to_buns(self, driver):
        driver.find_element(*SECTION_BUNS).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(TAB_HEADER_BUNS)
        )

        element = driver.find_element(*TAB_HEADER_BUNS)
        assert element.text == "Булки"

    def test_navigate_to_fillings(self, driver):
        driver.find_element(*SECTION_FILLINGS).click()

        WebDriverWait(driver, 7).until(
            EC.visibility_of_element_located(TAB_HEADER_FILLINGS)
        )

        element = driver.find_element(*TAB_HEADER_FILLINGS)
        assert element.text == "Начинки"
