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


driver.find_element(By.CSS_SELECTOR, ".Auth_login__3hAey .button_button__33qZ0").click()

WebDriverWait(driver, 10).until(
    EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

current_url = driver.current_url
expected_url = "https://stellarburgers.nomoreparties.site/login"
assert current_url == expected_url

driver.quit()
