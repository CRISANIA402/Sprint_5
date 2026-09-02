from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from data import URL 


def test_navigate_to_constructor_from_personal_account(driver):
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
    )
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys("crisaniapaladaina@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys("eliot38472")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//button"), "Оформить заказ"
        )
    )
    
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(PROFILE_TEXT)
    )
    
    driver.find_element(*CONSTRUCTOR_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//button"), "Оформить заказ"
        )
    )
    assert driver.current_url == URL

def test_navigate_to_constructor_by_logo(driver):

    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
    )
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys("crisaniapaladaina@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys("eliot38472")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//button"), "Оформить заказ"
        )
    )
    
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(PROFILE_TEXT)
    )
    
    driver.find_element(*LOGO).click()
    
    WebDriverWait(driver, 3).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//button"), "Оформить заказ"
        )
    )
    assert driver.current_url == URL
