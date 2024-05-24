from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (login_to_account, login_button, email_input, personal_account, password_recovery_form,
password_input, login_from_recovery_form, registration_form, reg_name_input, registration_button, reg_email_input, reg_password_input)
from faker import Faker
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def faker():
    return Faker()
class TestLoginToAccount:
    def test_login_to_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def test_login_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*personal_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def test_login_password_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
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

    def test_login_registration_form(self, driver, faker):
        driver.get("https://stellarburgers.nomoreparties.site")

        self.open_registration_page(driver)
        self.fill_registration_form(driver, faker)
        registration_data = self.get_registration_data()

        driver.find_element(*registration_form).click()

        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*email_input).send_keys(registration_data["email"])
        driver.find_element(*password_input).send_keys(registration_data["password"])

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def open_registration_page(self, driver):
        driver.find_element(*login_to_account).click()
        driver.find_element(*registration_button).click()

    def fill_registration_form(self, driver, faker, name=None, email=None, password=None):
        name_input = driver.find_element(*reg_name_input)
        email_input = driver.find_element(*reg_email_input)
        password_input = driver.find_element(*reg_password_input)

        self.generated_name = name if name else faker.name()
        self.generated_email = email if email else faker.email()
        self.generated_password = password if password else faker.password(length=8)

        name_input.send_keys(self.generated_name)
        email_input.send_keys(self.generated_email)
        password_input.send_keys(self.generated_password)

    def submit_registration(self, driver):
        submit_button = driver.find_element(*registration_form)
        submit_button.click()

    def get_registration_data(self):
        return {
            'name': self.generated_name,
            'email': self.generated_email,
            'password': self.generated_password
        }