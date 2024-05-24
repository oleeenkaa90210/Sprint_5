from selenium.webdriver.common.by import By

login_to_account = (By.CLASS_NAME, "button_button__33qZ0") #Войти в аккаунт
personal_account = (By.XPATH,"//nav[contains(@class, 'AppHeader_header__nav__g5hnF')]//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2')][contains(text(), 'Личный Кабинет')]")
#Личный кабинет
message_error_invalid_password = (By.CSS_SELECTOR, "p.input__error") #Ошибка некорректный пароль
registration_button = (By.CLASS_NAME, "Auth_link__1fOlj") #Зарегистрироваться
password_recovery_form = (By.XPATH,"//div[contains(@class, 'Auth_login__3hAey')]//a[contains(@class, 'Auth_link__1fOlj')][contains(text(), 'Восстановить пароль')]") #Восстановить пароль
reg_name_input = (By.XPATH,"//div[@class='Auth_login__3hAey']//label[text()='Имя']/following-sibling::input")  #Регистрация/Имя
reg_email_input = (By.XPATH,"//div[@class='Auth_login__3hAey']//label[text()='Email']/following-sibling::input") #Регистрация/Email
reg_password_input = (By.XPATH,"//div[@class='Auth_login__3hAey']//label[text()='Пароль']/following-sibling::input") #Регистрация/Пароль
email_input = (By.XPATH,"//input[@type='text']") #Вход/Email
password_input = (By.XPATH,"//input[@type='password']") #Вход/Пароль
construction = (By.XPATH,"//nav[contains(@class, 'AppHeader_header__nav__g5hnF')]//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2')][contains(text(), 'Конструктор')]") #Кнопка Конструктор
logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2') #Логотип
sauces_button = (By.XPATH,"//section[contains(@class,'BurgerIngredients_ingredients__1N8v2')]//span[contains(text(),'Соусы')]/ancestor::div[1]") #Раздел Соусы
buns_button = (By.XPATH,"//section[contains(@class,'BurgerIngredients_ingredients__1N8v2')]//span[contains(text(),'Булки')]/ancestor::div[1]") #Раздел Булки
fillings_button = (By.XPATH,"//section[contains(@class,'BurgerIngredients_ingredients__1N8v2')]//span[contains(text(),'Начинки')]/ancestor::div[1]") #Раздел Начинки
logout_button = (By.XPATH,"//nav[contains(@class, 'Account_nav__Lgali')]//button[contains(text(), 'Выход')]") #Кнопка Выход
login_button = (By.CSS_SELECTOR, ".Auth_form__3qKeq.mb-20 .button_button__33qZ0") #Войти
registration_form = (By.CSS_SELECTOR, ".Auth_login__3hAey .button_button__33qZ0") #Зарегистрироваться  в поле Регистрация
login_from_recovery_form = (By.XPATH,"//div[contains(@class, 'Auth_login__3hAey')]//a[contains(@class, 'Auth_link__1fOlj')][contains(text(), 'Войти')]") #Войти из формы восстановления пароля




