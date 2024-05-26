from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import login_to_account, login_button, email_input, personal_account, logout_button, password_input, logo, construction, sauces_button, fillings_button, buns_button
class TestPersonalAccount:

    def test_go_to_account(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*personal_account).click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
        assert current_url == expected_url

    def test_logout_from_personal_account(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*personal_account).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(*logout_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/login"
        assert current_url == expected_url

        driver.quit()

    def test_logo_from_personal_account(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*personal_account).click()

        driver.find_element(*logo).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def test_construction_from_personal_account(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        driver.find_element(*personal_account).click()

        driver.find_element(*construction).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        current_url = driver.current_url
        expected_url = "https://stellarburgers.nomoreparties.site/"
        assert current_url == expected_url

    def test_go_to_buns_section(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        sauces = driver.find_element(*sauces_button)
        sauces.click()

        buns = driver.find_element(*buns_button)
        buns.click()

        assert "tab_tab_type_current__2BEPc" in buns.get_attribute(
            "class"), "The div does not have the 'tab_tab_type_current__2BEPc' class"

    def test_go_to_fillings_section(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")
        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        fillings = driver.find_element(*fillings_button)
        fillings.click()

        assert "tab_tab_type_current__2BEPc" in fillings.get_attribute(
            "class"), "The div does not have the 'tab_tab_type_current__2BEPc' class"

    def test_go_to_sauces_section(self, driver, open_stellarburgers):
        driver.find_element(*login_to_account).click()
        driver.find_element(*email_input).send_keys("olyamishina9123@yandex.ru")
        driver.find_element(*password_input).send_keys("zxcvbnm")

        driver.find_element(*login_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        sauces = driver.find_element(*sauces_button)
        sauces.click()

        assert "tab_tab_type_current__2BEPc" in sauces.get_attribute(
            "class"), "The div does not have the 'tab_tab_type_current__2BEPc' class"



