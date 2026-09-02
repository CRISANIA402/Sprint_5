from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *

def test_navigate_to_sauces(driver):
    driver.find_element(*SECTION_SAUCES).click()
    
    WebDriverWait(driver, 7).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.text.text_type_main-default"), "Соусы"
        )
    )
    element = driver.find_element(By.CSS_SELECTOR, "span.text.text_type_main-default")
    assert "Соусы" in element.text


def test_navigate_to_buns(driver):
    driver.find_element(*SECTION_BUNS).click()

    WebDriverWait(driver, 7).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.text.text_type_main-default"), "Булки"
        )
    )
    element = driver.find_element(By.CSS_SELECTOR, "span.text.text_type_main-default")
    assert "Булки" in element.text


def test_navigate_to_fillings(driver):
    driver.find_element(*SECTION_FILLINGS).click()

    WebDriverWait(driver, 7).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.text.text_type_main-default"), "Начинки"
        )
    )
    element = driver.find_element(By.CSS_SELECTOR, "span.text.text_type_main-default")
    assert "Начинки" in element.text
    