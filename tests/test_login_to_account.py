from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
driver.find_element(
    By.XPATH,
    "//input[@type='text']").send_keys("olyamishina9123@yandex.ru")
driver.find_element(
    By.XPATH,
    "//input[@type='password']").send_keys("zxcvbnm")

driver.find_element(
    By.CSS_SELECTOR, ".Auth_form__3qKeq.mb-20 .button_button__33qZ0").click()

WebDriverWait(driver, 10).until(
    EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

current_url = driver.current_url
expected_url = "https://stellarburgers.nomoreparties.site/"
assert current_url == expected_url

driver.quit()

