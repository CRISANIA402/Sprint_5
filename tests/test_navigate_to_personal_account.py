from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import URL 

class TestNavigateToPersonalAccount:
    def test_navigate_to_personal_account(self, driver):
        # Вход в систему
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

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(PROFILE_TEXT)
        )
        assert driver.current_url == URL + "account/profile"
