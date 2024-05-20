from selenium.webdriver.common.by import By
from faker import Faker

class Registration:

    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()
        self.generated_name = None
        self.generated_email = None
        self.generated_password = None

    def open_registration_page(self):
        self.driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
        self.driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

    def fill_registration_form(self, name=None, email=None, password=None):
        name_input = self.driver.find_element(
            By.XPATH,
            "//div[@class='Auth_login__3hAey']//label[text()='Имя']/following-sibling::input")
        email_input = self.driver.find_element(
            By.XPATH,
            "//div[@class='Auth_login__3hAey']//label[text()='Email']/following-sibling::input")
        password_input = self.driver.find_element(
            By.XPATH,
            "//div[@class='Auth_login__3hAey']//label[text()='Пароль']/following-sibling::input")

        self.generated_name = name if name else self.fake.name()
        self.generated_email = email if email else self.fake.email()
        self.generated_password = password if password else self.fake.password(length=8)

        name_input.send_keys(self.generated_name)
        email_input.send_keys(self.generated_email)
        password_input.send_keys(self.generated_password)

    def submit_registration(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".Auth_login__3hAey .button_button__33qZ0")
        submit_button.click()

    def get_registration_data(self):
        return {
            'name': self.generated_name,
            'email': self.generated_email,
            'password': self.generated_password
        }
