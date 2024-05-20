from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from registration import Registration

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

registration = Registration(driver)
registration.open_registration_page()
registration.fill_registration_form(password="12")
name_input = driver.find_element(
    By.XPATH,
    "//div[@class='Auth_login__3hAey']//label[text()='Имя']/following-sibling::input")
name_input.click()

error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.input__error"))
)

assert "Некорректный пароль" in error_message.text

driver.quit()
