from selenium.webdriver.common.by import By

# === Главная страница ===

# Кнопка «Войти в аккаунт» (на главной, если не залогинен)
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Кнопка «Личный кабинет» (в шапке)
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

# Кнопка «Конструктор» (в шапке)
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

# Логотип Stellar Burgers
LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

# Разделы меню в конструкторе
SECTION_BUNS = (By.XPATH, "//h2[text()='Булки']/parent::div")
SECTION_SAUCES = (By.XPATH, "//h2[text()='Соусы']/parent::div")
SECTION_FILLINGS = (By.XPATH, "//h2[text()='Начинки']/parent::div")

# === Страница регистрации ===

# Поле «Имя»
REG_NAME_FIELD = (By.XPATH, "//label[text()='Имя']//following-sibling::input")

# Поле «Email»
REG_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']//following-sibling::input")

# Поле «Пароль»
REG_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")

# Кнопка «Зарегистрироваться»
REG_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Ссылка «Войти» на странице регистрации
LOGIN_LINK_FROM_REG = (By.XPATH, "//a[text()='Войти']")

# Сообщение об ошибке некорректного пароля
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")

# === Страница входа ===

# Поле «Email» на странице входа
LOGIN_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']//following-sibling::input")

# Поле «Пароль» на странице входа
LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")

# Кнопка «Войти» на странице входа
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Ссылка «Восстановить пароль»
RESET_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

# Ссылка «Зарегистрироваться» на странице входа
REG_LINK_FROM_LOGIN = (By.XPATH, "//a[text()='Зарегистрироваться']")

# === Страница восстановления пароля ===

# Поле email на странице восстановления
RESET_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']//following-sibling::input")

# Кнопка «Восстановить»
RESET_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

# Ссылка «Войти» на странице восстановления
LOGIN_LINK_FROM_RESET = (By.XPATH, "//a[text()='Войти']")

# === Личный кабинет ===

# Кнопка «Выйти»
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Текст профиля 
PROFILE_TEXT = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")