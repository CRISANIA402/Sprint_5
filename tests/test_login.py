from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import *

class TestLoginScenarios:

    def test_login_from_main_button(self, driver):
        driver.find_element(*LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
        )

        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys("crisaniapaladaina@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys("eliot38472")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(ORDER_SUBMIT_BUTTON, "Оформить заказ")
        )
        assert driver.current_url == URL

    def test_login_from_personal_account(self, driver):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
        )

        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys("crisaniapaladaina@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys("eliot38472")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(ORDER_SUBMIT_BUTTON, "Оформить заказ")
        )
        assert driver.current_url == URL

    def test_login_from_registration_form(self, driver):
        driver.get(URL + "register")
        driver.find_element(*LOGIN_LINK_FROM_REG).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
        )

        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys("crisaniapaladaina@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys("eliot38472")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(ORDER_SUBMIT_BUTTON, "Оформить заказ")
        )
        assert driver.current_url == URL

    def test_login_from_reset_password_form(self, driver):
        driver.get(URL + "login")
        driver.find_element(*RESET_PASSWORD_LINK).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RESET_SUBMIT_BUTTON)
        )
        driver.find_element(*LOGIN_LINK_FROM_RESET).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON)
        )

        driver.find_element(*LOGIN_EMAIL_FIELD).send_keys("crisaniapaladaina@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys("eliot38472")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(ORDER_SUBMIT_BUTTON, "Оформить заказ")
        )
        assert driver.current_url == URL
