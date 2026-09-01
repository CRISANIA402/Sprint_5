from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import *

def test_successful_registration(driver):
    driver.get(URL + "register")
    
    driver.find_element(*REG_NAME_FIELD).send_keys(generate_name())
    driver.find_element(*REG_EMAIL_FIELD).send_keys(generate_email())
    driver.find_element(*REG_PASSWORD_FIELD).send_keys(generate_password())
    driver.find_element(*REG_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
    )
    
    assert driver.current_url == URL + "login"

def test_registration_short_password_error(driver):
    driver.get(URL + "register")
    
    driver.find_element(*REG_NAME_FIELD).send_keys(generate_name())
    driver.find_element(*REG_EMAIL_FIELD).send_keys(generate_email())
    driver.find_element(*REG_PASSWORD_FIELD).send_keys(generate_short_password())
    driver.find_element(*REG_SUBMIT_BUTTON).click()
    
    error = WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PASSWORD_ERROR_MESSAGE)
    )
    assert error.text == "Некорректный пароль"