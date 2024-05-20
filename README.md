**registration.py**
Регистрация нового пользователя с рандомными именем, email и пароль 

**test_construction_from_personal_account.py**
Клик на кнопку из личного кабинета 'Конструктор'
-Выполняется вход зарегистрированного пользователя 
-Переход в Личный кабинет
-Клик на кнопку 'Конструктор'
Запуск через терминал:
pytest tests/test_construction_from_personal_account.py

**test_go_to_account**
Переход в личный кабинет через кнопку 'Личный кабинет'
-Выполняется вход зарегистрированного пользователя 
-Переход в Личный кабинет
Запуск через терминал:
pytest tests/test_go_to_account.py

**test_go_to_buns_section.py**
Переход к разделу 'Булки'
-Выполняется вход зарегистрированного пользователя 
-Переход к разделу 'Соусы'
-Переход к разделу 'Булки'
Запуск через терминал:
pytest tests/test_go_to_buns_section.py

**test_go_to_fillings_section.py**
Переход к разделу 'Начинки'
-Выполняется вход зарегистрированного пользователя 
-Переход к разделу 'Начинки'
Запуск через терминал:
pytest tests/test_go_to_fillings_section.py

**test_go_to_sauces_section.py**
Переход к разделу 'Соусы'
-Выполняется вход зарегистрированного пользователя 
-Переход к разделу 'Соусы'
Запуск через терминал:
pytest tests/test_go_to_sauces_section.py

**test_login_password_recovery_form.py**
Вход через кнопку в форме восстановления пароля
-Переход на форму входа
-Клик на "Восстановить пароль"
-Клик на "Войти"
-Ввод данных для Входа
Запуск через терминал:
pytest tests/test_login_password_recovery_form.py

**test_login_personal_account.py**
Вход через кнопку в форме регистрации
-Регистрация
-Ввод зарегистрированного пользователя 
-Вход
Запуск через терминал:
pytest tests/test_login_registration_form.py

**test_login_to_account.py**
Вход по кнопке «Войти в аккаунт» на главной
-Клик на "Войти в аккаунт"
-Ввод данных зарегистрированного пользователя
-Клик на "Войти"
Запуск через терминал:
pytest tests/test_login_to_account.py

**test_logo_from_personal_account**
Переход на логотип Stellar Burgers
-Клик на "Войти в аккаунт"
-Вход зарегистрированного пользователя
-Клик на логотип
Запуск через терминал:
pytest tests/test_logo_from_personal_account

**test_logout_from_personal_account**
Выход по кнопке «Выйти» в личном кабинете
-Клик на "Войти в аккаунт"
-Вход зарегистрированного пользователя
-Переход в личный кабинет
-Клик на "Выход"
Запуск через терминал:
pytest tests/test_logout_from_personal_account

**test_registratiom_incorrect_password.py**
Ошибкa для некорректного пароля
-Клик на "Войти в аккаунт"
-Клик на "Зарегистрироваться"
-Ввод данных для регистрации, пароль менее 6 символов
-Проверка на ошибку в поле пароля
Запуск через терминал:
pytest tests/test_registratiom_incorrect_password.py

**test_registration_pass.py**
Успешная регистрация
-Клик на "Войти в аккаунт"
-Клик на "Зарегистрироваться"
-Ввод данных корректных
Запуск через терминал:
pytest tests/test_registration_pass.py



















