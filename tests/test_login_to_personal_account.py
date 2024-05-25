from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (login_to_account, login_button, email_input, personal_account, password_recovery_form,
                      password_input, login_from_recovery_form, registration_form)


class TestLoginToAccount:
    def test_login_to_account(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def test_login_personal_account(self, driver, open_stellarburgers):
        driver.find_element(*personal_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def test_login_password_recovery_form(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*password_recovery_form).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password"))

        driver.find_element(*login_from_recovery_form).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def test_login_registration_form(self, driver, open_stellarburgers, open_registration_page, fill_registration_form):
        _, generated_email, generated_password = fill_registration_form(driver)

        driver.find_element(*registration_form).click()

        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*email_input).send_keys(generated_email)
        driver.find_element(*password_input).send_keys(generated_password)

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url
