(By.CLASS_NAME, "button_button__33qZ0") #Войти в аккаунт
(By.XPATH,"//nav[contains(@class, 'AppHeader_header__nav__g5hnF')]//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2')][contains(text(), 'Личный Кабинет')]")
#Личный кабинет
(By.CLASS_NAME, "Auth_link__1fOlj") #Зарегистрироваться
(By.XPATH,"//div[contains(@class, 'Auth_login__3hAey')]//a[contains(@class, 'Auth_link__1fOlj')][contains(text(), 'Восстановить пароль')]") #Восстановить пароль
(By.XPATH,"//div[@class='Auth_login__3hAey']//label[text()='Имя']/following-sibling::input")  #Регистрация/Имя
(By.XPATH,"//div[@class='Auth_login__3hAey']//label[text()='Email']/following-sibling::input") #Регистрация/Email
(By.XPATH,"//div[@class='Auth_login__3hAey']//label[text()='Пароль']/following-sibling::input") #Регистрация/Пароль
(By.XPATH,"//input[@type='text']") #Вход/Email
(By.XPATH,"//input[@type='password']") #Вход/Пароль
(By.XPATH,"//nav[contains(@class, 'AppHeader_header__nav__g5hnF')]//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2')][contains(text(), 'Конструктор')]") #Кнопка Конструктор
logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2') #Логотип
(By.XPATH,"//section[contains(@class,'BurgerIngredients_ingredients__1N8v2')]//span[contains(text(),'Соусы')]/ancestor::div[1]") #Раздел Соусы
(By.XPATH,"//section[contains(@class,'BurgerIngredients_ingredients__1N8v2')]//span[contains(text(),'Булки')]/ancestor::div[1]") #Раздел Булки
(By.XPATH,"//section[contains(@class,'BurgerIngredients_ingredients__1N8v2')]//span[contains(text(),'Начинки')]/ancestor::div[1]") #Раздел Начинки
(By.XPATH,"//nav[contains(@class, 'Account_nav__Lgali')]//button[contains(text(), 'Выход')]") #Кнопка Выход

