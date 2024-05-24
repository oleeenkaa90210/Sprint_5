from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import registration_button, reg_name_input, reg_email_input, reg_password_input, registration_form
from locators import message_error_invalid_password, login_to_account
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

class TestRegistration:
    def test_registration_pass(self, driver, faker):
        driver.get("https://stellarburgers.nomoreparties.site")

        self.open_registration_page(driver)
        self.fill_registration_form(driver, faker)

        driver.find_element(*registration_form).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/login"
        assert current_url == expected_url

    def test_registration_incorrect_password(self, driver, faker):
        driver.get("https://stellarburgers.nomoreparties.site")

        self.open_registration_page(driver)
        self.fill_registration_form(driver, faker, password="12")
        name_input = driver.find_element(*reg_name_input)
        name_input.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(message_error_invalid_password))

        assert "Некорректный пароль" in error_message.text

    def open_registration_page(self, driver):
        driver.find_element(*login_to_account).click()
        driver.find_element(*registration_button).click()

    def fill_registration_form(self, driver, faker, name=None, email=None, password=None):
        name_input = driver.find_element(*reg_name_input)
        email_input = driver.find_element(*reg_email_input)
        password_input = driver.find_element(*reg_password_input)

        generated_name = name if name else faker.name()
        generated_email = email if email else faker.email()
        generated_password = password if password else faker.password(length=8)

        name_input.send_keys(generated_name)
        email_input.send_keys(generated_email)
        password_input.send_keys(generated_password)

    def submit_registration(self, driver):
        submit_button = driver.find_element(*registration_form)
        submit_button.click()

    def get_registration_data(self):
        return {
            'name': self.generated_name,
            'email': self.generated_email,
            'password': self.generated_password
        }
