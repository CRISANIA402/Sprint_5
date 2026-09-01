from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from data import URL 

def test_navigate_to_personal_account(driver):
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
    )
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys("crisaniapaladaina@yandex.ru")
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys("eliot38472")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//button"), "Оформить заказ"
        )
    )
    
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PROFILE_TEXT)
    )
    assert driver.current_url == URL + "account/profile"