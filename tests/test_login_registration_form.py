from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from registration import Registration

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

registration = Registration(driver)
registration.open_registration_page()
registration.fill_registration_form()
registration_data = registration.get_registration_data()

driver.find_element(By.CSS_SELECTOR, ".Auth_login__3hAey .button_button__33qZ0").click()

WebDriverWait(driver, 10).until(
    EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
driver.find_element(
    By.XPATH,
    "//input[@type='text']").send_keys(registration_data["email"])
driver.find_element(
    By.XPATH,
    "//input[@type='password']").send_keys(registration_data["password"])

driver.find_element(
    By.CSS_SELECTOR,
    ".Auth_form__3qKeq.mb-20 .button_button__33qZ0").click()

WebDriverWait(driver, 10).until(
    EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

current_url = driver.current_url
expected_url = "https://stellarburgers.nomoreparties.site/"
assert current_url == expected_url

driver.quit()


