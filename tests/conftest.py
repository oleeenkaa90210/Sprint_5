import pytest
from selenium import webdriver
from faker import Faker
from locators import login_to_account, registration_button, reg_name_input, reg_email_input, reg_password_input


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_stellarburgers(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

@pytest.fixture
def open_registration_page(driver):
    driver.find_element(*login_to_account).click()
    driver.find_element(*registration_button).click()

@pytest.fixture
def fill_registration_form():
    def _fill_registration_form(driver, name=None, email=None, password=None):
        faker = Faker()

        name_input = driver.find_element(*reg_name_input)
        email_input = driver.find_element(*reg_email_input)
        password_input = driver.find_element(*reg_password_input)

        generated_name = name if name else faker.name()
        generated_email = email if email else faker.email()
        generated_password = password if password else faker.password(length=8)

        name_input.send_keys(generated_name)
        email_input.send_keys(generated_email)
        password_input.send_keys(generated_password)
        return generated_name, generated_email, generated_password

    return _fill_registration_form
