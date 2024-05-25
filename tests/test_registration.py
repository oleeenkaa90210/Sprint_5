from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import reg_name_input, registration_form
from locators import message_error_invalid_password

class TestRegistration:
    def test_registration_pass(self, driver, open_stellarburgers, open_registration_page, fill_registration_form):
        fill_registration_form(driver)

        driver.find_element(*registration_form).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/login"
        assert current_url == expected_url

    def test_registration_incorrect_password(self, driver, open_stellarburgers, open_registration_page, fill_registration_form):
        fill_registration_form(driver, password="12")
        name_input = driver.find_element(*reg_name_input)
        name_input.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(message_error_invalid_password))

        assert "Некорректный пароль" in error_message.text
